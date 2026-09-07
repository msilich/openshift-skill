<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform offers a set of command-line interface (CLI) tools that enable users to perform various administration and development operations from the terminal. These tools expose simple commands to manage the applications, as well as interact with each component of the system.

For example, you can use the CLI to complete the following operations:

- Manage clusters

- Build, deploy, and manage applications

- Manage deployment processes

- Create and maintain Operator catalogs

# List of CLI tools

Manage your OpenShift Container Platform cluster, applications, and Operators from the terminal by using primary command-line interface (CLI) tools.

The following list details these primary CLI tools:

- OpenShift CLI (`oc`): This is the most commonly used CLI tool by OpenShift Container Platform users. Cluster administrators and developers can use it to perform end-to-end operations across OpenShift Container Platform from the terminal, including working directly with project source code using command scripts.

- Kubernetes CLI (`kubectl`): OpenShift Container Platform is conformant with Cloud Native Computing Foundation (CNCF) Kubernetes and fully supports `kubectl` as a client. The OpenShift CLI (`oc`) is a superset of `kubectl`, where both CLI tools are included in the OpenShift Container Platform clients download. You can use the standard `kubectl` commands against OpenShift Container Platform clusters without any compatibility issues.

- Helm CLI (`helm`): Helm is a package manager for Kubernetes. The `helm` CLI provides commands to install, upgrade, and manage Helm charts on a cluster.

- opm CLI: The `opm` CLI tool helps Operator developers and cluster administrators create and maintain catalogs of Operators.

- Knative CLI: The Knative (`kn`) CLI tool provides commands to interact with OpenShift Serverless components, such as Knative Serving and Eventing.

- Pipelines CLI (tkn): OpenShift Pipelines is a continuous integration and delivery (CI/CD) solution in OpenShift Container Platform, which internally uses Tekton. The `tkn` CLI tool provides commands to interact with OpenShift Pipelines.

## Additional resources

- [OpenShift Container Platform CLI (`oc`)](openshift_cli/getting-started-cli.md#cli-getting-started)

- [Helm CLI (`helm`)](../applications/working_with_helm_charts/installing-helm.md#installing-helm)

- [`opm` CLI](opm/cli-opm-install.md#cli-opm-install)

- [Knative CLI (`kn`)](kn-cli-tools.md#kn-cli-tools)

- [OpenShift Pipelines CLI (`tkn`)](tkn_cli/installing-tkn.md#installing-tkn)
