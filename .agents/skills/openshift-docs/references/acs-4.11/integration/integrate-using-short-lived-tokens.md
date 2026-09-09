<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat Advanced Cluster Security for Kubernetes (RHACS) you can authenticate against selected cloud provider APIs by using short-lived tokens.

<a id="short-lived-tokens-integration-overview_integrate-using-short-lived-tokens"></a>

# Short-lived token integration overview

RHACS supports short-lived token authentication with Amazon Web Services, Google Cloud, and Microsoft Azure cloud providers on specific Kubernetes platforms.

RHACS supports the following cloud provider integrations:

- Amazon Web Services (AWS) using the Secure Token Service (STS)

- Google Cloud using workload identity federation

- Microsoft Azure using Microsoft Entra ID with managed identities

RHACS supports short-lived token integrations only when you install RHACS on the following platforms:

- Elastic Kubernetes Service (EKS) on AWS

- Google Kubernetes Engine (GKE) on GCP

- Microsoft Azure Kubernetes Service (AKS)

- OpenShift Container Platform

To activate short-lived authentication, you must establish trust between your Kubernetes or OpenShift Container Platform cluster and your cloud provider. For EKS, GKE and AKS clusters, use the cloud provider metadata service. For OpenShift Container Platform clusters, you need a publicly available OpenID Connect (OIDC) provider bucket containing the OpenShift Container Platform service account signer key.

> [!NOTE]
> You must establish trust with your cloud provider for every Central cluster that uses the short-lived token integration. However, if you use delegated scanning in combination with short-lived token image integrations, you must also establish trust for the Sensor cluster.

<a id="aws-secure-token-service-overview_integrate-using-short-lived-tokens"></a>

# Configuring AWS Secure Token Service

RHACS integrations can authenticate against Amazon Web Services by using the Secure Token Service. You must configure `AssumeRole` with RHACS before enabling the **Use container IAM role** option in integrations.

> [!IMPORTANT]
> Verify that the AWS role associated with the RHACS pod must have the IAM permissions required by the integration. For example, to set up a container role for integrating with the Elastic Container Registry, enable full read access to the registry.

<div>

<div class="title">

Additional resources

</div>

- [Secure Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html)

- [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html)

</div>

<a id="amazon-secure-token-service-eks_integrate-using-short-lived-tokens"></a>

## Configuring Elastic Kubernetes Service (EKS)

When running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on EKS, you can configure short-lived tokens through the Amazon Secure Token Service.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to enable the IAM OpenID Connect (OIDC) provider for your EKS cluster:

    ``` terminal
    $ eksctl utils associate-iam-oidc-provider --cluster <cluster_name> --approve
    ```

2.  Create an IAM role for your EKS cluster.

3.  Edit the permission policy of the role and grant the permissions required by the integration. For example:

    ``` json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:BatchGetImage",
                    "ecr:DescribeImages",
                    "ecr:DescribeRepositories",
                    "ecr:GetAuthorizationToken",
                    "ecr:GetDownloadUrlForLayer",
                    "ecr:ListImages"
                ],
                "Resource": "arn:aws:iam::<ecr_registry>:role/<role_name>"
            }
        ]
    }
    ```

4.  Update the trust relationship for the role that you want to assume:

    ``` json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::<ecr_registry>:role/<role_name>"
            ]
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```

    where:

    `<ecr_registry>`  
    Specifies the `<role_name>`, which should match with the new role that you have created in the earlier steps.

5.  Enter the following command to associate the newly created role with a service account:

    ``` terminal
    $ oc -n stackrox annotate sa central eks.amazonaws.com/role-arn=arn:aws:iam::67890:role/<role_name>
    ```

