<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Securing a containerized application relies on multiple levels of security:

- Container security begins with a trusted base container image and continues through the container build process as it moves through your CI/CD pipeline.

  > [!IMPORTANT]
  > Image streams by default do not automatically update. This default behavior might create a security issue because security updates to images referenced by an image stream do not automatically occur. For information about how to override this default behavior, see [Configuring periodic importing of imagestreamtags](../../openshift_images/image-streams-manage.md#images-imagestreams-import_image-streams-managing).

- When a container is deployed, its security depends on it running on secure operating systems and networks, and establishing firm boundaries between the container itself and the users and hosts that interact with it.

- Continued security relies on being able to scan container images for vulnerabilities and having an efficient way to correct and replace vulnerable images.

Beyond what a platform such as OpenShift Container Platform offers out of the box, your organization will likely have its own security demands. Some level of compliance verification might be needed before you can even bring OpenShift Container Platform into your data center.

Likewise, you may need to add your own agents, specialized hardware drivers, or encryption features to OpenShift Container Platform, before it can meet your organization’s security standards.

This guide provides a high-level walkthrough of the container security measures available in OpenShift Container Platform, including solutions for the host layer, the container and orchestration layer, and the build and application layer. It then points you to specific OpenShift Container Platform documentation to help you achieve those security measures.

This guide contains the following information:

- Why container security is important and how it compares with existing security standards.

- Which container security measures are provided by the host (RHCOS and RHEL) layer and which are provided by OpenShift Container Platform.

- How to evaluate your container content and sources for vulnerabilities.

- How to design your build and deployment process to proactively check container content.

- How to control access to containers through authentication and authorization.

- How networking and attached storage are secured in OpenShift Container Platform.

- Containerized solutions for API management and SSO.

The goal of this guide is to understand the incredible security benefits of using OpenShift Container Platform for your containerized workloads and how the entire Red Hat ecosystem plays a part in making and keeping containers secure. It will also help you understand how you can engage with the OpenShift Container Platform to achieve your organization’s security goals.

# What are containers?

Containers package an application and all its dependencies into a single image that can be promoted from development, to test, to production, without change. A container might be part of a larger application that works closely with other containers.

Containers provide consistency across environments and multiple deployment targets: physical servers, virtual machines (VMs), and private or public cloud.

Some of the benefits of using containers include:

| Infrastructure | Applications |
|----|----|
| Sandboxed application processes on a shared Linux operating system kernel | Package my application and all of its dependencies |
| Simpler, lighter, and denser than virtual machines | Deploy to any environment in seconds and enable CI/CD |
| Portable across different environments | Easily access and share containerized components |

See [Understanding Linux containers](https://www.redhat.com/en/topics/containers) from the Red Hat Customer Portal to find out more about Linux containers. To learn about RHEL container tools, see [Building, running, and managing containers](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html-single/building_running_and_managing_containers/index) in the RHEL product documentation.

# What is OpenShift Container Platform?

Automating how containerized applications are deployed, run, and managed is the job of a platform such as OpenShift Container Platform. At its core, OpenShift Container Platform relies on the Kubernetes project to provide the engine for orchestrating containers across many nodes in scalable data centers.

Kubernetes is a project, which can run using different operating systems and add-on components that offer no guarantees of supportability from the project. As a result, the security of different Kubernetes platforms can vary.

OpenShift Container Platform is designed to lock down Kubernetes security and integrate the platform with a variety of extended components. To do this, OpenShift Container Platform draws on the extensive Red Hat ecosystem of open source technologies that include the operating systems, authentication, storage, networking, development tools, base container images, and many other components.

OpenShift Container Platform can leverage Red Hat’s experience in uncovering and rapidly deploying fixes for vulnerabilities in the platform itself as well as the containerized applications running on the platform. Red Hat’s experience also extends to efficiently integrating new components with OpenShift Container Platform as they become available and adapting technologies to individual customer needs.

<div>

<div class="title">

Additional resources

</div>

- [OpenShift Container Platform architecture](../../architecture/architecture.md#architecture)

- [OpenShift Security Guide](https://www.redhat.com/en/resources/openshift-security-guide-ebook)

</div>
