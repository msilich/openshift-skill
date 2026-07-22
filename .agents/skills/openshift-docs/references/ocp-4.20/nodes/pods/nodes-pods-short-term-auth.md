<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Some OpenShift Container Platform clusters use [short-term security credentials for individual components](../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.md#cco-short-term-creds) that are created and managed outside the cluster. Applications in customer workloads on these clusters can authenticate by using the short-term authentication method that the cluster uses.

# Configuring short-term authentication for workloads

To use this authentication method in your applications, you must complete the following steps:

1.  Create a federated identity service account in the Identity and Access Management (IAM) settings for your cloud provider.

2.  Create an OpenShift Container Platform service account that can impersonate a service account for your cloud provider.

3.  Configure any workloads related to your application to use the OpenShift Container Platform service account.

## Environment and user access requirements

To configure this authentication method, you must meet the following requirements:

- Your cluster must use [short-term security credentials](../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.md#cco-short-term-creds).

- You must have access to the OpenShift CLI (`oc`) as a user with the `cluster-admin` role.

- In your cloud provider console, you must have access as a user with privileges to manage Identity and Access Management (IAM) and federated identity configurations.

# Configuring GCP Workload Identity authentication for applications on Google Cloud

To use short-term authentication for applications on a Google Cloud clusters that use GCP Workload Identity authentication, you must complete the following steps:

1.  [Configure access in Google Cloud.](nodes-pods-short-term-auth.md#pod-short-term-auth-gcp-cloud-sa_nodes-pods-short-term-auth)

2.  [Create an OpenShift Container Platform service account that can use this access.](nodes-pods-short-term-auth.md#pod-short-term-auth-gcp-cluster-sa_nodes-pods-short-term-auth)

3.  [Deploy customer workloads that authenticate with GCP Workload Identity.](nodes-pods-short-term-auth.md#pod-short-term-auth-gcp-deploy-pod_nodes-pods-short-term-auth)

## Creating a federated Google Cloud service account

You can use the Google Cloud console to create a workload identity pool and provider and allow an OpenShift Container Platform service account to impersonate a Google Cloud service account.

<div>

<div class="title">

Prerequisites

</div>

- Your Google Cloud cluster uses GCP Workload Identity.

- You have access to the Google Cloud console as a user with privileges to manage Identity and Access Management (IAM) and workload identity configurations.

- You have created a Google Cloud project to use with your application.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the IAM configuration for your Google Cloud project, identify the identity pool and provider that the cluster uses for GCP Workload Identity authentication.

2.  Grant permission for external identities to impersonate a Google Cloud service account. With these permissions, an OpenShift Container Platform service account can work as a federated workload identity.

    For more information, see Google Cloud documentation about [allowing your external workload to access Google Cloud resources](https://cloud.google.com/iam/docs/workload-identity-federation-with-other-clouds#service-account-impersonation).

</div>

## Creating an OpenShift Container Platform service account for Google Cloud

You create an OpenShift Container Platform service account and annotate it to impersonate a Google Cloud service account.

<div>

<div class="title">

Prerequisites

</div>

- Your Google Cloud cluster uses GCP Workload Identity.

- You have created a federated Google Cloud service account.

- You have access to the OpenShift CLI (`oc`) as a user with the `cluster-admin` role.

- You have access to the Google Cloud CLI (`gcloud`) as a user with privileges to manage Identity and Access Management (IAM) and workload identity configurations.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an OpenShift Container Platform service account to use for GCP Workload Identity pod authentication by running the following command:

    ``` terminal
    $ oc create serviceaccount <service_account_name>
    ```

2.  Annotate the service account with the identity provider and Google Cloud service account to impersonate by running the following command:

    ``` terminal
    $ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/workload-identity-provider": "projects/<project_number>/locations/global/workloadIdentityPools/<identity_pool>/providers/<identity_provider>"}}}'
    ```

    Replace `<project_number>`, `<identity_pool>`, and `<identity_provider>` with the values for your configuration.

    > [!NOTE]
    > For `<project_number>`, specify the Google Cloud project number, not the project ID.

3.  Annotate the service account with the email address for the Google Cloud service account by running the following command:

    ``` terminal
    $ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/service-account-email": "<service_account_email>"}}}'
    ```

    Replace `<service_account_email>` with the email address for the Google Cloud service account.

    > [!TIP]
    > Google Cloud service account email addresses typically use the format `<service_account_name>@<project_id>.iam.gserviceaccount.com`

4.  Annotate the service account to use the `direct` external credentials configuration injection mode by running the following command:

    ``` terminal
    $ oc patch serviceaccount <service_account_name> -p '{"metadata": {"annotations": {"cloud.google.com/injection-mode": "direct"}}}'
    ```

    In this mode, the Workload Identity Federation webhook controller directly generates the Google Cloud external credentials configuration and injects them into the pod.

5.  Use the Google Cloud CLI (`gcloud`) to specify the permissions for the workload by running the following command:

    ``` terminal
    $ gcloud projects add-iam-policy-binding <project_id> --member "<service_account_email>" --role "projects/<project_id>/roles/<role_for_workload_permissions>"
    ```

    Replace `<role_for_workload_permissions>` with the role for the workload. Specify a role that grants the permissions that your workload requires.

</div>

<div>

<div class="title">

Verification

</div>

- To verify the service account configuration, inspect the `ServiceAccount` manifest by running the following command:

  ``` terminal
  $ oc get serviceaccount <service_account_name>
  ```

  In the following example, the `service-a/app-x` OpenShift Container Platform service account can impersonate a Google Cloud service account called `app-x`:

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` yaml
  apiVersion: v1
  kind: ServiceAccount
  metadata:
    name: app-x
    namespace: service-a
    annotations:
      cloud.google.com/workload-identity-provider: "projects/<project_number>/locations/global/workloadIdentityPools/<identity_pool>/providers/<identity_provider>"
      cloud.google.com/service-account-email: "app-x@project.iam.googleapis.com"
      cloud.google.com/audience: "sts.googleapis.com"
      cloud.google.com/token-expiration: "86400"
      cloud.google.com/gcloud-run-as-user: "1000"
      cloud.google.com/injection-mode: "direct"
  ```

  - The workload identity provider for the service account of the cluster.

  - The allowed audience for the workload identity provider.

  - The token expiration time period in seconds.

  - The `direct` external credentials configuration injection mode.

  </div>

</div>

## Deploying customer workloads that authenticate with GCP Workload Identity

To use short-term authentication in your application, you must configure its related pods to use the OpenShift Container Platform service account. Use of the OpenShift Container Platform service account triggers the webhook to mutate the pods so they can impersonate the Google Cloud service account.

The following example demonstrates how to deploy a pod that uses the OpenShift Container Platform service account and verify the configuration.

<div>

<div class="title">

Prerequisites

</div>

- Your Google Cloud cluster uses GCP Workload Identity.

- You have created a federated Google Cloud service account.

- You have created an OpenShift Container Platform service account for Google Cloud.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To create a pod that authenticates with GCP Workload Identity, create a deployment YAML file similar to the following example:

    <div class="formalpara">

    <div class="title">

    Sample deployment

    </div>

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ubi9
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: ubi9
      template:
        metadata:
          labels:
            app: ubi9
        spec:
          serviceAccountName: "<service_account_name>"
          containers:
            - name: ubi
              image: 'registry.access.redhat.com/ubi9/ubi-micro:latest'
              command:
                - /bin/sh
                - '-c'
                - |
                  sleep infinity
    ```

    </div>

    - Specify the name of the OpenShift Container Platform service account.

2.  Apply the deployment file by running the following command:

    ``` terminal
    $ oc apply -f deployment.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- To verify that a pod is using short-term authentication, run the following command:

  ``` terminal
  $ oc get pods -o json | jq -r '.items[0].spec.containers[0].env[] | select(.name=="GOOGLE_APPLICATION_CREDENTIALS")'
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  {   "name": "GOOGLE_APPLICATION_CREDENTIALS",   "value": "/var/run/secrets/workload-identity/federation.json" }
  ```

  </div>

  The presence of the `GOOGLE_APPLICATION_CREDENTIALS` environment variable indicates a pod that authenticates with GCP Workload Identity.

- To verify additional configuration details, examine the pod specification. The following example pod specifications show the environment variables and volume fields that the webhook mutates.

  <div class="formalpara">

  <div class="title">

  Example pod specification with the `direct` injection mode:

  </div>

  ``` yaml
  apiVersion: v1
  kind: Pod
  metadata:
    name: app-x-pod
    namespace: service-a
  annotations:
    cloud.google.com/skip-containers: "init-first,sidecar"
    cloud.google.com/external-credentials-json: |-
      {
        "type": "external_account",
        "audience": "//iam.googleapis.com/projects/<project_number>/locations/global/workloadIdentityPools/on-prem-kubernetes/providers/<identity_provider>",
        "subject_token_type": "urn:ietf:params:oauth:token-type:jwt",
        "token_url": "https://sts.googleapis.com/v1/token",
        "service_account_impersonation_url": "https://iamcredentials.googleapis.com/v1/projects/-/serviceAccounts/app-x@project.iam.gserviceaccount.com:generateAccessToken",
        "credential_source": {
          "file": "/var/run/secrets/sts.googleapis.com/serviceaccount/token",
          "format": {
            "type": "text"
          }
        }
      }
  spec:
    serviceAccountName: app-x
    initContainers:
    - name: init-first
      image: container-image:version
    containers:
    - name: sidecar
      image: container-image:version
    - name: container-name
      image: container-image:version
      env:
      - name: GOOGLE_APPLICATION_CREDENTIALS
        value: /var/run/secrets/gcloud/config/federation.json
      - name: CLOUDSDK_COMPUTE_REGION
        value: asia-northeast1
      volumeMounts:
      - name: gcp-iam-token
        readOnly: true
        mountPath: /var/run/secrets/sts.googleapis.com/serviceaccount
      - mountPath: /var/run/secrets/gcloud/config
        name: external-credential-config
        readOnly: true
    volumes:
    - name: gcp-iam-token
      projected:
        sources:
        - serviceAccountToken:
            audience: sts.googleapis.com
            expirationSeconds: 86400
            path: token
    - downwardAPI:
        defaultMode: 288
        items:
        - fieldRef:
            apiVersion: v1
            fieldPath: metadata.annotations['cloud.google.com/external-credentials-json']
          path: federation.json
      name: external-credential-config
  ```

  </div>

  - The external credentials configuration generated by the webhook controller. The Kubernetes `downwardAPI` volume mounts the configuration into the container filesystem.

  - The webhook-injected environment variables for token-based authentication.

</div>
