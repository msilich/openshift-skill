#!/usr/bin/env node

import { spawnSync } from 'node:child_process';
import fs from 'node:fs';
import https from 'node:https';
import path from 'node:path';
import process from 'node:process';
import { fileURLToPath } from 'node:url';

const scriptDirectory = path.dirname(fileURLToPath(import.meta.url));
const policyPath = path.resolve(
  scriptDirectory,
  '..',
  'assets',
  'argocd-readonly-rbac',
  'policy.csv'
);

const usage = `Usage:
  node configure-argocd-mcp-opencode.mjs [options] [--apply]

Required:
  --kubeconfig PATH       Explicit administrative kubeconfig
  --expected-server URL   Exact OpenShift API URL expected from whoami
  --expected-identity ID  Exact OpenShift identity expected from whoami
  --namespace NAME        Namespace containing the ArgoCD resource
  --argocd-name NAME      Name of the operator-managed ArgoCD resource
  --base-url URL          HTTPS URL of the Argo CD API
  --opencode-config PATH  Existing plain-JSON OpenCode configuration
  --mcp-entrypoint PATH   Installed argocd-mcp dist/index.js
  --registry PATH         Protected token-registry output path

Optional:
  --node PATH             Node.js executable used by OpenCode (default: current)
  --ca PATH               PEM CA or CA bundle for the Argo CD URL
  --token-lifetime VALUE  Operator-managed token lifetime (default: 168h)
  --account NAME          Dedicated Argo CD account (default: opencode-mcp)
  --apply                 Persist the validated ArgoCD CR and local config changes
  -h, --help              Show this help

Without --apply, the script performs target verification and a server dry-run.
The script accesses only <account>-local-user.data.apiToken and never prints it.
`;

function fail(message) {
  throw new Error(message);
}

function parseArguments(argv) {
  const values = new Map();
  const flags = new Set();
  for (let index = 0; index < argv.length; index += 1) {
    const item = argv[index];
    if (item === '--apply' || item === '-h' || item === '--help') {
      flags.add(item);
      continue;
    }
    if (!item.startsWith('--')) fail(`Unknown argument: ${item}`);
    const value = argv[index + 1];
    if (!value || value.startsWith('--')) fail(`Missing value for ${item}`);
    values.set(item.slice(2), value);
    index += 1;
  }
  return { values, flags };
}

function required(values, name) {
  const value = values.get(name);
  if (!value) fail(`--${name} is required`);
  return value;
}

function run(command, args, options = {}) {
  const result = spawnSync(command, args, {
    encoding: 'utf8',
    windowsHide: true,
    maxBuffer: 16 * 1024 * 1024,
    ...options.spawn
  });
  if (result.error) fail(`Could not run ${command}: ${result.error.message}`);
  const allowed = options.allowedExitCodes ?? [0];
  if (!allowed.includes(result.status)) {
    const detail = options.sensitive
      ? 'command failed; output suppressed because it may contain a credential'
      : (result.stderr || result.stdout || '').trim();
    fail(`${command} exited with ${result.status}: ${detail}`);
  }
  return (result.stdout || '').trim();
}

function sleep(milliseconds) {
  return new Promise((resolve) => setTimeout(resolve, milliseconds));
}

function requestStatus(url, { ca, token } = {}) {
  return new Promise((resolve, reject) => {
    const request = https.request(url, {
      method: 'GET',
      ca,
      rejectUnauthorized: true,
      headers: token ? { Authorization: `Bearer ${token}` } : undefined,
      timeout: 15_000
    }, (response) => {
      response.resume();
      response.on('end', () => resolve(response.statusCode ?? 0));
    });
    request.on('timeout', () => request.destroy(new Error('HTTPS request timed out')));
    request.on('error', reject);
    request.end();
  });
}

function writeProtectedJson(targetPath, value) {
  fs.mkdirSync(path.dirname(targetPath), { recursive: true, mode: 0o700 });
  const temporaryPath = `${targetPath}.new-${process.pid}`;
  fs.writeFileSync(temporaryPath, `${JSON.stringify(value, null, 2)}\n`, {
    encoding: 'utf8',
    flag: 'wx',
    mode: 0o600
  });
  try {
    if (fs.existsSync(targetPath)) fs.unlinkSync(targetPath);
    fs.renameSync(temporaryPath, targetPath);
    fs.chmodSync(targetPath, 0o600);
    if (process.platform === 'win32') {
      const currentUser = run('whoami', []);
      run('icacls', [
        targetPath,
        '/inheritance:r',
        '/grant:r',
        `${currentUser}:F`,
        'SYSTEM:F'
      ]);
    }
  } catch (error) {
    if (fs.existsSync(temporaryPath)) fs.unlinkSync(temporaryPath);
    throw error;
  }
}

