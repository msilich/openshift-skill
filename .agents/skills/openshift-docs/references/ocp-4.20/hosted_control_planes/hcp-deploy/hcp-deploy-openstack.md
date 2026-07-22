<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

> [!IMPORTANT]
> Deploying hosted control planes clusters on Red Hat OpenStack Platform (RHOSP) is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

You can deploy hosted control planes with hosted clusters that run on Red Hat OpenStack Platform (RHOSP) 17.1.

A *hosted cluster* is an OpenShift Container Platform cluster with its API endpoint and control plane that are hosted on a management cluster. With hosted control planes, control planes exist as pods on a management cluster without the need for dedicated virtual or physical machines for each control plane.

# Prerequisites for OpenStack

Before you create a hosted cluster on Red Hat OpenStack Platform (RHOSP), ensure that you meet the prerequisites.

- You have administrative access to a management OpenShift Container Platform cluster version 4.17 or greater. This cluster can run on bare metal, RHOSP, or a supported public cloud.

- The HyperShift Operator is installed on the management cluster as specified in "Preparing to deploy hosted control planes".

- The management cluster is configured with OVN-Kubernetes as the default pod network CNI.

- The OpenShift CLI (`oc`) and hosted control planes CLI, `hcp` are installed.

- A load-balancer backend, for example, Octavia, is installed on the management OCP cluster. The load balancer is required for the `kube-api` service to be created for each hosted cluster.

  - When ingress is configured with an Octavia load balance, the RHOSP Octavia service is running in the cloud that hosts the guest cluster.

- A valid pull secret file is present for the `quay.io/openshift-release-dev` repository.

- The default external network for the management cluster is reachable from the guest cluster. The `kube-apiserver` load-balancer type service is created on this network.

- If you use a pre-defined floating IP address for ingress, you created a DNS record that points to it for the following wildcard domain: `*.apps.<cluster_name>.<base_domain>`, where:

  - `<cluster_name>` is the name of the management cluster.

  - `<base_domain>` is the parent DNS domain under which your cluster’s applications live.

<div>

<div class="title">

Additional resources

</div>

