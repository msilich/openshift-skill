<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After provisioning the DPUs and verifying system readiness, validate end-to-end traffic flow and configure DPU telemetry observability.

# Deploy traffic test pods and services

You can deploy traffic test pods and services across the management cluster to validate end-to-end connectivity through the DPU data plane. The test workloads include a server pod on a control plane node and worker pods on DPU-enabled nodes, with both standard and host-network configurations.

> [!NOTE]
> These test workloads use the `nicolaka/netshoot` container image, a community networking-troubleshooting image that is not officially supported by Red Hat or NVIDIA. Use it only for connectivity validation and testing, not in production workloads.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the DPF Operator and provisioned the DPU hosted cluster.

- At least one DPU-enabled worker node is available.

- You have access to the management cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `traffic-pods.yaml` with the following content:

    ``` yaml
    # 1. Namespace
    ---
    apiVersion: v1
    kind: Namespace
    metadata:
      name: workload

    # 2. SCC RoleBinding (grants 'default' ServiceAccount in 'workload' NS access to 'privileged' SCC)
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: RoleBinding
    metadata:
      name: privileged-scc-default-sa
      namespace: workload
    subjects:
    - kind: ServiceAccount
      name: default
      namespace: workload
    roleRef:
      kind: ClusterRole
      name: system:openshift:scc:privileged
      apiGroup: rbac.authorization.k8s.io

    # 3. Deployments and Services
    # Deployment: traffic-test-master
    ---
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: traffic-test-master
      namespace: workload
      labels:
        app: traffic-test-master
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: traffic-test-master
      template:
        metadata:
          labels:
            app: traffic-test-master
        spec:
          topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule
            labelSelector:
              matchLabels:
                app: traffic-test-master
          nodeSelector:
            node-role.kubernetes.io/control-plane: ""
          tolerations:
          - key: node-role.kubernetes.io/master
            operator: Exists
            effect: NoSchedule
          - key: node-role.kubernetes.io/control-plane
            operator: Exists
            effect: NoSchedule
          containers:
          - name: nginx
            securityContext:
              privileged: true
              capabilities:
                add:
                - NET_ADMIN
            image: nicolaka/netshoot
            command: ["nc", "-kl", "5000"]
            ports:
            - containerPort: 5000
              name: tcp-server
            resources:
              requests:
                cpu: 1
                memory: 1Gi
              limits:
                cpu: 1
                memory: 1Gi
    ---
    # Service: traffic-test-master
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-master
      namespace: workload
      labels:
        app: traffic-test-master
    spec:
      selector:
        app: traffic-test-master
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ---
    # Service: traffic-test-master-nodeport
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-master-nodeport
      namespace: workload
      labels:
        app: traffic-test-master
    spec:
      type: NodePort
      selector:
        app: traffic-test-master
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ---
    # Deployment: traffic-test-worker
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: traffic-test-worker
      namespace: workload
      labels:
        app: traffic-test-worker
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: traffic-test-worker
      template:
        metadata:
          labels:
            app: traffic-test-worker
        spec:
          topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule
            labelSelector:
              matchLabels:
                app: traffic-test-worker
          nodeSelector:
            feature.node.kubernetes.io/dpu-enabled: ""
          containers:
          - name: nginx
            securityContext:
              privileged: true
              capabilities:
                add:
                - NET_ADMIN
            image: nicolaka/netshoot
            command: ["nc", "-kl", "5000"]
            ports:
            - containerPort: 5000
              name: tcp-server
            resources:
              requests:
                cpu: 16
                memory: 6Gi
              limits:
                cpu: 16
                memory: 6Gi
    ---
    # Service: traffic-test-worker
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-worker
      namespace: workload
      labels:
        app: traffic-test-worker
    spec:
      selector:
        app: traffic-test-worker
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ---
    # Service: traffic-test-worker-nodeport
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-worker-nodeport
      namespace: workload
      labels:
        app: traffic-test-worker
    spec:
      type: NodePort
      selector:
        app: traffic-test-worker
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ---
    # Deployment: traffic-test-worker-hostnetwork
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: traffic-test-worker-hostnetwork
      namespace: workload
      labels:
        app: traffic-test-worker-hostnetwork
    spec:
      replicas: 1
      selector:
        matchLabels:
          app: traffic-test-worker-hostnetwork
      template:
        metadata:
          labels:
            app: traffic-test-worker-hostnetwork
        spec:
          topologySpreadConstraints:
          - maxSkew: 1
            topologyKey: kubernetes.io/hostname
            whenUnsatisfiable: DoNotSchedule
            labelSelector:
              matchLabels:
                app: traffic-test-worker-hostnetwork
          nodeSelector:
            feature.node.kubernetes.io/dpu-enabled: ""
          hostNetwork: true
          containers:
          - name: nginx
            securityContext:
              privileged: true
              capabilities:
                add:
                - NET_ADMIN
            image: nicolaka/netshoot
            command: ["nc", "-kl", "5000"]
            ports:
            - containerPort: 5000
              name: tcp-server
            resources:
              requests:
                cpu: 1
                memory: 1Gi
              limits:
                cpu: 1
                memory: 1Gi
    ---
    # Service: traffic-test-worker-hostnetwork
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-worker-hostnetwork
      namespace: workload
      labels:
        app: traffic-test-worker-hostnetwork
    spec:
      selector:
        app: traffic-test-worker-hostnetwork
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ---
    # Service: traffic-test-worker-hostnetwork-nodeport
    apiVersion: v1
    kind: Service
    metadata:
      name: traffic-test-worker-hostnetwork-nodeport
      namespace: workload
      labels:
        app: traffic-test-worker-hostnetwork
    spec:
      type: NodePort
      selector:
        app: traffic-test-worker-hostnetwork
      ports:
      - protocol: TCP
        port: 5000
        targetPort: 5000
    ```

    The manifest creates the following resources:

    - A `workload` namespace for the test pods.

    - A `RoleBinding` resource that grants the `default` service account in the `workload` namespace access to the `privileged` security context constraint.

    - A `traffic-test-master` deployment and `ClusterIP` and `NodePort` services on a control plane node.

    - A `traffic-test-worker` deployment and `ClusterIP` and `NodePort` services on DPU-enabled worker nodes.

    - A `traffic-test-worker-hostnetwork` deployment that uses host networking on DPU-enabled worker nodes, with `ClusterIP` and `NodePort` services.

      > [!NOTE]
      > The worker deployments set `replicas: 1` for a single DPU worker node. Set the replica count of the `traffic-test-worker` and `traffic-test-worker-hostnetwork` deployments to the number of DPU-enabled worker nodes so that the `topologySpreadConstraints` place one pod on each node.

