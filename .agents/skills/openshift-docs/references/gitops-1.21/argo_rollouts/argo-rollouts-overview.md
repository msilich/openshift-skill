<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

In the GitOps context, progressive delivery is a process of releasing application updates in a controlled and gradual manner. Progressive delivery reduces the risk of a release by exposing the new version only to a subset of users initially. The process involves continuously observing and analyzing the new version to verify that its behavior matches expectations. Verification continues as the process gradually exposes the update to a broader audience.

OpenShift Container Platform provides some progressive delivery capability by using routes to split traffic between different services, but this typically requires manual intervention and management.

With Argo Rollouts, cluster administrators can automate progressive deployment delivery for applications on Kubernetes and OpenShift Container Platform clusters. Argo Rollouts is a controller with custom resource definitions (CRDs) that provides advanced deployment capabilities such as blue-green, canary, canary analysis, and experimentation.

# Why use Argo Rollouts?

As a cluster administrator, managing and coordinating advanced deployment strategies in traditional infrastructure often involves long maintenance windows. Automation with tools like OpenShift Container Platform and Red Hat OpenShift GitOps can reduce these windows, but setting up these strategies can still be challenging.

Use Argo Rollouts to simplify progressive delivery by allowing application teams to define their rollout strategy declaratively. Teams no longer need to define multiple deployments and services or create automation for traffic shaping and integration of tests.

You can use Argo Rollouts for the following reasons:

- Your users can more easily adopt progressive delivery in end-user environments.

- With the available structure and guidelines of Argo Rollouts, your teams do not need knowledge of traffic managers and complex infrastructure.

- During an update, depending on your deployment strategy, you can optimize the existing traffic-shaping abilities of the deployed application versions by gradually shifting traffic to the new version.

- You can combine Argo Rollouts with a metric provider like Prometheus to do metric-based and policy-driven rollouts and rollbacks based on the parameters set.

- Your end-user environments get the Red Hat OpenShift GitOps Operator’s security and help to manage the resources, cost, and time effectively.

- Your existing users who use Argo CD with security and automated deployments get feedback early in the process that they can use to avoid problems that impact them.

## Benefits of Argo Rollouts

Using Argo Rollouts as a default workload in Red Hat OpenShift GitOps provides the following benefits:

- Automated progressive delivery as part of the GitOps workflow

- Advanced deployment capabilities

- Optimization of existing advanced deployment strategies, such as blue-green or canary

- Zero downtime updates for deployments

- Fine-grained, weighted traffic shifting

- Ability to test without any new traffic hitting the production environment

- Automated rollbacks and promotions

- Manual judgment

- Customizable metric queries and analysis of business key performance indicators (KPIs)

- Integration with ingress controller and Red Hat OpenShift Service Mesh for advanced traffic routing

- Integration with metric providers for deployment strategy analysis

- Usage of multiple providers

# About RolloutManager custom resources and specification

To use Argo Rollouts, you must install the Red Hat OpenShift GitOps Operator on the cluster, and then create and submit a `RolloutManager` custom resource (CR) to the Operator in the namespace of your choice. You can scope the `RolloutManager` CR for single or multiple namespaces. The Operator creates an `argo-rollouts` instance with the following namespace-scoped supporting resources:

- Argo Rollouts controller

- Argo Rollouts metrics service

- Argo Rollouts service account

- Argo Rollouts roles

- Argo Rollouts role bindings

- Argo Rollouts secret

You can specify the command arguments, environment variables, a custom image name, and so on for the Argo Rollouts controller resource in the spec of the `RolloutManager` CR. The `RolloutManager` CR spec defines the desired state of Argo Rollouts.

The following example displays a `RolloutManager` CR:

``` yaml
apiVersion: argoproj.io/v1alpha1
kind: RolloutManager
metadata:
  name: argo-rollout
  labels:
    example: basic
spec: {}
```

## Argo Rollouts controller

With the Argo Rollouts controller resource, you can manage the progressive application delivery in your namespace. The Argo Rollouts controller resource monitors the cluster for events, and reacts whenever there is a change in any resource related to Argo Rollouts. The controller reads all the rollout details and brings the cluster to the same state as described in the rollout definition.

# Argo Rollouts architecture overview

Argo Rollouts support is enabled on a cluster by installing the Red Hat OpenShift GitOps Operator and configuring a `RolloutManager` custom resource (CR) instance.

After you create a `RolloutManager` CR, the Red Hat OpenShift GitOps Operator installs Argo Rollouts in the same namespace. The Operator also installs the Argo Rollouts controller and required resources, such as CRs, roles, role bindings, and configuration data.

The Argo Rollouts controller can be installed in two different modes:

- **Cluster-scoped mode** (default): The controller oversees resources throughout all namespaces within the cluster.

- **Namespace-scoped mode**: The controller monitors resources within the namespace where Argo Rollouts is deployed.

Argo Rollouts consists of components and resources. Components manage resources. For example, the `AnalysisRun` controller manages the `AnalysisRun` CR.

Argo Rollouts uses multiple mechanisms to collect analysis metrics and verify a new application deployment:

- **Prometheus metrics**: The `AnalysisTemplate` CR connects to Prometheus to evaluate one or more metrics.

- **Kubernetes job metrics**: Argo Rollouts supports Kubernetes `Job` resources to analyze metrics. Successful jobs indicate a successful application deployment.

