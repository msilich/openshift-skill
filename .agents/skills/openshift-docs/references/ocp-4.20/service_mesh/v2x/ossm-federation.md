<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

*Federation* is a deployment model that lets you share services and workloads between separate meshes managed in distinct administrative domains.

# Federation overview

Federation is a set of features that let you connect services between separate meshes, allowing the use of Service Mesh features such as authentication, authorization, and traffic management across multiple, distinct administrative domains.

Implementing a federated mesh lets you run, manage, and observe a single service mesh running across multiple OpenShift clusters. Red Hat OpenShift Service Mesh federation takes an opinionated approach to a multi-cluster implementation of Service Mesh that assumes *minimal* trust between meshes.

Service Mesh federation assumes that each mesh is managed individually and retains its own administrator. The default behavior is that no communication is permitted and no information is shared between meshes. The sharing of information between meshes is on an explicit opt-in basis. Nothing is shared in a federated mesh unless it has been configured for sharing. Support functions such as certificate generation, metrics and trace collection remain local in their respective meshes.

You configure the `ServiceMeshControlPlane` on each service mesh to create ingress and egress gateways specifically for the federation, and to specify the trust domain for the mesh.

Federation also involves the creation of additional federation files. The following resources are used to configure the federation between two or more meshes.

- A **ServiceMeshPeer** resource declares the federation between a pair of service meshes.

- An **ExportedServiceSet** resource declares that one or more services from the mesh are available for use by a peer mesh.

- An **ImportedServiceSet** resource declares which services exported by a peer mesh will be imported into the mesh.

# Federation features

Features of the Red Hat OpenShift Service Mesh federated approach to joining meshes include the following:

- Supports common root certificates for each mesh.

- Supports different root certificates for each mesh.

- Mesh administrators must manually configure certificate chains, service discovery endpoints, trust domains, etc for meshes outside of the Federated mesh.

- Only export/import the services that you want to share between meshes.

  - Defaults to not sharing information about deployed workloads with other meshes in the federation. A service can be **exported** to make it visible to other meshes and allow requests from workloads outside of its own mesh.

  - A service that has been exported can be **imported** to another mesh, enabling workloads on that mesh to send requests to the imported service.

- Encrypts communication between meshes at all times.

- Supports configuring load balancing across workloads deployed locally and workloads that are deployed in another mesh in the federation.

When a mesh is joined to another mesh it can do the following:

- Provide trust details about itself to the federated mesh.

- Discover trust details about the federated mesh.

- Provide information to the federated mesh about its own exported services.

- Discover information about services exported by the federated mesh.

# Federation security

Red Hat OpenShift Service Mesh federation takes an opinionated approach to a multi-cluster implementation of Service Mesh that assumes minimal trust between meshes. Data security is built in as part of the federation features.

- Each mesh is considered to be a unique tenant, with a unique administration.

- You create a unique trust domain for each mesh in the federation.

- Traffic between the federated meshes is automatically encrypted using mutual Transport Layer Security (mTLS).

- The Kiali graph only displays your mesh and services that you have imported. You cannot see the other mesh or services that have not been imported into your mesh.

# Federation limitations

The Red Hat OpenShift Service Mesh federated approach to joining meshes has the following limitations:

- Federation of meshes is not supported on OpenShift Dedicated.

# Federation prerequisites

The Red Hat OpenShift Service Mesh federated approach to joining meshes has the following prerequisites:

- Two or more OpenShift Container Platform 4.6 or above clusters.

- Federation was introduced in Red Hat OpenShift Service Mesh 2.1 or later. You must have the Red Hat OpenShift Service Mesh 2.1 or later Operator installed on each mesh that you want to federate.

- You must have a version 2.1 or later `ServiceMeshControlPlane` deployed on each mesh that you want to federate.

- You must configure the load balancers supporting the services associated with the federation gateways to support raw TLS traffic. Federation traffic consists of HTTPS for discovery and raw encrypted TCP for service traffic.

- Services that you want to expose to another mesh should be deployed before you can export and import them. However, this is not a strict requirement. You can specify service names that do not yet exist for export/import. When you deploy the services named in the `ExportedServiceSet` and `ImportedServiceSet` they will be automatically made available for export/import.

# Planning your mesh federation

Before you start configuring your mesh federation, you should take some time to plan your implementation.

- How many meshes do you plan to join in a federation? You probably want to start with a limited number of meshes, perhaps two or three.

- What naming convention do you plan to use for each mesh? Having a pre-defined naming convention will help with configuration and troubleshooting. The examples in this documentation use different colors for each mesh. You should decide on a naming convention that will help you determine who owns and manages each mesh, as well as the following federation resources:

  - Cluster names

  - Cluster network names

  - Mesh names and namespaces

  - Federation ingress gateways

  - Federation egress gateways

  - Security trust domains

    > [!NOTE]
    > Each mesh in the federation must have its own unique trust domain.

- Which services from each mesh do you plan to export to the federated mesh? Each service can be exported individually, or you can specify labels or use wildcards.

  - Do you want to use aliases for the service namespaces?

  - Do you want to use aliases for the exported services?

- Which exported services does each mesh plan to import? Each mesh only imports the services that it needs.

  - Do you want to use aliases for the imported services?

# Mesh federation across clusters

To connect one instance of the OpenShift Service Mesh with one running in a different cluster, the procedure is not much different as when connecting two meshes deployed in the same cluster. However, the ingress gateway of one mesh must be reachable from the other mesh. One way of ensuring this is to configure the gateway service as a `LoadBalancer` service if the cluster supports this type of service.

The service must be exposed through a load balancer that operates at Layer4 of the OSI model.

## Exposing the federation ingress on clusters running on bare metal

If the cluster runs on bare metal and fully supports `LoadBalancer` services, the IP address found in the `.status.loadBalancer.ingress.ip` field of the ingress gateway `Service` object should be specified as one of the entries in the `.spec.remote.addresses` field of the `ServiceMeshPeer` object.

If the cluster does not support `LoadBalancer` services, using a `NodePort` service could be an option if the nodes are accessible from the cluster running the other mesh. In the `ServiceMeshPeer` object, specify the IP addresses of the nodes in the `.spec.remote.addresses` field and the service’s node ports in the `.spec.remote.discoveryPort` and `.spec.remote.servicePort` fields.

## Exposing the federation ingress on clusters running on IBM Power and IBM Z

If the cluster runs on IBM Power® or IBM Z® infrastructure and fully supports `LoadBalancer` services, the IP address found in the `.status.loadBalancer.ingress.ip` field of the ingress gateway `Service` object should be specified as one of the entries in the `.spec.remote.addresses` field of the `ServiceMeshPeer` object.

If the cluster does not support `LoadBalancer` services, using a `NodePort` service could be an option if the nodes are accessible from the cluster running the other mesh. In the `ServiceMeshPeer` object, specify the IP addresses of the nodes in the `.spec.remote.addresses` field and the service’s node ports in the `.spec.remote.discoveryPort` and `.spec.remote.servicePort` fields.

## Exposing the federation ingress on Amazon Web Services (AWS)

By default, LoadBalancer services in clusters running on AWS do not support L4 load balancing. In order for Red Hat OpenShift Service Mesh federation to operate correctly, the following annotation must be added to the ingress gateway service:

service.beta.kubernetes.io/aws-load-balancer-type: nlb

The Fully Qualified Domain Name found in the `.status.loadBalancer.ingress.hostname` field of the ingress gateway `Service` object should be specified as one of the entries in the `.spec.remote.addresses` field of the `ServiceMeshPeer` object.

## Exposing the federation ingress on Azure

On Microsoft Azure, merely setting the service type to `LoadBalancer` suffices for mesh federation to operate correctly.

The IP address found in the `.status.loadBalancer.ingress.ip` field of the ingress gateway `Service` object should be specified as one of the entries in the `.spec.remote.addresses` field of the `ServiceMeshPeer` object.

## Exposing the federation ingress on Google Cloud

On Google Cloud, merely setting the service type to `LoadBalancer` suffices for mesh federation to operate correctly.

The IP address found in the `.status.loadBalancer.ingress.ip` field of the ingress gateway `Service` object should be specified as one of the entries in the `.spec.remote.addresses` field of the `ServiceMeshPeer` object.

# Federation implementation checklist

Federating services meshes involves the following activities:

- [ ] Configure networking between the clusters that you are going to federate.

  - [ ] Configure the load balancers supporting the services associated with the federation gateways to support raw TLS traffic.

- [ ] Installing the Red Hat OpenShift Service Mesh version 2.1 or later Operator in each of your clusters.

- [ ] Deploying a version 2.1 or later `ServiceMeshControlPlane` to each of your clusters.

- [ ] Configuring the SMCP for federation for each mesh that you want to federate:

  - [ ] Create a federation egress gateway for each mesh you are going to federate with.

  - [ ] Create a federation ingress gateway for each mesh you are going to federate with.

  - [ ] Configure a unique trust domain.

- [ ] Federate two or more meshes by creating a `ServiceMeshPeer` resource for each mesh pair.

- [ ] Export services by creating an `ExportedServiceSet` resource to make services available from one mesh to a peer mesh.

- [ ] Import services by creating an `ImportedServiceSet` resource to import services shared by a mesh peer.

# Configuring a Service Mesh control plane for federation

Before a mesh can be federated, you must configure the `ServiceMeshControlPlane` for mesh federation. Because all meshes that are members of the federation are equal, and each mesh is managed independently, you must configure the SMCP for *each* mesh that will participate in the federation.

In the following example, the administrator for the `red-mesh` is configuring the SMCP for federation with both the `green-mesh` and the `blue-mesh`.

<div class="formalpara">

<div class="title">

Sample SMCP for red-mesh

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: red-mesh
  namespace: red-mesh-system
spec:
  version: v2.6
  runtime:
    defaults:
      container:
        imagePullPolicy: Always
  gateways:
    additionalEgress:
      egress-green-mesh:
        enabled: true
        requestedNetworkView:
        - green-network
        service:
          metadata:
            labels:
              federation.maistra.io/egress-for: egress-green-mesh
          ports:
          - port: 15443
            name: tls
          - port: 8188
            name: http-discovery  #note HTTP here
      egress-blue-mesh:
        enabled: true
        requestedNetworkView:
        - blue-network
        service:
          metadata:
            labels:
              federation.maistra.io/egress-for: egress-blue-mesh
          ports:
          - port: 15443
            name: tls
          - port: 8188
            name: http-discovery  #note HTTP here
    additionalIngress:
      ingress-green-mesh:
        enabled: true
        service:
          type: LoadBalancer
          metadata:
            labels:
              federation.maistra.io/ingress-for: ingress-green-mesh
          ports:
          - port: 15443
            name: tls
          - port: 8188
            name: https-discovery  #note HTTPS here
      ingress-blue-mesh:
        enabled: true
        service:
          type: LoadBalancer
          metadata:
            labels:
              federation.maistra.io/ingress-for: ingress-blue-mesh
          ports:
          - port: 15443
            name: tls
          - port: 8188
            name: https-discovery  #note HTTPS here
  security:
    trust:
      domain: red-mesh.local
```

</div>

<table>
<caption>ServiceMeshControlPlane federation configuration parameters</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>spec:
  cluster:
    name:</code></pre></td>
<td style="text-align: left;"><p>Name of the cluster. You are not required to specify a cluster name, but it is helpful for troubleshooting.</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  cluster:
    network:</code></pre></td>
<td style="text-align: left;"><p>Name of the cluster network. You are not required to specify a name for the network, but it is helpful for configuration and troubleshooting.</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
</tbody>
</table>

## Understanding federation gateways

You use a **gateway** to manage inbound and outbound traffic for your mesh, letting you specify which traffic you want to enter or leave the mesh.

You use ingress and egress gateways to manage traffic entering and leaving the service mesh (North-South traffic). When you create a federated mesh, you create additional ingress/egress gateways, to facilitate service discovery between federated meshes, communication between federated meshes, and to manage traffic flow between service meshes (East-West traffic).

To avoid naming conflicts between meshes, you must create separate egress and ingress gateways for each mesh. For example, `red-mesh` would have separate egress gateways for traffic going to `green-mesh` and `blue-mesh`.

<table>
<caption>Federation gateway parameters</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalEgress:
      &lt;egress_name&gt;:</code></pre></td>
<td style="text-align: left;"><p>Define an additional egress gateway for <em>each</em> mesh peer in the federation.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalEgress:
      &lt;egress_name&gt;:
        enabled:</code></pre></td>
<td style="text-align: left;"><p>This parameter enables or disables the federation egress.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalEgress:
      &lt;egress_name&gt;:
        requestedNetworkView:</code></pre></td>
<td style="text-align: left;"><p>Networks associated with exported services.</p></td>
<td style="text-align: left;"><p>Set to the value of <code>spec.cluster.network</code> in the SMCP for the mesh, otherwise use &lt;ServiceMeshPeer-name&gt;-network. For example, if the <code>ServiceMeshPeer</code> resource for that mesh is named <code>west</code>, then the network would be named <code>west-network</code>.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalEgress:
      &lt;egress_name&gt;:
        service:
          metadata:
            labels:
              federation.maistra.io/egress-for:</code></pre></td>
<td style="text-align: left;"><p>Specify a unique label for the gateway to prevent federated traffic from flowing through the cluster’s default system gateways.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalEgress:
      &lt;egress_name&gt;:
        service:
          ports:</code></pre></td>
<td style="text-align: left;"><p>Used to specify the <code>port:</code> and <code>name:</code> used for TLS and service discovery. Federation traffic consists of raw encrypted TCP for service traffic.</p></td>
<td style="text-align: left;"><p>Port <code>15443</code> is required for sending TLS service requests to other meshes in the federation. Port <code>8188</code> is required for sending service discovery requests to other meshes in the federation.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:</code></pre></td>
<td style="text-align: left;"><p>Define an additional ingress gateway gateway for <em>each</em> mesh peer in the federation.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIgress:
      &lt;ingress_name&gt;:
        enabled:</code></pre></td>
<td style="text-align: left;"><p>This parameter enables or disables the federation ingress.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
<td style="text-align: left;"><p><code>true</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:
      &lt;ingress_name&gt;:
        service:
          type:</code></pre></td>
<td style="text-align: left;"><p>The ingress gateway service must be exposed through a load balancer that operates at Layer 4 of the OSI model and is publicly available.</p></td>
<td style="text-align: left;"><p><code>LoadBalancer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:
      &lt;ingress_name&gt;:
        service:
          type:</code></pre></td>
<td style="text-align: left;"><p>If the cluster does not support <code>LoadBalancer</code> services, the ingress gateway service can be exposed through a <code>NodePort</code> service.</p></td>
<td style="text-align: left;"><p><code>NodePort</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:
      &lt;ingress_name&gt;:
        service:
          metadata:
            labels:
              federation.maistra.io/ingress-for:</code></pre></td>
<td style="text-align: left;"><p>Specify a unique label for the gateway to prevent federated traffic from flowing through the cluster’s default system gateways.</p></td>
<td style="text-align: left;"></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:
      &lt;ingress_name&gt;:
        service:
          ports:</code></pre></td>
<td style="text-align: left;"><p>Used to specify the <code>port:</code> and <code>name:</code> used for TLS and service discovery. Federation traffic consists of raw encrypted TCP for service traffic. Federation traffic consists of HTTPS for discovery.</p></td>
<td style="text-align: left;"><p>Port <code>15443</code> is required for receiving TLS service requests to other meshes in the federation. Port <code>8188</code> is required for receiving service discovery requests to other meshes in the federation.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    additionalIngress:
      &lt;ingress_name&gt;:
        service:
          ports:
            nodePort:</code></pre></td>
<td style="text-align: left;"><p>Used to specify the <code>nodePort:</code> if the cluster does not support <code>LoadBalancer</code> services.</p></td>
<td style="text-align: left;"><p>If specified, is required in addition to <code>port:</code> and <code>name:</code> for both TLS and service discovery. <code>nodePort:</code> must be in the range <code>30000</code>-<code>32767</code>.</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

In the following example, the administrator is configuring the SMCP for federation with the `green-mesh` using a `NodePort` service.

<div class="formalpara">

<div class="title">

Sample SMCP for NodePort

</div>

``` yaml
apiVersion: maistra.io/v2
kind: ServiceMeshControlPlane
metadata:
  name: green-mesh
  namespace: green-mesh-system
