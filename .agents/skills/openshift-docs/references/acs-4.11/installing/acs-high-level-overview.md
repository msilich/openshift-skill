<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) provides security services for your self-managed Red Hat OpenShift Kubernetes systems or platforms such as OpenShift Container Platform, Amazon Elastic Kubernetes Service (Amazon EKS), Google Kubernetes Engine (Google GKE), and Microsoft Azure Kubernetes Service (Microsoft AKS). RHACS offers several installation methods, depending on the type of platform you use.

<a id="acs-installation-guidelines_acs-high-level-overview"></a>

# Installation guidelines

To ensure the best installation experience, review the available platforms, understand the Red Hat Advanced Cluster Security for Kubernetes architecture, and check the default resource requirements before you begin.

Follow these installation guidelines:

1.  Understand the installation platforms and methods that are available.

2.  Understand the Red Hat Advanced Cluster Security for Kubernetes architecture. For more information, see "Red Hat Advanced Cluster Security for Kubernetes architecture".

3.  Check the default resource requirements. For more information, see "Default resource requirements".

<a id="install-platforms-methods_acs-high-level-overview"></a>

# Installation methods for different platforms

You can perform different types of installations on different platforms. Not all installation methods are supported for all platforms. See the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix" for more information.

| **Platform type** | **Platform** | **Recommended installation methods** | **Installation steps** |
|----|----|----|----|
| Managed service platform | Red Hat OpenShift Dedicated (OSD) | Operator (recommended), Helm charts, or `roxctl` CLI <sup>\[1\]</sup> | For more information, see Installing Central services for RHACS on Red Hat OpenShift and Installing Secured Cluster services for RHACS on Red Hat OpenShift |
| Azure Red Hat OpenShift (ARO) |  |  |  |
| Red Hat OpenShift Service on AWS (ROSA) |  |  |  |
| Red Hat OpenShift on IBM Cloud |  |  |  |
| Amazon Elastic Kubernetes Service (Amazon EKS) | Helm charts (recommended), or `roxctl` CLI <sup>\[1\]</sup> | For more information, see Installing Central services for RHACS on other platforms and Installing Secured Cluster services for RHACS on other platforms |  |
| Google Kubernetes Engine (Google GKE) |  |  |  |
| Microsoft Azure Kubernetes Service (Microsoft AKS) |  |  |  |
| Self-managed platform | Red Hat OpenShift Container Platform (OCP) | Operator (recommended), Helm charts, or `roxctl` CLI <sup>\[1\]</sup> | For more information, see Installing Central services for RHACS on Red Hat OpenShift and Installing Secured Cluster services for RHACS on Red Hat OpenShift |
| Red Hat OpenShift Kubernetes Engine (OKE) |  |  |  |

Platforms and recommended installation methods

1.  Do not use the `roxctl` installation method unless you have specific requirements for following this installation method.

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Installing Central services for RHACS on Red Hat OpenShift](installing_ocp/install-central-ocp.md)

- [Installing secured cluster services for RHACS on Red Hat OpenShift](installing_ocp/install-secured-cluster-ocp.md)

- [Installing Central services for RHACS on other platforms](installing_other/install-central-other.md)

- [Installing secured cluster services for RHACS on other platforms](installing_other/install-secured-cluster-other.md)

</div>

<a id="installation-methods-for-different-architectures_acs-high-level-overview"></a>

# Installation methods for different architectures

Red Hat Advanced Cluster Security for Kubernetes (RHACS) supports the following architectures. For information on supported platforms and architecture, see the "Red Hat Advanced Cluster Security for Kubernetes Support Matrix". Additionally, the following table gives information about installation methods available for each architecture.

| **Supported architectures** | **Supported installation methods** |
|----|----|
| AMD64 | Operator (preferred), Helm charts, or `roxctl` CLI (not recommended) |
| ppc64le (IBM Power) | Operator |
| s390x (IBM Z and IBM® LinuxONE) |  |
| AArch64 (`ARM64`) | Operator (preferred), Helm charts, or `roxctl` CLI |

Architectures and supported installation methods for each architecture

<div>

<div class="title">

Additional resources

</div>

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

</div>

<a id="installation-secrets-auth_acs-high-level-overview"></a>

# Setting up authentication between Central and secured clusters

When you install Red Hat Advanced Cluster Security for Kubernetes (RHACS), you must generate a component that is used between Central and the secured clusters to set up secure communication. Central, also called the Central instance in Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), is the specific service that provides the ACS Console, handles all API interactions, and manages data storage and image scanning. The user interface is called the RHACS portal for RHACS and is called the ACS Console for RHACS Cloud Service.

The original component used to authenticate when establishing the connection between Central and secured clusters is called an init bundle. A later component, called a cluster registration secret (CRS), provides a more secure mechanism to set up this communication. You generate an init bundle or a CRS in the cluster where Central is located, and then you install it onto the secured clusters.