2.  Apply the manifest:

    ``` terminal
    $ oc apply -f traffic-pods.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the test pods are running:

    ``` terminal
    $ oc get pods -n workload -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                               READY   STATUS    RESTARTS   AGE     IP             NODE               NOMINATED NODE   READINESS GATES
    traffic-test-master-7448bb5cc-mdftd                1/1     Running   0          2m10s   10.129.0.145   master-2           <none>           <none>
    traffic-test-worker-776486fb68-krz54               1/1     Running   0          2m10s   10.128.2.9     host-worker1       <none>           <none>
    traffic-test-worker-776486fb68-lz8vf               1/1     Running   0          2m10s   10.131.0.9     host-worker2       <none>           <none>
    traffic-test-worker-hostnetwork-596d569d99-cjpns   1/1     Running   0          2m10s   10.0.110.11    host-worker1       <none>           <none>
    traffic-test-worker-hostnetwork-596d569d99-x6m7r   1/1     Running   0          2m10s   10.0.110.12    host-worker2       <none>           <none>
    ```

    </div>

    Confirm that the `traffic-test-master` pod is on a control plane node and that the `traffic-test-worker` pods are distributed across different DPU-enabled worker nodes.

2.  Verify that the services are created:

    ``` terminal
    $ oc get svc -n workload
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                       TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)          AGE
    traffic-test-master                        ClusterIP   172.30.102.123   <none>        5000/TCP         13m
    traffic-test-master-nodeport               NodePort    172.30.98.22     <none>        5000:31368/TCP   13m
    traffic-test-worker                        ClusterIP   172.30.187.147   <none>        5000/TCP         13m
    traffic-test-worker-hostnetwork            ClusterIP   172.30.122.242   <none>        5000/TCP         13m
    traffic-test-worker-hostnetwork-nodeport   NodePort    172.30.122.214   <none>        5000:30209/TCP   13m
    traffic-test-worker-nodeport               NodePort    172.30.108.72    <none>        5000:32570/TCP   13m
    ```

    </div>

</div>

# Run traffic validation tests

You can run connectivity tests between the traffic test pods and services to verify that the DPU services and service chains are configured correctly. A successful test confirms that end-to-end traffic flows through the DPU data plane as expected.

<div>

<div class="title">

Prerequisites

</div>

- The traffic test pods and services are deployed in the `workload` namespace and all pods are in a `Running` state.

- You have access to the management cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Run a ping connectivity test between pods on different worker nodes.

    In the following example, replace `<worker_pod_name>` with the name of a `traffic-test-worker` pod and replace `<target_pod_ip>` with the IP address of a `traffic-test-worker` pod on a different worker node:

    ``` terminal
    $ oc -n workload exec -it <worker_pod_name> -- ping -c 4 <target_pod_ip>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    PING 10.131.0.9 (10.131.0.9) 56(84) bytes of data.
    64 bytes from 10.131.0.9: icmp_seq=1 ttl=62 time=1.61 ms
    64 bytes from 10.131.0.9: icmp_seq=2 ttl=62 time=0.876 ms
    64 bytes from 10.131.0.9: icmp_seq=3 ttl=62 time=0.510 ms
    64 bytes from 10.131.0.9: icmp_seq=4 ttl=62 time=0.421 ms

    --- 10.131.0.9 ping statistics ---
    4 packets transmitted, 4 received, 0% packet loss, time 3028ms
    rtt min/avg/max/mdev = 0.421/0.853/1.606/0.466 ms
    ```

    </div>

    Verify that all 4 packets are received with 0% packet loss.

2.  Run a service connectivity test from a worker pod to a service on a control plane node.

    In the following example, replace `<worker_pod_name>` with the name of a `traffic-test-worker` pod and replace `<service_cluster_ip>` with the cluster IP address of the `traffic-test-master` service:

    ``` terminal
    $ oc -n workload exec -it <worker_pod_name> -- nc -vz <service_cluster_ip> 5000
    ```

    A `succeeded` message confirms that the service is reachable through the DPU-accelerated network.

3.  Run a service connectivity test from a worker pod to another worker pod.

    In the following example, replace `<worker_pod_name>` with the name of a `traffic-test-worker` pod and replace `<service_cluster_ip>` with the cluster IP address of the `traffic-test-worker` service:

    ``` terminal
    $ oc -n workload exec -it <worker_pod_name> -- nc -vz <service_cluster_ip> 5000
    ```

    A `succeeded` message confirms end-to-end connectivity through the DPU-accelerated service chain between worker pods.

4.  Optional: Run an external service connectivity test.

    In the following example, replace `<worker_pod_name>` with the name of a `traffic-test-worker` pod, replace `<node_ip>` with the IP address of a cluster node, and replace `<nodeport>` with the NodePort for one of the services:

    ``` terminal
    $ oc -n workload exec -it <worker_pod_name> -- nc -vz <node_ip> <nodeport>
    ```

    A `succeeded` message confirms that NodePort services are reachable through the DPU networking stack.

</div>

# DPU telemetry observability with DOCA Telemetry Service

The DOCA Telemetry Service (DTS) exposes DPU hardware telemetry, such as PCIe link speed, uplink throughput, packets, errors, and NIC channel activity, as Prometheus metrics. You can view these metrics by using the OpenShift Container Platform web console or a Grafana dashboard.

> [!NOTE]
> In a standard DPF installation, the DTS deployment objects are applied automatically during the postinstallation step. Apply them manually only when you are adding DTS to an existing cluster.

> [!NOTE]
> Neither the DPF Operator nor the DTS `DPUService` installs Grafana on OpenShift Container Platform. Red Hat does not offer a certified Grafana Operator. The community Grafana Operator from OperatorHub is the standard way to run Grafana on OpenShift Container Platform.

DTS runs on every DPU in the hosted cluster and collects counters from sysfs and ethtool providers. OpenShift Container Platform includes a built-in Prometheus instance, so you do not need to deploy a separate monitoring stack to scrape DTS metrics.

## How DPF exposes DTS metrics to the management cluster

DTS runs on the DPU hosted cluster, but Prometheus runs on the management cluster. DPF bridges this gap with a built-in port-mirroring mechanism.

When a `DPUService` resource declares a port in its `configPorts` field, DPF performs the following actions:

- Publishes the service port as a `NodePort` on the DPU hosted cluster.

- Creates a mirror `Service` on the management cluster, labeled with `dpu.nvidia.com/exposed-port-for-dpucluster`.

The management-cluster Prometheus then scrapes the mirror service. This mechanism requires no additional configuration beyond the standard DTS deployment objects.

## DTS deployment objects

DTS is deployed through three standard DPF resources:

`DPUServiceTemplate`
Defines the Helm chart for the DOCA Telemetry Service, the DTS container image, and the metrics port. The `configMapData.prometheus.port` field is set to `9189`.

`DPUServiceConfiguration`
Declares the service port `httpserverport: 9189` under `configPorts`. This declaration triggers the management-cluster port-mirroring mechanism described previously.

`DPUDeployment`
References the template and configuration so that DTS is rolled out to the DPUs as a `DaemonSet` on the DPU hosted cluster. DTS defaults to the `sysfs` and `ethtool` providers.

# Enable user workload monitoring for DTS

OpenShift Container Platform includes Prometheus, but by default it only monitors OpenShift Container Platform platform components. You must enable user workload monitoring so that Prometheus can scrape user namespaces where DPF and DTS run, such as `dpf-operator-system`.

<div>

<div class="title">

Prerequisites

</div>

- A DPF cluster is deployed with at least one provisioned DPU.

- You have access to the management cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `cluster-monitoring-config.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: cluster-monitoring-config
      namespace: openshift-monitoring
    data:
      config.yaml: |
        enableUserWorkload: true
    ```

    > [!NOTE]
    > If the `cluster-monitoring-config` `ConfigMap` already exists with other settings, edit it instead of replacing it, and add only the `enableUserWorkload: true` line to the existing `config.yaml` data:
    >
    > ``` terminal
    > $ oc -n openshift-monitoring edit configmap cluster-monitoring-config
    > ```

2.  Apply the `ConfigMap`:

    ``` terminal
    $ oc apply -f cluster-monitoring-config.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the user workload monitoring pods are running in the `openshift-user-workload-monitoring` namespace:

  ``` terminal
  $ oc -n openshift-user-workload-monitoring get pods
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                                   READY   STATUS    RESTARTS   AGE
  prometheus-operator-...                1/1     Running   0          ...
  prometheus-user-workload-0             ...     Running   0          ...
  thanos-ruler-user-workload-0           ...     Running   0          ...
  ```

  </div>

  Confirm that pods named `prometheus-user-workload`, `thanos-ruler-user-workload`, and `prometheus-operator` are all in a `Running` state.

