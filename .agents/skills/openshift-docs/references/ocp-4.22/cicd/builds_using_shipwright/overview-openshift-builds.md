<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Builds is an extensible build framework based on the [Shipwright project](https://shipwright.io/), which you can use to build container images on your OpenShift Container Platform cluster. You can build container images from source code and Dockerfiles by using image build tools, such as Source-to-Image (S2I) and Buildah. You can create and apply build resources, view logs of build runs, and manage builds in your OpenShift Container Platform namespaces.

Builds includes the following capabilities:

- Standard Kubernetes-native API for building container images from source code and Dockerfiles

- Support for Source-to-Image (S2I) and Buildah build strategies

- Extensibility with your own custom build strategies

- Execution of builds from source code in a local directory

- Shipwright CLI for creating and viewing logs, and managing builds on the cluster

- Integrated user experience with the **Developer** perspective of the OpenShift Container Platform web console

> [!NOTE]
> Because Builds releases on a different cadence from OpenShift Container Platform, the Builds documentation is now available as a separate documentation set at [Builds for Red Hat OpenShift](https://docs.redhat.com/en/documentation/builds_for_red_hat_openshift).
