<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure how the control plane handles concurrency when you create or migrate virtual machines (VMs). For example, set the `QPS` or `burst` rates to batch create virtual machines (VMs) in a batch, or tune migration settings in the `HyperConverged` custom resource (CR).

# Configuring a highBurst profile

You can use the `highBurst` profile to create and maintain a large number of virtual machines (VMs) in one cluster.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Apply the following patch to enable the `highBurst` tuning policy profile:

  ``` terminal
  $ oc patch hyperconverged kubevirt-hyperconverged -n openshift-cnv \
    --type=json -p='[{"op": "add", "path": "/spec/tuningPolicy", \
    "value": "highBurst"}]'
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Run the following command to verify the `highBurst` tuning policy profile is enabled:

  ``` terminal
  $ oc get kubevirt.kubevirt.io/kubevirt-kubevirt-hyperconverged \
    -n openshift-cnv -o go-template --template='{{range $config, \
    $value := .spec.configuration}} {{if eq $config "apiConfiguration" \
    "webhookConfiguration" "controllerConfiguration" "handlerConfiguration"}} \
    {{"\n"}} {{$config}} = {{$value}} {{end}} {{end}} {{"\n"}}
  ```

</div>