</div>

# Configure the DTS ServiceMonitor

Create a `ServiceMonitor` resource to instruct the user workload monitoring Prometheus instance to scrape the DOCA Telemetry Service (DTS) metrics endpoint. The `ServiceMonitor` selects the mirrored DTS service in the `dpf-operator-system` namespace and scrapes its `/metrics` path on the `httpserverport` every 30 seconds.

<div>

<div class="title">

Prerequisites

</div>

- User workload monitoring is enabled in OpenShift Container Platform.

- The DTS `DPUServiceConfiguration` and `DPUDeployment` resources are applied.

  For details, see "DPU telemetry observability with DTS".

- You have access to the management cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dts-servicemonitor.yaml` with the following content:

    ``` yaml
    apiVersion: monitoring.coreos.com/v1
    kind: ServiceMonitor
    metadata:
      name: doca-telemetry-service-monitor
      namespace: dpf-operator-system
    spec:
      selector:
        matchExpressions:
          - key: dpu.nvidia.com/dpuservice-name
            operator: Exists
      endpoints:
        - port: httpserverport
          interval: 30s
          path: /metrics
          relabelings:
            - sourceLabels:
                - __meta_kubernetes_service_label_dpu_nvidia_com_dpuservice_name
              regex: doca-telemetry-service.*
              action: keep
      namespaceSelector:
        matchNames:
          - dpf-operator-system
    ```

2.  Apply the `ServiceMonitor`:

    ``` terminal
    $ oc apply -f dts-servicemonitor.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the `ServiceMonitor` is created in the `dpf-operator-system` namespace:

  ``` terminal
  $ oc -n dpf-operator-system get servicemonitor doca-telemetry-service-monitor
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                               AGE
  doca-telemetry-service-monitor     ...
  ```

  </div>

