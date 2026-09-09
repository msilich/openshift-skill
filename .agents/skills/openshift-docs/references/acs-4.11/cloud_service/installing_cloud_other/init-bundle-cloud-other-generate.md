<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before you set up a secured cluster, you must generate a cluster registration secret (CRS) or an init bundle. The secured cluster then uses the contained secrets for initial authentication with the Central instance, also called Central. To set up the secured connection between Central and your secured clusters, you can use either a CRS or an init bundle, but using a CRS is the preferred method.

<a id="generate-crs-init-bundle-methods-overview_init-bundle-cloud-other-generate"></a>

# Methods for generating a CRS or init bundle

You can generate a cluster registration secret (CRS) or init bundle by using the RHACS portal or the `roxctl` CLI.

You can generate a CRS or an init bundle by using either of the following methods:

- In the RHACS portal, go to **Platform Configuration** → **Clusters** and select **Cluster Registration Secrets** (preferred) or **Init bundles**.

- Use the `roxctl` CLI to generate a CRS or an init bundle by using the following commands:

  - `roxctl central crs generate`

  - `roxctl central init-bundles generate`

After you generate a CRS or an init bundle, you provide the CRS or the init bundle when you run the `helm install` command.

<a id="generate-init-bundle-cloud-kube_init-bundle-cloud-other-generate"></a>

# Generating a CRS or an init bundle

You can generate a cluster registration secret or init bundle by using the RHACS portal or the `roxctl` CLI.

<a id="portal-generate-init-bundle_init-bundle-cloud-other-generate"></a>

## Generating a cluster registration secret or init bundle by using the RHACS portal

You can generate a cluster registration secret (CRS) or an init bundle that contains secrets by using the RHACS portal, also called the ACS Console.

> [!NOTE]
> You must have the `Admin` user role to generate a CRS or an init bundle.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the RHACS portal. If you do not have secured clusters, or an existing CRS or an init bundle, the **Platform Configuration** → **Clusters** page is displayed.

2.  Click **Create cluster registration secret** or **Init bundles installation method**.

    > [!NOTE]
    > Init bundles are still supported, but using a CRS to secure clusters is the preferred method.

    Complete only one of the following actions:

    - If you chose to generate a CRS, enter a name for the CRS and click **Download** to generate and download it. This action creates the CRS as a YAML file and you can use it to secure all of your clusters if you are using the same installation method.

      > [!IMPORTANT]
      > Store this file securely because it contains secrets.

    - If you chose to generate an init bundle, complete these steps:

      1.  Enter a name for the cluster init bundle.

      2.  Select your platform.

      3.  Select the installation method you will use for your secured clusters: Operator or Helm chart.

      4.  Click **Download** to generate and download the init bundle as a YAML file. You can use one init bundle and its corresponding YAML file for all secured clusters if you are using the same installation method.

          > [!IMPORTANT]
          > Store this file securely because it contains secrets.

</div>

<div>

<div class="title">

Next steps

</div>

1.  Apply the CRS or the init bundle to the secured cluster.

2.  Install secured cluster services on each cluster.

</div>

<a id="crs-generate-roxctl_init-bundle-cloud-other-generate"></a>

## Generating a CRS by using the roxctl CLI

You can generate a cluster registration secret by using the `roxctl` CLI.

> [!NOTE]
> You must have the `Admin` user role to generate a CRS.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables:

  1.  Set the `ROX_API_TOKEN` by running the following command:

      ``` terminal
      $ export ROX_API_TOKEN=<api_token>
      ```

  2.  Set the `ROX_CENTRAL_ADDRESS` environment variable by running the following command:

      ``` terminal
      $ export ROX_CENTRAL_ADDRESS=<address>:<port_number>
      ```

      > [!IMPORTANT]
      > In RHACS Cloud Service, when using `roxctl` commands that require the Central address, use the **Central instance address** as displayed in the **Instance Details** section of the Red Hat Hybrid Cloud Console. For example, use `acs-ABCD12345.acs.rhcloud.com` instead of `acs-data-ABCD12345.acs.rhcloud.com`.

</div>

<div>

<div class="title">

Procedure

</div>

