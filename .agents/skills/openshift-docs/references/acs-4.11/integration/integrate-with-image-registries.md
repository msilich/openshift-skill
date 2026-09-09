<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) integrates with a variety of image registries so that you can understand your images and apply security policies for image usage.

When you integrate with image registries, you can view important image details, such as image creation date and Dockerfile details (including image layers).

After you integrate RHACS with your registry, you can scan images, view image components, and apply security policies to images before or after deployment.

> [!NOTE]
> When you integrate with an image registry, RHACS does not scan all images in your registry. RHACS only scans the images when you:
>
> - Use the images in deployments
>
> - Use the `roxctl` CLI to check images
>
> - Use a continuous integration (CI) system to enforce security policies

You can integrate RHACS with major image registries, including:

- [Amazon Elastic Container Registry (ECR)](https://aws.amazon.com/ecr/)

- [Docker Hub](https://hub.docker.com)

- [Google Container Registry (GCR)](https://cloud.google.com/container-registry/)

- [Google Artifact Registry](https://cloud.google.com/artifact-registry/)

- [IBM Cloud Container Registry (ICR)](https://www.ibm.com/cloud/container-registry)

- [JFrog Artifactory](https://jfrog.com/artifactory/)

- [Microsoft Azure Container Registry (ACR)](https://azure.microsoft.com/en-au/services/container-registry/)

- [Red Hat Quay](https://quay.io)

- [Red Hat container registries](https://access.redhat.com/RegistryAuthentication#red-hat-registries-1)

- [Sonatype Nexus](https://www.sonatype.com/nexus-repository-sonatype)

- [GitHub container registry (GHCR)](https://docs.github.com/en/packages)

- Any other registry that uses the [Docker Registry HTTP API](https://docs.docker.com/registry/spec/api/)

<a id="automatic-configuration-image-registry_integrate-with-image-registries"></a>

# Automatic configuration

Red Hat Advanced Cluster Security for Kubernetes includes default integrations with standard registries, such as Docker Hub and others. It can also automatically configure integrations based on artifacts found in the monitored clusters, such as image pull secrets. Usually, you do not need to configure registry integrations manually.

<div class="important">

<div class="title">

</div>

- If you use a Google Container Registry (GCR), Red Hat Advanced Cluster Security for Kubernetes does not create a registry integration automatically.

- If you use Red Hat Advanced Cluster Security Cloud Service, automatic configuration is unavailable, and you must manually create registry integrations.

</div>

<a id="amazon_ecr_integrate-with-image-registries"></a>

# Amazon ECR integrations

For Amazon ECR integrations, Red Hat Advanced Cluster Security for Kubernetes automatically generates ECR registry integrations if the following conditions are met:

- The cloud provider for the cluster is AWS.

- The nodes in your cluster have an Instance Identity and Access Management (IAM) Role association and the Instance Metadata Service is available in the nodes. For example, when using Amazon Elastic Kubernetes Service (EKS) to manage your cluster, this role is known as the EKS Node IAM role.

- The Instance IAM role has IAM policies granting access to the ECR registries from which you are deploying.

If the listed conditions are met, Red Hat Advanced Cluster Security for Kubernetes monitors deployments that pull from ECR registries and automatically generates ECR integrations for them. You can edit these integrations after they are automatically generated.

<a id="manual-configuration-image-registry"></a>

# Manually configuring image registries

If you are using GCR, you must manually create image registry integrations.

<a id="manual-configuration-image-registry-ocp_integrate-with-image-registries"></a>

## Manually configuring OpenShift Container Platform registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes with OpenShift Container Platform built-in container image registry.

<div>

<div class="title">

Prerequisites

</div>

- You need a username and a password for authentication with the OpenShift Container Platform registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Generic Docker Registry**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **Username** and **Password**.

5.  If you are not using a TLS certificate when connecting to the registry, select **Disable TLS certificate validation (insecure)**.

6.  Select **Create integration without testing** to create the integration without testing the connection to the registry.

7.  Select **Test** to test that the integration with the selected registry is working.

8.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-ecr_integrate-with-image-registries"></a>

## Manually configuring Amazon Elastic Container Registry

You can use Red Hat Advanced Cluster Security for Kubernetes to create and modify Amazon Elastic Container Registry (ECR) integrations manually. If you are deploying from Amazon ECR, integrations for the Amazon ECR registries are usually automatically generated. However, you might want to create integrations on your own to scan images outside deployments. You can also modify the parameters of an automatically-generated integration. For example, you can change the authentication method used by an automatically-generated Amazon ECR integration to use AssumeRole authentication or other authorization models.

> [!IMPORTANT]
> To erase changes you made to an automatically-generated ECR integration, delete the integration, and Red Hat Advanced Cluster Security for Kubernetes creates a new integration for you with the automatically-generated parameters when you deploy images from Amazon ECR.

<div>

<div class="title">

Prerequisites

</div>

- You must have an Amazon Identity and Access Management (IAM) access key ID and a secret access key. Alternatively, you can use a node-level IAM proxy such as `kiam` or `kube2iam`.

- The access key must have read access to ECR. See [How do I create an AWS access key?](https://aws.amazon.com/premiumsupport/knowledge-center/create-access-key/) for more information.

- If you are running Red Hat Advanced Cluster Security for Kubernetes in Amazon Elastic Kubernetes Service (EKS) and want to integrate with an ECR from a separate Amazon account, you must first set a repository policy statement in your ECR. Follow the instructions at [Setting a repository policy statement](https://docs.aws.amazon.com/AmazonECR/latest/userguide/set-repository-policy.html) and for **Actions**, choose the following scopes of the Amazon ECR API operations:

  - ecr:BatchCheckLayerAvailability

  - ecr:BatchGetImage

  - ecr:DescribeImages

  - ecr:GetDownloadUrlForLayer

  - ecr:ListImages

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Amazon ECR**.

3.  Click **New integration**, or click one of the automatically-generated integrations to open it, then click **Edit**.

4.  Enter or modify the details for the following fields:

    1.  **Update stored credentials**: Clear this box if you are modifying an integration without updating the credentials such as access keys and passwords.

    2.  **Integration name**: The name of the integration.

    3.  **Registry ID**: The ID of the registry.

    4.  **Endpoint**: The address of the registry. This value is required only if you are using a private virtual private cloud (VPC) endpoint for Amazon ECR. This field is not enabled when the AssumeRole option is selected.

    5.  **Region**: The region for the registry; for example, `us-west-1`.

5.  If you are using IAM, select **Use Container IAM role**. Otherwise, clear the **Use Container IAM role** box and enter the **Access key ID** and **Secret access key**.

6.  If you are using AssumeRole authentication, select **Use AssumeRole** and enter the details for the following fields:

    1.  **AssumeRole ID**: The ID of the role to assume.

    2.  **AssumeRole External ID** (optional): If you are using an [external ID with AssumeRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html), you can enter it here.

7.  Select **Create integration without testing** to create the integration without testing the connection to the registry.

8.  Select **Test** to test that the integration with the selected registry is working.

9.  Select **Save**.

</div>

<a id="use-assumerole-with-ecr"></a>

### Using assumerole with Amazon ECR

You can use [AssumeRole](https://docs.aws.amazon.com/STS/latest/APIReference/API_AssumeRole.html) to grant access to AWS resources without manually configuring each user’s permissions. Instead, you can define a role with the desired permissions so that the user is granted access to assume that role. `AssumeRole` enables you to grant, revoke, or otherwise generally manage more fine-grained permissions.

<a id="configuring-assumerole-with-iam_integrate-with-image-registries"></a>

#### Configuring AssumeRole with container IAM

Before you can use AssumeRole with Red Hat Advanced Cluster Security for Kubernetes, you must first configure it.

<div>

<div class="title">

Procedure

</div>

1.  Enable the IAM OIDC provider for your EKS cluster:

    ``` terminal
    $ eksctl utils associate-iam-oidc-provider --cluster <cluster name> --approve
    ```

2.  [Create an IAM role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) for your EKS cluster.

3.  Associate the newly created role with a service account:

    ``` terminal
    $ kubectl -n stackrox annotate sa central eks.amazonaws.com/role-arn=arn:aws:iam::67890:role/<role-name>
    ```

4.  Restart Central to apply the changes.

    ``` terminal
    $ kubectl -n stackrox delete pod -l app=central
    ```

5.  Assign the role to a policy that allows the role to assume another role as required:

    ``` json
    {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "VisualEditor0",
                "Effect": "Allow",
                "Action": "sts:AssumeRole",
                "Resource": "arn:aws:iam::<ecr-registry>:role/<assumerole-readonly>"
            }
        ]
    }
    ```

    where:

    `<assumerole-readonly>`  
    Specifies the role you want to assume.

6.  Update the trust relationship for the role you want to assume:

    ``` json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::<ecr-registry>:role/<role-name>"
            ]
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```

    where:

    `<role-name>`  
    Specifies the role name, which should match with the new role you have created earlier.

</div>

<a id="configuring-assumerole-without-iam_integrate-with-image-registries"></a>

#### Configuring AssumeRole without container IAM

To use AssumeRole without container IAM, you must use an access and a secret key to authenticate as an [AWS user with programmatic access](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

<div>

<div class="title">

Procedure

</div>

1.  Depending on whether the AssumeRole user is in the same account as the ECR registry or in a different account, you must either:

    - Create a new role with the desired permissions if the user for which you want to assume role is in the same account as the ECR registry.

      > [!NOTE]
      > When creating the role, you can choose any trusted entity as required. However, you must modify it after creation.

    - Or, you must provide permissions to access the ECR registry and define its trust relationship if the user is in a different account than the ECR registry:

      ``` json
      {
          "Version": "2012-10-17",
          "Statement": [
              {
                  "Sid": "VisualEditor0",
                  "Effect": "Allow",
                  "Action": "sts:AssumeRole",
                  "Resource": "arn:aws:iam::<ecr-registry>:role/<assumerole-readonly>"
              }
          ]
      }
      ```

      where:

      `<assumerole-readonly>`  
      Specifies the role you want to assume.

2.  Configure the trust relationship of the role by including the user ARN under the **Principal** field:

    ``` json
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Effect": "Allow",
          "Principal": {
            "AWS": [
              "arn:aws:iam::<ecr-registry>:user/<role-name>"
            ]
          },
          "Action": "sts:AssumeRole"
        }
      ]
    }
    ```

</div>

<a id="configuring-assumerole-acs_integrate-with-image-registries"></a>

#### Configuring AssumeRole in RHACS

After configuring AssumeRole in ECR, you can integrate Red Hat Advanced Cluster Security for Kubernetes with Amazon Elastic Container Registry (ECR) by using AssumeRole.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Amazon ECR**.

3.  Click **New Integration**.

4.  Enter the details for the following fields:

    1.  **Integration Name**: The name of the integration.

    2.  **Registry ID**: The ID of the registry.

    3.  **Region**: The region for the registry; for example, `us-west-1`.

5.  If you are using IAM, select **Use container IAM role**. Otherwise, clear the **Use custom IAM role** box and enter the **Access key ID** and **Secret access key**.

6.  If you are using AssumeRole, select **Use AssumeRole** and enter the details for the following fields:

    1.  **AssumeRole ID**: The ID of the role to assume.

    2.  **AssumeRole External ID** (optional): If you are using an [external ID with AssumeRole](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user_externalid.html), you can enter it here.

7.  Select **Test** to test that the integration with the selected registry is working.

8.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-gcr_integrate-with-image-registries"></a>

## Manually configuring Google Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes (RHACS) with Google Container Registry (GCR).

<div>

<div class="title">

Prerequisites

</div>

- You have a workload identity or service account key for authentication.

  For more information, see [Authenticate to Google Cloud APIs from GKE workloads](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) (Google Cloud documentation).

- You have access to the registry for the associated service account.

  For more information, see [Access control with IAM](https://cloud.google.com/container-registry/docs/access-control) (Google Cloud documentation).

- You have granted the following roles to the service account, if you use GCR Container Analysis:

  - Container Analysis Notes Viewer

  - Container Analysis Occurrences Viewer

  - Storage Object Viewer

    For more information, see [Container analysis and vulnerability scanning](https://cloud.google.com/container-registry/docs/container-analysis) (Google Cloud documentation).

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Integrations**.

2.  In the **Image Integrations** section, click **Google Container Registry**.

3.  To create a new integration, click **New integration**.

4.  Enter a name for your integration.

5.  Choose the appropriate type of integration that you want to configure:

    - To configure an integration that includes the container image registry, select **Registry**.

    - To configure an integration that includes Scanner, select **Scanner**.

    - To configure an integration that includes the container image registry and Scanner, select **Registry+Scanner**.

6.  Enter the address of your registry.

7.  Optional: Enter the name of your Google Cloud project. RHACS matches the images against the project of the registry. If you do not specify the project name, RHACS matches the images against all the projects.

8.  Optional: Select the **Use workload identity** checkbox to authenticate by using a workload identity.

9.  Enter your service account key for authentication.

10. Optional: Select the **Create integration without testing** checkbox to create your integration without testing the connection to the registry.

11. Optional: To test your integration with the selected registry, click **Test**.

12. To save your integration, click **Save**.

</div>

<a id="manual-configuration-image-registry-gar_integrate-with-image-registries"></a>

## Manually configuring Google Artifact Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes (RHACS) with the Google Artifact Registry (GAR).

<div>

<div class="title">

Prerequisites

</div>

- You have a workload identity or service account key for authentication.

  For more information, see [Authenticate to Google Cloud APIs from GKE workloads](https://cloud.google.com/kubernetes-engine/docs/how-to/workload-identity) (Google Cloud documentation).

- You have the artifact registry reader Identity and Access Management (IAM) role, `roles/artifactregistry.reader` for the associated service account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Integrations**.

2.  In the **Image Integrations** section, click **Google Artifact Registry**.

3.  To create a new integration, click **New integration**.

4.  Enter a name for your integration.

5.  Enter the address of your registry.

6.  Optional: Enter the name of your Google Cloud project. RHACS matches the images against the project of the registry. If you do not specify the project name, RHACS matches the images against all the projects.

7.  Optional: Select the **Use workload identity** checkbox to authenticate by using a workload identity.

8.  Enter your service account key for authentication.

9.  Optional: Select the **Create integration without testing** checkbox to create your integration without testing the connection to the registry.

10. Optional: To test your integration with the selected registry, click **Test**.

11. To save your integration, click **Save**.

</div>

<a id="manual-configuration-image-registry-acr_integrate-with-image-registries"></a>

## Manually configuring Microsoft Azure Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes with Microsoft Azure Container Registry.

<div>

<div class="title">

Prerequisites

</div>

- You have either an Azure managed or Azure workload identity.

  For more information about Azure managed identities, see [What are managed identities for Azure resources?](https://learn.microsoft.com/en-us/entra/identity/managed-identities-azure-resources/overview) (Microsoft Azure documentation).

  For more information about Azure workload identities, see [Workload identity federation](https://learn.microsoft.com/en-us/entra/workload-id/workload-identity-federation) (Microsoft Azure documentation).

- You have the **Reader** role for the identity over a scope that includes the container registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Microsoft Azure Container Registry**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **Username** and **Password**.

    4.  Optional: Select the **Use workload identity** checkbox, if you want to authenticate by using an Azure managed or workload identity.

5.  Select **Create integration without testing** to create the integration without testing the connection to the registry.

6.  Select **Test** to test that the integration with the selected registry is working.

7.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-jfrog_integrate-with-image-registries"></a>

## Manually configuring JFrog Artifactory

You can integrate Red Hat Advanced Cluster Security for Kubernetes with JFrog Artifactory.

<div>

<div class="title">

Prerequisites

</div>

- You must have a username and a password for authentication with JFrog Artifactory.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **JFrog Artifactory**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **Username** and **Password**.

5.  If you are not using a TLS certificate when connecting to the registry, select **Disable TLS certificate validation (insecure)**.

6.  Select **Create integration without testing** to create the integration without testing the connection to the registry.

7.  Select **Test** to test that the integration with the selected registry is working.

8.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-qcr_integrate-with-image-registries"></a>

## Manually configuring Quay Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes (RHACS) with Quay Container Registry. You can integrate with Quay by using the following methods:

- Integrating with the Quay public repository (registry): This method does not require authentication.

- Integrating with a Quay private registry:

  - By using a username and password: This method accepts either your Quay.io account credentials or Quay robot account credentials.

    For information about robot accounts, see the "Red Hat Quay Robot Account overview" topic in Quay documentation.

  - By using keyless authentication with external secret: This method uses OIDC federation and the External Secrets Operator (ESO). For more information, see "Enabling Quay registry keyless authentication using external secret".

- Integrating with Quay to use the Quay scanner rather than the RHACS scanner: This method uses the API and requires an OAuth token for authentication. For more information, see "Integrating with Quay Container Registry to scan images" in the "Additional resources" section.

<div>

<div class="title">

Prerequisites

</div>

- For authentication with a Quay private registry, you need either your Quay.io account credentials or Quay robot account credentials.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Red Hat Quay.io**.

3.  Click **New integration**.

4.  Enter the **Integration name.**

5.  Enter the **Endpoint**, or the address of the registry.

    1.  If you are integrating with the Quay public repository, under **Type**, select **Registry**, and then go to the next step.

    2.  If you are integrating with a Quay private registry, under **Type**, select **Registry** and enter information in the following fields:

        - **Username** and **Password**: To access the registry, enter your Quay.io account credentials or Quay robot account credentials. Both credential types are valid. If you are using a robot account, enter the user name in the format `<namespace>+<accountname>`.

        - **OAuth token**: An OAuth token is not required for a **Registry** type integration and is deprecated for registry access. Provide an OAuth token only if you are integrating with the Quay scanner. For more information, see "Integrating with Quay Container Registry to scan images".

6.  Optional: If you are not using a TLS certificate when connecting to the registry, select **Disable TLS certificate validation (insecure)**.

7.  Optional: To create the integration without testing, select **Create integration without testing**.

8.  Select **Save**.

</div>

> [!NOTE]
> If you are editing a Quay integration but do not want to update your credentials, verify that **Update stored credentials** is not selected.

<div>

<div class="title">

Additional resources

</div>

- [Integrating with Quay Container Registry to scan images](integrate-with-image-vulnerability-scanners.md#integrate-with-qcr-scanner_integrate-with-image-vulnerability-scanners)

- [Red Hat Quay Robot Account overview](https://docs.redhat.com/en/documentation/red_hat_quay/3.18/html/about_quay_io/allow-robot-access-user-repo)

- [External Secrets Operator - Quay](https://external-secrets.io/latest/api/generator/quay/)

</div>

<a id="quay-keyless-eso_integrate-with-image-registries"></a>

## Enabling Quay registry keyless authentication using external secret

For validating images stored in Quay private registries, you can configure RHACS to use keyless authentication with Red Hat Quay registries. This method uses the External Secrets Operator (ESO) and OpenID Connect (OIDC) federation.

<div>

<div class="title">

Prerequisites

</div>

- You have enabled delegated scanning in RHACS. For more information, see "Accessing delegated image scanning" in the "Additional resources" section.

- The Central endpoint configured for the Secured Cluster `centralEndpoint: central.stackrox:443` or similar.

- A robot account created in Red Hat Quay with OIDC federation configured.

  - The issuer URL in the Quay robot identity federation configuration must match the service account token issuer of your OpenShift Container Platform cluster.

  - The `sub claim` subject must match the service account name and namespace that you configure in your cluster.

  See the [Red Hat Quay Robot Account overview](https://docs.redhat.com/en/documentation/red_hat_quay/latest/html/about_quay_io/allow-robot-access-user-repo) topic in Quay documentation for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In your Quay instance, navigate to your robot account settings and configure OIDC federation.

    Ensure the **Issuer URL** and **Subject** fields are correctly set to match your OpenShift Container Platform service account that ESO uses. See the [Setting up robot account federation](https://docs.redhat.com/en/documentation/red_hat_quay/latest/html/about_quay_io/allow-robot-access-user-repo#setting-robot-federation) topic in the Red Hat Quay documentation for more information.

2.  If ESO is not already present in your cluster, install it using Helm or another preferred method.

    ``` terminal
    $ helm repo add external-secrets https://charts.external-secrets.io
    helm install external-secrets \
      external-secrets/external-secrets \
      -n external-secrets \
      --create-namespace
    ```

3.  Define and apply the following Kubernetes resources. This example creates a `ServiceAccount` resource, a `QuayAccessToken` generator resource provided by the ESO installation, and an `ExternalSecret` resource that uses the generator to create a `kubernetes.io/dockerconfigjson` secret in the specified namespace.

    > [!IMPORTANT]
    > Update the `robotAccount` field in the `QuayAccessToken` resource to match the name of your Quay robot account.

    ``` yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: quay
      namespace: quay
    ---
    apiVersion: generators.external-secrets.io/v1alpha1
    kind: QuayAccessToken
    metadata:
      name: quay-token
      namespace: quay
    spec:
      url: quay.io
      robotAccount: keyless+account #
      serviceAccountRef:
        name: quay
        namespace: quay
    ---
    apiVersion: external-secrets.io/v1beta1
    kind: ExternalSecret
    metadata:
      name: quay-credentials
      namespace: quay
    spec:
      dataFrom:
      - sourceRef:
          generatorRef:
            apiVersion: generators.external-secrets.io/v1alpha1
            kind: QuayAccessToken
            name: quay-token
      refreshInterval: 55m
      target:
        name: quay-credentials
        template:
          type: kubernetes.io/dockerconfigjson
          data:
            .dockerconfigjson: |
              {
                "auths": {
                  "{{ .registry }}": {
                    "auth": "{{ .auth }}"
                  }
                }
              }
    ```

    where:

    `spec.robotAccount`  
    Specifies the actual name of your Quay robot account.

    <div>

    <div class="title">

    Verification

    </div>

    - Confirm that ESO has successfully created a secret named `quay-credentials` of type `kubernetes.io/dockerconfigjson` in the specified namespace.

      ``` terminal
      $ kubectl get secret quay-credentials -n quay -o yaml
      ```

      The keyless authentication method supports image scanning by using **delegated scanning**.

    - Use delegated image scanning by running the following command:

      ``` terminal
      $ roxctl image scan <image_name> --namespace=<namespace_where_secret_exists>
      ```

      where:

      `<image_name>`  
      Specifies the image name.

      `<namespace_where_secret_exists>`  
      Specifies the namespace where you created the secret.

    </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Accessing delegated image scanning](../operating/examine-images-for-vulnerabilities.md#accessing-delegated-image-scanning_examine-images-for-vulnerabilities).

</div>

<a id="manual-configuration-image-registry-ghcr_integrate-with-image-registries"></a>

## Manually configuring GitHub Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes with GitHub Container Registry (GHCR).

<div>

<div class="title">

Prerequisites

</div>

- You need a GitHub account and personal access token with at least `packages:read` permissions. See [Working with the Container registry](https://docs.github.com/en/packages/working-with-a-github-packages-registry/working-with-the-container-registry) for more information.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  In the **Image Integrations** section, select **GitHub Container Registry**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **Username**: The GitHub username. Leave blank for anonymous access.

    4.  **GitHub Token**: The GitHub personal access token. Leave blank for anonymous access.

5.  Select **Create integration without testing** to create the integration without testing the connection to the registry. Enable this option to allow anonymous access.

6.  Select **Test** to test that the integration with the selected registry is working.

7.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-ibm_integrate-with-image-registries"></a>

## Manually configuring IBM Cloud Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes with IBM Cloud Container Registry.

<div>

<div class="title">

Prerequisites

</div>

- You must have an API key for authentication with the IBM Cloud Container Registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **IBM Cloud Container Registry**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **API key**.

5.  Select **Test** to test that the integration with the selected registry is working.

6.  Select **Save**.

</div>

<a id="manual-configuration-image-registry-redhat_integrate-with-image-registries"></a>

## Manually configuring Red Hat Container Registry

You can integrate Red Hat Advanced Cluster Security for Kubernetes with Red Hat Container Registry.

<div>

<div class="title">

Prerequisites

</div>

- You must have a username and a password for authentication with the Red Hat Container Registry.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integrations** section, select **Red Hat Registry**.

3.  Click **New integration**.

4.  Enter the details for the following fields:

    1.  **Integration name**: The name of the integration.

    2.  **Endpoint**: The address of the registry.

    3.  **Username** and **Password**.

5.  Select **Create integration without testing** to create the integration without testing the connection to the registry.

6.  Select **Test** to test that the integration with the selected registry is working.

7.  Select **Save**.

</div>