## Argo Rollouts components

Argo Rollouts consists of several components that enable users to practice progressive delivery in OpenShift Container Platform.

| Name | Description |
|----|----|
| Argo Rollouts controller | The Argo Rollouts Controller is an alternative to the standard `Deployment` resource and coexists alongside it. This controller only responds to changes in the Argo Rollouts resources and manages the `Rollout` CR. The Argo Rollouts Controller does not modify standard deployment resources. |
| `AnalysisRun` controller | The `AnalysisRun` controller manages and performs analysis for `AnalysisRun` and `AnalysisTemplate` CRs. It connects a rollout to the metrics provider and defines thresholds for metrics that determine if a deployment update is successful for your application. |
| `Experiment` controller | The `Experiment` controller runs analysis on short-lived replica sets and manages the `Experiment` CR. You can integrate it with a Rollout by specifying the experiment step in the canary deployment strategy. |
| `Service` and `Ingress` controller | The Service controller manages `Service` resources, and the Ingress controller manages `Ingress` resources modified by Argo Rollouts. These controllers add metadata annotations for traffic management. |
| Argo Rollouts CLI and UI | Argo Rollouts supports an `oc/kubectl` plugin called Argo Rollouts CLI. You can use it to interact with resources, such as rollouts, analyses, and experiments, from the command line. It can perform operations, such as `pause`, `promote`, or `retry`. The Argo Rollouts CLI plugin can start a local web UI dashboard in the browser to enhance the experience of visualizing the Argo Rollouts resources. |

Argo Rollouts components

## Argo Rollouts resources

Argo Rollout components manage several resources to enable progressive delivery:

- **Rollouts-specific resources**: For example, `Rollout`, `AnalysisRun`, or `Experiment`.

- **Kubernetes networking resources**: For example, `Service`, `Ingress`, or `Route` for network traffic shaping. Argo Rollouts integrate with these resources, which are referred to as traffic management.

These resources are essential for customizing the deployment of applications through the `Rollout` CR.

Argo Rollouts supports the following actions:

- Route percentage-based traffic for canary deployments.

- Forward incoming user traffic by using `Service` and `Ingress` resources to the correct application version.

- Use multiple mechanisms to collect analysis metrics to validate the deployment of a new version of an application.

| Name | Description |
|----|----|
| `Rollout` | This CR enables the deployment of applications by using canary or blue-green deployment strategies. It replaces the in-built Kubernetes `Deployment` resource. |
| `AnalysisRun` | This CR is used to perform an analysis and aggregate the results of analysis to guide the user toward the successful deployment delivery of an application. The `AnalysisRun` CR is an instance of the `AnalysisTemplate` CR. |
| `AnalysisTemplate` | The `AnalysisTemplate` CR is a template file that provides instructions on how to query metrics. The result of these instructions is attached to a rollout in the form of the `AnalysisRun` CR. The `AnalysisTemplate` CR can be defined globally on the cluster or on a specific rollout. You can link a list of `AnalysisTemplate` to be used on replica sets by creating an `Experiment` custom resource. |
| `Experiment` | The `Experiment` CR is used to run short-lived analysis on an application during its deployment to ensure the application is deployed correctly. The `Experiment` CR can be used independently or run as part of the `Rollout` CR. |
| `Service` and `Ingress` | Argo Rollouts natively support routing traffic by services and ingresses by using the Service and Ingress controllers. |
| `Route` and `VirtualService` | The OpenShift `Route` and Red Hat OpenShift Service Mesh `VirtualService` resources are used to perform traffic splitting across different application versions. |

Argo Rollouts resources

# Argo Rollouts CLI overview

You can use the Argo Rollouts CLI, which is an optional plugin, to manage and monitor Argo Rollouts resources directly, bypassing the need to use the OpenShift Container Platform web console or the CLI (`oc`).

With the Argo Rollouts CLI plugin, you can perform the following actions:

- Make changes to an Argo Rollouts image.

- Monitor the progress of an Argo Rollouts promotion.

- Proceed with the promotion steps in a canary deployment.

- Stop a failed Argo Rollouts deployment.

The Argo Rollouts CLI plugin directly integrates with `oc` and `kubectl` commands.

# Additional resources

- [Getting started with Argo Rollouts](getting-started-with-argo-rollouts.md#getting-started-with-argo-rollouts)

- [Creating RolloutManager custom resources](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-creating-rolloutmanager-custom-resource_using-argo-rollouts-for-progressive-deployment-delivery)

- [Installing the Argo Rollouts CLI](using-argo-rollouts-for-progressive-deployment-delivery.md#gitops-installing-argo-rollouts-cli-on-linux_using-argo-rollouts-for-progressive-deployment-delivery)

- [Canary deployments](https://docs.openshift.com/container-platform/latest/applications/deployments/deployment-strategies.html#deployments-canary-deployments_deployment-strategies)

- [Blue-green deployments](https://docs.openshift.com/container-platform/latest/applications/deployments/route-based-deployment-strategies.html#deployments-blue-green_route-based-deployment-strategies)

- [`RolloutManager` Custom Resource specification](https://argo-rollouts-manager.readthedocs.io/en/latest/crd_reference/)

- [Blue-green and Canary deployments with Argo Rollouts](https://www.redhat.com/architect/blue-green-canary-argo-rollouts)
