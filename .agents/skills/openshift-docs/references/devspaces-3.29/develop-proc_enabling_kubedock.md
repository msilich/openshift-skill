> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-proc_enabling_kubedock). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable kubedock in a workspace

Enable kubedock in an OpenShift Dev Spaces workspace by adding environment variables to the devfile.

## Before you begin

- You have an image compliant with [OpenShift Container Platform guidelines](https://docs.openshift.com/container-platform/4.22/openshift_images/create-images.html#images-create-guide-openshift_create-images).

## Procedure

1.  Add `KUBEDOCK_ENABLED=true` environment variable to the devfile.

2.  Optional: Use the `KUBEDOCK_PARAMS` variable to specify additional kubedock parameters. The list of parameters is available in the [kubedock server source](https://github.com/joyrex2001/kubedock/blob/master/cmd/server.go). Alternatively, you can use the following command to view the available options:

    ``` bash
    # kubedock server --help
    ```

3.  Configure the Podman or docker API to point to kubedock by setting `CONTAINER_HOST=tcp://127.0.0.1:2475` or `DOCKER_HOST=tcp://127.0.0.1:2475` in the devfile. Important

    Configure Podman to point to local Podman when building containers, and to kubedock when running containers.

    The following example devfile enables kubedock with Testcontainers support:

    ``` yaml
    schemaVersion: 2.2.0
    metadata:
      name: kubedock-sample-devfile
    components:
      - name: tools
        container:
          image: quay.io/devfile/universal-developer-image:latest
          memoryLimit: 8Gi
          memoryRequest: 1Gi
          cpuLimit: "2"
          cpuRequest: 200m
          env:
            - name: KUBEDOCK_PARAMS
              value: "--reverse-proxy --kubeconfig /home/user/.kube/config --initimage quay.io/agiertli/kubedock:0.13.0"
            - name: USE_JAVA17
              value: "true"
            - value: /home/jboss/.m2
              name: MAVEN_CONFIG
            - value: -Xmx4G -Xss128M -XX:MetaspaceSize=1G -XX:MaxMetaspaceSize=2G
              name: MAVEN_OPTS
            - name: KUBEDOCK_ENABLED
              value: 'true'
            - name: DOCKER_HOST
              value: 'tcp://127.0.0.1:2475'
            - name: TESTCONTAINERS_RYUK_DISABLED
              value: 'true'
            - name: TESTCONTAINERS_CHECKS_DISABLE
              value: 'true'
          endpoints:
            - exposure: none
              name: kubedock
              protocol: tcp
              targetPort: 2475
            - exposure: public
              name: http-booster
              protocol: http
              targetPort: 8080
              attributes:
                discoverable: true
                urlRewriteSupported: true
            - exposure: internal
              name: debug
              protocol: http
              targetPort: 5005
          volumeMounts:
            - name: m2
              path: /home/user/.m2
      - name: m2
        volume:
          size: 10G
    ```

**Related concepts**  

- [How kubedock works](develop-con_running_containers_with_kubedock.md "Kubedock is a minimal container engine implementation that gives you a Podman-/docker-like experience inside an OpenShift Dev Spaces workspace.")

**Related tasks**  

- [Use Kubedock in a workspace](develop-proc_using_kubedock_in_workspace.md "Use Kubedock to run containers in your workspace when Docker-in-Docker or privileged containers are not available.")
