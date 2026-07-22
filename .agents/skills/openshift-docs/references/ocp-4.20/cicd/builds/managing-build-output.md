<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the following sections for an overview of and instructions for managing build output.

# Build output

Builds that use the docker or source-to-image (S2I) strategy result in the creation of a new container image. The image is then pushed to the container image registry specified in the `output` section of the `Build` specification.

If the output kind is `ImageStreamTag`, then the image will be pushed to the integrated OpenShift image registry and tagged in the specified imagestream. If the output is of type `DockerImage`, then the name of the output reference will be used as a docker push specification. The specification may contain a registry or will default to DockerHub if no registry is specified. If the output section of the build specification is empty, then the image will not be pushed at the end of the build.

<div class="formalpara">

<div class="title">

Output to an ImageStreamTag

</div>

``` yaml
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "sample-image:latest"
```

</div>

<div class="formalpara">

<div class="title">

Output to a docker Push Specification

</div>

``` yaml
spec:
  output:
    to:
      kind: "DockerImage"
      name: "my-registry.mycompany.com:5000/myimages/myimage:tag"
```

</div>

# Output image environment variables

docker and source-to-image (S2I) strategy builds set the following environment variables on output images:

| Variable                    | Description                         |
|-----------------------------|-------------------------------------|
| `OPENSHIFT_BUILD_NAME`      | Name of the build                   |
| `OPENSHIFT_BUILD_NAMESPACE` | Namespace of the build              |
| `OPENSHIFT_BUILD_SOURCE`    | The source URL of the build         |
| `OPENSHIFT_BUILD_REFERENCE` | The Git reference used in the build |
| `OPENSHIFT_BUILD_COMMIT`    | Source commit used in the build     |

Additionally, any user-defined environment variable, for example those configured with S2I or docker strategy options, will also be part of the output image environment variable list.

# Output image labels

docker and source-to-image (S2I) builds set the following labels on output images:

| Label | Description |
|----|----|
| `io.openshift.build.commit.author` | Author of the source commit used in the build |
| `io.openshift.build.commit.date` | Date of the source commit used in the build |
| `io.openshift.build.commit.id` | Hash of the source commit used in the build |
| `io.openshift.build.commit.message` | Message of the source commit used in the build |
| `io.openshift.build.commit.ref` | Branch or reference specified in the source |
| `io.openshift.build.source-location` | Source URL for the build |

You can also use the `BuildConfig.spec.output.imageLabels` field to specify a list of custom labels that will be applied to each image built from the build configuration.

<div class="formalpara">

<div class="title">

Custom labels for built images

</div>

``` yaml
spec:
  output:
    to:
      kind: "ImageStreamTag"
      name: "my-image:latest"
    imageLabels:
    - name: "vendor"
      value: "MyCompany"
    - name: "authoritative-source-url"
      value: "registry.mycompany.com"
```

</div>
