<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can customize the OpenShift Container Platform web console to set a custom logo, product name, links, notifications, and command-line downloads. This is especially helpful if you need to tailor the web console to meet specific corporate or government requirements.

# Adding a custom logo and product name

You can create custom branding by adding a custom logo or custom product name. You can set both or one without the other, as these settings are independent of each other.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

- Create a file of the logo that you want to use. The logo can be a file in any common image format, including GIF, JPG, PNG, or SVG, and is constrained to a `max-height` of `60px`. Image size must not exceed 1 MB due to constraints on the `ConfigMap` object size.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Import your logo file into a config map in the `openshift-config` namespace:

    ``` terminal
    $ oc create configmap console-custom-logo --from-file /path/to/console-custom-logo.png -n openshift-config
    ```

    > [!TIP]
    > You can alternatively apply the following YAML to create the config map:
    >
    > ``` yaml
    > apiVersion: v1
    > kind: ConfigMap
    > metadata:
    >   name: console-custom-logo
    >   namespace: openshift-config
    > binaryData:
    >   console-custom-logo.png: <base64-encoded_logo> ...
    > ```
    >
    > Replace `<base64-encoded_logo>` with a base64-encoded string of the logo.

2.  Edit the web console’s Operator configuration to include `customLogoFile` and `customProductName`:

    ``` terminal
    $ oc edit consoles.operator.openshift.io cluster
    ```

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Console
    metadata:
      name: cluster
    spec:
      customization:
        customLogoFile:
          key: console-custom-logo.png
          name: console-custom-logo
        customProductName: My Console
    ```

    Once the Operator configuration is updated, it will sync the custom logo config map into the console namespace, mount it to the console pod, and redeploy.

3.  Check for success. If there are any issues, the console cluster Operator will report a `Degraded` status, and the console Operator configuration will also report a `CustomLogoDegraded` status, but with reasons such as `KeyOrFilenameInvalid` or `NoImageProvided`.

    To check the `clusteroperator`, run:

    ``` terminal
    $ oc get clusteroperator console -o yaml
    ```

    To check the console Operator configuration, run:

    ``` terminal
    $ oc get consoles.operator.openshift.io -o yaml
    ```

</div>

# Creating custom links in the web console

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From **Administration** → **Custom Resource Definitions**, click on **ConsoleLink**.

2.  Select **Instances** tab

3.  Click **Create Console Link** and edit the file:

    ``` yaml
    apiVersion: console.openshift.io/v1
    kind: ConsoleLink
    metadata:
      name: example
    spec:
      href: 'https://www.example.com'
      location: HelpMenu
      text: Link 1
    ```

    - Valid location settings are `HelpMenu`, `UserMenu`, `ApplicationMenu`, and `NamespaceDashboard`.

      To make the custom link appear in all namespaces, follow this example:

      ``` yaml
      apiVersion: console.openshift.io/v1
      kind: ConsoleLink
      metadata:
        name: namespaced-dashboard-link-for-all-namespaces
      spec:
        href: 'https://www.example.com'
        location: NamespaceDashboard
        text: This appears in all namespaces
      ```

      To make the custom link appear in only some namespaces, follow this example:

      ``` yaml
      apiVersion: console.openshift.io/v1
      kind: ConsoleLink
      metadata:
        name: namespaced-dashboard-for-some-namespaces
      spec:
        href: 'https://www.example.com'
        location: NamespaceDashboard
        # This text will appear in a box called "Launcher" under "namespace" or "project" in the web console
        text: Custom Link Text
        namespaceDashboard:
          namespaces:
          # for these specific namespaces
          - my-namespace
          - your-namespace
          - other-namespace
      ```

      To make the custom link appear in the application menu, follow this example:

      ``` yaml
      apiVersion: console.openshift.io/v1
      kind: ConsoleLink
      metadata:
        name: application-menu-link-1
      spec:
        href: 'https://www.example.com'
        location: ApplicationMenu
        text: Link 1
        applicationMenu:
          section: My New Section
          # image that is 24x24 in size
          imageURL: https://via.placeholder.com/24
      ```

4.  Click **Save** to apply your changes.

</div>

# Customizing console routes

For `console` and `downloads` routes, custom routes functionality uses the `ingress` config route configuration API. If the `console` custom route is set up in both the `ingress` config and `console-operator` config, then the new `ingress` config custom route configuration takes precedent. The route configuration with the `console-operator` config is deprecated.

## Customizing the console route

You can customize the console route by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the cluster as a user with administrative privileges.

- You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

  > [!TIP]
  > You can create a TLS secret by using the `oc create secret tls` command.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the cluster `Ingress` configuration:

    ``` terminal
    $ oc edit ingress.config.openshift.io cluster
    ```

2.  Set the custom hostname and optionally the serving certificate and key:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Ingress
    metadata:
      name: cluster
    spec:
      componentRoutes:
        - name: console
          namespace: openshift-console
          hostname: <custom_hostname>
          servingCertKeyPairSecret:
            name: <secret_name>
    ```

    - The custom hostname.

    - Reference to a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