- [Pull secret](https://console.redhat.com/openshift/install/platform-agnostic/user-provisioned)

</div>

# Preparing the management cluster for etcd local storage

In a hosted control planes deployment on Red Hat OpenStack Platform (RHOSP), you can improve etcd performance by using local ephemeral storage that is provisioned with the TopoLVM CSI driver instead of relying on the default Cinder-based Persistent Volume Claims (PVCs).

<div>

<div class="title">

Prerequisites

</div>

- You have access to a management cluster with HyperShift installed.

- You can create and manage RHOSP flavors and machine sets.

- You have the `oc` and `openstack` CLI tools installed and configured.

- You are familiar with TopoLVM and Logical Volume Manager (LVM) storage concepts.

- You installed the LVM Storage Operator on the management cluster. For more information, see "Installing LVM Storage by using the CLI" in the Storage section of the OpenShift Container Platform documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a Nova flavor with an additional ephemeral disk by using the `openstack` CLI. For example:

    ``` terminal
    $ openstack flavor create \
      --id auto \
      --ram 8192 \
      --disk 0 \
      --ephemeral 100 \
      --vcpus 4 \
      --public \
      hcp-etcd-ephemeral
    ```

    > [!NOTE]
    > Nova automatically attaches the ephemeral disk to the instance and formats it as `vfat` when a server is created with that flavor.

2.  Create a compute machine set that uses the new flavor. For more information, see "Creating a compute machine set on OpenStack" in the OpenShift Container Platform documentation.

3.  Scale the machine set to meet your requirements. If clusters are deployed for high availability, a minimum of 3 workers must be deployed so the pods can be distributed accordingly.

4.  Label the new worker nodes to identify them for etcd use. For example:

    ``` terminal
    $ oc label node <node_name> hypershift-capable=true
    ```

    This label is arbitrary; you can update it later.

5.  In a file called `lvmcluster.yaml`, create the following `LVMCluster` custom resource to the local storage configuration for etcd:

    ``` yaml
    apiVersion: lvm.topolvm.io/v1alpha1
    kind: LVMCluster
    metadata:
      name: etcd-hcp
      namespace: openshift-storage
    spec:
      storage:
        deviceClasses:
        - name: etcd-class
          default: true
          nodeSelector:
             nodeSelectorTerms:
             - matchExpressions:
               - key: hypershift-capable
                operator: In
                values:
                - "true"
          deviceSelector:
            forceWipeDevicesAndDestroyAllData: true
            paths:
            - /dev/vdb
    ```

    In this example resource:

    - The ephemeral disk location is `/dev/vdb`, which is the case in most situations. Verify that this location is true in your case, and note that symlinks are not supported.

    - The parameter `forceWipeDevicesAndDestroyAllData` is set to a `True` value because the default Nova ephemeral disk comes formatted in VFAT.

6.  Apply the `LVMCluster` resource by running the following command:

    ``` terminal
    oc apply -f lvmcluster.yaml
    ```

7.  Verify the `LVMCluster` resource by running the following command:

    ``` terminal
    $ oc get lvmcluster -A
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAMESPACE           NAME    STATUS
    openshift-storage   etcd-hcp   Ready
    ```

    </div>

8.  Verify the `StorageClass` resource by running the following command:

    ``` terminal
    $ oc get storageclass
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                    PROVISIONER               RECLAIMPOLICY   VOLUMEBINDINGMODE     ALLOWVOLUMEEXPANSION   AGE
    lvms-etcd-class         topolvm.io                Delete          WaitForFirstConsumer  true                   23m
    standard-csi (default)  cinder.csi.openstack.org  Delete          WaitForFirstConsumer  true                   56m
    ```

    </div>

    You can now deploy a hosted cluster with a performant etcd configuration. The deployment process is described in "Creating a hosted cluster on OpenStack".

</div>

# Creating a floating IP for ingress

If you want to make ingress available in a hosted cluster without manual intervention, you can create a floating IP address for it in advance.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the Red Hat OpenStack Platform (RHOSP) cloud.

- If you use a pre-defined floating IP address for ingress, you created a DNS record that points to it for the following wildcard domain: `*.apps.<cluster_name>.<base_domain>`, where:

  - `<cluster_name>` is the name of the management cluster.

  - `<base_domain>` is the parent DNS domain under which your cluster’s applications live.

</div>

<div>

<div class="title">

Procedure

</div>

- Create a floating IP address by running the following command:

  ``` terminal
  $ openstack floating ip create <external_network_id>
  ```

  where:

  `<external_network_id>`
  Specifies the ID of the external network.

  > [!NOTE]
  > If you specify a floating IP address by using the `--openstack-ingress-floating-ip` flag without creating it in advance, the `cloud-provider-openstack` component attempts to create it automatically. This process only succeeds if the Neutron API policy permits creating a floating IP address with a specific IP address.

</div>

# Uploading the RHCOS image to OpenStack

If you want to specify the RHCOS image to use when deploying node pools on hosted control planes and Red Hat OpenStack Platform (RHOSP) deployment, upload the image to the RHOSP cloud.

If you do not upload the image, the OpenStack Resource Controller (ORC) downloads an image from the OpenShift Container Platform mirror and deletes the image after deletion of the hosted cluster.

<div>

<div class="title">

Prerequisites

</div>

- You downloaded the RHCOS image from the OpenShift Container Platform mirror.

- You have access to your RHOSP cloud.

</div>

<div>

<div class="title">

Procedure

</div>

- Upload an RHCOS image to RHOSP by running the following command:

  ``` terminal
  $ openstack image create --disk-format qcow2 --file <image_file_name> rhcos
  ```

  where:

  `<image_file_name>`
  Specifies the file name of the RHCOS image.

</div>

# Creating a hosted cluster on OpenStack

You can create a hosted cluster on Red Hat OpenStack Platform (RHOSP) by using the `hcp` CLI.

<div>

<div class="title">

Prerequisites

</div>

- You completed all prerequisite steps in "Preparing to deploy hosted control planes".

- You reviewed "Prerequisites for OpenStack".

- You completed all steps in "Preparing the management cluster for etcd local storage".

- You have access to the management cluster.

- You have access to the RHOSP cloud.

</div>

<div>

<div class="title">

Procedure

</div>

- Create a hosted cluster by running the `hcp create` command. For example, for a cluster that takes advantage of the performant etcd configuration detailed in "Preparing the management cluster for etcd local storage", enter:

  ``` terminal
  $ hcp create cluster openstack \
    --name my-hcp-cluster \
    --openstack-node-flavor m1.xlarge \
    --base-domain example.com \
    --pull-secret /path/to/pull-secret.json \
    --release-image quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64 \
    --node-pool-replicas 3 \
    --etcd-storage-class lvms-etcd-class
  ```

  > [!NOTE]
  > Many options are available at cluster creation. For RHOSP-specific options, see "Options for creating a Hosted Control Planes cluster on OpenStack". For general options, see the `hcp` documentation.

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the hosted cluster is ready by running the following command on it:

    ``` terminal
    $ oc -n clusters-<cluster_name> get pods
    ```

    where:

    `<cluster_name>`
    Specifies the name of the cluster.

    After several minutes, the output should show that the hosted control plane pods are running.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                                  READY   STATUS    RESTARTS   AGE
    capi-provider-5cc7b74f47-n5gkr                        1/1     Running   0          3m
    catalog-operator-5f799567b7-fd6jw                     2/2     Running   0          69s
    certified-operators-catalog-784b9899f9-mrp6p          1/1     Running   0          66s
    cluster-api-6bbc867966-l4dwl                          1/1     Running   0          66s
    ...
    ...
    ...
    redhat-operators-catalog-9d5fd4d44-z8qqk              1/1     Running   0
    ```

    </div>

2.  To validate the etcd configuration of the cluster:

    1.  Validate the etcd persistent volume claim (PVC) by running the following command:

        ``` terminal
        $ oc get pvc -A
        ```

    2.  Inside the hosted control planes etcd pod, confirm the mount path and device by running the following command:

        ``` terminal
        $ df -h /var/lib
        ```

        > [!NOTE]
        > The RHOSP resources that the cluster API provider creates are tagged with the label `openshiftClusterID=<infraID>`.
        >
        > You can define additional tags for the resources as values in the `HostedCluster.Spec.Platform.OpenStack.Tags` field of a YAML manifest that you use to create the hosted cluster. After you scale up the node pool, the tags apply to resources.

</div>

## Options for creating a Hosted Control Planes cluster on OpenStack

You can supply several options to the `hcp` CLI while deploying a Hosted Control Planes Cluster on Red Hat OpenStack Platform (RHOSP).

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Required</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--openstack-ca-cert-file</code></p></td>
<td style="text-align: left;"><p>Path to the OpenStack CA certificate file. If not provided, this will be automatically extracted from the cloud entry in <code>clouds.yaml</code>.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-cloud</code></p></td>
<td style="text-align: left;"><p>Name of the cloud entry in <code>clouds.yaml</code>. The default value is <code>openstack</code>.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-credentials-file</code></p></td>
<td style="text-align: left;"><p>Path to the OpenStack credentials file. If not provided, <code>hcp</code> will search the following directories:</p>
<ul>
<li><p>The current working directory</p></li>
<li><p><code>$HOME/.config/openstack</code></p></li>
<li><p><code>/etc/openstack</code></p></li>
</ul></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-dns-nameservers</code></p></td>
<td style="text-align: left;"><p>List of DNS server addresses that are provided when creating the subnet.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-external-network-id</code></p></td>
<td style="text-align: left;"><p>ID of the OpenStack external network.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-ingress-floating-ip</code></p></td>
<td style="text-align: left;"><p>A floating IP for OpenShift ingress.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-node-additional-port</code></p></td>
<td style="text-align: left;"><p>Additional ports to attach to nodes. Valid values are: <code>network-id</code>, <code>vnic-type</code>, <code>disable-port-security</code>, and <code>address-pairs</code>.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-node-availability-zone</code></p></td>
<td style="text-align: left;"><p>Availability zone for the node pool.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-node-flavor</code></p></td>
<td style="text-align: left;"><p>Flavor for the node pool.</p></td>
<td style="text-align: left;"><p>Yes</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--openstack-node-image-name</code></p></td>
<td style="text-align: left;"><p>Image name for the node pool.</p></td>
<td style="text-align: left;"><p>No</p></td>
</tr>
</tbody>
</table>
