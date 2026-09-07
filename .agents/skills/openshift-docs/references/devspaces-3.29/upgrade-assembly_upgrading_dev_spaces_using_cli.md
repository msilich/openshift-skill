> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/upgrade-assembly_upgrading_dev_spaces_using_cli). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Upgrade from the command line

Upgrade OpenShift Dev Spaces to the latest version using the `dsc` CLI management tool so that you can automate upgrades or upgrade deployments in restricted environments.

<span id="assembly_upgrading-dev-spaces-using-cli_devspaces___how_the_cli_upgrade_works"></span>

## [How the CLI upgrade works](upgrade-assembly_upgrading_dev_spaces_using_cli.md#assembly_upgrading-dev-spaces-using-cli_devspaces___how_the_cli_upgrade_works)

The `dsc server:update` command performs the following operations in the `openshift-devspaces` namespace:

1.  Deploys the Operator image that matches the installed `dsc` version.
2.  Updates the CheCluster custom resource with the target version configuration.
3.  The Operator reconciles the updated resource and rolls out new container images for the gateway, dashboard, Dev Spaces server, and plug-in registry.

The upgrade preserves your existing CheCluster configuration, including custom properties, networking settings, and storage policies. Stop all running workspaces before starting the upgrade.

- **[Upgrade by using the dsc management tool](upgrade-proc_upgrading_using_cli.md)**  
  Upgrade OpenShift Dev Spaces from the previous minor version by using the `dsc` management tool so that your deployment receives the latest bug fixes, security patches, and features.
- **[Upgrade in an air-gapped environment](upgrade-proc_upgrading_dev_spaces_in_a_restricted_environment.md)**  
  Upgrade OpenShift Dev Spaces on a cluster with no internet access by mirroring updated container images and Operator catalogs to your private registry before running the upgrade.
