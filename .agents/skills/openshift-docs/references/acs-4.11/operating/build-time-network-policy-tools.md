<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Build-time network policy tools let you automate the creation and validation of network policies, including Kubernetes network policies, and the cluster-wide Admin Network Policy (ANP) and Baseline Admin Network Policy (BANP), in your development and operations workflows by using the `roxctl` CLI. These tools work with a specified file directory containing your project’s workload and network policy manifests and do not require RHACS authentication.

| Command | Description |
|----|----|
| `roxctl netpol generate` | Generates Kubernetes network policies by analyzing your project’s YAML manifests in a specified directory. For more information, see [Using the build-time network policy generator](build-time-network-policy-tools.md#using-the-build-time-network-policy-generator_network-policy-tools). |
| `roxctl netpol connectivity map` | Lists the allowed connections between workloads in your project directory by examining the workload, Kubernetes network policy, ANP, and BANP manifests. You can generate the output in various text formats or in a graphical `.dot` format. For more information, see [Connectivity mapping using the roxctl netpol connectivity map command](build-time-network-policy-tools.md#connectivity-mapping-using-the-roxctl-netpol-connectivity-map-command_network-policy-tools). |
| `roxctl netpol connectivity diff` | Creates a list of variations in the allowed connections between two project versions. This is determined by the workload and Kubernetes network policy, ANP, and BANP manifests in each version’s directory. This feature shows the semantic differences which are not obvious when performing a source code (syntactic) `diff`. For more information, see [Identifying the differences in allowed connections between project versions](build-time-network-policy-tools.md#identifying-the-differences-in-allowed-connections-between-project-versions_network-policy-tools). |

Network policy tools

<a id="build-time-network-policy-generator_network-policy-tools"></a>

# Build-time network policy generator

The build-time network policy generator can automatically generate Kubernetes network policies based on application YAML manifests. You can use it to develop network policies as part of the continuous integration/continuous deployment (CI/CD) pipeline before deploying applications on your cluster.

Red Hat developed this feature in partnership with the developers of the [NP-Guard project](https://np-guard.github.io/). First, the build-time network policy generator analyzes Kubernetes manifests in a local folder, including service manifests, config maps, and workload manifests such as `Pod`, `Deployment`, `ReplicaSet`, `Job`, `DaemonSet`, and `StatefulSet`. Then, it discovers the required connectivity and creates the Kubernetes network policies to achieve pod isolation. These policies allow no more and no less than the needed ingress and egress traffic.

<a id="using-the-build-time-network-policy-generator_network-policy-tools"></a>

## Using the build-time network policy generator

The build-time network policy generator is included in the `roxctl` CLI. For the build-time network policy generation feature, `roxctl` CLI does not need to communicate with RHACS Central so you can use it in any development environment.

<div>

<div class="title">

Prerequisites

</div>

1.  The build-time network policy generator recursively scans the directory you specify when you run the command. Therefore, before you run the command, you must already have service manifests, config maps, and workload manifests such as `Pod`, `Deployment`, `ReplicaSet`, `Job`, `DaemonSet`, and `StatefulSet` as YAML files in the specified directory.

2.  Verify that you can apply these YAML files by using the `kubectl apply -f` command. The build-time network policy generator does not work with files that use Helm style templating.

3.  Verify that the service network addresses are not hard-coded. Every workload that needs to connect to a service must specify the service network address as a variable. You can specify this variable by using the workload’s resource environment variable or in a config map.

    - [Example 1: Using an environment variable](https://github.com/np-guard/cluster-topology-analyzer/blob/main/tests/k8s_guestbook/frontend-deployment.yaml#L25:L28)

    - [Example 2: Using a config map](https://github.com/np-guard/cluster-topology-analyzer/blob/main/tests/onlineboutique/kubernetes-manifests.yaml#L105:L109)

    - [Example 3: Using a config map](https://github.com/np-guard/cluster-topology-analyzer/blob/main/tests/onlineboutique/kubernetes-manifests.yaml#L269:L271)

4.  Service network addresses must match the following official regular expression pattern:

        (http(s)?://)?<svc>(.<ns>(.svc.cluster.local)?)?(:<portNum>)?

    - `<svc>` is the service name.

    - `<ns>` is the namespace where you defined the service.

    - `<portNum>` is the exposed service port number.

    Following are some examples that match the pattern:

    - `wordpress-mysql:3306`

    - `redis-follower.redis.svc.cluster.local:6379`

    - `redis-leader.redis`

    - `http://rating-service.`

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the build-time network policy generation feature is available by running the help command:

    ``` terminal
    $ roxctl netpol generate -h
    ```

2.  Generate the policies by using the `netpol generate` command:

    ``` terminal
    $ roxctl netpol generate <folder_path> [flags]
    ```

    where:

    `<folder_path>`  
    Specifies the path to the folder, which can include sub-folders that contain YAML resources for analysis. The command scans the entire sub-folder tree. Optionally, you can also specify parameters to change the behavior of the command.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl netpol generate command options](../cli/command-reference/roxctl-netpol.md#roxctl-netpol-generate_roxctl-netpol).

</div>

<div>

<div class="title">

Next steps

</div>

- After generating the policies, you must inspect them for completeness and accuracy, in case any relevant network address was not specified as expected in the YAML files.

- Most importantly, verify that required connections are not blocked by the isolating policies. To help with this inspection you can use the `roxctl netpol connectivity map` tool.

</div>

> [!NOTE]
> Applying network policies to the cluster as part of the workload deployment using automation saves time and ensures accuracy. You can follow a GitOps approach by submitting the generated policies using pull requests, providing the team an opportunity to review the policies before deploying them as part of the pipeline.

<a id="connectivity-mapping-using-the-roxctl-netpol-connectivity-map-command_network-policy-tools"></a>

# Connectivity mapping using the roxctl netpol connectivity map command

Connectivity mapping shows you allowed connections between workloads. It uses network policies defined in Kubernetes manifests, including Admin Network Policy (ANP) and Baseline Admin Network Policy (BANP). You can visualize and understand how your Kubernetes workloads communicate based on these combined network policies.

To retrieve connectivity mapping information, the `roxctl netpol connectivity map` command requires a directory path. This directory must contain your Kubernetes network policy, ANP, and BANP manifests. The command’s output details the connectivity within the analyzed Kubernetes resources.

<a id="retrieving-connectivity-mapping-information-from-a-kubernetes-manifest-directory_network-policy-tools"></a>

## Retrieving connectivity mapping information from a Kubernetes manifest directory

Retrieve connectivity mapping information from a Kubernetes manifest directory by using the `roxctl netpol connectivity map` command.

<div>

<div class="title">

Procedure

</div>

1.  To retrieve the connectivity mapping information, run the following command:

    ``` terminal
    roxctl netpol connectivity map <folder_path> [flags]
    ```

    where:

    `<folder_path>`  
    Specifies the path to the folder, which can include sub-folders that contain YAML resources and network policies for analysis, for example, [`netpol-analysis-example-minimal/`](https://github.com/np-guard/netpol-analyzer/tree/main/tests/netpol-analysis-example-minimal). The command scans the entire sub-folder tree. Optionally, you can also specify parameters to modify the behavior of the command.

    | src                            | dst                            | conn     |
    |--------------------------------|--------------------------------|----------|
    | 0.0.0.0-255.255.255.255        | default/frontend\[Deployment\] | TCP 8080 |
    | default/frontend\[Deployment\] | 0.0.0.0-255.255.255.255        | UDP 53   |
    | default/frontend\[Deployment\] | default/backend\[Deployment\]  | TCP 9090 |

    Example output

    The output displays a table listing the allowed connectivity lines. Each line is composed of the following elements:

    `src`  
    Represents the source endpoint.

    `dst`  
    Represents the destination endpoint.

    `conn`  
    Represents the permissible connectivity attributes.

    An endpoint follows the format `namespace/name[Kind]`. For example, `default/backend[Deployment]`.

2.  Optional: To see which policies and rules are responsible for allowing or denying specific connections, you can use the `--explain` option with the `roxctl netpol connectivity map` command. You can use the output to debug network policy configurations. For more information about understanding the explanation output, see "Retriving explanations".

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl netpol connectivity map command options](../cli/command-reference/roxctl-netpol.md#roxctl-netpol-connectivity-map_roxctl-netpol).

</div>

<a id="retrieving-explanations_network-policy-tools"></a>

## Retrieving explanations

You can understand why connections are allowed or denied based on your Kubernetes network policy rules by retrieving the explanations.

<div>

<div class="title">

Procedure

</div>

- To generate a connectivity report with explanations, run the following command:

  ``` terminal
  $ roxctl netpol connectivity map --explain <folder_path>
  ```

  where:

  `<folder_path>`  
  Specifies the path to the folder, which can include sub-folders that contain YAML resources and network policies for analysis.

  When you use the `--explain` flag, the connectivity report includes an **explanation section** that details the specific policies and rules relevant to each allowed or blocked connection.

</div>

<a id="understanding-connectivity-explanations_network-policy-tools"></a>

### Understanding Connectivity Explanations

To understand precisely which parts of your Kubernetes network policy YAML files are responsible for allowing or denying connections, you can use the `roxctl netpol connectivity map` command which includes an explainability mode. You can debug and refine your network policies by using the explainability mode which provides additional details beyond the standard connectivity report.

As a developer or DevOps professional, you might encounter situations where a connection you expect to be open is denied, or you need to confirm which specific rules allow the connection.

The following are examples of some common issues:

- Mismatched ingress and egress rules, where one side of a connection allows traffic but the other denies it.

- Typographical errors that cause policies to open different ports or protocols than intended.

The explainability mode provides insights into how each side of a connection is affected by your policy rules. You can quickly identify the configuration mistakes by using the explainability mode.

<a id="_example_allowed_connections"></a>

#### Example allowed connections

Consider that you have a Kubernetes cluster with the following components:

- A **Monitoring service** called `monitoring-service` that collects data from various applications.

- A core **Internal application A** called `internal-app-a` that actively exposes monitoring endpoints and needs monitoring.

- A network policy configuration that defines Admin Network Policy (ANP) to `pass` connections from monitoring into namespaces with label `security: internal`, and a specific Network Policy (NP) that explicitly allows connections from `monitoring-service` into `internal-app-a`.

You can see the YAML manifest for this example at [`netpol-analyzer/tests/anp_banp_explain_demo/`](https://github.com/np-guard/netpol-analyzer/tree/0ac857e19bfab4b281ca9bdfb2bbc5ea319b5065/tests/anp_banp_explain_demo).

To analyze the network policies and provides an explanation for each connection, you can run the `roxctl netpol connectivity map --explain` command on this setup.

The explainability output for allowed connections from the `monitoring-service` deployment for such configuration shows:

``` terminal
Connections between monitoring/monitoring-service[Pod] => internal-apps/internal-app-a[Pod]:
Allowed connections:
    Allowed TCP, UDP, SCTP due to the following policies and rules:
        Egress (Allowed) due to the system default (Allow all)
        Ingress (Allowed)
            AdminNetworkPolicy 'pass-monitoring' passes connections by Ingress rule pass-ingress-from-monitoring
            NetworkPolicy 'internal-apps/allow-monitoring' allows connections by Ingress rule #1
```

In this example, the connection from `monitoring/monitoring-service` to `internal-apps/internal-app-a` is allowed by the combination of ANP `pass-monitoring` that applies broadly on all namespaces with the label `security: internal` and a more specific NP `internal-apps/allow-monitoring` tailored for `internal-app-a`. The output shows that multiple policies can contribute to allowing a connection.

<a id="_example_blocked_connections"></a>

#### Example blocked connections

Consider an isolated data service `isolated-data-service` which denies all external access by default for security reasons.

You can see the YAML manifest for this example at [`netpol-analyzer/tests/anp_banp_explain_demo_2/`](https://github.com/np-guard/netpol-analyzer/tree/7ab6bbd421d3d80cbfff7cd1529ff8caf0137fbc/tests/anp_banp_explain_demo_2).

To analyze the network policies and provides an explanation for each connection, you can run the `roxctl netpol connectivity map --explain` command on this setup.

The explainability output for blocked connections from the `monitoring-service` deployment to this workload shows:

``` terminal
Connections between monitoring/monitoring-service[Pod] => isolated-apps/isolated-data-service[Pod]:

Denied connections:
    Denied TCP, UDP, SCTP due to the following policies and rules:
        Egress (Allowed) due to the system default (Allow all)
        Ingress (Denied)
            AdminNetworkPolicy 'pass-monitoring' passes connections by Ingress rule pass-ingress-from-monitoring
            BaselineAdminNetworkPolicy 'default' denies connections by Ingress rule deny-ingress-from-monitoring
```

In this example, the connection to `data/isolated-data-service` is blocked by a combination of ANP with Pass action, and of BANP that denies all connections from `monitoring` by default.

<a id="connectivity-map-output-formats-and-visualizations_network-policy-tools"></a>

## Connectivity map output formats and visualizations

You can use various output formats, including `txt`, `md`, `csv`, `json`, and `dot`. The `dot` format is ideal for visualizing the output as a connectivity graph. It can be viewed using graph visualization software such as [Graphviz tool](https://graphviz.org/), and [extensions to VSCode](https://www.google.com/search?q=vscode+Graphviz+extension). You can convert the `dot` output to formats such as `svg`, `jpeg`, or `png` using Graphviz, whether it is installed locally or through an online viewer.

<a id="generating-svg-graphs-from-the-dot-output-using-graphviz_network-policy-tools"></a>

## Generating svg graphs from the dot output using Graphviz

Follow these steps to create a graph in `svg` format from the `dot` output.

<div>

<div class="title">

Prerequisites

</div>

- [Graphviz](https://graphviz.org/) is installed on your local system.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the following command to create the graph in `svg` format:

  ``` terminal
  $ dot -Tsvg connlist_output.dot > connlist_output_graph.svg
  ```

  The following are examples of the dot output and the resulting graph generated by Graphviz:

  - [Example 1: dot output](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/connlist/netpol-analysis-example-minimal_connlist_output.dot)

  - [Example 2: Graph generated by Graphviz](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/connlist/netpol-analysis-example-minimal_connlist_output.dot.svg)

</div>

<a id="identifying-the-differences-in-allowed-connections-between-project-versions_network-policy-tools"></a>

# Identifying the differences in allowed connections between project versions

The `roxctl netpol connectivity diff` command identifies differences in allowed connections between two project versions. It analyzes network policy, Admin Network Policy (ANP), and Baseline Admin Network Policy (BANP) manifests in each version’s directory. This analysis provides a text-based report of the differences. It also includes the impact of ANP and BANP resources, giving you a complete view of policy changes across cluster scopes.

You can view connectivity difference reports in a variety of output formats, including `text`, `md`, `dot`, and `csv`.

<a id="generating-connectivity-difference-reports_network-policy-tools"></a>

## Generating connectivity difference reports by using the roxctl netpol connectivity diff command

Generate a report on connectivity differences between two sets of Kubernetes manifests, including network policies by using the `roxctl netpol connectivity diff` command .

<div>

<div class="title">

Prerequisites

</div>

- You have two folders, `dir1` and `dir2`, each containing Kubernetes manifests, including network policies.

</div>

<div>

<div class="title">

Procedure

</div>

- To find the connectivity differences between the Kubernetes manifests in the specified directories, run the following command:

  ``` terminal
  $ roxctl netpol connectivity diff --dir1=<folder_path_1> --dir2=<folder_path_2> [flags]
  ```

  Specify the path to the folders, which can include sub-folders that contain YAML resources and network policies for analysis. The command scans the entire sub-folder trees for both the directories.

  For example, `<folder_path_1>` is [`netpol-analysis-example-minimal/`](https://github.com/np-guard/netpol-analyzer/tree/main/tests/netpol-analysis-example-minimal) and `<folder_path_2>` is [`netpol-diff-example-minimal/`](https://github.com/np-guard/netpol-analyzer/tree/main/tests/netpol-diff-example-minimal). Optionally, you can also specify parameters to change the behavior of the command.

  > [!NOTE]
  > The command considers all YAML files that you can accept by using `kubectl apply -f`, and the YAML files then become valid inputs for your `roxctl netpol connectivity diff` command.

  | diff-type | source | destination | dir 1 | dir 2 | workloads-diff-info |
  |----|----|----|----|----|----|
  | changed | default/frontend\[Deployment\] | default/backend\[Deployment\] | TCP 9090 | TCP 9090,UDP 53 |  |
  | added | 0.0.0.0-255.255.255.255 | default/backend\[Deployment\] | No Connections | TCP 9090 |  |

  Example output

  The semantic difference report gives you an overview of the connections that were changed, added, or removed in `dir2` compared to the connections allowed in `dir1`. When you review the output, each line represents one allowed connection that was added, removed, or changed in `dir2` compared to `dir1`.

  If applicable, the `workloads-diff-info` provides additional details about added or removed workloads related to the added or removed connection.

  For example, if a connection from workload `A` to workload `B` is removed because workload `B` was deleted, the `workloads-diff-info` indicates that workload `B` was removed. However, if such a connection was removed only because of network policy changes and neither workload `A` nor `B` was deleted, the `workloads-diff-info` is empty.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl netpol connectivity diff command options](../cli/command-reference/roxctl-netpol.md#roxctl-netpol-connectivity-diff_roxctl-netpol).

- [Output generated by the `roxctl netpol connectivity diff` command. Example 1: text format](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/diff/diff_between_netpol-diff-example-minimal_and_netpol-analysis-example-minimal.txt)

- [Output generated by the `roxctl netpol connectivity diff` command. Example 2: md format](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/diff/diff_between_netpol-diff-example-minimal_and_netpol-analysis-example-minimal.md)

- [Output generated by the `roxctl netpol connectivity diff` command. Example 3: svg graph generated from dot format](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/diff/diff_between_netpol-diff-example-minimal_and_netpol-analysis-example-minimal.dot.svg)

- [Output generated by the `roxctl netpol connectivity diff` command. Example 4: csv format](https://github.com/np-guard/netpol-analyzer/blob/main/test_outputs/diff/diff_between_netpol-diff-example-minimal_and_netpol-analysis-example-minimal.csv)

</div>

<a id="distinguishing-between-syntactic-and-semantic-difference-outputs_network-policy-tools"></a>

## Distinguishing between syntactic and semantic difference outputs

In the following example, `dir1` is [`netpol-analysis-example-minimal/`](https://github.com/np-guard/netpol-analyzer/tree/main/tests/netpol-analysis-example-minimal), and `dir2` is [`netpol-diff-example-minimal/`](https://github.com/np-guard/netpol-analyzer/tree/main/tests/netpol-diff-example-minimal). The difference between the directories is a small change in the network policy `backend-netpol`.

<div class="formalpara">

<div class="title">

Example policy from `dir1`:

</div>

``` yaml
apiVersion: networking.k8s.io/v1
kind: NetworkPolicy
metadata:
  creationTimestamp: null
  name: backend-netpol
spec:
  ingress:
  - from:
    - podSelector:
        matchLabels:
          app: frontend
    ports:
    - port: 9090
      protocol: TCP
  podSelector:
    matchLabels:
      app: backendservice
  policyTypes:
  - Ingress
  - Egress
status: {}
```

</div>

The change in `dir2` is an added `-` before the ports attribute, which produces a difference output.

<a id="syntactic-difference-output_network-policy-tools"></a>

### Syntactic difference output

<div>

<div class="title">

Procedure

</div>

- Run the following command to compare the contents of the `netpols.yaml` files in the two specified directories:

      $ diff netpol-diff-example-minimal/netpols.yaml netpol-analysis-example-minimal/netpols.yaml

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  12c12
  <   - ports:
  ---
  >     ports:
  ```

  </div>

</div>

<a id="semantic-difference-output_network-policy-tools"></a>

### Semantic difference output

<div>

<div class="title">

Procedure

</div>

- Run the following command to analyze the connectivity differences between the Kubernetes manifests and network policies in the two specified directories:

  ``` terminal
  $ roxctl netpol connectivity diff --dir1=roxctl/netpol/connectivity/diff/testdata/netpol-analysis-example-minimal/ --dir2=roxctl/netpol/connectivity/diff/testdata/netpol-diff-example-minimal
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` text
  Connectivity diff:
  diff-type: changed, source: default/frontend[Deployment], destination: default/backend[Deployment], dir1:  TCP 9090, dir2: TCP 9090,UDP 53
  diff-type: added, source: 0.0.0.0-255.255.255.255, destination: default/backend[Deployment], dir1:  No Connections, dir2: TCP 9090
  ```

  </div>

</div>
