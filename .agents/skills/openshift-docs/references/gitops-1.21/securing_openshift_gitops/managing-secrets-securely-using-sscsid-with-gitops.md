<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can integrate the Secrets Store Container Storage Interface (SSCSI) driver with the GitOps Operator in OpenShift Container Platform 4.14 and later to manage secrets securely.

# Overview of managing secrets using Secrets Store CSI driver with GitOps

Applications require sensitive information, such as passwords and usernames, which must be protected as a security best practice. If RBAC is not configured properly on your cluster, anyone with API or etcd access can retrieve or modify a secret.

> [!IMPORTANT]
> Anyone who is authorized to create a pod in a namespace can use that RBAC to read any secret in that namespace. With the SSCSI Driver Operator, you can use an external secrets store to store and provide sensitive information to pods securely.

> [!WARNING]
> Avoid modifying the `argocd-secret` secret that GitOps creates, using external secret management solutions such as the External Secrets Operator or Vault plugins. The `openshift-gitops-operator` manages this secret as part of its core functionality. If you modify this secret externally, it can cause reconciliation conflicts, unpredictable behavior, or disruption of Argo CD instances and GitOps workflows. To maintain consistency and reliability, allow the GitOps Operator to exclusively manage the `argocd-secret` secret.

## Benefits

Integrating the SSCSI driver with the GitOps Operator provides the following benefits:

- Prevent secrets from being stored in etcd by mounting them directly from external providers

- Reduce the risk of unauthorized access through centralized secret management

- Enable automatic secret rotation without modifying application code

# Secrets store providers

The following secrets store providers are available for use with the Secrets Store CSI Driver Operator:

- AWS Secrets Manager

- AWS Systems Manager Parameter Store

- Microsoft Azure Key Vault

- HashiCorp Vault

# Configure AWS Secrets Manager on OpenShift with GitOps

This guide provides instructions with examples to help you use GitOps workflows with the Secrets Store Container Storage Interface (SSCSI) Driver Operator to mount secrets from AWS Secrets Manager to a CSI volume in OpenShift Container Platform.

As an example, consider that you are using AWS Secrets Manager as your secrets store provider with the SSCSI Driver Operator. The following example shows the directory structure in GitOps repository that is ready to use the secrets from AWS Secrets Manager:

**Example directory structure in GitOps repository:**

    ├── config
    │   ├── argocd
    │   │   ├── argo-app.yaml
    │   │   ├── secret-provider-app.yaml
    │   │   ├── ...
    │   └── sscsid
    │       └── aws-provider.yaml
    ├── environments
    │   ├── dev
    │   │   ├── apps
    │   │   │   └── app-taxi
    │   │   │       ├── ...
    │   │   ├── credentialsrequest-dir-aws
    │   │   └── env
    │   │       ├── ...
    │   ├── new-env
    │   │   ├── ...

where:

`sscsid`
Specifies the directory that stores the `aws-provider.yaml` file.

`aws-provider.yaml`
Specifies the configuration file that installs the AWS Secrets Manager provider and deploys resources for it.

`secret-provider-app.yaml`
Specifies the configuration file that creates an application and deploys resources for AWS Secrets Manager.

`dev`
Specifies the directory that stores the deployment pod and credential requests.

`app-taxi`
Specifies the directory that stores the `SecretProviderClass` resources to define your secrets store provider.

`credentialsrequest-dir-aws`
Specifies the folder that stores the `credentialsrequest.yaml` file. This file contains the configuration for the credentials request to mount a secret to the deployment pod.

## Storing AWS Secrets Manager resources in GitOps repository

You can store AWS Secrets Manager configurations in the GitOps repository for declarative and version-controlled secret management.

> [!IMPORTANT]
> Using the SSCSI Driver Operator with AWS Secrets Manager is not supported in a hosted control plane cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster with `cluster-admin` privileges.

- You have access to the OpenShift Container Platform web console.

- You have extracted and prepared the `ccoctl` binary.

- You have installed the `jq` CLI tool.

- Your cluster is installed on AWS and uses AWS Security Token Service (STS).

- You have configured AWS Secrets Manager to store the required secrets.