<a id="init-bundle-overview_acs-high-level-overview"></a>

## Init bundles

An init bundle is a YAML file that contains security secrets that allow a new Kubernetes cluster to connect securely to Central.

This file is used to create the specific Kubernetes secrets of `sensor-tls`, `collector-tls`, and `admission-control-tls`. These services contain certificates and private keys required for mutual TLS (mTLS) authentication. The certificates inside an init bundle are valid for one year by default. If they expire, the secured cluster will disconnect, and you must generate and apply a new bundle.

A single init bundle can be used to connect multiple different clusters to the same Central instance, although using unique bundles for different groups of clusters can make revoking access easier if credentials are compromised. You can reapply an init bundle to a secured cluster to provide an existing secured cluster with new or updated certificates.

<a id="cluster-registration-secret-overview_acs-high-level-overview"></a>

## Cluster registration secrets

Beginning with RHACS version 4.7, RHACS provides a more secure alternative to init bundles, called Cluster Registration Secrets (CRSes).

Unlike an init bundle, which contains long-lived certificates, a CRS contains a token that the secured cluster uses to request its own certificates. Therefore, you can revoke the CRS immediately after installation without breaking the cluster’s connection. Unlike init bundles, you cannot put a new CRS on the cluster and have the secured cluster use this CRS to reestablish the communication with Central. You must generate a new CRS in Central and then reapply the new CRS to the secured cluster and reestablish the secured connection.

<a id="installing-rhacs-ocp-steps_acs-high-level-overview"></a>

# Installation steps for RHACS on OpenShift Container Platform

You can install RHACS on Red Hat OpenShift by using the RHACS Operator, Helm charts, or the `roxctl` CLI.

<a id="installing-ocp-operator-steps_acs-high-level-overview"></a>

## Installing RHACS on Red Hat OpenShift by using the RHACS Operator

Follow these steps to install RHACS on Red Hat OpenShift by using the RHACS Operator.

<div>

<div class="title">

Procedure

</div>

1.  On the Red Hat OpenShift cluster, install the RHACS Operator into the `rhacs-operator` project, or namespace.

2.  On the Red Hat OpenShift cluster that has Central, called the central cluster, use the RHACS Operator to install Central services into the `stackrox` project. One central cluster can secure many clusters.

3.  Log in to the RHACS web console from the central cluster, and generate a cluster registration secret (CRS) or an init bundle and download it. The CRS or the init bundle is then installed on the cluster that you want to secure, called the secured cluster. The CRS or the init bundle contains the cryptographic artifacts that RHACS uses to establish trusted connections between Central and secured clusters.

    > [!NOTE]
    > Init bundles are still supported, but using a CRS is the preferred method for securing your cluster.

4.  For the secured cluster:

    1.  Install the RHACS Operator into the `rhacs-operator` namespace.

    2.  Apply the CRS or the init bundle that you generated in RHACS to the secured cluster by performing one of these steps:

        - Use the OpenShift Container Platform web console to import the YAML file of the CRS or the init bundle that you generated. Make sure you are in the `stackrox` namespace.

        - Use the OpenShift CLI to perform one of the following actions:

          - If you generated a CRS, in the terminal window, run the `oc create -f <file_name.yaml> -n <stackrox>` command, specifying the path to the downloaded CRS.

          - If you generated an init bundle, in the terminal window, run the `oc create -f <init_bundle.yaml> -n <stackrox>` command, specifying the path to the downloaded YAML file of the init bundle.

    3.  On the secured cluster, use the RHACS Operator to install Secured Cluster services into the `stackrox` namespace. When creating these services, be sure to enter the address of Central in the **Central Endpoint** field so that the secured cluster can communicate with Central.

</div>

<a id="installing-ocp-helm-steps_acs-high-level-overview"></a>

## Installing RHACS on Red Hat OpenShift by using Helm charts

Follow these steps to install RHACS on Red Hat OpenShift by using Helm charts.

<div>

<div class="title">

Procedure

</div>

1.  Add the RHACS Helm charts repository.

2.  Install the `central-services` Helm chart on the Red Hat OpenShift cluster that will contain Central, called the central cluster.

3.  Log in to the RHACS web console on the Central cluster and generate a CRS or an init bundle.

4.  For each cluster that you want to secure, log in to the secured cluster and use the `helm install` command to install the `secured-cluster-services` Helm chart, specifying the path to the CRS or the init bundle that you generated.

</div>

<a id="installing-ocp-roxctl-steps_acs-high-level-overview"></a>

## Installing RHACS on Red Hat OpenShift by using the `roxctl` CLI

This installation method is also called the *manifest installation method*.

<div>

<div class="title">

Procedure

