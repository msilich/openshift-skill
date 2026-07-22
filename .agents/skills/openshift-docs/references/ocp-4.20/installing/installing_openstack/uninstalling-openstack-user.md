<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can remove a cluster that you deployed to Red Hat OpenStack Platform (RHOSP) on user-provisioned infrastructure.

# Downloading playbook dependencies

The Ansible playbooks that simplify the removal process on user-provisioned infrastructure require several Python modules. On the machine where you will run the process, add the modules' repositories and then download them.

> [!NOTE]
> These instructions assume that you are using Red Hat Enterprise Linux (RHEL) 8.

<div>

<div class="title">

Prerequisites

</div>

- Python 3 is installed on your machine.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, add the repositories:

    1.  Register with Red Hat Subscription Manager:

        ``` terminal
        $ sudo subscription-manager register # If not done already
        ```

    2.  Pull the latest subscription data:

        ``` terminal
        $ sudo subscription-manager attach --pool=$YOUR_POOLID # If not done already
        ```

    3.  Disable the current repositories:

        ``` terminal
        $ sudo subscription-manager repos --disable=* # If not done already
        ```

    4.  Add the required repositories:

        ``` terminal
        $ sudo subscription-manager repos \
          --enable=rhel-9-for-x86_64-appstream-rpms \
          --enable=rhel-9-for-x86_64-baseos-rpms \
          --enable=openstack-17.1-for-rhel-9-x86_64-rpms
        ```

2.  Install the modules:

    ``` terminal
    $ sudo yum install python3-openstackclient ansible python3-openstacksdk
    ```

3.  Ensure that the `python` command points to `python3`:

    ``` terminal
    $ sudo alternatives --set python /usr/bin/python3
    ```

</div>

# Removing a cluster from RHOSP that uses your own infrastructure

You can remove an OpenShift Container Platform cluster on Red Hat OpenStack Platform (RHOSP) that uses your own infrastructure. To complete the removal process quickly, run several Ansible playbooks.

<div>

<div class="title">

Prerequisites

</div>

- Python 3 is installed on your machine.

- You downloaded the modules in "Downloading playbook dependencies."

- You have the playbooks that you used to install the cluster.

- You modified the playbooks that are prefixed with `down-` to reflect any changes that you made to their corresponding installation playbooks. For example, changes to the `bootstrap.yaml` file are reflected in the `down-bootstrap.yaml` file.

- All of the playbooks are in a common directory.

</div>

<div>

<div class="title">

Procedure

</div>

1.  On a command line, run the playbooks that you downloaded:

    ``` terminal
    $ ansible-playbook -i inventory.yaml  \
        down-bootstrap.yaml      \
        down-control-plane.yaml  \
        down-compute-nodes.yaml  \
        down-load-balancers.yaml \
        down-network.yaml        \
        down-security-groups.yaml
    ```

2.  Remove any DNS record changes you made for the OpenShift Container Platform installation.

</div>

OpenShift Container Platform is removed from your infrastructure.