spec:
# ...
  gateways:
     additionalIngress:
      ingress-green-mesh:
        enabled: true
        service:
          type: NodePort
          metadata:
            labels:
              federation.maistra.io/ingress-for: ingress-green-mesh
          ports:
          - port: 15443
            nodePort: 30510
            name: tls
          - port: 8188
            nodePort: 32359
            name: https-discovery
```

</div>

## Understanding federation trust domain parameters

Each mesh in the federation must have its own unique trust domain. This value is used when configuring mesh federation in the `ServiceMeshPeer` resource.

``` yaml
kind: ServiceMeshControlPlane
metadata:
  name: red-mesh
  namespace: red-mesh-system
spec:
  security:
    trust:
      domain: red-mesh.local
```

<table>
<caption>Federation security parameters</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
<th style="text-align: left;">Default value</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>spec:
  security:
    trust:
      domain:</code></pre></td>
<td style="text-align: left;"><p>Used to specify a unique name for the trust domain for the mesh. Domains must be unique for every mesh in the federation.</p></td>
<td style="text-align: left;"><p><code>&lt;mesh-name&gt;.local</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Procedure from the Console

</div>

Follow this procedure to edit the `ServiceMeshControlPlane` with the OpenShift Container Platform web console. This example uses the `red-mesh` as an example.

</div>

1.  Log in to the OpenShift Container Platform web console as a user with the cluster-admin role.

2.  Navigate to **Ecosystem** → **Installed Operators**.

3.  Click the **Project** menu and select the project where you installed the Service Mesh control plane. For example, `red-mesh-system`.

4.  Click the Red Hat OpenShift Service Mesh Operator.

5.  On the **Istio Service Mesh Control Plane** tab, click the name of your `ServiceMeshControlPlane`, for example `red-mesh`.

6.  On the **Create ServiceMeshControlPlane Details** page, click `YAML` to modify your configuration.

7.  Modify your `ServiceMeshControlPlane` to add federation ingress and egress gateways and to specify the trust domain.

8.  Click **Save**.

<div class="formalpara">

<div class="title">

Procedure from the CLI

</div>

Follow this procedure to create or edit the `ServiceMeshControlPlane` with the command line. This example uses the `red-mesh` as an example.

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.

    ``` terminal
    $ oc login --username=<NAMEOFUSER> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the Service Mesh control plane, for example red-mesh-system.

    ``` terminal
    $ oc project red-mesh-system
    ```

3.  Edit the `ServiceMeshControlPlane` file to add federation ingress and egress gateways and to specify the trust domain.

4.  Run the following command to edit the Service Mesh control plane where `red-mesh-system` is the system namespace and `red-mesh` is the name of the `ServiceMeshControlPlane` object:

    ``` terminal
    $ oc edit -n red-mesh-system smcp red-mesh
    ```

5.  Enter the following command, where `red-mesh-system` is the system namespace, to see the status of the Service Mesh control plane installation.

    ``` terminal
    $ oc get smcp -n red-mesh-system
    ```

    The installation has finished successfully when the READY column indicates that all components are ready.

        NAME       READY   STATUS            PROFILES      VERSION   AGE
        red-mesh   10/10   ComponentsReady   ["default"]   2.1.0     4m25s

# Joining a federated mesh

