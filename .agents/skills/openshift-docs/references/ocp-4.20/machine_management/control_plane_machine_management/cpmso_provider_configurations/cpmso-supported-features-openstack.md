<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can enable or change the configuration of features for your control plane machines by editing values in the control plane machine set specification.

When you save an update to the control plane machine set, the Control Plane Machine Set Operator updates the control plane machines according to your configured update strategy. For more information, see "Updating the control plane configuration".

# Changing the RHOSP compute flavor by using a control plane machine set

You can change the Red Hat OpenStack Platform (RHOSP) compute service (Nova) flavor that your control plane machines use by updating the specification in the control plane machine set custom resource.

In RHOSP, flavors define the compute, memory, and storage capacity of computing instances. By increasing or decreasing the flavor size, you can scale your control plane vertically.

<div>

<div class="title">

Prerequisites

</div>

- Your RHOSP cluster uses a control plane machine set.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the following line under the `providerSpec` field:

    ``` yaml
    providerSpec:
      value:
    # ...
        flavor: m1.xlarge
    ```

    - Specify a RHOSP flavor type that has the same base as the existing selection. For example, you can change `m6i.xlarge` to `m6i.2xlarge` or `m6i.4xlarge`. You can choose larger or smaller flavors depending on your vertical scaling needs.

2.  Save your changes.

</div>

After you save your changes, machines are replaced with ones that use the flavor you chose.

# Additional resources

- [Updating the control plane configuration](../cpmso-managing-machines.md#cpmso-feat-config-update_cpmso-managing-machines)

- [Control plane configuration options for {rh-openstack-full}](cpmso-config-options-openstack.md#cpmso-config-options-openstack)