</div>

# Install the DTS console dashboard

You can install a DTS dashboard that integrates directly into the OpenShift Container Platform web console. This dashboard provides visibility of DPU telemetry metrics without requiring Grafana or additional tools.

<div>

<div class="title">

Prerequisites

</div>

- User workload monitoring is enabled in OpenShift Container Platform.

- The DTS `ServiceMonitor` is configured and collecting metrics.

- You have access to the management cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `dts-console-dashboard.yaml` with the following content to define a console dashboard `ConfigMap` in the `openshift-config-managed` namespace:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: dpf-dts-console-dashboard
      namespace: openshift-config-managed
      labels:
        console.openshift.io/dashboard: "true"
    data:
      doca-dpu-telemetry-dts.json: |
        {
          "title": "DOCA DPU Telemetry (DTS)",
          "uid": "doca-dpu-telemetry-dts-console",
          "editable": false,
          "schemaVersion": 16,
          "tags": ["dpf", "dpu", "dts", "telemetry"],
          "timezone": "browser",
          "time": {"from": "now-1h", "to": "now"},
          "refresh": "30s",
          "templating": {"list": []},
          "rows": [
            {
              "title": "PCIe / Link",
              "showTitle": true,
              "height": "250px",
              "panels": [
                {
                  "type": "graph", "title": "PCIe Link Speed (GT/s)", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true},
                  "yaxes": [{"format": "none", "show": true}, {"format": "none", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "current_link_speed", "legendFormat": "{{source}} {{hca}}"}
                  ]
                },
                {
                  "type": "graph", "title": "PCIe Link Width (lanes)", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true},
                  "yaxes": [{"format": "none", "show": true}, {"format": "none", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "current_link_width", "legendFormat": "{{source}} {{hca}}"}
                  ]
                }
              ]
            },
            {
              "title": "Uplink Throughput (p0/p1)",
              "showTitle": true,
              "height": "250px",
              "panels": [
                {
                  "type": "graph", "title": "Uplink RX (bits/s)", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "values": true, "avg": true, "max": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "bps", "show": true}, {"format": "bps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_bytes\"}[5m])) * 8",
                     "legendFormat": "{{source}}"}
                  ]
                },
                {
                  "type": "graph", "title": "Uplink TX (bits/s)", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "values": true, "avg": true, "max": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "bps", "show": true}, {"format": "bps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_tx_bytes\"}[5m])) * 8",
                     "legendFormat": "{{source}}"}
                  ]
                }
              ]
            },
            {
              "title": "Uplink Packets & Errors",
              "showTitle": true,
              "height": "250px",
              "panels": [
                {
                  "type": "graph", "title": "Uplink packets/s (rx + tx)", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "pps", "show": true}, {"format": "pps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_packets\"}[5m]))",
                     "legendFormat": "{{source}} rx"},
                    {"refId": "B", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_tx_packets\"}[5m]))",
                     "legendFormat": "{{source}} tx"}
                  ]
                },
                {
                  "type": "graph", "title": "Uplink errors & drops/s", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "cps", "show": true}, {"format": "cps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_errors\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_tx_errors\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_rx_dropped\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_tx_dropped\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_rx_crc_errors\"}[5m]))",
                     "legendFormat": "{{source}}"}
                  ]
                }
              ]
            },
            {
              "title": "NIC Channel Activity",
              "showTitle": true,
              "height": "250px",
              "panels": [
                {
                  "type": "graph", "title": "NIC channel poll/s", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "cps", "show": true}, {"format": "cps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate(ch_poll[5m]))", "legendFormat": "{{source}}"}
                  ]
                },
                {
                  "type": "graph", "title": "NIC channel events/s", "span": 6,
                  "datasource": "prometheus", "nullPointMode": "null",
                  "legend": {"show": true, "alignAsTable": true, "rightSide": true},
                  "yaxes": [{"format": "cps", "show": true}, {"format": "cps", "show": false}],
                  "targets": [
                    {"refId": "A", "format": "time_series", "intervalFactor": 2,
                     "expr": "sum by(source)(rate(ch_events[5m]))", "legendFormat": "{{source}}"}
                  ]
                }
              ]
            }
          ]
        }
    ```

2.  Apply the console dashboard:

    ``` terminal
    $ oc apply -f dts-console-dashboard.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the dashboard `ConfigMap` is created:

    ``` terminal
    $ oc -n openshift-config-managed get configmap dpf-dts-console-dashboard
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                        DATA   AGE
    dpf-dts-console-dashboard   1      ...
    ```

    </div>

