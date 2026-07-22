<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can apply global configuration options in OpenShift Container Platform. Operators apply these configuration settings across the cluster.

# Interacting with your cluster resources

You can interact with cluster resources by using the OpenShift CLI (`oc`) tool in OpenShift Container Platform. The cluster resources that you see after running the `oc api-resources` command can be edited.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to the web console or you have installed the `oc` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To see which configuration Operators have been applied, run the following command:

    ``` terminal
    $ oc api-resources -o name | grep config.openshift.io
    ```

2.  To see what cluster resources you can configure, run the following command:

    ``` terminal
    $ oc explain <resource_name>.config.openshift.io
    ```

3.  To see the configuration of custom resource definition (CRD) objects in the cluster, run the following command:

    ``` terminal
    $ oc get <resource_name>.config -o yaml
    ```

4.  To edit the cluster resource configuration, run the following command:

    ``` terminal
    $ oc edit <resource_name>.config -o yaml
    ```

</div>
