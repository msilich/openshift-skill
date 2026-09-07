<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can manage the Compliance Operator security content lifecycle to keep compliance profiles current and create custom `ProfileBundle` objects tailored to your organization security requirements.

# ProfileBundle CR example

You can configure a `ProfileBundle` to provide the Compliance Operator with the security profiles it needs to scan your cluster.

A `ProfileBundle` custom resource (CR) defines the container image URL in `contentImage` and the compliance content file path in `contentFile`, relative to the root of the file system.

``` yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
metadata:
  creationTimestamp: "2022-10-19T12:06:30Z"
  finalizers:
  - profilebundle.finalizers.compliance.openshift.io
  generation: 1
  name: rhcos4
  namespace: openshift-compliance
  resourceVersion: "46741"
  uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
spec:
  contentFile: ssg-rhcos4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e...
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
```

where:

`spec.contentFile`
Specifies the location of the file containing the compliance content.

`spec.contentImage`
Specifies the content image location.

> [!IMPORTANT]
> The base image used for the content images must include `coreutils`.

# Updating security content

Track `ProfileBundle` updates accurately and ensure predictable compliance profile versions across cluster deployments, by using container image digests instead of tags.

Security content is included as container images that the `ProfileBundle` objects refer to. To accurately track updates to `ProfileBundles` and the custom resources parsed from the bundles, such as rules or profiles, you can view the container image digest in the `ProfileBundle` status.

``` terminal
$ oc -n openshift-compliance get profilebundles rhcos4 -oyaml
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: ProfileBundle
metadata:
  creationTimestamp: "2022-10-19T12:06:30Z"
  finalizers:
  - profilebundle.finalizers.compliance.openshift.io
  generation: 1
  name: rhcos4
  namespace: openshift-compliance
  resourceVersion: "46741"
  uid: 22350850-af4a-4f5c-9a42-5e7b68b82d7d
spec:
  contentFile: ssg-rhcos4-ds.xml
  contentImage: registry.redhat.io/compliance/openshift-compliance-content-rhel8@sha256:900e...
status:
  conditions:
  - lastTransitionTime: "2022-10-19T12:07:51Z"
    message: Profile bundle successfully parsed
    reason: Valid
    status: "True"
    type: Ready
  dataStreamStatus: VALID
```

</div>

where:

`spec.contentImage`
Specifies the security container image.

Each `ProfileBundle` is backed by a deployment. When the Compliance Operator detects that the container image digest has changed, the deployment is updated to reflect the change and parse the content again. Using the digest instead of a tag ensures that you use a stable and predictable set of profiles.

# Additional resources

- [Using Operator Lifecycle Manager in disconnected environments](../../../disconnected/using-olm.md#olm-restricted-networks)
