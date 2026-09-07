<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To allow the Cloud Credential Operator (CCO) to pass cloud credentials to the components that request them, you can configure the Cloud Credential Operator (CCO) to operate in passthrough mode.

The credential must have permissions to perform the installation and complete the operations that are required by components in the cluster, but does not need to be able to create new credentials. The CCO does not attempt to create additional limited-scoped credentials in passthrough mode.

Passthrough mode is supported for Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere.

> [!NOTE]
> Manual mode is the only supported CCO configuration for Microsoft Azure Stack Hub.

# Passthrough mode permissions requirements

When using the CCO in passthrough mode, ensure that the credential you provide meets the requirements of the cloud on which you are running or installing OpenShift Container Platform. If the provided credentials the CCO passes to a component that creates a `CredentialsRequest` CR are not sufficient, that component will report an error when it tries to call an API that it does not have permissions for.

Amazon Web Services (AWS) permissions
The credential you provide for passthrough mode in AWS must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see "Manually creating long-term credentials for AWS.

Microsoft Azure permissions
The credential you provide for passthrough mode in Azure must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see "Manually creating long-term credentials for Azure".

Google Cloud permissions
The credential you provide for passthrough mode in Google Cloud must have all the requested permissions for all `CredentialsRequest` CRs that are required by the version of OpenShift Container Platform you are running or installing.

To locate the `CredentialsRequest` CRs that are required, see "Manually creating long-term credentials for Google Cloud".

Red Hat OpenStack Platform (RHOSP) permissions
To install an OpenShift Container Platform cluster on RHOSP, the CCO requires a credential with the permissions of a `member` user role.

VMware vSphere permissions
To install an OpenShift Container Platform cluster on VMware vSphere, the CCO requires a credential with the following vSphere privileges:

| Category               | Privileges                                |
|------------------------|-------------------------------------------|
| Datastore              | *Allocate space*                          |
| Folder                 | *Create folder*, *Delete folder*          |
| vSphere Tagging        | All privileges                            |
| Network                | *Assign network*                          |
| Resource               | *Assign virtual machine to resource pool* |
| Profile-driven storage | All privileges                            |
| vApp                   | All privileges                            |
| Virtual machine        | All privileges                            |

Required vSphere privileges

If `CredentialsRequest` CRs change over time as the cluster is upgraded, you must manually update the passthrough mode credential to meet the requirements. To avoid credentials issues during an upgrade, check the `CredentialsRequest` CRs in the release image for the new version of OpenShift Container Platform before upgrading.

To locate the `CredentialsRequest` CRs that are required for AWS, Azure, or Google Cloud, see the *Manually creating long-term credentials* topic for your platform.

# Admin credentials root secret format

The Cloud Credential Operator (CCO) creates a credentials root secret by minting new credentials with *mint mode* or by copying the credentials root secret with *passthrough mode*.

Each cloud provider uses a credentials root secret in the `kube-system` namespace by convention, which is then used to satisfy all credentials requests and create their respective secrets.

The format for the secret varies by cloud, and is also used for each `CredentialsRequest` secret.

<div class="formalpara">

<div class="title">

Amazon Web Services (AWS) secret format

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: aws-creds
stringData:
  aws_access_key_id: <base64-encoded_access_key_id>
  aws_secret_access_key: <base64-encoded_secret_access_key>
```

</div>

<div class="formalpara">

<div class="title">

Microsoft Azure secret format

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: azure-credentials
stringData:
  azure_subscription_id: <base64-encoded_subscription_id>
  azure_client_id: <base64-encoded_client_id>
  azure_client_secret: <base64-encoded_client_secret>
  azure_tenant_id: <base64-encoded_tenant_id>
  azure_resource_prefix: <base64-encoded_resource_prefix>
  azure_resourcegroup: <base64-encoded_resource_group>
  azure_region: <base64-encoded_region>
```

</div>

On Microsoft Azure, the credentials secret format includes two properties that must contain the cluster’s infrastructure ID, generated randomly for each cluster installation. This value can be found after running create manifests:

``` terminal
$ cat .openshift_install_state.json | jq '."*installconfig.ClusterID".InfraID' -r
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
mycluster-2mpcn
```

</div>

This value would be used in the secret data as follows:

``` yaml
azure_resource_prefix: mycluster-2mpcn
azure_resourcegroup: mycluster-2mpcn-rg
```

<div class="formalpara">

<div class="title">

