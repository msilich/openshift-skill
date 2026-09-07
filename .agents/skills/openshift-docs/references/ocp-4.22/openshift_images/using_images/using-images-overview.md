<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To build and deploy containerized applications in OpenShift Container Platform, you can use Source-to-Image (S2I), database, and other container images. These images provide the base components you need to run applications on your cluster.

Red Hat official container images are provided in the Red Hat Registry at registry.redhat.io. OpenShift Container Platform’s supported S2I, database, and Jenkins images are provided in the `openshift4` repository in the Red Hat Quay Registry. For example, `quay.io/openshift-release-dev/ocp-v4.0-<address>` is the name of an OpenShift Container Platform image.

The xPaaS middleware images are provided in their product repositories on the Red Hat Registry but suffixed with a `-openshift`. For example, `registry.redhat.io/jboss-eap-6/eap64-openshift` is the name of the Red Hat JBoss Enterprise Application Platform (JBoss EAP) image.

All Red Hat supported images are described in the Red Hat Ecosystem Catalog. For every version of each image, you can find details on its contents and usage.

> [!IMPORTANT]
> The newer versions of container images are not compatible with earlier versions of OpenShift Container Platform. Verify and use the correct version of container images, based on your version of OpenShift Container Platform.

# Additional resources

- [Red Hat container registry](https://registry.redhat.io)

- [Container images section of the Red Hat Ecosystem Catalog](https://catalog.redhat.com/software/containers/explore)