</div>

1.  Install the `roxctl` CLI.

2.  On the Red Hat OpenShift cluster that will contain Central, perform these steps:

    1.  In the terminal window, run the interactive install command by using the `roxctl` CLI.

    2.  Run the setup shell script.

    3.  In the terminal window, create the Central resources by using the `oc create` command.

3.  Perform one of the following actions:

    - In the RHACS web console, create and download the sensor YAML file and keys.

    - On the secured cluster, use the `roxctl sensor generate openshift` command.

4.  On the secured cluster, run the sensor installation script.

</div>

<a id="installing-rhacs-kubernetes-steps_acs-high-level-overview"></a>

# Installation steps for RHACS on Kubernetes

You can install RHACS on Kubernetes platforms by using Helm charts or the `roxctl` CLI.

<a id="installing-kube-helm-steps_acs-high-level-overview"></a>

## Installing RHACS on Kubernetes platforms by using Helm charts

Follow these steps to install RHACS on Kubernetes platforms by using Helm charts.

<div>

<div class="title">

Procedure

</div>

1.  Add the RHACS Helm charts repository.

2.  Install the `central-services` Helm chart on the cluster that will contain Central, called the Central cluster.

3.  Log in to the RHACS web console from the Central cluster and generate a cluster registration secret (CRS). You need to apply the CRS to the cluster that you want to secure, called the secured cluster. The CRS has the cryptographic artifacts that RHACS uses to establish trusted connections between Central and secured clusters.

    > [!NOTE]
    > Init bundles are still supported, but using a CRS is the preferred method for securing your cluster.

4.  For each secured cluster, install the `secured-cluster-services` Helm chart by running one of the following commands:

    - For a CRS, run the following command:

      ``` terminal
      $ helm install -n stackrox \
        --create-namespace stackrox-secured-cluster-services rhacs/secured-cluster-services \
        --set-file crs.file=<crs_file_name.yaml> \
        -f <path_to_values_public.yaml> \
        -f <path_to_values_private.yaml> \
        --set imagePullSecrets.username=<username> \
        --set imagePullSecrets.password=<password>
      ```

      where:

      `<crs_file_name.yaml>`  
      Specifies the name of the file which has the generated CRS.

      `<path_to_values_public.yaml>`  
      Specifies the path to your public YAML configuration file.

      `<path_to_values_private.yaml>`  
      Specifies the path to your private YAML configuration file.

      `<username>`  
      Specifies the user name for your pull secret for Red Hat Container Registry authentication.

      `<password>`  
      Specifies the password for your pull secret for Red Hat Container Registry authentication.

    - For an init bundle, run the following command:

      ``` terminal
      $ helm install -n stackrox \
        --create-namespace stackrox-secured-cluster-services rhacs/secured-cluster-services \
        -f <name_of_cluster_init_bundle.yaml> \
        -f <path_to_values_public.yaml> \
        -f <path_to_values_private.yaml> \
        --set imagePullSecrets.username=<username> \
        --set imagePullSecrets.password=<password>
      ```

      where:

      `<path_to_values_public.yaml>`  
      Specifies the path to your public YAML configuration file.

      `<path_to_values_private.yaml>`  
      Specifies the path to your private YAML configuration file.

      `<username>`  
      Specifies the user name for your pull secret for Red Hat Container Registry authentication.

      `<password>`  
      Specifies the password for your pull secret for Red Hat Container Registry authentication.

</div>

<a id="installing-kube-roxctl-steps_acs-high-level-overview"></a>

## Installing RHACS on Kubernetes platforms by using the `roxctl` CLI

This installation method is also called the *manifest installation method*.

<div>

<div class="title">

Procedure

</div>

1.  Install the `roxctl` CLI.

2.  On the Kubernetes cluster that will contain Central, perform these steps:

    1.  In the terminal window, run the interactive install command by using the `roxctl` CLI.

    2.  Run the setup shell script.

    3.  In the terminal window, create the Central resources by using the `kubectl create` command.

3.  Perform one of the following actions:

    - In the RHACS web console, create and download the sensor YAML file and keys.

    - On the cluster that you want to secure, called the secured cluster, use the `roxctl sensor generate openshift` command.

4.  On the secured cluster, run the sensor installation script.

</div>

<a id="additional-resources_acs-high-level-overview"></a>

# Additional resources

- [Red Hat Advanced Cluster Security for Kubernetes Support Matrix](https://access.redhat.com/articles/7045053)

- [Red Hat Advanced Cluster Security for Kubernetes Support Policy](https://access.redhat.com/support/policy/updates/rhacs)

- [Red Hat Advanced Cluster Security for Kubernetes architecture](../architecture/acs-architecture.md#acs-architecture_acs-architecture)

- [Default resource requirements](acs-default-requirements.md)
