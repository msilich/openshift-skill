[CmdletBinding()]
param(
    [string]$AdminKubeconfig = (Join-Path $env:USERPROFILE ".kube\config"),
    [string]$TargetKubeconfig = (Join-Path $env:USERPROFILE ".config\opencode\openshift-mcp\read-all.kubeconfig"),
    [string]$Namespace = "openshift-mcp",
    [string]$ServiceAccount = "opencode-admin-readonly",
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

$adminPath = (Resolve-Path -LiteralPath $AdminKubeconfig).Path
$targetPath = (Resolve-Path -LiteralPath $TargetKubeconfig).Path
$targetConfig = Invoke-OcText @("--kubeconfig", $targetPath, "config", "view", "--raw", "-o", "json") | ConvertFrom-Json
if (@($targetConfig.contexts).Count -ne 1 -or @($targetConfig.clusters).Count -ne 1 -or @($targetConfig.users).Count -ne 1) {
    throw "Target kubeconfig is not limited to one context, cluster and user"
}

$targetCluster = @($targetConfig.clusters)[0].cluster
$targetServer = $targetCluster.server
$targetInsecureProperty = $targetCluster.PSObject.Properties["insecure-skip-tls-verify"]
$targetInsecure = $null -ne $targetInsecureProperty -and [bool]$targetInsecureProperty.Value
if ([string]::IsNullOrWhiteSpace($targetCluster."certificate-authority-data") -or $targetInsecure) {
    throw "Target kubeconfig has no embedded CA or disables TLS verification"
}

$adminServer = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=8s", "whoami", "--show-server")
if ($adminServer -ne $targetServer) {
    throw "Admin and target kubeconfig point to different clusters: $adminServer != $targetServer"
}

$token = Invoke-OcText @("--kubeconfig", $adminPath, "--request-timeout=30s", "create", "token", $ServiceAccount, "--namespace", $Namespace, "--duration=$Duration")
if ([string]::IsNullOrWhiteSpace($token)) {
    throw "TokenRequest returned an empty token"
}

& oc config set-credentials $ServiceAccount "--token=$token" "--kubeconfig=$targetPath" | Out-Null
if ($LASTEXITCODE -ne 0) {
    throw "Could not update the target kubeconfig"
}
Protect-CredentialFile -Path $targetPath

$expectedIdentity = "system:serviceaccount:${Namespace}:${ServiceAccount}"
$actualIdentity = Invoke-OcText @("--kubeconfig", $targetPath, "--request-timeout=8s", "whoami")
$actualServer = Invoke-OcText @("--kubeconfig", $targetPath, "--request-timeout=8s", "whoami", "--show-server")
if ($actualIdentity -ne $expectedIdentity -or $actualServer -ne $targetServer) {
    throw "Updated token has an unexpected identity or API server"
}

[pscustomobject]@{
    TargetKubeconfig = $targetPath
    ApiServer = $actualServer
    ServiceAccountIdentity = $actualIdentity
    EmbeddedCARetained = $true
    RequestedDuration = $Duration
}
