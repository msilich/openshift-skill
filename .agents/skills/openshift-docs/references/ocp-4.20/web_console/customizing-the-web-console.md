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

You can create a `ConsoleLink` custom resource to add a link to the help menu, user menu, application menu, or namespace dashboard in the web console.

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

1.  From **Administration** → **Custom Resource Definitions**, click **ConsoleLink**.

2.  Select the **Instances** tab.

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

    The `location` field accepts `HelpMenu`, `UserMenu`, `ApplicationMenu`, or `NamespaceDashboard`.

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

# Console and download route customization

You can customize the `console` and `downloads` routes by using the `ingress` config route configuration API. Using this API centralizes route configuration for both routes and takes precedence over the deprecated `console-operator` config method.

If the `console` custom route is configured in both the `ingress` config and the `console-operator` config, the `ingress` config custom route configuration takes precedence. Configuring custom routes through the `console-operator` config is deprecated.

# Customizing the console route

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

    The `hostname` field specifies the custom hostname. The `servingCertKeyPairSecret.name` field references a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

3.  Save the file to apply the changes.

    > [!NOTE]
    > Add a DNS record for the custom console route that points to the application ingress load balancer.

</div>

# Customizing the download route

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

    The `hostname` field specifies the custom hostname. The `servingCertKeyPairSecret.name` field references a secret in the `openshift-config` namespace that contains a TLS certificate (`tls.crt`) and key (`tls.key`). This is required if the domain for the custom hostname suffix does not match the cluster domain suffix. The secret is optional if the suffix matches.

3.  Save the file to apply the changes.

    > [!NOTE]
    > Add a DNS record for the custom downloads route that points to the application ingress load balancer.

</div>

# Customizing the login page

You can customize the login page to display Terms of Service information or apply custom branding for third-party login providers.

Custom login pages can also be helpful if you use a third-party login provider, such as GitHub or Google, to show users a branded page that they trust and expect before being redirected to the authentication provider. You can also render custom error pages during the authentication process.

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

1.  From **Administration** → **Custom Resource Definitions**, click **ConsoleExternalLogLink**.

2.  Select the **Instances** tab.

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

You can create a `ConsoleNotification` custom resource to display a banner at the top or bottom of every page in the web console.

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

1.  From **Administration** → **Custom Resource Definitions**, click **ConsoleNotification**.

2.  Select the **Instances** tab.

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

    The `location` field accepts `BannerTop`, `BannerBottom`, or `BannerTopBottom`.

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

1.  From **Administration** → **Custom Resource Definitions**, click **ConsoleYAMLSample**.

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

As a cluster administrator, you can show or hide web console perspectives for all users or for a specific user role, ensuring users see only the perspectives relevant to their role and tasks. For example, you can hide the **Administrator** perspective from users without administrative access.

You can also customize the perspective visibility for users based on role-based access control (RBAC). For example, if you customize a perspective for monitoring purposes, which requires specific permissions, you can define that the perspective is visible only to users with required permissions.

Each perspective includes the following mandatory parameters, which you can edit in the YAML view:

- `id`: Defines the ID of the perspective to show or hide

- `visibility`: Defines the state of the perspective along with access review checks, if needed

- `state`: Defines whether the perspective is enabled, disabled, or needs an access review check

> [!NOTE]
> By default, all perspectives are enabled. When you customize the user perspective, your changes are applicable to the entire cluster.

## Customizing a perspective using YAML view

You can customize a perspective by editing the console resource YAML content.

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

You can customize a perspective by using the form view of the console resource.

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

    > [!NOTE]
    > By default, the developer catalog types are enabled in the Administrator view of the Web Console.

</div>

### Example YAML file changes

You can customize a developer catalog by dynamically editing YAML content in the YAML editor.

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
    <img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAxAAAABKCAYAAAArBLLxAAAABHNCSVQICAgIfAhkiAAAABl0RVh0U29mdHdhcmUAZ25vbWUtc2NyZWVuc2hvdO8Dvz4AAB0RSURBVHic7d13eI33/8fxZ4REJCixQ+n61l61R9QWxI5N7RGCGq3R1qy9xd6ziqpSNVojqL1HY28VJbUSSURyfn+c5sjJOUkOEsHv9bgu15Vzzmfe433O+9yf+7AzGAwGREREREREbJAsqQcgIiIiIiJvDyUQIiIiIiJis+TRH9itrZJU4xARERERkTeQocEfZo/tot8D8S+PX/uARERERETkzZWe1GaPtYRJRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERspgRCRERERERsljwxGg0mhBNBVzj2+Cq/BPoDUNc1D0VS56KQywc445QY3YqIiIiISCKzMxgMhqgH//I4QRp13doWgh5Yf9HlPQKrLUyQfkREREREJHGlJ7XZ4wRfwuS6u0fsyQNA0ANjmbeQAUP8hURERERE3mEJmkC4HhkKd2/EX/DuDWNZG50JvEy1Rb1x/aY6riPq4bNxLNce3X6Fkb4414nN6bRu5GvtU0RERETkTZNgCcTqe7vg2nHbK1w7bqwTj8sPbuE+sjVHDu6C8Kdw+xYrNq6i6BAvbgT98wojfkEXzxMeEfH6+hMREREReQMlSAIRZAihy4llNpXN+nFJ099dTiwjyBASZ/kFh9dBSCh1qtThzphtHB21nqoVPKhc3J0cLpleadwiIiIiIvJiEiSBOBJ0AR7ejbdc1o9LcrpgfzoWbWh84uFdY904PAwLBiBzqrQkJxk502RlZZPhrGg63FRm2YlfyTOnC669y+E6rQ2Hbp5m3bntuHoXw3VyS1O5VqsG4+pdjEl7jcnOwqO/4DqsDq49SuE6rolZv4dunsZ1citce5bGdainTdtBRERERORdlyAJxP6HF+MtE5U8AGx68Pw+ifjqVv2wOABz1y/FdUQ9Ru6ez4k750luZ28qM/XwZv45/xdkyQb+p6kxvRef5yoO6dLD+bP437sCwG8HtkOKFLQu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" alt="Developer catalog customization options in the form view" />
    </figure>

</div>

> [!NOTE]
> As an administrator, you can define the navigation items that appear by default for all users. You can also reorder the navigation items.

> [!TIP]
> You can use a similar procedure to customize Web UI items such as Quick starts, Cluster roles, and Actions.
