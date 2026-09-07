> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_deploying_a_telemetry_plugin). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Deploy a telemetry plugin

Deploy the telemetry backend as a container image, create a devfile v2 plugin, and host the plugin on a web server so that Dev Workspaces can load it.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).
- You have a running instance of Red Hat OpenShift Dev Spaces.
- You have a telemetry backend created and tested. See [Create a telemetry backend](extend-proc_creating_a_telemetry_backend.md "Create a Quarkus-based telemetry backend that extends the OpenShift Dev Spaces telemetry client and implements custom event handling logic.").

## About this task

This guide demonstrates hosting the plugin on an Apache web server on OpenShift. In production, deploy the plugin file to a corporate web server.

## Procedure

1.  Package the Quarkus application as a container image and push it to a container registry by using one of the following options. See [the Quarkus documentation](https://quarkus.io/guides/building-native-image#using-a-multi-stage-docker-build) for details.
    Option A: JVM image  
    1.  Create a `Dockerfile.jvm`:

        ``` plaintext
        FROM registry.access.redhat.com/ubi8/openjdk-11:1.11

        ENV LANG='en_US.UTF-8' LANGUAGE='en_US:en'

        COPY --chown=185 target/quarkus-app/lib/ /deployments/lib/
        COPY --chown=185 target/quarkus-app/*.jar /deployments/
        COPY --chown=185 target/quarkus-app/app/ /deployments/app/
        COPY --chown=185 target/quarkus-app/quarkus/ /deployments/quarkus/

        EXPOSE 8080
        USER 185

        ENTRYPOINT ["java", "-Dquarkus.http.host=0.0.0.0", "-Djava.util.logging.manager=org.jboss.logmanager.LogManager", "-Dquarkus.http.port=${DEVWORKSPACE_TELEMETRY_BACKEND_PORT}", "-jar", "/deployments/quarkus-run.jar"]
        ```

    2.  Build and push the image:

        ``` bash
        mvn package && \
        podman build -f src/main/docker/Dockerfile.jvm -t image:tag .
        ```

    Option B: Native image  
    1.  Create a `Dockerfile.native`:

        ``` plaintext
        FROM registry.access.redhat.com/ubi8/ubi-minimal:8.5
        WORKDIR /work/
        RUN chown 1001 /work \
            && chmod "g+rwX" /work \
            && chown 1001:root /work
        COPY --chown=1001:root target/*-runner /work/application

        EXPOSE 8080
        USER 1001

        CMD ["./application", "-Dquarkus.http.host=0.0.0.0", "-Dquarkus.http.port=${DEVWORKSPACE_TELEMETRY_BACKEND_PORT}"]
        ```

    2.  Build and push the image:

        ``` bash
        mvn package -Pnative -Dquarkus.native.container-build=true && \
        podman build -f src/main/docker/Dockerfile.native -t image:tag .
        ```

2.  Create a `plugin.yaml` devfile v2 file representing a Dev Workspace plugin that runs your custom backend in a Dev Workspace Pod. For more information about devfile v2, see [Devfile v2 documentation](https://devfile.io/docs/2.1.0/overview).

    ``` yaml
    schemaVersion: 2.1.0
    metadata:
      name: devworkspace-telemetry-backend-plugin
      version: 0.0.1
      description: A Demo telemetry backend
      displayName: Devworkspace Telemetry Backend
    components:
      - name: devworkspace-telemetry-backend-plugin
        attributes:
          workspaceEnv:
            - name: DEVWORKSPACE_TELEMETRY_BACKEND_PORT
              value: '4167'
        container:
          image: <your_image>
          env:
            - name: WELCOME_MESSAGE
              value: 'hello world!'
    ```

    where:

    ` `*`<your_image>`*` `  
    The container image built in the previous step.

    `WELCOME_MESSAGE`  
    Set the value for the `welcome.message` optional configuration property.

3.  Create a `ConfigMap` object that references the `plugin.yaml` file:

    ``` bash
    $ oc create configmap --from-file=plugin.yaml -n openshift-devspaces telemetry-plugin-yaml
    ```

4.  Create a `manifest.yaml` file with a Deployment, a Service, and a Route to expose the Apache web server. The Deployment references this `ConfigMap` object and places the `plugin.yaml` in the `/var/www/html` directory.

    ``` yaml
    kind: Deployment
    apiVersion: apps/v1
    metadata:
      name: apache
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: apache
      template:
        metadata:
          labels:
            app: apache
        spec:
          volumes:
            - name: plugin-yaml
              configMap:
                name: telemetry-plugin-yaml
                defaultMode: 420
          containers:
            - name: apache
              image: 'registry.redhat.io/rhscl/httpd-24-rhel7:latest'
              ports:
                - containerPort: 8080
                  protocol: TCP
              resources: {}
              volumeMounts:
                - name: plugin-yaml
                  mountPath: /var/www/html
      strategy:
        type: RollingUpdate
        rollingUpdate:
          maxUnavailable: 25%
          maxSurge: 25%
      revisionHistoryLimit: 10
      progressDeadlineSeconds: 600
    ---
    kind: Service
    apiVersion: v1
    metadata:
      name: apache
    spec:
      ports:
        - protocol: TCP
          port: 8080
          targetPort: 8080
      selector:
        app: apache
      type: ClusterIP
    ---
    kind: Route
    apiVersion: route.openshift.io/v1
    metadata:
      name: apache
    spec:
      host: apache-che.apps-crc.testing
      to:
        kind: Service
        name: apache
        weight: 100
      port:
        targetPort: 8080
      wildcardPolicy: None
    ```

5.  Apply the manifest:

    ``` bash
    $ oc apply -f manifest.yaml
    ```

## Results

- After the deployment has started, confirm that `plugin.yaml` is available in the web server:

  ``` bash
  $ curl apache-che.apps-crc.testing/plugin.yaml
  ```

**Related tasks**  

- [Configure workspaces to load a telemetry plugin](extend-proc_configuring_workspaces_to_load_telemetry_plugin.md "Configure Dev Workspaces to load the telemetry plugin so that workspace activity events are sent to your telemetry backend for collection and analysis.")

**Related information**  

- [Configure the CheCluster Custom Resource using the CLI](configure-proc_using_cli_to_configure_checluster.md)