- [SSCSI Driver Operator is installed on your cluster](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets-store.html#persistent-storage-csi-secrets-store-driver-install_nodes-pods-secrets-store).

- Red Hat OpenShift GitOps Operator is installed on your cluster.

- You have a GitOps repository ready to use the secrets.

- You are logged in to the Argo CD instance by using the Argo CD admin account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the AWS Secrets Manager provider and add resources:

    1.  In your GitOps repository, create a directory and add `aws-provider.yaml` file in it with the following configuration to deploy resources for the AWS Secrets Manager provider:

        > [!IMPORTANT]
        > The AWS Secrets Manager provider for the SSCSI driver is an upstream provider.
        >
        > This configuration is modified from the configuration provided in the upstream [AWS documentation](https://github.com/aws/secrets-store-csi-driver-provider-aws#installing-the-aws-provider) so that it works properly with OpenShift Container Platform. Changes to this configuration might impact functionality.

        **Example `aws-provider.yaml` file:**

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: csi-secrets-store-provider-aws
          namespace: openshift-cluster-csi-drivers
        ---
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRole
        metadata:
          name: csi-secrets-store-provider-aws-cluster-role
        rules:
        - apiGroups: [""]
          resources: ["serviceaccounts/token"]
          verbs: ["create"]
        - apiGroups: [""]
          resources: ["serviceaccounts"]
          verbs: ["get"]
        - apiGroups: [""]
          resources: ["pods"]
          verbs: ["get"]
        - apiGroups: [""]
          resources: ["nodes"]
          verbs: ["get"]
        ---
        apiVersion: rbac.authorization.k8s.io/v1
        kind: ClusterRoleBinding
        metadata:
          name: csi-secrets-store-provider-aws-cluster-rolebinding
        roleRef:
          apiGroup: rbac.authorization.k8s.io
          kind: ClusterRole
          name: csi-secrets-store-provider-aws-cluster-role
        subjects:
        - kind: ServiceAccount
          name: csi-secrets-store-provider-aws
          namespace: openshift-cluster-csi-drivers
        ---
        apiVersion: apps/v1
        kind: DaemonSet
        metadata:
          namespace: openshift-cluster-csi-drivers
          name: csi-secrets-store-provider-aws
          labels:
            app: csi-secrets-store-provider-aws
        spec:
          updateStrategy:
            type: RollingUpdate
          selector:
            matchLabels:
              app: csi-secrets-store-provider-aws
          template:
            metadata:
              labels:
                app: csi-secrets-store-provider-aws
            spec:
              serviceAccountName: csi-secrets-store-provider-aws
              hostNetwork: false
              containers:
                - name: provider-aws-installer
                  image: public.ecr.aws/aws-secrets-manager/secrets-store-csi-driver-provider-aws:1.0.r2-50-g5b4aca1-2023.06.09.21.19
                  imagePullPolicy: Always
                  args:
                      - --provider-volume=/etc/kubernetes/secrets-store-csi-providers
                  resources:
                    requests:
                      cpu: 50m
                      memory: 100Mi
                    limits:
                      cpu: 50m
                      memory: 100Mi
                  securityContext:
                    privileged: true
                  volumeMounts:
                    - mountPath: "/etc/kubernetes/secrets-store-csi-providers"
                      name: providervol
                    - name: mountpoint-dir
                      mountPath: /var/lib/kubelet/pods
                      mountPropagation: HostToContainer
              tolerations:
              - operator: Exists
              volumes:
                - name: providervol
                  hostPath:
                    path: "/etc/kubernetes/secrets-store-csi-providers"
                - name: mountpoint-dir
                  hostPath:
                    path: /var/lib/kubelet/pods
                    type: DirectoryOrCreate
              nodeSelector:
                kubernetes.io/os: linux
        ```

    2.  Add a `secret-provider-app.yaml` file in your GitOps repository to create an application and deploy resources for AWS Secrets Manager:

        **Example `secret-provider-app.yaml` file:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: secret-provider-app
          namespace: openshift-gitops
        spec:
          destination:
            namespace: openshift-cluster-csi-drivers
            server: https://kubernetes.default.svc
          project: default
          source:
            path: path/to/aws-provider/resources
            repoURL: https://github.com/<my-domain>/<gitops>.git
          syncPolicy:
            automated:
            prune: true
            selfHeal: true
        ```

        where:

        `spec.source.repoURL`
        Defines the repository URL value to point to your GitOps repository.

2.  Synchronize resources with the default Argo CD instance to deploy them in the cluster:

    1.  Add a label to the `openshift-cluster-csi-drivers` namespace your application is deployed in so that the Argo CD instance in the `openshift-gitops` namespace can manage it:

        ``` terminal
        $ oc label namespace openshift-cluster-csi-drivers argocd.argoproj.io/managed-by=openshift-gitops
        ```

    2.  Apply the resources in your GitOps repository to your cluster, including the `aws-provider.yaml` file you just pushed:

        **Example output:**

        ``` terminal
        application.argoproj.io/argo-app created
        application.argoproj.io/secret-provider-app created
        ...
        ```

        In the Argo CD UI, you can observe that the `csi-secrets-store-provider-aws` daemonset continues to synchronize resources. To resolve this issue, you must configure the SSCSI driver to mount secrets from the AWS Secrets Manager.

</div>

## Configuring SSCSI driver to mount secrets from AWS Secrets Manager

To store and manage your secrets securely, use GitOps workflows and configure the Secrets Store Container Storage Interface (SSCSI) Driver Operator to mount secrets from AWS Secrets Manager to a CSI volume in OpenShift Container Platform. For example, consider that you want to mount a secret to a deployment pod under the `dev` namespace which is in the `/environments/dev/` directory.

<div>

<div class="title">

Prerequisites

</div>

- You have the AWS Secrets Manager resources stored in your GitOps repository.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Grant privileged access to the `csi-secrets-store-provider-aws` service account by running the following command:

    ``` terminal
    $ oc adm policy add-scc-to-user privileged -z csi-secrets-store-provider-aws -n openshift-cluster-csi-drivers
    ```

    **Example output:**

    ``` terminal
    clusterrole.rbac.authorization.k8s.io/system:openshift:scc:privileged added: "csi-secrets-store-provider-aws"
    ```

2.  Grant permission to allow the service account to read the AWS secret object:

    1.  Create a `credentialsrequest-dir-aws` folder under a namespace-scoped directory in your GitOps repository because the credentials request is namespace-scoped. For example, create a `credentialsrequest-dir-aws` folder under the `dev` namespace which is in the `/environments/dev/` directory by running the following command:

        ``` terminal
        $ mkdir credentialsrequest-dir-aws
        ```

    2.  Create a YAML file with the following configuration for the credentials request in the `/environments/dev/credentialsrequest-dir-aws/` path to mount a secret to the deployment pod in the `dev` namespace:

        **Example `credentialsrequest.yaml` file:**

        ``` yaml
        apiVersion: cloudcredential.openshift.io/v1
        kind: CredentialsRequest
        metadata:
          name: aws-provider-test
          namespace: openshift-cloud-credential-operator
        spec:
          providerSpec:
            apiVersion: cloudcredential.openshift.io/v1
            kind: AWSProviderSpec
            statementEntries:
            - action:
              - "secretsmanager:GetSecretValue"
              - "secretsmanager:DescribeSecret"
              effect: Allow
              resource: "<aws_secret_arn>"
        secretRef:
          name: aws-creds
          namespace: dev
        serviceAccountNames:
          - default
        ```

        where:

        `metadata.namespace`
        Specifies the namespace for the secret reference. Update this value according to your project deployment setup.

        `spec.providerSpec.statementEntries[].resource`
        Specifies the ARN of your secret in the cluster region. The `<aws_region>` in `<aws_secret_arn>` must match the cluster region. If it does not match, replicate the secret in the cluster region.

        > [!TIP]
        > To find your cluster region, run the command:
        >
        > ``` terminal
        > $ oc get infrastructure cluster -o jsonpath='{.status.platformStatus.aws.region}'
        > ```
        >
        > **Example output:**
        >
        > ``` terminal
        > us-west-2
        > ```

    3.  Retrieve the OIDC provider by running the following command:

        ``` terminal
        $ oc get --raw=/.well-known/openid-configuration | jq -r '.issuer'
        ```

        **Example output:**

        ``` terminal
        https://<oidc_provider_name>
        ```

        Copy the OIDC provider name `<oidc_provider_name>` from the output to use in the next step.

    4.  Use the `ccoctl` tool to process the credentials request by running the following command:

        ``` terminal
        $ ccoctl aws create-iam-roles \
            --name my-role --region=<aws_region> \
            --credentials-requests-dir=credentialsrequest-dir-aws \
            --identity-provider-arn arn:aws:iam::<aws_account>:oidc-provider/<oidc_provider_name> \
            --output-dir=credrequests-ccoctl-output
        ```

        **Example output:**

        ``` terminal
        2023/05/15 18:10:34 Role arn:aws:iam::<aws_account_id>:role/my-role-my-namespace-aws-creds created
        2023/05/15 18:10:34 Saved credentials configuration to: credrequests-ccoctl-output/manifests/my-namespace-aws-creds-credentials.yaml
        2023/05/15 18:10:35 Updated Role policy for Role my-role-my-namespace-aws-creds
        ```

        Copy the `<aws_role_arn>` from the output to use in the next step. For example, `arn:aws:iam::<aws_account_id>:role/my-role-my-namespace-aws-creds`.

    5.  Check the role policy on AWS to confirm the `<aws_region>` of `"Resource"` in the role policy matches the cluster region:

        **Example role policy:**

        ``` json
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Effect": "Allow",
                    "Action": [
                        "secretsmanager:GetSecretValue",
                        "secretsmanager:DescribeSecret"
                    ],
                    "Resource": "arn:aws:secretsmanager:<aws_region>:<aws_account_id>:secret:my-secret-xxxxxx"
                }
            ]
        }
        ```

    6.  Bind the service account with the role ARN by running the following command:

        ``` terminal
        $ oc annotate -n <namespace> sa/<app_service_account> eks.amazonaws.com/role-arn="<aws_role_arn>"
        ```

        **Example command:**

        ``` terminal
        $ oc annotate -n dev sa/default eks.amazonaws.com/role-arn="<aws_role_arn>"
        ```

        **Example output:**

        ``` terminal
        serviceaccount/default annotated
        ```

3.  Create a namespace-scoped `SecretProviderClass` resource to define your secrets store provider. For example, you create a `SecretProviderClass` resource in `/environments/dev/apps/app-taxi/services/taxi/base/config` directory of your GitOps repository.

    1.  Create a `secret-provider-class-aws.yaml` file in the same directory where the target deployment is located in your GitOps repository:

        **Example `secret-provider-class-aws.yaml`:**

        ``` yaml
        apiVersion: secrets-store.csi.x-k8s.io/v1
        kind: SecretProviderClass
        metadata:
          name: my-aws-provider
          namespace: dev
        spec:
          provider: aws
          parameters:
            objects: |
              - objectName: "testSecret"
                objectType: "secretsmanager"
        ```

        where:

        `metadata.name`
        Specifies the name of the secret provider class.

        `metadata.namespace`
        Specifies the namespace for the secret provider class. The namespace must match the namespace of the resource which will use the secret.

        `spec.provider`
        Specifies the name of the secret store provider.

        `spec.parameters`
        Specifies the provider-specific configuration parameters.

        `spec.parameters.objects`
        Specifies the secret name you created in AWS.

    2.  Verify that after pushing this YAML file to your GitOps repository, the namespace-scoped `SecretProviderClass` resource is populated in the target application page in the Argo CD UI.

        > [!NOTE]
        > If the Sync Policy of your application is not set to `Auto`, you can manually sync the `SecretProviderClass` resource by clicking **Sync** in the Argo CD UI.

</div>

## Configuring GitOps managed resources to use mounted secrets

You must configure the GitOps managed resources by adding volume mounts configuration to a deployment and configuring the container pod to use the mounted secret.

<div>

<div class="title">

Prerequisites

</div>

- You have the AWS Secrets Manager resources stored in your GitOps repository.

- You have the Secrets Store Container Storage Interface (SSCSI) driver configured to mount secrets from AWS Secrets Manager.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the GitOps managed resources. For example, consider that you want to add volume mounts configuration to the deployment of `app-taxi` application and the `100-deployment.yaml` file is in the `/environments/dev/apps/app-taxi/services/taxi/base/config/` directory.

    1.  Add the volume mounting to the deployment YAML file and configure the container pod to use the secret provider class resources and mounted secret:

        **Example YAML file:**

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: taxi
          namespace: dev
        spec:
          replicas: 1
          template:
            metadata:
              # ...
            spec:
              serviceAccountName: default
              containers:
                - name: taxi
                  image: nginxinc/nginx-unprivileged:latest
                  imagePullPolicy: Always
                  ports:
                    - containerPort: 8080
                  volumeMounts:
                    - name: secrets-store-inline
                      mountPath: "/mnt/secrets-store"
                      readOnly: true
                  resources: {}
              volumes:
                - name: secrets-store-inline
                  csi:
                    driver: secrets-store.csi.k8s.io
                    readOnly: true
                    volumeAttributes:
                      secretProviderClass: "my-aws-provider"
        # ...
        ```

        where:

        `metadata.name`
        Specifies the name of the deployment.

        `metadata.namespace`
        Specifies the namespace where the deployment is created. This must match the namespace of the `SecretProviderClass`.

        `spec.replicas`
        Specifies the number of pod replicas for the deployment.

        `spec.template.spec.containers[].volumeMounts[].mountPath`
        Specifies the path inside the container where the secrets are mounted.

        `spec.template.spec.volumes[].csi.volumeAttributes.secretProviderClass`
        Specifies the name of the `SecretProviderClass` used to retrieve secrets from the external provider.

    2.  Push the updated resource YAML file to your GitOps repository.

2.  In the Argo CD UI, click **REFRESH** on the target application page to apply the updated deployment manifest.

3.  Verify that all the resources are successfully synchronized on the target application page.

4.  Verify that you can access the secrets from AWS Secrets manager in the pod volume mount:

    1.  List the secrets in the pod mount:

        ``` terminal
        $ oc exec <deployment_name>-<hash> -n <namespace> -- ls /mnt/secrets-store/
        ```

        **Example command:**

        ``` terminal
        $ oc exec taxi-5959644f9-t847m -n dev -- ls /mnt/secrets-store/
        ```

        **Example output:**

        ``` terminal
        <secret_name>
        ```

    2.  View a secret in the pod mount:

        ``` terminal
        $ oc exec <deployment_name>-<hash> -n <namespace> -- cat /mnt/secrets-store/<secret_name>
        ```

        **Example command:**

        ``` terminal
        $ oc exec taxi-5959644f9-t847m -n dev -- cat /mnt/secrets-store/testSecret
        ```

        **Example output:**

        ``` terminal
        <secret_value>
        ```

</div>

# Configure HashiCorp Vault as a secrets provider on OpenShift with GitOps

You can configure HashiCorp Vault as a secrets provider by using the Secrets Store CSI Driver Operator on the OpenShift Container Platform. When combined with GitOps workflows managed by Argo CD, this setup enables you to securely retrieve secrets from Vault and inject them into your applications running on OpenShift.

Structure the GitOps repository and configure the Vault CSI provider to integrate with the Secrets Store CSI Driver in OpenShift Container Platform.

The following sample GitOps repository layout is used for integrating Vault with your application.

**Example directory structure in GitOps repository:**

    ├── config
    │   ├── argocd
    │   │   ├── vault-secret-provider-app.yaml
    │   │   ├── ...
    │── environments
    │   ├── dev
    │   │   ├── apps
    │   │   │   ├── demo-app
    │   │   │       ├── manifest
    │   │   │       |    ├── secretProviderClass.yaml
    │   │   │       |    ├── serviceAccount.yaml
    │   │   │       |    ├── deployment.yaml
    │   │   │       ├── argocd
    │   │   │            ├── demo-app.yaml

where:

`config/argocd/`
Specifies the directory that stores Argo CD Application definitions for cluster-wide tools like the Vault CSI provider.

`environments/<env>/apps/<app-name>/manifest/`
Specifies the directory that contains Kubernetes manifests specific to an application in a particular environment.

`environments/<env>/apps/<app-name>/argocd/`
Specifies the directory that contains the Argo CD Application definition that deploys the application and its resources.

## Installing the Vault CSI Provider using GitOps

Install the Vault CSI provider by deploying an Argo CD Application that uses HashiCorp’s official Helm chart. This method follows GitOps best practices by managing the installation declaratively through a version-controlled Argo CD Application resource.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform cluster as an administrator.

- You have access to the OpenShift Container Platform web console.

- The [SSCSI Driver Operator](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets-store.html#persistent-storage-csi-secrets-store-driver-install_nodes-pods-secrets-store) is installed on your cluster.

- You installed [Red Hat OpenShift GitOps](../installing_gitops/installing-openshift-gitops.md#installing-openshift-gitops) on your OpenShift Container Platform cluster.

- You have a GitOps repository ready to use the secrets.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the Argo CD Application resource for the Vault CSI Provider.

    1.  Create an Argo CD Application resource to deploy the Vault CSI provider. Add this resource to your GitOps repository, for example, `config/argocd/vault-secret-provider-app.yaml`:

        **Example `vault-secret-provider-app.yaml` file:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: vault-secret-provider-app
          namespace: openshift-gitops
        spec:
          destination:
            namespace: vault-csi-provider
            server: https://kubernetes.default.svc
          project: default
          source:
            repoURL: https://helm.releases.hashicorp.com
            chart: vault
            targetRevision: 0.30.0
            helm:
              releaseName: vault
              values: |
                csi:
                  enabled: true
                server:
                  enabled: true
                  dataStorage:
                     enabled: false
                injector:
                  enabled: false
          syncPolicy:
            automated:
              prune: true
              selfHeal: true
            syncOptions:
            - CreateNamespace=true
          ignoreDifferences:
          - kind: DaemonSet
            group: apps
            jsonPointers:
              - /spec/template/spec/containers/0/securityContext/privileged
        ```

        > [!NOTE]
        > The `server.enabled: true` and `dataStorage.enabled: false` settings in the Helm values deploy a HashiCorp Vault server instance using ephemeral storage. This setup is suitable for development or testing environments. For production, you can enable `dataStorage` with a persistent volume (PV) or use an external Vault cluster and set `server.enabled` to `false`. If a Vault server is already deployed, you can set `server.enabled` to `false`.

2.  Apply the `vault-secret-provider-app.yaml` file from the GitOps repository to your cluster:

    ``` terminal
    $ oc apply -f vault-secret-provider-app.yaml
    ```

    After deploying the Vault CSI provider, the `vault-csi-provider` DaemonSet may fail to run. This issue occurs because OpenShift Container Platform restricts privileged containers by default. In addition, the Vault CSI provider and the Secrets Store CSI Driver require access to `hostPath` mounts, which OpenShift Container Platform blocks unless the pods run as privileged.

    1.  To resolve permission issues in OpenShift Container Platform:

        1.  Patch the `vault-csi-provider` DaemonSet to run its containers as privileged:

            ``` terminal
            $ oc patch daemonset vault-csi-provider -n vault-csi-provider --type=json --patch='[{"op":"add","path":"/spec/template/spec/containers/0/securityContext","value":{"privileged":true}}]
            ```

        2.  Grant the Secrets Store CSI Driver service account access to the privileged Security Context Constraints (SCC) in OpenShift Container Platform.

            ``` terminal
            $ oc adm policy add-scc-to-user privileged \
              system:serviceaccount:openshift-cluster-csi-drivers:secrets-store-csi-driver-operator
            ```

        3.  Grant the Vault CSI Provider service account access to the privileged Security Context Constraints (SCC) in OpenShift Container Platform.

            ``` terminal
            $ oc adm policy add-scc-to-user privileged \
            system:serviceaccount:vault-csi-provider:vault-csi-provider
            ```

            > [!NOTE]
            > If `server.enabled` is set to `true` in the Helm chart, the Vault server pods run with specific user IDs (UIDs) or group IDs (GIDs) that OpenShift Container Platform blocks by default.

        4.  Grant the Vault server service account the required Security Context Constraints (SCC) permissions.

            ``` terminal
            $ oc adm policy add-scc-to-user anyuid  system:serviceaccount:vault-csi-provider:vault
            ```

</div>

## Initializing and configuring Vault to store a Secret

After deploying Vault using Argo CD and applying the necessary SCC permissions and DaemonSet patches, initialize Vault, unseal it, and configure Kubernetes authentication to enable secure secret storage and access.

<div>

<div class="title">

Procedure

</div>

1.  Access the Vault Pod.

    1.  If Vault is running within your OpenShift Container Platform cluster, for example, as the `vault-0` pod in the `vault-csi-provider` namespace, run the following command to access the Vault CLI inside the pod:

        ``` terminal
        $ oc exec -it vault-0 -n vault-csi-provider -- /bin/sh
        ```

2.  Initialize Vault.

    1.  If your Vault instance is not yet initialized, run the following command:

        ``` terminal
        $ vault operator init
        ```

        As a result, the following output is displayed.

        ``` output
        5 Unseal Keys - required to unseal the Vault.
        Initial Root Token - required to log in and configure Vault.
        ```

        > [!IMPORTANT]
        > Store these credentials securely. At least 3 out of 5 unseal keys are required to unseal Vault. If the keys are lost, access to stored secrets is permanently blocked.

3.  Unseal Vault.

    1.  Vault starts in a sealed state. Run the following commands to use three of the five Unseal Keys obtained in the earlier step:

        ``` terminal
        $ vault operator unseal <Unseal Key 1>
        $ vault operator unseal <Unseal Key 2>
        $ vault operator unseal <Unseal Key 3>
        ```

        Once unsealed, the Vault becomes active and ready for use.

4.  Log into Vault.

    1.  To use the root token to log in to Vault, run the following command:

        ``` terminal
        $ vault login <Initial Root Token>
        ```

        This provides administrator access to enable and configure secret engines and authentication methods.

5.  Enable Kubernetes Authentication in Vault.

    1.  Run the following command to enable Kubernetes authentication in Vault.

        ``` terminal
        $ vault auth enable kubernetes
        ```

        This allows Kubernetes workloads, for example, pods, to authenticate with Vault using their service accounts.

6.  Configure Kubernetes authentication method in Vault.

    1.  To configure Vault for communicating with the Kubernetes API, run the following command:

        ``` terminal
        $ vault write auth/kubernetes/config \
          issuer="https://kubernetes.default.svc" \
          token_reviewer_jwt="$(cat /var/run/secrets/kubernetes.io/serviceaccount/token)" \
          kubernetes_host="https://${KUBERNETES_PORT_443_TCP_ADDR}:443" \
          kubernetes_ca_cert=@/var/run/secrets/kubernetes.io/serviceaccount/ca.crt
        ```

        As a result, the following output is displayed.

        ``` output
        Success! Data written to: auth/kubernetes/config
        ```

        where:

        - `<issuer>` is the name of the Kubernetes token issuer URL.

        - `<token_reviewer_jwt>` is a JSON Web Token (JWT) that Vault uses to call the Kubernetes `TokenReview` API and to validate service account tokens.

        - `<kubernetes_host>` is the URL that Vault uses to communicate with the Kubernetes API server.

        - `<kubernetes_ca_cert>` is the CA certificate that Vault uses for secure communication with the Kubernetes API server.

</div>

## Managing Secrets, Policies, and Roles in Vault

To create a secret in Vault, define a Vault policy and configure a Kubernetes authentication role that enables a Kubernetes workload to retrieve the secret securely.

<div>

<div class="title">

Procedure

</div>

1.  Enable the KV Secrets Engine.

    1.  Use the Key-Value (KV) Version 2 secrets engine to store arbitrary secrets with versioning support. Run the following command to enable the KV secrets engine at the path secret/:

        ``` terminal
        $ vault secrets enable -path=secret/ kv
        ```

2.  Store a secret in Vault.

    1.  Store a secret using the KV Version 2 secrets engine. Run the following command to store the secret data, username and password, at path `secret/demo/config`:

        ``` terminal
        $ vault kv put secret/demo/config username="demo-user" password="demo-pass"
        ```

3.  Create a Vault policy.

    1.  To create a policy that grants read access to the secret, run the following command:

        ``` terminal
        $ vault write auth/kubernetes/role/app \
          bound_service_account_names=demo-app-sa \
          bound_service_account_namespaces=demo-app \
          policies=demo-app-policy \
          ttl=24h
        ```

        This `demo-app-policy` grants read access to the secret at `secret/demo/config` and is later linked to a Kubernetes role.

4.  Create a Kubernetes Authentication Role in Vault.

    1.  To create a role that binds a Kubernetes service account to the Vault policy, run the following command.

        ``` terminal
        $ vault write auth/kubernetes/role/app \
          bound_service_account_names=demo-app-sa \
          bound_service_account_namespaces=demo-app \
          policies=demo-app-policy \
          ttl=24h
        ```

        This allows any pod using the service account to authenticate to Vault and retrieve the secret.

        where:

        - `<bound_service_account_names>` is the name of the Kubernetes service account that Vault trusts.

        - `<bound_service_account_namespaces>` is the name of the namespace where the service account is located.

        - `<policies>` is the name of the attached Vault policy.

        - `<ttl>` is the `Time-to-live` value issued for the token.

</div>

## Configuring GitOps managed resources to use Vault-mounted secrets

Securely inject secrets from HashiCorp Vault into GitOps-managed Kubernetes workloads using the Secrets Store CSI driver and Vault provider. The secrets are mounted as files in the pod’s filesystem, allowing applications to access the data without storing it in Kubernetes Secret objects.

<div>

<div class="title">

Procedure

</div>

1.  Creating the `SecretProviderClass`.

    1.  Create a `SecretProviderClass` resource in the application’s manifest directory for example, `environments/dev/apps/demo-app/manifest/secretProviderClass.yaml`. This resource defines how the Secrets Store CSI driver retrieves secrets from Vault.

        **Example `secretProviderClass.yaml` file:**

        ``` yaml
        apiVersion: secrets-store.csi.x-k8s.io/v1
        kind: SecretProviderClass
        metadata:
          name: demo-app-creds
          namespace: demo-app
        spec:
          provider: vault
          parameters:
            vaultAddress: http://vault.vault-csi-provider:8200 # <name>.<namespace>:port
            roleName: app
            objects: |
              - objectName: "demoAppUsername"
                secretPath: "secret/demo/config"
                secretKey: "username"
              - objectName: "demoAppPassword"
                secretPath: "secret/demo/config"
                secretKey: "password"
        ---
        ```

        where:

        `<spec.provider>`
        Specifies the name of the HashiCorp Vault.

        `<spec.parameters.vaultAddress>`
        Specifies the network address of the Vault server. Adjust this based on your Vault setup, such as, in-cluster service or an external URL.

        `<spec.parameters.roleName>`
        Specifies the Vault Kubernetes authentication role used by the application Service Account. Describes an array that defines which secrets to retrieve and how to map them to file names. `<spec.objects>` - Specifies an array that defines which secrets to retrieve and how to map them to file names. The `secretPath` for KV v2 includes `/data/`.

2.  Create an Application, such as, `ServiceAccount`.

    1.  Create a Kubernetes `ServiceAccount` for the application workload. The `ServiceAccount` name must match the `bound_service_account_names` value defined in the Vault Kubernetes authentication role. Store the manifest in the GitOps repository, for example, `environments/dev/apps/demo-app/manifest/serviceAccount.yaml`.

        **Example `ServiceAccount.yaml` file:**

        ``` yaml
        apiVersion: v1
        kind: ServiceAccount
        metadata:
          name: demo-app-sa
          namespace: demo-app
        ```

3.  Create the Application deployment:

    1.  Modify the application’s deployment to use the designated `ServiceAccount` and mount secrets using the CSI volume. Store the updated manifest in the GitOps repository, for example, `environments/dev/apps/demo-app/manifest/deployment.yaml`:

        **Example `deployment.yaml` file:**

        ``` yaml
        apiVersion: apps/v1
        kind: Deployment
        metadata:
          name: app
          namespace: demo-app
          labels:
            app: demo
        spec:
          replicas: 1
          selector:
            matchLabels:
              app: demo
          template:
            metadata:
              labels:
                app: demo
            spec:
              serviceAccountName: demo-app-sa
              containers:
                - name: app
                  image: nginxinc/nginx-unprivileged:latest
                  volumeMounts:
                    - name: vault-secrets
                      mountPath: /mnt/secrets-store
                      readOnly: true
              volumes:
                - name: vault-secrets
                  csi:
                    driver: secrets-store.csi.k8s.io
                    readOnly: true
                    volumeAttributes:
                      secretProviderClass: demo-app-creds
        ```

        where:

        `spec.template.spec.serviceAccountName`
        Specifies the Kubernetes `ServiceAccount`, for example `demo-app-sa`, used by the application pod. This service account is used to authenticate with HashiCorp Vault through the configured Vault role.

        `spec.template.spec.containers[].volumeMounts[]`
        Specifies the volume mount that exposes secrets inside the container at the `/mnt/secrets-store` directory.

        `spec.template.spec.volumes[]`
        Defines the `vault-secrets` volume using the `secrets-store.csi.k8s.io` CSI driver and references the `demo-app-creds` `SecretProviderClass` to retrieve secrets from Vault.

4.  Define the Argo CD application for the workload:

    1.  Define an Argo CD application resource to deploy application components such as `ServiceAccount`, `SecretProviderClass`, and `Deployment` from the GitOps repository. Store the Argo CD manifest in a directory location, such as, `environments/dev/apps/demo-app/argocd/demo-app.yaml`.

        **Example `demo-app.yaml` file:**

        ``` yaml
        apiVersion: argoproj.io/v1alpha1
        kind: Application
        metadata:
          name: demo-app
          namespace: openshift-gitops
        spec:
          project: default
          source:
            repoURL: https://your-git-repo-url.git
            targetRevision: HEAD
            path: environments/dev/apps/demo-app/manifest
          destination:
            server: https://kubernetes.default.svc
            namespace: demo-app
          syncPolicy:
            automated:
              prune: true
              selfHeal: true
            syncOptions:
              - CreateNamespace=true
        ```

</div>

## Verifying secret injection

Verify the secret injection to ensure that Vault contains the expected values.

<div>

<div class="title">

Procedure

</div>

1.  Check the Pod status.

    1.  After the Argo CD Application has synced and all the resources are deployed, verify that the application pod is running successfully in the `demo-app` namespace. Run the following command:

        ``` terminal
        $ oc get pods -n demo-app
        ```

2.  Open the Shell session.

    1.  Use the name of the application pod to open a shell session. Replace `<your-app-pod-name>` with the actual pod name.

        ``` terminal
        $ oc exec -it <your-app-pod-name> -n demo-app -- sh
        ```

3.  Verify mounted secrets.

    1.  To verify that the secrets are mounted at the expected path, run the following commands:

        ``` terminal
        $ ls -l /mnt/secrets-store
        $ cat /mnt/secrets-store/demoAppUsername
        $ cat /mnt/secrets-store/demoAppPassword
        ```

        Verify that the mounted secret files `demoAppUsername` and `demoAppPassword` contain the expected values from Vault.

</div>

# Additional resources

- [Obtaining the `ccoctl` tool](https://github.com/redhat-developer/gitops-operator/blob/bfdf81944ea60b1d62d7de7c223c3bea3e7363a6/docs/Integrate%20GitOps%20with%20Secrets%20Management.md#obtain-the-ccoctl-tool)

- [About the Cloud Credential Operator](https://docs.openshift.com/container-platform/latest/authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.html)

- [Determining the Cloud Credential Operator mode](https://docs.openshift.com/container-platform/latest/authentication/managing_cloud_provider_credentials/about-cloud-credential-operator.html#cco-determine-mode_about-cloud-credential-operator)

- [Configure your AWS cluster to use AWS STS](https://github.com/redhat-developer/gitops-operator/blob/bfdf81944ea60b1d62d7de7c223c3bea3e7363a6/docs/Integrate%20GitOps%20with%20Secrets%20Management.md#configure-your-aws-cluster-to-use-aws-security-token-service-sts)

- [Configuring AWS Secrets Manager to store the required secrets](https://docs.aws.amazon.com/secretsmanager/latest/userguide/create_secret.html)

- [About the Secrets Store CSI Driver Operator](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets-store.html#persistent-storage-csi-secrets-store-driver-overview_nodes-pods-secrets-store)

- [Mounting secrets from an external secrets store to a CSI volume](https://docs.openshift.com/container-platform/latest/nodes/pods/nodes-pods-secrets-store.html#mounting-secrets-external-secrets-store)