- To generate a CRS, run the following command:

  ``` terminal
  $ roxctl -e "$ROX_CENTRAL_ADDRESS" \
    central crs generate <crs_name> \
    --output <file_name>
  ```

  where:

  `<crs_name>`  
  Specifies an identifier or name for the CRS.

  `<file_name>`  
  Specifies a file name. Use `-` for standard output.

  > [!IMPORTANT]
  > Ensure that you store this file securely because it contains secrets. You can use the same file to set up more than one secured cluster. You cannot retrieve a previously generated CRS.

  Depending on the output that you select, the command might return some INFO messages about the CRS and the YAML file.

  The following is an example output:

  ``` terminal
  INFO:    Successfully generated new CRS
  INFO:
  INFO:     Name:       test-crs
  INFO:     Created at: 2025-02-26T19:07:21Z
  INFO:     Expires at: 2026-02-26T19:07:00Z
  INFO:     Created By: sample-token
  INFO:     ID:         9214a63f-7e0e-485a-baae-0757b0860ac9
  # This is a StackRox Cluster Registration Secret (CRS).
  # It is used for setting up StackRox secured clusters.
  # NOTE: This file contains secret data that allows connecting new secured clusters to central,
  # and needs to be handled and stored accordingly.
  apiVersion: v1
  data:
    crs: EXAMPLEZXlKMlpYSnphVzl1SWpveExDSkRRWE1pT2xzaUxTMHRMUzFDUlVkSlRpQkRSVkpVU1VaSlEwREXAMPLE=
  kind: Secret
  metadata:
    annotations:
      crs.platform.stackrox.io/created-at: "2025-02-26T19:07:21.800414339Z"
      crs.platform.stackrox.io/expires-at: "2026-02-26T19:07:00Z"
      crs.platform.stackrox.io/id: 9214a63f-7e0e-485a-baae-0757b0860ac9
      crs.platform.stackrox.io/name: test-crs
    creationTimestamp: null
    name: cluster-registration-secret
  INFO:   Then CRS needs to be stored securely, since it contains secrets.
  INFO:   It is not possible to retrieve previously generated CRSs.
  ```

</div>

<a id="roxctl-generate-init-bundle_init-bundle-cloud-other-generate"></a>

## Generating an init bundle by using the roxctl CLI

You can generate an init bundle with secrets by using the `roxctl` CLI.

> [!NOTE]
> You must have the `Admin` user role to create init bundles.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the `ROX_API_TOKEN` and the `ROX_CENTRAL_ADDRESS` environment variables:

  1.  Set the `ROX_API_TOKEN` by running the following command:

      ``` terminal
      $ export ROX_API_TOKEN=<api_token>
      ```

  2.  Set the `ROX_CENTRAL_ADDRESS` environment variable by running the following command:

      ``` terminal
      $ export ROX_CENTRAL_ADDRESS=<address>:<port_number>
      ```

      > [!IMPORTANT]
      > In RHACS Cloud Service, when using `roxctl` commands that require the Central address, use the **Central instance address** as displayed in the **Instance Details** section of the Red Hat Hybrid Cloud Console. For example, use `acs-ABCD12345.acs.rhcloud.com` instead of `acs-data-ABCD12345.acs.rhcloud.com`.

</div>

<div>

<div class="title">

Procedure

</div>

- To generate a cluster init bundle containing secrets for Helm installations, run the following command:

  ``` terminal
  $ roxctl -e "$ROX_CENTRAL_ADDRESS" \
    central init-bundles generate <cluster_init_bundle_name> --output \
    cluster_init_bundle.yaml
  ```

- To generate a cluster init bundle containing secrets for Operator installations, run the following command:

  ``` terminal
  $ roxctl -e "$ROX_CENTRAL_ADDRESS" \
    central init-bundles generate <cluster_init_bundle_name> --output-secrets \
    cluster_init_bundle.yaml
  ```

  > [!IMPORTANT]
  > Ensure that you store this bundle securely because it contains secrets. You can use the same bundle to set up more than one secured cluster.

</div>

<a id="next-steps_init-bundle-cloud-other-generate"></a>

# Next steps

After generating the cluster registration secret or init bundle, create resources to apply them to your secured clusters.

Create resources by using the CRS or the init bundle.

<a id="additional-resources_init-bundle-cloud-other-generate"></a>

# Additional resources

- [Creating resources by using the CRS or the init bundle](init-bundle-cloud-other-apply.md#create-resource-init-bundle_init-bundle-cloud-other-apply)
