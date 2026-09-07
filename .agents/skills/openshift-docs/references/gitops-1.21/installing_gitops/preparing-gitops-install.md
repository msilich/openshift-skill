<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Read the following sizing requirements before you install Red Hat OpenShift GitOps on OpenShift Container Platform. This information includes the sizing details for the default Argo CD instance that is instantiated by the Red Hat OpenShift GitOps Operator.

# Sizing requirements for GitOps

Red Hat OpenShift GitOps is a declarative way to implement continuous deployment for cloud-native applications. Through GitOps, you can define and configure the CPU and memory requirements of your application.

When you install the Red Hat OpenShift GitOps Operator, the resources are deployed to the namespace within the defined limits. If the namespace has resource quotas configured and the installation does not set limits or requests, the Operator installation may fail. Additionally, without sufficient resources, the cluster cannot schedule Argo CD related pods.

The following table details the resource requests and limits for the default workloads.

| Workload | CPU requests | CPU limits | Memory requests | Memory limits |
|----|----|----|----|----|
| openshift-gitops-application-controller | 250m | 2 | 1024Mi | 2048Mi |
| applicationset-controller | 250m | 2 | 512Mi | 1024Mi |
| openshift-gitops-server | 125m | 500m | 128Mi | 256Mi |
| openshift-gitops-repo-server | 250m | 1 | 256Mi | 1024Mi |
| openshift-gitops-redis | 250m | 500m | 128Mi | 256Mi |
| openshift-gitops-dex-server | 250m | 500m | 128Mi | 256Mi |
| openshift-gitops-redis-ha-haproxy | 250m | 500m | 128Mi | 256Mi |

Optionally, you can also use the ArgoCD custom resource with the `oc` command to see the specifics and modify them:

``` terminal
oc edit argocd <name of argo cd> -n namespace
```

## Sizing requirements for Argo CD redis

During the capacity planning stage for your application in the Red Hat OpenShift GitOps Operator, you must ensure that an adequate amount of resources, such as memory, CPU, and storage, are allocated for the `argocd-redis` pod.

The default memory limit for the Redis pod might not be enough to manage a large number of resources. In these instances, you must increase the memory limit, monitor the memory metrics, and change the memory configuration while the application deployment scales up.

The following command shows the example of the memory configuration for a Redis pod in the `openshift-gitops` namespace:

``` terminal
$ oc get argocd -n openshift-gitops openshift-gitops -o json | jq '.spec.redis.resources'
```

Example Output:

``` terminal
{
    "limits": {
        "cpu": "500m",
        "memory": "256Mi"
  },
  "requests": {
    "cpu": "250m",
    "memory": "128Mi"
  }
}
```

where:

`limits`
Specifies the highest resource limit threshold allocated to the pod.

`requests`
Specifies the lowest resource limit threshold allocated to the pod.

The following example command changes the memory configuration for a Redis pod. The highest resource limit threshold is set to 8 Gi and the lowest is set to 256 Mi.

``` terminal
$ oc patch argocd -n openshift-gitops openshift-gitops --type json -p '[{"op": "replace", "path":  \
  "/spec/redis/resources/limits/memory", "value": "8Gi"}, {"op": "replace", "path": \
  "/spec/redis/resources/requests/memory", "value": "256Mi"}]'
```

Example Output:

``` terminal
argocd.argoproj.io/openshift-gitops patched
```
