<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Note the following limitations when working with Windows nodes managed by the WMCO (Windows nodes):

- The following OpenShift Container Platform features are not supported on Windows nodes:

  - Image builds

  - OpenShift Pipelines

  - OpenShift Service Mesh

  - OpenShift monitoring of user-defined projects

  - OpenShift Serverless

  - Vertical Pod Autoscaling

  - Hosted Control Planes

- The following Red Hat features are not supported on Windows nodes:

  - [Red Hat Lightspeed cost management](https://docs.redhat.com/en/documentation/cost_management_service/1-latest)

  - [Red Hat OpenShift Local](https://developers.redhat.com/products/openshift-local/overview)

- Dual NIC is not supported on WMCO-managed Windows instances.

- Windows nodes do not support workloads created by using deployment configs. You can use a deployment or other method to deploy workloads.

- Red Hat OpenShift support for Windows Containers does not support adding Windows nodes to a cluster through a trunk port. The only supported networking configuration for adding Windows nodes is through an access port that carries traffic for the VLAN.

- Red Hat OpenShift support for Windows Containers does not support any Windows operating system language other than English (United States).

- Due to a limitation within the Windows operating system, `clusterNetwork` CIDR addresses of class E, such as `240.0.0.0`, are not compatible with Windows nodes.

- Kubernetes has identified the following [node feature limitations](https://kubernetes.io/docs/concepts/windows/intro/#limitations) :

  - Huge pages are not supported for Windows containers.

  - Privileged containers are not supported for Windows containers.

- Kubernetes has identified [several API compatibility issues](https://kubernetes.io/docs/concepts/windows/intro/#api).
