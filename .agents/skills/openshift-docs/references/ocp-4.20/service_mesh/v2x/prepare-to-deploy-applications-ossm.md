<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After adding the namespaces that contain your services to your mesh, the next step is to enable automatic sidecar injection in the Deployment resource for your application. You must enable automatic sidecar injection for each deployment.

If you have installed the Bookinfo sample application, the application was deployed and the sidecars were injected as part of the installation procedure. If you are using your own project and service, deploy your applications on OpenShift Container Platform.

For more information, see the OpenShift Container Platform documentation, [Understanding deployments](../../applications/deployments/what-deployments-are.md).

> [!NOTE]
> Traffic started by Init Containers, specialized containers that run before the application containers in a pod, cannot travel outside of the service mesh by default. Any action Init Containers perform that requires establishing a network traffic connection outside of the mesh fails.
>
> For more information about connecting Init Containers to a service, see the Red Hat Knowledgebase solution [initContainer in CrashLoopBackOff on pod with Service Mesh sidecar injected](https://access.redhat.com/solutions/6653601)

# Prerequisites

- [Services deployed to the mesh](ossm-create-mesh.md#ossm-tutorial-bookinfo-overview_ossm-create-mesh), for example the Bookinfo sample application.

- A Deployment resource file.

# Enabling automatic sidecar injection

When deploying an application, you must opt-in to injection by configuring the label `sidecar.istio.io/inject` in `spec.template.metadata.labels` to `true` in the `deployment` object. Opting in ensures that the sidecar injection does not interfere with other OpenShift Container Platform features such as builder pods used by numerous frameworks within the OpenShift Container Platform ecosystem.

<div>

<div class="title">

Prerequisites

</div>

- Identify the namespaces that are part of your service mesh and the deployments that need automatic sidecar injection.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To find your deployments use the `oc get` command.

    ``` terminal
    $ oc get deployment -n <namespace>
    ```

    For example, to view the `Deployment` YAML file for the 'ratings-v1' microservice in the `bookinfo` namespace, use the following command to see the resource in YAML format.

    ``` terminal
    oc get deployment -n bookinfo ratings-v1 -o yaml
    ```

2.  Open the application’s `Deployment` YAML file in an editor.

3.  Add `spec.template.metadata.labels.sidecar.istio/inject` to your Deployment YAML file and set `sidecar.istio.io/inject` to `true` as shown in the following example.

    <div class="formalpara">

    <div class="title">

    Example snippet from bookinfo deployment-ratings-v1.yaml

    </div>

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: ratings-v1
      namespace: bookinfo
      labels:
        app: ratings
        version: v1
    spec:
      template:
        metadata:
          labels:
            sidecar.istio.io/inject: 'true'
    ```

    </div>

    > [!NOTE]
    > Using the `annotations` parameter when enabling automatic sidecar injection is deprecated and is replaced by using the `labels` parameter.

4.  Save the `Deployment` YAML file.

5.  Add the file back to the project that contains your app.

    ``` terminal
    $ oc apply -n <namespace> -f deployment.yaml
    ```

    In this example, `bookinfo` is the name of the project that contains the `ratings-v1` app and `deployment-ratings-v1.yaml` is the file you edited.

    ``` terminal
    $ oc apply -n bookinfo -f deployment-ratings-v1.yaml
    ```

6.  To verify that the resource uploaded successfully, run the following command.

    ``` terminal
    $ oc get deployment -n <namespace> <deploymentName> -o yaml
    ```

    For example,

    ``` terminal
    $ oc get deployment -n bookinfo ratings-v1 -o yaml
    ```

</div>

# Validating sidecar injection

The Kiali console offers several ways to validate whether or not your applications, services, and workloads have a sidecar proxy.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAADUAAAA2CAIAAADoEEaJAAAACXBIWXMAABYlAAAWJQFJUiTwAAADM0lEQVRoge2aPUzbQBTHnx3XsRODlHRISkaiDlWsqgNZEpRuNSMSVUUnUlYqqMRA16oVSB2qSunOxNJIdGu6NUq7pAsolTqQLJWCQGqJCjZ2Psh1OBQiOEgvOWxT8Zsi+3z55967957fhUMIAYCpo/WMUSo0LAOBowRCfHzCm5qSZYUDAA4hVC23MvP7jivrJhDiZ18NRaICb+rIbeIAoLbbXls2TB157gwv/vzRcloPgYNaWxDBc9u72Go6reUczAPg3WbZbrYrLd5pDT0QiFdlhVOTopb2BUI8AHxaNXOrhwDw5vPNUyOf3f8NANqM78GM3H391COWgUqFRj5rVct0vk7WNznnH9O8VBNdjOTnxjSvOi6+eFQzdQqPIthXVjh1XGSn7QTJz8Upfza3kPp16lJc804vKQCwXWm9nv3DRJmaFJ+8HAKAymYzM7//7w8S1i8Y9uAPVIa4mL6nIvjf3s5RZbMJANWto4FEsYCgr5irF3N1+6UQIe9f5lTLrXcL+0BvaIK+uOaNT3gBoLp1tJ4xzg6IRIXUlBS8xSC2mzoqFRoXmIugLxj2jN69QRwtK9zc2+GRUZarHkuIWtq3tqyXNwh1AN0aqEmRrThMIMSnHkrEW3Rf1pnlW66+t9MeVBcAAODEGEuIwTB/dk46fZ3FW1vRmYgDgOg9AbtTMOw5q+8K1i/FnIVdlWH+6Bti/miz8q3BIcYXHqdgU0e05RpziPFZwnuKtta4DNy+P671DYbb9V3Xp4NxBe3bsz61E7r61H4I9jX14+SLO5jOQt4fWton+bmRUaG74YJbLTZDXD9UKjTsl0KEvH/XM8aHjFHbdb7KItf3po7yWSuftSJRwVkv7PH+4Xj95/b4/J/qs80p6d5/K5tNnFoeP1eYVDeywnVy1d4OYUI6fcWPdTxdLCHGEoPLO+G8hgSdfYu5+vev7EN3bbedz1rEW4T+c0+CYT6ukds5fVDeaBI7V5h+9NmJq+OL5Of4y+jnsUIdF3ktLfce6BCpKYlXkyLboyxWTC8pkajA4f8f5FYP8+8tl5y1Sn5u8qkfn4Qd6wNcln5pEIO4nQTDHjUpdvLnX4+yQH3QJ8hGAAAAAElFTkSuQmCC" alt="Missing Sidecar badge" />
<figcaption>Missing sidecar badge</figcaption>
</figure>

The **Graph** page displays a node badge indicating a **Missing Sidecar** on the following graphs:

- App graph

- Versioned app graph

- Workload graph

<figure>
<img src="data:image/png;base64,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" alt="Missing Sidecar icon" />
<figcaption>Missing sidecar icon</figcaption>
</figure>

The **Applications** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar.

The **Workloads** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar.

The **Services** page displays a **Missing Sidecar** icon in the **Details** column for any applications in a namespace that do not have a sidecar. When there are multiple versions of a service, you use the **Service Details** page to view **Missing Sidecar** icons.

The **Workload Details** page has a special unified **Logs** tab that lets you view and correlate application and proxy logs. You can view the Envoy logs as another way to validate sidecar injection for your application workloads.

The **Workload Details** page also has an **Envoy** tab for any workload that is an Envoy proxy or has been injected with an Envoy proxy. This tab displays a built-in Envoy dashboard that includes subtabs for **Clusters**, **Listeners**, **Routes**, **Bootstrap**, **Config**, and **Metrics**.

For information about enabling Envoy access logs, see the [Troubleshooting](ossm-troubleshooting-istio.md#enabling-envoy-access-logs) section.

For information about viewing Envoy logs, see [Viewing logs in the Kiali console](ossm-observability.md#ossm-viewing-logs_observability).

# Setting proxy environment variables through annotations

Configuration for the Envoy sidecar proxies is managed by the `ServiceMeshControlPlane`.

You can set environment variables for the sidecar proxy for applications by adding pod annotations to the deployment in the `injection-template.yaml` file. The environment variables are injected to the sidecar.

<div class="formalpara">

<div class="title">

Example injection-template.yaml

</div>

``` yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: resource
spec:
  replicas: 7
  selector:
    matchLabels:
      app: resource
  template:
    metadata:
      annotations:
        sidecar.maistra.io/proxyEnv: "{ \"maistra_test_env\": \"env_value\", \"maistra_test_env_2\": \"env_value_2\" }"
```

</div>

> [!WARNING]
> You should never include `maistra.io/` labels and annotations when creating your own custom resources. These labels and annotations indicate that the resources are generated and managed by the Operator. If you are copying content from an Operator-generated resource when creating your own resources, do not include labels or annotations that start with `maistra.io/`. Resources that include these labels or annotations will be overwritten or deleted by the Operator during the next reconciliation.

# Updating sidecar proxies

In order to update the configuration for sidecar proxies the application administrator must restart the application pods.

If your deployment uses automatic sidecar injection, you can update the pod template in the deployment by adding or modifying an annotation. Run the following command to redeploy the pods:

``` terminal
$ oc patch deployment/<deployment> -p '{"spec":{"template":{"metadata":{"annotations":{"kubectl.kubernetes.io/restartedAt": "'`date -Iseconds`'"}}}}}'
```

If your deployment does not use automatic sidecar injection, you must manually update the sidecars by modifying the sidecar container image specified in the deployment or pod, and then restart the pods.

# Next steps

Configure Red Hat OpenShift Service Mesh features for your environment.

- [Security](ossm-security.md#ossm-security)

- [Traffic management](ossm-traffic-manage.md#ossm-routing-traffic)

- [Metrics, logs, and traces](ossm-observability.md#ossm-observability)
