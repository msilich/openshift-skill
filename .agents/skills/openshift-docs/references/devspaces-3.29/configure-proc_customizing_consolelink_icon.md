> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-proc_customizing_consolelink_icon). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Apply your organization’s branding to the dashboard

Apply custom branding images to the OpenShift Dev Spaces dashboard by overriding the default images in the `assets/branding` directory, so that the dashboard reflects your organization’s visual identity.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## About this task

The following images can be customized:

- `che-logo.svg`: the logo displayed in the dashboard header.
- `loader.svg`: the loader icon displayed during dashboard loading. The loader image supports the following formats, in priority order: `jpg`, `jpeg`, `png`, `gif`, `webp`, `svg`. The `svg` format is used as the default fallback.
- `favicon.ico`: the browser tab icon.

## Procedure

1.  Create a Secret that mounts custom branding images into the dashboard:

    ``` bash
    oc apply -f - <<EOF
    apiVersion: v1
    kind: Secret
    metadata:
      name: devspaces-dashboard-customization
      namespace: openshift-devspaces
      annotations:
        che.eclipse.org/mount-as: subpath
        che.eclipse.org/mount-path: /public/dashboard/assets/branding
      labels:
        app.kubernetes.io/component: devspaces-dashboard-secret
        app.kubernetes.io/part-of: che.eclipse.org
    data:
      che-logo.svg: <Base64_encoded_content_of_the_image>
      loader.svg: <Base64_encoded_content_of_the_image>
      favicon.ico: <Base64_encoded_content_of_the_image>
    type: Opaque
    EOF
    ```

    where:

    `che-logo.svg`  
    The dashboard logo. Replace the value with the Base64-encoded content of your custom logo with disabled line wrapping.

    `loader.svg`  
    The loader icon. Replace `loader.svg` with the filename matching your image format (for example, `loader.png`, `loader.webp`). The value is the Base64-encoded content of the image with disabled line wrapping.

    `favicon.ico`  
    The favicon. The value is the Base64-encoded content of the `.ico` file with disabled line wrapping.

    Note

    You can override one or all images from the `/public/dashboard/assets/branding` directory in the dashboard pod. Only the images specified in the Secret `data` section are overridden. Unspecified images remain unchanged.

2.  Verify that the rollout completes:

    ``` bash
    $ oc rollout status deployment/devspaces-dashboard -n openshift-devspaces
    ```

## Results

- Open the OpenShift Dev Spaces dashboard in a browser and confirm that the custom branding images are displayed.

**Related information**  

- [Creating custom links in the web console](https://docs.openshift.com/container-platform/4.22/web_console/customizing-the-web-console.html#creating-custom-links_customizing-web-console)
