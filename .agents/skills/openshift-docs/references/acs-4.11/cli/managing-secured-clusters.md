<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To secure a Kubernetes or an OpenShift Container Platform cluster, you must deploy Red Hat Advanced Cluster Security for Kubernetes (RHACS) services into the cluster. You can generate deployment files in the RHACS portal by navigating to the **Platform Configuration → Clusters** view, or you can use the `roxctl` CLI.

<a id="setting-up-environment-variables_managing-secured-clusters"></a>

# Prerequisites

Configure the `ROX_ENDPOINT` environment variable to specify the host and port information for Central.

<div>

<div class="title">

Procedure

</div>

- To configure the `ROX_ENDPOINT` environment variable, run the following command:

  ``` terminal
  $ export ROX_ENDPOINT=<host:port>
  ```

  where:

  `<host:port>`  
  Specifies the host and port information that you want to store in the `ROX_ENDPOINT` environment variable.

</div>

<a id="generating-sensor-deployment-files_managing-secured-clusters"></a>

# Generating Sensor deployment files

You can generate Sensor deployment files for both Kubernetes and OpenShift Container Platform systems by using the `roxctl` CLI. The deployment files contain the necessary configuration to deploy and associate Sensor with your Central instance.

<a id="generating-sensor-k8s_managing-secured-clusters"></a>

## Generating Sensor files for Kubernetes systems

You can generate the required Sensor configuration for your Kubernetes cluster and associate it with your Central instance by using the `roxctl` CLI.

<div>

<div class="title">

Procedure

</div>

- To generate the required sensor configuration for your Kubernetes cluster and associate it with your Central instance, run the following command:

  ``` terminal
  $ roxctl sensor generate k8s --name <cluster_name> --central "$ROX_ENDPOINT"
  ```

</div>

<a id="generating-sensor-openshift_managing-secured-clusters"></a>

## Generating Sensor files for OpenShift Container Platform systems

You can generate the required Sensor configuration for your OpenShift Container Platform cluster and associate it with your Central instance by using the `roxctl` CLI.

<div>

<div class="title">

Procedure

</div>

- To generate the required sensor configuration for your OpenShift Container Platform cluster and associate it with your Central instance, run the following command:

  ``` terminal
  $ roxctl sensor generate openshift --openshift-version <ocp_version> --name <cluster_name> --central "$ROX_ENDPOINT"
  ```

  where:

  \<ocp_version\>  
  Specifies the major OpenShift Container Platform version number for your cluster. For example, specify `3` for OpenShift Container Platform version `3.x` and specify `4` for OpenShift Container Platform version `4.x`.

  Read the `--help` output to see other options that you might need to use depending on your system architecture.

  Verify that the cluster where you are deploying Red Hat Advanced Cluster Security for Kubernetes services can reach the endpoint you give for `--central`.

  > [!IMPORTANT]
  > If you are using a non-gRPC capable load balancer, such as HAProxy, AWS Application Load Balancer (ALB), or AWS Elastic Load Balancing (ELB), follow these guidelines:
  >
  > - Use the WebSocket Secure (`wss`) protocol. To use `wss`, prefix the address with **`wss://`**.
  >
  > - Add the port number after the address, for example:
  >
  >   ``` terminal
  >   $ roxctl sensor generate k8s --central wss:
  >   ```

</div>

<a id="installing-sensor-by-using-the-sensorsh-script_managing-secured-clusters"></a>

# Installing Sensor by using the sensor.sh script

When you generate the Sensor deployment files, `roxctl` creates a directory called `sensor-<cluster_name>` in your working directory. This directory contains the script to install Sensor.

<div>

<div class="title">

Procedure

</div>

- To install Sensor, run the following command:

  ``` terminal
  $ ./sensor-<cluster_name>/sensor.sh
  ```

  If you get a warning that you do not have the required permissions to install Sensor, follow the on-screen instructions, or contact your cluster administrator for help.

</div>

<a id="downloading-sensor-bundles-for-existing-clusters_managing-secured-clusters"></a>

# Downloading Sensor bundles for existing clusters

You can download Sensor bundles for clusters that are already integrated with Central by using the `roxctl` CLI.

<div>

<div class="title">

Procedure

</div>

- To download Sensor bundles for existing clusters, specify a `cluster name` or `ID` and run the following command:

  ``` terminal
  $ roxctl sensor get-bundle <cluster_name_or_id>
  ```

</div>

<a id="deleting-cluster-integration_managing-secured-clusters"></a>

# Deleting cluster integration

You can remove a cluster integration from Central by using the `roxctl` CLI. This removes the cluster from Central’s management but does not uninstall the services running in the cluster.

<div>

<div class="title">

Procedure

</div>

- To delete the cluster integration, ensure you have the correct cluster name and run the following command:

  ``` terminal
  $ roxctl cluster delete --name=<cluster_name>
  ```

  > [!IMPORTANT]
  > Deleting the cluster integration does not remove the RHACS services running in the cluster, depending on the installation method. You can remove the services by running the `delete-sensor.sh` script from the Sensor installation bundle.

</div>