3.  Save the file to apply the changes.

</div>

> [!NOTE]
> Add a DNS record for the custom console route that points to the application ingress load balancer.

## Customizing the download route

You can customize the download route by setting the custom hostname and TLS certificate in the `spec.componentRoutes` field of the cluster `Ingress` configuration.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the cluster as a user with administrative privileges.

- You have created a secret in the `openshift-config` namespace containing the TLS certificate and key. This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

  > [!TIP]
  > You can create a TLS secret by using the `oc create secret tls` command.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the cluster `Ingress` configuration:

    ``` terminal
    $ oc edit ingress.config.openshift.io cluster
    ```

2.  Set the custom hostname and optionally the serving certificate and key:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Ingress
    metadata:
      name: cluster
    spec:
      componentRoutes:
        - name: downloads
          namespace: openshift-console
          hostname: <custom_hostname>
          servingCertKeyPairSecret:
            name: <secret_name>
    ```

    - The custom hostname.

    - Reference to a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

3.  Save the file to apply the changes.

</div>

> [!NOTE]
> Add a DNS record for the custom downloads route that points to the application ingress load balancer.

# Customizing the login page

Create Terms of Service information with custom login pages. Custom login pages can also be helpful if you use a third-party login provider, such as GitHub or Google, to show users a branded page that they trust and expect before being redirected to the authentication provider. You can also render custom error pages during the authentication process.

> [!NOTE]
> Customizing the error template is limited to identity providers (IDPs) that use redirects, such as request header and OIDC-based IDPs. It does not have an effect on IDPs that use direct password authentication, such as LDAP and htpasswd.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run the following commands to create templates you can modify:

    ``` terminal
    $ oc adm create-login-template > login.html
    ```

    ``` terminal
    $ oc adm create-provider-selection-template > providers.html
    ```

    ``` terminal
    $ oc adm create-error-template > errors.html
    ```

2.  Create the secrets:

    ``` terminal
    $ oc create secret generic login-template --from-file=login.html -n openshift-config
    ```

    ``` terminal
    $ oc create secret generic providers-template --from-file=providers.html -n openshift-config
    ```

    ``` terminal
    $ oc create secret generic error-template --from-file=errors.html -n openshift-config
    ```

3.  Run:

    ``` terminal
    $ oc edit oauths cluster
    ```

4.  Update the specification:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: OAuth
    metadata:
      name: cluster
    # ...
    spec:
      templates:
        error:
            name: error-template
        login:
            name: login-template
        providerSelection:
            name: providers-template
    ```

    Run `oc explain oauths.spec.templates` to understand the options.

</div>

# Defining a template for an external log link

If you are connected to a service that helps you browse your logs, but you need to generate URLs in a particular way, then you can define a template for your link.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From **Administration** → **Custom Resource Definitions**, click on **ConsoleExternalLogLink**.

2.  Select **Instances** tab

3.  Click **Create Console External Log Link** and edit the file:

    ``` yaml
    apiVersion: console.openshift.io/v1
    kind: ConsoleExternalLogLink
    metadata:
      name: example
    spec:
      hrefTemplate: >-
        https://example.com/logs?resourceName=${resourceName}&containerName=${containerName}&resourceNamespace=${resourceNamespace}&podLabels=${podLabels}
      text: Example Logs
    ```

