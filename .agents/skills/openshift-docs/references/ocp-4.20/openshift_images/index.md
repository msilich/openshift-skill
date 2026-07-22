<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To understand how containerized applications work in OpenShift Container Platform, you need to know about containers, images, and image streams. This overview explains these core concepts and how they work together in your cluster.

# Images

Container images are binaries that include all requirements for running a single container. You can use images to package applications and deploy them consistently across multiple containers and hosts in OpenShift Container Platform.

Containers only have access to resources defined in the image unless you give the container additional access when creating it. By deploying the same image in multiple containers across multiple hosts and load balancing between them, OpenShift Container Platform can provide redundancy and horizontal scaling for a service packaged into an image.

You can use the [podman](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/managing_containers/#using_podman_to_work_with_containers) or `docker` CLI directly to build images, but OpenShift Container Platform also supplies builder images that assist with creating new images by adding your code or configuration to existing images.

Because applications develop over time, a single image name can actually refer to many different versions of the same image. Each different image is referred to uniquely by its hash, a long hexadecimal number such as `fd44297e2ddb050ec4f…​`, which is usually shortened to 12 characters, such as `fd44297e2ddb`.

# Additional resources

- [Creating images](create-images.md#creating-images)

- [Managing images](managing_images/managing-images-overview.md#managing-images-overview)

- [Using images](using_images/using-images-overview.md#using-images-overview)

# Image registry

An image registry is a content server that stores and serves container images in OpenShift Container Platform. You can use registries to access container images from external sources or the integrated registry in OpenShift Container Platform.

Registries contain a collection of one or more image repositories, which contain one or more tagged images. Red Hat provides a registry at [registry.redhat.io](https://catalog.redhat.com/en) for subscribers. OpenShift Container Platform can also supply its own OpenShift image registry for managing custom container images.

# Image repository

An image repository is a collection of related container images and tags that identify them. You can use image repositories to organize and manage related container images in OpenShift Container Platform.

For example, the OpenShift Container Platform Jenkins images are in the following repository:

``` text
docker.io/openshift/jenkins-2-centos7
```

# Understanding image tags in image streams

Image tags in OpenShift Container Platform help you organize, identify, and reference specific versions of container images in image streams. Tags are human-readable labels that act as pointers to particular image layers and digests.

Tags function as mutable pointers within an image stream. When a new image is imported or tagged into the stream, the tag is updated to point to the new image’s immutable SHA digest. A single image digest can have multiple tags simultaneously assigned to it. For example, the `:v3.11.59-2` and `:latest` tags are assigned to the same image digest.

Tags offer two main benefits:

- Tags serve as the primary mechanism for builds and deployments to request a specific version of an image from an image stream.

- Tags help maintain clarity and allow for easy promotion of images between environments. For example, you can promote an image from the `:test` tag to the `:prod` tag.

While image tags are primarily used for referencing images in configurations, OpenShift Container Platform provides the `oc tag` command for managing tags directly within image streams. This command is similar to the `podman tag` or `docker tag` commands, but it operates on image streams instead of directly on local images. It is used to create a new tag pointer or update an existing tag pointer within an image stream to point to a new image.

Image tags are appended to the image name or image stream name by using a colon (`:`) as a separator.

| Context | Syntax Format | Example |
|----|----|----|
| **External Registry** | `<registry_path>:<tag>` | `registry.access.redhat.com/openshift3/jenkins-2-rhel7:v3.11.59-2` |
| **Local Image Stream** | `<image_stream_name>:<tag>` | `jenkins:latest` |

# Image IDs

Image IDs are Secure Hash Algorithm (SHA) codes that uniquely identify container images in OpenShift Container Platform. You can use image IDs to pull specific versions of images that never change.

For example, the following image ID is for the `docker.io/openshift/jenkins-2-centos7` image:

``` text
docker.io/openshift/jenkins-2-centos7@sha256:ab312bda324
```

# Containers

Containers are isolated running instances of container images that serve as the basic units of OpenShift Container Platform applications. By understanding containers, you can work with containerized applications and manage how they run in your cluster.

Many application instances can be running in containers on a single host without visibility into each others' processes, files, network, and so on. Typically, each container provides a single service, often called a micro-service, such as a web server or a database, though containers can be used for arbitrary workloads.

The Linux kernel has been incorporating capabilities for container technologies for years. The Docker project developed a convenient management interface for Linux containers on a host. More recently, the [Open Container Initiative](https://github.com/opencontainers/) has developed open standards for container formats and container runtimes. OpenShift Container Platform and Kubernetes add the ability to orchestrate OCI- and Docker-formatted containers across multi-host installations.

Though you do not directly interact with container runtimes when using OpenShift Container Platform, understanding their capabilities and terminology is important for understanding their role in OpenShift Container Platform and how your applications function inside of containers.

Tools such as [Podman](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux_atomic_host/7/html-single/managing_containers/#using_podman_to_work_with_containers) can be used to replace Docker command-line tools for running and managing containers directly. By using the `podman` CLI, you can experiment with containers separately from OpenShift Container Platform.

# Using image streams

Image streams provide an abstraction for referencing container images from within OpenShift Container Platform. You can use image streams to manage image versions and automate builds and deployments in your cluster.

Image streams do not contain actual image data, but present a single virtual view of related images, similar to an image repository.

You can configure builds and deployments to watch an image stream for notifications when new images are added and react by performing a build or deployment, respectively.

For example, if a deployment is using a certain image and a new version of that image is created, a deployment could be automatically performed to pick up the new version of the image.

However, if the image stream tag used by the deployment or build is not updated, then even if the container image in the container image registry is updated, the build or deployment continues using the previous, presumably known good image.

The source images can be stored in any of the following:

- OpenShift Container Platform’s integrated registry.

- An external registry, for example registry.redhat.io or quay.io.

- Other image streams in the OpenShift Container Platform cluster.

When you define an object that references an image stream tag, such as a build or deployment configuration, you point to an image stream tag and not the repository. When you build or deploy your application, OpenShift Container Platform queries the repository using the image stream tag to locate the associated ID of the image and uses that exact image.

The image stream metadata is stored in the etcd instance along with other cluster information.

Using image streams has several significant benefits:

- You can tag, rollback a tag, and quickly deal with images, without having to re-push using the command line.

- You can trigger builds and deployments when a new image is pushed to the registry. Also, OpenShift Container Platform has generic triggers for other resources, such as Kubernetes objects.

- You can mark a tag for periodic re-import. If the source image has changed, that change is picked up and reflected in the image stream, which triggers the build or deployment flow, depending upon the build or deployment configuration.

- You can share images using fine-grained access control and quickly distribute images across your teams.

- If the source image changes, the image stream tag still points to a known-good version of the image, ensuring that your application does not break unexpectedly.

- You can configure security around who can view and use the images through permissions on the image stream objects.

- Users that lack permission to read or list images on the cluster level can still retrieve the images tagged in a project using image streams.

# Additional resources

- [Managing image streams](image-streams-manage.md#managing-image-streams)

- [Using image streams with Kubernetes resources](using-imagestreams-with-kube-resources.md#using-imagestreams-with-kube-resources)

- [Triggering updates on image stream updates](triggering-updates-on-imagestream-changes.md#triggering-updates-on-imagestream-changes)

# Image stream tags

Image stream tags are named pointers to images in image streams in OpenShift Container Platform. You can configure image stream tags to reference specific versions of container images.

# Image stream images

Image stream images are API resource objects in OpenShift Container Platform that retrieve specific container images from image streams. You can use image stream images to access metadata about particular image SHA identifiers.

# Image stream triggers

Image stream triggers in OpenShift Container Platform cause specific actions when image stream tags change. You can configure triggers to automatically start builds or deployments when new images are imported.

For example, importing a new image can cause the value of the tag to change, which causes a trigger to fire when there are deployments, builds, or other resources listening for those.

# How you can use the Cluster Samples Operator

To manage sample image streams and templates in OpenShift Container Platform, you can use the Cluster Samples Operator. The Cluster Samples Operator creates default samples during initial startup to initiate image streams and templates in the `openshift` namespace.

# Additional resources

- [Configuring the Cluster Samples Operator](configuring-samples-operator.md#configuring-samples-operator)

- [Use the Operator with an alternate registry](samples-operator-alt-registry.md#samples-operator-alt-registry)

- [Understanding templates](../applications/creating_applications/using-templates.md#templates-overview)

- [Creating applications using Ruby on Rails](../applications/creating_applications/templates-using-ruby-on-rails.md#templates-using-ruby-on-rails)
