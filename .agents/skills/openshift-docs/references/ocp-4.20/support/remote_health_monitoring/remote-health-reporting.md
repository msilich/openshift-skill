<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can *opt in*, enable, or *opt out*, disable, reporting health and usage data for your cluster.

# Enabling remote health reporting

If you or your organization have disabled remote health reporting, you can enable this feature again. You can see that remote health reporting is disabled from the message `Insights not available` in the **Status** tile on the OpenShift Container Platform web console **Overview** page.

To enable remote health reporting, you must change the global cluster pull secret with a new authorization token. Enabling remote health reporting enables both Insights Operator and Telemetry.

# Changing your global cluster pull secret to enable remote health reporting

You can change your existing global cluster pull secret to enable remote health reporting. If you have disabled remote health monitoring, you must download a new pull secret with your `console.openshift.com` access token from Red Hat OpenShift Cluster Manager.

<div>

<div class="title">

Prerequisites

</div>

- Access to the cluster as a user with the `cluster-admin` role.

- Access to OpenShift Cluster Manager.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [Downloads](https://console.redhat.com/openshift/downloads) page on the Red Hat Hybrid Cloud Console.

2.  From **Tokens** → **Pull secret**, click the **Download** button.

    The `pull-secret` file contains your `cloud.openshift.com` access token in JSON format:

    ``` json
    {
      "auths": {
        "cloud.openshift.com": {
          "auth": "<your_token>",
          "email": "<email_address>"
        }
      }
    }
    ```

3.  Download the global cluster pull secret to your local file system.

    ``` terminal
    $ oc get secret/pull-secret -n openshift-config \
      --template='{{index .data ".dockerconfigjson" | base64decode}}' \
      > pull-secret
    ```

4.  Make a backup copy of your pull secret.

    ``` terminal
    $ cp pull-secret pull-secret-backup
    ```

5.  Open the `pull-secret` file in a text editor.

6.  Append the `cloud.openshift.com` JSON entry from the `pull-secret` file that you downloaded earlier into the `auths` file.

7.  Save the file.

8.  Update the secret in your cluster by running the following command:

    ``` terminal
    $ oc set data secret/pull-secret -n openshift-config \
      --from-file=.dockerconfigjson=pull-secret
    ```

    You might need to wait several minutes for the secret to update and your cluster to begin reporting.

</div>

<div>

<div class="title">

Verification

</div>

1.  For a verification check from the OpenShift Container Platform web console, complete the following steps:

    1.  Go to the **Overview** page on the OpenShift Container Platform web console.

    2.  View the **Red Hat Lightspeed** section in the **Status** tile that reports the number of issues found.

2.  For a verification check from the OpenShift CLI (`oc`), enter the following command and then check that the value of the `status` parameter states `false`:

    ``` terminal
    $ oc get co insights -o jsonpath='{.status.conditions[?(@.type=="Disabled")]}'
    ```

</div>

# Consequences of disabling remote health reporting

You can disable reporting usage information, but understand potential consequences before doing so.

Before you disable remote health reporting, read the following benefits of a connected cluster:

- Red Hat can react more quickly to problems and better support our customers.

- Red Hat can better understand how product upgrades impact clusters.

- Connected clusters help to simplify the subscription and entitlement process.

- Connected clusters enable the OpenShift Cluster Manager service to offer an overview of your clusters and their subscription status.

> [!NOTE]
> Consider leaving health and usage reporting enabled for pre-production, test, and production clusters. This means that Red Hat can participate in qualifying OpenShift Container Platform in your environments and react more rapidly to product issues.

The following lists some consequences of disabling remote health reporting on a connected cluster:

- Red Hat cannot view the success of product upgrades or the health of your clusters without an open support case.

- Red Hat cannot use configuration data to better triage customer support cases and identify which configurations our customers find important.

- The OpenShift Cluster Manager cannot show data about your clusters, which includes health and usage information.

- You must manually enter your subscription information in the `console.redhat.com` web console without the benefit of automatic usage reporting.

In restricted networks, Telemetry and Red Hat Lightspeed data still gets gathered through the appropriate configuration of your proxy.

# Disabling remote health reporting

You can change your existing global cluster pull secret to disable remote health reporting. This configuration disables both Telemetry and the Insights Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the global cluster pull secret to your local file system:

    ``` terminal
    $ oc extract secret/pull-secret -n openshift-config --to=.
    ```

2.  In a text editor, edit the `.dockerconfigjson` file that you downloaded by removing the `cloud.openshift.com` JSON entry:

    ``` json
    "cloud.openshift.com":{"auth":"<hash>","email":"<email_address>"}
    ```

3.  Save the file.

4.  Update the secret in your cluster. For more information, see "Updating the global cluster pull secret".

    You might need to wait several minutes for the secret to update in your cluster.

</div>

# Registering your disconnected cluster

Register your disconnected OpenShift Container Platform cluster on the Red Hat Hybrid Cloud Console so that your cluster does not get impacted by disabling remote health reporting. For more information, see "Consequences of disabling remote health reporting".

> [!IMPORTANT]
> By registering your disconnected cluster, you can continue to report your subscription usage to Red Hat. Red Hat can then return accurate usage and capacity trends associated with your subscription, so that you can use the returned information to better organize subscription allocations across all of your resources.

<div>

<div class="title">

Prerequisites

</div>

- You logged in to the OpenShift Container Platform web console as the `cluster-admin` role.

- You can log in to the Red Hat Hybrid Cloud Console.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Go to the [**Register disconnected cluster**](https://console.redhat.com/openshift/register) web page on the Red Hat Hybrid Cloud Console.

2.  Optional: To access the **Register disconnected cluster** web page from the home page of the Red Hat Hybrid Cloud Console, go to the **Cluster List** navigation menu item and then select the **Register cluster** button.

3.  Enter your cluster’s details in the provided fields on the **Register disconnected cluster** page.

4.  From the **Subscription settings** section of the page, select the subscription settings that apply to your Red Hat subscription offering.

5.  To register your disconnected cluster, select the **Register cluster** button.

</div>

<div>

<div class="title">

Additional resources

</div>

- [How does the subscriptions service show my subscription data?(Getting Started with the Subscription Service)](https://access.redhat.com/documentation/en-us/subscription_central/2023/html/getting_started_with_the_subscriptions_service/con-how-does-subscriptionwatch-show-data_assembly-viewing-understanding-subscriptionwatch-data-ctxt)

</div>

# Updating the global cluster pull secret

To add new registries or change authentication for your OpenShift Container Platform cluster, you can update the global pull secret by replacing it or appending new credentials. Use the `oc set data secret/pull-secret` command to apply the updated pull secret to all nodes in your cluster.

Use this procedure when you need a separate registry to store images than the registry used during installation.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Optional: To append a new pull secret to the existing pull secret:

    1.  Download the pull secret by entering the following command:

        ``` terminal
        $ oc get secret/pull-secret -n openshift-config --template='{{index .data ".dockerconfigjson" | base64decode}}' > <pull_secret_location>
        ```

        where:

        `<pull_secret_location>`
        Specifies the path to the pull secret file.

    2.  Add the new pull secret by entering the following command:

        ``` terminal
        $ oc registry login --registry="<registry>" \
        --auth-basic="<username>:<password>" \
        --to=<pull_secret_location>
        ```

        where:

        `<registry>`
        Specifies the new registry. You can include many repositories within the same registry, for example: `--registry="<registry/my-namespace/my-repository>`.

        `<username>:<password>`
        Specifies the credentials of the new registry.

        `<pull_secret_location>`
        Specifies the path to the pull secret file.

2.  Update the global pull secret for your cluster by entering the following command. Note that this update rolls out to all nodes, which can take some time depending on the size of your cluster.

    ``` terminal
    $ oc set data secret/pull-secret -n openshift-config \
      --from-file=.dockerconfigjson=<pull_secret_location>
    ```

    where:

    `<pull_secret_location>`
    Specifies the path to the new pull secret file.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Transferring cluster ownership](https://docs.redhat.com/en/documentation/openshift_cluster_manager/1-latest/html-single/managing_clusters/index#transferring-cluster-ownership_downloading-and-updating-pull-secrets)

</div>
