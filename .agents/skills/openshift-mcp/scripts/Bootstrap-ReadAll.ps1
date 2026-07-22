[CmdletBinding()]
param(
    [Parameter(Mandatory = $true, Position = 0)]
    [ValidateSet("Preview", "ApplyRbac", "CreateKubeconfig")]
    [string]$Command,

    [Parameter(Mandatory = $true)]
    [string]$AdminKubeconfig,

    [Parameter(Mandatory = $true)]
    [string]$ExpectedServer,

    [Parameter(Mandatory = $true)]
    [string]$ExpectedAdminIdentity,

    [Parameter(Mandatory = $true)]
    [string]$OutputKubeconfig,

    [string]$ClusterCAPath,
    [string]$Duration = "24h"
)

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

function Assert-AbsolutePath {
    param(
        [string]$Label,
        [string]$Path
    )

    if (-not [IO.Path]::IsPathRooted($Path)) {
        throw "${Label} must be an absolute path: $Path"
    }
}

function Invoke-OcText {
    param(
        [string[]]$Arguments,
        [int[]]$AllowedExitCodes = @(0)
    )

    $result = (& oc @Arguments 2>&1 | Out-String).Trim()
    $exitCode = $LASTEXITCODE
    if ($AllowedExitCodes -notcontains $exitCode) {
        if ([string]::IsNullOrWhiteSpace($result)) {
            throw "oc failed with exit code $exitCode"
        }
        throw $result
    }
    return $result
}

function Invoke-AdminOcText {
    param(
        [string[]]$Arguments,
        [int[]]$AllowedExitCodes = @(0)
    )

    $combined = @("--kubeconfig", $script:AdminPath) + $Arguments
    return Invoke-OcText -Arguments $combined -AllowedExitCodes $AllowedExitCodes
}

function Test-ReadAllWriteNone {
    $readIdentity = "system:serviceaccount:openshift-mcp:opencode-admin-readonly"
    $null = Invoke-AdminOcText @(
        "--request-timeout=8s", "get", "serviceaccount", "opencode-admin-readonly",
        "--namespace", "openshift-mcp", "-o", "name"
    )

    $canGetNamespaces = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "get", "namespaces", "--as=$readIdentity"
    )
    $canListPods = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "list", "pods", "--all-namespaces", "--as=$readIdentity"
    )
    $canGetSecrets = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "get", "secrets", "--all-namespaces", "--as=$readIdentity"
    )
    $canCreate = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "create", "deployments.apps", "--all-namespaces", "--as=$readIdentity"
    )
    $canPatch = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "patch", "deployments.apps", "--all-namespaces", "--as=$readIdentity"
    )
    $canDelete = Invoke-AdminOcText @(
        "--request-timeout=8s", "auth", "can-i", "delete", "pods", "--all-namespaces", "--as=$readIdentity"
    )

    if ($canGetNamespaces -ne "yes") { throw "Read check failed: cannot get namespaces" }
    if ($canListPods -ne "yes") { throw "Read check failed: cannot list Pods cluster-wide" }
    if ($canGetSecrets -ne "yes") { throw "Read check failed: cannot get Secrets cluster-wide" }
    if ($canCreate -ne "no") { throw "Write check failed: can create Deployments" }
    if ($canPatch -ne "no") { throw "Write check failed: can patch Deployments" }
    if ($canDelete -ne "no") { throw "Write check failed: can delete Pods" }

    return [pscustomobject]@{
        CanGetNamespaces = $canGetNamespaces
        CanListPodsClusterWide = $canListPods
        CanGetSecretsClusterWide = $canGetSecrets
        CanCreateDeployments = $canCreate
        CanPatchDeployments = $canPatch
        CanDeletePods = $canDelete
    }
}

function Invoke-RbacPreview {
    $diff = Invoke-AdminOcText -Arguments @("diff", "-f", $script:RbacDirectory) -AllowedExitCodes @(0, 1)
    if (-not [string]::IsNullOrWhiteSpace($diff)) {
        Write-Output $diff
    }
    $dryRun = Invoke-AdminOcText @(
        "apply", "--dry-run=server", "-o", "name", "-f", $script:RbacDirectory
    )
    if (-not [string]::IsNullOrWhiteSpace($dryRun)) {
        Write-Output $dryRun
    }
}

if (-not (Get-Command oc -ErrorAction SilentlyContinue)) {
    throw "oc was not found in PATH"
}

Assert-AbsolutePath -Label "Admin kubeconfig" -Path $AdminKubeconfig
Assert-AbsolutePath -Label "Output kubeconfig" -Path $OutputKubeconfig

$script:AdminPath = (Resolve-Path -LiteralPath $AdminKubeconfig).Path
$outputPath = [IO.Path]::GetFullPath($OutputKubeconfig)
if (Test-Path -LiteralPath $outputPath) {
    throw "Output already exists; refusing to overwrite: $outputPath"
}

$scriptDirectory = $PSScriptRoot
$skillDirectory = Split-Path -Parent $scriptDirectory
$script:RbacDirectory = Join-Path $skillDirectory "assets\read-all-rbac"
$createKubeconfigScript = Join-Path $scriptDirectory "New-ReadAllKubeconfig.ps1"
if (-not (Test-Path -LiteralPath $script:RbacDirectory -PathType Container)) {
    throw "Bundled RBAC directory is missing: $($script:RbacDirectory)"
}
if (-not (Test-Path -LiteralPath $createKubeconfigScript -PathType Leaf)) {
    throw "Kubeconfig creation script is missing: $createKubeconfigScript"
}

