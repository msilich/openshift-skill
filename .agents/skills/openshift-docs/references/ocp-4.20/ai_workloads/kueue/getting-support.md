<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you experience difficulty with a procedure described in this documentation, or with Red Hat build of Kueue in general, visit the [Red Hat Customer Portal](http://access.redhat.com).

From the Customer Portal, you can:

- Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

# About the Red Hat Knowledgebase

The [Red Hat Knowledgebase](https://access.redhat.com/knowledgebase) provides rich content aimed at helping you make the most of Red Hat’s products and technologies. The Red Hat Knowledgebase consists of articles, product documentation, and videos outlining best practices on installing, configuring, and using Red Hat products. In addition, you can search for solutions to known issues, each providing concise root cause descriptions and remedial steps.

# Collecting data for Red Hat Support

You can use the `oc adm must-gather` CLI command to collect the information about your Red Hat build of Kueue instance that is most likely needed for debugging issues, including:

- Red Hat build of Kueue custom resources, such as workloads, cluster queues, local queues, resource flavors, admission checks, and their corresponding cluster resource definitions (CRDs)

- Services

- Endpoints

- Webhook configurations

- Logs from the `openshift-kueue-operator` namespace and `kueue-controller-manager` pods

Collected data is written into a new directory named `must-gather/` in the current working directory by default.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat build of Kueue Operator is installed on your cluster.

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to the directory where you want to store the `must-gather` data.

2.  Collect `must-gather` data by running the following command:

    ``` terminal
    $ oc adm must-gather \
      --image=registry.redhat.io/kueue/kueue-must-gather-rhel9:<version>
    ```

    Where `<version>` is your current version of Red Hat build of Kueue.

3.  Create a compressed file from the `must-gather` directory that was just created in your working directory. Make sure you provide the date and cluster ID for the unique `must-gather` data. For more information about how to find the cluster ID, see [How to find the cluster-id or name on OpenShift cluster](https://access.redhat.com/solutions/5280291).

4.  Attach the compressed file to your support case on the [the **Customer Support** page](https://access.redhat.com/support/cases/#/case/list) of the Red Hat Customer Portal.

</div>

# Additional resources

- [Support overview](../../support/index.md#support-overview)
