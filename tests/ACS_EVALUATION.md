# ACS verification boundaries

## Documentation and static checks

RHACS 4.11 uses the complete 225-topic `openshift-acs` map at
`e516555e0cb6bcc6ba88c423e88c8dd054532425`, including all REST services and the
common object reference. The build produces 227 Markdown files and 9 source images.
The RHACS-only converter compares 836 code blocks and 1,960 tables through a
DocBook -> GFM -> rendered HTML -> AST round trip. It compares code values and
table cell text; layout and table captions can be represented differently.
The final bundled Markdown is parsed again after link rewriting; all 225 topics
must still match the pre-rewrite code-value and table-text hashes.
Credential-shaped Slack webhook examples from the source are replaced with
placeholders before the comparison and marked in the affected chapter and report.
GitHub push protection detected the original vendor example; no bypass was used
and the endpoint was not contacted. Source AsciiDoc -> DocBook is not an independent semantic validation of vendor
text. Explicit section anchors are retained and required images are local.

The local link check covers both Markdown and raw HTML links, local fragments and
image paths. `CONVERSION.json` inventories every topic, image hash, external URL,
conversion warning and unresolved reference. The pinned snapshot has 262 distinct
external references, 183 fragment adjustments and one missing upstream target:
`installing/acs-default-requirements.md` links to the absent legacy
`installing/installing-rhacs-on-red-hat-openshift` topic. Missing fragments fall
back to the local topic or a visible source-ID notice; no section content is
invented. External references are not included or downloaded at runtime.

Known source formatting issue: `modules/roxctl-sensor-generate-openshift-options.adoc`
contains unescaped `false|true|auto` option alternatives inside an AsciiDoc table.
The resulting cell split/literal backticks are retained in the CLI chapter, not
silently rewritten into an assumed CLI schema. Consult version-matched local
`roxctl --help` before execution. The RHACS-only converter also fixes a separate
Pandoc inline-code pipe-escaping issue to prevent further loss during GFM rendering.

The ACS Markdown manifest is pinned in `tools/docs/acs.lock.json`. Two builds
must match that manifest, CONVERSION.json and all images. Rebuilding OCP and
GitOps with the updated converter must preserve their existing Markdown hashes;
SOURCE.json then records the converter actually used. Dev Spaces is built by its
unchanged HTML importer and must retain every pinned content hash.

Build verification on September 9, 2026: two full ACS output directories were
byte-identical, including SOURCE.json, CONVERSION.json and all images. Markdown
manifest: `03a692e64d3e3c171e17f969ca685b0adb5f9f00b7548f6424435849d3033e6e`.
All ten skills passed the skill validator. Installer tests copy the complete
bundle into a temporary user home and compare every file; relocated-link tests
run from an unrelated directory. No real user configuration is used for installation.

Local suite result: 92 tests, no failures or errors, six reported skips (Windows
PowerShell cases and unavailable OpenCode/OpenShift-MCP runtime checks). ACS runtime
is not silently counted as passed: it remains untested as described below. On the
macOS development host the existing Linux bootstrap fixture uses GNU chmod only
inside its temporary fake-command directory; product scripts are unchanged. The
suite uses the pinned Python/PyYAML/BeautifulSoup/Pandoc documentation dependencies.

## Synthetic tests

`test_acs.py` checks exact MCP allowlists, stdio/static/TLS/read-only settings,
narrow CLI/HTTP permission patterns, relocated documentation and fixture coverage.
`fake_acs.py` provides test-only MCP, `oc`, `roxctl` and Central responses. It makes
no network calls and accepts only explicitly listed fixture operations.

The synthetic Central test reads a policy, prepares a local delta, denies an
unapproved preview, accepts a separately approved preview, rejects an unapproved
PUT, accepts one approved PUT and reads the changed policy back. Approval cannot
be reused, a read-only identity cannot write, and unknown fields fail. The timeout
case simulates an applied change followed by a 504; the next call is a GET, not
another PUT. This demonstrates the test protocol, not an OpenCode permission
implementation or proof that Qwen behaves that way.

The bilingual corpus includes missing tools, Forbidden, duplicate names/wrong
Central IDs, version/schema conflicts, stale feeds, absent sources, all four
Secret choices and controller ownership. Corpus assertions verify presence of
these cases; model reasoning for them remains a separate evaluation.

## Runtime evaluation remains separate

OpenCode 1.18.4, Qwen, the pinned OpenShift MCP and StackRox MCP runtime are not
available in the development environment. No binary is built to fill this gap;
no actual cluster or Central is contacted. Therefore automatic skill selection,
real `once` permission prompts, MCP tool execution and end-to-end model behavior
are **not verified** by this change. No customer installation is performed.

When an approved runtime is available, use an isolated temporary installation of
all ten skills and only fake transports. Adapt the base instructions in
[DOMAIN_EVALUATION.md](DOMAIN_EVALUATION.md) to `fake_acs.py --transport mcp` and the
ACS scenario corpus. Keep production MCP servers, credentials and inherited
permissions out of the test configuration. Route CLI calls only to fake executables
invoking `fake_acs.py --transport oc|roxctl`, never the real binaries. Do not grant
real curl access for synthetic model testing; the stateful Central sequence above
is exercised directly by unittest. Review full transcripts for target mapping,
schema source, Secret choice, explicit preview/once approval, denied-access behavior
and outcome verification. Record failures and skipped cases separately.
