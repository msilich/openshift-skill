> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_configuring_editors_definitions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Add custom editors to the dashboard

Add custom editor definitions to OpenShift Dev Spaces by creating a devfile with the editor configuration and storing it in a ConfigMap to offer additional IDE options to your users.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Create the `my-editor-definition-devfile.yaml` YAML file with the editor definition configuration. Provide actual values for `publisher` and `version` under `metadata.attributes` because these construct the editor ID in the format `publisher/name/version`.

    For example:

    ``` yaml
    # Version of the devfile schema
    schemaVersion: 2.2.2
    # Meta information of the editor
    metadata:
      # (MANDATORY) The editor name
      # Must consist of lower case alphanumeric characters, '-' or '.'
      name: editor-name
      displayName: Display Name
      description: Run Editor Foo on top of OpenShift Dev Spaces
      # (OPTIONAL) Array of tags of the current editor. The Tech-Preview tag means the option is considered experimental and is not recommended for production environments. While it can include new features and improvements, it may still contain bugs or undergo significant changes before reaching a stable version.
      tags:
        - Tech-Preview
      # Additional attributes
      attributes:
        title: This is my editor
        # (MANDATORY) The supported architectures
        arch:
          - x86_64
          - arm64
        # (MANDATORY) The publisher name
        publisher: publisher
        # (MANDATORY) The editor version
        version: version
        repository: https://github.com/editor/repository/
        firstPublicationDate: '2024-01-01'
        iconMediatype: image/svg+xml
        iconData: |
          <icon-content>
    # List of editor components
    components:
      # Name of the component
      - name: che-code-injector
        # Configuration of devworkspace-related container
        container:
          # Image of the container
          image: 'quay.io/che-incubator/che-code:insiders'
          # The command to run in the dockerimage component instead of the default one provided in the image
          command:
            - /entrypoint-init-container.sh
          # (OPTIONAL) List of volumes mounts that should be mounted in this container
          volumeMounts:
              # The name of the mount
            - name: checode
              # The path of the mount
              path: /checode
          # (OPTIONAL) The memory limit of the container
          memoryLimit: 256Mi
          # (OPTIONAL) The memory request of the container
          memoryRequest: 32Mi
          # (OPTIONAL) The CPU limit of the container
          cpuLimit: 500m
          # (OPTIONAL) The CPU request of the container
          cpuRequest: 30m
      # Name of the component
      - name: che-code-runtime-description
        # (OPTIONAL) Map of implementation-dependant free-form YAML attributes
        attributes:
          # The component within the architecture
          app.kubernetes.io/component: che-code-runtime
          # The name of a higher level application this one is part of
          app.kubernetes.io/part-of: che-code.eclipse.org
          # Defines a container component as a "container contribution". If a flattened DevWorkspace has a container component with the merge-contribution attribute, then any container contributions are merged into that container component
          controller.devfile.io/container-contribution: true
        container:
          # Can be a placeholder image because the component is expected to be injected into workspace dev component
          image: quay.io/devfile/universal-developer-image:latest
          # (OPTIONAL) List of volume mounts that should be mounted in this container
          volumeMounts:
              # The name of the mount
            - name: checode
              # (OPTIONAL) The path in the component container where the volume should be mounted. If no path is defined, the default path is /<name>
              path: /checode
          # (OPTIONAL) The memory limit of the container
          memoryLimit: 1024Mi
          # (OPTIONAL) The memory request of the container
          memoryRequest: 256Mi
          # (OPTIONAL) The CPU limit of the container
          cpuLimit: 500m
          # (OPTIONAL) The CPU request of the container
          cpuRequest: 30m
          # (OPTIONAL) Environment variables used in this container
          env:
            - name: ENV_NAME
              value: value
          # Component endpoints
          endpoints:
            # Name of the editor
            - name: che-code
              # (OPTIONAL) Map of implementation-dependant string-based free-form attributes
              attributes:
                # Type of the endpoint. You can only set its value to main, indicating that the endpoint should be used as the mainUrl in the workspace status (i.e. it should be the URL used to access the editor in this context)
                type: main
                # An attribute that instructs the service to automatically redirect the unauthenticated requests for current user authentication. Setting this attribute to true has security consequences because it makes Cross-site request forgery (CSRF) attacks possible. The default value of the attribute is false.
                cookiesAuthEnabled: true
                # Defines an endpoint as "discoverable", meaning that a service should be created using the endpoint name (i.e. instead of generating a service name for all endpoints, this endpoint should be statically accessible)
                discoverable: false
                # Used to secure the endpoint with authorization on OpenShift, so that not anyone on the cluster can access the endpoint, the attribute enables authentication.
                urlRewriteSupported: true
              # Port number to be used within the container component
              targetPort: 3100
              # (OPTIONAL) Describes how the endpoint should be exposed on the network (public, internal, none)
              exposure: public
              # (OPTIONAL) Describes whether the endpoint should be secured and protected by some authentication process
              secure: true
              # (OPTIONAL) Describes the application and transport protocols of the traffic that will go through this endpoint
              protocol: https
        # Mandatory name that allows referencing the component from other elements
      - name: checode
        # (OPTIONAL) Allows specifying the definition of a volume shared by several other components. Ephemeral volumes are not stored persistently across restarts. Defaults to false
        volume: {ephemeral: true}
    # (OPTIONAL) Bindings of commands to events. Each command is referred-to by its name
    events:
      # IDs of commands that should be executed before the devworkspace start. These commands would typically be executed in an init container
      preStart:
        - init-container-command
      # IDs of commands that should be executed after the devworkspace has completely started. In the case of Che-Code, these commands should be executed after all plugins and extensions have started, including project cloning. This means that those commands are not triggered until the user opens the IDE within the browser
      postStart:
        - init-che-code-command
    # (OPTIONAL) Predefined, ready-to-use, devworkspace-related commands
    commands:
        # Mandatory identifier that allows referencing this command
      - id: init-container-command
        apply:
          # Describes the component for the apply command
          component: che-code-injector
        # Mandatory identifier that allows referencing this command
      - id: init-che-code-command
        # CLI Command executed in an existing component container
        exec:
          # Describes component for the exec command
          component: che-code-runtime-description
          # The actual command-line string
          commandLine: 'nohup /checode/entrypoint-volume.sh > /checode/entrypoint-logs.txt
            2>&1 &'
    ```

    where:

    ` `*`<icon-content>`*` `  
    The SVG icon data for the editor, displayed in the OpenShift Dev Spaces Dashboard editor selector.

