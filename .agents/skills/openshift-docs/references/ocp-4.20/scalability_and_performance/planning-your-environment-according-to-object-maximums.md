<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To ensure your cluster meets performance and scalability requirements, plan your environment according to tested object maximums. By reviewing these limits, you can design a OpenShift Container Platform deployment that operates reliably within supported boundaries.

The example guidelines are based on the largest possible cluster. For smaller clusters, the maximums are lower. There are many factors that influence the stated thresholds, including the etcd version or storage data format. In most cases, exceeding these numbers results in lower overall performance but might not cause your cluster to fail.

> [!WARNING]
> Clusters that experience rapid change, such as those with many starting and stopping pods, can have a lower practical maximum size than documented.

# OpenShift Container Platform tested cluster maximums for major releases

To ensure your deployment remains supported, plan your cluster configuration by using tested cluster maximums. OpenShift Container Platform validates these specific limits for major releases rather than theoretical absolute cluster maximums, ensuring stability for your environment.

> [!NOTE]
> Red Hat does not provide direct guidance on sizing your OpenShift Container Platform cluster. This is because determining whether your cluster is within the supported bounds of OpenShift Container Platform requires careful consideration of all the multidimensional factors that limit the cluster scale.

OpenShift Container Platform supports tested cluster maximums rather than absolute cluster maximums. Not every combination of OpenShift Container Platform version, control plane workload, and network plugin are tested, so the following table does not represent an absolute expectation of scale for all deployments. Scaling to a maximum on all dimensions simultaneously might not be possible. The table contains tested maximums for specific workloads and deployments, and serves as a scale guide as to what can be expected with similar deployments.