</div>

# Creating custom notification banners

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From **Administration** → **Custom Resource Definitions**, click on **ConsoleNotification**.

2.  Select **Instances** tab

3.  Click **Create Console Notification** and edit the file:

    ``` yaml
    apiVersion: console.openshift.io/v1
    kind: ConsoleNotification
    metadata:
      name: example
    spec:
      text: This is an example notification message with an optional link.
      location: BannerTop
      link:
        href: 'https://www.example.com'
        text: Optional link text
      color: '#fff'
      backgroundColor: '#0088ce'
    ```

    - Valid location settings are `BannerTop`, `BannerBottom`, and `BannerTopBottom`.

4.  Click **Create** to apply your changes.

</div>

# Customizing CLI downloads

You can configure links for downloading the CLI with custom link text and URLs, which can point directly to file packages or to an external page that provides the packages.

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Administration** → **Custom Resource Definitions**.

2.  Select **ConsoleCLIDownload** from the list of Custom Resource Definitions (CRDs).

3.  Click the **YAML** tab, and then make your edits:

    ``` yaml
    apiVersion: console.openshift.io/v1
    kind: ConsoleCLIDownload
    metadata:
      name: example-cli-download-links
    spec:
      description: |
        This is an example of download links
      displayName: example
      links:
      - href: 'https://www.example.com/public/example.tar'
        text: example for linux
      - href: 'https://www.example.com/public/example.mac.zip'
        text: example for mac
      - href: 'https://www.example.com/public/example.win.zip'
        text: example for windows
    ```

4.  Click the **Save** button.

</div>

# Adding YAML examples to Kubernetes resources

You can dynamically add YAML examples to any Kubernetes resources at any time.

<div>

<div class="title">

Prerequisites

</div>

- You must have cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  From **Administration** → **Custom Resource Definitions**, click on **ConsoleYAMLSample**.

2.  Click **YAML** and edit the file:

    ``` yaml
    apiVersion: console.openshift.io/v1
    kind: ConsoleYAMLSample
    metadata:
      name: example
    spec:
      targetResource:
        apiVersion: batch/v1
        kind: Job
      title: Example Job
      description: An example Job YAML sample
      yaml: |
        apiVersion: batch/v1
        kind: Job
        metadata:
          name: countdown
        spec:
          template:
            metadata:
              name: countdown
            spec:
              containers:
              - name: counter
                image: centos:7
                command:
                - "bin/bash"
                - "-c"
                - "for i in 9 8 7 6 5 4 3 2 1 ; do echo $i ; done"
              restartPolicy: Never
    ```

    Use `spec.snippet` to indicate that the YAML sample is not the full YAML resource definition, but a fragment that can be inserted into the existing YAML document at the user’s cursor.

3.  Click **Save**.

</div>

# Customizing user perspectives

The OpenShift Container Platform web console provides two perspectives by default, **Administrator** and **Developer**. You might have more perspectives available depending on installed console plugins. As a cluster administrator, you can show or hide a perspective for all users or for a specific user role. Customizing perspectives ensures that users can view only the perspectives that are applicable to their role and tasks. For example, you can hide the **Administrator** perspective from unprivileged users so that they cannot manage cluster resources, users, and projects. Similarly, you can show the **Developer** perspective to users with the developer role so that they can create, deploy, and monitor applications.

You can also customize the perspective visibility for users based on role-based access control (RBAC). For example, if you customize a perspective for monitoring purposes, which requires specific permissions, you can define that the perspective is visible only to users with required permissions.

Each perspective includes the following mandatory parameters, which you can edit in the YAML view:

- `id`: Defines the ID of the perspective to show or hide

- `visibility`: Defines the state of the perspective along with access review checks, if needed

- `state`: Defines whether the perspective is enabled, disabled, or needs an access review check

> [!NOTE]
> By default, all perspectives are enabled. When you customize the user perspective, your changes are applicable to the entire cluster.