You declare the federation between two meshes by creating a `ServiceMeshPeer` resource. The `ServiceMeshPeer` resource defines the federation between two meshes, and you use it to configure discovery for the peer mesh, access to the peer mesh, and certificates used to validate the other mesh’s clients.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAALpCAIAAABzJpD9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjBFQUIzQjA3MEZEQjExRUNCQTY0QjRDODUyRTYyMTA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjBFQUIzQjA4MEZEQjExRUNCQTY0QjRDODUyRTYyMTA3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MEVBQjNCMDUwRkRCMTFFQ0JBNjRCNEM4NTJFNjIxMDciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MEVBQjNCMDYwRkRCMTFFQ0JBNjRCNEM4NTJFNjIxMDciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz647EP2AAChQ0lEQVR42uzd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QSvv3Lmz1vnpp59+nU/rDAsLa9So0aBBg8wTcM9/33v27Dl8+PCDBw/++uuvAwcOnD17ttZmbkArqFTaI5W5evXqLs/QOds6KWj9KrPjtaP+T53ouP7rjJvbsmVLw4YN33zzTR2C5cuXL1u2zJb/U2Xahe7duz/33HPOIzguh0Mrcd5WQVw+k6oZrXzDhg3aU/cr5DyPZuGfFgZ0AAAAAODc3XpN8KqX67z226Gflh+35dptZ7xMJtPeoFLAO3dEquvm4+3Ztvr/rpiICvFd+nztnUfSbY5LZtyep12NwK2HM9wqsTqM6TmlQnwH3l6+//VlShd3t1eYkVHY+kNDQ9PT09XHfuONN3Jzc53f0p/q95rrPtTXVS86JSXFZXGXrrWbayuoG6yiPvbYY7/88ku9evXU54+KilK/evr06S6rKojWHxgYqEK+9dZbDRo0cFm54zk73vm0rYSEhMJ3x5kWGTp0aM+ePaOjo9WfV1d/w4YNM2bMWLly5axZs1Tg89x3qVSpUvv27UeNGjVlypTHH3984sSJmZmZHTp0qFixYkGl0v6qzOaGrNMW3s06cesDeEqBT53o5uaaNGkyc+bMJUuWrFu3TjWp+ty4caPqTUfk448/LugonLYApzp1cTMaaK5ycrOE53k0C/m0zJkzhwEdAAAAADgvdSOKjX+06tRWJ16bfCh6W5LN2/N/90OdKtdepoRP57pBp32zelk//Vf45gqaJ9edbmpGrpevZ+/2ZV/oGl61jN8FrIRmzZqNGjXq0KFDVapUqVChQkGzqWc7fvx4db/VQW3atKljuqenp/NQgptrK4i6vr///ntISMhXX33VokULM7Fr166tW7d26aWbh5JoovPtYxUrVoyKilq7dm1MTMxTTz1V0FY0W3h4uPrYP/74Y+fOnc9qyKBhPvN6//79//jHP8zvhderV+88993o3bv3xIkTN23apBpYsWJFUFDQPffcU8j8LVu2HDdunHZ50aJF1113nfOgg7mexc06uVDc31xoaGi3fHqdnZ395Zdfav758+cfP368VKlS51wAHUGz4w6rVq1Seby8vMyFSG6W8IIczdN+WubNm+dJ8AUAAACA83dL/ZIL/1lrWO9KYSE+trScvKt1CpCTa78M5cvKtWXktqsbNHdwjW8eqnRhR3Oke/futWrV2rdv33333ffnn39mZmZmZWVt3Lhx8ODBmzZtcsx2xx13REZGJiQkDBgwYOHChZotJydn+/bt7777rvONJ26urSC5+dQnd75rRms79ZoLddrNrTfLli3Lzs5OTEzMyMgIDg42wx9fffXVW2+9deTIEb2Oj4//+uuvP/roI81mli1Tpox2R1uZPHnyq6++an7Q+sSJE99///2KFSucR4icJSUlaeYFCxY4Bn2CgoLMZRpa4fnvu9GqVavGjRtrW6rYo0ePNmvWzPxseUF69OhRo0YNHZcnn3xy2rRp8fnmzJnTuXPn8ePHq6hu1smF4ubmpk6d+v7775t3bfnXswQEBOgTVbx4cZdnKp0tfRrfe++9LVu2qPJ1CPRZffzxx48dO6ZPr3metJslPM+jWcinJTQ0lCt0AAAAAODC8PfxGHhj2V6NQ96fefiL32PTU7Pzfrzc43IXK8duy8ytHFns+S7hfVqXducRyOcgPDz8k08+eeCBBxYtWnTrrbc2aNDAw8Nj8+bNMTExy5Yt++2339QB1myVK1dWB/Wxxx5bvXp1z549zU+Mq2ebm5urHrh5IK77aytIzZo1W7ZsOWPGjP79+995552lS5devnz5/PnzzTN0nOesVKmSuujqb7/55psTJ05Ut1wd8ubNmw8YMEClGjVq1MsvvzxmzBjNc/jwYfXD1RtXR1qdc7P4oEGD1NX/448/3n77bS2uYmu2PXv2BAYGulzf4fDtt9++9tprH374YbNmzWrXrq2Outawfv361q1bd+nS5fz33fDz8+vVq9eSJUvMrzvddddd3t7ehR8+Fal3794qyd133129enUttW3bNrN4t27dVHVu1smFcsbNxcbGPvvss6qZkSNHNmrUqHz58jt27Jg3b56vr2+/fv0CAgLO61z2958zZ86CBQv0EVX9q1qOHz8eFBT07rvvOu5cc6dCzvNoFvJp6dixIz9bDgAAAAAXXvSelK6fbLc9tNz24HKXny2//v2tF2OL60792fJ+K2y9lwUNWPXchP1Hk7LObbXqr5q+pcuPQ59+r6Oj1WtVJ9aWf/GLurg9evRQV9ZcL+MwduzYFi1amOcih4SE9OnTR1sxl884b+WMa9PMBZVt586dt912m9mEOuc33XTTm2++aS5tcJl5/PjxNWvWNP1//bt8+XIzPS0t7e23365fv755S6u65pprzLUYzosfPHjw0UcfVSdf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R9TC1p8tWrQYO3asiVzanALWvffee+DAAVv+U6IVMrZt23bbbbeZVd1///0ffvihiURaXAHotddeW7VqlSmzKUlISIhm+7//+z/NYIKym7XnXBuO8quEWpsi9bBhw8ycWslPP/2kI6W6euaZZxTRzFI//PCD9vH555833y24f+DcqXyX72127typRK4Qbzak8kyYMEG5PywsjLsMAKuP6aTns+X/lEm7du0++eQTR/+8kDaTIonCglpmChHFixcfP368+VKxoOnnEBsvZbJQPaiF+tlnny1ZskSzaZ1ffvnlrbfeqrfMyj///HMVQ3uUlJSk/oxyweLFix2rOttkYX7k+6233lIk1wpNVWvi8OHD1YkaOHCg2uWnfsN8KZOFalgNgyFDhqhlb8ZuNKe5z0INdDXTdZT1gmQBWJ2izebNmxcuXKjQpD8VWxRaFR7N/VamSa9Iq3/VV1dsUUBw9OSdA74yyKhRoxTEpk6dqoh69OjR++67Ty/cD/7ut2MdGw0ODn7vvfe++eYbLegIO7/++qv6Jgq5p44RuJlTFOvcCdEXNqeouk5NnSqJgqei6LfffpuQkOAoicrcqFEjBfYmTZqYMbgikFPKly/vPPSmfRwxYsQbb7yRnJxsNvT999+/8MILDzzwwNX2uGhcdp5XVMj2P0lR+8SJE4mJieYaNv2ps9FcraNzu1+/fuvWrTNP1TFRW681RaFK0dxM19p0bvfp0+eLL744cOCAucpx9erVihqOZU9LoUoz6ISMjY0119EpB+ik1eI6w5VUHA/ddL8w5rQ3D4A4dOjQO++8o70z1yUqDrZv375q1apmtGVdPvM0UO2C2p379u3ThrT1rl27VqpUydx6YDiu5zQNdEWQFStWOK5FNNcBKoIrgH766adam9bvZoFP/cbAbFFBfO7cuVqhDo3+NA+52LNnz1NPPaVgum3bNh0sbVQTtTmFOQVQs0I368r9yneMjmu6guysWbM0j+Y3j95YsGCBuYmaMxywLsUTRS3FE8WBkiVL6mSfOXOmiQBqR6qZqOnOX8G5cA6VLncbuUx3P5hfrmShqlDrX1nANDE155QpUxxfpWoe1Yz5clUtzttuu808sfLckoWma8pLL730ySefaD2aR6s129WfH330kVr5BT2i4pIlC61T3aRffvnFXOtePJ9ppqve1FXTFp0/GyQLwKJ0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TovBMG7cuHPOOef999/fCU5aKoFEbH2OWAAAsy9ErIjV0NnZPPLII6tWrerVq9fhhx+evSdiNKIz4vXFF1/cZOEYABdeeOHYsWN/9atf3XzzzaNGjTrppJMKCgpuu+22GDPVi5WXl7dt2/Zvf/vb/fff/7Of/WzEiBG33357DJXZs2fvHF8Xl0kgEVufIxYAwOwLESti6xofufpMlixZEkGZn58/ePDgDRs2ZBuW++6772677TZjxowYCUOHDq25fDqdPv3006vfe9a+fftf/OIXEehz5syJ9ey///7V4d6jR4++fftWP/C0006LxW688cYXXnhh/vz5HTt2TPR5mzBhQhxFnLek7HBFRcVxxx0XOUjE1s+IBQAw+0LEiti6RkPnMxk1atSsWbOaNWv20EMP1bzud8R9kyZNxowZM2/evF133bXmQ7KfGKzWuXPnnj17zpw5c9q0aTXvr6ys3GRbxx577G9+85vFixfHOpMe7kuXLp07d25BQUFSdjgS0CZPnIitVxELAGD2hYgVsXWNhs6nl06nR4wYkZubm5eXl0ql4m/+7P1xu7CwMG7Mnz//qaee+sY3vlHzUZ/laiw7zQd/Bg4cuM8++8SpS9BzXVxcLGLrbcQCAJh9IWJFbF2jofPpTZkyZfz48ZWVlcOGDTvzzDMrKiqqA7qsrOyb3/zmpEmThg8ffu6559b8bFF2JFSbM2fOtGnTYsD07t275v1xzyabGzVqVGxi11137dSpU9JPXZs2bVq0aJGgKw1Hoql+G6GIrYcRCwBg9oWIFbF1jYbOpxehvHz58vbt25911lm77777Jr8dOnTo5MmTX3vttfjZv3//7J25ubkPPfRQt27dmjRpEv+cO3fupZdeOn/+/JYtW5500knVjy0oKIgxEGNp4MCBOVWN0ocffvi+++6LoTVkyJAOHTok/dTFgcTQTVZDZydoHotYAACzLxCxOw0NnU9p5cqVo0aNihuDBg3aPNbDqaee+vvf/3716tURqdXh3qhRo9/+9rfPPPNM9ovf/vGPf8yYMSOVSl122WU1+5eFhYULFy487rjjDjvssM6dO8cyzz///Lp163r16nXVVVc5+YhYAACzL7MvRGw9p6HzKT322GOTJ0+OGyeeeOIWF+jZs2ePHj0iTP/85z9feeWV2QsAV1ZWfv/73//rX//6u9/9LhvWbdu2HTZsWIR7zcdu2LBhyJAhe+2111133VVWVhb3NGvWLEI/hkpEv5OPiAUAMPsy+0LE1nMaOp9S+/btr7/++qZNm55wwglbXCBC+brrrnv55Zfj9vr166vj+PTTT4+If+qpp+bOnduxY8fBgwd36dJlk8fGqGjRokUMibPOOmvixIlxz3777RdLJuhroRCxIhYAMPsy+0LEitjPj4bOp3RMla0vc0iV7O1Zs2Zlb5SUlLRq1eorX/nK1h+bvQDV4CrONiIWAMDsq/7MvlL/8nms3DcrididhoZO7aUkJwERCwCA2dfH+vy+kyQvLy+dTuvpiNidg4ZO7aWk8vLynG3oB1dWVlb/BBELAGD2Vd9mXxMnTpw/f37N78beXie5adOm/fr1a9iwYTqdFnUiNuk0dGpJQUFB69atsze2vmTz5s1btmwZP500RCwAgNlXPZx9LVmyZM6cOZ/HBVYqKir22GOPjh07auiI2J2Ahk4t6dev3/Tp0+NGUVHR1pf8wx/+EFlmu3ejQcQCAJh9JcLAgQO7d++em5u7HdeZl5c3YcKEBQsWCDYRu9NwTmtJpI9mzZpty5KNGzd2uhCxAABmX/V29tWmTZsWLVps36u05OfnT5kyxdVzROzOREMHAACAOqSysrKiomK7X3ZXN4edTK5TAAAAAJAsGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACaOhAwAAAJAwGjoAAAAACbPDGjqpVMrZJ0FELACA2ReIWOqO/B0V6+vWrcvLy8tkMp6DepjpKioqkpXv6nPE5ubmTp06ddmyZX369GnRokU6nRaxAIDZl9mX2ZeIFbE7PGLzd9Qxb9iwQaGqzxU6cftcbyM2Pz//rbfeev/99zt27NiwYcNIVSIWADD7Mvsy+xKxInaHR2y+IQoidusHXlBQ0KBBg7y8vFQVwQAAmH2ZfSFiRewO56LIAAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMBo6AAAAAAmjoQMAAACQMPlOAXysVConVV+PPbfq2FNVJyG36j9qR2aHBvzG591zbZTVrnQmSXurLohYdQGjTF2AHU5DB7ahrObk1NuZe24qZFI5mar5RMpkrpYn0DtsHmnibpTVfsDH36vJmburCyJWXcAoUxdgh9PQgY/RID917VOrpi0oS+Wlql4eq19FNSYRixfvtn59q7GPVzRstDijrtaWyvL0jV9p2nvXwtrf9E9Gr5r8wdq8Ap/JNcpqRybOQLoic9XRzffrUFhakYDDVxfUBXUBo0xd4N+esyrOQ+3T0IGPEbOXf8zc8Nr0DfV0uERmzm+Wk2rxzjsVOem1OV6dqzUb0ktOSu+QLT83o3TC6+tyGpq4G2W19rdLTk55zv87qGnk21J1QcSiLmCUJa0ukKOns4No6MDHl9SG+amcVOa6Mzr13rVROu2UUBsqKzN9dm20QzZ90xc7Lj6qTV6ev9KoDbm5OT94bMHU99ZGxCVlGqguoC6AurBpachkmjZtWlBQUA+bGqlUasiQIQMHDmzfvn3Dhg3r5xlYs2ZNeXl57X9CUkMHtk06M3SfZgO7FDkT7PQO2rOJk0Bt+s3YpVOTeOlLdQF1AdSFGgoLCwsKCurnU9apU6d6HrS5uTvmPYzeOQnbqqTci7AA219lYr/IRF0AUBeq+cARtU9DBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQAAAAAEkZDBwAAACBhNHQgeSorK8vKypyHpHtl5roHxi9P1j7PXFb6++eXbSjPGGUgYlEX1AXY6cO+tIpTUWflOwWQFHPmzHn88cfHjRs3e/bs1atX77bbbl26dDmqSkFBwWdZ84YNGxo2bOgM15olaypuGLXot6MXnbR/8dkDixO056tLKi+4f9a9Lyz971M6Ht2zmVFmlCFiURfUBaOMnVJpaemZZ545derUdDr9jW9846qrrnJO6iANHUiG22+//cYbb5wxY0ak1MLCwphDvPHGG3H/3XffPXDgwOuvvz5+forV3nPPPcOHD+/YseOdd97pJNeCinTmnpc+/NmTCz+YX5KTySlqkLC3Seblpgob5I5/Z80xN7/3pf4tf3B8+94dGxllRhkiFnVBXTDK2MlMmjTpmWeeqaysrKioePjhhy+66KJmzZo5LXWNhg7UdZlM5vLLL7/lllviRpcuXU488cT999+/RYsW7733XiTZF1544dlnnz3llFOeeuqp3r17f9KVP/TQQ6NHjz7hhBOc51rw7DtrrvnL/Benr9n4addGeTml6SQeRSr+r/p7Y/iLy558c9VFh7e57Ki2rYryjTKjDBGLuqAuGGXsNP73f/+3tLR01113LSsri8iPmD/55JOdlrpGQwfqunvvvfd//ud/8vLyDj744Jtuuqlnz57Vvxo2bNhjjz12ySWXfPWrX43ZxqdYebbR7h2/n7e3Fm64/m8L//zq8kxZOqcwt2rym3BVf3usLan8+WPzR0xccdVx7c89sFVuyigzyhCxqAvqglFG4i1cuHDUqFGZTOZ73/ve6NGjH3/88eHDh2vo1EEaOlCnLV269Fe/+lUqldp7773vu+++du3a/dvcKTf3tNNO692791577bX5Y5ctWzZt2rSZM2eWlJS0b99+4MCBHTp0yP4q7nn00UdXr149Z86cRo0axc/bb7+9oqKidevWp556akxfqtcwbty4+fPn77LLLn369OnatWv1yseMGTN16tTu3bsfc8wx1bsaiT7mKLFLjRs3jntihbGVqAdHHnlk9UxoK3v16quvjh8/Pj8/P9bQpk2b6m2tW7duxIgRsbexksMPPzxZz+CK9ZU3j1l889OLV68qz2mQl9Ng57oUfV4qpu8zFpZ8/Y6Z97+87NpTOhy8V1OjzChDxIpYdUFdMMpItAi2CJhdd931y1/+coTH3//+9xdf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lz5cW5Yefv4ebZsVGGVGGSJWXVAX1AWjbMeK8xanMc5nnJZMJrMd1xxnbOjQoXHyk36Knn766ffff7958+aPPfbY3//+9+r7V69eXVRUNHr06M2bL+Xl5TX/GWHTq1evOXPmvPnmm5uc/E22dfLJJ99+++0RkHPnztXQ0dCBndCQIUNuvPHG0tLS+++/f/DgwdX3962Svf3kk09++OGHUZwOOOCA7D3Tpk079dRT33333R49ehx88MExA3jggQciVxYWFm7LRgsKCuIhbdq0OeaYY6qnFDlVH5SNRNyhQ4ds/RswYEC7du0++OCDSNYxS4gCFnvYpEmTn/3sZ88880z8KlJz3FP9jZ7buFenn376X//617feeiuWjAOPihvrPOecc+r+k3Xega36dGp87RMLHpu4PCddNXPdurL0Fwe1uvmMTjlV04kWjf/vXettm+a/fHn38orM//0BUDeWeXvRhmP/572ysnTO1r+KNp3JKU13atfwqnPbx2lpWJBrlBlliFh1QV1QF4yyHa5x48apVGrevHlxVrfvG2rKyspqRktCRZiNGDEie3vlypXV7yOLcxXRHlE6Z86cMWPGbBIbm7fGspeF2uRtaFto8xYWxprTVdR3DR3YCQ0aNOjII4984oknIrfGjc3f+LpkyZJrrrkmSki/fv2qv1Ty7rvvjnp8xBFHPPjgg9lXltatW3faaaeNHj16i1vJzf23edV+++03fPjwyNoxOdhKqYu5Qrdu3V599dV77703pgt9+vRp3759JPTddttt4sSJ8fB4bP/+/bPfwrDtexVHsddee8UKY2IRC6xevfqwww7LXuev7uvTqdGjF3T96+utrv/bwgnvrs2+yfyja2ZOkwZ5HZpv4SXKOOutm3xMft4hy6zeUPkxc58o6KWVjZrkf2to2/86ul375gVGmVGGiFUX1AV1wSirCyorKwcMGNC5c+c4Y9v941Gx8k0uupRE06dPf/nll9Pp9Pnnnx+RX92RiXAtLS0dNmzYlClTIlC/8pWv1Py68erLJGctWrTo7bffjgV69uxZ8/7Nv6F87Nix5eXlEb0dO3ZU3z+dXKcA6rL8/Pyf/vSnHTp0iOIaOTRuR4qsLhvPPffcGWecEdW3qKjoiiuuaNKkSfZX8+bNi59du3atfp9wLNC4cePN2+fZVyfWrFlT887jjz++TZs2sdoLLrgg+7WCOVUvOzz++ONr166tXqywsDBmPLHOhx9+eNWqVdlvgohZRd++fWPq8OijjxYUFFR/UHbb96ply5ZHH3107NUf//jHRx55JFZy5plnVs9LEuHkPi1evKL7LV/t3LFlQU5J5caXJT9Ceru+17cWlFdudYfL0jkV6eP3L37h8u6//lKnRMzajbKEjjJ1QcSqC+qCUWaUfVJx1HHse+6551577bXn9rb33ntnv10+0SKuli1bVlxc/PWvfz2Cqv+/9OvX78ADDzziiCMiSF599dWan6WKe5544onq1s+HH3541VVXzZ49u1mzZieccELNYRUhOn369Op7Ro0addddd8VwGDx4sG+5+vT5yimAOq5bt2733HPPxRdf/NZbb/33f//3fffd16tXr8izkRDjnuXLl0cN/tGPfnTyySdXPyT7QejIkrfeemtU/aj3I0eOHDdu3OaFeY899sjLy3v99dfPO++8qPQtWrS48sore/fuHT9jjhLbnTx58pFHHpmbm/vKK688++yzX/ziF++4446mTZtWb+g3v/lNSUlJFLDslCJy+qGHHhqbjofE9GK//fb7FHv1pS99KTYdk6eYNnXp0qXmoSVFYV5q2BFt/uMLLW4YteiO55eVlVTEXTk78XcpxIS+PN23a5OrTmh/+hdaGmVGGSJWxKoL6oJRVgd9fp/uyVRJ9MlZu3btk08+GUcxcODAPffcc/MFTjvttDvvvHPlypUjRozo06dP9s7GjRvfcMMNzz33XARbnNunn376zTffjCj6zne+079//+rHNmjQYPbs2RHYxx577O677/7uu+9GWMaqunbtetVVV/nGMQ0d2JkddthhTzzxxE033RQ1eO7cuZEBc6r63E2aNImcOGzYsGOOOabm8l/72tcmTpz48MMPX3TRRUVFRZGXBw8eHDOPhQsXZi+tV+1b3/rW6NGjZ8yYETOV+Gck2ZhMxI3vfve7hYWFv/zlL1977bVXX301u7nOnTv369ev5oeuY8bQvHnzBQsWxLyn+lsespe+jwS9//7712y3b/texWqjkDz//PPl5eXHHXdcu3btEvrEdWpZ+Nsv7/blAcXXPbHwqTdWbryrYKd7X2R64wuw7XYp/P5Rbb8zpE1RYa5RZpQhYkWsuqAuGGUkToR6NvBqvrOmpt69e3fv3v3ll1/+85//fPnll2cvlJNO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aq427o81x42SkpLKyspYMhJx9n2S1Sk+El8sU1RU1KRJk1hbw4YNs13tWD4eVXMNsd34bdyzYcOGmhWioEqsJx4Sa/6kVyCLdUZxihXGJmI9sZOxqvhnrOpjO+vZwhZqnoGaj6q58rgRK49jjP0sLS3dfOXZtWWPZRt3AEBdUBcA1AV1AQ0d6qlILkuXLr377rsjHbRu3fqGG26IHL127drq7FBcXHzppZcOGTKkf//+6So5//oA7Zo1a954441FixZFGu3Spcsee+wR2SebPWO1y5YtGz9+fNw+8MAD27ZtO3369Pfffz+SVLdu3Xbbbbfs+yTj5/PPPx+PioUbNGgQP0eMGBEpuFmzZvGoDz/8cNy4cdk1xG689NJLsa0+ffp06tQpHpLNjLNnz54xY0Y8pE2bNt27d2/evHnc3sbUFg/PrrN9+/aHHHLIzJkz33nnndil2L1YVeTKrXxGNw4kTsXcKsuXL49/7r777nvttVecmWyhql55u3btYuVxaFOnTl25cmX8s1evXrHymvUsm5fj/HzwwQdxAnfddde99947TkgtXFsOQF1QFwDUBXUBDR2SJzJL5JFIDXH7jDPOiOwcabfmApGkcnNzBw0aVN0njlQSCWXs2LF33XXX22+/HekpUkmk4GOOOeYb3/jGLrvsEg+JeyLffe9734uF//CHP0yYMGH48OGrVq0qKiqKDHX++eeffvrpsbaoDVdddVUkr0iskZTffffdb3/727GJyPWjRo2KbBVriH/+8Y9/fPnll2Nzseaf/vSne+65Z2SxeFTcM3r06IULF8a+tWzZMrLqN7/5zcMOO2yTzvdHiZ38/e9//+KLLw4ePHjWrFm33XZbrCruj0M44IADLr744tiNLabIOPw4onvvvfett96KQ8g21KNCxKOimMWpiB2oXvnhhx8eJ/C6666LQhI5vUWLFgMHDoyjjvOQzdGx5OLFi3/7298+++yzkdBjmdiBqEOXXHJJz549o96IUkBdUBfUBUBdUBfUBTR02NSbb74Z6Szy4yGHHLLFHnOkjJppIhLKI4888pOf/GTdunUdOnTo37//ihUrpk+ffs8998TPX//615Fts19h2KRJk0aNGv3mN7+JRx199NFr166NvBY56Oc///luu+124IEHNmzY8LTTTlu9evWkSZMiSUVqO/HEEyMnxmpzq2TXEMn9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" alt="Service Mesh federated mesh peers illustration" />
</figure>

