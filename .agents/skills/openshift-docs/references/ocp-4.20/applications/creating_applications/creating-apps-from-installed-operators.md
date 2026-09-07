<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can deploy applications on your OpenShift Container Platform cluster from Operators that a cluster administrator installed. Use the **Installed Operators** page in the web console to create an application from an Operator custom resource (CR) API.

<div>

<div class="title">

Additional resources

</div>

- [What are Operators?](../../operators/understanding/olm-what-operators-are.md#olm-what-operators-are)

</div>

# Creating an etcd cluster using an Operator

You can create an etcd cluster using the etcd Operator in the OpenShift Container Platform web console. The Operator creates the pods, services, and other cluster resources for you.

<div>

<div class="title">

Prerequisites

</div>

- Access to an OpenShift Container Platform 4.20 cluster.

- The etcd Operator already installed cluster-wide by an administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new project in the OpenShift Container Platform web console for this procedure. This example uses a project called `my-etcd`.

2.  Navigate to the **Ecosystem** → **Installed Operators** page.

    The Operators installed on the cluster by the cluster administrator and available for use are shown here as a list of cluster service versions (CSVs). Each CSV launches and manages the software provided by the Operator.

    > [!TIP]
    > You can get this list from the CLI by running the following command:
    >
    > ``` terminal
    > $ oc get csv
    > ```

3.  On the **Installed Operators** page, click the etcd Operator to view more details and available actions.

    As shown under **Provided APIs**, this Operator makes available three new resource types, including one for an **etcd Cluster**, the `EtcdCluster` resource.

    These objects work similarly to the built-in native Kubernetes ones, such as `Deployment` or `ReplicaSet`, but contain logic specific to managing etcd.

4.  Create a new etcd cluster:

    1.  In the **etcd Cluster** API box, click **Create instance**.

    2.  Optional: Modify the minimal starting template of an `EtcdCluster` object, such as the size of the cluster.

    3.  Click **Create** to finalize. This triggers the Operator to start up the pods, services, and other components of the new etcd cluster.

5.  Click the **example** etcd cluster.

6.  Click the **Resources** tab.

    Your project contains several resources that the Operator created and configured.

7.  Verify that a Kubernetes service exists that allows you to access the database from other pods in your project.

8.  Optional: To grant another user permission to create Operator-managed applications in the project, add the `edit` role by running the following command:

    ``` terminal
    $ oc policy add-role-to-user edit <user> -n <target_project>
    ```

    Users with the `edit` role in a project can create, manage, and delete Operator-managed application instances, such as an etcd cluster.

</div>

<div class="formalpara">

<div class="title">

Results

</div>

You have an etcd cluster that reacts to failures and rebalances data as pods become unhealthy or migrate between nodes in the cluster. Cluster administrators or developers with proper access can use the database with their applications.

</div>