function updateOpenCodeConfig(configPath, desiredServer) {
  const original = fs.readFileSync(configPath, 'utf8');
  let config;
  try {
    config = JSON.parse(original);
  } catch {
    fail(
      `OpenCode config is not plain JSON: ${configPath}. ` +
      'Use the documented profile merge for commented JSONC files.'
    );
  }
  config.mcp ??= {};
  config.permission ??= {};
  config.mcp.argocd_read = desiredServer;
  config.permission['argocd_read_*'] = 'allow';
  const rendered = `${JSON.stringify(config, null, 2)}\n`;
  JSON.parse(rendered);
  if (rendered === original) return false;

  const backupPath = `${configPath}.backup-before-argocd-mcp`;
  if (!fs.existsSync(backupPath)) fs.copyFileSync(configPath, backupPath, fs.constants.COPYFILE_EXCL);
  const temporaryPath = `${configPath}.new-${process.pid}`;
  fs.writeFileSync(temporaryPath, rendered, { encoding: 'utf8', flag: 'wx' });
  fs.renameSync(temporaryPath, configPath);
  return true;
}

async function main() {
  const { values, flags } = parseArguments(process.argv.slice(2));
  if (flags.has('-h') || flags.has('--help')) {
    process.stdout.write(usage);
    return;
  }

  const kubeconfig = path.resolve(required(values, 'kubeconfig'));
  const expectedServer = required(values, 'expected-server').replace(/\/$/, '');
  const expectedIdentity = required(values, 'expected-identity');
  const namespace = required(values, 'namespace');
  const argocdName = required(values, 'argocd-name');
  const baseUrl = required(values, 'base-url').replace(/\/$/, '');
  const opencodeConfig = path.resolve(required(values, 'opencode-config'));
  const mcpEntrypoint = path.resolve(required(values, 'mcp-entrypoint'));
  const registryPath = path.resolve(required(values, 'registry'));
  const nodePath = path.resolve(values.get('node') ?? process.execPath);
  const caPath = values.get('ca') ? path.resolve(values.get('ca')) : undefined;
  const tokenLifetime = values.get('token-lifetime') ?? '168h';
  const account = values.get('account') ?? 'opencode-mcp';
  const apply = flags.has('--apply');

  if (!/^https:\/\//i.test(baseUrl)) fail('--base-url must use HTTPS');
  if (!/^\d+h$/.test(tokenLifetime)) fail('--token-lifetime must use whole hours, for example 24h');
  if (!/^[a-z0-9]([-a-z0-9]*[a-z0-9])?$/.test(account)) fail('--account must be a DNS-compatible name');
  for (const file of [kubeconfig, opencodeConfig, mcpEntrypoint, nodePath, policyPath]) {
    if (!fs.existsSync(file)) fail(`Required file does not exist: ${file}`);
  }
  const ca = caPath ? fs.readFileSync(caPath) : undefined;

  // Parse the local config before any cluster mutation so a JSONC mismatch fails early.
  JSON.parse(fs.readFileSync(opencodeConfig, 'utf8'));

  const ocPrefix = ['--kubeconfig', kubeconfig];
  const context = run('oc', [...ocPrefix, 'config', 'current-context']);
  const identity = run('oc', [...ocPrefix, '--request-timeout=8s', 'whoami']);
  const server = run('oc', [...ocPrefix, '--request-timeout=8s', 'whoami', '--show-server']).replace(/\/$/, '');
  if (identity !== expectedIdentity) fail(`OpenShift identity mismatch: ${identity}`);
  if (server !== expectedServer) fail(`OpenShift API mismatch: ${server}`);

  const crd = JSON.parse(run('oc', [...ocPrefix, 'get', 'crd', 'argocds.argoproj.io', '-o', 'json']));
  const version = crd.spec.versions.find((item) => item.name === 'v1beta1' && item.served);
  const specProperties = version?.schema?.openAPIV3Schema?.properties?.spec?.properties;
  if (!specProperties?.localUsers || !specProperties?.rbac) {
    fail('Live argoproj.io/v1beta1 schema lacks spec.localUsers or spec.rbac');
  }

  const current = JSON.parse(run('oc', [
    ...ocPrefix,
    '-n', namespace,
    'get', 'argocd', argocdName,
    '-o', 'json'
  ]));
  if (current.apiVersion !== 'argoproj.io/v1beta1') {
    fail(`Unexpected ArgoCD apiVersion: ${current.apiVersion}`);
  }

  const policyLines = fs.readFileSync(policyPath, 'utf8')
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean);
  const invalidAllow = policyLines.find((line) => line.endsWith(', allow') && !line.includes(', get, '));
  if (invalidAllow) fail(`Policy contains a non-read allow rule: ${invalidAllow}`);

  const users = [...(current.spec.localUsers ?? [])];
  const desiredUser = {
    name: account,
    enabled: true,
    apiKey: true,
    login: false,
    tokenLifetime,
    autoRenewToken: true
  };
  const userIndex = users.findIndex((item) => item.name === account);
  if (userIndex >= 0) users[userIndex] = desiredUser;
  else users.push(desiredUser);

  const existingPolicyLines = (current.spec.rbac?.policy ?? '')
    .split(/\r?\n/)
    .map((line) => line.trim())
    .filter(Boolean)
    .filter((line) => {
      const fields = line.split(',').map((field) => field.trim());
      return !(fields[0] === 'p' && fields[1] === account);
    });
  const desiredPolicy = [...existingPolicyLines, ...policyLines].join('\n');
  const patch = [{ op: 'add', path: '/spec/localUsers', value: users }];
  if (current.spec.rbac) {
    patch.push({ op: 'add', path: '/spec/rbac/policy', value: desiredPolicy });
  } else {
    patch.push({ op: 'add', path: '/spec/rbac', value: { policy: desiredPolicy } });
  }
  const patchJson = JSON.stringify(patch);

  run('oc', [
    ...ocPrefix,
    '-n', namespace,
    'patch', 'argocd', argocdName,
    '--type=json',
    '--patch', patchJson,
    '--dry-run=server',
    '-o', 'name'
  ]);

  console.log(`Context: ${context}`);
  console.log(`Identity: ${identity}`);
  console.log(`API server: ${server}`);
  console.log(`Argo CD: ${namespace}/${argocdName}`);
  console.log(`Account: ${account} (API only, ${tokenLifetime}, auto-renew)`);
  console.log(`RBAC: ${policyLines.filter((line) => line.endsWith(', allow')).length} read allows, no write allows`);
  console.log('Server dry-run: passed');
  if (!apply) {
    console.log('Persistent changes: none (rerun with --apply)');
    return;
  }

  run('oc', [
    ...ocPrefix,
    '-n', namespace,
    'patch', 'argocd', argocdName,
    '--type=json',
    '--patch', patchJson
  ]);

  const secretName = `${account}-local-user`;
  let encodedToken = '';
  for (let attempt = 0; attempt < 60; attempt += 1) {
    encodedToken = run('oc', [
      ...ocPrefix,
      '-n', namespace,
      'get', 'secret', secretName,
      '-o', "jsonpath={.data.apiToken}"
    ], { allowedExitCodes: [0, 1], sensitive: true });
    if (encodedToken) break;
    await sleep(2_000);
  }
  if (!encodedToken) fail(`Operator did not create ${namespace}/${secretName} with data.apiToken`);
  const token = Buffer.from(encodedToken, 'base64').toString('utf8').trim();
  if (!token || /\s/.test(token)) fail('Operator token is empty or malformed');

  run('argocd', [
    'admin', 'settings', 'rbac', 'validate',
    '--kubeconfig', kubeconfig,
    '--namespace', namespace
  ]);
  const canRead = run('argocd', [
    'admin', 'settings', 'rbac', 'can', account,
    'get', 'applications', '*',
    '--kubeconfig', kubeconfig,
    '--namespace', namespace
  ]);
  const canSync = run('argocd', [
    'admin', 'settings', 'rbac', 'can', account,
    'sync', 'applications', '*',
    '--kubeconfig', kubeconfig,
    '--namespace', namespace
  ], { allowedExitCodes: [1] });
  const canDelete = run('argocd', [
    'admin', 'settings', 'rbac', 'can', account,
    'delete', 'applications', '*',
    '--kubeconfig', kubeconfig,
    '--namespace', namespace
  ], { allowedExitCodes: [1] });
  if (canRead !== 'Yes' || canSync !== 'No' || canDelete !== 'No') {
    fail(`Unexpected RBAC result: read=${canRead}, sync=${canSync}, delete=${canDelete}`);
  }

  await requestStatus(`${baseUrl}/`, { ca });
  const apiStatus = await requestStatus(`${baseUrl}/api/v1/applications`, { ca, token });
  if (apiStatus !== 200) fail(`Argo CD read API returned HTTP ${apiStatus}`);

  writeProtectedJson(registryPath, [{ baseUrl, token }]);
  const environment = {
    ARGOCD_BASE_URL: baseUrl,
    ARGOCD_TOKEN_REGISTRY_PATH: registryPath,
    MCP_READ_ONLY: 'true'
  };
  if (caPath) environment.NODE_EXTRA_CA_CERTS = caPath;
  const changed = updateOpenCodeConfig(opencodeConfig, {
    type: 'local',
    command: [nodePath, mcpEntrypoint, 'stdio'],
    enabled: true,
    timeout: 10_000,
    environment
  });

  console.log('Argo CD CR reconciliation: verified');
  console.log('RBAC: read=Yes, sync=No, delete=No');
  console.log('Argo CD API token test: HTTP 200');
  console.log(`Token registry: ${registryPath} (token not printed)`);
  console.log(`OpenCode config: ${opencodeConfig} (${changed ? 'updated' : 'unchanged'})`);
  console.log('Restart OpenCode after this command. Rerun the script to refresh a renewed token.');
}

main().catch((error) => {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
});
