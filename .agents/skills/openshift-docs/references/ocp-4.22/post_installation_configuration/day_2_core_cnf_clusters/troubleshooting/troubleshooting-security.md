<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Implementing a robust cluster security profile is important for building resilient environments.

# Authentication

Determine which identity providers are in your cluster. For more information about supported identity providers, see "Supported identity providers" in *Authentication and authorization*.

After you know which providers are configured, you can inspect the `openshift-authentication` namespace to determine if there are potential issues.

<div>

<div class="title">

Procedure

</div>

1.  Check the events in the `openshift-authentication` namespace by running the following command:

    ``` terminal
    $ oc get events -n openshift-authentication --sort-by='.metadata.creationTimestamp'
    ```

2.  Check the pods in the `openshift-authentication` namespace by running the following command:

    ``` terminal
    $ oc get pod -n openshift-authentication
    ```

3.  Optional: If you need more information, check the logs of one of the running pods by running the following command:

    ``` terminal
    $ oc logs -n openshift-authentication <pod_name>
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Supported identity providers](../../../authentication/understanding-identity-provider.md#supported-identity-providers_understanding-identity-provider)

</div>