Meshes are federated on a one-to-one basis, so each pair of peers requires a pair of `ServiceMeshPeer` resources specifying the federation connection to the other service mesh. For example, federating two meshes named `red` and `green` would require two `ServiceMeshPeer` files.

1.  On red-mesh-system, create a `ServiceMeshPeer` for the green mesh.

2.  On green-mesh-system, create a `ServiceMeshPeer` for the red mesh.

Federating three meshes named `red`, `blue`, and `green` would require six `ServiceMeshPeer` files.

1.  On red-mesh-system, create a `ServiceMeshPeer` for the green mesh.

2.  On red-mesh-system, create a `ServiceMeshPeer` for the blue mesh.

3.  On green-mesh-system, create a `ServiceMeshPeer` for the red mesh.

4.  On green-mesh-system, create a `ServiceMeshPeer` for the blue mesh.

5.  On blue-mesh-system, create a `ServiceMeshPeer` for the red mesh.

6.  On blue-mesh-system, create a `ServiceMeshPeer` for the green mesh.

Configuration in the `ServiceMeshPeer` resource includes the following:

- The address of the other mesh’s ingress gateway, which is used for discovery and service requests.

- The names of the local ingress and egress gateways that is used for interactions with the specified peer mesh.

- The client ID used by the other mesh when sending requests to this mesh.

- The trust domain used by the other mesh.

- The name of a `ConfigMap` containing a root certificate that is used to validate client certificates in the trust domain used by the other mesh.

In the following example, the administrator for the `red-mesh` is configuring federation with the `green-mesh`.

<div class="formalpara">

<div class="title">

Example ServiceMeshPeer resource for red-mesh

</div>

``` yaml
kind: ServiceMeshPeer
apiVersion: federation.maistra.io/v1
metadata:
  name: green-mesh
  namespace: red-mesh-system
spec:
  remote:
    addresses:
    - ingress-red-mesh.green-mesh-system.apps.domain.com
  gateways:
    ingress:
      name: ingress-green-mesh
    egress:
      name: egress-green-mesh
  security:
    trustDomain: green-mesh.local
    clientID: green-mesh.local/ns/green-mesh-system/sa/egress-red-mesh-service-account
    certificateChain:
      kind: ConfigMap
      name: green-mesh-ca-root-cert
```

</div>

<table>
<caption>ServiceMeshPeer configuration parameters</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  name:</code></pre></td>
<td style="text-align: left;"><p>Name of the peer mesh that this resource is configuring federation with.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  namespace:</code></pre></td>
<td style="text-align: left;"><p>System namespace for this mesh, that is, where the Service Mesh control plane is installed.</p></td>
<td style="text-align: left;"><p>String</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  remote:
    addresses:</code></pre></td>
<td style="text-align: left;"><p>List of public addresses of the peer meshes' ingress gateways that are servicing requests from this mesh.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  remote:
    discoveryPort:</code></pre></td>
<td style="text-align: left;"><p>The port on which the addresses are handling discovery requests.</p></td>
<td style="text-align: left;"><p>Defaults to 8188</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  remote:
    servicePort:</code></pre></td>
<td style="text-align: left;"><p>The port on which the addresses are handling service requests.</p></td>
<td style="text-align: left;"><p>Defaults to 15443</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    ingress:
      name:</code></pre></td>
<td style="text-align: left;"><p>Name of the ingress on this mesh that is servicing requests received from the peer mesh. For example, <code>ingress-green-mesh</code>.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  gateways:
    egress:
      name:</code></pre></td>
<td style="text-align: left;"><p>Name of the egress on this mesh that is servicing requests sent to the peer mesh. For example, <code>egress-green-mesh</code>.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  security:
    trustDomain:</code></pre></td>
<td style="text-align: left;"><p>The trust domain used by the peer mesh.</p></td>
<td style="text-align: left;"><p>&lt;peerMeshName&gt;.local</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  security:
    clientID:</code></pre></td>
<td style="text-align: left;"><p>The client ID used by the peer mesh when calling into this mesh.</p></td>
<td style="text-align: left;"><p>&lt;peerMeshTrustDomain&gt;/ns/&lt;peerMeshSystem&gt;/sa/&lt;peerMeshEgressGatewayName&gt;-service-account</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  security:
    certificateChain:
      kind: ConfigMap
      name:</code></pre></td>
<td style="text-align: left;"><p>The kind (for example, ConfigMap) and name of a resource containing the root certificate used to validate the client and server certificate(s) presented to this mesh by the peer mesh. The key of the config map entry containing the certificate should be <code>root-cert.pem</code>.</p></td>
<td style="text-align: left;"><p>kind: ConfigMap name: &lt;peerMesh&gt;-ca-root-cert</p></td>
</tr>
</tbody>
</table>

## Creating a ServiceMeshPeer resource

<div>

<div class="title">

Prerequisites

</div>

- Two or more OpenShift Container Platform 4.6 or above clusters.

- The clusters must already be networked.

- The load balancers supporting the services associated with the federation gateways must be configured to support raw TLS traffic.

- Each cluster must have a version 2.1 or later `ServiceMeshControlPlane` configured to support federation deployed.

- An account with the `cluster-admin` role.

</div>

<div class="formalpara">

<div class="title">

Procedure from the CLI

</div>

Follow this procedure to create a `ServiceMeshPeer` resource from the command line. This example shows the `red-mesh` creating a peer resource for the `green-mesh`.

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.

    ``` terminal
    $ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the control plane, for example, `red-mesh-system`.

    ``` terminal
    $ oc project red-mesh-system
    ```

3.  Create a `ServiceMeshPeer` file based the following example for the two meshes that you want to federate.

    <div class="formalpara">

    <div class="title">

    Example ServiceMeshPeer resource for red-mesh to green-mesh

    </div>

    ``` yaml
    kind: ServiceMeshPeer
    apiVersion: federation.maistra.io/v1
    metadata:
      name: green-mesh
      namespace: red-mesh-system
    spec:
      remote:
        addresses:
        - ingress-red-mesh.green-mesh-system.apps.domain.com
      gateways:
        ingress:
          name: ingress-green-mesh
        egress:
          name: egress-green-mesh
      security:
        trustDomain: green-mesh.local
        clientID: green-mesh.local/ns/green-mesh-system/sa/egress-red-mesh-service-account
        certificateChain:
          kind: ConfigMap
          name: green-mesh-ca-root-cert
    ```

    </div>

4.  Run the following command to deploy the resource, where `red-mesh-system` is the system namespace and `servicemeshpeer.yaml` includes a full path to the file you edited:

    ``` terminal
    $ oc create -n red-mesh-system -f servicemeshpeer.yaml
    ```

5.  To confirm that connection between the red mesh and green mesh is established, inspect the status of the green-mesh `ServiceMeshPeer` in the red-mesh-system namespace:

    ``` terminal
    $ oc -n red-mesh-system get servicemeshpeer green-mesh -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example ServiceMeshPeer connection between red-mesh and green-mesh

    </div>

    ``` yaml
    status:
      discoveryStatus:
        active:
        - pod: istiod-red-mesh-b65457658-9wq5j
          remotes:
          - connected: true
            lastConnected: "2021-10-05T13:02:25Z"
            lastFullSync: "2021-10-05T13:02:25Z"
            source: 10.128.2.149
          watch:
            connected: true
            lastConnected: "2021-10-05T13:02:55Z"
            lastDisconnectStatus: 503 Service Unavailable
            lastFullSync: "2021-10-05T13:05:43Z"
    ```

    </div>

    The `status.discoveryStatus.active.remotes` field shows that istiod in the peer mesh (in this example, the green mesh) is connected to istiod in the current mesh (in this example, the red mesh).

    The `status.discoveryStatus.active.watch` field shows that istiod in the current mesh is connected to istiod in the peer mesh.

    If you check the `servicemeshpeer` named `red-mesh` in `green-mesh-system`, you can find information about the same two connections from the perspective of the green mesh.

    When the connection between two meshes is not established, the `ServiceMeshPeer` status indicates this in the `status.discoveryStatus.inactive` field.

    For more information on why a connection attempt failed, inspect the Istiod log, the access log of the egress gateway handling egress traffic for the peer, and the ingress gateway handling ingress traffic for the current mesh in the peer mesh.

    For example, if the red mesh cannot connect to the green mesh, check the following logs:

    - istiod-red-mesh in red-mesh-system

    - egress-green-mesh in red-mesh-system

    - ingress-red-mesh in green-mesh-system

# Exporting a service from a federated mesh

