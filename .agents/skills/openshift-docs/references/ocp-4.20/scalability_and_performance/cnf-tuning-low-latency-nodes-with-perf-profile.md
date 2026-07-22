<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Tune nodes for low latency by using the cluster performance profile. You can restrict CPUs for infra and application containers, configure huge pages, Hyper-Threading, and configure CPU partitions for latency-sensitive processes.

# Creating a performance profile

You can create a cluster performance profile by using the Performance Profile Creator (PPC) tool. The PPC is a function of the Node Tuning Operator.

The PPC combines information about your cluster with user-supplied configurations to generate a performance profile that is appropriate to your hardware, topology and use-case.

> [!NOTE]
> Performance profiles are applicable only to bare-metal environments where the cluster has direct access to the underlying hardware resources. You can configure performances profiles for both single-node OpenShift and multi-node clusters.

The following is a high-level workflow for creating and applying a performance profile in your cluster:

- Create a machine config pool (MCP) for nodes that you want to target with performance configurations. In single-node OpenShift clusters, you must use the `master` MCP because there is only one node in the cluster.

- Gather information about your cluster using the `must-gather` command.

- Use the PPC tool to create a performance profile by using either of the following methods:

  - Run the PPC tool by using Podman as described in *Running the Performance Profile Creator using Podman*. .

  - Run the PPC tool by using a wrapper script as described in *Running the Performance Profile Creator wrapper script*..

- Configure the performance profile for your use case and apply the performance profile to your cluster.

## About the Performance Profile Creator

The Performance Profile Creator (PPC) is a command-line tool and is delivered with the Node Tuning Operator. You can use the PPC CLI to create a performance profile for your cluster.

Initially, you can use the PPC tool to process the `must-gather` data to display key performance configurations for your cluster, including the following information:

- NUMA cell partitioning with the allocated CPU IDs

- Hyper-Threading node configuration

You can use this information to help you configure the performance profile.

Specify performance configuration arguments to the PPC tool to generate a proposed performance profile that is appropriate for your hardware, topology, and use-case.

You can run the PPC by using one of the following methods:

- Run the PPC by using Podman

- Run the PPC by using the wrapper script

> [!NOTE]
> Using the wrapper script abstracts some of the more granular Podman tasks into an executable script. For example, the wrapper script handles tasks such as pulling and running the required container image, mounting directories into the container, and providing parameters directly to the container through Podman. Both methods achieve the same result.

## Creating a machine config pool to target nodes for performance tuning

For multi-node clusters, you can define a machine config pool (MCP) to identify the target nodes that you want to configure with a performance profile.

In single-node OpenShift clusters, you must use the `master` MCP because there is only one node in the cluster. You do not need to create a separate MCP for single-node OpenShift clusters.

<div>

<div class="title">

Prerequisites

</div>

- You have `cluster-admin` role access.

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Label the target nodes for configuration by running the following command:

    ``` terminal
    $ oc label node <node_name> node-role.kubernetes.io/worker-cnf=""
    ```

    - `<node_name>`: Specifies the name of your node. This example applies the `worker-cnf` label.

2.  Create a `MachineConfigPool` resource containing the target nodes:

    1.  Create a YAML file that defines the `MachineConfigPool` resource:

        <div class="formalpara">

        <div class="title">

        Example `mcp-worker-cnf.yaml` file

        </div>

        ``` yaml
        apiVersion: machineconfiguration.openshift.io/v1
        kind: MachineConfigPool
        metadata:
          name: worker-cnf
          labels:
            machineconfiguration.openshift.io/role: worker-cnf
        spec:
          machineConfigSelector:
            matchExpressions:
              - {
                   key: machineconfiguration.openshift.io/role,
                   operator: In,
                   values: [worker, worker-cnf],
                }
          paused: false
          nodeSelector:
            matchLabels:
              node-role.kubernetes.io/worker-cnf: ""
        ```

        </div>

        where:

        `metadata.name`
        Specifies a name for the `MachineConfigPool` resource.

        `machineconfiguration.openshift.io/role`
        Specifes a unique label for the machine config pool.

        `node-role.kubernetes.io/worker-cnf`
        Specifies the nodes with the target label that you defined.

    2.  Apply the `MachineConfigPool` resource by running the following command:

        ``` terminal
        $ oc apply -f mcp-worker-cnf.yaml
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        machineconfigpool.machineconfiguration.openshift.io/worker-cnf created
        ```

        </div>

</div>

<div>

<div class="title">

Verification

</div>

- Check the machine config pools in your cluster by running the following command:

  ``` terminal
  $ oc get mcp
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
  master       rendered-master-58433c7c3c1b4ed5ffef95234d451490       True      False      False      3              3                   3                     0                      6h46m
  worker       rendered-worker-168f52b168f151e4f853259729b6azc4       True      False      False      2              2                   2                     0                      6h46m
  worker-cnf   rendered-worker-cnf-168f52b168f151e4f853259729b6azc4   True      False      False      1              1                   1                     0                      73s
  ```

  </div>

</div>

## Gathering data about your cluster for the PPC

The Performance Profile Creator (PPC) tool requires `must-gather` data. As a cluster administrator, run the `must-gather` command to capture information about your cluster.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- You installed the OpenShift CLI (`oc`).

- You identified a target MCP that you want to configure with a performance profile.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the directory where you want to store the `must-gather` data.

2.  Collect cluster information by running the following command:

    ``` terminal
    $ oc adm must-gather
    ```

    The command creates a folder with the `must-gather` data in your local directory with a naming format similar to the following: `must-gather.local.1971646453781853027`.

