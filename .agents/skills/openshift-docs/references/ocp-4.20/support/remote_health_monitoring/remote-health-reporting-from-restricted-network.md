<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can manually gather and upload Insights Operator archives to diagnose issues from a restricted network.

To use the Insights Operator in a restricted network, you must:

- Create a copy of your Insights Operator archive.

- Upload the Insights Operator archive to [console.redhat.com](https://console.redhat.com).

Additionally, you can select to obfuscate the Insights Operator data before data upload.

<div>

<div class="title">

Additional resources

</div>

- [Enabling Insights Operator data obfuscation](remote-health-reporting-from-restricted-network.md#insights-operator-enable-obfuscation_remote-health-reporting-from-restricted-network)

</div>

# Running an Insights Operator gather operation

You must run a gather operation to create an Insights Operator archive.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as `cluster-admin`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a file named `gather-job.yaml` using this template:

    ``` yaml
    link:https://raw.githubusercontent.com/openshift/insights-operator/release-4.20/docs/gather-job.yaml[role=include]
    ```

2.  Copy your `insights-operator` image version:

    ``` terminal
    $ oc get -n openshift-insights deployment insights-operator -o yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: apps/v1
    kind: Deployment
    metadata:
      name: insights-operator
      namespace: openshift-insights
    # ...
    spec:
      template:
    # ...
        spec:
          containers:
          - args:
    # ...
            image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
    # ...
    ```

    </div>

    The `spec.template.spec.containers.image` field specifies your insights-operator image version.

3.  Paste your image version in `gather-job.yaml`:

    ``` yaml
    apiVersion: batch/v1
    kind: Job
    metadata:
      name: insights-operator-job
    # ...
    spec:
    # ...
      template:
        spec:
        initContainers:
        - name: insights-operator
          image: image: registry.ci.openshift.org/ocp/4.15-2023-10-12-212500@sha256:a0aa581400805ad0...
          terminationMessagePolicy: FallbackToLogsOnError
          volumeMounts:
    ```

    Replace the value of `spec.template.initContainers.image` with your `insights-operator` image version.

4.  Create the gather job:

    ``` terminal
    $ oc apply -n openshift-insights -f gather-job.yaml
    ```

5.  Find the name of the job pod:

    ``` terminal
    $ oc describe -n openshift-insights job/insights-operator-job
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name:             insights-operator-job
    Namespace:        openshift-insights
    # ...
    Events:
      Type    Reason            Age    From            Message
      ----    ------            ----   ----            -------
      Normal  SuccessfulCreate  7m18s  job-controller  Created pod: insights-operator-job-<your_job>
    ```

    </div>

    Replace `insights-operator-job-<your_job>` with the name of the pod.

6.  Verify that the operation has finished:

    ``` terminal
    $ oc logs -n openshift-insights insights-operator-job-<your_job> insights-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    I0407 11:55:38.192084       1 diskrecorder.go:34] Wrote 108 records to disk in 33ms
    ```

    </div>

7.  Save the created archive:

    ``` terminal
    $ oc cp openshift-insights/insights-operator-job-<your_job>:/var/lib/insights-operator ./insights-data
    ```

8.  Clean up the job:

    ``` terminal
    $ oc delete -n openshift-insights job insights-operator-job
    ```

</div>

# Uploading an Insights Operator archive

You can manually upload an Insights Operator archive to [console.redhat.com](https://console.redhat.com) to diagnose potential issues.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to OpenShift Container Platform as `cluster-admin`.

- You have a workstation with unrestricted internet access.

- You have created a copy of the Insights Operator archive.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Download the `dockerconfig.json` file:

    ``` terminal
    $ oc extract secret/pull-secret -n openshift-config --to=.
    ```

2.  Copy your `"cloud.openshift.com"` `"auth"` token from the `dockerconfig.json` file:

    ``` json
    {
      "auths": {
        "cloud.openshift.com": {
          "auth": "<your_token>",
          "email": "asd@redhat.com"
        }
    }
    ```

3.  Upload the archive to [console.redhat.com](https://console.redhat.com):

    ``` terminal
    $ curl -v -H "User-Agent: insights-operator/one10time200gather184a34f6a168926d93c330 cluster/<cluster_id>" -H "Authorization: Bearer <your_token>" -F "upload=@<path_to_archive>; type=application/vnd.redhat.openshift.periodic+tar" https://console.redhat.com/api/ingress/v1/upload
    ```

    where:

    `<cluster_id>`
    Specifies the cluster ID.

    `<your_token>`
    Specifies the token from your pull secret.

    `<path_to_archive>`
    Specifies the path to the Insights Operator archive.

    If the operation is successful, the command returns a `"request_id"` and `"account_number"`:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    * Connection #0 to host console.redhat.com left intact
    {"request_id":"393a7cf1093e434ea8dd4ab3eb28884c","upload":{"account_number":"6274079"}}%
    ```

    </div>

</div>

<div>

<div class="title">

Verification

</div>

1.  Log in to <https://console.redhat.com/openshift>.

2.  Click the **Cluster List** menu in the left pane.

3.  To display the details of the cluster, click the cluster name.

4.  Open the **Red Hat Lightspeed Advisor** tab of the cluster.

    If the upload was successful, the tab displays one of the following:

    - **Your cluster passed all recommendations**, if the Red Hat Lightspeed advisor service did not identify any issues.

    - A list of issues that the Red Hat Lightspeed advisor service has detected, prioritized by risk (low, moderate, important, and critical).

</div>

# Enabling Insights Operator data obfuscation

You can enable obfuscation to mask sensitive and identifiable IPv4 addresses and cluster base domains that the Insights Operator sends to [console.redhat.com](https://console.redhat.com).

> [!WARNING]
> Although this feature is available, Red Hat recommends keeping obfuscation disabled for a more effective support experience.

Obfuscation assigns non-identifying values to cluster IPv4 addresses, and uses a translation table that is retained in memory to change IP addresses to their obfuscated versions throughout the Insights Operator archive before uploading the data to [console.redhat.com](https://console.redhat.com).

For cluster base domains, obfuscation changes the base domain to a hardcoded substring. For example, `cluster-api.openshift.example.com` becomes `cluster-api.<CLUSTER_BASE_DOMAIN>`.

The following procedure enables obfuscation using the `support` secret in the `openshift-config` namespace.

<div>

<div class="title">

Prerequisites

</div>

- You are logged in to the OpenShift Container Platform web console as `cluster-admin`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Navigate to **Workloads** → **Secrets**.

2.  Select the **openshift-config** project.

3.  Search for the **support** secret using the **Search by name** field. If it does not exist, click **Create** → **Key/value secret** to create it.

4.  Click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=), and then click **Edit Secret**.

5.  Click **Add Key/Value**.

6.  Create a key named `enableGlobalObfuscation` with a value of `true`, and click **Save**.

7.  Navigate to **Workloads** → **Pods**

8.  Select the `openshift-insights` project.

9.  Find the `insights-operator` pod.

10. To restart the `insights-operator` pod, click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=), and then click **Delete Pod**.

</div>

<div>

<div class="title">

Verification

</div>

1.  Navigate to **Workloads** → **Secrets**.

2.  Select the **openshift-insights** project.

3.  Search for the **obfuscation-translation-table** secret using the **Search by name** field.

    If the `obfuscation-translation-table` secret exists, then obfuscation is enabled and working.

    Alternatively, you can inspect `/insights-operator/gathers.json` in your Insights Operator archive for the value `"is_global_obfuscation_enabled": true`.

</div>

<div>

<div class="title">

Additional resources

</div>

- For more information on how to download your Insights Operator archive, see [Showing data collected by the Insights Operator](showing-data-collected-by-remote-health-monitoring.md#insights-operator-showing-data-collected-from-the-cluster_showing-data-collected-by-remote-health-monitoring).

</div>