2.  Access the dashboard in the OpenShift Container Platform web console:

    1.  Navigate to **Observe** → **Dashboards**.

    2.  In the **Dashboard** dropdown menu, select **DOCA DPU Telemetry (DTS)**.

        The dashboard displays PCIe link speed and width, uplink throughput, packets per second, errors and drops per second, and NIC channel activity, with each DPU as its own line.

</div>

> [!NOTE]
> The DTS console dashboard renders against the platform Thanos or user workload monitoring Prometheus instance. No Grafana dependency is required for basic DPU telemetry viewing.

# Install Grafana for DTS metrics visualization

You can install the Grafana Operator and a Grafana instance to provide enhanced visualization for DPU telemetry metrics, including per-DPU filtering and customizable dashboards. You can also deploy a dashboard ConfigMap that adds DTS metrics to the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You have enabled user workload monitoring in OpenShift Container Platform.

- You have configured the DTS `ServiceMonitor` and it is collecting metrics.

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- You have installed the `helm` CLI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Install the Grafana Operator by using Helm:

    ``` terminal
    $ helm upgrade -i grafana-operator oci://ghcr.io/grafana/helm-charts/grafana-operator \
        --version 5.24.0 \
        --namespace grafana-operator \
        --create-namespace
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Pulled: ghcr.io/grafana/helm-charts/grafana-operator:5.24.0
    Digest: sha256:4f69cdaecfed2cc61d4e5f4a8e7142795e9b00997e4bcbd37a8c154a225a2f1f
    Release "grafana-operator" has been upgraded. Happy Helming!
    NAME: grafana-operator
    LAST DEPLOYED: Tue Aug  4 08:51:36 2026
    NAMESPACE: grafana-operator
    STATUS: deployed
    REVISION: 2
    TEST SUITE: None
    ```

    </div>

