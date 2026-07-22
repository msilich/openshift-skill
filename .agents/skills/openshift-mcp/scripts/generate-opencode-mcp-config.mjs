#!/usr/bin/env node

import {
  chmodSync,
  copyFileSync,
  existsSync,
  mkdirSync,
  readFileSync,
  renameSync,
  statSync,
  unlinkSync,
  writeFileSync
} from 'node:fs';
import { basename, dirname, resolve } from 'node:path';
import { homedir } from 'node:os';

const DEFAULT_OPENSHIFT_COMMAND = [
  '{env:OPENSHIFT_MCP_BINARY}',
  '--config',
  '{env:OPENSHIFT_MCP_READ_CONFIG}',
  '--kubeconfig',
  '{env:OPENSHIFT_MCP_READ_KUBECONFIG}',
  '--cluster-provider',
  'disabled'
];

const DEFAULT_ARGOCD_COMMAND = [
  '{env:ARGOCD_MCP_NODE}',
  '{env:ARGOCD_MCP_ENTRYPOINT}',
  'stdio'
];

const usage = `Usage:
  node generate-opencode-mcp-config.mjs --profile PROFILE [options] [--apply]

Required:
  --profile PROFILE              openshift, argocd, or both

Options:
  --config PATH                  OpenCode JSON config (default: XDG_CONFIG_HOME/opencode/opencode.json)
  --openshift-command-json JSON  Exact OpenShift MCP command array
  --argocd-command-json JSON     Exact Argo CD MCP command array
  --openshift-name NAME          MCP name (default: ocp_read)
  --argocd-name NAME             MCP name (default: argocd_read)
  --permission MODE              allow or ask (default: allow)
  --include-argocd-ca            Add NODE_EXTRA_CA_CERTS from the same-named environment variable
  --replace                      Replace a conflicting target-name entry after preview
  --apply                        Atomically write the reviewed configuration
  -h, --help                     Show this help

Without --apply, the script validates and previews only the MCP entries it would
merge. It never installs a package and has no token option. Do not put secrets
in command arrays. For an npx command, include --no-install or --offline in the
JSON array so it cannot fetch from a registry at OpenCode startup.

Examples:
  node generate-opencode-mcp-config.mjs --profile both

  node generate-opencode-mcp-config.mjs --profile argocd \\
    --argocd-command-json '["npx","--no-install","<argocd-mcp-command>","stdio"]' \\
    --include-argocd-ca --apply
`;

function fail(message) {
  throw new Error(message);
}

function defaultConfigPath() {
  const base = process.env.XDG_CONFIG_HOME || resolve(homedir(), '.config');
  return resolve(base, 'opencode', 'opencode.json');
}

function parseArgs(argv) {
  const values = new Map();
  const flags = new Set();
  const valueOptions = new Set([
    '--profile',
    '--config',
    '--openshift-command-json',
    '--argocd-command-json',
    '--openshift-name',
    '--argocd-name',
    '--permission'
  ]);
  const flagOptions = new Set(['--include-argocd-ca', '--replace', '--apply', '-h', '--help']);

  for (let index = 0; index < argv.length; index += 1) {
    const item = argv[index];
    if (flagOptions.has(item)) {
      flags.add(item);
      continue;
    }
    if (!valueOptions.has(item)) fail(`Unknown option: ${item}`);
    if (values.has(item)) fail(`Option supplied more than once: ${item}`);
    const value = argv[index + 1];
    if (value === undefined || value.startsWith('--')) fail(`Missing value for ${item}`);
    values.set(item, value);
    index += 1;
  }
  return { values, flags };
}

function parseCommand(raw, optionName, fallback) {
  if (raw === undefined) return [...fallback];
  let command;
  try {
    command = JSON.parse(raw);
  } catch (error) {
    fail(`${optionName} must be a valid JSON array: ${error.message}`);
  }
  if (!Array.isArray(command) || command.length === 0) {
    fail(`${optionName} must be a non-empty JSON array`);
  }
  if (command.some((item) => typeof item !== 'string' || item.length === 0)) {
    fail(`${optionName} entries must be non-empty strings`);
  }

  const forbidden = /(^|[-_])(token|password|passwd|api[-_]?key|authorization)(=|:|$)/i;
  if (command.some((item) => forbidden.test(item))) {
    fail(`${optionName} must not contain token, password, API-key, or authorization arguments`);
  }

  const executable = basename(command[0]).toLowerCase();
  if ((executable === 'npx' || executable === 'npx.cmd') &&
      !command.includes('--no-install') && !command.includes('--offline')) {
    fail(`${optionName} uses npx without --no-install or --offline`);
  }
  return command;
}

function parseConfig(path) {
  if (!existsSync(path)) return {};
  const text = readFileSync(path, 'utf8');
  try {
    const config = JSON.parse(text);
    if (!config || Array.isArray(config) || typeof config !== 'object') {
      fail('OpenCode configuration root must be a JSON object');
    }
    return config;
  } catch (error) {
    fail(`OpenCode configuration must be plain JSON; comments are not rewritten safely: ${error.message}`);
  }
}

function objectProperty(config, name) {
  if (config[name] === undefined) config[name] = {};
  if (!config[name] || Array.isArray(config[name]) || typeof config[name] !== 'object') {
    fail(`OpenCode configuration property ${name} must be an object`);
  }
  return config[name];
}

function stable(value) {
  if (Array.isArray(value)) return `[${value.map(stable).join(',')}]`;
  if (value && typeof value === 'object') {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${stable(value[key])}`).join(',')}}`;
  }
  return JSON.stringify(value);
}

function sameEntry(left, right) {
  return stable(left) === stable(right);
}

function commandKey(entry) {
  if (!entry || !Array.isArray(entry.command)) return null;
  return JSON.stringify(entry.command);
}

