<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As a cluster administrator, you can list the names of any existing egress firewalls and view the traffic rules for a specific egress firewall.

# Viewing an EgressFirewall custom resource (CR)

You can view an `EgressFirewall` CR in your cluster.

<div>

<div class="title">

Prerequisites

</div>

- A cluster using the OVN-Kubernetes network plugin.

- Install the OpenShift Command-line Interface (CLI), commonly known as `oc`.

- You must log in to the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: To view the names of the `EgressFirewall` CR defined in your cluster, enter the following command:

    ``` terminal
    $ oc get egressfirewall --all-namespaces
    ```

2.  To inspect a policy, enter the following command. Replace `<policy_name>` with the name of the policy to inspect.

    ``` terminal
    $ oc describe egressfirewall <policy_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:        default
    Namespace:  project1
    Created:    20 minutes ago
    Labels:     <none>
    Annotations:    <none>
    Rule:       Allow to 1.2.3.0/24
    Rule:       Allow to www.example.com
    Rule:       Deny to 0.0.0.0/0
    ```

    </div>

</div>