## Customizing a perspective using YAML view

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective, navigate to **Administration** → **Cluster Settings**.

2.  Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource.

3.  Click the **YAML** tab and make your customization:

    1.  To enable or disable a perspective, insert the snippet for **Add user perspectives** and edit the YAML code as needed:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: Console
        metadata:
          name: cluster
        spec:
          customization:
            perspectives:
              - id: admin
                visibility:
                  state: Enabled
              - id: dev
                visibility:
                  state: Enabled
        ```

    2.  To hide a perspective based on RBAC permissions, insert the snippet for **Hide user perspectives** and edit the YAML code as needed:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: Console
        metadata:
          name: cluster
        spec:
          customization:
            perspectives:
              - id: admin
                requiresAccessReview:
                  - group: rbac.authorization.k8s.io
                    resource: clusterroles
                    verb: list
              - id: dev
                state: Enabled
        ```

    3.  To customize a perspective based on your needs, create your own YAML snippet:

        ``` yaml
        apiVersion: operator.openshift.io/v1
        kind: Console
        metadata:
          name: cluster
        spec:
          customization:
            perspectives:
              - id: admin
                visibility:
                  state: AccessReview
                  accessReview:
                    missing:
                      - resource: deployment
                        verb: list
                    required:
                      - resource: namespaces
                        verb: list
              - id: dev
                visibility:
                  state: Enabled
        ```

4.  Click **Save**.

</div>

## Customizing a perspective using form view

<div>

<div class="title">

Prerequisites

</div>

- You must have administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective, navigate to **Administration** → **Cluster Settings**.

2.  Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource.

3.  Click **Actions** → **Customize** on the right side of the page.

