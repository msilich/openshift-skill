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

$apiServer = Invoke-OcText @(
    "--kubeconfig", $adminPath, "config", "view", "--raw", "--minify", "--flatten",
    "-o", "jsonpath={.clusters[0].cluster.server}"
)
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
$workingPath = Join-Path $outputDirectory (".read-all.kubeconfig.{0}.tmp" -f [guid]::NewGuid().ToString("N"))
$resultObject = $null
try {
    $stream = [IO.File]::Open(
        $workingPath,
        [IO.FileMode]::CreateNew,
        [IO.FileAccess]::Write,
        [IO.FileShare]::None
    )
    $stream.Dispose()
    Protect-CredentialFile -Path $workingPath

    & oc config set-cluster openshift-mcp-cluster "--server=$apiServer" "--certificate-authority=$caPath" "--embed-certs=true" "--kubeconfig=$workingPath" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Could not write cluster configuration" }
    & oc config set-credentials $ServiceAccount "--token=$token" "--kubeconfig=$workingPath" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Could not write the ServiceAccount token" }
    & oc config set-context $ContextName "--cluster=openshift-mcp-cluster" "--user=$ServiceAccount" "--namespace=$DefaultNamespace" "--kubeconfig=$workingPath" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Could not write context" }
    & oc config use-context $ContextName "--kubeconfig=$workingPath" | Out-Null
    if ($LASTEXITCODE -ne 0) { throw "Could not select context" }

    $countText = Invoke-OcText @(
        "--kubeconfig", $workingPath, "config", "view", "--raw", "-o",
        "go-template={{len .contexts}} {{len .clusters}} {{len .users}}"
    )
    $counts = @($countText -split "\s+" | Where-Object { $_ })
    if ($counts.Count -ne 3 -or $counts[0] -ne "1" -or $counts[1] -ne "1" -or $counts[2] -ne "1") {
        throw "Generated kubeconfig is not limited to one context, cluster and user"
    }

    $resultCAData = Invoke-OcText @(
        "--kubeconfig", $workingPath, "config", "view", "--raw", "-o",
        "jsonpath={.clusters[0].cluster.certificate-authority-data}"
    )
    $resultInsecure = Invoke-OcText @(
        "--kubeconfig", $workingPath, "config", "view", "--raw", "-o",
        "jsonpath={.clusters[0].cluster.insecure-skip-tls-verify}"
    )
    $expectedCAData = [Convert]::ToBase64String([IO.File]::ReadAllBytes($caPath))
    if ([string]::IsNullOrWhiteSpace($resultCAData) -or $resultCAData -ne $expectedCAData -or $resultInsecure -eq "true") {
        throw "Customer CA was not embedded securely or differs from the selected CA"
    }

    $expectedIdentity = "system:serviceaccount:${Namespace}:${ServiceAccount}"
    $actualIdentity = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "whoami")
    $actualServer = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "whoami", "--show-server")
    if ($actualIdentity -ne $expectedIdentity -or $actualServer -ne $apiServer) {
        throw "Generated kubeconfig has an unexpected identity or API server"
    }

    $canReadSecrets = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "auth", "can-i", "get", "secrets", "--all-namespaces")
    $canCreate = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "auth", "can-i", "create", "deployments.apps", "--all-namespaces")
    $canPatch = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "auth", "can-i", "patch", "deployments.apps", "--all-namespaces")
    $canDelete = Invoke-OcText @("--kubeconfig", $workingPath, "--request-timeout=8s", "auth", "can-i", "delete", "pods", "--all-namespaces")
    if ($canReadSecrets -ne "yes" -or $canCreate -ne "no" -or $canPatch -ne "no" -or $canDelete -ne "no") {
        throw "Effective RBAC does not match the expected read-all/write-none profile"
    }

    [IO.File]::Move($workingPath, $outputPath)
    $workingPath = $null
    Protect-CredentialFile -Path $outputPath

    $resultObject = [pscustomobject]@{
        OutputKubeconfig = $outputPath
        ApiServer = $actualServer
        AdminIdentityUsedForTokenRequest = $adminIdentity
        ServiceAccountIdentity = $actualIdentity
        CustomerCAEmbedded = $true
        InsecureSkipTLSVerify = $false
        CanReadSecrets = $canReadSecrets
        CanCreateDeployments = $canCreate
        CanPatchDeployments = $canPatch
        CanDeletePods = $canDelete
        TokenExpiresLocal = Get-JwtExpiry -Token $token
    }
}
finally {
    $token = $null
    if ($workingPath -and (Test-Path -LiteralPath $workingPath)) {
        Remove-Item -LiteralPath $workingPath -Force
    }
}

$resultObject
