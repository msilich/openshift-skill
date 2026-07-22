<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Before performing an upgrade on the cluster with applied KMM modules, you must verify that kernel modules installed using KMM are able to be installed on the nodes after the cluster upgrade and possible kernel upgrade. Preflight attempts to validate every `Module` loaded in the cluster, in parallel. Preflight does not wait for validation of one `Module` to complete before starting validation of another `Module`.

# Validation kickoff

Create a `PreflightValidationOCP` resource to trigger preflight validation and specify the kernel version and DTK image for validation.

Preflight validation is triggered by creating a `PreflightValidationOCP` resource in the cluster. This resource contains the following fields:

`dtkImage`
The DTK container image released for the specific OpenShift Container Platform version of the cluster. If this value is not set, the `DTK_AUTO` feature cannot be used.

You can obtain the image by running one of the following commands in the cluster:

``` terminal
# For x86_64 image:
$ oc adm release info quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64 --image-for=driver-toolkit
```

``` terminal
# For ARM64 image:
$ oc adm release info quay.io/openshift-release-dev/ocp-release:4.20.0-aarch64 --image-for=driver-toolkit
```

`kernelVersion`
Required field that provides the version of the kernel that the cluster is upgraded to.

You can obtain the version by running the following command in the cluster:

``` terminal
$ podman run -it --rm $(oc adm release info quay.io/openshift-release-dev/ocp-release:4.20.0-x86_64 --image-for=driver-toolkit) cat /etc/driver-toolkit-release.json
```

`pushBuiltImage`
If `true`, then the images created during the Build and Sign validation are pushed to their repositories. This field is `false` by default.

# Validation lifecycle

Preflight validation continuously validates all cluster modules, retrying failures after changes until all modules succeed or the validation resource is deleted.

Each module stops being validated after it succeeds individually. Failed modules are retried in subsequent validation loops.

If you want to run Preflight validation for an additional kernel, then you should create another `PreflightValidationOCP` resource for that kernel. After all the modules have been validated, it is recommended to delete the `PreflightValidationOCP` resource.

# Validation status

The `PreflightValidationOCP` resource reports validation status and progress for each cluster module in its `.status.modules` list.

The following outlines the fields included in the `.status.modules` list:

`name`
The name of the `Module` resource.

`namespace`
The namespace of the `Module` resource.

`statusReason`
Verbal explanation regarding the status.

`verificationStage`
Describes the validation stage being executed:

- `Image`: Image existence verification

- `Done`: Verification is done

`verificationStatus`
The status of the Module verification:

- `Success`: Verified

- `Failure`: Verification failed

- `InProgress`: Verification is in progress

# Image validation stage

Image validation checks whether kernel module images exist and are accessible before attempting to build or sign new images.

Image validation is always the first stage of the preflight validation to be executed. If image validation is successful, no other validations are run on that specific module. The Operator uses the container runtime to check the image existence and accessibility for the updaded kernel in the module.

If the image validation fails and there is a `build/sign` section in the module that is relevant to the upgraded kernel, the controller tries to build or sign the image. If the `PushBuiltImage` flag is defined in the `PreflightValidationOCP` resource, the controller will also try to push the resulting image into its repository. The resulting image name is taken from the definition of the `containerImage` field of the `Module` CR.

> [!NOTE]
> In case a `build` section exists, the input image in the `sign` section is used as the output image by the `build` section. Therefore, in order for the input image to be available to the `sign` section, the `PushBuiltImage` flag must be defined in the `PreflightValidationOCP` CR.

# Example PreflightValidationOCP resource

The example `PreflightValidationOCP` resource validates kernel modules and pushes built images to repositories.

The example verifies all of the currently present modules against the upcoming `5.14.0-570.19.1.el9_6.x86_64` kernel. Because `.spec.pushBuiltImage` is set to `true`, KMM pushes the resulting images of Build/Sign into the defined repositories.

``` yaml
apiVersion: kmm.sigs.x-k8s.io/v1beta2
kind: PreflightValidationOCP
metadata:
  name: preflight
spec:
  kernelVersion: 5.14.0-570.19.1.el9_6.x86_64
  dtkImage: quay.io/openshift-release-dev/ocp-v4.0-art-dev@sha256:fe0322730440f1cbe6fffaaa8cac131b56574bec8abe3ec5b462e17557fecb32
  pushBuiltImage: true
```
