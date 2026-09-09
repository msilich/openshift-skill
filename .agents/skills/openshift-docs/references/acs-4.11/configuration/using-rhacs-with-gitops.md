<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure key RHACS attributes by using GitOps workflows by storing the values as code and applying them to RHACS declaratively.

<a id="using-rhacs-with-gitops-overview_using-rhacs-with-gitops"></a>

# GitOps configuration mechanisms

RHACS provides two mechanisms to configure attributes by using GitOps workflows: declarative configuration and policy as code.

RHACS provides the following two different mechanisms to control two different sets of attributes:

- *Declarative configuration* is a lightweight mechanism that uses config maps and secrets to configure mostly authentication and authorization resources.

- *Policy as code* leverages an RHACS-provided custom resource (CR), along with its controller, to manage RHACS policies.

<a id="config-using-declarative-config_using-rhacs-with-gitops"></a>

# Configuration by using declarative configuration

You can configure the following resources by using the RHACS declarative configuration method:

- Authentication providers

- Roles

- Permission sets

- Notifiers

- Access scopes

- Short-lived tokens

To configure these resources, you create YAML files that contain configuration information. You use these files to create a ConfigMap or Secret that you add to RHACS by using a mount point during installation of the RHACS Central resource.

<a id="config-using-policy-as-code_using-rhacs-with-gitops"></a>

# Configuration by using policy as code

You can create and manage policies as code by authoring policies as Kubernetes custom resources (CRs), and then applying them to the RHACS Central namespace by using a GitOps tool such as OpenShift GitOps, which builds on ArgoCD.

<div>

<div class="title">

Additional resources

</div>

- [Using declarative configuration](declarative-configuration-using.md)

- [Managing policies as code](../operating/manage_security_policies/custom-security-policies.md)

</div>