3.  Optional: Create a compressed file from the `must-gather` directory:

    ``` terminal
    $ tar cvaf must-gather.tar.gz <must_gather_folder>
    ```

    - `<must_gather_folder>`: Specifies the name of the `must-gather` data folder.

      > [!NOTE]
      > Compressed output is required if you are running the Performance Profile Creator wrapper script.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Gathering data about your cluster](../support/gathering-cluster-data.md#nodes-nodes-managing)

- [Gathering data for a hosted cluster by using the CLI](../hosted_control_planes/hcp-troubleshooting.md#hcp-must-gather-cli)

</div>

## Running the Performance Profile Creator using Podman

As a cluster administrator, you can use Podman with the Performance Profile Creator (PPC) to create a performance profile.

For more information about the PPC arguments, see the section "Performance Profile Creator arguments".

> [!IMPORTANT]
> The PPC uses the `must-gather` data from your cluster to create the performance profile. If you make any changes to your cluster, such as relabeling a node targeted for performance configuration, you must re-create the `must-gather` data before running PPC again.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- A cluster installed on bare-metal hardware.

- You installed `podman` and the OpenShift CLI (`oc`).

- Access to the Node Tuning Operator image.

- You identified a machine config pool containing target nodes for configuration.

- You have access to the `must-gather` data for your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the machine config pool by running the following command:

    ``` terminal
    $ oc get mcp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    master       rendered-master-58433c8c3c0b4ed5feef95434d455490       True      False      False      3              3                   3                     0                      8h
    worker       rendered-worker-668f56a164f151e4a853229729b6adc4       True      False      False      2              2                   2                     0                      8h
    worker-cnf   rendered-worker-cnf-668f56a164f151e4a853229729b6adc4   True      False      False      1              1                   1                     0                      79m
    ```

    </div>

2.  Use Podman to authenticate to `registry.redhat.io` by running the following command:

    ``` terminal
    $ podman login registry.redhat.io
    ```

    ``` bash
    Username: <user_name>
    Password: <password>
    ```

3.  Optional: Display help for the PPC tool by running the following command:

    ``` terminal
    $ podman run --rm --entrypoint performance-profile-creator registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17 -h
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    A tool that automates creation of Performance Profiles

    Available Commands:
      completion  Generate the autocompletion script for the specified shell
      help        Help about any command
      info        requires --must-gather-dir-path, ignores other arguments. [Valid values: log,json]

    Usage:
      performance-profile-creator [flags]
    performance-profile-creator [command]

    Flags:
          --disable-ht                        Disable Hyperthreading
          --enable-hardware-tuning            Enable setting maximum cpu frequencies
      -h, --help                              help for performance-profile-creator
          --mcp-name string                   MCP name corresponding to the target machines (required)
          --must-gather-dir-path string       Must gather directory path (default "must-gather")
          --offlined-cpu-count int            Number of offlined CPUs
          --per-pod-power-management          Enable Per Pod Power Management
          --power-consumption-mode string     The power consumption mode.  [Valid values: default, low-latency, ultra-low-latency] (default "default")
          --profile-name string               Name of the performance profile to be created (default "performance")
          --reserved-cpu-count int            Number of reserved CPUs (required)
          --rt-kernel                         Enable Real Time Kernel (required)
          --split-reserved-cpus-across-numa   Split the Reserved CPUs across NUMA nodes
          --topology-manager-policy string    Kubelet Topology Manager Policy of the performance profile to be created. [Valid values: single-numa-node, best-effort, restricted] (default "restricted")
          --user-level-networking             Run with User level Networking(DPDK) enabled

    Use "performance-profile-creator [command] --help" for more information about a command.
    ```

    </div>

4.  To display information about the cluster, run the PPC tool with the `log` argument by running the following command:

    ``` terminal
    $ podman run --entrypoint performance-profile-creator -v <path_to_must_gather>:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17 info --must-gather-dir-path /must-gather
    ```

    - `--entrypoint performance-profile-creator` defines the performance profile creator as a new entry point to `podman`.

    - `-v <path_to_must_gather>` specifies the path to either of the following components:

      - The directory containing the `must-gather` data.

      - An existing directory containing the `must-gather` decompressed .tar file.

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        level=info msg="Nodes names targeted by master pool are: "
        level=info msg="Nodes names targeted by worker-cnf pool are: host2.example.com "
        level=info msg="Nodes names targeted by worker pool are: host.example.com host1.example.com "
        level=info msg="Cluster info:"
        level=info msg="MCP 'master' nodes:"
        level=info msg=---
        level=info msg="MCP 'worker' nodes:"
        level=info msg="Node: host.example.com (NUMA cells: 1, HT: true)"
        level=info msg="NUMA cell 0 : [0 1 2 3]"
        level=info msg="CPU(s): 4"
        level=info msg="Node: host1.example.com (NUMA cells: 1, HT: true)"
        level=info msg="NUMA cell 0 : [0 1 2 3]"
        level=info msg="CPU(s): 4"
        level=info msg=---
        level=info msg="MCP 'worker-cnf' nodes:"
        level=info msg="Node: host2.example.com (NUMA cells: 1, HT: true)"
        level=info msg="NUMA cell 0 : [0 1 2 3]"
        level=info msg="CPU(s): 4"
        level=info msg=---
        ```

        </div>

5.  Create a performance profile by running the following command. The example uses sample PPC arguments and values:

    ``` terminal
    $ podman run --entrypoint performance-profile-creator -v <path_to_must_gather>:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17 --mcp-name=worker-cnf --reserved-cpu-count=1 --rt-kernel=true --split-reserved-cpus-across-numa=false --must-gather-dir-path /must-gather --power-consumption-mode=ultra-low-latency --offlined-cpu-count=1 > my-performance-profile.yaml
    ```

    - `-v <path_to_must_gather>` specifies the path to either of the following components:

      - The directory containing the `must-gather` data.

      - The directory containing the `must-gather` decompressed .tar file.

    - `--mcp-name=worker-cnf` specifies the `worker-cnf` machine config pool.

    - `--reserved-cpu-count=1` specifies one reserved CPU.

    - `--rt-kernel=true` enables the real-time kernel.

    - `--split-reserved-cpus-across-numa=false` disables reserved CPUs splitting across NUMA nodes.

    - `--power-consumption-mode=ultra-low-latency` specifies minimal latency at the cost of increased power consumption.

    - `--offlined-cpu-count=1` specifies one offlined CPU.

      > [!NOTE]
      > The `mcp-name` argument in this example is set to `worker-cnf` based on the output of the command `oc get mcp`. For single-node OpenShift use `--mcp-name=master`.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      level=info msg="Nodes targeted by worker-cnf MCP are: [worker-2]"
      level=info msg="NUMA cell(s): 1"
      level=info msg="NUMA cell 0 : [0 1 2 3]"
      level=info msg="CPU(s): 4"
      level=info msg="1 reserved CPUs allocated: 0 "
      level=info msg="2 isolated CPUs allocated: 2-3"
      level=info msg="Additional Kernel Args based on configuration: []"
      ```

      </div>

6.  Review the created YAML file by running the following command:

    ``` terminal
    $ cat my-performance-profile.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    ---
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: performance
    spec:
      cpu:
        isolated: 2-3
        offlined: "1"
        reserved: "0"
      machineConfigPoolSelector:
        machineconfiguration.openshift.io/role: worker-cnf
      net:
        userLevelNetworking: false
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
      numa:
        topologyPolicy: restricted
      realTimeKernel:
        enabled: true
      workloadHints:
        highPowerConsumption: true
        perPodPowerManagement: false
        realTime: true
    ```

    </div>

7.  Apply the generated profile:

    ``` terminal
    $ oc apply -f my-performance-profile.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    performanceprofile.performance.openshift.io/performance created
    ```

    </div>

</div>

## Running the Performance Profile Creator wrapper script

The wrapper script simplifies the process of creating a performance profile with the Performance Profile Creator (PPC) tool. The script handles tasks such as pulling and running the required container image, mounting directories into the container, and providing parameters directly to the container through Podman.

For more information about the Performance Profile Creator arguments, see the section "Performance Profile Creator arguments".

> [!IMPORTANT]
> The PPC uses the `must-gather` data from your cluster to create the performance profile. If you make any changes to your cluster, such as relabeling a node targeted for performance configuration, you must re-create the `must-gather` data before running PPC again.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- A cluster installed on bare-metal hardware.

- You installed `podman` and the OpenShift CLI (`oc`).

- Access to the Node Tuning Operator image.

- You identified a machine config pool containing target nodes for configuration.

- Access to the `must-gather` tarball.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file on your local machine named, for example, `run-perf-profile-creator.sh`:

    ``` terminal
    $ vi run-perf-profile-creator.sh
    ```

2.  Paste the following code into the file:

    ``` bash
    #!/bin/bash

    readonly CONTAINER_RUNTIME=${CONTAINER_RUNTIME:-podman}
    readonly CURRENT_SCRIPT=$(basename "$0")
    readonly CMD="${CONTAINER_RUNTIME} run --entrypoint performance-profile-creator"
    readonly IMG_EXISTS_CMD="${CONTAINER_RUNTIME} image exists"
    readonly IMG_PULL_CMD="${CONTAINER_RUNTIME} image pull"
    readonly MUST_GATHER_VOL="/must-gather"

    NTO_IMG="registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17"
    MG_TARBALL=""
    DATA_DIR=""

    usage() {
      print "Wrapper usage:"
      print "  ${CURRENT_SCRIPT} [-h] [-p image][-t path] -- [performance-profile-creator flags]"
      print ""
      print "Options:"
      print "   -h                 help for ${CURRENT_SCRIPT}"
      print "   -p                 Node Tuning Operator image"
      print "   -t                 path to a must-gather tarball"

      ${IMG_EXISTS_CMD} "${NTO_IMG}" && ${CMD} "${NTO_IMG}" -h
    }

    function cleanup {
      [ -d "${DATA_DIR}" ] && rm -rf "${DATA_DIR}"
    }
    trap cleanup EXIT

    exit_error() {
      print "error: $*"
      usage
      exit 1
    }

    print() {
      echo  "$*" >&2
    }

    check_requirements() {
      ${IMG_EXISTS_CMD} "${NTO_IMG}" || ${IMG_PULL_CMD} "${NTO_IMG}" || \
          exit_error "Node Tuning Operator image not found"

      [ -n "${MG_TARBALL}" ] || exit_error "Must-gather tarball file path is mandatory"
      [ -f "${MG_TARBALL}" ] || exit_error "Must-gather tarball file not found"

      DATA_DIR=$(mktemp -d -t "${CURRENT_SCRIPT}XXXX") || exit_error "Cannot create the data directory"
      tar -zxf "${MG_TARBALL}" --directory "${DATA_DIR}" || exit_error "Cannot decompress the must-gather tarball"
      chmod a+rx "${DATA_DIR}"

      return 0
    }

    main() {
      while getopts ':hp:t:' OPT; do
        case "${OPT}" in
          h)
            usage
            exit 0
            ;;
          p)
            NTO_IMG="${OPTARG}"
            ;;
          t)
            MG_TARBALL="${OPTARG}"
            ;;
          ?)
            exit_error "invalid argument: ${OPTARG}"
            ;;
        esac
      done
      shift $((OPTIND - 1))

      check_requirements || exit 1

      ${CMD} -v "${DATA_DIR}:${MUST_GATHER_VOL}:z" "${NTO_IMG}" "$@" --must-gather-dir-path "${MUST_GATHER_VOL}"
      echo "" 1>&2
    }

    main "$@"
    ```

3.  Add execute permissions for everyone on this script:

    ``` terminal
    $ chmod a+x run-perf-profile-creator.sh
    ```

4.  Use Podman to authenticate to `registry.redhat.io` by running the following command:

    ``` terminal
    $ podman login registry.redhat.io
    ```

    ``` bash
    Username: <user_name>
    Password: <password>
    ```

5.  Optional: Display help for the PPC tool by running the following command:

    ``` terminal
    $ ./run-perf-profile-creator.sh -h
    ```

    ``` terminal
    Wrapper usage:
      run-perf-profile-creator.sh [-h] [-p image][-t path] -- [performance-profile-creator flags]

    Options:
       -h                 help for run-perf-profile-creator.sh
       -p                 Node Tuning Operator image
       -t                 path to a must-gather tarball
    A tool that automates creation of Performance Profiles

    Usage:
      performance-profile-creator [flags]

    Flags:
          --disable-ht                        Disable Hyperthreading
      -h, --help                              help for performance-profile-creator
          --info string                       Show cluster information; requires --must-gather-dir-path, ignore the other arguments. [Valid values: log, json] (default "log")
          --mcp-name string                   MCP name corresponding to the target machines (required)
          --must-gather-dir-path string       Must gather directory path (default "must-gather")
          --offlined-cpu-count int            Number of offlined CPUs
          --per-pod-power-management          Enable Per Pod Power Management
          --power-consumption-mode string     The power consumption mode.  [Valid values: default, low-latency, ultra-low-latency] (default "default")
          --profile-name string               Name of the performance profile to be created (default "performance")
          --reserved-cpu-count int            Number of reserved CPUs (required)
          --rt-kernel                         Enable Real Time Kernel (required)
          --split-reserved-cpus-across-numa   Split the Reserved CPUs across NUMA nodes
          --topology-manager-policy string    Kubelet Topology Manager Policy of the performance profile to be created. [Valid values: single-numa-node, best-effort, restricted] (default "restricted")
          --user-level-networking             Run with User level Networking(DPDK) enabled
          --enable-hardware-tuning            Enable setting maximum CPU frequencies
    ```

    > [!NOTE]
    > You can optionally set a path for the Node Tuning Operator image using the `-p` option. If you do not set a path, the wrapper script uses the default image: `registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17`.

6.  To display information about the cluster, run the PPC tool with the `log` argument by running the following command:

    ``` terminal
    $ ./run-perf-profile-creator.sh -t /<path_to_must_gather_dir>/must-gather.tar.gz -- --info=log
    ```

    - `-t /<path_to_must_gather_dir>/must-gather.tar.gz`: Specifies the path to directory containing the must-gather tarball. This is a required argument for the wrapper script.

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      level=info msg="Cluster info:"
      level=info msg="MCP 'master' nodes:"
      level=info msg=---
      level=info msg="MCP 'worker' nodes:"
      level=info msg="Node: host.example.com (NUMA cells: 1, HT: true)"
      level=info msg="NUMA cell 0 : [0 1 2 3]"
      level=info msg="CPU(s): 4"
      level=info msg="Node: host1.example.com (NUMA cells: 1, HT: true)"
      level=info msg="NUMA cell 0 : [0 1 2 3]"
      level=info msg="CPU(s): 4"
      level=info msg=---
      level=info msg="MCP 'worker-cnf' nodes:"
      level=info msg="Node: host2.example.com (NUMA cells: 1, HT: true)"
      level=info msg="NUMA cell 0 : [0 1 2 3]"
      level=info msg="CPU(s): 4"
      level=info msg=---
      ```

      </div>

7.  Create a performance profile by running the following command. The example command uses sample PPC arguments and values.

    ``` terminal
    $ ./run-perf-profile-creator.sh -t /path-to-must-gather/must-gather.tar.gz -- --mcp-name=worker-cnf --reserved-cpu-count=1 --rt-kernel=true --split-reserved-cpus-across-numa=false --power-consumption-mode=ultra-low-latency --offlined-cpu-count=1 > my-performance-profile.yaml
    ```

    - `--mcp-name=worker-cnf` specifies the `worker-cnf` machine config pool.

    - `--reserved-cpu-count=1` specifies one reserved CPU.

    - `--rt-kernel=true` enables the real-time kernel.

    - `--split-reserved-cpus-across-numa=false` disables reserved CPUs splitting across NUMA nodes.

    - `--power-consumption-mode=ultra-low-latency` specifies minimal latency at the cost of increased power consumption.

    - `--offlined-cpu-count=1` specifies one offlined CPUs.

      > [!NOTE]
      > The `mcp-name` argument in this example is set to `worker-cnf` based on the output of the command `oc get mcp`. For single-node OpenShift use `--mcp-name=master`.

8.  Review the created YAML file by running the following command:

    ``` terminal
    $ cat my-performance-profile.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: performance
    spec:
      cpu:
        isolated: 2-3
        offlined: "1"
        reserved: "0"
      machineConfigPoolSelector:
        machineconfiguration.openshift.io/role: worker-cnf
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
      numa:
        topologyPolicy: restricted
      realTimeKernel:
        enabled: true
      workloadHints:
        highPowerConsumption: true
        perPodPowerManagement: false
        realTime: true
    ```

    </div>

9.  Apply the generated profile:

    ``` terminal
    $ oc apply -f my-performance-profile.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    performanceprofile.performance.openshift.io/performance created
    ```

    </div>

</div>

## Performance Profile Creator arguments

To customize the generation of performance profiles, review the arguments for the Performance Profile Creator.

<table>
<caption>Required Performance Profile Creator arguments</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Argument</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>mcp-name</code></p></td>
<td style="text-align: left;"><p>Name for MCP; for example, <code>worker-cnf</code> corresponding to the target machines.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>must-gather-dir-path</code></p></td>
<td style="text-align: left;"><p>The path of the must gather directory.</p>
<p>This argument is only required if you run the PPC tool by using Podman. If you use the PPC with the wrapper script, do not use this argument. Instead, specify the directory path to the <code>must-gather</code> tarball by using the <code>-t</code> option for the wrapper script.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>reserved-cpu-count</code></p></td>
<td style="text-align: left;"><p>Number of reserved CPUs. Use a natural number greater than zero.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rt-kernel</code></p></td>
<td style="text-align: left;"><p>Enables real-time kernel.</p>
<p>Possible values: <code>true</code> or <code>false</code>.</p></td>
</tr>
</tbody>
</table>

<table>
<caption>Optional Performance Profile Creator arguments</caption>
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Argument</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>disable-ht</code></p></td>
<td style="text-align: left;"><p>Disable Hyper-Threading.</p>
<p>Possible values: <code>true</code> or <code>false</code>.</p>
<p>Default: <code>false</code>.</p>
<div class="warning">
<div class="title">
&#10;</div>
<p>If this argument is set to <code>true</code> you should not disable Hyper-Threading in the BIOS. Disabling Hyper-Threading is accomplished with a kernel command-line argument.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p>enable-hardware-tuning</p></td>
<td style="text-align: left;"><p>Enable the setting of maximum CPU frequencies.</p>
<p>To enable this feature, set the maximum frequency for applications running on isolated and reserved CPUs for both of the following fields:</p>
<ul>
<li><p><code>spec.hardwareTuning.isolatedCpuFreq</code></p></li>
<li><p><code>spec.hardwareTuning.reservedCpuFreq</code></p></li>
</ul>
<p>This is an advanced feature. If you configure hardware tuning, the generated <code>PerformanceProfile</code> includes warnings and guidance on how to set frequency settings.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>info</code></p></td>
<td style="text-align: left;"><p>This captures cluster information. This argument also requires the <code>must-gather-dir-path</code> argument. If any other arguments are set they are ignored.</p>
<p>Possible values:</p>
<ul>
<li><p><code>log</code></p></li>
<li><p><code>JSON</code></p></li>
</ul>
<p>Default: <code>log</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>offlined-cpu-count</code></p></td>
<td style="text-align: left;"><p>Number of offlined CPUs.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Use a natural number greater than zero. If not enough logical processors are offlined, then error messages are logged. The messages are:</p>
<pre class="terminal"><code>Error: failed to compute the reserved and isolated CPUs: please ensure that reserved-cpu-count plus offlined-cpu-count should be in the range [0,1]</code></pre>
<pre class="terminal"><code>Error: failed to compute the reserved and isolated CPUs: please specify the offlined CPU count in the range [0,1]</code></pre>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>power-consumption-mode</code></p></td>
<td style="text-align: left;"><p>The power consumption mode.</p>
<p>Possible values:</p>
<ul>
<li><p><code>default</code>: Performance achieved through CPU partitioning only.</p></li>
<li><p><code>low-latency</code>: Enhanced measures to improve latency.</p></li>
<li><p><code>ultra-low-latency</code>: Priority given to optimal latency, at the expense of power management.</p></li>
</ul>
<p>Default: <code>default</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>per-pod-power-management</code></p></td>
<td style="text-align: left;"><p>Enable per pod power management. You cannot use this argument if you configured <code>ultra-low-latency</code> as the power consumption mode.</p>
<p>Possible values: <code>true</code> or <code>false</code>.</p>
<p>Default: <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>profile-name</code></p></td>
<td style="text-align: left;"><p>Name of the performance profile to create.</p>
<p>Default: <code>performance</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>split-reserved-cpus-across-numa</code></p></td>
<td style="text-align: left;"><p>Split the reserved CPUs across NUMA nodes.</p>
<p>Possible values: <code>true</code> or <code>false</code>.</p>
<p>Default: <code>false</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>topology-manager-policy</code></p></td>
<td style="text-align: left;"><p>Kubelet Topology Manager policy of the performance profile to be created.</p>
<p>Possible values:</p>
<ul>
<li><p><code>single-numa-node</code></p></li>
<li><p><code>best-effort</code></p></li>
<li><p><code>restricted</code></p></li>
</ul>
<p>Default: <code>restricted</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>user-level-networking</code></p></td>
<td style="text-align: left;"><p>Run with user level networking (DPDK) enabled.</p>
<p>Possible values: <code>true</code> or <code>false</code>.</p>
<p>Default: <code>false</code>.</p></td>
</tr>
</tbody>
</table>

# Reference performance profiles

Use the following reference performance profiles as the basis to develop your own custom profiles.

## Performance profile template for clusters that use OVS-DPDK on OpenStack

To maximize machine performance in a cluster that uses Open vSwitch with the Data Plane Development Kit (OVS-DPDK) on Red Hat OpenStack Platform (RHOSP), you can use a performance profile.

You can use the following performance profile template to create a profile for your deployment.

<div class="formalpara">

<div class="title">

Performance profile template for clusters that use OVS-DPDK

</div>

``` yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: cnf-performanceprofile
spec:
  additionalKernelArgs:
    - nmi_watchdog=0
    - audit=0
    - mce=off
    - processor.max_cstate=1
    - idle=poll
    - intel_idle.max_cstate=0
    - default_hugepagesz=1GB
    - hugepagesz=1G
    - intel_iommu=on
  cpu:
    isolated: <CPU_ISOLATED>
    reserved: <CPU_RESERVED>
  hugepages:
    defaultHugepagesSize: 1G
    pages:
      - count: <HUGEPAGES_COUNT>
        node: 0
        size: 1G
  nodeSelector:
    node-role.kubernetes.io/worker: ''
  realTimeKernel:
    enabled: false
    globallyDisableIrqLoadBalancing: true
```

</div>

Insert values that are appropriate for your configuration for the `CPU_ISOLATED`, `CPU_RESERVED`, and `HUGEPAGES_COUNT` keys.

## Telco RAN DU reference design performance profile

You can use a pre-configured design performance profile that configures node-level performance settings for OpenShift Container Platform clusters on commodity hardware to host telco RAN DU workloads.

<div class="formalpara">

<div class="title">

Telco RAN DU reference design performance profile

</div>

``` yaml
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  # if you change this name make sure the 'include' line in TunedPerformancePatch.yaml
  # matches this name: include=openshift-node-performance-${PerformanceProfile.metadata.name}
  # Also in file 'validatorCRs/informDuValidator.yaml':
  # name: 50-performance-${PerformanceProfile.metadata.name}
  name: openshift-node-performance-profile
  annotations:
    ran.openshift.io/reference-configuration: "ran-du.redhat.com"
spec:
  additionalKernelArgs:
    - "rcupdate.rcu_normal_after_boot=0"
    - "efi=runtime"
    - "vfio_pci.enable_sriov=1"
    - "vfio_pci.disable_idle_d3=1"
    - "module_blacklist=irdma"
  cpu:
    isolated: $isolated
    reserved: $reserved
  hugepages:
    defaultHugepagesSize: $defaultHugepagesSize
    pages:
      - size: $size
        count: $count
        node: $node
  machineConfigPoolSelector:
    pools.operator.machineconfiguration.openshift.io/$mcp: ""
  nodeSelector:
    node-role.kubernetes.io/$mcp: ''
  numa:
    topologyPolicy: "restricted"
  # To use the standard (non-realtime) kernel, set enabled to false
  realTimeKernel:
    enabled: true
  workloadHints:
    # WorkloadHints defines the set of upper level flags for different type of workloads.
    # See https://github.com/openshift/cluster-node-tuning-operator/blob/master/docs/performanceprofile/performance_profile.md#workloadhints
    # for detailed descriptions of each item.
    # The configuration below is set for a low latency, performance mode.
    realTime: true
    highPowerConsumption: false
    perPodPowerManagement: false
```

</div>

## Telco core reference design performance profile

You can use a pre-configured design performance profile that configures node-level performance settings for OpenShift Container Platform clusters on commodity hardware to host telco core workloads.

<div class="formalpara">

<div class="title">

Telco core reference design performance profile

</div>

``` yaml
# required
# count: 1
apiVersion: performance.openshift.io/v2
kind: PerformanceProfile
metadata:
  name: $name
  annotations:
    # Some pods want the kernel stack to ignore IPv6 router Advertisement.
    kubeletconfig.experimental: |
      {"allowedUnsafeSysctls":["net.ipv6.conf.all.accept_ra"]}
spec:
  cpu:
    # node0 CPUs: 0-17,36-53
    # node1 CPUs: 18-34,54-71
    # siblings: (0,36), (1,37)...
    # we want to reserve the first Core of each NUMA socket
    #
    # no CPU left behind! all-cpus == isolated + reserved
    isolated: $isolated # eg 1-17,19-35,37-53,55-71
    reserved: $reserved # eg 0,18,36,54
  # Guaranteed QoS pods will disable IRQ balancing for cores allocated to the pod.
  # default value of globallyDisableIrqLoadBalancing is false
  globallyDisableIrqLoadBalancing: false
  hugepages:
    defaultHugepagesSize: 1G
    pages:
      # 32GB per numa node
      - count: $count # eg 64
        size: 1G
  #machineConfigPoolSelector: {}
  #  pools.operator.machineconfiguration.openshift.io/worker: ''
  nodeSelector: {}
  #node-role.kubernetes.io/worker: ""
  workloadHints:
    realTime: false
    highPowerConsumption: false
    perPodPowerManagement: true
  realTimeKernel:
    enabled: false
  numa:
    # All guaranteed QoS containers get resources from a single NUMA node
    topologyPolicy: "single-numa-node"
  net:
    userLevelNetworking: false
```

</div>

# Supported performance profile API versions

The Node Tuning Operator supports `v2`, `v1`, and `v1alpha1` for the performance profile `apiVersion` field. The v1 and v1alpha1 APIs are identical. The v2 API includes an optional boolean field `globallyDisableIrqLoadBalancing` with a default value of `false`.

Upgrading the performance profile to use device interrupt processing
When you upgrade the Node Tuning Operator performance profile custom resource definition (CRD) from v1 or v1alpha1 to v2, `globallyDisableIrqLoadBalancing` is set to `true` on existing profiles.

> [!NOTE]
> `globallyDisableIrqLoadBalancing` toggles whether IRQ load balancing will be disabled for the Isolated CPU set. When the option is set to `true` it disables IRQ load balancing for the Isolated CPU set. Setting the option to `false` allows the IRQs to be balanced across all CPUs.

Upgrading Node Tuning Operator API from v1alpha1 to v1
When upgrading Node Tuning Operator API version from v1alpha1 to v1, the v1alpha1 performance profiles are converted on-the-fly using a "None" Conversion strategy and served to the Node Tuning Operator with API version v1.

Upgrading Node Tuning Operator API from v1alpha1 or v1 to v2
When upgrading from an older Node Tuning Operator API version, the existing v1 and v1alpha1 performance profiles are converted using a conversion webhook that injects the `globallyDisableIrqLoadBalancing` field with a value of `true`.

# Node power consumption and realtime processing with workload hints

You can create a performance profile appropriate for the hardware and topology of an environment by using the Performance Profile Creator (PPC) tool.

The following table describes the possible values set for the `power-consumption-mode` flag associated with the PPC tool and the workload hint that is applied.

<table>
<caption>Impact of combinations of power consumption and real-time settings on latency</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Performance Profile creator setting</th>
<th style="text-align: left;">Hint</th>
<th style="text-align: left;">Environment</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Default</p></td>
<td style="text-align: left;"><pre class="terminal"><code>workloadHints:
highPowerConsumption: false
realTime: false</code></pre></td>
<td style="text-align: left;"><p>High throughput cluster without latency requirements</p></td>
<td style="text-align: left;"><p>Performance achieved through CPU partitioning only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Low-latency</p></td>
<td style="text-align: left;"><pre class="terminal"><code>workloadHints:
highPowerConsumption: false
realTime: true</code></pre></td>
<td style="text-align: left;"><p>Regional data-centers</p></td>
<td style="text-align: left;"><p>Both energy savings and low-latency are desirable: compromise between power management, latency and throughput.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Ultra-low-latency</p></td>
<td style="text-align: left;"><pre class="terminal"><code>workloadHints:
highPowerConsumption: true
realTime: true</code></pre></td>
<td style="text-align: left;"><p>Far edge clusters, latency critical workloads</p></td>
<td style="text-align: left;"><p>Optimized for absolute minimal latency and maximum determinism at the cost of increased power consumption.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Per-pod power management</p></td>
<td style="text-align: left;"><pre class="terminal"><code>workloadHints:
realTime: true
highPowerConsumption: false
perPodPowerManagement: true</code></pre></td>
<td style="text-align: left;"><p>Critical and non-critical workloads</p></td>
<td style="text-align: left;"><p>Allows for power management per pod.</p></td>
</tr>
</tbody>
</table>

The following configuration is commonly used in a telco RAN DU deployment:

``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: workload-hints
    spec:
      ...
      workloadHints:
        realTime: true
        highPowerConsumption: false
        perPodPowerManagement: false
```

`perPodPowerManagement`
Specifies to disable some debugging and monitoring features that can affect system latency.

> [!NOTE]
> When the `realTime` workload hint flag is set to `true` in a performance profile, add the `cpu-quota.crio.io: disable` annotation to every guaranteed pod with pinned CPUs. This annotation is necessary to prevent the degradation of the process performance within the pod. If the `realTime` workload hint is not explicitly set, it defaults to `true`.

For more information how combinations of power consumption and real-time settings impact latency, see "Understanding workload hints".

<div>

<div class="title">

Additional resources

</div>

- [Understanding workload hints](https://access.redhat.com/articles/7081587)

</div>

# Configuring power saving for nodes that run colocated high and low priority workloads

You can enable power savings for a node that has low priority workloads that are colocated with high priority workloads without impacting the latency or throughput of the high priority workloads. Power saving is possible without modifications to the workloads themselves.

> [!IMPORTANT]
> The feature is supported on Intel Ice Lake and later generations of Intel CPUs. The capabilities of the processor might impact the latency and throughput of the high priority workloads.

<div>

<div class="title">

Prerequisites

</div>

- You enabled C-states and operating system controlled P-states in the BIOS

</div>

<div>

<div class="title">

Procedure

</div>

1.  Generate a `PerformanceProfile` with the `per-pod-power-management` argument set to `true`:

    ``` terminal
    $ podman run --entrypoint performance-profile-creator -v \
    /must-gather:/must-gather:z registry.redhat.io/openshift4/ose-cluster-node-tuning-rhel9-operator:v4.17 \
    --mcp-name=worker-cnf --reserved-cpu-count=20 --rt-kernel=true \
    --split-reserved-cpus-across-numa=false --topology-manager-policy=single-numa-node \
    --must-gather-dir-path /must-gather --power-consumption-mode=low-latency \
    --per-pod-power-management=true > my-performance-profile.yaml
    ```

    The `power-consumption-mode` argument must be `default` or `low-latency` when the `per-pod-power-management` argument is set to `true`.

    <div class="formalpara">

    <div class="title">

    Example `PerformanceProfile` with `perPodPowerManagement`

    </div>

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
         name: performance
    spec:
        [.....]
        workloadHints:
            realTime: true
            highPowerConsumption: false
            perPodPowerManagement: true
    # ...
    ```

    </div>

2.  Set the default `cpufreq` governor as an additional kernel argument in the `PerformanceProfile` custom resource (CR):

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
         name: performance
    spec:
        ...
        additionalKernelArgs:
        - cpufreq.default_governor=schedutil
    # ...
    ```

    where:

    `cpufreq.default_governor=schedutil`
    Specifies using the `schedutil` governor. You can use other governors, such as the `ondemand` or `powersave` governors.

3.  Set the maximum CPU frequency in the `TunedPerformancePatch` CR:

    ``` yaml
    spec:
      profile:
      - data: |
          [sysfs]
          /sys/devices/system/cpu/intel_pstate/max_perf_pct = <x>
    ```

    where:

    `/sys/devices/system/cpu/intel_pstate/max_perf_pct`
    Specifies the `max_perf_pct` that controls the maximum frequency that the `cpufreq` driver is allowed to set as a percentage of the maximum supported cpu frequency. This value applies to all CPUs. You can check the maximum supported frequency in `/sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_max_freq`. As a starting point, you can use a percentage that caps all CPUs at the `All Cores Turbo` frequency. The `All Cores Turbo` frequency is the frequency that all cores will run at when the cores are all fully occupied.

</div>

<div>

<div class="title">

Additional resources

</div>

- [About the Performance Profile Creator](cnf-tuning-low-latency-nodes-with-perf-profile.md#cnf-about-the-profile-creator-tool_cnf-tuning-low-latency-nodes-with-perf-profile)

- [Disabling power saving mode for high priority pods](cnf-provisioning-low-latency-workloads.md#cnf-configuring-high-priority-workload-pods_cnf-provisioning-low-latency)

- [Managing device interrupt processing for guaranteed pod isolated CPUs](cnf-tuning-low-latency-nodes-with-perf-profile.md#managing-device-interrupt-processing-for-guaranteed-pod-isolated-cpus_cnf-tuning-low-latency-nodes-with-perf-profile)

</div>

# CPUs for infra and application containers

Generic housekeeping and workload tasks use CPUs in a way that might impact latency-sensitive processes. By default, the container runtime uses all online CPUs to run all containers together, which can result in context switches and spikes in latency.

Partitioning the CPUs prevents noisy processes from interfering with latency-sensitive processes by separating them from each other. The following table describes how processes run on a CPU after you have tuned the node using the Node Tuning Operator:

| Process type | Details |
|----|----|
| `Burstable` and `BestEffort` pods | Runs on any CPU except where low latency workload is running |
| Infrastructure pods | Runs on any CPU except where low latency workload is running |
| Interrupts | Redirects to reserved CPUs (optional in OpenShift Container Platform 4.7 and later) |
| Kernel processes | Pins to reserved CPUs |
| Latency-sensitive workload pods | Pins to a specific set of exclusive CPUs from the isolated pool |
| OS processes/systemd services | Pins to reserved CPUs |

Process' CPU assignments

The allocatable capacity of cores on a node for pods of all QoS process types, `Burstable`, `BestEffort`, or `Guaranteed`, is equal to the capacity of the isolated pool. The capacity of the reserved pool is removed from the node’s total core capacity for use by the cluster and operating system housekeeping duties.

Example 1
A node features a capacity of 100 cores. Using a performance profile, the cluster administrator allocates 50 cores to the isolated pool and 50 cores to the reserved pool. The cluster administrator assigns 25 cores to QoS `Guaranteed` pods and 25 cores for `BestEffort` or `Burstable` pods. This matches the capacity of the isolated pool.

Example 2
A node features a capacity of 100 cores. Using a performance profile, the cluster administrator allocates 50 cores to the isolated pool and 50 cores to the reserved pool. The cluster administrator assigns 50 cores to QoS `Guaranteed` pods and one core for `BestEffort` or `Burstable` pods. This exceeds the capacity of the isolated pool by one core. Pod scheduling fails because of insufficient CPU capacity.

The exact partitioning pattern to use depends on many factors like hardware, workload characteristics and the expected system load. Some sample use cases are as follows:

- If the latency-sensitive workload uses specific hardware, such as a network interface controller (NIC), ensure that the CPUs in the isolated pool are as close as possible to this hardware. At a minimum, you should place the workload in the same Non-Uniform Memory Access (NUMA) node.

- The reserved pool is used for handling all interrupts. When depending on system networking, allocate a sufficiently-sized reserve pool to handle all the incoming packet interrupts. In 4.17 and later versions, workloads can optionally be labeled as sensitive.

The decision regarding which specific CPUs should be used for reserved and isolated partitions requires detailed analysis and measurements. Factors like NUMA affinity of devices and memory play a role. The selection also depends on the workload architecture and the specific use case.

> [!IMPORTANT]
> The reserved and isolated CPU pools must not overlap and together must span all available cores in the worker node.

To ensure that housekeeping tasks and workloads do not interfere with each other, specify two groups of CPUs in the `spec` section of the performance profile.

- `isolated` - Specifies the CPUs for the application container workloads. These CPUs have the lowest latency. Processes in this group have no interruptions and can, for example, reach much higher DPDK zero packet loss bandwidth.

- `reserved` - Specifies the CPUs for the cluster and operating system housekeeping duties. Threads in the `reserved` group are often busy. Do not run latency-sensitive applications in the `reserved` group. Latency-sensitive applications run in the `isolated` group.

# Partitioning CPUs for infra and application containers

By partitioning CPUs, you can prevent noisy processes from interfering with latency-sensitive processes by separating the processes from each other.

<div>

<div class="title">

Procedure

</div>

1.  Create a performance profile appropriate for the environment’s hardware and topology. The following example adds the `reserved` and `isolated` parameters with the CPUs you want reserved and isolated for the infra and application containers:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: infra-cpus
    spec:
      cpu:
        reserved: "0-4,9"
        isolated: "5-8"
      nodeSelector:
        node-role.kubernetes.io/worker: ""
    # ...
    ```

    where:

    `spec.cpu.reserved`
    Specifies which CPUs are for infra containers to perform cluster and operating system housekeeping duties.

    `spec.cpu.isolated`
    Specifies which CPUs are for application containers to run workloads.

    `spec.nodeSelector`
    Specifies a node selector to apply the performance profile to specific nodes. Optional parameter.

</div>

# Configuring Hyper-Threading for a cluster

To configure Hyper-Threading for an OpenShift Container Platform cluster, set the CPU threads in the performance profile to the same cores that are configured for the reserved or isolated CPU pools.

> [!NOTE]
> If you configure a performance profile, and subsequently change the Hyper-Threading configuration for the host, ensure that you update the CPU `isolated` and `reserved` fields in the `PerformanceProfile` YAML to match the new configuration.

> [!WARNING]
> Disabling a previously enabled host Hyper-Threading configuration can cause the CPU core IDs listed in the `PerformanceProfile` YAML to be incorrect. This incorrect configuration can cause the node to become unavailable because the listed CPUs can no longer be found.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Ascertain which threads are running on what CPUs for the host you want to configure.

    You can view which threads are running on the host CPUs by logging in to the cluster and running the following command:

    ``` terminal
    $ lscpu --all --extended
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    CPU NODE SOCKET CORE L1d:L1i:L2:L3 ONLINE MAXMHZ    MINMHZ
    0   0    0      0    0:0:0:0       yes    4800.0000 400.0000
    1   0    0      1    1:1:1:0       yes    4800.0000 400.0000
    2   0    0      2    2:2:2:0       yes    4800.0000 400.0000
    3   0    0      3    3:3:3:0       yes    4800.0000 400.0000
    4   0    0      0    0:0:0:0       yes    4800.0000 400.0000
    5   0    0      1    1:1:1:0       yes    4800.0000 400.0000
    6   0    0      2    2:2:2:0       yes    4800.0000 400.0000
    7   0    0      3    3:3:3:0       yes    4800.0000 400.0000
    ```

    </div>

    In this example, there are eight logical CPU cores running on four physical CPU cores. CPU0 and CPU4 are running on physical Core0, CPU1 and CPU5 are running on physical Core 1, and so on. Alternatively, to view the threads that are set for a particular physical CPU core (`cpu0` in the example below), open a shell prompt and run the following:

    ``` terminal
    $ cat /sys/devices/system/cpu/cpu0/topology/thread_siblings_list
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    0-4
    ```

    </div>

2.  Apply the isolated and reserved CPUs in the `PerformanceProfile` YAML. For example, you can set logical cores CPU0 and CPU4 as `isolated`, and logical cores CPU1 to CPU3 and CPU5 to CPU7 as `reserved`. When you configure reserved and isolated CPUs, the infra containers in pods use the reserved CPUs and the application containers use the isolated CPUs.

    ``` yaml
    ...
      cpu:
        isolated: 0,4
        reserved: 1-3,5-7
    ...
    ```

    > [!NOTE]
    > The reserved and isolated CPU pools must not overlap and together must span all available cores in the worker node.

    > [!IMPORTANT]
    > Hyper-Threading is enabled by default on most Intel processors. If you enable Hyper-Threading, all threads processed by a particular core must be isolated or processed on the same core.
    >
    > When Hyper-Threading is enabled, all guaranteed pods must use multiples of the simultaneous multi-threading (SMT) level to avoid a "noisy neighbor" situation that can cause the pod to fail. See [Static policy options](https://kubernetes.io/docs/tasks/administer-cluster/cpu-management-policies/#static-policy-options) for more information.

</div>

# Disabling Hyper-Threading for low latency applications

When configuring clusters for low latency processing, consider whether you want to disable Hyper-Threading before you deploy the cluster.

To disable Hyper-Threading, perform the following steps:

<div>

<div class="title">

Procedure

</div>

- Create a performance profile that is appropriate for your hardware and topology. The following example sets `nosmt` as an additional kernel argument:

  <div class="formalpara">

  <div class="title">

  Example performance profile

  </div>

  ``` yaml
  apiVersion: performance.openshift.io/v2
  kind: PerformanceProfile
  metadata:
    name: example-performanceprofile
  spec:
    additionalKernelArgs:
      - nmi_watchdog=0
      - audit=0
      - mce=off
      - processor.max_cstate=1
      - idle=poll
      - intel_idle.max_cstate=0
      - nosmt
    cpu:
      isolated: 2-3
      reserved: 0-1
    hugepages:
      defaultHugepagesSize: 1G
      pages:
        - count: 2
          node: 0
          size: 1G
    nodeSelector:
      node-role.kubernetes.io/performance: ''
    realTimeKernel:
      enabled: true
  ```

  </div>

  > [!NOTE]
  > When you configure reserved and isolated CPUs, the infra containers in pods use the reserved CPUs and the application containers use the isolated CPUs.

</div>

# Managing device interrupt processing for guaranteed pod isolated CPUs

The Node Tuning Operator can manage host CPUs by dividing them into reserved CPUs for cluster and operating system housekeeping duties, including pod infra containers, and isolated CPUs for application containers to run the workloads. By completing these tasks, you can set CPUs for low-latency workloads as isolated workloads.

Device interrupts are load balanced between all isolated and reserved CPUs to avoid CPUs being overloaded, with the exception of CPUs where there is a guaranteed pod running. Guaranteed pod CPUs are prevented from processing device interrupts when the relevant annotations are set for the pod.

In the performance profile, `globallyDisableIrqLoadBalancing` is used to manage whether device interrupts are processed or not. For certain workloads, the reserved CPUs are not always sufficient for dealing with device interrupts, and for this reason, device interrupts are not globally disabled on the isolated CPUs. By default, Node Tuning Operator does not disable device interrupts on isolated CPUs.

## Finding the effective IRQ affinity setting for a node

Some IRQ controllers lack support for an IRQ affinity setting and might always expose all online CPUs as the IRQ mask. Because these IRQ controllers effectively run on CPU 0, you must find the effective IRQ affinity setting for a node.

The following are examples of drivers and hardware that Red Hat are aware lack support for IRQ affinity setting. The list is, by no means, exhaustive:

- Some RAID controller drivers, such as `megaraid_sas`

- Many non-volatile memory express (NVMe) drivers

- Some LAN on motherboard (LOM) network controllers

- The driver uses `managed_irqs`

> [!NOTE]
> The reason they do not support IRQ affinity setting might be associated with factors such as the type of processor, the IRQ controller, or the circuitry connections in the motherboard.

If the effective affinity of any IRQ is set to an isolated CPU, it might be a sign of some hardware or driver not supporting IRQ affinity setting. To find the effective affinity, log in to the host and run the following command:

``` terminal
$ find /proc/irq -name effective_affinity -printf "%p: " -exec cat {} \;
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
/proc/irq/0/effective_affinity: 1
/proc/irq/1/effective_affinity: 8
/proc/irq/2/effective_affinity: 0
/proc/irq/3/effective_affinity: 1
/proc/irq/4/effective_affinity: 2
/proc/irq/5/effective_affinity: 1
/proc/irq/6/effective_affinity: 1
/proc/irq/7/effective_affinity: 1
/proc/irq/8/effective_affinity: 1
/proc/irq/9/effective_affinity: 2
/proc/irq/10/effective_affinity: 1
/proc/irq/11/effective_affinity: 1
/proc/irq/12/effective_affinity: 4
/proc/irq/13/effective_affinity: 1
/proc/irq/14/effective_affinity: 1
/proc/irq/15/effective_affinity: 1
/proc/irq/24/effective_affinity: 2
/proc/irq/25/effective_affinity: 4
/proc/irq/26/effective_affinity: 2
/proc/irq/27/effective_affinity: 1
/proc/irq/28/effective_affinity: 8
/proc/irq/29/effective_affinity: 4
/proc/irq/30/effective_affinity: 4
/proc/irq/31/effective_affinity: 8
/proc/irq/32/effective_affinity: 8
/proc/irq/33/effective_affinity: 1
/proc/irq/34/effective_affinity: 2
```

</div>

Some drivers use `managed_irqs`, whose affinity is managed internally by the kernel and userspace cannot change the affinity. In some cases, these IRQs might be assigned to isolated CPUs. For more information about `managed_irqs`, see "Affinity of managed interrupts cannot be changed even if they target isolated CPU".

<div>

<div class="title">

Additional resources

</div>

- [Affinity of managed interrupts cannot be changed even if they target isolated CPU](https://access.redhat.com/solutions/4819541)

</div>

## Configuring node interrupt affinity

Configure a cluster node for IRQ dynamic load balancing to control which cores can receive device interrupt requests (IRQ).

<div>

<div class="title">

Prerequisites

</div>

- For core isolation, all server hardware components must support IRQ affinity. To check if the hardware components of your server support IRQ affinity, view the hardware specifications of the server or contact your hardware provider.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform cluster as a user with cluster-admin privileges.

2.  Set the performance profile `apiVersion` to use `performance.openshift.io/v2`.

3.  Remove the `globallyDisableIrqLoadBalancing` field or set it to `false`.

4.  Set the appropriate isolated and reserved CPUs. The following snippet illustrates a profile that reserves 2 CPUs. IRQ load-balancing is enabled for pods running on the `isolated` CPU set:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: dynamic-irq-profile
    spec:
      cpu:
        isolated: 2-5
        reserved: 0-1
    ...
    ```

    > [!NOTE]
    > When you configure reserved and isolated CPUs, operating system processes, kernel processes, and systemd services run on reserved CPUs. Infrastructure pods run on any CPU except where the low latency workload is running. Low latency workload pods run on exclusive CPUs from the isolated pool. For more information, see "Partitioning CPUs for infra and application containers".

</div>

# Configuring memory page sizes

By configuring memory page sizes, system administrators can implement more efficient memory management on a specific node to suit workload requirements. The Node Tuning Operator provides a method for configuring huge pages and kernel page sizes by using a performance profile.

## Configuring kernel page sizes

Use the `kernelPageSize` specification in a performance profile to configure the kernel page size on a specific node. Specify larger kernel page sizes for memory-intensive, high-performance workloads.

> [!NOTE]
> For nodes with an x86_64 or AMD64 architecture, you can only specify `4k` for the `kernelPageSize` specification. For nodes with an AArch64 architecture, you can specify `4k` or `64k` for the `kernelPageSize` specification. You must disable the realtime kernel before you can use the `64k` option. The default value is `4k`.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a performance profile to target nodes where you want to configure the kernel page size by creating a YAML file that defines the `PerformanceProfile` resource:

    <div class="formalpara">

    <div class="title">

    Example `pp-kernel-pages.yaml` file

    </div>

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
        name: example-performance-profile
    #...
    spec:
        kernelPageSize: "64k"
        realTimeKernel:
            enabled: false
        nodeSelector:
            node-role.kubernetes.io/worker: ""
    ```

    </div>

    where:

    `spec.kernelPageSize`
    Specifies a kernel page size of `64k`. You can only specify `64k` for nodes with an AArch64 architecture. The default value is `4k`.

    `spec.realTimeKernel.enabled:false`
    Specifies whether to disable the realtime kernel. A setting of `false` disables the kernel. You must disable the realtime kernel to use the `64k` kernel page size option.

    `spec.nodeSelector.node-role.kubernetes.io/worker`
    Specifies targets nodes with the `worker` role.

2.  Apply the performance profile to the cluster:

    ``` bash
    $ oc create -f pp-kernel-pages.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

        performanceprofile.performance.openshift.io/example-performance-profile created

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Start a debug session on the node where you applied the performance profile by running the following command:

    ``` bash
    $ oc debug node/<node_name>
    ```

    - `<node_name>`: Replace `<node_name>` with the name of the node with the performance profile applied.

2.  Verify that the kernel page size is set to the value you specified in the performance profile by running the following command:

    ``` bash
    $ getconf PAGESIZE
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

        65536

    </div>

</div>

## Configuring huge pages

Because nodes must pre-allocate huge pages used in an OpenShift Container Platform cluster, use the Node Tuning Operator to allocate huge pages on a specific node.

OpenShift Container Platform provides a method for creating and allocating huge pages. Node Tuning Operator provides an easier method for doing this using the performance profile.

<div>

<div class="title">

Procedure

</div>

- In the `hugepages.pages` section of the performance profile, specify multiple blocks of `size`, `count`, and, optionally, `node`:

  <div class="formalpara">

  <div class="title">

  Example configuration

  </div>

  ``` yaml
  hugepages:
     defaultHugepagesSize: "1G"
     pages:
     - size:  "1G"
       count:  4
       node:  0
  # ...
  ```

  </div>

  where:

  `hugepages.pages.node`
  Specifies the `node` that is the NUMA node in which the huge pages are allocated. If you omit `node`, the pages are evenly spread across all NUMA nodes.

  > [!NOTE]
  > Wait for the relevant machine config pool status that indicates the update is finished.

  These are the only configuration steps you need to do to allocate huge pages.

</div>

<div>

<div class="title">

Verification

</div>

- To verify the configuration, see the `/proc/meminfo` file on the node:

  ``` terminal
  $ oc debug node/ip-10-0-141-105.ec2.internal
  ```

  ``` terminal
  # grep -i huge /proc/meminfo
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  AnonHugePages:    ###### ##
  ShmemHugePages:        0 kB
  HugePages_Total:       2
  HugePages_Free:        2
  HugePages_Rsvd:        0
  HugePages_Surp:        0
  Hugepagesize:       #### ##
  Hugetlb:            #### ##
  ```

  </div>

- Use `oc describe` to report the new size:

  ``` terminal
  $ oc describe node worker-0.ocp4poc.example.com | grep -i huge
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
                                     hugepages-1g=true
   hugepages-###:  ###
   hugepages-###:  ###
  ```

  </div>

</div>

## Allocating multiple huge page sizes

You can request huge pages with different sizes under the same container. By doing this task, you can define more complicated pods consisting of containers with different huge page size needs.

The following example, shows you how to define sizes `1G` and `2M`. The Node Tuning Operator configures both sizes on the node.

<div>

<div class="title">

Procedure

</div>

- Edit the `PerformanceProfile` object to define `1G` and `2M` sizes for the huge pages. The Node Tuning Operator configures both sizes on the node.

  ``` yaml
  apiVersion: performance.openshift.io/v2
  kind: PerformanceProfile
  metadata:
      name: example-performance-profile
  #...
  spec:
    hugepages:
      defaultHugepagesSize: 1G
      pages:
      - count: 1024
        node: 0
        size: 2M
      - count: 4
        node: 1
        size: 1G
  # ...
  ```

</div>

# Reducing NIC queues using the Node Tuning Operator

The Node Tuning Operator facilitates reducing NIC queues for enhanced performance. Adjustments are made using the performance profile, allowing customization of queues for different network devices.

## Adjusting the NIC queues with the performance profile

You can use a performance profile to adjust the queue count for each network device. By using the Node Tuning Operator, you can reduce NIC queues for enhanced performance.

Supported network devices:

- Non-virtual network devices

- Network devices that support multiple queues (channels)

Unsupported network devices:

- Pure software network interfaces

- Block devices

- Intel DPDK virtual functions

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Install the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform cluster running the Node Tuning Operator as a user with `cluster-admin` privileges.

2.  Create and apply a performance profile appropriate for your hardware and topology. For guidance on creating a profile, see the "Creating a performance profile" section.

3.  Edit this created performance profile:

    ``` terminal
    $ oc edit -f <your_profile_name>.yaml
    ```

4.  Populate the `spec` field with the `net` object. The object list can contain two fields:

    - `userLevelNetworking` is a required field specified as a boolean flag. If `userLevelNetworking` is `true`, the queue count is set to the reserved CPU count for all supported devices. The default is `false`.

    - `devices` is an optional field specifying a list of devices that will have the queues set to the reserved CPU count. If the device list is empty, the configuration applies to all network devices. The configuration is as follows:

      - `interfaceName`: This field specifies the interface name, and it supports shell-style wildcards, which can be positive or negative.

        - Example wildcard syntax is as follows: `<string> .*`

        - Negative rules are prefixed with an exclamation mark. To apply the net queue changes to all devices other than the excluded list, use `!<device>`, for example, `!eno1`.

      - `vendorID`: The network device vendor ID represented as a 16-bit hexadecimal number with a `0x` prefix.

      - `deviceID`: The network device ID (model) represented as a 16-bit hexadecimal number with a `0x` prefix.

        > [!NOTE]
        > When a `deviceID` is specified, the `vendorID` must also be defined. A device that matches all of the device identifiers specified in a device entry `interfaceName`, `vendorID`, or a pair of `vendorID` plus `deviceID` qualifies as a network device. This network device then has its net queues count set to the reserved CPU count.
        >
        > When two or more devices are specified, the net queues count is set to any net device that matches one of them.

5.  Set the queue count to the reserved CPU count for all devices by using this example performance profile:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: manual
    spec:
      cpu:
        isolated: 3-51,55-103
        reserved: 0-2,52-54
      net:
        userLevelNetworking: true
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    # ...
    ```

6.  Set the queue count to the reserved CPU count for all devices matching any of the defined device identifiers by using this example performance profile:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: manual
    spec:
      cpu:
        isolated: 3-51,55-103
        reserved: 0-2,52-54
      net:
        userLevelNetworking: true
        devices:
        - interfaceName: "eth0"
        - interfaceName: "eth1"
        - vendorID: "0x1af4"
          deviceID: "0x1000"
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    # ...
    ```

7.  Set the queue count to the reserved CPU count for all devices starting with the interface name `eth` by using this example performance profile:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: manual
    spec:
      cpu:
        isolated: 3-51,55-103
        reserved: 0-2,52-54
      net:
        userLevelNetworking: true
        devices:
        - interfaceName: "eth*"
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    # ...
    ```

8.  Set the queue count to the reserved CPU count for all devices with an interface named anything other than `eno1` by using this example performance profile:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: manual
    spec:
      cpu:
        isolated: 3-51,55-103
        reserved: 0-2,52-54
      net:
        userLevelNetworking: true
        devices:
        - interfaceName: "!eno1"
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    # ...
    ```

9.  Set the queue count to the reserved CPU count for all devices that have an interface name `eth0`, `vendorID` of `0x1af4`, and `deviceID` of `0x1000` by using this example performance profile:

    ``` yaml
    apiVersion: performance.openshift.io/v2
    kind: PerformanceProfile
    metadata:
      name: manual
    spec:
      cpu:
        isolated: 3-51,55-103
        reserved: 0-2,52-54
      net:
        userLevelNetworking: true
        devices:
        - interfaceName: "eth0"
        - vendorID: "0x1af4"
          deviceID: "0x1000"
      nodeSelector:
        node-role.kubernetes.io/worker-cnf: ""
    # ...
    ```

10. Apply the updated performance profile:

    ``` terminal
    $ oc apply -f <your_profile_name>.yaml
    ```

</div>

## Verifying the queue status

To ensure that your performance profile changes are active, verify the queue status.

By reviewing the provided examples, you can confirm that specific tuning configurations are successfully applied to your environment.

In this section, several examples illustrate different performance profiles and how to verify the changes are applied.

Example 1
Example 1 demonstrates that the net queue count that is set to the reserved CPU count (2) for *all* supported devices.

The relevant section from the performance profile is:

``` yaml
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
  spec:
    cpu:
      reserved: 0-1  #total = 2
      isolated: 2-8
    net:
      userLevelNetworking: true
# ...
```

The following command displays the status of the queues associated with a device:

> [!NOTE]
> Run this command on the node where the performance profile was applied.

``` terminal
$ ethtool -l <device>
```

The following command verifies the queue status before the profile is applied:

``` terminal
$ ethtool -l ens4
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   4
```

</div>

The following command verifies the queue status after the profile is applied:

``` terminal
$ ethtool -l ens4
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```

</div>

- `Combined`: Specifies the combined channel that shows the total count of reserved CPUs for *all* supported devices is 2. This matches what is configured in the performance profile.

Example 2
Example 2 demonstrates that the net queue count is set to the reserved CPU count (2) for *all* supported network devices with a specific `vendorID`.

The relevant section from the performance profile is:

``` yaml
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
  spec:
    cpu:
      reserved: 0-1
      isolated: 2-8
    net:
      userLevelNetworking: true
      devices:
      - vendorID = 0x1af4
# ...
```

The following command displays the status of the queues associated with a device:

> [!NOTE]
> Run this command on the node where the performance profile was applied.

``` terminal
$ ethtool -l <device>
```

The following command verifies the queue status after the profile is applied:

``` terminal
$ ethtool -l ens4
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```

</div>

- `Combined`: Specifies that the total count of reserved CPUs for all supported devices with `vendorID=0x1af4` is 2. For example, if there is another network device `ens2` with `vendorID=0x1af4` it will also have total net queues of 2. This matches what is configured in the performance profile.

Example 3
Example 3 shows that the net queue count is set to the reserved CPU count (2) for *all* supported network devices that match any of the defined device identifiers. The command `udevadm info` provides a detailed report on a device. In this example the devices are:

``` terminal
# udevadm info -p /sys/class/net/ens4
...
E: ID_MODEL_ID=0x1000
E: ID_VENDOR_ID=0x1af4
E: INTERFACE=ens4
...
```

``` terminal
# udevadm info -p /sys/class/net/eth0
...
E: ID_MODEL_ID=0x1002
E: ID_VENDOR_ID=0x1001
E: INTERFACE=eth0
...
```

Set the net queues to 2 for a device with `interfaceName` equal to `eth0` and any devices that have a `vendorID=0x1af4` with the following performance profile:

``` terminal
apiVersion: performance.openshift.io/v2
metadata:
  name: performance
spec:
  kind: PerformanceProfile
    spec:
      cpu:
        reserved: 0-1  #total = 2
        isolated: 2-8
      net:
        userLevelNetworking: true
        devices:
        - interfaceName = eth0
        - vendorID = 0x1af4
# ...
```

The following command verifies the queue status after the profile is applied:

``` terminal
$ ethtool -l ens4
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Channel parameters for ens4:
Pre-set maximums:
RX:         0
TX:         0
Other:      0
Combined:   4
Current hardware settings:
RX:         0
TX:         0
Other:      0
Combined:   2
```

</div>

- `Combined`: Specifies that the total count of reserved CPUs for all supported devices with `vendorID=0x1af4` is set to 2.

  For example, if there is another network device `ens2` with `vendorID=0x1af4`, it will also have the total net queues set to 2. Similarly, a device with `interfaceName` equal to `eth0` will have total net queues set to 2.

## Logging associated with adjusting NIC queues

To verify NIC queue adjustments, review the Tuned daemon logs. These log messages detail the assigned devices that are recorded in the respective Tuned daemon logs.

The following messages might be recorded to the `/var/log/tuned/tuned.log` file:

- An `INFO` message is recorded detailing the successfully assigned devices:

  ``` terminal
  INFO tuned.plugins.base: instance net_test (net): assigning devices ens1, ens2, ens3
  ```

- A `WARNING` message is recorded if none of the devices can be assigned:

  ``` terminal
  WARNING  tuned.plugins.base: instance net_test: no matching devices available
  ```
