<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can enable or disable features that are Technology Preview by using feature flags.

> [!IMPORTANT]
> Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features give early access to upcoming product features, enabling customers to test functionality and give feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see the "Technology Preview Features Support Scope".

<a id="managing-feature-flags_managing-preview-features"></a>

# Managing feature flags

You can use feature flags to enable or disable Technology Preview features in RHACS. You control feature flags through environment variables that you configure on the Kubernetes deployment or during installation by using the Helm chart or the Operator custom resource.

<a id="prerequisites_managing-preview-features"></a>

## Prerequisites

Requirements for managing feature flags in RHACS.

- You have access to the environment running the RHACS component.

- You have permission to change environment variables.

- You understand that the Technology Preview features might be incomplete and have limited support.

- You know if you must configure the flag for the Technology Preview feature before the deployment. Check the installation manifests to see if they use the required flag.

<a id="managing-feature-flags-procedure_managing-preview-features"></a>

## Managing feature flags

You can enable or disable Technology Preview features by modifying environment variables associated with feature flags.

<div>

<div class="title">

Procedure

</div>

1.  Identify the environment variable name associated with the feature flag. Consult the release notes or the `/v1/featureflags` API endpoint to identify the flag for the feature you want to enable or disable.

2.  Change the feature flag by completing one of the following actions:

    - To enable a feature, configure the environment variable associated with the flag by setting its value to `true`. Configure this directly on the Kubernetes deployment or during installation by using the Helm chart or the Operator custom resource (CR).

    - To disable a feature, set the environment variable associated with the flag to `false`.

3.  After you restart or redeploy the application, verify that you enabled or disabled the feature by completing the following steps:

    - Check the output of the `/v1/featureflags` API endpoint.

    - Check the application functionality related to the feature.

    - Review logs or monitoring tools for any errors or confirmation messages.

</div>

<a id="best-practices_managing-preview-features"></a>

## Best practices

Best practices for using feature flags to manage Technology Preview features.

- Always test feature changes in a staging environment before applying them to production.

- Keep a record of all feature flags and their current status.

- Prepare to revert the changes if the feature causes issues.

<a id="troubleshooting_managing-preview-features"></a>

## Troubleshooting

Troubleshooting guidelines for resolving issues with feature flags.

- If the feature does not appear, ensure that the environment variable is correctly named and set. Check application logs for any errors related to feature flag parsing.

- If enabling a feature causes application errors, disable the feature and contact Red Hat Support.

<div>

<div class="title">

Additional resources

</div>

- [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/)

</div>