| Maximum type | 4.x tested maximum | Notes |
|----|----|----|
| Number of nodes | 2,000 | Pause pods were deployed to stress the control plane components of OpenShift Container Platform at 2000 node scale. The ability to scale to similar numbers will vary depending upon specific deployment and workload parameters. |
| Number of pods | 150,000 | The pod count displayed here is the number of test pods. The actual number of pods depends on the application’s memory, CPU, and storage requirements. |
| Number of pods per node | 2,500 | This was tested on a cluster with 31 servers: 3 control planes, 2 infrastructure nodes, and 26 compute nodes. If you need 2,500 user pods, you need both a `hostPrefix` of `20`, which allocates a network large enough for each node to contain more than 2000 pods, and a custom kubelet config with `maxPods` set to `2500`. For more information, see [Running 2500 pods per node on OCP 4.13](https://cloud.redhat.com/blog/running-2500-pods-per-node-on-ocp-4.13). |
| Number of namespaces | 10,000 | When there are a large number of active projects, etcd might suffer from poor performance if the keyspace grows excessively large and exceeds the space quota. Periodic maintenance of etcd, including defragmentation, is highly recommended to free etcd storage. |
| Number of builds | 10,000 (Default pod RAM 512 Mi) - Source-to-Image (S2I) build strategy | \- |
| Number of pods per namespace | 25,000 | There are several control loops in the system that must iterate over all objects in a given namespace as a reaction to some changes in state. Having a large number of objects of a given type in a single namespace can make those loops expensive and slow down processing given state changes. The limit assumes that the system has enough CPU, memory, and disk to satisfy the application requirements. |
| Number of routes per default 2-router deployment | 9,000 | \- |
| Number of secrets | 80,000 | \- |
| Number of config maps | 90,000 | \- |
| Number of services | 10,000 | Each service port and each service back-end has a corresponding entry in `iptables`. The number of back-ends of a given service impact the size of the `Endpoints` objects, which impacts the size of data that is being sent all over the system. |
| Number of services per namespace | 5,000 | \- |
| Number of back-ends per service | 5,000 | \- |
| Number of deployments per namespace | 2,000 | \- |
| Number of build configs | 12,000 | \- |
| Number of custom resource definitions (CRD) | 1,024 | Tested on a cluster with 29 servers: 3 control planes, 2 infrastructure nodes, and 24 compute nodes. The cluster had 500 namespaces. OpenShift Container Platform has a limit of 1,024 total custom resource definitions (CRD), including those installed by OpenShift Container Platform, products integrating with OpenShift Container Platform, and user-created CRDs. If there are more than 1,024 CRDs created, then there is a possibility that `oc` command requests might be throttled. |

Example scenario
As an example, 500 compute nodes (m5.2xl) were tested, and are supported, by using OpenShift Container Platform 4.17, the OVN-Kubernetes network plugin, and the following workload objects:

- 200 namespaces, in addition to the defaults

- 60 pods per node; 30 server and 30 client pods (30k total)

- 57 image streams/ns (11.4k total)

- 15 services/ns backed by the server pods (3k total)

- 15 routes/ns backed by the previous services (3k total)

- 20 secrets/ns (4k total)

- 10 config maps/ns (2k total)

- 6 network policies/ns, including deny-all, allow-from ingress and intra-namespace rules

- 57 builds/ns

The following factors are known to affect cluster workload scaling, positively or negatively, and should be factored into the scale numbers when planning a deployment. For additional information and guidance, contact your sales representative or [Red Hat support](https://access.redhat.com/support/).

- Number of pods per node

- Number of containers per pod

- Type of probes used (for example, liveness/readiness, exec/http)

- Number of network policies

- Number of projects, or namespaces

- Number of image streams per project

- Number of builds per project

- Number of services/endpoints and type

- Number of routes

- Number of shards

- Number of secrets

- Number of config maps

- Rate of API calls, or the cluster “churn”, which is an estimation of how quickly things change in the cluster configuration.

  - Prometheus query for pod creation requests per second over 5 minute windows: `sum(irate(apiserver_request_count{resource="pods",verb="POST"}[5m]))`

  - Prometheus query for all API requests per second over 5 minute windows: `sum(irate(apiserver_request_count{}[5m]))`

- Cluster node resource consumption of CPU

- Cluster node resource consumption of memory

# OpenShift Container Platform environment and configuration on which the cluster maximums are tested

To validate your deployment limits, review the environment and configuration details for the cloud platforms on which OpenShift Container Platform cluster maximums are tested. This reference ensures your infrastructure aligns with the specific scenarios used to validate scalability limits.

## AWS cloud platform cluster maximums

| Node | Flavor | vCPU | RAM (GiB) | Disk type | Disk size (GiB) or IOS | Count | Region |
|----|----|----|----|----|----|----|----|
| Control plane/etcd | r5.4xlarge | 16 | 128 | gp3 | 220 | 3 | us-west-2 |
| Infra | m5.12xlarge | 48 | 192 | gp3 | 100 | 3 | us-west-2 |
| Workload | m5.4xlarge | 16 | 64 | gp3 | 500 | 1 | us-west-2 |
| Compute | m5.2xlarge | 8 | 32 | gp3 | 100 | 3/25/250/500 | us-west-2 |

where:

Control plane/etcd
Control plane/etcd nodes use gp3 disks with a baseline performance of 3000 IOPS and 125 MiB per second because etcd is latency sensitive. The gp3 volumes do not use burst performance.

Infra
Infra nodes are used to host Monitoring, Ingress, and Registry components to ensure they have enough resources to run at large scale.

Workload
The workload node is dedicated to run performance and scalability workload generators.

Using a larger disk size of 500 GiB ensures that there is enough space to store the large amounts of data that is collected during the performance and scalability test run.

Compute
The cluster is scaled in iterations of 3, 25, 250, and 500 compute nodes. Performance and scalability tests are executed at the specified node counts.

## IBM Power platform cluster maximums

| Node               | vCPU | RAM (GiB) | Disk type | Disk size (GiB) or IOS | Count    |
|--------------------|------|-----------|-----------|------------------------|----------|
| Control plane/etcd | 16   | 32        | io1       | 120 / 10 IOPS per GiB  | 3        |
| Infra              | 16   | 64        | gp2       | 120                    | 2        |
| Workload           | 16   | 256       | gp2       | 120                    | 1        |
| Compute            | 16   | 64        | gp2       | 120                    | 2 to 100 |

where:

Control plane/etcd
io1 disks with 120 / 10 IOPS per GiB are used for control plane/etcd nodes as etcd is I/O intensive and latency sensitive.

Infra
Infra nodes are used to host Monitoring, Ingress, and Registry components to ensure they have enough resources to run at large scale.

Workload
Workload node is dedicated to run performance and scalability workload generators.

Workload.120
Larger disk size is used so that there is enough space to store the large amounts of data that is collected during the performance and scalability test run.

Compute.2 to 100
Cluster is scaled in iterations.

## IBM Z platform cluster maximums

| Node | vCPU | RAM (GiB) | Disk type | Disk size (GiB) or IOS | Count |
|----|----|----|----|----|----|
| Control plane/etcd | 8 | 32 | ds8k | 300 / LCU 1 | 3 |
| Compute | 8 | 32 | ds8k | 150 / LCU 2 | 4 nodes (scaled to 100/250/500 pods per node) |

where:

Control plane/etcd
Nodes are distributed between two logical control units (LCUs) to optimize disk I/O load of the control plane/etcd nodes as etcd is I/O intensive and latency sensitive. Etcd I/O demand should not interfere with other workloads. Four compute nodes are used for the tests running several iterations with 100/250/500 pods at the same time. First, idling pods were used to evaluate if pods can be instanced. Next, a network and CPU demanding client/server workload were used to evaluate the stability of the system under stress. Client and server pods were pairwise deployed and each pair was spread over two compute nodes.

Compute
No separate workload node was used. The workload simulates a microservice workload between two compute nodes.

vCPU
Physical number of processors used is six Integrated Facilities for Linux (IFLs).

RAM (GiB)
Total physical memory used is 512 GiB.

# How to plan your environment according to tested cluster maximums

To ensure your infrastructure meets operational requirements, plan your OpenShift Container Platform environment according to tested cluster maximums. Designing your cluster within these validated limits ensures that you can maintain stability and ensures your deployment remains supported

> [!IMPORTANT]
> Oversubscribing the physical resources on a node affects resource guarantees the Kubernetes scheduler makes during pod placement. Learn what measures you can take to avoid memory swapping.
>
> Some of the tested maximums are stretched only in a single dimension. They will vary when many objects are running on the cluster.
>
> The numbers noted in this documentation are based on Red Hat’s test methodology, setup, configuration, and tunings. These numbers can vary based on your own individual setup and environments.

While planning your environment, determine how many pods are expected to fit per node by using the following formula:

``` text
required pods per cluster / pods per node = total number of nodes needed
```

The default maximum number of pods per node is 250. However, the number of pods that fit on a node is dependent on the application itself. Consider the application’s memory, CPU, and storage requirements, as described in "How to plan your environment according to application requirements".

Example scenario
If you want to scope your cluster for 2200 pods per cluster, you would need at least five nodes, assuming that there are 500 maximum pods per node. The following formula shows the calculation:

``` text
2200 / 500 = 4.4
```

If you increase the number of nodes to 20, then the pod distribution changes to 110 pods per node. The following formula shows the calculation:

``` text
2200 / 20 = 110
```

Where:

``` text
required pods per cluster / total number of nodes = expected pods per node
```

OpenShift Container Platform includes several system pods, such as OVN-Kubernetes, DNS, Operators, and others, which run across every compute node by default. Therefore, the result of the above formula can vary.

# How to plan your environment according to application requirements

To ensure your infrastructure handles workload demands efficiently, plan your environment according to application requirements. By planning in this way, you can determine the necessary compute, storage, and networking resources to maintain performance and stability.

Consider an example application environment:

| Pod type   | Pod quantity | Max memory | CPU cores | Persistent storage |
|------------|--------------|------------|-----------|--------------------|
| apache     | 100          | 500 MB     | 0.5       | 1 GB               |
| node.js    | 200          | 1 GB       | 1         | 1 GB               |
| postgresql | 100          | 1 GB       | 2         | 10 GB              |
| JBoss EAP  | 100          | 1 GB       | 1         | 1 GB               |

Extrapolated requirements: 550 CPU cores, 450GB RAM, and 1.4TB storage.

Instance size for nodes can be modulated up or down, depending on your preference. Nodes are often resource overcommitted. In this deployment scenario, you can choose to run additional smaller nodes or fewer larger nodes to provide the same amount of resources. Factors such as operational agility and cost-per-instance should be considered.

| Node type        | Quantity | CPUs | RAM (GB) |
|------------------|----------|------|----------|
| Nodes (option 1) | 100      | 4    | 16       |
| Nodes (option 2) | 50       | 8    | 32       |
| Nodes (option 3) | 25       | 16   | 64       |

Some applications lend themselves well to overcommitted environments, and some do not. Most Java applications and applications that use huge pages are examples of applications that would not allow for overcommitment. That memory can not be used for other applications. In the example above, the environment would be roughly 30 percent overcommitted, a common ratio.

The application pods can access a service either by using environment variables or DNS. If using environment variables, for each active service the variables are injected by the kubelet when a pod is run on a node. A cluster-aware DNS server watches the Kubernetes API for new services and creates a set of DNS records for each one.

If DNS is enabled throughout your cluster, then all pods should automatically be able to resolve services by their DNS name. Service discovery using DNS can be used in case you must go beyond 5000 services. When using environment variables for service discovery, the argument list exceeds the allowed length after 5000 services in a namespace, then the pods and deployments will start failing. Disable the service links in the deployment’s service specification file to overcome this:

``` yaml
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: deployment-config-template
  creationTimestamp:
  annotations:
    description: This template will create a deploymentConfig with 1 replica, 4 env vars and a service.
    tags: ''
objects:
- apiVersion: apps.openshift.io/v1
  kind: DeploymentConfig
  metadata:
    name: deploymentconfig${IDENTIFIER}
  spec:
    template:
      metadata:
        labels:
          name: replicationcontroller${IDENTIFIER}
      spec:
        enableServiceLinks: false
        containers:
        - name: pause${IDENTIFIER}
          image: "${IMAGE}"
          ports:
          - containerPort: 8080
            protocol: TCP
          env:
          - name: ENVVAR1_${IDENTIFIER}
            value: "${ENV_VALUE}"
          - name: ENVVAR2_${IDENTIFIER}
            value: "${ENV_VALUE}"
          - name: ENVVAR3_${IDENTIFIER}
            value: "${ENV_VALUE}"
          - name: ENVVAR4_${IDENTIFIER}
            value: "${ENV_VALUE}"
          resources: {}
          imagePullPolicy: IfNotPresent
          capabilities: {}
          securityContext:
            capabilities: {}
            privileged: false
        restartPolicy: Always
        serviceAccount: ''
    replicas: 1
    selector:
      name: replicationcontroller${IDENTIFIER}
    triggers:
    - type: ConfigChange
    strategy:
      type: Rolling
- apiVersion: v1
  kind: Service
  metadata:
    name: service${IDENTIFIER}
  spec:
    selector:
      name: replicationcontroller${IDENTIFIER}
    ports:
    - name: serviceport${IDENTIFIER}
      protocol: TCP
      port: 80
      targetPort: 8080
    clusterIP: ''
    type: ClusterIP
    sessionAffinity: None
  status:
    loadBalancer: {}
parameters:
- name: IDENTIFIER
  description: Number to append to the name of resources
  value: '1'
  required: true
- name: IMAGE
  description: Image to use for deploymentConfig
  value: gcr.io/google-containers/pause-amd64:3.0
  required: false
- name: ENV_VALUE
  description: Value to use for environment variables
  generate: expression
  from: "[A-Za-z0-9]{255}"
  required: false
labels:
  template: deployment-config-template
```

The number of application pods that can run in a namespace is dependent on the number of services and the length of the service name when the environment variables are used for service discovery. `ARG_MAX` on the system defines the maximum argument length for a new process and the variable is set to 2097152 bytes (2 MiB) by default. The Kubelet injects environment variables in to each pod scheduled to run in the namespace including the following variables:

- `<SERVICE_NAME>_SERVICE_HOST=<IP>`

- `<SERVICE_NAME>_SERVICE_PORT=<PORT>`

- `<SERVICE_NAME>_PORT=tcp://<IP>:<PORT>`

- `<SERVICE_NAME>_PORT_<PORT>_TCP=tcp://<IP>:<PORT>`

- `<SERVICE_NAME>_PORT_<PORT>_TCP_PROTO=tcp`

- `<SERVICE_NAME>_PORT_<PORT>_TCP_PORT=<PORT>`

- `<SERVICE_NAME>_PORT_<PORT>_TCP_ADDR=<ADDR>`

The pods in the namespace will start to fail if the argument length exceeds the allowed value and the number of characters in a service name impacts it. For example, in a namespace with 5000 services, the limit on the service name is 33 characters, which enables you to run 5000 pods in the namespace.