4.  In the **General** settings, customize the perspective by selecting one of the following options from the dropdown list:

    - **Enabled**: Enables the perspective for all users

    - **Only visible for privileged users**: Enables the perspective for users who can list all namespaces

    - **Only visible for unprivileged users**: Enables the perspective for users who cannot list all namespaces

    - **Disabled**: Disables the perspective for all users

      A notification opens to confirm that your changes are saved.

      <figure>
      <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAA8oAAAEtCAYAAADQsZknAAAABHNCSVQICAgIfAhkiAAAIABJREFUeF7t3Qm8TPX/x/EP2ZcQka1SIZU9KqFsWbNEu1RoUSTZIu1K2heSpKSUtKBSWqVFEUJp12LJkrLv2/+8v/3O/OeOmXtnmHvNnXl9Pebhzpxzvuf7fZ4zy+d8l5Nj/fr1+4yEAAIIIIAAAggggAACCCCAAAJOICcOCCCAAAIIIIAAAggggAACCCDw/wIEypwNCCCAAAIIIIAAAggggAACCAQJEChzOiCAAAIIIIAAAggggAACCCAQJECgzOmAAAIIIIAAAggggAACCCCAQJAAgTKnAwIIIIAAAggggAACCCCAAAJBAgTKnA4IIIAAAggggAACCCCAAAIIBAkQKHM6IIAAAggggAACCCCAAAIIIBAkQKDM6YAAAggggAACCCCAAAIIIIBAkACBMqcDAggggAACCCCAAAIIIIAAAkECBMqcDggggAACCCCAAAIIIIAAAggECRAoczoggAACCCCAAAIIIIAAAgggECRAoMzpgAACCCCAAAIIIIAAAggggECQAIEypwMCCCCAAAIIIIAAAggggAACQQIEypwOCCCAAAIIIIAAAggggAACCAQJEChzOiCAAAIIIIAAAggggAACCCAQJJArXhpLly61qlWrxis78kEAAQQQQAABBBBAAAEEEEAgKoENGzZEtV60K9GiHK0U6yGAAAIIIIAAAggggAACCKSEAIFyShxmKokAAggggAACCCCAAAIIIBCtAIFytFKshwACCCCAAAIIIIAAAgggkBICBMopcZipJAIIIIAAAggggAACCCCAQLQCBMrRSrEeAggggAACCCCAAAIIIIBASggQKKfEYaaSCCCAAAIIIIAAAggggAAC0QoQKEcrxXoIIIAAAggggAACCCCAAAIpIUCgnBKHmUoigAACCCCAAAIIIIAAAghEK0CgHK0U6yGAAAIIIIAAAggggAACCKSEAIFyShxmKokAAggggAACCCCAAAIIIBCtAIFytFKshwACCCCAAAIIIIAAAgggkBICBMopcZipJAIIIIAAAggggAACCCCAQLQCBMrRSrEeAggggAACCCCAAAIIIIBASggQKKfEYaaSCCCAAAIIIIAAAggggAAC0QoQKEcrxXoIIIAAAggggAACCCCA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qQVoUU7qw0vlEDg4AbXGli5d2nr27GnHHXfcfl2jv/76a6tZs6YdfvjhdtFFF9mGDRsCO5w4caLrsv3UU09ZuXLl7Mgjj7SxY8e6Fl49L1GihI0ZM8atv2rVKrfuuHHj3PMTTzzRLrjgArv44outQIECduqpp9pPP/0Udt3Ro0fbMcccY4ULF7b69evbO++8Y9p3/vz53fp9+vRxeX/yySfudf397LPPunpp2VdffWVt27a1UqVKWdGiRd1+161bFyjT7NmzberUqW67O+64w+X5ww8/mFqa1QJeqVIlmzx5sntd6dprr3UtmQ8++KBride2JAQQQAABBBBAAIHsJUCgnL2OF6VFIMsE1JL66quvWseOHS1nzpzWoUMHe/fdd82frGv16tXWpEkTF0CqxVnBoYLK0PTdd9+5YLFatWouiPzoo4/c8zPPPNMF4GvWrAndxD2fMWOGXXjhhW7dP/74w3r16rXfen5X1Ztuusnefvtta9iwoW3ZssWaNm3q9qN0ww032GeffeYCej9pLLQC9quvvtrVTeOjH374YRsyZIhNmTLF7rzzTitevLjb7qSTTrIGDRq4v7t27erGPOu5utc+/vjjVqdOHTvvvPPsgw8+COSvdTRW9b333nPLSYkjsGDBAnf8HnnkEXd+1atXz9QC7aelS5e643zaaadZrVq13AWglStXBparp4Iugqgrty6S3HvvvRF7Lmgows0332wnn3yyVa1a1W2nMe9++uuvv6xz584uH114+fjjjxMHipIggAACCKSEgH4n6TdepEdKIESoJF2vI8DwMgKpLqCWWbWstmrVygWFLVq0sIceeshee+016969uz3//PNu0qLp06e7QFNJQXHorNf9+vVzQbS6bisQUMCrAKRv37725ptvui7XChRCk8Z6arypkgKaSZMmha5imqxLgcumTZvcGOe7777bDjvsMLeeAiClChUquJbm4KQgSYG7n+rWrRv4WwH6/PnzLXfu3G47tVQrbz8PBTsKxuWjVnIF2wrYZdOsWTOXj1qS1Vqu8dSkxBNQgKqu2epR8O+//7oLPrqgoUexYsXssssus7PPPtsV/LbbbrO77rrLRo0a5Z4vW7bMqlSp4s4R9aDQmOKhQ4cGehsE11b56/z55ptvTBN16UKRLq7odb13dBHq8ssvdz0pFFRrPyQEEEAAAQSyUkDz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AAIIIIAAAodYIOnHKB9iX3aPAAIIIIAAAggggAACCCCQzQQIlLPZAaO4CCCAAAIIIIAAAggggAACmStAoJy5vuSOAAIIIIAAAggggAACCCCQzQQIlLPZAaO4CCCAAAIIIIAAAggggAACmStAoJy5vuSOAAIIIIAAAggggAACCCCQzQQIlLPZAaO4CCCAAAIIIIAAAggggAACmStAoJy5vuSOAAIIIIAAAggggAACCCCQzQQIlLPZAaO4CCCAAAIIIIAAAggggAACmStAoJy5vuSOAAIIIIAAAggggAACCCCQzQQIlLPZAaO4CCCAAAIIIIAAAggggAACmStAoJy5vuSOAAIIIIAAAggggAACCCCQzQRyZbPyUlwEEEAAgRQV2LBhQ4rWnGojgAACCCCQ/QWKFCmSrSpBoJytDheFRQABBFJbILt9yab20aL2CCCAAAII/CeQHS920/WasxcBBBBAAAEEEEAAAQQQQACBIAECZU4HBBBAAAEEEEAAAQQQQAABBIIECJQ5HRBAAAEEEEAAAQQQQAABBBAIEiBQ5nRAAAEEEEAAAQQQQAABBBBAIEiAQJnTAQEEEEAAAQQQQAABBBBAAIEgAQJlTgcEEEAAAQQQQAABBBBAAAEEggQIlDkdEEAAAQQQQAABBBBAAAEEEAgSIFDmdEAAgYQU2L59e0KWi0IhgAACCCCAAAIIJL8AgXLyH2NqiMABCRx11FGWI0cO98idO7dVqVLFHnnkEduzZ88B5RfLRvXq1bMePXrEsgnrIpDlAosWLbKdO3dG3O/y5cvt77//jrg8owXafvXq1RmtxnIEEEAAAQQQyAQBAuVMQCVLBJJFoGbNmi44HjZsmB177LF200032QUXXGD79u3L1Cr++++/mb6PTK0AmR8ygfbt25su8pQuXdrKli1rOoeHDBlia9euTVOmjh072sSJEw+qnG3btrXNmzdHzGPgwIH21VdfRVye0YLbbrvNZs2aldFqLEcAAQQQQACBTBAgUM4EVLJEIFkEKlWqZDfeeKP169fP3n33Xbv55pvtjTfesPHjxydLFalHEgqMGTPGVq5caWqRnTJlim3cuNGaNm1qf/75Z6C26rFQv379JKw9VUIAAQQQQACBeAgQKMdDkTwQSBGB22+/3Y488kh75plnAjVeuHChnX766ZYvXz479dRTTc+VOnXqZGXK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" alt="customizing user perspective" />
      </figure>

      > [!NOTE]
      > When you customize the user perspective, your changes are automatically saved and take effect after a browser refresh.

