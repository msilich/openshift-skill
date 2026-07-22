<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Helm is a software package manager that simplifies deployment of applications and services to OpenShift Container Platform clusters.

Helm uses a packaging format called *charts*. A Helm chart is a collection of files that describes the OpenShift Container Platform resources.

Creating a chart in a cluster creates a running instance of the chart known as a *release*.

Each time a chart is created, or a release is upgraded or rolled back, an incremental revision is created.

# Key features

Helm provides the ability to:

- Search through a large collection of charts stored in the chart repository.

- Modify existing charts.

- Create your own charts with OpenShift Container Platform or Kubernetes resources.

- Package and share your applications as charts.

# Red Hat Certification of Helm charts for OpenShift

You can choose to verify and certify your Helm charts by Red Hat for all the components you will be deploying on the Red Hat OpenShift Container Platform. Charts go through an automated Red Hat OpenShift certification workflow that guarantees security compliance as well as best integration and experience with the platform. Certification assures the integrity of the chart and ensures that the Helm chart works seamlessly on Red Hat OpenShift clusters.

# Additional resources

- For more information on how to certify your Helm charts as a Red Hat partner, see [Red Hat Certification of Helm charts for OpenShift](https://redhat-connect.gitbook.io/partner-guide-for-red-hat-openshift-and-container/helm-chart-certification/overview).

- For more information on OpenShift and Container certification guides for Red Hat partners, see [Partner Guide for OpenShift and Container Certification](https://access.redhat.com/documentation/en-us/red_hat_software_certification/8.51/html-single/red_hat_software_certification_workflow_guide/index#con_container-certification_openshift-sw-cert-workflow-introduction-to-redhat-openshift-operator-certification).

- For a list of the charts, see [the Red Hat `Helm index` file](https://charts.openshift.io/index.yaml).
