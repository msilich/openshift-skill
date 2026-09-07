<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Prevent accidental exposure of sensitive information by masking annotation values in the Argo CD web UI. Configure which annotation keys to hide by adding them to the Argo CD custom resource (CR). This enhances security for sensitive data, such as tokens or API keys, stored in annotations on `Secret` resources.

# Prerequisites

- You have created an Argo CD instance. For more information, see "Installing a user-defined Argo CD instance".

# Enabling sensitive annotations masking in the Argo CD web UI

Configure the Argo CD web UI to hide sensitive values in annotations on `Secret` resources by specifying the annotation keys to mask in the Argo CD custom resource (CR).

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform web console.

2.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

3.  From the **Project** list, create or select the project where you want to install the user-defined Argo CD instance.

4.  From the installed Operators list, select **Red Hat OpenShift GitOps**, and then click the **Argo CD** tab.

5.  To edit the Argo CD CR, complete the following steps:

    1.  Under the `.spec.extraConfig` section, add the `resource.sensitive.mask.annotations` key.

    2.  To mask a comma-separated list of values, specify the annotation key in the following YAML snippet:

        ``` yaml
        apiVersion: argoproj.io/v1beta1
        kind: ArgoCD
        metadata:
          name: example
        spec:
          extraConfig:
            resource.sensitive.mask.annotations: openshift.io/token-secret.value, api-key, token
        ```

        where:

        `spec.extraConfig.resource.sensitive.mask.annotations`
        Specifies a comma-separated list of annotation keys to mask in the Argo CD web UI, such as `openshift.io/token-secret.value`, `api-key`, and `token`.

        > [!IMPORTANT]
        > Ensure that the annotation keys listed in `resource.sensitive.mask.annotations` are accurate and relevant to your use case. Wildcards are not supported. Specify each annotation key explicitly.

6.  Click **Save**.

7.  To verify that the value in the Argo CD resource has been updated successfully, complete the following steps:

    1.  In the **Administrator** perspective of the web console, click **Operators** → **Installed Operators**.

    2.  In the **Project** option, select the `Argo CD` namespace.

    3.  From the installed Operators list, select **Red Hat OpenShift GitOps**, and then click the **Argo CD** tab.

    4.  Verify that the **Status** field of the ArgoCD instance shows as **Phase: Available**.

        Argo CD hides the values of the specified annotation keys in the Argo CD UI.

</div>

# Additional resources

- [Installing a user-defined Argo CD instance](../argocd_instance/setting-up-argocd-instance.md#gitops-argo-cd-installation)
