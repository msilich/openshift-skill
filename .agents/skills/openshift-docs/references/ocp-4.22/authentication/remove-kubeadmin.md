<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

After installation, OpenShift Container Platform creates a cluster administrator user called `kubeadmin` with the `cluster-admin` role. To improve cluster security, you can remove this user after configuring an identity provider and creating a new `cluster-admin` user.

# The kubeadmin user

OpenShift Container Platform creates a cluster administrator, `kubeadmin`, after the installation process completes. This user has the `cluster-admin` role automatically applied and is treated as the root user for the cluster.

The password is dynamically generated and unique to your OpenShift Container Platform environment. After the installation completes, the password is provided in the installation program’s output. For example:

``` terminal
INFO Install complete!
INFO Run 'export KUBECONFIG=<your working directory>/auth/kubeconfig' to manage the cluster with 'oc', the OpenShift CLI.
INFO The cluster is ready when 'oc login -u kubeadmin -p <provided>' succeeds (wait a few minutes).
INFO Access the OpenShift web-console here: https://console-openshift-console.apps.demo1.openshift4-beta-abcorp.com
INFO Login to the console with user: kubeadmin, password: <provided>
```

# Removing the kubeadmin user

After you define an identity provider and create a new `cluster-admin` user, you can remove the `kubeadmin` to improve cluster security.

> [!WARNING]
> If you follow this procedure before another user is a `cluster-admin`, then OpenShift Container Platform must be reinstalled. It is not possible to undo this command.

<div>

<div class="title">

Prerequisites

</div>

- You must have configured at least one identity provider.

- You must have added the `cluster-admin` role to a user.

- You must be logged in as an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

- Remove the `kubeadmin` secrets:

  ``` terminal
  $ oc delete secrets kubeadmin -n kube-system
  ```

</div>
