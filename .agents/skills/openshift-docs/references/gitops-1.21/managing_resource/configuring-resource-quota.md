<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With the Argo CD custom resource (CR), you can create, update, and delete resource requests and limits for Argo CD workloads.

# Configuring workloads with resource requests and limits

You can create Argo CD custom resource workloads with resource requests and limits. This is required when you want to deploy the Argo CD instance in a namespace that is configured with resource quotas.

The following Argo CD instance deploys the Argo CD workloads such as `Application Controller`, `ApplicationSet Controller`, `Dex`, `Redis`, `Repo Server`, and `Server` with resource requests and limits. You can also create the other workloads with resource requirements in the same manner.

``` yaml
apiVersion: argoproj.io/v1beta1
kind: ArgoCD
metadata:
  name: example
spec:
  server:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 125m
        memory: 128Mi
    route:
      enabled: true
  applicationSet:
    resources:
      limits:
        cpu: '2'
        memory: 1Gi
      requests:
        cpu: 250m
        memory: 512Mi
  repo:
    resources:
      limits:
        cpu: '1'
        memory: 512Mi
      requests:
        cpu: 250m
        memory: 256Mi
  dex:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  redis:
    resources:
      limits:
        cpu: 500m
        memory: 256Mi
      requests:
        cpu: 250m
        memory: 128Mi
  controller:
    resources:
      limits:
        cpu: '2'
        memory: 2Gi
      requests:
        cpu: 250m
        memory: 1Gi
```

# Patching Argo CD instance to update the resource requirements

You can update the resource requirements for all or any of the workloads post installation.

<div>

<div class="title">

Procedure

</div>

1.  Update the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

    ``` terminal
    oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/cpu", "value":"1"}]'

    oc -n argocd patch argocd example --type='json' -p='[{"op": "replace", "path": "/spec/controller/resources/requests/memory", "value":"512Mi"}]'
    ```

</div>

# Removing resource requests

You can also remove resource requirements for all or any of your workloads after installation.

<div>

<div class="title">

Procedure

</div>

1.  Remove the `Application Controller` resource requests of an Argo CD instance in the Argo CD namespace.

    ``` terminal
    oc -n argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/cpu"}]'

    oc -n argocd patch argocd example --type='json' -p='[{"op": "remove", "path": "/spec/controller/resources/requests/memory"}]'
    ```

</div>
