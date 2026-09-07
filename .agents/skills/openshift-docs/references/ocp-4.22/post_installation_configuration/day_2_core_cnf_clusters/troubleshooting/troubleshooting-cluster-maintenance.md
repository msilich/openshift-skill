<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When deploying OpenShift Container Platform on bare-metal infrastructure, you must pay more attention to certain configurations which can have a significant impact on cluster stability. You can troubleshoot more effectively by completing these tasks:

- Monitor for failed or failing hardware components

- Periodically check the status of the cluster Operators

> [!NOTE]
> For hardware monitoring, contact your hardware vendor to find the appropriate logging tool for your specific hardware.

# Checking cluster Operators

Periodically check the status of your cluster Operators to find issues early.

<div>

<div class="title">

Procedure

</div>

- Check the status of the cluster Operators by running the following command:

  ``` terminal
  $ oc get co
  ```

</div>

# Watching for failed pods

To reduce troubleshooting time, regularly monitor for failed pods in your cluster.

<div>

<div class="title">

Procedure

</div>

- To watch for failed pods, run the following command:

  ``` terminal
  $ oc get po -A | grep -Eiv 'complete|running'
  ```

</div>
