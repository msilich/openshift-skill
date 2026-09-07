<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To manage image updates and optimize pod startup performance in OpenShift Container Platform, you can configure the `imagePullPolicy` parameter in your container specifications. This setting controls when container images are pulled from registries.

# About the imagePullPolicy parameter

To control when OpenShift Container Platform pulls container images from registries or uses locally cached copies when starting containers, you can configure the `imagePullPolicy` parameter. This policy helps you manage image updates and optimize pod startup performance.

The following table lists the possible values for the `imagePullPolicy` parameter:

| Value | Description |
|----|----|
| `Always` | Always pull the image. |
| `IfNotPresent` | Only pull the image if it does not already exist on the node. |
| `Never` | Never pull the image. |

`imagePullPolicy` values

The following example sets the `imagePullPolicy` parameter to `IfNotPresent` for the image tagged `v1.2.3`:

<div class="formalpara">

<div class="title">

Example `imagePullPolicy` configuration

</div>

``` yaml
apiVersion: apps/v1
kind: Deployment
# ...
spec:
  # ...
  template:
    spec:
      containers:
      - name: my-app-container
        image: registry.example.com/myapp:v1.2.3
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 8080
```

</div>

where:

`spec.template.spec.containers.image`
Specifies is the image to use. In this example, the image tag is explicitly set to `v1.2.3`.

`spec.template.spec.containers.imagePullPolicy`
Specifies the policy to use. In this example, the policy is set to `IfNotPresent` because the image tag is not `latest`.

## Omitting the imagePullPolicy parameter

When you omit the `imagePullPolicy` parameter, OpenShift Container Platform automatically determines the policy based on the image tag. This default behavior ensures that the `latest` tag always pulls the newest image, while specific version tags use locally cached images when available to improve efficiency.

| Image tag | `imagePullPolicy` setting | Behavior |
|----|----|----|
| `latest` | `Always` | Always pulls the image. This policy helps ensure that the container always uses the latest version of the image. |
| Any other tag (for example, `v1.2.3`, `stable`, `production`) | `IfNotPresent` | Pull only if necessary. This policy uses the locally cached version of the image if it exists on the node, avoiding unnecessary pulls from the registry. |
