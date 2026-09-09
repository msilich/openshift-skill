<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By configuring and integrating the Red Hat Advanced Cluster Security for Kubernetes (RHACS) plugin with Red Hat Developer Hub (RHDH), you can view the security information for your deployments in RHDH.

> [!IMPORTANT]
> Integration of vulnerability findings into the RHDH is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<a id="viewing-security-information-in-red-hat-developer-hub_configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub"></a>

# Viewing security information in Red Hat Developer Hub

By configuring and integrating the Red Hat Advanced Cluster Security for Kubernetes (RHACS) plugin with Red Hat Developer Hub (RHDH), you can access vulnerability data, assess risks, and take proactive security actions without leaving the RHDH environment.

Review the upstream plugin progress and details by visiting [Community plugins for Backstage](https://github.com/backstage/community-plugins).

<div>

<div class="title">

Prerequisites

</div>

- You have enabled the RHACS plugin installation in RHDH.

  For more information, see [Installing dynamic plugins using the Helm chart](https://docs.redhat.com/en/documentation/red_hat_developer_hub/1.4/html/installing_and_viewing_plugins_in_red_hat_developer_hub/rhdh-installing-rhdh-plugins_title-plugins-rhdh-about#con-install-dynamic-plugin-helm_rhdh-installing-rhdh-plugins) (RHDH documentation).

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the `app-config.yaml` file, add the `proxy` and `acs` stanzas by using the following content:

    ``` yaml
    # ...
    proxy:
      endpoints:
        /acs:
          target: ${ACS_API_URL}
          headers:
            authorization: Bearer ${ACS_API_KEY}
    acs:
      acsUrl: ${ACS_API_URL}
    # ...
    ```

2.  To enable the RHACS plugin, perform the following steps:

    1.  Navigate to the dynamic plugins configuration file in your RHDH setup.

    2.  To include the RHACS plugin, add the following content to the configuration file, for example:

        ``` yaml
        # ...
        - package: "oci://ghcr.io/redhat-developer/rhdh-plugin-export-overlays/backstage-community-plugin-acs:pr_986__0.0.4!backstage-community-plugin-acs"
            disabled: false
          pluginConfig:
            dynamicPlugins:
              frontend:
                backstage-community.plugin-acs:
                  entityTabs:
                    - path: /acs
                      title: Security
                      mountPoint: entity.page.acs
                  mountPoints:
                    - mountPoint: entity.page.acs/cards
                      importName: EntityACSContent
                      config:
                        layout:
                          gridColumnEnd:
                            lg: span 12
                            md: span 12
                            xs: span 12
        # ...
        ```

3.  To add annotations for entities in the RHDH catalog, perform the following steps:

    > [!NOTE]
    > To display the vulnerability data, each component entity in the RHDH catalog must reference the RHACS deployments.
    >
    > The following values are associated with the entities in the RHDH catalog:
    >
    > - `API`
    >
    > - `Component`
    >
    > - `Domain`
    >
    > - `Group`
    >
    > - `Location`
    >
    > - `Resource`
    >
    > - `System`
    >
    > - `Template`
    >
    > - `User`

    1.  Navigate to the entity configuration file for your service in your RHDH setup.

    2.  Add the following annotation to the configuration file, for example:

        ``` yaml
        apiVersion: backstage.io/v1alpha1
        kind: Component
        metadata:
          name: test-service
          annotations:
            acs/deployment-name: test-deployment-1,test-deployment-2,test-deployment-3
        # ...
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  In the RHDH portal, click **Catalog**.

2.  Click an entity and verify that the **RHACS** tab appears.

3.  To view the violations and vulnerability data, click the **RHACS** tab.

</div>

After you configure and integrate the RHACS plugin with RHDH, you need to rebuild the Open Container Initiative (OCI) artifact. See "Rebuilding the OCI artifact" for instructions.

<div>

<div class="title">

Additional resources

</div>

- [Rebuilding the OCI artifact](configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub.md#rebuilding-the-oci-artifact_configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub)

</div>

<a id="rebuilding-the-oci-artifact_configuring-and-integrating-the-rhacs-plugin-with-red-hat-developer-hub"></a>

# Rebuilding the OCI artifact

To rebuild the Open Container Initiative (OCI) artifact, update the `repo-ref` field in the `source.json` file to reference the new commit ID of the plugin repository.

<div>

<div class="title">

Procedure

</div>

- To rebuild the OCI artifact, update the `repo-ref` field in the `source.json` file, for example:

  > [!IMPORTANT]
  > You can find the `source.json` file in the `workspaces/acs` directory of the `rhdh-plugin-export-overlays` repository.

  ``` json
  {"repo":"https://github.com/backstage/community-plugins","repo-ref":"19ddb7837c6823a253c87af9524f8aef26a90b35","repo-flat":false}
  ```

</div>
