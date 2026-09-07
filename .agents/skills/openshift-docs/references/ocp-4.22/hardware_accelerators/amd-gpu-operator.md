<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

AMD Instinct GPU accelerators combined with the AMD GPU Operator within your OpenShift Container Platform cluster lets you seamlessly harness computing capabilities for machine learning, Generative AI, and GPU-accelerated applications.

This documentation provides the information you need to enable, configure, and test the AMD GPU Operator. For more information, see [AMD Instinct™ Accelerators](https://www.amd.com/en/products/accelerators/instinct.html).

# About the AMD GPU Operator

The hardware acceleration capabilities of the AMD GPU Operator provide enhanced performance and cost efficiency for data scientists and developers using Red Hat OpenShift AI for creating artificial intelligence and machine learning (AI/ML) applications. Accelerating specific areas of GPU functions can minimize CPU processing and memory usage, improving overall application speed, memory consumption, and bandwidth restrictions.

# Installing the AMD GPU Operator

As a cluster administrator, you can install the AMD GPU Operator by using the OpenShift CLI and the web console. This is a multi-step procedure that requires the installation of the Node Feature Discovery Operator, the Kernel Module Management Operator, and then the AMD GPU Operator. Use the following steps in succession to install the AMD community release of the Operator.

<div>

<div class="title">

Next steps

</div>

1.  Install the [Node Feature Discovery Operator](../hardware_enablement/psap-node-feature-discovery-operator.md#installing-the-node-feature-discovery-operator_node-feature-discovery-operator).

2.  Install the [Kernel Module Management Operator](../hardware_enablement/kmm-kernel-module-management.md#kmm-install_kernel-module-management-operator).

3.  Install and configure the [AMD GPU Operator](https://instinct.docs.amd.com/projects/gpu-operator/en/main/installation/openshift-olm.html#install-amd-gpu-operator).

</div>

# Testing the AMD GPU Operator

Use the following procedure to test the ROCmInfo installation and view the logs for the AMD MI210 GPU.

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file that tests ROCmInfo:

    ``` terminal
    $ cat << EOF > rocminfo.yaml

    apiVersion: v1
    kind: Pod
    metadata:
     name: rocminfo
    spec:
     containers:
     - image: docker.io/rocm/pytorch:latest
       name: rocminfo
       command: ["/bin/sh","-c"]
       args: ["rocminfo"]
       resources:
        limits:
          amd.com/gpu: 1
        requests:
          amd.com/gpu: 1
     restartPolicy: Never
    EOF
    ```

2.  Create the `rocminfo` pod:

    ``` terminal
    $ oc create -f rocminfo.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    apiVersion: v1
    pod/rocminfo created
    ```

    </div>

3.  Check the `rocmnfo` log with one MI210 GPU:

    ``` terminal
    $ oc logs rocminfo | grep -A5 "Agent"
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    HSA Agents
    ==========
    *******
    Agent 1
    *******
      Name:                    Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
      Uuid:                    CPU-XX
      Marketing Name:          Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
      Vendor Name:             CPU
    --
    Agent 2
    *******
      Name:                    Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
      Uuid:                    CPU-XX
      Marketing Name:          Intel(R) Xeon(R) Gold 6330 CPU @ 2.00GHz
      Vendor Name:             CPU
    --
    Agent 3
    *******
      Name:                    gfx90a
      Uuid:                    GPU-024b776f768a638b
      Marketing Name:          AMD Instinct MI210
      Vendor Name:             AMD
    ```

    </div>

4.  Delete the pod:

    ``` terminal
    $ oc delete -f rocminfo.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    pod "rocminfo" deleted
    ```

    </div>

</div>