Google Cloud secret format

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: gcp-credentials
stringData:
  service_account.json: <base64-encoded_service_account>
```

</div>

<div class="formalpara">

<div class="title">

Red Hat OpenStack Platform (RHOSP) secret format

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: openstack-credentials
data:
  clouds.yaml: <base64-encoded_cloud_creds>
  clouds.conf: <base64-encoded_cloud_creds_init>
```

</div>

<div class="formalpara">

<div class="title">

VMware vSphere secret format

</div>

``` yaml
apiVersion: v1
kind: Secret
metadata:
  namespace: kube-system
  name: vsphere-creds
data:
 vsphere.openshift.example.com.username: <base64-encoded_username>
 vsphere.openshift.example.com.password: <base64-encoded_password>
```

</div>

## Maintaining cloud provider credentials

If your cloud provider credentials are changed for any reason, you must manually update the secret that the Cloud Credential Operator (CCO) uses to manage cloud provider credentials.

The process for rotating cloud credentials depends on the mode that the CCO is configured to use. After you rotate credentials for a cluster that is using mint mode, you must manually remove the component credentials that were created by the removed credential.

<div>

<div class="title">

Prerequisites

</div>

- Your cluster is installed on a platform that supports rotating cloud credentials manually with the CCO mode that you are using:

  - For passthrough mode, Amazon Web Services (AWS), Microsoft Azure, Google Cloud, Red Hat OpenStack Platform (RHOSP), and VMware vSphere are supported.

- You have changed the credentials that are used to interface with your cloud provider.

- The new credentials have sufficient permissions for the mode CCO is configured to use in your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, navigate to **Workloads** → **Secrets**.

2.  In the table on the **Secrets** page, find the root secret for your cloud provider.

    | Platform       | Secret name             |
    |----------------|-------------------------|
    | AWS            | `aws-creds`             |
    | Azure          | `azure-credentials`     |
    | Google Cloud   | `gcp-credentials`       |
    | RHOSP          | `openstack-credentials` |
    | VMware vSphere | `vsphere-creds`         |

3.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) in the same row as the secret and select **Edit Secret**.

4.  Record the contents of the **Value** field or fields. You can use this information to verify that the value is different after updating the credentials.

5.  Update the text in the **Value** field or fields with the new authentication information for your cloud provider, and then click **Save**.

6.  If you are updating the credentials for a vSphere cluster that does not have the vSphere CSI Driver Operator enabled, you must force a rollout of the Kubernetes controller manager to apply the updated credentials.

    > [!NOTE]
    > If the vSphere CSI Driver Operator is enabled, this step is not required.

    To apply the updated vSphere credentials, log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role and run the following command:

    ``` terminal
    $ oc patch kubecontrollermanager cluster \
      -p='{"spec": {"forceRedeploymentReason": "recovery-'"$( date )"'"}}' \
      --type=merge
    ```

    While the credentials are rolling out, the status of the Kubernetes Controller Manager Operator reports `Progressing=true`. To view the status, run the following command:

    ``` terminal
    $ oc get co kube-controller-manager
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  In the **Administrator** perspective of the web console, navigate to **Workloads** → **Secrets**.

2.  Verify that the contents of the **Value** field or fields have changed.

</div>

<div>

<div class="title">

Additional resources

</div>

- [vSphere CSI Driver Operator](../../storage/container_storage_interface/persistent-storage-csi-vsphere.md)

</div>

## Reducing permissions after installation

When using passthrough mode, after installing you can reduce the installed permissions to only those permissions required to run the cluster.

In passthrough mode, each component has the same permissions used by all other components. If you do not reduce the permissions after installing, all components have the broad permissions that are required to run the installation program.

After installation, reduce the permissions on your credential to only those defined by the `CredentialsRequest` CRs in the release image for the version of OpenShift Container Platform that you are using.

To locate the `CredentialsRequest` CRs that are required for AWS, Azure, or Google Cloud and learn how to change the permissions the CCO uses, see the *Manually creating long-term credentials* topic for your platform.

# Additional resources

- [Manually creating long-term credentials for AWS](../../installing/installing_aws/ipi/installing-aws-customizations.md#manually-create-iam_installing-aws-customizations)

- [Manually creating long-term credentials for Azure](../../installing/installing_azure/ipi/installing-azure-customizations.md#manually-create-iam_installing-azure-customizations)

- [Manually creating long-term credentials for Google Cloud](../../installing/installing_gcp/installing-gcp-customizations.md#manually-create-iam_installing-gcp-customizations)