2.  Grant OpenShift Route permissions to the Grafana Operator:

    The community Grafana Operator requires additional RBAC permissions to manage OpenShift Container Platform routes. Create a file named `grafana-operator-route-rbac.yaml` with the following content:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: grafana-operator-route-manager
    rules:
    - apiGroups:
      - route.openshift.io
      resources:
      - routes
      - routes/custom-host
      verbs:
      - create
      - delete
      - get
      - list
      - patch
      - update
      - watch
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: grafana-operator-route-manager
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: grafana-operator-route-manager
    subjects:
    - kind: ServiceAccount
      name: grafana-operator
      namespace: grafana-operator
    ```

    Apply the file:

    ``` terminal
    $ oc apply -f grafana-operator-route-rbac.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    clusterrole.rbac.authorization.k8s.io/grafana-operator-route-manager created
    clusterrolebinding.rbac.authorization.k8s.io/grafana-operator-route-manager created
    ```

    </div>

3.  Create Grafana RBAC for Prometheus access:

    Create a `ServiceAccount` with a long-lived token and bind it to the `cluster-monitoring-view` `ClusterRole` so Grafana can query the platform Prometheus:

    ``` yaml
    apiVersion: v1
    kind: ServiceAccount
    metadata:
      name: grafana-prometheus-reader
      namespace: dpf-operator-system
    ---
    apiVersion: v1
    kind: Secret
    metadata:
      name: grafana-prometheus-reader-token
      namespace: dpf-operator-system
      annotations:
        kubernetes.io/service-account.name: grafana-prometheus-reader
    type: kubernetes.io/service-account-token
    ---
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRoleBinding
    metadata:
      name: grafana-prometheus-reader-cluster-monitoring
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: cluster-monitoring-view
    subjects:
      - kind: ServiceAccount
        name: grafana-prometheus-reader
        namespace: dpf-operator-system
    ```

    Apply the YAML:

    ``` terminal
    $ oc apply -f grafana-rbac.yaml
    ```

4.  Deploy the Grafana instance with control-plane scheduling:

    ``` yaml
    apiVersion: grafana.integreatly.org/v1beta1
    kind: Grafana
    metadata:
      name: dpf-grafana
      namespace: dpf-operator-system
      labels:
        dashboards: "dpf-grafana"
    spec:
      route:
        spec:
          port:
            targetPort: grafana
          tls:
            termination: edge
      config:
        log:
          mode: "console"
          level: "info"
        auth.anonymous:
          enabled: "true"
          org_role: "Viewer"
        security:
          admin_user: "admin"
          admin_password: "admin"
      deployment:
        spec:
          template:
            spec:
              nodeSelector:
                node-role.kubernetes.io/control-plane: ""
              tolerations:
              - key: node-role.kubernetes.io/master
                operator: Exists
                effect: NoSchedule
              - key: node-role.kubernetes.io/control-plane
                operator: Exists
                effect: NoSchedule
    ```

    Apply the YAML:

    ``` terminal
    $ oc apply -f grafana-cr.yaml
    ```

    > [!WARNING]
    > The default credentials (`admin`/`admin`) are suitable for lab environments only. Change the `admin_password` for non-lab deployments.

5.  Configure the Prometheus datasource:

    ``` yaml
    apiVersion: grafana.integreatly.org/v1beta1
    kind: GrafanaDatasource
    metadata:
      name: prometheus
      namespace: dpf-operator-system
    spec:
      instanceSelector:
        matchLabels:
          dashboards: "dpf-grafana"
      valuesFrom:
        - targetPath: "secureJsonData.httpHeaderValue1"
          valueFrom:
            secretKeyRef:
              name: grafana-prometheus-reader-token
              key: token
      datasource:
        name: prometheus
        type: prometheus
        uid: prometheus
        access: proxy
        url: https://thanos-querier.openshift-monitoring.svc.cluster.local:9091
        isDefault: true
        jsonData:
          tlsSkipVerify: true
          httpHeaderName1: "Authorization"
          timeInterval: "30s"
        secureJsonData:
          httpHeaderValue1: "Bearer ${token}"
    ```

    Apply the YAML:

    ``` terminal
    $ oc apply -f grafana-datasource.yaml
    ```

6.  Create a file named `dts-grafana-dashboard.yaml` with the following content:

    ``` yaml
    apiVersion: v1
    kind: ConfigMap
    metadata:
      name: dpf-dts-grafana-dashboard
      namespace: dpf-operator-system
      labels:
        app.kubernetes.io/part-of: dpf
    data:
      doca-dpu-telemetry-dts.json: |
        {
          "title": "DOCA DPU Telemetry (DTS)",
          "uid": "doca-dpu-telemetry-dts",
          "tags": ["dpf", "dpu", "dts", "telemetry"],
          "timezone": "browser",
          "schemaVersion": 39,
          "editable": true,
          "time": {"from": "now-1h", "to": "now"},
          "refresh": "30s",
          "templating": {
            "list": [
              {
                "name": "source",
                "label": "DPU (source)",
                "type": "query",
                "datasource": {"type": "prometheus", "uid": "prometheus"},
                "query": "label_values(current_link_speed, source)",
                "refresh": 2,
                "includeAll": true,
                "multi": true,
                "current": {"text": "All", "value": "$__all"},
                "sort": 1
              }
            ]
          },
          "panels": [
            {
              "type": "stat",
              "title": "PCIe Link Speed (GT/s)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 4, "w": 6, "x": 0, "y": 0},
              "fieldConfig": {"defaults": {"unit": "none"}, "overrides": []},
              "options": {"reduceOptions": {"calcs": ["lastNotNull"]}, "colorMode": "value", "graphMode": "none"},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "current_link_speed{source=~\"$source\"}", "legendFormat": "{{source}} {{hca}}"}
              ]
            },
            {
              "type": "stat",
              "title": "PCIe Link Width (lanes)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 4, "w": 6, "x": 6, "y": 0},
              "fieldConfig": {"defaults": {"unit": "none"}, "overrides": []},
              "options": {"reduceOptions": {"calcs": ["lastNotNull"]}, "colorMode": "value", "graphMode": "none"},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "current_link_width{source=~\"$source\"}", "legendFormat": "{{source}} {{hca}}"}
              ]
            },
            {
              "type": "stat",
              "title": "Max PCIe Link Speed (GT/s)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 4, "w": 6, "x": 12, "y": 0},
              "fieldConfig": {"defaults": {"unit": "none"}, "overrides": []},
              "options": {"reduceOptions": {"calcs": ["lastNotNull"]}, "colorMode": "value", "graphMode": "none"},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "max_link_speed{source=~\"$source\"}", "legendFormat": "{{source}} {{hca}}"}
              ]
            },
            {
              "type": "stat",
              "title": "Max PCIe Link Width (lanes)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 4, "w": 6, "x": 18, "y": 0},
              "fieldConfig": {"defaults": {"unit": "none"}, "overrides": []},
              "options": {"reduceOptions": {"calcs": ["lastNotNull"]}, "colorMode": "value", "graphMode": "none"},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "max_link_width{source=~\"$source\"}", "legendFormat": "{{source}} {{hca}}"}
              ]
            },
            {
              "type": "timeseries",
              "title": "Uplink RX throughput (p0/p1)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 0, "y": 4},
              "fieldConfig": {"defaults": {"unit": "bps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_bytes\", source=~\"$source\"}[5m])) * 8",
                 "legendFormat": "{{source}}"}
              ]
            },
            {
              "type": "timeseries",
              "title": "Uplink TX throughput (p0/p1)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 12, "y": 4},
              "fieldConfig": {"defaults": {"unit": "bps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_tx_bytes\", source=~\"$source\"}[5m])) * 8",
                 "legendFormat": "{{source}}"}
              ]
            },
            {
              "type": "timeseries",
              "title": "Uplink packets/s (p0/p1 rx+tx)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 0, "y": 12},
              "fieldConfig": {"defaults": {"unit": "pps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_packets\", source=~\"$source\"}[5m]))",
                 "legendFormat": "{{source}} rx"},
                {"refId": "B", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_tx_packets\", source=~\"$source\"}[5m]))",
                 "legendFormat": "{{source}} tx"}
              ]
            },
            {
              "type": "timeseries",
              "title": "Uplink errors & drops/s (p0/p1)",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 12, "y": 12},
              "fieldConfig": {"defaults": {"unit": "cps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "sum by(source)(rate({__name__=~\"p[01]_eth_rx_errors\", source=~\"$source\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_tx_errors\", source=~\"$source\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_rx_dropped\", source=~\"$source\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_tx_dropped\", source=~\"$source\"}[5m])) + sum by(source)(rate({__name__=~\"p[01]_eth_rx_crc_errors\", source=~\"$source\"}[5m]))",
                 "legendFormat": "{{source}}"}
              ]
            },
            {
              "type": "timeseries",
              "title": "NIC channel poll/s",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 0, "y": 20},
              "fieldConfig": {"defaults": {"unit": "cps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "rate(ch_poll{source=~\"$source\"}[5m])",
                 "legendFormat": "{{source}} {{device_name}}"}
              ]
            },
            {
              "type": "timeseries",
              "title": "NIC channel events/s",
              "datasource": {"type": "prometheus", "uid": "prometheus"},
              "gridPos": {"h": 8, "w": 12, "x": 12, "y": 20},
              "fieldConfig": {"defaults": {"unit": "cps", "custom": {"drawStyle": "line", "fillOpacity": 10}}, "overrides": []},
              "options": {"legend": {"displayMode": "table", "placement": "bottom", "calcs": ["mean", "max"]}, "tooltip": {"mode": "multi"}},
              "targets": [
                {"refId": "A", "datasource": {"type": "prometheus", "uid": "prometheus"},
                 "expr": "rate(ch_events{source=~\"$source\"}[5m])",
                 "legendFormat": "{{source}} {{device_name}}"}
              ]
            }
          ]
        }
    ---
    apiVersion: grafana.integreatly.org/v1beta1
    kind: GrafanaDashboard
    metadata:
      name: doca-dpu-telemetry-dts
      namespace: dpf-operator-system
    spec:
      instanceSelector:
        matchLabels:
          dashboards: "dpf-grafana"
      configMapRef:
        name: dpf-dts-grafana-dashboard
        key: doca-dpu-telemetry-dts.json
    ```

    Apply the YAML:

    ``` terminal
    $ oc apply -f dts-grafana-dashboard.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the Grafana Operator is running:

    ``` terminal
    $ oc get pods -n grafana-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                               READY   STATUS    RESTARTS   AGE
    grafana-operator-66d8c8c7b-xyz12   1/1     Running   0          5m42s
    ```

    </div>

2.  Verify that the Grafana instance is running:

    ``` terminal
    $ oc get grafana -n dpf-operator-system
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          AGE
    dpf-grafana   3m15s
    ```

    </div>

3.  Verify that the Grafana pod is running on a control plane node:

    ``` terminal
    $ oc get pods -n dpf-operator-system -o wide | grep grafana
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                             READY   STATUS    RESTARTS   AGE     IP             NODE            NOMINATED NODE   READINESS GATES
    grafana-deployment-7c8b9d-xyz12  1/1     Running   0          2m38s   10.128.0.45   master-node-1   <none>           <none>
    ```

    </div>

4.  Verify the Grafana route exists:

    ``` terminal
    $ oc get route -n dpf-operator-system
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                HOST/PORT                               PATH   SERVICES      PORT      TERMINATION   WILDCARD
    dpf-grafana-route   dpf-grafana-route-dpf-operator-system.apps.cluster.example.com          dpf-grafana   grafana   edge          None
    ```

    </div>

5.  Access the Grafana web interface:

    Get the Grafana URL:

    ``` terminal
    $ echo "https://$(oc -n dpf-operator-system get route dpf-grafana-route -o jsonpath='{.spec.host}')"
    ```

    Open the returned URL in a web browser. Use anonymous access (read-only) or sign in with the default credentials (`admin`/`admin`) for editing capabilities.

6.  Navigate to the DTS dashboard:

    1.  In Grafana, go to **Dashboards** and open **DOCA DPU Telemetry (DTS)**.

    2.  Use the **DPU (source)** dropdown menu to focus on a specific DPU or select **All**.

    3.  Adjust the time range by using the **time-range** control on the dashboard toolbar. The dashboard refreshes every 30 seconds.

    4.  Optional: In the OpenShift Container Platform web console, go to **Observe** → **Dashboards** and open **DOCA DPU Telemetry (DTS)** to view the console-integrated dashboard.

    5.  Review the following metrics:

        - PCIe status: current and maximum link speed and width

        - Throughput: receive (RX) and transmit (TX) data rates for uplink ports `p0` and `p1`

        - Packet rates: packets-per-second statistics with RX and TX breakdown

        - Error monitoring: combined error, drop, and CRC error rates

</div>

# View DTS metrics and dashboards

After you configure the DTS `ServiceMonitor`, you can view DPU telemetry metrics by using the OpenShift Container Platform web console, `PromQL` queries, or Grafana dashboards.

<div>

<div class="title">

Prerequisites

</div>

- You have configured the DTS `ServiceMonitor`.

- You have access to the management cluster as a user with the `cluster-admin` role.

- You have installed the `oc` CLI.

- Optional: You have installed Grafana for DTS metrics visualization.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that the DTS `DPUService` is ready on the management cluster. The object name carries a generated suffix, so select it by its stable label:

    ``` terminal
    $ oc -n dpf-operator-system get dpuservice \
      -l svc.dpu.nvidia.com/dpudeployment-service=doca-telemetry-service
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           READY   PHASE     AGE
    doca-telemetry-service-89p28   True    Success   ...
    ```

    </div>

    A status of `READY: True` and `PHASE: Success` confirms that DTS is deployed and running.

2.  View metrics in the OpenShift Container Platform web console.

    > [!NOTE]
    > The OpenShift Container Platform web console reads from the cluster Prometheus instance through Thanos and user workload monitoring. Grafana is not required for basic metric viewing.

    To run an ad hoc query, go to **Observe** → **Metrics** in the web console, enter a DTS `PromQL` query, and click **Run queries**.

    Example query to validate DTS metrics:

    ``` text
    current_link_speed{job=~"doca-telemetry-service.*"}
    ```

    You should get one series per DPU. Hover over a line to see its labels. Note the `source` label, which is the DPU node name that identifies each DPU.

    | Query | Description |
    |----|----|
    | `current_link_speed{job=~"doca-telemetry-service.*"}` | Returns the current PCIe link speed for each DPU. Each series includes a `source` label that identifies the DPU node name. |
    | `rate(p0_eth_rx_bytes{job=~"doca-telemetry-service.*"}[5m]) * 8` | Calculates the uplink receive throughput in bits per second over a 5-minute window. |
    | `rate(ch_poll{job=~"doca-telemetry-service.*"}[5m])` | Calculates the NIC channel polling activity rate over a 5-minute window. |

    DTS `PromQL` queries

    To view the console dashboard, go to **Observe** → **Dashboards**, then in the **Dashboard** dropdown menu, select **DOCA DPU Telemetry (DTS)**. The dashboard displays PCIe link speed and width, uplink throughput, packets per second, errors and drops per second, and NIC channel activity, with each DPU as its own line.

3.  Optional: View metrics in Grafana.

    Grafana provides richer dashboards with per-DPU dropdown filters and customizable panels. After you install the Grafana Operator and Grafana instance, retrieve the route URL:

    ``` terminal
    $ echo "https://$(oc -n dpf-operator-system get route dpf-grafana-route -o jsonpath='{.spec.host}')"
    ```

    Open the outputted URL in a browser. Anonymous access provides read-only viewer permissions. To edit dashboards, click **Sign in** and use `admin` / `admin` as the default credentials set in the Grafana custom resource.

    > [!IMPORTANT]
    > Change the default Grafana credentials for non-lab clusters.

    In Grafana, go to **Dashboards** and open **DOCA DPU Telemetry (DTS)**. Use the **DPU (source)** dropdown menu to focus on a specific DPU or select **All**. Adjust the time range by using the **time-range** control on the dashboard toolbar. The dashboard refreshes every 30 seconds.

4.  Optional: Review DPF framework dashboards in Grafana.

    The DPF Operator installs framework dashboards that track DPU lifecycle and control-plane health separately from the DTS hardware telemetry dashboard. These dashboards are loaded into Grafana automatically through `GrafanaDashboard` resources created from `ConfigMaps`.

    | Dashboard | Description |
    |----|----|
    | DOCA Platform DPU Fleet Health | Fleet-wide DPU health, provisioning state, and version distribution. |
    | DOCA Platform DPU Health Detail | Per-DPU status, conditions, and history timelines. |
    | DOCA Platform Framework State | Inventory and readiness of every DPF resource type. |
    | DOCA Platform Framework Performance | Time for DPF resources to reach their conditions, including reconcile and provisioning timings. |
    | Controller Runtime | DPF controller internals: CPU and memory usage, reconcile rates, queues, and errors. |

    DPF framework dashboards

</div>