</div>

# Developer catalog and sub-catalog customization

As a cluster administrator, you have the ability to organize and manage the Developer catalog or its sub-catalogs. You can enable or disable the sub-catalog types or disable the entire developer catalog.

The `developerCatalog.types` object includes the following parameters that you must define in a snippet to use them in the YAML view:

- `state`: Defines if a list of developer catalog types should be enabled or disabled.

- `enabled`: Defines a list of developer catalog types (sub-catalogs) that are visible to users.

- `disabled`: Defines a list of developer catalog types (sub-catalogs) that are not visible to users.

You can enable or disable the following developer catalog types (sub-catalogs) using the YAML view or the form view.

- `Builder Images`

- `Templates`

- `Devfiles`

- `Samples`

- `Helm Charts`

- `Event Sources`

- `Event Sinks`

- `Operator Backed`

## Customizing a developer catalog or its sub-catalogs using the YAML view

You can customize a developer catalog by editing the YAML content in the YAML view.

<div>

<div class="title">

Prerequisites

</div>

- An OpenShift web console session with cluster administrator privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective of the web console, navigate to **Administration** → **Cluster Settings**.

2.  Select the **Configuration** tab, click the **Console (operator.openshift.io)** resource and view the **Details** page.

3.  Click the **YAML** tab to open the editor and edit the YAML content as needed.

    For example, to disable a developer catalog type, insert the following snippet that defines a list of disabled developer catalog resources:

    ``` yaml
    apiVersion: operator.openshift.io/v1
    kind: Console
    metadata:
      name: cluster
    ...
    spec:
      customization:
        developerCatalog:
          categories:
          types:
            state: Disabled
            disabled:
              - BuilderImage
              - Devfile
              - HelmChart
    ...
    ```

4.  Click **Save**.

</div>

> [!NOTE]
> By default, the developer catalog types are enabled in the Administrator view of the Web Console.

## Customizing a developer catalog or its sub-catalogs using the form view

