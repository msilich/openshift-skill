<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The first step in troubleshooting is to retrieve the logs and pods status. The logs allow you to identify the root cause of an error. In addition, examining the pod’s most recent status can give information about failure messages.

<a id="retrieving-the-collector-logs_logs-and-pod-status"></a>

# Retrieving the Collector logs

First, you should examine the logs from failing Collectors. Depending on your environment and access rights, you can obtain these logs in two ways:

- Retrieving the logs with the `oc` or `kubectl` command

- Retrieving logs from a RHACS diagnostic bundle

<div>

<div class="title">

Additional resources

</div>

- [Retrieving the logs with the `oc` or `kubectl` command](retrieving-and-analyzing-the-collector-logs-and-pod-status.md#retrieving-the-logs-with-the-oc-or-kubectl-command_logs-and-pod-status)

- [Retrieving logs from a RHACS diagnostic bundle](retrieving-and-analyzing-the-collector-logs-and-pod-status.md#retrieving-logs-from-a-rhacs-diagnostic-bundle_logs-and-pod-status)

</div>

<a id="retrieving-the-logs-with-the-oc-or-kubectl-command_logs-and-pod-status"></a>

## Retrieving the logs with the `oc` or `kubectl` command

You can use either the `oc` or `kubectl` command to obtain logs from your running Collector pod. Optionally, you can even check the logs from an earlier Collector pod if your current Collector pod is restarting.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Prerequisites

</div>

- Ensure that you have the authority to list the pods and logs:

  ``` terminal
  $ oc auth can-i get pods && oc auth can-i get pods --subresource=logs
  ```

</div>

<div>

<div class="title">

Procedure

</div>

1.  List all the pods with label `app=collector`:

    ``` terminal
    $ oc get pods -n stackrox -l app=collector
    ```

    The following is an example output:

    ``` terminal
    collector-vclg5    1/2     CrashLoopBackOff   2 (25s ago)   2m41s
    ```

2.  Get the logs for the Collector pod:

    ``` terminal
    $ oc logs -n stackrox <collector_pod_name> collector
    ```

    where:

    `<collector_pod_name>`  
    Specifies the name of your Collector pod, for example, `collector-vclg5`.

3.  (Optional) If the current Collector pod is restarting, you can check the logs for the earlier Collector pod:

    ``` terminal
    $ oc logs -n stackrox <collector_pod_name> collector --previous
    ```

    where:

    `<collector_pod_name>`  
    Specifies the name of your Collector pod, for example, `collector-vclg5`.

</div>

<a id="retrieving-logs-from-a-rhacs-diagnostic-bundle_logs-and-pod-status"></a>

## Retrieving logs from a RHACS diagnostic bundle

You can access Collector logs by downloading a diagnostic bundle from the Red Hat Advanced Cluster Security for Kubernetes (RHACS) user interface.

Once you have downloaded the diagnostic bundle, you can inspect the logs for all the Collector pods. For more information, see "Generating a diagnostic bundle".

<div>

<div class="title">

Additional resources

</div>

- [Generating a diagnostic bundle](../configuration/generate-diagnostic-bundle.md)

</div>

<a id="analyzing-the-collector-pod-status_logs-and-pod-status"></a>

# Analyzing the Collector pod status

Examining the pod’s most recent status is another easy way to find the cause of a Collector crash. The most recent status records failure messages, and you can access them by using the `kubectl describe pod` or `oc describe pod` command.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- Describe the Collector pod:

  ``` terminal
  $ oc describe pod -n stackrox <collector_pod_name>
  ```

  where:

  `<collector_pod_name>`  
  Specifies the name of your Collector pod, for example, `collector-vclg5`.

  The following is an example output:

  ``` text
  # ...
      Last State:     Terminated
        Reason:       Error
        Message:      No suitable kernel object downloaded
        Exit Code:    1
        Started:      Fri, 21 Oct 2022 11:50:56 +0100
        Finished:     Fri, 21 Oct 2022 11:51:25 +0100
  # ...
  ```

  In this example, you can see that Collector has failed to download a kernel driver.

</div>
