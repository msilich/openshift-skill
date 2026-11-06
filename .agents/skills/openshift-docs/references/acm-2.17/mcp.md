> Source: [Red Hat Advanced Cluster Management for Kubernetes 2.17](https://docs.redhat.com/en/documentation/red_hat_advanced_cluster_management_for_kubernetes/2.17/html/mcp/index). Copyright Red Hat.
> Adapted from AsciiDoc to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md), [CC BY-SA 3.0](LICENSE.md) and SOURCE.json for source revisions and gaps.

<a id="acm-mcp-intro"></a>

# MCP server overview (Technology Preview)

The MCP server is a Model Context Protocol (MCP) server that provides access to the Red Hat Advanced Cluster Management for Kubernetes search database, which stores information about Kubernetes resources across managed clusters.

You must have Red Hat Advanced Cluster Management installed to use the MCP server. See [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

Use the MCP server to query cluster resources from AI assistants and other MCP clients. The server shows tools that search the same data that powers the Red Hat Advanced Cluster Management search service.

The MCP server provides output controls and filters for your artificial intelligence agents to use.

- **Available tools:** The MCP server provides the `find_resources` tool for advanced Kubernetes resource search across all managed clusters.

- **Basic filters:** `kind`, `name`, `namespace`, `cluster`, `status`

- **Advanced filters:** `labelSelector`, `clusterSelector`, `textSearch`, `ageNewerThan`, `ageOlderThan`

- **Output control:** `outputMode` (`list`, `count`, `summary`, or `health`), `groupBy`, `sortBy`, `sortOrder`, `limit`, `countOnly`

Learn how to install the MCP server and configure OpenShift Lightspeed or Claude Code to use it:

- [Install the MCP server](mcp.md#install-acm-mcp)

- [Configure OpenShift Lightspeed to use the MCP server](mcp.md#enable-acm-mcp-lightspeed)

- [Configure Claude Code to use the MCP server](mcp.md#enable-acm-mcp-claude)

<a id="install-acm-mcp"></a>

## Install the MCP server (Technology Preview)

Install the MCP server from the published Helm repository on your Red Hat Advanced Cluster Management hub cluster. The Helm chart automatically discovers your Red Hat Advanced Cluster Management `MultiClusterHub` installation, extracts database credentials, and deploys the MCP server with the required configuration.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- You must have a OpenShift Container Platform cluster with Red Hat Advanced Cluster Management installed. See [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

- You must have Helm 3.x installed locally. For more information, see [Installing Helm](https://helm.sh/docs/intro/install/).

- You need to access to the cluster using the `oc` command. See [Getting started with the OpenShift CLI](https://docs.redhat.com/en/documentation/openshift_container_platform/4.20/html/cli_tools/openshift-cli-oc#cli-getting-started) in the OpenShift Container Platform documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Add the MCP server Helm repository. Run the following command:

    ``` bash
    helm repo add acm-search https://raw.githubusercontent.com/stolostron/search-mcp-server/main/charts
    helm repo update
    ```

2.  Install the MCP server with auto-discovery. Run the following command:

    ``` bash
    helm install acm-mcp-server acm-search/acm-mcp-server \
      --create-namespace \
      --namespace acm-search
    ```

    The Helm chart automatically completes the following tasks:

    - Discovers your Red Hat Advanced Cluster Management `MultiClusterHub` installation

    - Builds the complete database connection URL

    - Deploys the MCP server with the required configuration

3.  Verify that the MCP server is running in the `acm-search` namespace. Run the following command:

    ``` bash
    oc get pods -n acm-search
    ```

    After you install the MCP server, you can connect your AI assistants or MCP clients.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring OpenShift Lightspeed to use the MCP server](mcp.md#enable-acm-mcp-lightspeed)

- [Configuring Claude Code to use the MCP server](mcp.md#enable-acm-mcp-claude)

</div>

<a id="enable-acm-mcp-lightspeed"></a>

## Configure OpenShift Lightspeed to use the MCP server (Technology Preview)

Configure OpenShift Lightspeed to use the MCP server so that you can query Red Hat Advanced Cluster Management search data from the Lightspeed assistant.

**Required access:** Cluster administrator

<div>

<div class="title">

Prerequisites

</div>

- The MCP server is installed on your Red Hat Advanced Cluster Management hub cluster. See [Installing the MCP server](mcp.md#install-acm-mcp).

- OpenShift Lightspeed is installed and configured on the Red Hat Advanced Cluster Management hub cluster where you want to add the MCP server. For more information, see [Red Hat OpenShift Lightspeed](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/install/index) installation documentation.

</div>

**Important:**

- If you already have MCP servers configured in your `OLSConfig` custom resource, add the MCP server to the existing list rather than replacing it.

- Use the exact configuration that is shown in this topic for proper functionality.

- The `acm-search`, which is the default namespace for the Helm chart, is used as the service URL.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `OLSConfig` custom resource to add the MCP server. Run the following command:

    ``` bash
    oc edit olsconfig cluster
    ```

    - If you do not have MCP servers configured in your `OLSConfig` custom resource, add `featureGates` and `mcpServers` to the following configuration:

      ``` yaml
      spec:
        featureGates:
          - MCPServer
        mcpServers:
          - headers:
              - name: Authorization
                valueFrom:
                  type: kubernetes
            name: acm
            timeout: 30
            url: 'http://acm-mcp-server.acm-search.svc.cluster.local/mcp'
      ```

    - If your `OLSConfig` custom resource already has MCP servers configured, add the MCP server to the existing `mcpServers` list. Your configuration might resemble the following example:

    ``` yaml
    mcpServers:
      - name: existing-server
        # ... existing server config ...
      - name: acm
        streamableHTTP:
          enableSSE: false
          headers:
            kubernetes-authorization: kubernetes
          sseReadTimeout: 10
          timeout: 30
          url: 'http://acm-mcp-server.acm-search.svc.cluster.local/mcp'
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Enabling a custom MCP server](https://docs.redhat.com/en/documentation/red_hat_openshift_lightspeed/1.0/html/configure/ols-configuring-openshift-lightspeed#ols-enabling-mcp-server_ols-configuring-openshift-lightspeed)

</div>

<a id="enable-acm-mcp-claude"></a>

## Configure Claude Code to use the MCP server (Technology Preview)

Configure and run Claude Code on your machine to connect to the MCP server that is installed on your Red Hat Advanced Cluster Management hub cluster. After you configure Claude Code, you can query Red Hat Advanced Cluster Management search data.

<div>

<div class="title">

Prerequisites

</div>

- You must install Red Hat Advanced Cluster Management for Kubernetes. See [Get started with Red Hat Advanced Cluster Management](get_started.md#get-started-acm).

- The MCP server is installed on your Red Hat Advanced Cluster Management hub cluster. See [Installing the MCP server](mcp.md#install-acm-mcp).

- Claude Code is installed on the machine where you run this procedure.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the Red Hat Advanced Cluster Management hub cluster by using the `oc` command. **Note:** If your cluster uses a self-signed certificate, start Claude by setting the `NODE_TLS_REJECT_UNAUTHORIZED` environment variable to `0` in your command-line environment:

    ``` bash
    export NODE_TLS_REJECT_UNAUTHORIZED=0
    ```

2.  Retrieve the route that was created by the MCP server installation in the `acm-search` namespace:

    ``` bash
    export ROUTE=$(oc get route acm-mcp-server -n acm-search -o jsonpath='{.spec.host}')
    ```

3.  Run the following command to add the MCP server to Claude Code:

    ``` bash
    claude mcp add --transport http -s project acm-search https://${ROUTE}/mcp --header "Authorization: Bearer $(oc whoami -t)"
    ```

4.  Log in to Claude Code, connect to the MCP server named `acm-search`, use the tools.

</div>