Exporting services allows a mesh to share one or more of its services with another member of the federated mesh.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAALpCAIAAABzJpD9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE5RkJFMzk0MTFGNDExRUNCQTY0QjRDODUyRTYyMTA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE5RkJFMzk1MTFGNDExRUNCQTY0QjRDODUyRTYyMTA3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MTlGQkUzOTIxMUY0MTFFQ0JBNjRCNEM4NTJFNjIxMDciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MTlGQkUzOTMxMUY0MTFFQ0JBNjRCNEM4NTJFNjIxMDciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz4kE/fSAACdg0lEQVR42uzd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2T//+U/vDGhDI0eO9L6hLCoq6oYbboiJiVGBLF++vGQhFBQUPPHEE6GhoUocHh4eEBCgF06n87bbbsvMzDRp0tPT7777bu+BEmVv4MCBu3fvLme/unXr9uWXX5rMvPXWW94b/fTTT7XQ399/4cKFnkIWvfCkWbRo0YUXXuh965m+hcsuu2zNmjW+5+pU9/Sk5ZyYmBgbG6uFkZGROh70r0lTmFWGcgEAAAAAluZ02GwFbn+nvXLXrK6+uc7F/OlyuQIDAydMmNC4cWOzpE2bNlOmTBkxYsSyZcvGjx//97///f333//4448jIiLeeOMN8/QiM7+yfP7559dff33fvn1zc3PV5//222+/+OKL0NBQrcEMvmzYsOGee+5JSEho3779zTffrG6/SfPPf/5Tm9a/nlwpGzt27NizZ8/DDz/cqVMnvZuXl3fLLbd07949Li7OXKvy2muvaT0FBQUdOnTQn6tWrRo1alRycvLQoUPvuusurWHGjBkfffTRn/70p9q1a2tzZgcfffTRDz74QLkdNGjQNddco4wtWbJk5syZJa8k8li6dOnLL79cv379t99+W5nJzs5euXLltGnT2rZta8ZilIcHH3xQu9mwYcMHHnigR48e27dvnzx58sKFC0ePHj1r1qywsLBS98vtdl922WUDBgyYP3++cqvCMaMzWj59+nS73W7e9RSyzesOJhXmnXfemZiY2LRp0xtvvLF169Zbt27VSvRN7d+/v1u3bj7m6pT21Jdyjo6O1pGQlZX1/PPPr1ixonfv3n/5y19U8oUjOwzlAgAAAAAs7bu41Cdm/pyZW1BZazZX6NStW7fY1MIBAQGbN28ulnjixInqt8fExOhFu3btHA7Hs88+63l3+fLlWlVoaKj3NSb5+fl//vOftTwsLGzBggXm6g/19v38/M4///ydO3d6Uj733HP6bHR0tOfqmGuvvVaba9iw4fz580vmfN26dcFF9MJ7c9dcc43yf8MNN3gn1sq1xZ49e6akpOjPJUuWhIeH67Pjxo3TRzzJ3nnnHeWhrCt0XnjhBa35qquu8l6YmZmpPTKvtYNap8pn0aJFngT79+/v2LGjyur9998vf7+mTJmi5bVr1/ZcWaPyadSokb4LveVdyJ4cKvM33XSTdq1t27be5bB+/frZs2efUq5OaU99LGdjxIgRSql/PUu4QgcAAAAAYG3924Trv0pfc25u7r333tu0aVP12M2FIeqWl3xg+dixYzdu3PjFF1+MHz8+Ly9PXfrHH3+8WBp9tlu3bp4/tR6l+frrr7dv375w4cKBAwceOHBg1apVDodjzJgxrVu39qR86KGHZsyYofXPmTPHM5lOTk5O9+7dBw0aVDLPWVlZZg5jvfAs3L17txno6dmz5/r1683uKFnHjh21O8rDrl27lL358+dnZmZ26NDhscce877t64ILLnCXPYFO+/btAwIC1qxZM3r06B49epiJb8ydaIZyrgx36tQpKirqxx9/9AyNde7ceevWrYsWLTI3qZW1XyrPF198cefOnZ9//rkpw1mzZsXHx2tDZvSkpP37969YsUK7oCx16dLFe0fkVHPl+576WM4msXnX/GswoAMAAAAAQAXIzc0dNWpU165dy0/m5+c3YcKEFStWHDt2LDIy8rnnnjOzq5Rcm/ef0dHRrVu33rJlizr5+jMhIcE8xNp7AMJW9NSqpk2brl+/fseOHd7LT+nJU1pzcnJyeHj4008//eijj3qWOxyOwMDArKwsM9AQFxdXUFDQsmVLz8Qupea8mMGDB2udb7zxxrtFtM769eur0B555BEzGfPevXuDg4N/+umn7t27ew8MqZTcRfMQ5eXleW7pKrlfMTExw4YNmzhx4pw5c8aNGxcaGjp79myXyzV8+HC9VWqWEhMTjx496nQ6+/TpU1a2TylXPu6pj+VcVpYY0AEAAAAAWFuBy5acmV8nzFnpa87OzvYl2Zw5c9STLygoSEtLmzZt2sSJE0umKTlUYa6mMXO1BBXJyMjIzMwsmQclCw//zYVFbvcpPNNdn9VWtPIJEyZ07ty52Gc98+wEBgZqQ0p20pz/ZhjC6Rw/fvz111+/Zs2auLi4n376acuWLfPmzVu7du2CBQs6duwYExOjXejSpctzzz3ncrm8P6s/lTfvq4FK3a8bbrjh3Xff1ZpXrVpVu3btDRs21KlT58YbbywrS4FFtNGjR4+WleaUcuXjnvpYzmWWJGc+AAAAAMDSnvkq/oMVxxb/qW2z2gGVu+Zic+iUavXq1c8884xeXHnlld99992bb77ZqVOn22+/3TuN+vYOh8N7ybp16zZu3Ojn52cu2WjWrFmTJk02bdo0a9asyy67zJNsaxEl69Gjhy8ZNrOx2O1274dzN23atHHjxtpcQkLCH//4x7I+26VLl08//VR5WLNmTffu3T3LlXOzznK226WIeX3w4MHf/e53q1atWrhwYceOHZXzqVOnxsfHt2jRQvt4Gt/aBRdc0K9fv5kzZ3788cdhYWFpaWmDBg0q+cB1D21Iu7xly5b//Oc/Q4YMKTXNaeeqnD31sZw935TNaxbnwnLmzAcAAAAAWNo329P27k7fnZRduWu22+3Hjx8/ceLE8d9KTk5OS0szaZKSkh544IHDhw8PGjTo//7v/26++easrKwnnnhi3bp13qvy9/d/8cUXd+zYkZeXl5ubu3Tp0vvuu+/YsWONGjW69tprbUV3YOmz2uKHH3742muvaRP5+fnr169XsoSEhDZt2gwfPtyXPDscDnuRH374QWtITU3NycmJioq65ZZb9O4777wzYcIE5VavtYl333331VdfVTLz2REjRig/KSkp999/v3KofBYUFOzatWvixInlPOVKRfHMM88sWbLEc0FKRESEGacw8w0NHTr0vPPOO3DgwG233bZ8+XKtVoWwdevWRx99dNu2bT7ulAonODh4wYIFM2bM0IuRI0cWGyDzpsLUtvRi7ty5jzzyyL59+1QO+vfxxx/Xcn1lp5erk+6pj+Xs2Sl99uDBg/Hx8dq0ip2nXAEAAAAArO2Sl+JsN638Ni61stZsnnJVu3btTp069ejRo9tvdejQ4d577zUpR48erc75eeedt2fPHv2ZlJSk9Oqr9+3b99ixY54HMNWtWzcyMjImJuaSSy659NJL9UKd+ejo6E8//dSz0fT09OHDh2t5YGBg165dL7vssnr16tnt9jp16nzxxReeZGYASP+WmvP4+Pg2bdoEBQXFxsZqDR07dly1apWWZ2dnjxo1Sit3Op1aOHjw4AsuuMAM00ybNs3z8X//+9/BwcFaro1eWkR50Gvlv6ynXL322mu2oru6tLn777//vvvuU6FpSZ8+fY4ePWrSfPPNN40aNdJCFanWOWDAAGVPf6qUjh8/7st+KVmXLl3Ci3Tv3v3EiRPe7xZ7ypXZ31tuuUU7q11u0aJFr169mjVrZiu6Imb69Om+5+pU99THcpa///3v+nJ1VCiBsjdmzBgGdAAAAAAADOic0ZqnTp1qK5rXRj1z9bodv6W31PlXskmTJplkn3/+ueezS5cujYqK0vLbb789Nzd35cqVISEhWjJ58uRrr73W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" alt="Service Mesh federation exporting service illustration" />
</figure>

You use an `ExportedServiceSet` resource to declare the services from one mesh that you are making available to another peer in the federated mesh. You must explicitly declare each service to be shared with a peer.

- You can select services by namespace or name.

- You can use wildcards to select services; for example, to export all the services in a namespace.

- You can export services using an alias. For example, you can export the `foo/bar` service as `custom-ns/bar`.

- You can only export services that are visible to the mesh’s system namespace. For example, a service in another namespace with a `networking.istio.io/exportTo` label set to ‘.’ would not be a candidate for export.

- For exported services, their target services will only see traffic from the ingress gateway, not the original requestor (that is, they won’t see the client ID of either the other mesh’s egress gateway or the workload originating the request)

The following example is for services that `red-mesh` is exporting to `green-mesh`.

<div class="formalpara">

<div class="title">

Example ExportedServiceSet resource

</div>

``` yaml
kind: ExportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: green-mesh
  namespace: red-mesh-system
spec:
  exportRules:
  # export ratings.mesh-x-bookinfo as ratings.bookinfo
  - type: NameSelector
    nameSelector:
      namespace: red-mesh-bookinfo
      name: red-ratings
      alias:
        namespace: bookinfo
        name: ratings
  # export any service in red-mesh-bookinfo namespace with label export-service=true
  - type: LabelSelector
    labelSelector:
      namespace: red-mesh-bookinfo
      selector:
        matchLabels:
          export-service: "true"
      aliases: # export all matching services as if they were in the bookinfo namespace
      - namespace: "*"
        name: "*"
        alias:
          namespace: bookinfo
```

</div>

<table>
<caption>ExportedServiceSet parameters</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  name:</code></pre></td>
<td style="text-align: left;"><p>Name of the ServiceMeshPeer you are exposing this service to.</p></td>
<td style="text-align: left;"><p>Must match the <code>name</code> value for the mesh in the <code>ServiceMeshPeer</code> resource.</p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  namespace:</code></pre></td>
<td style="text-align: left;"><p>Name of the project/namespace containing this resource (should be the system namespace for the mesh) .</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  exportRules:
  - type:</code></pre></td>
<td style="text-align: left;"><p>Type of rule that will govern the export for this service. The first matching rule found for the service will be used for the export.</p></td>
<td style="text-align: left;"><p><code>NameSelector</code>, <code>LabelSelector</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  exportRules:
  - type: NameSelector
    nameSelector:
      namespace:
      name:</code></pre></td>
<td style="text-align: left;"><p>To create a <code>NameSelector</code> rule, specify the <code>namespace</code> of the service and the <code>name</code> of the service as defined in the <code>Service</code> resource.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  exportRules:
  - type: NameSelector
    nameSelector:
      alias:
        namespace:
        name:</code></pre></td>
<td style="text-align: left;"><p>To create a <code>NameSelector</code> rule that uses an alias for the service, after specifying the <code>namespace</code> and <code>name</code> for the service, then specify the alias for the <code>namespace</code> and the alias to be used for <code>name</code> of the service.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  exportRules:
  - type: LabelSelector
    labelSelector:
      namespace: &lt;exportingMesh&gt;
      selector:
        matchLabels:
          &lt;labelKey&gt;: &lt;labelValue&gt;</code></pre></td>
<td style="text-align: left;"><p>To create a <code>LabelSelector</code> rule, specify the <code>namespace</code> of the service and specify the <code>label</code> defined in the <code>Service</code> resource. In the example above, the label is <code>export-service</code>.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  exportRules:
  - type: LabelSelector
    labelSelector:
      namespace: &lt;exportingMesh&gt;
      selector:
        matchLabels:
          &lt;labelKey&gt;: &lt;labelValue&gt;
      aliases:
      - namespace:
        name:
        alias:
          namespace:
          name:</code></pre></td>
<td style="text-align: left;"><p>To create a <code>LabelSelector</code> rule that uses aliases for the services, after specifying the <code>selector</code>, specify the aliases to be used for <code>name</code> or <code>namespace</code> of the service. In the example above, the namespace alias is <code>bookinfo</code> for all matching services.</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Export services with the name "ratings" from all namespaces in the red-mesh to blue-mesh.

</div>

``` yaml
kind: ExportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: blue-mesh
  namespace: red-mesh-system
spec:
  exportRules:
  - type: NameSelector
    nameSelector:
      namespace: "*"
      name: ratings
```

</div>

<div class="formalpara">

<div class="title">

Export all services from the west-data-center namespace to green-mesh

</div>

``` yaml
kind: ExportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: green-mesh
  namespace: red-mesh-system
spec:
  exportRules:
  - type: NameSelector
    nameSelector:
      namespace: west-data-center
      name: "*"
```

</div>

## Creating an ExportedServiceSet

You create an `ExportedServiceSet` resource to explicitly declare the services that you want to be available to a mesh peer.

Services are exported as `<export-name>.<export-namespace>.svc.<ServiceMeshPeer.name>-exports.local` and will automatically route to the target service. This is the name by which the exported service is known in the exporting mesh. When the ingress gateway receives a request destined for this name, it will be routed to the actual service being exported. For example, if a service named `ratings.red-mesh-bookinfo` is exported to `green-mesh` as `ratings.bookinfo`, the service will be exported under the name `ratings.bookinfo.svc.green-mesh-exports.local`, and traffic received by the ingress gateway for that hostname will be routed to the `ratings.red-mesh-bookinfo` service.

> [!NOTE]
> When you set the `importAsLocal` parameter to `true` to aggregate the remote endpoint with local services, you must use an alias for the service. When you set the parameter `false`, no alias is required.

<div>

<div class="title">

Prerequisites

</div>

- The cluster and `ServiceMeshControlPlane` have been configured for mesh federation.

- An account with the `cluster-admin` role.

</div>

> [!NOTE]
> You can configure services for export even if they do not exist yet. When a service that matches the value specified in the ExportedServiceSet is deployed, it will be automatically exported.

<div class="formalpara">

<div class="title">

Procedure from the CLI

</div>

Follow this procedure to create an `ExportedServiceSet` from the command line.

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.

    ``` terminal
    $ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the Service Mesh control plane; for example, `red-mesh-system`.

    ``` terminal
    $ oc project red-mesh-system
    ```

3.  Create an `ExportedServiceSet` file based on the following example where `red-mesh` is exporting services to `green-mesh`.

    <div class="formalpara">

    <div class="title">

    Example ExportedServiceSet resource from red-mesh to green-mesh

    </div>

    ``` yaml
    apiVersion: federation.maistra.io/v1
    kind: ExportedServiceSet
    metadata:
      name: green-mesh
      namespace: red-mesh-system
    spec:
      exportRules:
      - type: NameSelector
        nameSelector:
          namespace: red-mesh-bookinfo
          name: ratings
          alias:
            namespace: bookinfo
            name: red-ratings
      - type: NameSelector
        nameSelector:
          namespace: red-mesh-bookinfo
          name: reviews
    ```

    </div>

4.  Run the following command to upload and create the `ExportedServiceSet` resource in the red-mesh-system namespace.

    ``` terminal
    $ oc create -n <ControlPlaneNamespace> -f <ExportedServiceSet.yaml>
    ```

    For example:

    ``` terminal
    $ oc create -n red-mesh-system -f export-to-green-mesh.yaml
    ```

5.  Create additional `ExportedServiceSets` as needed for each mesh peer in your federated mesh.

<div>

<div class="title">

Verification

</div>

- Run the following command to validate the services the red-mesh exports to share with green-mesh:

  ``` terminal
  $ oc get exportedserviceset <PeerMeshExportedTo> -o yaml
  ```

  For example:

  ``` terminal
  $ oc -n red-mesh-system get exportedserviceset green-mesh -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example validating the services exported from the red mesh that are shared with the green mesh.

  </div>

  ``` yaml
    status:
      exportedServices:
      - exportedName: red-ratings.bookinfo.svc.green-mesh-exports.local
        localService:
          hostname: ratings.red-mesh-bookinfo.svc.cluster.local
          name: ratings
          namespace: red-mesh-bookinfo
      - exportedName: reviews.red-mesh-bookinfo.svc.green-mesh-exports.local
        localService:
          hostname: reviews.red-mesh-bookinfo.svc.cluster.local
          name: reviews
          namespace: red-mesh-bookinfo
  ```

  </div>

  The `status.exportedServices` array lists the services that are currently exported (these services matched the export rules in the `ExportedServiceSet object`). Each entry in the array indicates the name of the exported service and details about the local service that is exported.

  If a service that you expected to be exported is missing, confirm the Service object exists, its name or labels match the `exportRules` defined in the `ExportedServiceSet` object, and that the Service object’s namespace is configured as a member of the service mesh using the `ServiceMeshMemberRoll` or `ServiceMeshMember` object.

