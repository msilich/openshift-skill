<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) uses a special artifact during installation that allows Central to communicate securely with the secured clusters that you are adding. This file is called a cluster registration secret (CRS) or an init bundle. Init bundles are still supported, but using a CRS is the preferred way to set up a secured cluster.

A cluster registration secret (CRS) is an authentication secret that offers improved security and are easier to use than init bundles. A CRS contain a single token that can be used when installing RHACS by using both Operator and Helm installation methods.

A CRS provides better security because it is only used for registering a new secured cluster. If leaked, the certificates and keys in an init bundle can be used to impersonate services running on a secured cluster. By contrast, the certificate and key in a CRS can only be used for *registering* a new cluster.

After the cluster is set up by using the CRS, service-specific certificates are issued by Central and sent to the new secured cluster. These service certificates are used for communication between Central and secured clusters. Therefore, a CRS can be revoked after the cluster is registered without disconnecting secured clusters.

Unlike init bundles, which can be re-applied on an existing secured cluster if secrets on the secured cluster need to be manually refreshed, you cannot apply a new CRS to a cluster and re-establish communication between Central and the secured cluster. If there is a problem with the CRS on a secured cluster, for example, if the certificate and keys are deleted, you must revoke the original CRS in Central and remove it from the secured cluster. Then, you create a new CRS in Central, and apply the new CRS to the secured clusters.

<a id="init-bundles-and-cluster-registration-secrets_init-bundle-other"></a>

# Init bundles and cluster registration secrets

To establish a secure communication channel between RHACS Central and your secured clusters, you must generate and apply authentication artifacts. You can generate a cluster registration secret (CRS) or an init bundle by using the RHACS portal or CLI.

Although init bundles are still supported, using a CRS to establish the connection between Central and your secured clusters is the preferred method because it offers a reusable, time-bound token that you can use to register multiple clusters.

After creating a CRS or an init bundle, you provide the CRS or the init bundle when you run the `helm install` command.

> [!NOTE]
> You must have the `Admin` user role to generate a CRS or an init bundle.

<a id="generate-crs-other_init-bundle-other"></a>

# Cluster registration secrets

A cluster registration secret (CRS) is a security artifact that allows a secured cluster to authenticate with Central. You generate a CRS by using the `roxctl` CLI.

The CRS ensures that the services on the secured cluster such as Sensor and Collector are authorized to communicate with your Central instance. When you generate a CRS, the output is a standard Kubernetes Secret YAML file. You must apply this secret to the project namespace on the cluster where you intend to install the secured cluster services.

The following are the key characteristics of a CRS:

Security  
The generated file contains sensitive credentials and must be stored securely.

One-time generation  
You cannot retrieve a previously generated CRS from Central. If you lose the file, you must generate a new one.

Reuse  
You can use a single CRS to authenticate more than one secured cluster.

Expiration  
The secret includes an expiration date, after which it is no longer valid for registering new clusters.

> [!NOTE]
> If you are installing secured cluster services by using Helm charts, you provide the CRS file during the `helm install` command execution rather than applying it as a separate step.

<a id="portal-generate-crs_init-bundle-other"></a>

# Generating a cluster registration secret by using the RHACS portal

You can generate a cluster registration secret (CRS) by using the RHACS portal.

> [!NOTE]
> You must have the `Admin` user role to generate a CRS.

<div>

<div class="title">

Procedure

</div>

1.  Find the address of the RHACS portal as described in "Verifying Central installation using the Operator method".

2.  Log in to the RHACS portal. If you do not have secured clusters or an existing CRS, the **Platform Configuration** → **Clusters** page appears.

3.  Click **Create cluster registration secret**.

4.  Enter a name for the CRS and click **Download** to generate and download it. The CRS is created in the form of a YAML file and you can use it to secure all of your clusters if you are using the same installation method.

    > [!IMPORTANT]
    > Store this file securely because it contains secrets.

</div>

<div>

<div class="title">

Next steps

</div>

1.  Apply the CRS to the secured cluster.

2.  Install secured cluster services on each cluster.

</div>

<a id="crs-generate-roxctl_init-bundle-other"></a>

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

<a id="crs-apply-secured-cluster_init-bundle-other"></a>

## Applying the cluster registration secret (CRS) on the secured cluster

Before you configure a secured cluster, you must apply the CRS to the cluster. After you have applied the CRS, the services on the secured cluster can communicate securely with Central.