6.  Enter the following command to restart the Central pod and apply the changes:

    ``` terminal
    $ oc -n stackrox delete pod -l "app in (central,sensor)"
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html)

</div>

<a id="amazon-secure-token-service-openshift_integrate-using-short-lived-tokens"></a>

## Configuring OpenShift Container Platform

When running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on OpenShift Container Platform, you can configure short-lived tokens through the Amazon Secure Token Service.

<div>

<div class="title">

Prerequisites

</div>

- You must have a public OpenID Connect (OIDC) configuration bucket with the OpenShift Container Platform service account signer key. To get the OIDC configuration for the OpenShift Container Platform cluster, Red Hat recommends using the "Cloud Credential Operator in manual mode for short-term credentials" instructions.

- You must have access to AWS IAM and the permissions to create and change roles.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Follow the "Creating OpenID Connect (OIDC) identity providers" instructions to create web identity of the OpenShift Container Platform cluster. Use `openshift` as the value for **Audience**.

2.  Create an IAM role for the web identity of the OpenShift Container Platform cluster.

3.  Edit the permission policy of the role and grant the permissions required by the integration. For example:

    ``` json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": [
                    "ecr:BatchCheckLayerAvailability",
                    "ecr:BatchGetImage",
                    "ecr:DescribeImages",
                    "ecr:DescribeRepositories",
                    "ecr:GetAuthorizationToken",
                    "ecr:GetDownloadUrlForLayer",
                    "ecr:ListImages"
                ],
                "Resource": "arn:aws:iam::<ecr_registry>:role/<role_name>"
            }
        ]
    }
    ```

4.  Update the trust relationship for the role that you want to assume:

    ``` json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {
                    "Federated": "<oidc_provider_arn>"
                },
                "Action": "sts:AssumeRoleWithWebIdentity",
                "Condition": {
                    "StringEquals": {
                        "<oidc_provider_name>:aud": "openshift"
                    }
                }
            }
        ]
    }
    ```

5.  Set the following RHACS environment variables on the Central or Sensor deployment:

        AWS_ROLE_ARN=<role_arn>
        AWS_WEB_IDENTITY_TOKEN_FILE=/var/run/secrets/openshift/serviceaccount/token

</div>

<div>

<div class="title">

Additional resources

</div>

- [Cloud Credential Operator in manual mode for short-term credentials](https://docs.openshift.com/container-platform/4.14/authentication/managing_cloud_provider_credentials/cco-short-term-creds.html)

- [Creating OpenID Connect (OIDC) identity providers](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_create_oidc.html)

- [Create an IAM role for web identity](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-idp_oidc.html)

</div>

<a id="google-workload-identity-federation-overview_integrate-using-short-lived-tokens"></a>

# Configuring Google workload identity federation

RHACS integrations can authenticate against the Google Cloud by using workload identities. Select the **Use workload identity** option upon creation to enable workload identity authentication in a Google Cloud integration.

> [!IMPORTANT]
> The Google service account associated with the RHACS pod through the workload identity must have the IAM permissions required by the integration. For example, to set up a workload identity for integrating with Google Artifact Registry, connect a service account with the **roles/artifactregistry.reader** role.

<div>

<div class="title">

Additional resources

</div>

- [Workload identities](https://cloud.google.com/iam/docs/workload-identity-federation)

- [Configure roles and permissions](https://cloud.google.com/artifact-registry/docs/access-control)

</div>

<a id="google-workload-identity-federation-gke_integrate-using-short-lived-tokens"></a>

## Configuring Google Kubernetes Engine (GKE)

When running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on GKE, you can configure short-lived tokens through Google workload identities.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Prerequisites

</div>

- You must have access to the Google Cloud project containing the cluster and integration resources.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Follow the instructions in the Google Cloud documentation to use workload identity federation for GKE.

2.  Annotate the RHACS service account by running the following command:

    ``` terminal
    $ oc annotate serviceaccount \
        central \
        --namespace stackrox \
        iam.gke.io/gcp-service-account=<GSA_NAME>@<GSA_PROJECT>.iam.gserviceaccount.com
    ```

    > [!IMPORTANT]
    > When setting up delegated scanning, use **sensor** instead of **central**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Use workload identity federation for GKE](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity)

</div>

<a id="google-workload-identity-federation-openshift_integrate-using-short-lived-tokens"></a>

## Configuring OpenShift Container Platform

You can configure short-lived tokens through Google workload identities when running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- You must have a public OIDC configuration bucket with the OpenShift Container Platform service account signer key. The recommended way to obtain the OIDC configuration for the OpenShift Container Platform cluster is to use the [Cloud Credential Operator in manual mode for short-term credentials](https://docs.openshift.com/container-platform/4.14/authentication/managing_cloud_provider_credentials/cco-short-term-creds.html) instructions.

- Access to a Google Cloud project with the **roles/iam.workloadIdentityPoolAdmin** role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Follow the "Manage workload identity pools" instructions to create a workload identity pool. For example:

    ``` terminal
    $ gcloud iam workload-identity-pools create rhacs-pool \
        --location="global" \
        --display-name="RHACS workload pool"
    ```

2.  Follow the "Manage workload identity pool providers" instructions to create a workload identity pool provider. For example:

    ``` terminal
    $ gcloud iam workload-identity-pools providers create-oidc rhacs-provider \
        --location="global" \
        --workload-identity-pool="rhacs-pool" \
        --display-name="RHACS provider" \
        --attribute-mapping="google.subject=assertion.sub" \
        --issuer-uri="https://<oidc_configuration_url>" \
        --allowed-audiences=openshift
    ```

3.  Connect a Google service account to the workload identity pool. For example:

    ``` terminal
    $ gcloud iam service-accounts add-iam-policy-binding <GSA_NAME>@<GSA_PROJECT>.iam.gserviceaccount.com \
        --role roles/iam.workloadIdentityUser \
        --member="principal://iam.googleapis.com/projects/<GSA_PROJECT_NUMBER>/locations/global/workloadIdentityPools/rhacs-provider/subject/system:serviceaccount:stackrox:central"
    ```

    where:

    `<system:serviceaccount:stackrox:central>`  
    Specifies the subject. For delegated scanning, you must set the subject to **system:serviceaccount:stackrox:sensor**.

4.  Create a service account JSON containing the Security token service (STS) configuration. For example:

    ``` json
    {
      "type": "external_account",
      "audience": "//iam.googleapis.com/projects/<GSA_PROJECT_ID>/locations/global/workloadIdentityPools/rhacs-pool/providers/rhacs-provider",
      "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
      "token_url": "https://sts.googleapis.com/v1/token",
      "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/<GSA_NAME>@<GSA_PROJECT>.iam.gserviceaccount.com:generateAccessToken",
      "credential_source": {
        "file": "/var/run/secrets/openshift/serviceaccount/token",
        "format": {
          "type": "text"
        }
      }
    }
    ```

5.  Use the service account JSON as a secret to the RHACS namespace:

    ``` yaml
    apiVersion: v1
    kind: Secret
    metadata:
      name: gcp-cloud-credentials
      namespace: stackrox
    data:
      credentials: <base64_encoded_json>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Manage workload identity pools](https://cloud.google.com/iam/docs/manage-workload-identity-pools-providers#iam-workload-pools-list-gcloud)

- [Manage workload identity pool providers](https://cloud.google.com/iam/docs/manage-workload-identity-pools-providers#manage-providers)

</div>

<a id="azure-entra-id-federation-overview_integrate-using-short-lived-tokens"></a>

# Configuring Microsoft Entra ID federation

RHACS integrations can authenticate to Microsoft Azure by using managed or workload identities. Select the **Use workload identity** checkbox during the creation of a new Microsoft Azure Container Registry (ACR) integration, if you want to enable authentication by using managed or workload identities in a Microsoft Azure integration.

> [!IMPORTANT]
> The identity associated with the RHACS pod through the workload identity must have the IAM permissions for the integration. For example, to set up a workload identity for integrating with Microsoft ACR, assign the **Reader** role over a scope that includes the registry.

<div>

<div class="title">

Additional resources

</div>

- [What are managed identities for Azure resources?](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview)

- [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation)

- [Azure RBAC documentation](https://learn.microsoft.com/en-us/azure/role-based-access-control/)

</div>

<a id="azure-workload-identity-federation-gke_integrate-using-short-lived-tokens"></a>

## Configuring Microsoft Azure Kubernetes Service

By running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on Microsoft Azure Kubernetes Service (AKS), you can configure short-lived tokens by using Microsoft Entra ID managed identities.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster and integration resources within Microsoft Azure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a trust relationship between the external IdP and a user-assigned managed identity or application in Microsoft Entra ID.

2.  Annotate the RHACS service account by running the following command:

    > [!IMPORTANT]
    > When setting up the delegated scanning, use **sensor** instead of **central**.

    ``` terminal
    $ oc annotate serviceaccount \
        central \
        --namespace stackrox \
        azure.workload.identity/client-id=<CLIENT_ID>
    ```

    where:

    `<CLIENT_ID>`  
    Specifies the client ID of the associated identity.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    serviceaccount/central annotated
    ```

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation#how-it-works)

</div>

<a id="azure-workload-identity-federation-openshift_integrate-using-short-lived-tokens"></a>

## Configuring OpenShift Container Platform

By running Red Hat Advanced Cluster Security for Kubernetes (RHACS) on OpenShift Container Platform, you can configure short-lived tokens by using Microsoft Entra ID managed identities.

<div>

<div class="title">

Prerequisites

</div>

- You have a public OpenID Connect (OIDC) configuration bucket with the OpenShift Container Platform service account signer key.

  For more information, see ["Manual mode with short-term credentials for components"](https://docs.openshift.com/container-platform/4.21/authentication/managing_cloud_provider_credentials/cco-short-term-creds.html) in *OpenShift Container Platform* documentation.

- You have a Microsoft Entra ID user-assigned managed identity.

- You have access to a Microsoft Azure subscription with the permission to assign role assignments.

</div>

<div>

<div class="title">

Procedure

</div>

- To add the federated identity credentials to a user-assigned managed identity, run the following command, for example:

  > [!IMPORTANT]
  > When setting up the delegated scanning, set the subject to **system:serviceaccount:stackrox:sensor**.

  ``` terminal
  $ az identity federated-credential create \
      --name "${FEDERATED_CREDENTIAL_NAME}" \
      --identity-name "${MANAGED_IDENTITY_NAME}" \
      --resource-group "${RESOURCE_GROUP}" \
      --issuer "${OIDC_ISSUER_URL}" \
      --subject system:serviceaccount:stackrox:central \
      --audience openshift
  ```

  where:

  `--identity-name`  
  Specifies the identity name. The managed identity must have all the permissions for federation.

  `--issuer`  
  Specifies the issuer. The issuer must match the service account token issuer of the OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configure a user-assigned managed identity to trust an external identity provider](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation-create-trust-user-assigned-managed-identity?pivots=identity-wif-mi-methods-azp)

</div>