</div>

# Importing a service into a federated mesh

Importing services lets you explicitly specify which services exported from another mesh should be accessible within your service mesh.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAALpCAIAAABzJpD9AAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyZpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDcuMS1jMDAwIDc5LmRhYmFjYmIsIDIwMjEvMDQvMTQtMDA6Mzk6NDQgICAgICAgICI+IDxyZGY6UkRGIHhtbG5zOnJkZj0iaHR0cDovL3d3dy53My5vcmcvMTk5OS8wMi8yMi1yZGYtc3ludGF4LW5zIyI+IDxyZGY6RGVzY3JpcHRpb24gcmRmOmFib3V0PSIiIHhtbG5zOnhtcD0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wLyIgeG1sbnM6eG1wTU09Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9tbS8iIHhtbG5zOnN0UmVmPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvc1R5cGUvUmVzb3VyY2VSZWYjIiB4bXA6Q3JlYXRvclRvb2w9IkFkb2JlIFBob3Rvc2hvcCAyMi41IChNYWNpbnRvc2gpIiB4bXBNTTpJbnN0YW5jZUlEPSJ4bXAuaWlkOjE5RkJFMzkwMTFGNDExRUNCQTY0QjRDODUyRTYyMTA3IiB4bXBNTTpEb2N1bWVudElEPSJ4bXAuZGlkOjE5RkJFMzkxMTFGNDExRUNCQTY0QjRDODUyRTYyMTA3Ij4gPHhtcE1NOkRlcml2ZWRGcm9tIHN0UmVmOmluc3RhbmNlSUQ9InhtcC5paWQ6MEVBQjNCMDkwRkRCMTFFQ0JBNjRCNEM4NTJFNjIxMDciIHN0UmVmOmRvY3VtZW50SUQ9InhtcC5kaWQ6MEVBQjNCMEEwRkRCMTFFQ0JBNjRCNEM4NTJFNjIxMDciLz4gPC9yZGY6RGVzY3JpcHRpb24+IDwvcmRmOlJERj4gPC94OnhtcG1ldGE+IDw/eHBhY2tldCBlbmQ9InIiPz5EfV2TAADTzUlEQVR42uzdB3xUVdrH8WnJpEJCQgsdBKQqCKIIYlkQlSKW1VUXXeuuq6517b66yrqLva6uAq+va11RrFRBQSkivXcCmARCCaSXmXn/maN3Z9MYYgi5ye/7cdnJnTv3nnvm3uec88wtzkAg4AAAAAAAAIB9uKgCAAAAAAAAeyGhAwAAAAAAYDMkdAAAAAAAAGyGhA4AAAAAAIDNkNABAAAAAACwGRI6AAAAAAAANkNCBwAAAAAAwGZI6AAAAAAAANgMCR0AAAAAAACbIaEDAAAAAABgMyR0AAAAAAAAbIaEDgAAAAAAgM2Q0AEAAAAAALAZEjoAAAAAAAA2Q0IHAAAAAADAZkjoAAAAAAAA2AwJHQAAAAAAAJshoQMAAAAAAGAzJHQAAAAAAABshoQOAAAAAACAzZDQAQAAAAAAsBkSOgAAAAAAADZDQgcAAAAAAMBmSOgAAAAAAADYDAkdAAAAAAAAmyGhAwAAAAAAYDMkdAAAAAAAAGyGhA4AAAAAAIDNkNABAAAAAACwGRI6AAAAAAAANkNCBwAAAAAAwGY8VAEAAAAAwNayC3x/m56RnlXidjlKSgJj+iaOOqGxpucV+Z+YlrFoY47D4yydryQwoEvcfcNbxESWntywcFvuuM/TC0v8DqfTEQh4Pa4HRrQ8pUOs3jqQ63tiavrePJ/b6XAGHJed3OSs4+OpZ9QpJHQAAAAAAPa2bGfeX/+9y+FyOor8jgL/roPFJqGzL7fkH99k7tue6/AEL08p8S9Nz79hcHJMZKT+mr7m4OdzM0s/ZfgD/TrEmITO2oz8J7VAcTsdAcfmvYUkdFDXkNABAAAAANibL+BwBBxd28f+eXhzh99xepefki9tEiMX3Xv81t2FP91uxO/o2Nyriebd+89tOaRLfHFJwPwZ4XGe1inOvO7XLnbK/cfvyylZm17w9Mc/+vzUMeocEjoAAAAAAJsLlCZ1WjaOuGZgcpl3OjX16r8KPxThdp7RpeLzbrwe5+gTEhzBy7Ke/nBXIEAVo87hpsgAAAAAAHvzRjgd/kCkx1njS/YHAvpfdKSTSkZd4wyQaQQAAAAA2FlhSWDamoPHt4jq2jzKLkvGsZWWlrZ3797evXvbdxNI6AAAAAAA8Ivs3bt3y5YtetG9e/f4+IZ+++TMzMy333575cqVd9xxR8+ePetgCdevX3/RRRdt3779mWeeufHGG21az1xyBQAAAADALzJt2rRTglasWGG7wufk5KxcufLAgQM1tcANGzbcfvvtkyZNqsFl1qz169evXbs2Ly/vq6++ssvX5PP5du7cuW7dOmsKCR0AAAAAgL0VlgT+Nn3399tyj9WS3W53TJDLZbNR9urVq08//fTBgwevWrWqppapSjC1oWqpm1s9dOjQ+++//8ILL3zkkUfs8k3dc889/fr1u/vuu60pPOUKAAAAAGBvS3bk3jdx67BTk6ff1tkuS64jsrKyVqxYERkZ6fE0oPxAbGzsuHHj7FXmtWvX7tmzJyIiwppCQgcAAAAAYG+FxQGH01lQErDRkuuIuLg4r7f0se4xMTE1tUynk4eC1TzzBYWe9ERCBwAAAABgb6UJBKfD5axDS167du19992nF88//3xkZOQ///nP1atXt27deuzYsX379tX0xYsXf/zxxxs2bGjTps1VV13Vp0+fMh989tlnfT7fm2++uXHjxuTk5KFDh44YMSL0BA1j//79n3zyyXfffZednd2pUyfNM3DgwNAZ/vKXv8yfP3/QoEEPPvjgO++889FHH7Vt2/aZZ57RpyZOnFhQUBAdHe0IXtGTkJCgP2+//fYzzjjDfDYjI2Py5MlLliwpLCzs2bPnyJEjy9/kWIWcNm3azJkzU1NTO3To8Nvf/tbj8Tidh3kE07x586ZPn75p06aoqKiuXbsOHjxYxS5zidbs2bM1z7Zt21q0aKF3R48ebYpa2XZpOarhqVOnNm7c+O9//3tKSoo184EDB+6+++60tLQLL7zwuuuusyr5iSee6N69e+hsn3766ffff5+ZmaltUT2cddZZJuEVZqmqt6VV1PPBgwdV1N27d69atUrbtXLlyksvvbSoqKhbt26OAAAAAAAAdjZ7/SHHpQtOf3LDsVryO++8Y+4a891335kpc+fO1Wg8MjLyb3/7W5cuXX46pcLjSUlJmTNnzltvvaW3rIktW7acOnVq6Ae9Xu91113XvHlza8wfHR190UUXaWAfut5p06b17ds3NDuQmJh46623ZmdnW/Occ845mj569OiXXnrJzNO9e3dN/+tf/+oInvHRLMhayIQJE8wHP//8865du4bmHTTbiy++GFoArWjs2LFRUf95pntCQsIll1ySnJwcWhuhfD7f/fffHxsbq5nj4+NNPagSrrzyyry8PDNPTk7OtddeG5ooUfGGDh26ZcuWKrarX79+n332mSnMP/7xj9CVfvDBB5oYERExc+ZMq5JFL6x5Zs2addJJJ4VeeqZv4eyzz168eHH4pTrSLT1sPWdkZGj30MTGjRtrf9C/Zp7SopLKBQAAAADYWoTH6fAFPK46tGRzm2QN/l9//fXrrrtuwIABixYteuGFF7Kzs3/3u995vd5HH33UmnjgwAH9OXDgwEaNGln3V/7www8vvvjiQYMGFRUVacw/Z86cjz/+ODY2duLEiSb5snz5ci05PT29e/fuv/nNbzTsN/O8+OKLfr9f/1qZIK1u/fr1W7duvf3223v16qV3i4uLL7/88v79+2/YsME6k0jL8fl8PXr00J8LFy685ppr9u/fP2rUKFPgjz766N1337377ruTkpK0Os2j5dx1111vv/22Sjts2LCRI0eqYN98882UKVPKn0lkmTt37tNPP92iRYtXX31VhSkoKFiwYMFbb73VtWtXk4tRGW699VZtZqtWrW655ZaTTz553bp1r7322syZM6+//vpPPvkkLi6uwu0KBAJnn332WWedNX36dJVWlWOyM5o+efJkp9Np3rW+HUfIFUyqzKuvvjojI6Ndu3aXXnpp586d16xZo4XMmzcvNTW1X79+YZbqiLY0nHpOTEzUnpCfn//444/Pnz9fO8nDDz+smi/N7JDKBQAAAADYWl6R7/4pP3694dCxWnL5M3T0wkzR4Nyabdy4cbGxsZGRkZo/dGJ0dHRycvLy5cutD2q20HNMSkpK/vznP2t6XFzcjBkzzNkfGu273e4TTjhh48aN1pyPPfaYPpuYmGiV5IILLvB6va1atZo+fXr5ki9dujQ6SC9CVzdy5EiHw3HJJZeEzqyFa40DBgzIysrSn9988018fLw+e9999+kj1myvv/66ylDZGTp///vfteTzzjvvv+o5L09bZF5rA02FzJo1y5ohNTW1Z8+eLpdr0qRJVW/XxIkTNT0pKck6s0b107p1a1W73irz7ZgSqvCXXXaZNq1r166h9bBs2bJPP/30iEp1RFsaZj0bF110kebUv9YUHlsOAAAAALC36AjXuNEpQ7rE18Eld+rUyXp9xhlnaBzu8XiOO+640IlOpzM3NzcnJ8eaqNn69esXer7Pvffe27Fjx/z8/JkzZ2rKjh07Fi5c6HK5brjhhs6d//MErttuu61Lly4HDx784osvrImFhYX9+/cfNmxY+eJpgc4gvbAmbtmyxSR6BgwYsGzZsh+ClixZ0rNnz6ZNm65bt27Tpk2abfr06Xl5eVr7PffcE3rZ14knnhio/AY63bt3j4yMXLx48fXXX//666/PnTt369atWpf1xHeVXAXWxiYkJPzws6ysrN69eweCF0ZVvV0jR47UZzX/hx9+aKZ88sknaWlp+iJM9qS81NTU+fPnaxNUJOtmRmZDrI+EX6rwtzTMejZ8Pp/1r8ElVwAAAAAAHC3FxcXWa+vxT+UnmqxK6AeLiopC/0xMTOzcufPq1avNID89Pd08xDo0AeEIPrWqXbt2y5YtW79+fej0I3rylJa8f//++Pj4hx566K677rKmu1wur9ebn5+vMvTr12/Dhg0+n69Tp07WjV0qLHkZw4cP1zJffvnlN4K0zBYtWvTt2/fOO+80N2Petm1bdHT05s2b+/fvH5oYioyM1J9aqWrPuqSr/HYlJyePHj16/PjxX3zxxX333RcbG/vpp5/6/f4xY8borQqLlJGRsXfvXo/Hc9ppp1VW7CMqVZhbGmY9V1YkEjoAAAAAANvLzClpEuNxu+r0kis8b6Wyk1nKpyrM2TTmXi1RQbm5uXl5eWVmKygo0Gzx8fHhrKVC+qzWooU/8cQT5gyU0Het++x4vV5zbtFhSx7K4/GMGzfu4osvXrx48YYNGzZv3rx69epp06YtWbJkxowZPXv2TE5O1ib06dPnscce8/v9oZ/Vnypb6NlAFW7XJZdc8sYbb2jJCxcuTEpKWr58edOmTS+99NLKiuQN0kr37t1b2TxHVKowtzTMeq60JjnsAQAAAAC2tn1f0VlPbrhiYNJjo1LssuSqld4hxfVfOaSlS5euWLHC7XabUzbat2/ftm3blStXfvLJJ2effbY125ogzXbyySeHuSJxOp2hD+du165dmzZttLr09PQ//elPlX22T58+H3zwgcqwePHi/v37W9NVcrPMKtbbJ8i83rlz569//euFCxfOnDmzZ8+eKvmbb76ZlpbWsWNHbWM1au/EE08cPHjwlClT3nvvvbi4uOzs7GHDhpV/4LpFK9Imr169+l//+teIESMqnKfapapiS8OsZ+ubcoTcxbm0njnyAQAAAAC2tiWzYNuWnK/WZdtoyVWLiIh48skn169fX1xcXFRUNHfu3D/+8Y/79u1r3br1BRdc4AhegfWb3/zG6XS+8847zz///P79+0tKSpYtW6bZ0tPTu3TpMmbMmHBW5HK5zNVeixYt0hIOHTpUWFiYkJBw+eWX693XX3/9iSee2L17t15rFW+88cZzzz2n2cxnL7roIpUnKyvr5ptvVglVTp/Pt2nTpvHjx1fxlKvs7OxHHnnkm2++sU5IMc/20oumTZvq31GjRh1//PE7duy48sorv/vuOy1WlbBmzZq77rpr7dq1YW6UKic6OnrGjBkfffSRXowdO7ZMgiyUKlPr0oupU6feeeed27dvVz3o33vvvVfTMzMzq1eqw25pmPVsbZQ+u3PnzrS0NK1a1c4ZOgAAAAAAe3O7nA6P0+tx2mjJVYuKipo1a9Y333zTs2dPp9O5atWqAwcONGrUaPz48e3atTPz3HTTTQsWLPj000/vueee//u//0tMTFy9evWePXuSk5PHjRvXsmXLcFbUvn371q1b79ix4/HHH//oo4927979xhtvDBgw4Oabb167du2bb7758MMPv/POO5onIyNjzZo1xcXFWr5Jf3To0OGRRx75wx/+sGzZsosvvticAqNP+f1+lT/0Hs+hJk2a9Oijjz7zzDMnn3xyt27dAoHA3LlztYGnnXbaueeeqxlU8hdeeOGqq66aN2/e6NGje/furRpYt25denr6okWLPvvss4SEhMNu19ChQ7t27bp582a9VsHMPWuqoO1dunTpBx988Pzzz0+ZMqV58+Za3fbt291u94VB1SjVYbfUrPew9WzoS1HBNmzYcP7550dHR/fq1YuEDgAAAAAAv4iG3+ZeNtZDiPSizJQjmlhUVDR+/PipU6fOmjUrJycnKSnplFNOueeee0Kf0xQbG/vmm2+++OKL7733nsb5ubm5KSkpo0aNuvvuu0Nv7msWXv5WO0bLli0ff/zxhx56aOfOnV999VVMTIw5k8Xr9b788stdunR5++23t2zZsnr16saNG3fv3v2yyy4LfarUVVddpTmff/75devWzZkzJzExccyYMUOGDLn66qvNs9XLr3HEiBH79u3Tpi1fvlxrdLvdKvbYsWPHjRunzTTznHXWWR9//LEK9v3332uxKpLm0ZLvuOMO6wbMVW9XQkKC5n/44YcdwTOJGjVqFPpu+TrXVkyYMKF3797a3m3btm3dujU5OVkbcuutt44ePTr8Uh3ploZZz/L7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XkxMjOKADtuBAweecsopOpaXLl367bffKj4osCjIlLnkqkzANze11b+KElqaFRXDD/7hzFl+pYqE4YedMNuUcEJ0TbUp+uCdd96pFlmbY7I5Ze5kp7VYodWczlO9AturTTEn7Jgt0gxaIHkuNOiEjg6AO+6448wzzzThVd57772HHnpIB5Ii7/Llyzdv3nz88ceb40TRPCsr6/PPP1+xYkV6enqzZs1OPPHEs846q0mTJmXuthMRlJaWtm/fPv3ZunVrzXPYtL1mULxITU2dO3fuhg0b9u7dqz/btWt30kknaUXmvmvWzIctjA5ytS7qVeuFNichIUGL+u677z755BO9e/PNNytwZGZm6l/zbug9fcylBCbpo3fbtm2r+Pvjjz+qDNqogwcPtmzZ0oq/qih12efMmbN48WK9GxcX16NHDzV4nTt3ViSylhl+7VllCC2/ZlMx1HbOnDlz9+7dXbt2HTNmjKao0rZv3z59+vRVq1ZpFfoqf/WrX5k7mIZfV0da+SbammtZp0yZog3XZp566qnnn3++5iSqAramvtFVV11ltQsKkuPGjXvxxRcV6xTYV69efejQocqeyW0FT31Qr9u0aaNel8JFZdOrERtrs7HQiq699lpzQ2jThLVv3159UxNgNb9i4M6dO80HtSK9a+79X+3GwvR9VVRt2qZNm/RZvTt48OC+fftWNs6p5cZC+4B65F9//fWSJUv0Fajkmk1rGTBgQIcOHcyQj8YCsDsT8Z5//nmFEQUrHbmKTg8++ODYsWNN9NYUBZn7779/x44dd9555z333GMNv8sE/I4dO6oXPWHCBAWW008//dJLLzU/CYQf/MOZM3Sl0qVLF7314YcfWmHnvPPOU9ip8NeI8NuUcEJ0DbYp+qDKo4rVehW6NZ6ymk41zXqttcybN2/t2rUKp2pYTz755P79+zdq1MiqlnrQppQvnjZcX+u0adNUV61atRoxYkSfPn0qTCcBDSKh4whek1kUZA6qUaNG/e///q9Cg46W/fv3Z2ZmqsdpjkmFjMcff1zHrUmdmojZu3fv//mf/1GgtO62oyCoT6n3P3v2bB29mqKoesstt1jNQ2X0QUXev/71rxkZGSYimGvBVKrjjjvu5ptvVtms1NJhC6OlLVy48JJLLtHMiho33njjoEGD/vCHPyhI6Zi/+OKLVbYbbrhBPWz9ecop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pJ6Dvh11vq+55hpzwbW+ZY4goB5Q0OvSpctFF1306quvNmrUSKH1/fffVxy46aabUlJSFN737ds3KcjECh3+CsjqTFb9/JMjCjjmTuq10IU+bJuSmZmp4UwNhuhqtyna0nZBaj4087p169S4/PGPf1TzqsK89tprrVu3vuCCC1SStm3b0qYADSWhY5hbiF199dULFizQMab4NWvWrEWLFp1yyik69s4+++xevXqtXr06JiZm+vTpY8eOvfjiixX+pk2b9tlnn916660333yzlqDjcNiwYTomlyxZEh8fv3v3bsX9zp0763hW7NAMOpgri7nmMeH333//xo0bL7/88jPOOENjBk3cu3evOS1Q/d3k5GSFnjALE+aGa+t69ux56qmnzpgxQws0vypojaNGjTI3EqsiFquQXbt23bRpkz6oYKRmYOjQodpALUrbm5aWNm7cOBW7ZgscvvC/ODUD4VR+hVfJAqhn1PlT7FKLoLBgemNbt27Va4VHReAOHTqoK2Zufl/hx1u1amU9DOWll17SZ1u2bDl79myFSi3ZCiPhB6g60lho4eolT5kyxcRMR/BHXbV3/fr1q/ocnzAbi+bNm6vL+8MPP2hFWuBtt92mjrjKv3379okTJ6oyX3nlFetBM8eksVDdaq+YOnWqBg+DBw/WqEPjARUsIyMjPz9fX4EZonAEAfWDYtQtt9wyf/78VatWqVevmP/ee+9pdNClSxcd7wpNu3btUgRQyDp06NCvf/1rhbVwTngMP/hXu5k4IuG0KU2aNImLi6vZEF29NkXladSo0YUXXrh48WIN1lTOp556aunSpWpiVEszZ87Uu6of1Zte0KYADSuhIzp4dPiVP0lHgUaB7MEHH7z22mvVRdaR9tVXX6l3bm6yoy7+o48+euDAgYceekgHnuLdI488cv311+to1DFsznnReEDHcLNmzczlV5UNIRRZtGS9UGzSa61UASgrK0tTtHwFWTUhKmSYhQnznp0KZGqiRo0apSBodb6PO+44czvkqts5Rfx77rlHIcmcbrpt2zYV2yxQYfSdd97p1q3bn/70pzALXOM5cnNaZjirVkMSTuUfjXMyAdQ16kUpmlldZEUMk+nOyclRQFDQS0lJUUipMKGjIHbmmWcq+unj5mKi999/X9FSH1RUDO2khh+gysTGY9VYaBX9+/fv2bOn+sTmZCVt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saiwswmdSKzzKSppPETFqVNMTdRfMaqIfOyxx9TgPOSQQ1RTH3744Wqyqu6eO3euGo0mDaEgU7Pzqquu0jZrTrVg58+frxearibo+eeff9FFFykEVdNpyp133jlv3jwt54MPPrj11ltVk5rgnjZt2o9+9CM1hnvI6Zi6VXWl/jVTtNinn3567dq1euvII4/cXjZnw4YN+hZq/e67777OHUlms3/yk59oD5t7cMyf+lIrVqxYvHixzgQ6f0ycOPH222/X17n00ktNuaqurj7wwAP/93//d6+99tLMWs4f/vAHNb+1W+677z5ticm86INXX331Mccc4/QnUuFctmzZNddc8+qrr+rkod2r2fbff/+f/exn2r2azdkkFdrf/e53zz77rGJALfZDDz307rvv7kjS9v/+97/XevfZZ5+TTz5Z1YfpMaQ/zzjjjMcff/zb3/728OHDe0hvDUzhaMKKxNN+3JCibs2aNXpx8cUXd8nmOLbN5qgKvu666xQbGzduNIdJh2D06NE61t/61rf0pyrcSy65ROdpRZ3O3++///43v/lNTd9zzz1PPfVUk9DRobn55psVzwoSFYHKysoLLrhAwWy68+hY//SnP1XAHHXUUeZy4YknnvjOd76joz9+/PjPfOYzmlJVVaWjphDSt1Cx2uFWKdK0VVayQ9zll1+euhO0arNJ2XX0/7ag/ro5m5ava+/slZPBe6D+vrD+xWUts8+sLC/0WdjRKUn1lUkWV1RUbHvVbs5Tpkd96lW7ZlNFqqKkSsl8RAVHdbhqNp1NrOSPpZs2bTIXQ3pLL9atW6clqBpU5Wx+mzIVrOn2qCmq1YcOHaolmB+yVCuqsKhS1YWRmaJNVbHSazMkp6bozKIp2gbV2+a5jT1slTmXaZnmNzHVqM6Vlgrd+vXr9adOiKntExCxRCwoZZQyStlgKwIKlcbGRhOcCi3nThQFUmqQKFAVbCY8dJ2vmFEUmWhU3JquAybzqMDWAtXoUHzW1NRoUZpoUj8jR47UWsjpZDqho9bpGQfkq9bZb7g/1Md7p3SM165dq5rloIMOSmMgsV1CVfNrr7321ltvqWl68sknqyKbOHGimqZz5859+umnv/rVr5q62+RZCpJuueUWRds555yj6YsWLVJ1fOONN+q1mp0mxWhmW7FixbJlyw455BDFuirBN998c968eQr0+++/X7Xh9jqYmA4sv/3tb80M2kWqyh988EHV0WeddZZWahJM235qyZIlmvO0005LrWTNZquQOL1ATYJfDemLLrpo9uzZ+uC//vUvtaIvvvhiFbYLL7xwxowZWqka5FddddXPfvazu+66S3/qs0OGDHnnnXf+85//qGF/wAEHaEctXLhQbfL//u///vvf/z59+vSOjg5z89qXv/xlnWM025FHHqnPahepta+Jmk0H2vk1QF9qypQpzz77rEnH6t9//vOf2oHnnntuWVmZZtZrUws4505FiL7gX//6V31ZHaysS+icN73M67EmjcpL7+MKVO0BnXS75PV0LLYtOzro5pY3/fvGG29UV1d/7nOfGzFihHbaggULdNHwgx/8QKGuiSp6V155ZX19vfb/qlWrxo8ff8opp2i20aNHm6zibbfddsUVV+jFiSeeOHnyZM2jo3b99derLr711lt1jDRdhUIFYc2aNfvtt5/mfP755011/MILL5iEjoKnoaFBATBt2rTebJXoa77yyita1/e+9z3n0V0PPPCA1njwwQfPnDkzW477/JWt18/Z/MySxs67qzI+nM3tL259dUGdYu+YiUUWdsSkF01t36UuNX9u253e/KsKUCVRpcn8pKk6UFG9efNmnUF0aa4qTiVXVZlqcpMi15WNeUKK+bguaFSC9FqX4OZJf5pTBUTLVEk001UZmjtYVbi0Cl0qmXyrXuhdK/mIOq1CW64lmN9ae94qfUpvaaIuvLQ9zjdV0TYPTOT2eCKWiAUoZZSyQZ7QMf22dPldUlJiRh1RJDQnlZeXm3aimdPcP6imvaJLLUcr2bNe8akA0zy64DdzmuykuR9Fi9JrzWOiTtE4btw4pyMbMpTQ6YgkvnFY4fmfLszx2ZFYoq/DQZguf9Jfz+pT5D3zzDOqp/bff/8jjjjC3Npz0kknvfjii++///6iRYuOPfbY1EGIVQ+effbZP/7xj02YqnF71VVXvfzyy3fccYeaoFOnTnXa2KoT1cpVo1Sr0Ne8//77Z8+evXLlyt/85je//vWve0gwffDBB6ZvQupEtYp/9rOfDR06VIWn23315ptvDh8+fM8999xhmkMbc84553z9619XyVG5mjVr1vLly3/xi1/cdNNN3/jGN5qamrT8b37zm4sXL3700UdXr1697777Wsk7v1QO1bYfO3as6Y2p/TBhwoTT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Ibv2VjItrayszBkzOHsTOmY4ZAVbc3OzXqc2yhROJvniDIzgfHfnW5uBtMUMm7vtXkr9iApUXV2d6TeQ7bsu+xI6alD4vXZHJJF1MarYmjNnjqnFGhsbUyspBa4ZzmbevHkXXHBB6ltd+pWZBw2aTiU9F2xzP1HPiQwzIJkKTOp9XuPHjz/77LPVeF64cOH7779/8MEHd1sk0s5ldltgelmKzKnL6SNqdsi2nzXpoe3txl2ywa53zDHH3HLLLapV//znPx9++OHO9AOTzOunn37adKo69NBDzZSlS5eeeeaZK1as2G+//Y444ghVrH/961+rq6u310esC/Mrjc7oM2bMSE3nmaziqFGjzLE45JBDRowYsWbNmnfeeWfBggUVFRXaQp37Z8+e/cILL+itDRs2aIrzPPVebtUXv/jFxx9//L333tOc+uIqAlrml7/85YF/sC74zNCpY/KvnbPp0dfrLUV9YEddsyKJo6aW3HDax7nj22aOufELlR8ngxKW32eXF3xYUQ8v8r3yg30i0cSHMyQLRGn+x1mb3583dsGhQ71eOxZLjC4LHDgm30IvKMC2bt1qHgtiBiCwPvpJ01SwKlwqYuYXVPObp/ldVMFvHtmgJThPFellnWwS9ypT3T4fwAxzYLbB3Gduhq43Azo4wyXoLa3RPKzEnA56s1V6rat/M4KDaB59Sss0v5KBiCViAUqZi0uZGUzafM1du2STXMv2/aNvYR5cZVIzXZ5kb5rSarQOHTq052DufdhT4fRPQsfrsWtaY6vqooftkRPte7f+fnzmvGq3JUuWLFq0SBswa9asM844w8mSmKT4j370I7Ukn3jiiZkzZ5o+jYYZjt5Utaol165du3LlStWh5rngqSkMzWkyvmZY4pdffjkajVZWVqp923P2p0vomyVoq0zSPfV+XUd5eXlVVZXJx++mXWq2oct3fPvtt7Un99hjDzPIjjZDTfouvXu0czTRzLYzNab5YUHMaHBZp7Y1uqIm9Jk9C9L7+GGHHXbcccfNmTPnoYce0ottbzuqqan56U9/am6Xcx7pfffdd69YseLYY4/929/+Zvr1KITOOuusuXPnbm8np/45ZcqUBx54QAd09uzZPdSz48aNU/wvXLjw3nvvXbp06dSpU0eOHGmehvD666+b8vLpT3/aPAOr91ulb7H33ntrgY8//rhm0OXF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" alt="Service Mesh federation importing service illustration" />
</figure>

