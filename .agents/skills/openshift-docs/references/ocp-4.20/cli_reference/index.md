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

- [OpenShift CLI (`oc`)](openshift_cli/getting-started-cli.md#cli-getting-started): This is the most commonly used CLI tool by OpenShift Container Platform users. It helps both cluster administrators and developers to perform end-to-end operations across OpenShift Container Platform using the terminal. Unlike the web console, it allows the user to work directly with the project source code using command scripts.

- Kubernetes CLI (`kubectl`): OpenShift Container Platform is conformant with Cloud Native Computing Foundation (CNCF) Kubernetes and fully supports `kubectl` as a client. The OpenShift CLI (`oc`) is a superset of `kubectl`, where both CLI tools are included in the OpenShift Container Platform clients download. You can use the standard `kubectl` commands against OpenShift Container Platform clusters without any compatibility issues.

- [Knative CLI (kn)](kn-cli-tools.md#kn-cli-tools): The Knative (`kn`) CLI tool provides simple and intuitive terminal commands that can be used to interact with OpenShift Serverless components, such as Knative Serving and Eventing.

- [Pipelines CLI (tkn)](tkn_cli/installing-tkn.md#installing-tkn): OpenShift Pipelines is a continuous integration and continuous delivery (CI/CD) solution in OpenShift Container Platform, which internally uses Tekton. The `tkn` CLI tool provides simple and intuitive commands to interact with OpenShift Pipelines using the terminal.

- [opm CLI](opm/cli-opm-install.md#cli-opm-install): The `opm` CLI tool helps the Operator developers and cluster administrators to create and maintain the catalogs of Operators from the terminal.
