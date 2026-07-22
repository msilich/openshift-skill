<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

By default, provider-managed encryption is used to secure the following when you deploy an OpenShift Container Platform cluster:

- The root (boot) volume of control plane and compute machines

- Persistent volumes (data volumes) that are provisioned after the cluster is deployed

You can override the default behavior by specifying an IBM® Key Protect for IBM Cloud® (Key Protect) root key as part of the installation process.

When you bring our own root key, you modify the installation configuration file (`install-config.yaml`) to specify the Cloud Resource Name (CRN) of the root key by using the `encryptionKey` parameter.

You can specify that:

- The same root key be used be used for all cluster machines. You do so by specifying the key as part of the cluster’s default machine configuration.

  When specified as part of the default machine configuration, all managed storage classes are updated with this key. As such, data volumes that are provisioned after the installation are also encrypted using this key.

- Separate root keys be used for the control plane and compute machine pools.

For more information about the `encryptionKey` parameter, see [Additional IBM Cloud configuration parameters](installation-config-parameters-ibm-cloud-vpc.md#installation-configuration-parameters-additional-ibm-cloud_installation-config-parameters-ibm-cloud-vpc).

> [!NOTE]
> Make sure you have integrated Key Protect with your IBM Cloud Block Storage service. For more information, see the Key Protect [documentation](https://cloud.ibm.com/docs/key-protect?topic=key-protect-integrate-services#grant-access).

# Next steps

Install an OpenShift Container Platform cluster:

- [Installing a cluster on IBM Cloud with customizations](installing-ibm-cloud-customizations.md#installing-ibm-cloud-customizations)

- [Installing a cluster on IBM Cloud with network customizations](installing-ibm-cloud-customizations.md#installing-ibm-cloud-customizations)

- [Installing a cluster on IBM Cloud into an existing VPC](installing-ibm-cloud-vpc.md#installing-ibm-cloud-vpc)

- [Installing a private cluster on IBM Cloud](installing-ibm-cloud-private.md#installing-ibm-cloud-private)