You use an `ImportedServiceSet` resource to select services for import. Only services exported by a mesh peer and explicitly imported are available to the mesh. Services that you do not explicitly import are not made available within the mesh.

- You can select services by namespace or name.

- You can use wildcards to select services, for example, to import all the services that were exported to the namespace.

- You can select services for export using a label selector, which may be global to the mesh, or scoped to a specific member namespace.

- You can import services using an alias. For example, you can import the `custom-ns/bar` service as `other-mesh/bar`.

- You can specify a custom domain suffix, which will be appended to the `name.namespace` of an imported service for its fully qualified domain name; for example, `bar.other-mesh.imported.local`.

The following example is for the `green-mesh` importing a service that was exported by `red-mesh`.

<div class="formalpara">

<div class="title">

Example ImportedServiceSet

</div>

``` yaml
kind: ImportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: red-mesh #name of mesh that exported the service
  namespace: green-mesh-system #mesh namespace that service is being imported into
spec:
  importRules: # first matching rule is used
  # import ratings.bookinfo as ratings.bookinfo
  - type: NameSelector
    importAsLocal: false
    nameSelector:
      namespace: bookinfo
      name: ratings
      alias:
        # service will be imported as ratings.bookinfo.svc.red-mesh-imports.local
        namespace: bookinfo
        name: ratings
```

