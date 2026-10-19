"""Bounded network retries; no live requests or real sleeps."""
from http.client import IncompleteRead
import importlib.util
from pathlib import Path
import ssl
import tempfile
import unittest
from unittest.mock import MagicMock, call, patch
from urllib.error import HTTPError, URLError

ROOT = Path(__file__).resolve().parents[1]


@unittest.skipUnless(importlib.util.find_spec("bs4"), "requires importer dependency")
class DocumentationDownloadTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        spec = importlib.util.spec_from_file_location("download_importer", ROOT / "tools/docs/import_devspaces.py")
        cls.module = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(cls.module)

    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.cache = Path(self.temp.name)
        self.url = "https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-con_installation_overview"
        self.response = MagicMock()
        self.response.__enter__.return_value = self.response
        self.response.url = self.url
        self.response.headers = {"Content-Type": "text/html"}
        self.response.read.return_value = b"complete documentation"
        opening = patch.object(self.module, "urlopen", return_value=self.response)
        self.open = opening.start()
        self.addCleanup(opening.stop)
        sleeping = patch.object(self.module.time, "sleep")
        self.sleep = sleeping.start()
        self.addCleanup(sleeping.stop)

    def test_timeouts_retry_then_cache_only_the_complete_response(self):
        self.open.side_effect = [TimeoutError("timeout"), URLError(TimeoutError("timeout")), self.response]
        data, metadata = self.module.download(self.url, self.cache)
        self.assertEqual(data, b"complete documentation")
        self.assertEqual(metadata["response_sha256"], self.module.digest(data))
        self.assertEqual(self.open.call_count, 3)
        self.assertEqual(self.sleep.call_args_list, [call(2), call(4)])
        self.open.side_effect = AssertionError("must use validated cache")
        self.assertEqual(self.module.download(self.url, self.cache), (data, metadata))

    def test_retries_stop_after_four_attempts_without_cache_files(self):
        self.open.side_effect = TimeoutError("read timed out")
        with self.assertRaisesRegex(RuntimeError, "failed after 4 attempts") as raised:
            self.module.download(self.url, self.cache)
        self.assertIn(self.url, str(raised.exception))
        self.assertEqual(self.open.call_count, 4)
        self.assertEqual(self.sleep.call_args_list, [call(2), call(4), call(8)])
        self.assertEqual(list(self.cache.iterdir()), [])

    def test_failed_body_read_and_broken_connection_are_retried(self):
        self.response.read.side_effect = [IncompleteRead(b"partial", 100), b"complete documentation"]
        self.open.side_effect = [ConnectionResetError("reset"), self.response, self.response]
        self.assertEqual(self.module.download(self.url, self.cache)[0], b"complete documentation")
        self.assertEqual(self.open.call_count, 3)
        self.assertEqual(self.sleep.call_args_list, [call(2), call(4)])

    def test_transient_http_errors_are_retried(self):
        for code in (408, 429, 500, 502, 503, 504):
            with self.subTest(code=code):
                self.open.reset_mock()
                self.sleep.reset_mock()
                self.open.side_effect = [HTTPError(self.url, code, "temporary", {}, None), self.response]
                cache = self.cache / str(code)
                cache.mkdir()
                self.module.download(self.url, cache)
                self.assertEqual(self.open.call_count, 2)
                self.sleep.assert_called_once_with(2)

    def test_permanent_http_and_certificate_errors_are_not_retried(self):
        errors = [HTTPError(self.url, code, "permanent", {}, None) for code in (400, 401, 403, 404)]
        errors.append(URLError(ssl.SSLCertVerificationError("certificate verify failed")))
        for error in errors:
            with self.subTest(error=error):
                self.open.reset_mock()
                self.open.side_effect = error
                with self.assertRaises(type(error)):
                    self.module.download(self.url, self.cache)
                self.open.assert_called_once()
                self.sleep.assert_not_called()
                self.assertEqual(list(self.cache.iterdir()), [])

    def test_redirect_and_size_checks_remain_permanent_failures(self):
        self.response.url = "https://unapproved.example.invalid/document"
        with self.assertRaisesRegex(ValueError, "Cross-host redirect"):
            self.module.download(self.url, self.cache)
        self.open.assert_called_once()
        self.sleep.assert_not_called()
        self.open.reset_mock()
        self.response.url = self.url
        self.response.read.return_value = b"x" * (20 * 1024 * 1024 + 1)
        with self.assertRaisesRegex(ValueError, "20 MiB"):
            self.module.download(self.url, self.cache)
        self.open.assert_called_once()
        self.sleep.assert_not_called()
        self.assertEqual(list(self.cache.iterdir()), [])

    def test_corrupt_cache_is_not_silently_redownloaded(self):
        self.module.download(self.url, self.cache)
        next(self.cache.glob("*.body")).write_bytes(b"corrupt")
        self.open.reset_mock()
        with self.assertRaisesRegex(ValueError, "Corrupt preparation cache"):
            self.module.download(self.url, self.cache)
        self.open.assert_not_called()
        self.sleep.assert_not_called()


if __name__ == "__main__":
    unittest.main()