$actualContext = Invoke-AdminOcText @("config", "current-context")
$actualAdminIdentity = Invoke-AdminOcText @("--request-timeout=8s", "whoami")
$actualServer = Invoke-AdminOcText @("--request-timeout=8s", "whoami", "--show-server")
if ($actualAdminIdentity -ne $ExpectedAdminIdentity) {
    throw "Admin identity mismatch: $actualAdminIdentity != $ExpectedAdminIdentity"
}
if ($actualServer -ne $ExpectedServer) {
    throw "API server mismatch: $actualServer != $ExpectedServer"
}

$temporaryCAPath = $null
try {
    if ($PSBoundParameters.ContainsKey("ClusterCAPath")) {
        Assert-AbsolutePath -Label "Cluster CA" -Path $ClusterCAPath
        $caPath = (Resolve-Path -LiteralPath $ClusterCAPath).Path
        $caSource = $caPath
    }
    else {
        $adminInsecureTLS = Invoke-AdminOcText @(
            "config", "view", "--raw", "--minify", "--flatten", "-o",
            "jsonpath={.clusters[0].cluster.insecure-skip-tls-verify}"
        )
        if ($adminInsecureTLS -eq "true") {
            throw "Admin kubeconfig disables TLS verification; refusing to copy its trust settings"
        }

        $adminCAData = Invoke-AdminOcText @(
            "config", "view", "--raw", "--minify", "--flatten", "-o",
            "jsonpath={.clusters[0].cluster.certificate-authority-data}"
        )
        if ([string]::IsNullOrWhiteSpace($adminCAData)) {
            throw "Admin kubeconfig has no embedded CA; provide -ClusterCAPath explicitly"
        }

        $temporaryCAPath = Join-Path ([IO.Path]::GetTempPath()) (
            "openshift-mcp-ca-{0}.pem" -f [guid]::NewGuid().ToString("N")
        )
        [IO.File]::WriteAllBytes($temporaryCAPath, [Convert]::FromBase64String($adminCAData))
        $caPath = $temporaryCAPath
        $caSource = "embedded CA from admin kubeconfig"
    }

    $caText = Get-Content -Raw -LiteralPath $caPath
    if ($caText -notmatch "-----BEGIN CERTIFICATE-----") {
        throw "Selected CA is not a PEM certificate or PEM CA bundle"
    }

    $null = Invoke-AdminOcText @(
        "--server=$ExpectedServer", "--certificate-authority=$caPath",
        "--insecure-skip-tls-verify=false", "--request-timeout=8s",
        "get", "--raw", "/version"
    )

    $summary = [ordered]@{
        Command = $Command
        AdminContext = $actualContext
        AdminIdentity = $actualAdminIdentity
        ApiServer = $actualServer
        CustomerCAValidation = "success"
        CustomerCASource = $caSource
        RbacDirectory = $script:RbacDirectory
        OutputKubeconfig = $outputPath
    }

    switch ($Command) {
        "Preview" {
            Invoke-RbacPreview
            $summary.PersistentChanges = "none"
            $summary.NextCommand = "ApplyRbac after Gate 1 approval"
        }
        "ApplyRbac" {
            Invoke-RbacPreview
            $applyResult = Invoke-AdminOcText @("apply", "-f", $script:RbacDirectory)
            if (-not [string]::IsNullOrWhiteSpace($applyResult)) {
                Write-Output $applyResult
            }
            $permissions = Test-ReadAllWriteNone
            $summary.Permissions = $permissions
            $summary.CredentialCreated = $false
            $summary.NextCommand = "CreateKubeconfig after Gate 2 approval"
        }
        "CreateKubeconfig" {
            $permissions = Test-ReadAllWriteNone
            $creationResult = & $createKubeconfigScript `
                -AdminKubeconfig $script:AdminPath `
                -ClusterCAPath $caPath `
                -OutputKubeconfig $outputPath `
                -Duration $Duration
            $actualReadIdentity = Invoke-OcText @(
                "--kubeconfig", $outputPath, "--request-timeout=8s", "whoami"
            )
            $actualReadServer = Invoke-OcText @(
                "--kubeconfig", $outputPath, "--request-timeout=8s", "whoami", "--show-server"
            )
            $expectedReadIdentity = "system:serviceaccount:openshift-mcp:opencode-admin-readonly"
            if ($actualReadIdentity -ne $expectedReadIdentity) {
                throw "Generated kubeconfig has an unexpected identity: $actualReadIdentity"
            }
            if ($actualReadServer -ne $ExpectedServer) {
                throw "Generated kubeconfig has an unexpected API server: $actualReadServer"
            }
            $summary.Permissions = $permissions
            $summary.ServiceAccountIdentity = $actualReadIdentity
            $summary.BootstrapCompleted = $true
            $summary.TokenExpiresLocal = $creationResult.TokenExpiresLocal
        }
    }

    [pscustomobject]$summary
}
finally {
    if ($temporaryCAPath -and (Test-Path -LiteralPath $temporaryCAPath)) {
        Remove-Item -LiteralPath $temporaryCAPath -Force
    }
}
