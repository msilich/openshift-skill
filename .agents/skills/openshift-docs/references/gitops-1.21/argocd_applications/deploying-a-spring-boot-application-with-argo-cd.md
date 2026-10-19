<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Argo CD, you can deploy your applications to the OpenShift Container Platform cluster either by using the Argo CD dashboard or by using the `oc` tool.

# Creating an application by using the Argo CD dashboard

Argo CD provides a dashboard which allows you to create applications.

<div>

<div class="title">

Prerequisites

</div>

- You have logged in to the OpenShift Container Platform cluster as an administrator.

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD dashboard, click **NEW APP** to add a new Argo CD application.

2.  For this workflow, create a **spring-petclinic** application with the following configurations:

    Application Name
    `spring-petclinic`

    Project
    `default`

    Sync Policy
    `Automatic`

    Repository URL
    `https://github.com/redhat-developer/openshift-gitops-getting-started`

    Revision
    `HEAD`

    Path
    `app`

    Destination
    `https://kubernetes.default.svc`

    Namespace
    `spring-petclinic`

    Auto Create Namespace
    `checked`

3.  Click **CREATE** to create your application.

    The `spring-petclinic` namespace is automatically created when you enable **Auto Create Namespace**.

    > [!IMPORTANT]
    > You must label the namespace manually.

4.  Open the **Administrator** perspective of the web console and expand **Administration** → **Namespaces**.

5.  Search for and select the `spring-petclinic` namespace, then enter `argocd.argoproj.io/managed-by=openshift-gitops` in the **Label** field so that the Argo CD instance in the `openshift-gitops` namespace can manage your namespace.

</div>

# Creating an application by using the `oc` tool

You can create Argo CD applications in your terminal by using the `oc` tool.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

- You have access to the `oc` CLI tool.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download [the sample application](https://github.com/redhat-developer/openshift-gitops-getting-started):

    ``` terminal
    $ git clone git@github.com:redhat-developer/openshift-gitops-getting-started.git
    ```

2.  Create and configure the destination namespace:

    ``` terminal
    $ oc create namespace spring-petclinic
    ```

    ``` terminal
    $ oc label namespace spring-petclinic argocd.argoproj.io/managed-by=openshift-gitops
    ```

3.  Create the application:

    ``` terminal
    $ oc create -f openshift-gitops-getting-started/argo/app.yaml
    ```

4.  Run the `oc get` command to review the created application:

    ``` terminal
    $ oc get application -n openshift-gitops
    ```

</div>

<div class="formalpara">

<div class="title">

Cleanup (optional)

</div>

To delete the application and namespace after you are done:

</div>

1.  Delete the application:

    ``` terminal
    $ oc delete -n openshift-gitops -f openshift-gitops-getting-started/argo/app.yaml
    ```

2.  Delete the namespace:

    ``` terminal
    $ oc delete namespace spring-petclinic
    ```

# Verifying Argo CD self-healing behavior

Argo CD constantly monitors the state of deployed applications, detects differences between the specified manifests in Git and live changes in the cluster, and then automatically corrects them. This behavior is referred to as self-healing.

You can test and observe the self-healing behavior in Argo CD.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the Red Hat OpenShift GitOps Operator on your OpenShift Container Platform cluster.

- You have logged in to an Argo CD instance.

- The sample `spring-petclinic` application is deployed and configured.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the Argo CD dashboard, verify that your application has the `Synced` status.

2.  Click the `spring-petclinic` tile in the Argo CD dashboard to view the application resources that are deployed to the cluster.

3.  In the OpenShift Container Platform web console, navigate to the **Developer** perspective.

4.  Fork the [OpenShift GitOps getting started repository](https://github.com/redhat-developer/openshift-gitops-getting-started).

    1.  Modify the Spring PetClinic deployment and commit the changes to the `app/` directory of the Git repository. Argo CD will automatically deploy the changes to the cluster.

    2.  In the `deployment.yaml` file, change the `failureThreshold` value to `5`.

    3.  Commit and push the changes.

    4.  In the OpenShift Container Platform cluster, run the following command to verify the changed value of the `failureThreshold` field:

        ``` terminal
        $ oc edit deployment spring-petclinic -n spring-petclinic
        ```

5.  Test the self-healing behavior by scaling the deployment up to two pods and observing Argo CD automatically scale it back down.

    1.  Run the following command to modify the deployment:

        ``` terminal
        $ oc scale deployment spring-petclinic --replicas 2  -n spring-petclinic
        ```

    2.  In the OpenShift Container Platform web console, notice that the deployment scales up to two pods and immediately scales down again to one pod. Argo CD detected a difference from the Git repository and auto-healed the application on the OpenShift Container Platform cluster.

6.  In the Argo CD dashboard, click the **spring-petclinic** tile → **APP DETAILS** → **EVENTS**. The **EVENTS** tab displays the following events: Argo CD detecting out of sync deployment resources on the cluster and then resyncing the Git repository to correct it.

</div>