You can customize a developer catalog by using the form view in the Web Console.

<div>

<div class="title">

Prerequisites

</div>

- An OpenShift web console session with cluster administrator privileges.

- The Developer perspective is enabled.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the **Administrator** perspective, navigate to **Administration** → **Cluster Settings**.

2.  Select the **Configuration** tab and click the **Console (operator.openshift.io)** resource.

3.  Click **Actions** → **Customize**.

4.  Enable or disable items in the **Pre-pinned navigation items**, **Add page**, and **Developer Catalog** sections.

    <div class="formalpara">

    <div class="title">

    Verification

    </div>

    After you have customized the developer catalog, your changes are automatically saved in the system and take effect in the browser after a refresh.

    </div>

    <figure>
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAxAAAABKCAYAAAArBLLxAAAABHNCSVQICAgIfAhkiAAAABl0RVh0U29mdHdhcmUAZ25vbWUtc2NyZWVuc2hvdO8Dvz4AAB0RSURBVHic7d13eI33/8fxZ4REJCixQ+n61l61R9QWxI5N7RGCGq3R1qy9xd6ziqpSNVojqL1HY28VJbUSSURyfn+c5sjJOUkOEsHv9bgu15Vzzmfe433O+9yf+7AzGAwGREREREREbJAsqQcgIiIiIiJvDyUQIiIiIiJis+TRH9itrZJU4xARERERkTeQocEfZo/tot8D8S+PX/uARERERETkzZWe1GaPtYRJRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERsljwxGg0mhBNBVzj2+Cq/BPoDUNc1D0VS56KQywc445QY3YqIiIiISCKzMxgMhqgH//I4QRp13doWgh5Yf9HlPQKrLUyQfkREREREJHGlJ7XZ4wRfwuS6u0fsyQNA0ANjmbeQAUP8hURERERE3mEJmkC4HhkKd2/EX/DuDWNZG50JvEy1Rb1x/aY6riPq4bNxLNce3X6Fkb4414nN6bRu5GvtU0RERETkTZNgCcTqe7vg2nHbK1w7bqwTj8sPbuE+sjVHDu6C8Kdw+xYrNq6i6BAvbgT98wojfkEXzxMeEfH6+hMREREReQMlSAIRZAihy4llNpXN+nFJ099dTiwjyBASZ/kFh9dBSCh1qtThzphtHB21nqoVPKhc3J0cLpleadwiIiIiIvJiEiSBOBJ0AR7ejbdc1o9LcrpgfzoWbWh84uFdY904PAwLBiBzqrQkJxk502RlZZPhrGg63FRm2YlfyTOnC669y+E6rQ2Hbp5m3bntuHoXw3VyS1O5VqsG4+pdjEl7jcnOwqO/4DqsDq49SuE6rolZv4dunsZ1citce5bGdainTdtBRERERORdlyAJxP6HF+MtE5U8AGx68Pw+ifjqVv2wOABz1y/FdUQ9Ru6ez4k750luZ28qM/XwZv45/xdkyQb+p6kxvRef5yoO6dLD+bP437sCwG8HtkOKFLQu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" alt="odc customizing developer catalog" />
    </figure>

</div>

> [!NOTE]
> As an administrator, you can define the navigation items that appear by default for all users. You can also reorder the navigation items.

> [!TIP]
> You can use a similar procedure to customize Web UI items such as Quick starts, Cluster roles, and Actions.

### Example YAML file changes

You can dynamically add the following snippets in the YAML editor for customizing a developer catalog.

Use the following snippet to display all the sub-catalogs by setting the *state* type to **Enabled**.

``` yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
```

Use the following snippet to disable all sub-catalogs by setting the *state* type to **Disabled**:

``` yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Disabled
```

Use the following snippet when a cluster administrator defines a list of sub-catalogs, which are enabled in the Web Console.

``` yaml
apiVersion: operator.openshift.io/v1
kind: Console
metadata:
  name: cluster
...
spec:
  customization:
    developerCatalog:
      categories:
      types:
        state: Enabled
        enabled:
          - BuilderImage
          - Devfile
          - HelmChart
          - ...
```