2.  Create a ConfigMap with the editor definition content:

    ``` bash
    oc create configmap my-editor-definition --from-file=my-editor-definition-devfile.yaml -n openshift-devspaces
    ```

3.  Add the required labels to the ConfigMap:

    ``` bash
    oc label configmap my-editor-definition app.kubernetes.io/part-of=che.eclipse.org app.kubernetes.io/component=editor-definition -n openshift-devspaces
    ```

## Results

- Refresh the OpenShift Dev Spaces Dashboard page and verify that the new editor is available.

- Verify the editor definition through the OpenShift Dev Spaces Dashboard API:

  `https://`*`<openshift_dev_spaces_fqdn>`*`/dashboard/api/editors`

  To retrieve a specific editor definition, use the publisher, name, and version values:

  `https://`*`<openshift_dev_spaces_fqdn>`*`/dashboard/api/editors/devfile?che-editor=publisher/editor-name/version`

  When retrieving the editor definition from within the OpenShift cluster, access the OpenShift Dev Spaces Dashboard API through the dashboard service: `http://devspaces-dashboard.openshift-devspaces.svc.cluster.local:8080/dashboard/api/editors`

**Related information**  

- [Devfile documentation](https://devfile.io/docs/2.2.2/what-is-a-devfile)
- [Editor definition samples](https://github.com/devfile/devworkspace-operator/tree/main/samples/editors)