> [!NOTE]
> If you are installing by using Helm charts, do not perform this step. Complete the installation by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You must have generated a CRS.

</div>

<div>

<div class="title">

Procedure

</div>

- Using the `kubectl` CLI, run the following commands to create the resources:

  ``` terminal
  $ kubectl create namespace stackrox
  ```

  This command creates the project where secured cluster resources will be installed. This example uses `stackrox`.

  ``` terminal
  $ kubectl create -f <file_name.yaml> \
    -n <stackrox>
  ```

  where:

  `<file_name.yaml>`  
  Specifies the file name of the CRS.

  `<stackrox>`  
  Specifies the project name that you created. This example uses `stackrox`.

</div>

<a id="generate-init-bundle-other_init-bundle-other"></a>

# Init bundles for secured cluster authentication

You can establish secure communication between your secured cluster services and Red Hat Advanced Cluster Security for Kubernetes (RHACS) Central by generating and applying an init bundle. You can create an YAML file containing essential TLS secrets by using the RHACS portal or the `roxctl` CLI, and then apply the resources to your cluster to authorize service connections.

When you apply the init bundle to a secured cluster, it creates the necessary TLS certificate resources, including:

- `collector-tls`

- `sensor-tls`

- `admission-control-tls`

You can generate init bundles by using either the RHACS portal or the `roxctl` CLI. The bundle is generated as a YAML file containing the required secrets. Because this file contains sensitive credentials, it must be stored securely.

> [!NOTE]
> If you are installing secured cluster services by using Helm charts, the init bundle is often applied as part of the Helm installation command rather than as a separate step.

<a id="portal-generate-init-bundle_init-bundle-other"></a>

## Generating a cluster registration secret or init bundle by using the RHACS portal

You can generate a cluster registration secret (CRS) or an init bundle that contains secrets by using the RHACS portal.

> [!NOTE]
> You must have the `Admin` user role to generate a CRS or an init bundle.

<div>

<div class="title">

Procedure

</div>

1.  Find the address of the RHACS portal as described in "Verifying Central installation using the Operator method".

2.  Log in to the RHACS portal. If you do not have secured clusters, or an existing CRS or an init bundle, the **Platform Configuration** → **Clusters** page is displayed.

3.  Click **Create cluster registration secret** or **Init bundles installation method**.

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

<a id="roxctl-generate-init-bundle_init-bundle-other"></a>

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

<a id="create-resource-init-bundle_init-bundle-other"></a>

## Applying the init bundle on the secured cluster

Before you configure a secured cluster, you must apply the init bundle to the secured cluster. Applying the init bundle allows the services on the secured cluster to communicate with Central.

> [!NOTE]
> If you are installing by using Helm charts, do not perform this step. Complete the installation by using Helm.

<div>

<div class="title">

Prerequisites

</div>

- You must have generated an init bundle containing secrets. The preferred way to set up a secured cluster is by using a CRS.

- You must have created the `stackrox` project, or namespace, on the cluster where you will install secured cluster services. Using `stackrox` for the project is not required, but ensures that vulnerabilities for RHACS processes are not reported when scanning your clusters.

</div>

<div>

<div class="title">

Procedure

</div>

- Using the `kubectl` CLI, run the following commands to create the resources:

  ``` terminal
  $ kubectl create namespace stackrox
  ```

  This command creates the project where secured cluster resources will be installed. This example uses `stackrox`.

  ``` terminal
  $ kubectl create -f <init_bundle.yaml> \
    -n <stackrox>
  ```

  where:

  `<init_bundle.yaml>`  
  Specifies the file name of the init bundle containing the secrets.

  `<stackrox>`  
  Specifies the project name that you created. This example uses `stackrox`.

</div>

<a id="next-steps_init-bundle-other_init-bundle-other"></a>

# Next steps

After you have generated and applied the cluster registration secret (CRS) or the init bundle, you can proceed to install the services.

Install Red Hat Advanced Cluster Security for Kubernetes (RHACS) secured cluster services in all clusters that you want to monitor.

<a id="_additional_resources"></a>

# Additional resources

- [Installing secured cluster services for RHACS on Red Hat OpenShift](../installing_ocp/install-secured-cluster-ocp.md)

- [Installing secured cluster services for RHACS on other platforms](install-secured-cluster-other.md)