function mergeEntry(mcp, name, entry, replace, actions) {
  const desiredCommand = commandKey(entry);
  for (const [existingName, existingEntry] of Object.entries(mcp)) {
    if (existingName !== name && commandKey(existingEntry) === desiredCommand) {
      fail(`Equivalent MCP command already exists as ${existingName}; refusing duplicate ${name}`);
    }
  }

  if (mcp[name] === undefined) {
    mcp[name] = entry;
    actions.push({ name, action: 'add' });
    return;
  }
  if (sameEntry(mcp[name], entry)) {
    actions.push({ name, action: 'unchanged' });
    return;
  }
  if (!replace) {
    fail(`MCP entry ${name} already exists with different settings; preview with --replace before applying`);
  }
  mcp[name] = entry;
  actions.push({ name, action: 'replace' });
}

function validateName(value, optionName) {
  if (!/^[A-Za-z0-9][A-Za-z0-9_-]*$/.test(value)) {
    fail(`${optionName} must contain only letters, digits, underscores, and hyphens`);
  }
  return value;
}

function backupPath(path) {
  const timestamp = new Date().toISOString().replace(/[:.]/g, '-');
  return `${path}.backup-${timestamp}`;
}

function writeAtomic(path, config) {
  mkdirSync(dirname(path), { recursive: true });
  const temporary = `${path}.tmp-${process.pid}`;
  const existed = existsSync(path);
  const mode = existed ? statSync(path).mode & 0o777 : 0o600;
  let backup = null;
  try {
    if (existed) {
      backup = backupPath(path);
      copyFileSync(path, backup, 0);
      chmodSync(backup, mode);
    }
    writeFileSync(temporary, `${JSON.stringify(config, null, 2)}\n`, {
      encoding: 'utf8',
      flag: 'wx',
      mode
    });
    renameSync(temporary, path);
  } catch (error) {
    if (existsSync(temporary)) unlinkSync(temporary);
    fail(`Could not write OpenCode configuration: ${error.message}`);
  }
  return backup;
}

function main() {
  const { values, flags } = parseArgs(process.argv.slice(2));
  if (flags.has('-h') || flags.has('--help')) {
    process.stdout.write(usage);
    return;
  }

  const profile = values.get('--profile');
  if (!['openshift', 'argocd', 'both'].includes(profile)) {
    fail('--profile must be openshift, argocd, or both');
  }
  const configPath = resolve(values.get('--config') || defaultConfigPath());
  const permissionMode = values.get('--permission') || 'allow';
  if (!['allow', 'ask'].includes(permissionMode)) fail('--permission must be allow or ask');
  const openshiftName = validateName(values.get('--openshift-name') || 'ocp_read', '--openshift-name');
  const argocdName = validateName(values.get('--argocd-name') || 'argocd_read', '--argocd-name');
  if (profile === 'both' && openshiftName === argocdName) fail('OpenShift and Argo CD MCP names must differ');

  const openshiftCommand = parseCommand(
    values.get('--openshift-command-json'),
    '--openshift-command-json',
    DEFAULT_OPENSHIFT_COMMAND
  );
  const argocdCommand = parseCommand(
    values.get('--argocd-command-json'),
    '--argocd-command-json',
    DEFAULT_ARGOCD_COMMAND
  );

  const config = parseConfig(configPath);
  const originalConfig = stable(config);
  const mcp = objectProperty(config, 'mcp');
  const permission = objectProperty(config, 'permission');
  const actions = [];
  const selected = [];

  if (profile === 'openshift' || profile === 'both') {
    const entry = { type: 'local', command: openshiftCommand, enabled: true };
    mergeEntry(mcp, openshiftName, entry, flags.has('--replace'), actions);
    permission[`${openshiftName}_*`] = permissionMode;
    selected.push({ name: openshiftName, entry, permission: permissionMode });
  }

  if (profile === 'argocd' || profile === 'both') {
    const environment = {
      ARGOCD_BASE_URL: '{env:ARGOCD_BASE_URL}',
      ARGOCD_TOKEN_REGISTRY_PATH: '{env:ARGOCD_TOKEN_REGISTRY_PATH}',
      MCP_READ_ONLY: 'true'
    };
    if (flags.has('--include-argocd-ca')) {
      environment.NODE_EXTRA_CA_CERTS = '{env:NODE_EXTRA_CA_CERTS}';
    }
    const entry = {
      type: 'local',
      command: argocdCommand,
      enabled: true,
      timeout: 10_000,
      environment
    };
    mergeEntry(mcp, argocdName, entry, flags.has('--replace'), actions);
    permission[`${argocdName}_*`] = permissionMode;
    selected.push({ name: argocdName, entry, permission: permissionMode });
  }

  const changed = stable(config) !== originalConfig;
  console.log(`Mode: ${flags.has('--apply') ? 'apply' : 'preview'}`);
  console.log(`Config: ${configPath}`);
  for (const action of actions) console.log(`MCP ${action.name}: ${action.action}`);
  console.log('Proposed entries (credential values are environment references only):');
  console.log(JSON.stringify(selected, null, 2));

  if (!flags.has('--apply')) {
    console.log('Persistent changes: none (rerun the reviewed command with --apply)');
    return;
  }
  if (!changed) {
    console.log('Persistent changes: none (configuration already matches)');
    return;
  }
  const backup = writeAtomic(configPath, config);
  console.log(`OpenCode config: ${configPath} (updated)`);
  if (backup) console.log(`Backup: ${backup}`);
  console.log('Restart OpenCode and run: opencode mcp list');
}

try {
  main();
} catch (error) {
  console.error(`ERROR: ${error.message}`);
  process.exitCode = 1;
}
