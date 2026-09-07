> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/optimize-proc_configuring_number_of_replicas). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Scale OpenShift Dev Spaces for high availability

Scale OpenShift Dev Spaces for high availability by defining a Kubernetes `HorizontalPodAutoscaler` (HPA) resource for OpenShift Dev Spaces operands. The HPA dynamically adjusts the number of replicas based on specified metrics.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

Create an `HPA` resource for a deployment, specifying the target metrics and desired replica count.

``` yaml
apiVersion: autoscaling/v2
kind: HorizontalPodAutoscaler
metadata:
  name: scaler
  namespace: openshift-devspaces
spec:
  scaleTargetRef:
    apiVersion: apps/v1
    kind: Deployment
    name: <deployment_name>
  ...
```

where:

` `*`<deployment_name>`*` `  
One of the following deployments:

- `devspaces`

- `che-gateway`

- `devspaces-dashboard`

- `plugin-registry`

- `devfile-registry`

  For example:

  ``` yaml
  apiVersion: autoscaling/v2
  kind: HorizontalPodAutoscaler
  metadata:
    name: devspaces-scaler
    namespace: openshift-devspaces
  spec:
    scaleTargetRef:
      apiVersion: apps/v1
      kind: Deployment
      name: devspaces
    minReplicas: 2
    maxReplicas: 5
    metrics:
      - type: Resource
        resource:
          name: cpu
          target:
            type: Utilization
            averageUtilization: 75
  ```

  In this example, the HPA targets the `devspaces` deployment with a minimum of 2 replicas, a maximum of 5 replicas, and scales based on CPU utilization.

## Results

- Verify that the HPA resource is created and targeting the correct deployment:

  ``` bash
  oc get hpa -n openshift-devspaces
  ```

**Related information**  

- [Horizontal Pod Autoscaling](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale)