</div>

<table>
<caption>ImportedServiceSet parameters</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Values</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  name:</code></pre></td>
<td style="text-align: left;"><p>Name of the ServiceMeshPeer that exported the service to the federated mesh.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>metadata:
  namespace:</code></pre></td>
<td style="text-align: left;"><p>Name of the namespace containing the ServiceMeshPeer resource (the mesh system namespace).</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  importRules:
  - type:</code></pre></td>
<td style="text-align: left;"><p>Type of rule that will govern the import for the service. The first matching rule found for the service will be used for the import.</p></td>
<td style="text-align: left;"><p><code>NameSelector</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  importRules:
  - type: NameSelector
    nameSelector:
      namespace:
      name:</code></pre></td>
<td style="text-align: left;"><p>To create a <code>NameSelector</code> rule, specify the <code>namespace</code> and the <code>name</code> of the exported service.</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  importRules:
  - type: NameSelector
    importAsLocal:</code></pre></td>
<td style="text-align: left;"><p>Set to <code>true</code> to aggregate remote endpoint with local services. When <code>true</code> services are imported as <code>&lt;name&gt;.&lt;namespace&gt;.svc.cluster.local</code>. When <code>true</code>, an alias is required. When <code>false</code>, no alias is required.</p></td>
<td style="text-align: left;"><p><code>true</code>/<code>false</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><pre><code>spec:
  importRules:
  - type: NameSelector
    nameSelector:
      namespace:
      name:
      alias:
        namespace:
        name:</code></pre></td>
<td style="text-align: left;"><p>To create a <code>NameSelector</code> rule that uses an alias for the service, after specifying the <code>namespace</code> and <code>name</code> for the service, then specify the alias for the <code>namespace</code> and the alias to be used for <code>name</code> of the service.</p></td>
<td style="text-align: left;"></td>
</tr>
</tbody>
</table>

<div class="formalpara">

<div class="title">

Import the "bookinfo/ratings" service from the red-mesh into blue-mesh

</div>

``` yaml
kind: ImportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: red-mesh
  namespace: blue-mesh-system
spec:
  importRules:
  - type: NameSelector
    importAsLocal: false
    nameSelector:
      namespace: bookinfo
      name: ratings
```

</div>

<div class="formalpara">

<div class="title">

Import all services from the red-mesh’s west-data-center namespace into the green-mesh. These services will be accessible as \<name\>.west-data-center.svc.red-mesh-imports.local

</div>

``` yaml
kind: ImportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: red-mesh
  namespace: green-mesh-system
spec:
  importRules:
  - type: NameSelector
    importAsLocal: false
    nameSelector:
      namespace: west-data-center
      name: "*"
```

</div>

## Creating an ImportedServiceSet

You create an `ImportedServiceSet` resource to explicitly declare the services that you want to import into your mesh.

Services are imported with the name `<exported-name>.<exported-namespace>.svc.<ServiceMeshPeer.name>.remote` which is a "hidden" service, visible only within the egress gateway namespace and is associated with the exported service’s hostname. The service will be available locally as `<export-name>.<export-namespace>.<domainSuffix>`, where `domainSuffix` is `svc.<ServiceMeshPeer.name>-imports.local` by default, unless `importAsLocal` is set to `true`, in which case `domainSuffix` is `svc.cluster.local`. If `importAsLocal` is set to `false`, the domain suffix in the import rule will be applied. You can treat the local import just like any other service in the mesh. It automatically routes through the egress gateway, where it is redirected to the exported service’s remote name.

<div>

<div class="title">

Prerequisites

</div>

- The cluster and `ServiceMeshControlPlane` have been configured for mesh federation.

- An account with the `cluster-admin` role.

</div>

> [!NOTE]
> You can configure services for import even if they have not been exported yet. When a service that matches the value specified in the ImportedServiceSet is deployed and exported, it will be automatically imported.

<div class="formalpara">

<div class="title">

Procedure

</div>

Follow this procedure to create an `ImportedServiceSet` from the command line.

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.

    ``` terminal
    $ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the Service Mesh control plane; for example, `green-mesh-system`.

    ``` terminal
    $ oc project green-mesh-system
    ```

3.  Create an `ImportedServiceSet` file based on the following example where `green-mesh` is importing services previously exported by `red-mesh`.

    <div class="formalpara">

    <div class="title">

    Example ImportedServiceSet resource from red-mesh to green-mesh

    </div>

    ``` yaml
    kind: ImportedServiceSet
    apiVersion: federation.maistra.io/v1
    metadata:
      name: red-mesh
      namespace: green-mesh-system
    spec:
      importRules:
      - type: NameSelector
        importAsLocal: false
        nameSelector:
          namespace: bookinfo
          name: red-ratings
          alias:
            namespace: bookinfo
            name: ratings
    ```

    </div>

4.  Run the following command to upload and create the `ImportedServiceSet` resource in the green-mesh-system namespace.

    ``` terminal
    $ oc create -n <ControlPlaneNamespace> -f <ImportedServiceSet.yaml>
    ```

    For example:

    ``` terminal
    $ oc create -n green-mesh-system -f import-from-red-mesh.yaml
    ```

5.  Create additional `ImportedServiceSet` resources as needed for each mesh peer in your federated mesh.

<div>

<div class="title">

Verification

</div>

- Run the following command to verify that the services were imported into `green-mesh`:

  ``` terminal
  $ oc get importedserviceset <PeerMeshImportedInto> -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example verifying that the services exported from the red mesh have been imported into the green mesh using the status section of the `importedserviceset/red-mesh' object in the 'green-mesh-system` namespace

  </div>

  ``` terminal
  $ oc -n green-mesh-system get importedserviceset/red-mesh -o yaml
  ```

  </div>

  ``` yaml
  status:
    importedServices:
    - exportedName: red-ratings.bookinfo.svc.green-mesh-exports.local
      localService:
        hostname: ratings.bookinfo.svc.red-mesh-imports.local
        name: ratings
        namespace: bookinfo
    - exportedName: reviews.red-mesh-bookinfo.svc.green-mesh-exports.local
      localService:
        hostname: ""
        name: ""
        namespace: ""
  ```

  In the preceding example only the ratings service is imported, as indicated by the populated fields under `localService`. The reviews service is available for import, but is not currently imported because it does not match any `importRules` in the `ImportedServiceSet` object.

</div>

# Configuring a federated mesh for failover

Failover is the ability to switch automatically and seamlessly to a reliable backup system, for example another server. In the case of a federated mesh, you can configure a service in one mesh to failover to a service in another mesh.

You configure Federation for failover by setting the `importAsLocal` and `locality` settings in an `ImportedServiceSet` resource and then configuring a `DestinationRule` that configures failover for the service to the locality specified in the `ImportedServiceSet`.

<div>

<div class="title">

Prerequisites

</div>

- Two or more OpenShift Container Platform 4.6 or above clusters already networked and federated.

- `ExportedServiceSet` resources already created for each mesh peer in the federated mesh.

- `ImportedServiceSet` resources already created for each mesh peer in the federated mesh.

- An account with the `cluster-admin` role.

</div>

## Configuring an ImportedServiceSet for failover

Locality-weighted load balancing allows administrators to control the distribution of traffic to endpoints based on the localities of where the traffic originates and where it will terminate. These localities are specified using arbitrary labels that designate a hierarchy of localities in {region}/{zone}/{sub-zone} form.

In the examples in this section, the `green-mesh` is located in the `us-east` region, and the `red-mesh` is located in the `us-west` region.

<div class="formalpara">

<div class="title">

Example `ImportedServiceSet` resource from red-mesh to green-mesh

</div>

``` yaml
kind: ImportedServiceSet
apiVersion: federation.maistra.io/v1
metadata:
  name: red-mesh #name of mesh that exported the service
  namespace: green-mesh-system #mesh namespace that service is being imported into
spec:
  importRules: # first matching rule is used
  # import ratings.bookinfo as ratings.bookinfo
  - type: NameSelector
    importAsLocal: true
    nameSelector:
      namespace: bookinfo
      name: ratings
      alias:
        # service will be imported as ratings.bookinfo.svc.red-mesh-imports.local
        namespace: bookinfo
        name: ratings
  #Locality within which imported services should be associated.
  locality:
    region: us-west
```

</div>

| Name | Description | Type |
|----|----|----|
| region: | Region within which imported services are located. | string |
| subzone: | Subzone within which imported services are located. I Subzone is specified, Zone must also be specified. | string |
| zone: | Zone within which imported services are located. If Zone is specified, Region must also be specified. | string |

`ImportedServiceLocality` fields table

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role, enter the following command:

    ``` terminal
    $ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the Service Mesh control plane, enter the following command:

    ``` terminal
    $ oc project <smcp-system>
    ```

    For example, `green-mesh-system`.

    ``` terminal
    $ oc project green-mesh-system
    ```

3.  Edit the `ImportedServiceSet` file, where `<ImportedServiceSet.yaml>` includes a full path to the file you want to edit, enter the following command:

    ``` terminal
    $ oc edit -n <smcp-system> -f <ImportedServiceSet.yaml>
    ```

    For example, if you want to modify the file that imports from the red-mesh-system to the green-mesh-system as shown in the previous `ImportedServiceSet` example.

    ``` terminal
    $ oc edit -n green-mesh-system -f import-from-red-mesh.yaml
    ```

4.  Modify the file:

    1.  Set `spec.importRules.importAsLocal` to `true`.

    2.  Set `spec.locality` to a `region`, `zone`, or `subzone`.

    3.  Save your changes.

</div>

## Configuring a DestinationRule for failover

Create a `DestinationRule` resource that configures the following:

- Outlier detection for the service. This is required in order for failover to function properly. In particular, it configures the sidecar proxies to know when endpoints for a service are unhealthy, eventually triggering a failover to the next locality.

- Failover policy between regions. This ensures that failover beyond a region boundary will behave predictably.

<div>

<div class="title">

Procedure

</div>

1.  Log in to the OpenShift Container Platform CLI as a user with the `cluster-admin` role. Enter the following command. Then, enter your username and password when prompted.

    ``` terminal
    $ oc login --username=<NAMEOFUSER> <API token> https://<HOSTNAME>:6443
    ```

2.  Change to the project where you installed the Service Mesh control plane.

    ``` terminal
    $ oc project <smcp-system>
    ```

    For example, `green-mesh-system`.

    ``` terminal
    $ oc project green-mesh-system
    ```

3.  Create a `DestinationRule` file based on the following example where if green-mesh is unavailable, the traffic should be routed from the green-mesh in the `us-east` region to the red-mesh in `us-west`.

    <div class="formalpara">

    <div class="title">

    Example `DestinationRule`

    </div>

    ``` yaml
    apiVersion: networking.istio.io/v1beta1
    kind: DestinationRule
    metadata:
      name: default-failover
      namespace: bookinfo
    spec:
      host: "ratings.bookinfo.svc.cluster.local"
      trafficPolicy:
        loadBalancer:
          localityLbSetting:
            enabled: true
            failover:
              - from: us-east
                to: us-west
        outlierDetection:
          consecutive5xxErrors: 3
          interval: 10s
          baseEjectionTime: 1m
    ```

    </div>

4.  Deploy the `DestinationRule`, where `<DestinationRule>` includes the full path to your file, enter the following command:

    ``` terminal
    $ oc create -n <application namespace> -f <DestinationRule.yaml>
    ```

    For example:

    ``` terminal
    $ oc create -n bookinfo -f green-mesh-us-west-DestinationRule.yaml
    ```

</div>

# Removing a service from the federated mesh

If you need to remove a service from the federated mesh, for example if it has become obsolete or has been replaced by a different service, you can do so.

## To remove a service from a single mesh

Remove the entry for the service from the `ImportedServiceSet` resource for the mesh peer that no longer should access the service.

## To remove a service from the entire federated mesh

Remove the entry for the service from the `ExportedServiceSet` resource for the mesh that owns the service.

# Removing a mesh from the federated mesh

If you need to remove a mesh from the federation, you can do so.

1.  Edit the removed mesh’s `ServiceMeshControlPlane` resource to remove all federation ingress gateways for peer meshes.

2.  For each mesh peer that the removed mesh has been federated with:

    1.  Remove the `ServiceMeshPeer` resource that links the two meshes.

    2.  Edit the peer mesh’s `ServiceMeshControlPlane` resource to remove the egress gateway that serves the removed mesh.
