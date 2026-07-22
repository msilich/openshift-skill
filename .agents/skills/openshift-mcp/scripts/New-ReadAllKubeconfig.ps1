[CmdletBinding()]
param(
    [Parameter(Mandatory = $true)]
    [string]$ClusterCAPath,

    [string]$AdminKubeconfig = (Join-Path $env:USERPROFILE ".kube\config"),
    [string]$OutputKubeconfig = (Join-Path $env:USERPROFILE ".config\opencode\openshift-mcp\read-all.kubeconfig"),
    [string]$Namespace = "openshift-mcp",
    [string]$ServiceAccount = "opencode-admin-readonly",
    [string]$ContextName = "opencode-admin-readonly",
    [string]$DefaultNamespace = "default",
    [string]$Duration = "24h"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Invoke-OcText {
    param([string[]]$Arguments)

    $result = (& oc @Arguments 2>&1 | Out-String).Trim()
    if ($LASTEXITCODE -ne 0) {
        throw $result
    }
    return $result
}

function Protect-CredentialFile {
    param([string]$Path)

    if ($env:OS -eq "Windows_NT") {
        $aclIdentity = (& "$env:SystemRoot\System32\whoami.exe").Trim()
        & icacls $Path /inheritance:r /grant:r "${aclIdentity}:(F)" "SYSTEM:(F)" | Out-Null
    }
    else {
        & chmod 600 $Path
    }
    if ($LASTEXITCODE -ne 0) {
        throw "Could not protect file permissions: $Path"
    }
}

function Get-JwtExpiry {
    param([string]$Token)

    $parts = $Token.Split(".")
    if ($parts.Count -lt 2) {
        return $null
    }
    $payload = $parts[1].Replace("-", "+").Replace("_", "/")
    switch ($payload.Length % 4) {
        2 { $payload += "==" }
        3 { $payload += "=" }
    }
    try {
        $claims = [Text.Encoding]::UTF8.GetString([Convert]::FromBase64String($payload)) | ConvertFrom-Json
        if ($claims.exp) {
            return [DateTimeOffset]::FromUnixTimeSeconds([long]$claims.exp).ToLocalTime()
        }
    }
    catch {
        return $null
    }
    return $null
}

if (-not (Get-Command oc -ErrorAction SilentlyContinue)) {
    throw "oc was not found in PATH"
}

$adminPath = (Resolve-Path -LiteralPath $AdminKubeconfig).Path
$caPath = (Resolve-Path -LiteralPath $ClusterCAPath).Path
$outputPath = [IO.Path]::GetFullPath($OutputKubeconfig)

if (Test-Path -LiteralPath $outputPath) {
    throw "Output already exists; use the token update script: $outputPath"
}

$caText = Get-Content -Raw -LiteralPath $caPath
if ($caText -notmatch "-----BEGIN CERTIFICATE-----") {
    throw "CA file is not a PEM certificate or PEM CA bundle: $caPath"
}

$adminConfig = Invoke-OcText @("--kubeconfig", $adminPath, "config", "view", "--raw", "--minify", "--flatten", "-o", "json") | ConvertFrom-Json
$adminContext = @($adminConfig.contexts)[0].context
$adminCluster = @($adminConfig.clusters | Where-Object { $_.name -eq $adminContext.cluster })[0].cluster
$apiServer = $adminCluster.server
if ([string]::IsNullOrWhiteSpace($apiServer)) {
    throw "No API server found in the admin kubeconfig"
}

$adminIdentity = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=8s", "whoami")
$adminServer = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=8s", "whoami", "--show-server")
if ($adminServer -ne $apiServer) {
    throw "Admin context and selected API server differ: $adminServer != $apiServer"
}

$null = Invoke-OcText @("--kubeconfig", $adminPath, "--server=$apiServer", "--certificate-authority=$caPath", "--insecure-skip-tls-verify=false", "--request-timeout=8s", "get", "--raw", "/version")
$null = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=8s", "get", "serviceaccount", $ServiceAccount, "--namespace", $Namespace, "-o", "name")
$token = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=30s", "create", "token", $ServiceAccount, "--namespace", $Namespace, "--duration=$Duration")
if ([string]::IsNullOrWhiteSpace($token)) {
    throw "TokenRequest returned an empty token"
}

$outputDirectory = Split-Path -Parent $outputPath
New-Item -ItemType Directory -Path $outputDirectory -Force | Out-Null

& oc config set-cluster openshift-mcp-cluster "--server=$apiServer" "--certificate-authority=$caPath" "--embed-certs=true" "--kubeconfig=$outputPath" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Could not write cluster configuration" }
& oc config set-credentials $ServiceAccount "--token=$token" "--kubeconfig=$outputPath" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Could not write the ServiceAccount token" }
Protect-CredentialFile -Path $outputPath
& oc config set-context $ContextName "--cluster=openshift-mcp-cluster" "--user=$ServiceAccount" "--namespace=$DefaultNamespace" "--kubeconfig=$outputPath" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Could not write context" }
& oc config use-context $ContextName "--kubeconfig=$outputPath" | Out-Null
if ($LASTEXITCODE -ne 0) { throw "Could not select context" }

$resultConfig = Invoke-OcText @("--kubeconfig", $outputPath, "config", "view", "--raw", "-o", "json") | ConvertFrom-Json
$resultCluster = @($resultConfig.clusters)[0].cluster
if (@($resultConfig.contexts).Count -ne 1 -or @($resultConfig.clusters).Count -ne 1 -or @($resultConfig.users).Count -ne 1) {
    throw "Generated kubeconfig is not limited to one context, cluster and user"
}
$resultInsecureProperty = $resultCluster.PSObject.Properties["insecure-skip-tls-verify"]
$resultInsecure = $null -ne $resultInsecureProperty -and [bool]$resultInsecureProperty.Value
if ([string]::IsNullOrWhiteSpace($resultCluster."certificate-authority-data") -or $resultInsecure) {
    throw "Customer CA was not embedded securely"
}

$expectedIdentity = "system:serviceaccount:${Namespace}:${ServiceAccount}"
$actualIdentity = Invoke-OcText @("--kubeconfig", $outputPath, "--request-timeout=8s", "whoami")
$actualServer = Invoke-OcText @("--kubeconfig", $outputPath, "--request-timeout=8s", "whoami", "--show-server")
if ($actualIdentity -ne $expectedIdentity -or $actualServer -ne $apiServer) {
    throw "Generated kubeconfig has an unexpected identity or API server"
}

$canReadSecrets = Invoke-OcText @("--kubeconfig", $outputPath, "--request-timeout=8s", "auth", "can-i", "get", "secrets", "--all-namespaces")
$canCreate = Invoke-OcText @("--kubeconfig", $outputPath, "--request-timeout=8s", "auth", "can-i", "create", "deployments.apps", "--all-namespaces")
$canDelete = Invoke-OcText @("--kubeconfig", $outputPath, "--request-timeout=8s", "auth", "can-i", "delete", "pods", "--all-namespaces")
if ($canReadSecrets -ne "yes" -or $canCreate -ne "no" -or $canDelete -ne "no") {
    throw "Effective RBAC does not match the expected read-all/write-none profile"
}

[pscustomobject]@{
    OutputKubeconfig = $outputPath
    ApiServer = $actualServer
    AdminIdentityUsedForTokenRequest = $adminIdentity
    ServiceAccountIdentity = $actualIdentity
    CustomerCAEmbedded = $true
    InsecureSkipTLSVerify = $false
    CanReadSecrets = $canReadSecrets
    CanCreateDeployments = $canCreate
    CanDeletePods = $canDelete
    TokenExpiresLocal = Get-JwtExpiry -Token $token
}
