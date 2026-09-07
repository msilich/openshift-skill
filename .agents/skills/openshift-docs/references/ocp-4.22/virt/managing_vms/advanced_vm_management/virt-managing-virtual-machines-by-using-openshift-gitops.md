<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To automate and optimize virtual machine (VM) management in {VirtProductName}, you can use Red Hat OpenShift GitOps.

With GitOps, you can set up VM deployments based on configuration files stored in a Git repository. This also makes it easier to automate, update, or replicate these configurations, as well to use version control for tracking their changes.

<div>

<div class="title">

Prerequisites

</div>

- You have a GitHub account. For instructions to set up an account, see [Creating an account on GitHub](https://docs.github.com/en/get-started/start-your-journey/creating-an-account-on-github).

- OpenShift Virtualuzation has been installed on your OpenShift cluster. For instructions, see [OpenShift Virtualization installation](../../install/installing-virt.md#installing-virt).

- The OpenShift GitOps operator has been installed on your OpenShift cluster. For instructions, see [Installing GitOps](https://docs.openshift.com/gitops/1.15/installing_gitops/preparing-gitops-install.html).

</div>

<div class="formalpara">

<div class="title">

Procedure

</div>

Follow [the *Manage OpenShift virtual machines with GitOps* learning path](https://developers.redhat.com/learning/learn:manage-openshift-virtual-machines-gitops/resource/resources:connect-and-configure-external-repository-argo-cd-virtual-machines) in performing these steps:

</div>

1.  Connect an external Git repository to your Argo CD instance.

2.  Create the required VM configuration in the Git repository.

3.  Use the VM configuration to create VMs on your cluster.

<div>

<div class="title">

Additional resources

</div>

- [OpenShift GitOps documentation](https://docs.openshift.com/gitops/)

</div>
