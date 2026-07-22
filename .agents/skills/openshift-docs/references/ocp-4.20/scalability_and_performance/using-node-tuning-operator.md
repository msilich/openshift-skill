<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn about the Node Tuning Operator and how you can use it to manage node-level tuning by orchestrating the tuned daemon.

# About the Node Tuning Operator

The Node Tuning Operator helps you manage node-level tuning by orchestrating the TuneD daemon and achieves low latency performance by using the Performance Profile controller. The majority of high-performance applications require some level of kernel tuning. The Node Tuning Operator provides a unified management interface to users of node-level sysctls and more flexibility to add custom tuning specified by user needs.

The Operator manages the containerized TuneD daemon for OpenShift Container Platform as a Kubernetes daemon set. It ensures the custom tuning specification is passed to all containerized TuneD daemons running in the cluster in the format that the daemons understand. The daemons run on all nodes in the cluster, one per node.

Node-level settings applied by the containerized TuneD daemon are rolled back on an event that triggers a profile change or when the containerized TuneD daemon is terminated gracefully by receiving and handling a termination signal.

The Node Tuning Operator uses the Performance Profile controller to implement automatic tuning to achieve low latency performance for OpenShift Container Platform applications.

The cluster administrator configures a performance profile to define node-level settings such as the following:

- Updating the kernel to kernel-rt.

- Choosing CPUs for housekeeping.

- Choosing CPUs for running workloads.

The Node Tuning Operator is part of a standard OpenShift Container Platform installation in version 4.1 and later.

> [!NOTE]
> In earlier versions of OpenShift Container Platform, the Performance Addon Operator was used to implement automatic tuning to achieve low latency performance for OpenShift applications. In OpenShift Container Platform 4.11 and later, this functionality is part of the Node Tuning Operator.

# Accessing an example Node Tuning Operator specification

Use this process to access an example Node Tuning Operator specification.

<div>

<div class="title">

Procedure

</div>

- Run the following command to access an example Node Tuning Operator specification:

  ``` terminal
  oc get tuned.tuned.openshift.io/default -o yaml -n openshift-cluster-node-tuning-operator
  ```

  The default CR is meant for delivering standard node-level tuning for the OpenShift Container Platform platform and it can only be modified to set the Operator Management state. Any other custom changes to the default CR will be overwritten by the Operator. For custom tuning, create your own Tuned CRs. Newly created CRs will be combined with the default CR and custom tuning applied to OpenShift Container Platform nodes based on node or pod labels and profile priorities.

  > [!WARNING]
  > While in certain situations the support for pod labels can be a convenient way of automatically delivering required tuning, this practice is discouraged and strongly advised against, especially in large-scale clusters. The default Tuned CR ships without pod label matching. If a custom profile is created with pod label matching, then the functionality will be enabled at that time. The pod label functionality will be deprecated in future versions of the Node Tuning Operator.

</div>

# Default profiles set on a cluster

The following are the default profiles set on a cluster.

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: default
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Optimize systems running OpenShift (provider specific parent profile)
      include=-provider-${f:exec:cat:/var/lib/ocp-tuned/provider},openshift
    name: openshift
  recommend:
  - profile: openshift-control-plane
    priority: 30
    match:
    - label: node-role.kubernetes.io/master
    - label: node-role.kubernetes.io/infra
  - profile: openshift-node
    priority: 40
```

Starting with OpenShift Container Platform 4.9, all OpenShift TuneD profiles are shipped with the TuneD package. You can use the `oc exec` command to view the contents of these profiles:

``` terminal
$ oc exec $tuned_pod -n openshift-cluster-node-tuning-operator -- find /usr/lib/tuned/openshift{,-control-plane,-node} -name tuned.conf -exec grep -H ^ {} \;
```

# Verifying that the TuneD profiles are applied

Verify the TuneD profiles that are applied to your cluster node.

<div>

<div class="title">

Procedure

</div>

1.  Run the following command to verify the TuneD profiles that are applied to your cluster node:

    ``` terminal
    $ oc get profile.tuned.openshift.io -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME             TUNED                     APPLIED   DEGRADED   AGE
    master-0         openshift-control-plane   True      False      6h33m
    master-1         openshift-control-plane   True      False      6h33m
    master-2         openshift-control-plane   True      False      6h33m
    worker-a         openshift-node            True      False      6h28m
    worker-b         openshift-node            True      False      6h28m
    ```

    </div>

    where:

    - `NAME`: Name of the Profile object. There is one Profile object per node and their names match.

    - `TUNED`: Name of the desired TuneD profile to apply.

    - `APPLIED`: `True` if the TuneD daemon applied the desired profile. (`True/False/Unknown`).

    - `DEGRADED`: `True` if any errors were reported during application of the TuneD profile (`True/False/Unknown`).

    - `AGE`: Time elapsed since the creation of Profile object.

2.  Run the following command to get status information about the `ClusterOperator/node-tuning` object:

    ``` terminal
    $ oc get co/node-tuning -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME          VERSION   AVAILABLE   PROGRESSING   DEGRADED   SINCE   MESSAGE
    node-tuning   4.17.1    True        False         True       60m     1/5 Profiles with bootcmdline conflict
    ```

    </div>

    The `ClusterOperator/node-tuning` object also contains useful information about the Operator and its node agents' health. For example, Operator misconfiguration is reported by `ClusterOperator/node-tuning` status messages.

    If either the `ClusterOperator/node-tuning` or a profile object’s status is `DEGRADED`, additional information is provided in the Operator or operand logs.

</div>

# Custom tuning specification

The custom resource (CR) for the Operator has two major sections. The first section, `profile:`, is a list of TuneD profiles and their names. The second, `recommend:`, defines the profile selection logic.

Multiple custom tuning specifications can co-exist as multiple CRs in the Operator’s namespace. The existence of new CRs or the deletion of old CRs is detected by the Operator. All existing custom tuning specifications are merged and appropriate objects for the containerized TuneD daemons are updated.

**Management state**

The Operator Management state is set by adjusting the default Tuned CR. By default, the Operator is in the Managed state and the `spec.managementState` field is not present in the default Tuned CR. Valid values for the Operator Management state are as follows:

- Managed: the Operator will update its operands as configuration resources are updated

- Unmanaged: the Operator will ignore changes to the configuration resources

- Removed: the Operator will remove its operands and resources the Operator provisioned

**Profile data**

The `profile:` section lists TuneD profiles and their names.

``` yaml
profile:
- name: tuned_profile_1
  data: |
    # TuneD profile specification
    [main]
    summary=Description of tuned_profile_1 profile

    [sysctl]
    net.ipv4.ip_forward=1
    # ... other sysctl's or other TuneD daemon plugins supported by the containerized TuneD

# ...

- name: tuned_profile_n
  data: |
    # TuneD profile specification
    [main]
    summary=Description of tuned_profile_n profile

    # tuned_profile_n profile settings
```

**Recommended profiles**

The `profile:` selection logic is defined by the `recommend:` section of the CR. The `recommend:` section is a list of items to recommend the profiles based on a selection criteria.

``` yaml
recommend:
<recommend-item-1>
# ...
<recommend-item-n>
```

The individual items of the list:

``` yaml
- machineConfigLabels:
    <mcLabels>
  match:
    <match>
  priority: <priority>
  profile: <tuned_profile_name>
  operand:
    debug: <bool>
    tunedConfig:
      reapply_sysctl: <bool>
```

where:

`machineConfigLabels`
Optional.

`<mcLabels>`
A dictionary of key/value `MachineConfig` labels. The keys must be unique.

`match`
If omitted, profile match is assumed unless a profile with a higher priority matches first or `machineConfigLabels` is set.

`<match>`
An optional list.

`<priority>`
Profile ordering priority. Lower numbers mean higher priority (`0` is the highest priority).

`<tuned_profile_name>`
A TuneD profile to apply on a match. For example `tuned_profile_1`.

`operand`
Optional operand configuration.

`debug`
Turn debugging on or off for the TuneD daemon. Options are `true` for on or `false` for off. The default is `false`.

`reapply_sysctl`
Turn `reapply_sysctl` functionality on or off for the TuneD daemon. Options are `true` for on and `false` for off.

The `<match>` parameter is an optional list recursively defined as follows:

``` yaml
- label: <label_name>
  value: <label_value>
  type: <label_type>
    <match>
```

where:

`<label_name>`
Node or pod label name.

`<label_value>`
Optional node or pod label value. If omitted, the presence of `<label_name>` is enough to match.

`<label_type>`
Optional object type (`node` or `pod`). If omitted, `node` is assumed.

`<match>`
An optional `<match>` list.

If `<match>` is not omitted, all nested `<match>` sections must also evaluate to `true`. Otherwise, `false` is assumed and the profile with the respective `<match>` section will not be applied or recommended. Therefore, the nesting (child `<match>` sections) works as logical AND operator. Conversely, if any item of the `<match>` list matches, the entire `<match>` list evaluates to `true`. Therefore, the list acts as logical OR operator.

If `machineConfigLabels` is defined, machine config pool based matching is turned on for the given `recommend:` list item. `<mcLabels>` specifies the labels for a machine config. The machine config is created automatically to apply host settings, such as kernel boot parameters, for the profile `<tuned_profile_name>`. This involves finding all machine config pools with machine config selector matching `<mcLabels>` and setting the profile `<tuned_profile_name>` on all nodes that are assigned the found machine config pools. To target nodes that have both master and worker roles, you must use the master role.

The list items `match` and `machineConfigLabels` are connected by the logical OR operator. The `match` item is evaluated first in a short-circuit manner. Therefore, if it evaluates to `true`, the `machineConfigLabels` item is not considered.

> [!IMPORTANT]
> When using machine config pool based matching, it is advised to group nodes with the same hardware configuration into the same machine config pool. Not following this practice might result in TuneD operands calculating conflicting kernel parameters for two or more nodes sharing the same machine config pool.

<div class="formalpara">

<div class="title">

Example: Node or pod label based matching

</div>

``` yaml
- match:
  - label: tuned.openshift.io/elasticsearch
    match:
    - label: node-role.kubernetes.io/master
    - label: node-role.kubernetes.io/infra
    type: pod
  priority: 10
  profile: openshift-control-plane-es
- match:
  - label: node-role.kubernetes.io/master
  - label: node-role.kubernetes.io/infra
  priority: 20
  profile: openshift-control-plane
- priority: 30
  profile: openshift-node
```

</div>

The CR above is translated for the containerized TuneD daemon into its `recommend.conf` file based on the profile priorities. The profile with the highest priority (`10`) is `openshift-control-plane-es` and, therefore, it is considered first. The containerized TuneD daemon running on a given node looks to see if there is a pod running on the same node with the `tuned.openshift.io/elasticsearch` label set. If not, the entire `<match>` section evaluates as `false`. If there is such a pod with the label, in order for the `<match>` section to evaluate to `true`, the node label also needs to be `node-role.kubernetes.io/master` or `node-role.kubernetes.io/infra`.

If the labels for the profile with priority `10` matched, `openshift-control-plane-es` profile is applied and no other profile is considered. If the node/pod label combination did not match, the second highest priority profile (`openshift-control-plane`) is considered. This profile is applied if the containerized TuneD pod runs on a node with labels `node-role.kubernetes.io/master` or `node-role.kubernetes.io/infra`.

Finally, the profile `openshift-node` has the lowest priority of `30`. It lacks the `<match>` section and, therefore, will always match. It acts as a profile catch-all to set `openshift-node` profile, if no other profile with higher priority matches on a given node.

<figure>
<img src="data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABfAAAAQ1CAIAAAB1CnmTAAAAA3NCSVQICAjb4U/gAAAAX3pUWHRSYXcgcHJvZmlsZSB0eXBlIEFQUDEAAAiZ40pPzUstykxWKCjKT8vMSeVSAANjEy4TSxNLo0QDAwMLAwgwNDAwNgSSRkC2OVQo0QAFmBqYWZoZmxmaAzGIzwUASLYUyTrUQzIAACAASURBVHic7N13nFXlnfjx5znltukDwwzSYUAQ6YiggCKoIMYaszEmutFEE03WJJpNNclmdTdmN4kplvVndDXqBhO72IgVpIgMXZEiRTrMwLR776nP748D1+udwoDD3LnD5/2aP2bmtOc5d+Z8z/mep0illAAAAAAAAEDu0LJdAAAAAAAAABwdEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjiGhAwAAAAAAkGNI6AAAAAAAAOQYEjoAAAAAAAA5hoQOAAAAAABAjjHmbXzpo5qN2S4GAHSokB65euy1utSzXZATwse125794ElTM7JdEADoOI7vXn/ajSE9nO2CnBAc33lg6b2alNkuCAB0KOOVDXPnb3kz28UAgA6lSePLo6/RdRI6HWHrwc3/8+6fYmY02wUBgI4TdxLXjLmOhE7HcD3nniW/J9AAONEY+aGCqBkTQvjKtzwr2+UBgONIl1pwb50XKhCC93gdJKSHYmYsakYJNAC6vFSgEUJKGox0FCllcaRY13QhhO1ZnvKzXSIAOI7CeliTmhDiUAN4X/kzBp1/3uDZnvKyWjAAOF40IQ8mD/xh0W8STjzbZTkR+cofVjb8q+NuINAA6KqkEJab/NPi31XH92e7LCeobrHu35r43bARUdkuCQAcJ7rU/7bm8aXbF2vy8IgGlmud0W/qxD5nZLdkAHBc+cq7e/Fd2S7FCcpyrdE9xxFoAHR5f37vf7JdhBNX1IhNG3hutksBAMfX1oObF2x5K2pGP5nlyvWcLBYIADqA5/u8sssi2uYA6PKUUr6gv0/W+MJXilAPoIvzfDf4hmnLAQAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMSR0AAAAAAAAcgwJHQAAAAAAgBxDQgcAAAAAACDHkNABAAAAAADIMUZ2D6+ESjgJ2cJSTWq6ZhhaZiFb36qVDYUQnu9ZniWFUEKYmmnqZrN7SDiJlburttduq03WCiFKoqV9i/uNKB8VNiLNru94juM7LRdJ6poe0kMtHUsIJYRQQkTNqBRSCJF0k0r5LVfxE0qIkB4yNCPuxFMFkFJGjGhLm1iu5Svv8OYqZua1fohg/dbPmBDCcpPLdy3bWbfjYPJAXiivPL/n+F4T8kMFbakFABwnnTbQKKE+Prh17d7Vexv2uL4b0kMVBScNLTulT1HfZtdv90DjKc9yrVbqmLH/iBFJuolPfm7XQCOEsNzkil1VO+t3HEjURI1oz8JebQki2w5uWbt3dU282vGdkmi3U8qGD+o2WJO8rwLQcTo+0IgWLuxND9FhgabZ2NfZAs3HtdvW7Fm5p2G3EKJbrPuwsuGDug1u9tSlI9CgM8tyQqfBaphy/9ioGWt2qSa17nlls4Z87nNDL+lV2KeNW6U2PK9y1oVDL+lXPCB90Ssb5v741VuiZizhxL88+tpbp/woY1tfeU+sfvyBpffW2XUZi7pFu9048TsXnnyJlJn/9r9f+N+PrniwlSLFQrFhZafOPvni8ypn6Zqe+r3jO7MePstyLSFEwonPv76qIFzgK/+Kxy/cH9/X0t7SJZz4LVN+9JXR187b+NLPX/tR1IwKJeJOfM4Xnx1adkrT9eNOfMaDZwbZIl/5Y08af89FDzatUUqD3XDeQ1OU8ls6Y4F3ty/68au31lm16b8MaeY3J9585cirueQByJZOGGiEEJsPfPTf8+9Ysn1RxuXRV/45A8/97pk/6FlwUsYm7RtohBCLtr3zreeua2WH6WzPeueG5Qu2vvX9l29u90CjlHrhw2fuWXxXdaI6/fchzfz6hJu+MvraZoOI5Vm/fP0nr2x4MX2pr/zRPcf8dNrt/T/9oQDA8dPxgaalC3u6jgw0ooXY13kCjeVZt7/xs5fWP58RMib2OeMnZ/9bz4JeLW1FoEEnl+XHbClF2IiEjXCzX6Zu1iYPPlz1/y76y7nvbJvfxq1SGz664qFLH5311ubX049o6ubhbSMRM7O5jeM7N7/wzd++8ytXuTEzlvGVcBP//sZPfzrv+36TtjMRM9J6kTzfW7W76qfzvn/9M1cHF99DdRGiIFx4eLVI6ipUEC5oZW+f/ooYmimEuGjoZWN7jjc1M2yECyOF//7GbY7nND3nd7z5c13Tgm11Tf/1zN83e+3zlHcweeAfm1755rNfPbx+M2cs8M7Wt7/x7Fdd38k4Y4Zu/n7hf/3iteZzQADQATpboBFCLN2x5J/+73Or9qzID+VnXDbzQ/mLPl7w+cdnf7BvbcZW7R5oTM1ofYfpX1EzT5P6uZWz2jHQBJTyfzrv+//+xk8TbqJpELl78e9+9o8fNt3K8ewbnr76zY/+kXEO80P5H+5f9/nHZm+v3dbSEQGgfXV8oGnpwp7SwYFGtBD7OkmgSbrJ65780uubXmkaMlbuXv5Pf72kwW5ouhWBBjmhc7WbsD0r6SaCL9s7dI0IG5GCcOFNz1675eDmI26VsWFhpPDmF25oacOmfvHaj6t2vptqsJfac2qfMTNv3qaXH676cys78ZWfXp6kmwgSQJrUC8IF6/atve21HxyxJHZzV64Wj+h7Qggp5W3n3J50ElJIXeobqj/8y/IHM9ZcsWvZvI0v6VIXQiScxC/O+Y+CcGGz+1y07Z2z/t+EH796y9aDHwXrt6TOqrv5hRsKD+/H9qyEE08/Yy9vmLtw6/yWdwAAHSfrgWZ77bZvPHNNLJQXXFrTQ0YQLHSpm7r5taeuarDrW9pJuwSapi8nWuF4tud7Qoh2DDSBR5Y/OG/Ty2mR1447jQnnUI1iZt7L659fuXt5xlYPvHfv+/vWmnooqEjCSaQ20aUeDUV/+Or3HP8oIikAtBcCTfpO2lhmcdwCja/8G565ZvOBj1oKGUr4//nmz5tuSKBBTshyl6t0utTPHTQrL5wf/Bi3G9/dvrjerjOkoYQqiBTe9c6vfzf7noxejhlbBRsu2vZOwo0HTeOiZuypNXO+N7mZ93sZ3t+75pX1L+SHC4QQUsikm7hq9D+fWj5SCLFiV9X/rXwkZuYpoWJm7N4ld82oPL/Z3qe+8geUDBpePiL9lxur16/atTxqxpRQph56fdOrBxMHiqMlLZVECtkjr4evPCGkEEKTmuUlG6x6JZQQwtCMokixEFIpJYRImvG80KHqDygZ+LXTbvzze/dFzWjMjN239I/TBs0YUDIoWGp71g9f/m7MjAXlHN5jxLmVs1oqg6kZESMSNVvstpryl+V/Dq50Ukjbs68b943zBl/w3o5373rnTk3qwRn75Ru3zb3mtdYTQwBwvGU90CilfvnGT2OhQ8kL13cGlg7+/Klf7Bbttj++b87qx7Yd3BI0utQ0/T/e/MV/nPebpjtpl0AjhAgbkW6xbhHjUEt4TWoHrRrP85RQUsi8cF5Ejx2+F1d+xA9efrZjoAnWWfzxO0op27PDelgIcePp3zl/8AVbD2658+1f7mnYrUktGor977L/97vZ96S2qk0e/N+qB1JH6V3Y51+n3hYxIve9+8f3diw2NFOX+rq9axdsfWvagBmtHB0A2h2BJl1nCDRJNzmyfPS22q1xu1Epf3L/s742/kZf+L+d/6uNNes1qelSf2fbAtuzQno4tRWBBrmiEyV08kL5P5t+R/ozv+M5/7P0T4+veDhkhHSpL9v5ru1aGcMSN91KCJF0Ez9+9db3dizRpBY2wq999Oq/nHFrSyOKpdyz5PfRUEwIIYW0POt/LnlkZMXoYNHZA2ac3vuM7754Y9SIKqF0zXj2gye/NfG7TXdiudY1Y792zsBzM36/bMe7//LCDcHwYLrU392+6LzBF7RUEinlny56IEjfBOXZ3bDr84/NDhkhIUSemf/w55+ImdFDi5VI79V5zdivvbJ+7r743qDuv3z9tgcu+0twfh5Z/mCtVRs2wlLIuB2/7ZzbW+9o2mg3+MqPmJEgAjW7muPZT66dEzbCQd2/cfq3rx5znRCiT1G/gSWDvvHsV4NFBxLVH9VsHNzt5JYOBwAdIOuBZmPNhqod7+WH84UQvvLP6DvljvN+Y2qHRk2eNeSim1+4Ye3e1cH95T82vvqDqQeLIsUZO2mXQCOEGHPSuOe/8lrqmUIK+ev5tz/3/lMhI2S51s1nfv+ioZelX/xTZ6C9Ao0QQpPaPRc9+OH+959c88TcD5996ssvVeT3FEKU5fX4t+m/+uqTV0bNaPCG1vXd1Ol9Y/NrQcGkkGE9cv+ljwRjJ//2grv/5fnrV+1ZEaSBnnn/72cPmH7E0S4BoB0RaNJ1hkATM2O3TPnRTZO+u2zHu5tqNnxl9LXB+nddeN9FfzmUi0k4cdtz0hM6BBrkik7U5UoJlTGvk6mb14y5LvUPYru247tH3EoIETGi35r4vVTHznqrzm2yYYY6q/bd7YuDy4TlWt+eeEsqmxOY1Hfy1aOvC/YZNsJPrZ3TbH9OIYTX3LHG9ZowrteEVLPDmkRN6+UJLrLBlya14kiJd3gUd1/4USOqHV6qa3r6VSysh38+/Y64ExdC6FJfu3fVE6sfF0JsPrDp/qV3B+mVuBO/fsJNA0oGtlKASX0nL7i+at61C64Z87WMLrLpthzc0mg3Bt+H9PAVp16ZWjSq59gxPcelqrx698rWqwwAx1t2A40Q4tUNc4P7YClk2Ij82/Q7UzfZQoiQHrrz/Ls83wtuDaUUGYMmpLRLoJFC6pqeHmsKw8VBrPGUVxAqTI9E6Y8Z7RVoDhVDyqFlw38y7d9e+9qiIJsT6FXYO/W9Ep86/69vejX1IuErY65NzYSlSe3bZ9wSfCi61FfsqmopUgPAcUKgSddJAo0QImJEzuw39eox16Wem/JD+ekTKWYkZQg0yBWdKKHTLO1YO+kYmi7SWrgccf0Vu6pSKxmacdGwS5uuc+Woq1Mp5Ea7cVvtlqMqkqmZQScpIYTWaiK5qdScfIGMW9sMIyvGTBs44/DoA7H7l/5p5e7lv13wq+CqFDQavGbs145Y2uJoSXGkZFDpEO/TR0+3sXr94RL6I3uOzhjEftbJnwuud5rUNtVsaP2IAJAVHRZoPOW9lnaD+E8jrmrarbUwUnTFqV8KrpwhI/T6R/OOqkifJdCIT8cav+Urv2inQJMh+um5ae9a+F9Bu1Rf+RX5J6Vu9B3f2Vi9PvjRU96ZfaekbzWwpLIwXBR8n3QSrQwPAQAdhkCTkt1Ak275rmUHEjVCCClkQaggiDgBAg1ySCdK6GhCy7jYKaXmrH40dcmImtGQbh5xKyGE53sPLrs/ZISFEFLIkmhpSA+JVu1r3Bt84yv/lPIRqVFp0hWGC7vHylIX080HPmp2V6bWzLE2VH+4dMfi1PR+FU2mCWxfP5t2u+u7QVGVUt9+/voVu6uCq1Lcif98+h3htCaFrXN9u5WltcmDwTeWa03uNzVjaVleefBN2AhX7Xwv9VECQFZkN9C4nnsgceDQ5sqb3O+sZlcbUTEySKPrUv+oZmOz72O7WKDJkHASv3zjp69umJtqNnv+4AtS71Q930vdPYeNcO9Pj2ena3q3WPdUpN6w/8NjKwMAHBsCTTtq90Dj+u6f37vvwWX/84NXbv6X578eNGWKO/F/nfrT9HZMBBrkkE40hk6DU/+HRb8pTBuifOmOxat2r0hlYcedNMFschVrulXcaZy/5c2d9TtSN4KXDr8ifZSZZu1v3Bd8Y7nWpL6Tm11H1/SJfc6c++GzQQb34OHLZbqQEZqz+tGPDmxM/+X66nWLt70TlCHohznupAmtl+czKggX/vycO372jx8GWXlNSiEOjXI/beCMkRVj2utAqYSOEKI4WpqxdHC3IanvE07cU54hO9GfHIATTXYDjes7CSceTOaqSa1f8YBmV0u/RNdb9V7a2DGBLhxolFALty342bwf2L6VGm7f0IxZQz6XWsfzXcdzgo+sMFyka5867ZrURvcc+9wHTwWRutFp/AxVBICjRqBpR+0eaBzPuWvhr6NmLGKEg09Bk9oXRnzp3MGfGlaZQIMc0omerj3fm7PqL15a99GIEQ5ypVLIeqv+O2f+a9Omhk230qUWNiLBtU8KGTLCXzj1S0c8uuV9MkxM5NOjlKUry+/hKjckQkII22tmZJmgk+eynUvTfxkxwqmke9yJ33zGrXmHR54/fs6rvGDOqseCwduD30ghXd/92bTb2/Eo6eet6aeT3gPL8d2WRlYGgI6R3UCjhEpdBk3dbGkQx/Qu/Y5n+03aNnbVQGO51g9e+c6ibfOjZixtqt3kfRc/lD4frRIqNXxDs+ewOFqSitQMbQCggxFo2lf7BhopRXGkND1B43ruqIqxGZ8IgQY5pBMldIQQ4eYyKbZn2551z0V/7lfcv+1biUOzaFsPXPZYxsAuzUpv+uh4LXYyWrfv/SBZK4RomlwPaFKPNXfEYFbvGZXnf3Hkl49Yns9OSnnbOf/+hf+7OD+UF1zZ4078lzN+lX5b/Nl9uuVnZjCw3GTqe0MzGAEeQNZlMdBIIVOXwVYGttzdsDP1vdHC7XjXCzRJN/n1p7+yqWZDcCalkHGn8eSyU35xzn8OLB30qYOmncZm1Vt1qQF3jjgdDAC0OwJNO2rfJxqlRK11MGZGhRAhPaxJTdO0n8y71dCMswdO/+SgBBrkjk709yeFTLhxz//UcL/FkeLZJ1987bgbusW6H3ErXdOiRiyVlq7IP+m+Sx5qOg9fs7rFyoJvQkZoyfZFXx791abreL774f4PUv+9xZGSZsvjKjfpHEpkpM/5nXSTPzjrtouHXt761HrtaEDJoOtPu/GhZfeHjJCv/GFlp5xX2drMgscg/STUJusylm6qOdRQUwoZ0SP6sQ4IBwDtIruBRteMoBm8EMLzve21H1d2G9x0tfQh5AtC+U3vFLteoLE9+/qnr9lUsyF4SeAr33Kt26bdMWvIhamRGlJ0TU+9UKm36jzlp58gpdTKXctTr16afRoBgOOHQNPu2vGJJmSE/jD7Pik127Oe++Cp5buWGZoRNaPfnXvjm9e/W3R4qGMCDXJIJ0roRI3oQ5f/tTj6ydVKk1rYiLQ+2FX6VrXJ2uueuso73LWnzq5tdmzjZnU/fHnVpb5618qEk2g6Jny9XV8Tr0799/Yt7td0P5ZrXTv+hs+f+sXgxyfXzLl/6d3BrpRQYT3cYde+wKBug4MxzyzXOr3Pme1+9FR2XJPaloObMpbWJKqDZjuWa405aVwH1x0AMmQ30JiaWRgurrdqlVCa1BZtm9/sffbaPauDhuW+8vsWD2h6n931As0vX//JxpoPg2yO67un9Bjxq/N+Wxrr1uzKujTyQrGkmxRCJJxE3G4MRz/5+DzlHUibRrey28lHWxgA+CwINMdDez3R6FI/e+CM4Pvpg87/ztxvrNhVpUktZITmb37jwqGXHF6NQIOc0YlmuTJ0s29xv+JISeqrMFx0xKHL07fqV9z/+1N+EnfiwaKaePUrG+a28eije45Th7tKWl5y3saXmq7z2MqHg2+CYcAGlAxsuo6nvEGlQ1JVuHrMtb0KewedMCNG5O7Fd7XSn+t48NIaW7Yy+/gxG1RaGXwTNsIvffhCeh8rIcRLHz4fjMzvKW9I96HtfnQAOCrZDTS6pp89cHowU2zYCP919V/sJhGhzqqbs+rR1Iyz0w7fd6brYoFmy4GPXln/YqptzrmVM++9+MGWsjlCCFM3B5YODuqrSe3VT8frbQe37osfmrYyakaLIkVHWx4A+CwINMfDZ3+isT27aufS9AE9NaldcsoVycMPL3sadqcWEWiQQzpRQkcJ5R/9/2fGVudWzuxT1Df49wsb4XuW/N7z27TP4mjJiIpRqQ1/s+A/P6r51Ljui7YteHT5Q6lr34VDLw61cGlOn+fb1EO3Tvlx6oq8t3HP21vePKoKdnIDSysjRjToZRp3Gl9a/0Jq0YbqD5dsX3h4YEtvaI/hWSslAAghsh1ohBDnVc6yD8eIOqvuzrf/3U8bAtP27B+8fLOuH3pTqpTf7H226FqB5rl1TxuHq9yzoNePzvqFLvVgXM/0r/RNZgw6L/W48pflD6a/S7j33T+kppIZ0m2o2WRuYAA4rgg0nU2D3fDU2ieu+L/ZX33yyne2vp2+6IO9a1MjQlifnu6GQINc0YkSOu1Ck9r3Jv8wdbnZ17h31Z4VbdlQCnnTxO+lNpRSfvXJLz6+8uGVu6qW73zvgffu/c7cbwT/ulJIy7MuP9wE8YhO73NGv+L+qSvyw8sfSL+q5rqQHrpo2GWp691v3vnPp9c+UW/Vr9xVdcMz/5x649qveMDJtNAB0CUcc6ARQpzS49RhZcODKKBL/aX1z9/8wjfmb3lz7Z7Vr38074Znrlm5e3lqgqdJfSe3NNpChtwNNK7vzl33TKovs+Umv/fijdc+9aXrnroq/euf/35lEGgCZw881/f94F1CrXXwO3Nv3HxgU51Vd/sbP3tn61vBCYw78a+Ov57B+AHkIgJNe1FK3fjstXe+/cvaZG1JtPSWF2/6y/IHd9Rtr7NqH6564P9WPZIKQOX5FekbEmiQKzrRGDrtZWKfMweXDtlRv12TWtgI/3bBfz78+SdSE921YsxJ487oM6Vq19KgH6mU2h8X/cY7dDXUUgPLx534deO+kepqdES61H8w9bYbn7suP5SvS/39PatX7l4+pue4Y61fp/PVcdc/svzPYSOshNKlfuf82389/3YpZaoFU9yJ3zLlR4yIDKDLOOZAo0nt5+fccfnjs0ujpUqokB5auXvZku0Lg6URIxzkwaWQSdf6txm/amN5cjfQ1Fv1tcna1BCeB5MHDiYPNF0t4STSnxxKo6X/NPLLf1vzeNSM6lJfs3flF/96iSaloZupFwkDigdO6D2pY2oBAO2OQNMupJS3TPnR1X/7QszMU0JFzdjdS+760+LfaVIqISJGRATzdjXpekagQa7oai10hBCa1L4/9adBSluX+gd7167du7otG0ohfz3r9wNLKpNuIvhN2IjEzFjMjKXmEUy6idN6T7xhwk1HVaTxvU4f1v2U4GY0Gor9YeF/KZU5w3fuKo2W3nn+72qt2iA/HTEiYSOSyuYk3cSZfadO7HNmVssIAO3pmAONEKKy25DfXnD3geSBw53z9SDQxMyYdviVaaPTePfnHmh2LsWW5GigWb9/XUZ3qmaF9HDGCJg3TfxOn6J+waS8utSjZjRsRFLvnGuTtf9x/m94kQAgdxFo2suoijG/nPGr1NmIGJEgZKSyObVW7b+f+1+l0cyx2wg0yAlZTuj4SjXYDY12Q6PdsK9xbxsvCUfcanTPsYNKK+utuka7wRfq5//4YerNXtJNBNs22A0NVuY02xEj8ufLHr1mzNdd3026yaSbOPyVTDgJpdS3Jn7v97Pv05sMBd9g1aV2m8oHpWhS++7kH1THqxvthqSbXLxt4bKd7waLlBD7Gvc2Ht7Wb+GyeGwn6oj1ba89zBxy4Z3n32V5yYyTVm/VXzXqq/99wR9piwggWzpboBFCTB903qNX/L1fycAgKGRcNoeWDZ/zxWdP6316xlbHO9Ac8RAt+SyBZn98b+o8t/JVk6jOeGyImtGHPz9nRMWYT5/DZKPd0CO/4rEvPDmYaUcAdJSODzRHvLB3cKARbY4FHR9ohBAXD7v8nov+XBItzQgZCSfh+t6d5//uwqEXN92KQIOcIH/+jx++ufm1hJP4t+n/OXPIhR18eKXUweSBYOY5KWRRpPiIm7RxK8uz4nZjsI7v+yWx0iCnYHt2o90gpVRKRYxIqiNVhjqrduG2+Tvrtu+P75dCdot1H14+cmT56KZzmQcSTjzpJoPd5oXyg5Z4GQ4kaoLyZBy6NnkweD+plCqOlDQ7D9+xnai217dd9lBv1S3Y+tbWg5sPJg+G9NCAkoFT+k/rHis72iMCx4/jOZc8NrPRrs8LFTxz1cuMY9cx3t2+6NvPXy+E+MqYa7818bsdfPROG2h85X+wb+2q3Suq4/sa7IaCcGF5Xvnk/meX51U0GwiOd6Bp4yGa+iyBJrVt66sppYqjJU3fDSil3t+3ZsWuZbvqd7q+WxItHd/r9FEVY5pOwQt0GKXUVX+7fGfd9oSTeO26hfmhgmyX6ISQdBPnPjhZ1/STCns/dsWTHTypdscHGtG2C3tHBpo2xoKODzQpju+s2rV8+a5lwUuC4mjJqIqxo3uOjRzuitEsAg06p8dXPvz7hf8dNaNZ/kOUUpZES4/HVmE9HI42MwtVSA+F2nDEwnDRzMFHkd6KmrEjXllaKnNbLvrHdqJEm+vb+50RIwAAIABJREFULnsoCBfOGvK5z3IsAGh3nTbQaFIb3mPE8B4j2lik4x1o2niIpj5LoPmMQUpKeVTnEACOh44PNKJtF/aODDRtvJ53fKBJMTVzXK8J43pNOKqtCDTo5LrgGDoAAAAAAABdGwkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAAAAAACAHENCBwAAAAAAIMcY2S4AAADHhed56T/qup7+o+/7SqlmN8xYM2M/KVJKTfvkvYhSyvM8KeUxr6mUMoxPxeWWCtn2NY+5Om1fs5Xq6Lqe/vvPXvGm1WlpzXavTtvX7FSfY7tUJ+NzPB7VaffPMWPNpksBoF3U1NT86U9/KioquummmzKugUAH4G8OANAFbd26df78+amnUM/zZs6c2aNHj+BH27b//ve/N/sA6fv+lVdembonW7du3ZIlS5q9RdM07YorrkgtWr169fLly5tdMxQKXXbZZakn2JbWdF13woQJw4YNC350HOeZZ56xbbvpDjPWbKU6ruueccYZgwcPTq05Z86cZp9sM6rz2Svuuu7YsWNHjBiR+s2KFStWrVp1xIofVXVaWrPdqyNy83Nsl+qkf47HqTrt/jlu3LjxnXfeSf0opZw5c2ZpaWnTDQHgs3jrrbeqqqqEENOmTRs5cmS2i4MTTtYSOkqofY17feVL0cxbIwAnAiWUJrWyvB5cB9Du9u/fH7Qs8DwvaHqwffv2VEKnoaHBsqxmHwtd1/V9P/Xj5s2bpZTpv0mxbTv999u3b29pzYaGBs/zUk/OLa3p+35tbW36Vg0NDc0WsumaLVXH9/2ampr0NV3XbXbNjOp89or7vt/Y2Jj+m127drWx4m2vTktrtnt1RG5+ju1SnfTP8ThVp90/x+rqat/3fd+XUuq67rruzp07SegAaHe6rgfp9ZYaJALHVfZa6Cjxce0213NoAQucsHzfN3SzLNaDfA7aXdA2RynVu3fvUCikadrw4cNTS0tKSkaMGNFsKwNd19MfLCdNmrR27dpme6yEw2HTNFM/TpgwYd26dc0Gtby8vLas6ft+ZWVl6sfi4uKxY8dm5ESaXbOV6iilTj755PR9nnLKKc12WsmozmevuO/7/fv3T//NuHHjNmzYcMSKt706razZ7tURufk5tkt10j/H41Gd4/E5Dh061HVdKaVlWbt27RJCcMMJAOh6stnlytRMKaTWXFQGcCLwpTI0On7i+JoyZUrGaB1CCCnl+PHj27J5cXHxmWee2ZY1u3fvPnny5HZcU0o5atSotuyw7dXRNO30009vy5rHo+Ll5eXl5eVHXK3t1eFzPKKcqM7x+ByLioqCNR3H+etf/9qWTQAAyDm8rAAAdEFB5wvXdWkCDZzIUlcA13WzWxIAANodCR0AQBcUi8Usy8rPz6efBXAi0zTN933btouLi7NdFgAA2hmdHQAAXdCwYcMGDBgQjJ6T7bIAyBrDML70pS95nheJRLJdFgAA2hkJHQBAFySljEaj2S4FgOwzTTN9vGQAALoM3lsCAAAAAADkGBI6AAAAAAAAOYaEDgCgC4rH42vXrvU8L9sFAZBlmzZt2r17d7ZLAQBA+yOhAwDoghYtWrR06dJXXnklmL8cwImptrb2rbfeeumll3bt2pXtsgAA0M5I6AAAuqBIJGKa5v79+13XzXZZAGRNMCKyYRgff/xxtssCAEA7I6EDAOiCYrGY7/tSymwXBEA2pea3MgymdgUAdDUkdAAAXZBSKttFAJB9XAoAAF0YCR0AAAAAAIAcQ+tTAACEECIejzOCMpAr8vLy6FMJADjBkdABAEAIIerq6pjmHMgJSqlYLEZCBwBwgiOhAwDogo5h4AxN02ihA3RV/HcDALoeEjoAgC7IMAzbtg3D0DRGiwNOXJqm2bYthIhGo9kuCwAA7YyEDgCgCxoxYsTgwYMNw2CuYuBEZhjGl7/8Zc/zSOgAALoebnMBAF2QpmmxWCzbpQCQfeFwONtFAADguKAhOgAAAAAAQI4hoQMAAAAAAJBjSOgAALogpRRzkAMQQniexxRXAIAuiTF0AABd0MKFCzdt2tSvX7+pU6dKKbNdHADZ0dDQ8PTTTxuGMWPGjLKysmwXBwCA9kQLHQBAF6SU0nV9y5YtjuNkuywAsibI57quu3nz5myXBQCAdkZCBwDQBeXl5fm+r2mEOeCEFgqFgm8Mg2bpAICuhjtdAEAXpJTKdhEAZB+XAgBAF0ZCBwAAAAAAIMeQ0AEAAAAAAMgxJHQAAAAAAAByDAkdAEAXFAycwfAZAAKu62a7CAAAtDMSOgCArsmyrJKSEqa2AU5kUkrbtm3brqioyHZZAABoZyf6ba6maZrUpZRCCN/3fOXzOhcAuoDRo0cPGzYsEokwczlwIjNN86qrrpJShsPhbJcFAIB21nUSOlLKsBERsplFSilfea7npidrNE0z9VA8Ga+NV1tOUpd6XiSvKK9Y06Xt2p9sK4Spm4be5EQp4Qvf8z3PowUvAHQ6uq7HYrFslwJA9kUikWwXAQCA46KLJHQ0TYsnEy+8MDcRj2fkdEJmqLy8vO/Avv1O6ud4rlK+EMLQTduxFy95e93C9Qf2HLQTtpCisKSgYkj5aWef1r9Xf8ezg+yPqZurP1i1dsUHQvNT+9Q1vaioqKxHj34D+nUv7u76ju/7AgAAAAAAoEN0kYSOFNJ1nE3zt1hxq2kjnQ/FJt1cPGrmiHNnzBBS0zStvrH+2Uef2756h9KVkirYpPZAXd2ihs3Ltk778tTTxp4WtNPRpLZv+/6tb3/s637mIYWIFcVGzhg+efJkXdc93+uYygIAAAAAgBNc1xlZQEppxgxl+MrwhaaEFKkvZfiucpc/t2rBwgUhIyR88eLfX9q+eodv+EoI6WmRaCRkhKQvle7brvOP/31zw5aNISMU7Fk3NN/wleEr3f9kt0L4mt/Q0LD4b0uffvwZz/UYpgEAOhXP82g+CcD3fc/jrRsAoAvqIi100kklT512Srce3TzP0zSttqZ27YL3Hdv1DW/la2tOn3D6lh1bPnpvizJ84cui7gVT/2lKRVmF67tVC6tWzVurdN/3vXdeXDjg+v7BYMmp3RZU5I+dOubQbg/UfrDoQ7vB9k1/07ub3+4zf8Y5M2zfymLFAQApa9asqaqqisVil156qa7r2S4OgOxwHOdvf/ub4ziTJ08eNGhQtosDAEB76oIJHeHLUycOP6XvcMu1hBCmbuaX5r8zZ7HS/cYDjdV11auXrglWDIVDF153wZB+JyfdpCa13hf3ci3n/bfXK93f+cGubbu3Deg9IH23hRX508+eHuxW07TRE7Y+/T/P1VbX+rq/8tXVo8eOLikqYYxkAOgMdu7caRhGIpHwPI+EDnDCamhoCF7FHThwINtlAQCgnXXNXkKu5zqe7XiO4zm+8nv37xX83hf+vn3792+uUZovPW3g+H6D+lQ2Wg2e5zqurYQaP3W8ETKEEEqJbRs/lp8+P76vLNeyXct2raSd6HdS/7O+MEVTmpAi2WBt2rhRlzwzAECnUFZWRicLAPn5+cE3dI0HAHQ9XTS2eUL5QvlKKtmYaFi9eI2QSggRiUWErxoPNgSD4PSt7OurT4ZXcDy3e3H3wvJ8qaQQonpfdesHsV1rQN/+BWUFQkkhxO6Pdx+/CgEAjkowUyGAExyXAgBAF9YFu1wp3X/jibcXxpYIpaSUifpk9a4aoSnpyYrKHnmFeXbcCRJZRT0KP7Wh8mPRvEj3sPhYCiFqa2tbP5Dne/mxgliPSN3eeiHEgRqa8gIAAAAAgI7QBRM6Qoj926vl4fcxSgohlfS0aEHknIvPSbpxoaQQSjT30kYpX/mHfqnJJvOfN6FpmjQOrcYLIAAAAAAA0DG6Zpcr6cvUl+bJkBHufWqvS791cb+e/Uw9ZJiHRro5uKc2fR4rTdMaE/HkXktpSghRVFx0hKNILZ5oTO63g/WLi4uPW4UAAAAAAAA+0QVb6EhfnvZPY3qeVOG6rhBCk3q3ou7l3XoYhpGw4wXRwkhhxDngCCG2btw26fRJUsqgqY6ph7bs3VK3r15IJYTsVtat9QOFzfCmrZvqdtULqYSS5b3LO6B2AIC2Y/gMAIHgthAAgK6kCyZ0hJKVlZXD+w63XFsIoYTyfM/zXcd1hBDF+UU9BpU1vNuodH/L0q0fTHh/xMkjbc/WpWY7zqKXF3ueJzQhpewzsI8SfvpEV5omw0Y4GFDZ0Iz9tfvnP7PA9V2hCSOiDxo80FPMqAIAnYLv+67r5ufnM2c5cILzPE8p1b1792wXBACAdtYVEzpCOI6dcJK2azWzTIqxU0Z/9O4WIYTjOS8+/Er1BTV9B/VJNCaWvVm1bc12pSnpab1HntS3Z1/Xc009dGhDTSVqkivfX+G6rhKiprp67TvvH9hRKzSludqpM04pLym3PbvjKgkAaNmgQYPi8fiECRNI6AAnMtM0hw8fXlhYOHDgwGyXBQCAdtY1EzqtcDxncL8hp5w15IM3NvimF69NvPnYfKGpYExjpSmppBEyps6erOma537S4kZJVb3twJN/eFYIJYJWOppSmtJcrXxwj6nTp9I8BwA6j5KSkqlTp2a7FMdISqlpmqZpUkr/sGwXCshJUsrTTjst26UAAOC46DoJHaWUZ3vSk9KXfsuDJiillPTP+9z5tu1uWviRkkppSgglpJBKSleLFkXOvWZ6/14DUg18fM+XnhRSBlNjBbsRQkhP6qY+bPrJ55w/LRaNeR59swEcR0qpoOOAlFLXddmGmfiQRVLKcDgcfEy2bXvep5L+4XA4aDpk23bG0B6maQohDh482NDQ4HleJBIpKirKy8uzbTs9rWMYRigUyhgkSCkV/J00HS6k2fXTS9u0JABONAQaAMgtXSSho4TSdL3boNKG+gbpy3AopESLLzM934uEwpd/8dLVI1evXrSmZvtBJ+FqugwXhQeM6Df+jHHl3Spsxzq8Zz+vOL94UKHSP7kJNgy9qLi4R6+yQUMH9u3Zz1ce2Rygy/N9/7XXXnMcp9mlnucNHz48vUn/gQMHFixYoOu67/vnn39+8JTe7A49z5s5c2bTFVKUUkuXLn3qqaf27t3b2NgYjUYrKiouvvjiiRMnpu62Wy+eEMI0zenTp2ta15zcsLPRNK2xsfHvf/97XV2druszZ87s3bu3bR/qlmua5vPPP799+3YhxGmnnTZ27Njgg5NShkKhzZs3v/7661u2bDl48GAwDFD37t3Hjx9/xhlnhEKhIOdimmZVVdXSpUtTfzZKKV3XS0pKysvLBw8eXFZW5jhOKgHUdP0MjuOklwRAVnTyQCOE2LFjR1VVVUtdWT3PGzt2bK9evY6izgCAz6CLJHR8349Folddd6UUUgjhKz8YArklnu9JKceMGDty+Mi6hvpEMq7rRmFeQTQS9ZSfyuYIIRzXGTd23GnjxmfsQUpNk1IJ5biMmwOcEHzfv++++1rq+ZJIJK677rr0++wXX3zxscceC4fDiUSiqKhoypQpLe0wkUicc845rdxn33PPPfPmzYvFYkIIXddt2962bdudd9557rnn3njjjcGtduvFE0JomjZt2rQTKqHjeV7Qd6njDy2ldBxnxYoV+/btU0rV1dXddNNNhmEE7XQ0Tfvggw/WrFkjhOjVq9f48YdCTCgUWrhw4Zw5c+LxePD3IKVsbGysr6/fsGHDmjVrrrnmmoKCAtd1NU3buXPnokWLwuFw+nGDypaUlEyZMmXGjBm6rqeO2Oz6KZZlpZcE6Ep83w8yntkuyJF18kAjhFi3bt3dd98djUZbKuH3v/99EjoA0GG61J297/ue73m+15Z5apVStmv5yi/Izy8vq+he2t0wTdu1m7a1UerQbtO/XM+xXbv1tBGALqa0tDQajUajUcMw9CbS32E6jjNv3rzi4uJoNFpUVPTKK680e10KdhiLxVpp1r5+/fpXX301Ly8v2EMsFrMsSymVl5f36quvLliwoI3Fy4mHmXa0Zs2axx577Kmnnsro69Rhgi5XkUikoKBg3bp1r776avqjVCgUikQikUjEMIzUb9atW/f44487jhOJRFzXDYVCBQUFwa6i0ejKlSufeOKJoCuEEMIwjGAPoVAotdvgqbWuru6pp5565JFHgtRPsKjZ9YEuz3GcOXPmPProo5s2bcp2WdqkkweacDgci8Wi0WjQb7T1EgIAjrcu0kLnmAXDDYiW+2cBQAal1BVXXNGzZ8/0TIHrukOGDEn9uGrVqtra2uAdpq7ra9as2blz57G9tAwat3ueN3r06G9/+9vhcLi+vv6uu+5avXq1lHLbtm1tKZ4QIng2OIYC5KidO3cahpFIJDzPy3rFQ6HQvHnzKisrhw8fnkwmm64gpXRd9+WXX7YsK8jmnH322WeccUYkEtm5c+czzzyzd+/eWCxWVVV1+umnjxo1KrWh67rl5eWTJ08OcjcHDhxYtmxZXV1dLBZbsmTJSSedNHv2bMuyml0/vQCe51VWVjKGDrqehoaG1H9HtstyFDp/oOnbt+/nPve5jEDjuu7w4cOPoQAAgGNzoid0AOBoWZZ10UUXRSKRVtZ5+eWXg3YQQTZB1/W33377yiuvPIbDBYMpOI4zYsSIvLw8IURJSckPf/jDN954Y9KkSSUlJcdQvBNB9+7d9+zZk+1SHKJpmm3bTz75ZK9evfLz85uuYJrmxo0bN2zYEA6HLcuaNGnSl770JSGE53m9e/cuKiq6++67LcvyPG/x4sUjR45MvQP3PK+0tHT27NnJZDLoX3b66ac/8MAD1dXVoVDo7bffPu2007p165Y6UPr66QUIMkrZas0EHD+p/7jc6nDa+QPNqFGjmvbwAgB0sFyKbQDQGaT6vLSkoaFh2bJlQVeaiRMnCiHC4fDcuXPTG0q0XfA0Hg6HH3vssXvvvXfnzp2+70ej0QsuuKDpTXZbioeO5/t+KBTaunXrCy+80GxzISnlpk2bglGTY7HYtGnTlFKWZbmu29jYWFlZOXLkSMdxDMPYvn37gQMH0h9Nfd+3LMu2bcuyEonEoEGDLr30UiGErus1NTUffvhh0yOmOkdomuY4TrAt2Rx0SW3pht8Jdf5Ak1sJMgDoqmihAwBHJxQKPfHEE927dw9+jEajZ511Vvqd92uvvSal9H2/srLyuuuuW7VqlW3bjY2NK1eunDBhwtEebvLkyffff39w9/zmm2/OmzevV69eM2fOnDRpUmlpaevFc1133LhxJ5100rHWFe1A07RwOJxMJiORyIIFC4YMGdLsa+29e/cGzWQqKirKysrSez8ppSorKxcuXKhpWn19fV1dXXl5eUuHsyyrsrKyR48ewQ4z+kqYprlr164//elPvu97nldYWDhr1qy8vLxWhtMG0PE6f6CpqqoqLi4OfjQMg1kUASArSOgAwNHRdf2ZZ55JPQAXFhaeddZZqaWe5z333HPBA/zZZ59dWFg4derUF198MRQKvfTSS8dwn11YWPjrX//617/+dXV1dTCobXV19YMPPvi///u/11133fnnn5/xFje9eMGEIyR0ssvzvOnTp7/55ptBA5ynn356yJAhqbGQU4IBPnzfz8/Pz8vLy3jNHjzXaZoWj8fj8Xgrr+49zysoKCgqKtq9e7cQorq6On2ppml1dXWLFi0SQriuW1ZWNmPGDJp0AZ1N5w80H3/88f333x/8eALOoggAnQRXXgA4apqmpTqtZDyZb926taamRggRjUbPPPNMIcTMmTN939d1fcWKFcEz9tEaMmTIvffee/PNN3fv3r2hocG2bdM0Q6HQfffd99BDD7VSPMMweFbPOsdxhg8fPm3aNMuyDMPYt2/fs88+23p/iqadRFL9oaSUR/xMNU3TNC3YSY72NwHQyQONSOu82TRDDQDoGFx/AeDoBJOPVFRUBO9OMwatnDNnTjBKZXl5+Y4dOzRNSyQS3bp1a2hoCJqyf/GLXzyGg5qmefbZZ0+dOrW6unrBggVz586tr6/Py8t7/vnnv/CFL6SPs5tePCYc6QyUUo7jzJ49e926dcGwx1VVVZqmmaYZtNkJBP0adF1vaGhobGwMh8Opl/NSyv379wshfN+PxWKxWKyVHlJBK57g7833/YzuEsEsV2eeeabnecEYGZFIhKQP0Nl0/kDTt2/fCy+8MCjeiTaLIgB0HiR0AODotDL5SDwef++998LhsBBi9+7d//qv/+r7fjCEihAiHA6//PLLl19+uWmabT+cUmr79u0NDQ3Dhg3TNK2srOzSSy8977zzfvzjH+/Zs0dKuWrVqjPOOKMtxTuheJ7XeUb59X0/EolcccUVf/jDH5LJZDA+TkZDmx49eiildF3ft2/f3r17Bw4cGPS6CobJ+OCDD4Jv8vPzCwsLW0nohMPhDRs27Nq1yzAMy7J69+6dvjSY5erCCy8MZsUKkk0MoIOuLbgUdJ4LQlt0/kAzatSoqVOnfuaKAgA+E7pcAcBRa+kBeP78+akVbNuWUuq6LqW0bTvYpLa2dtWqVRlbBY/xze6wtrb229/+9s0333zrrbdu2rQp9fu8vLzy8vKgYUX66LmCWa4O69evX//+/UeOHHlUTzXHj23bAwYMuPDCC5vN5iilBg4cGDyPJZPJV155xfO8SCRimmZeXt7KlSvXrl1rmqbrun369CkuLk7/Cwwe5EKhUCgUysvLq6mpee6554IGOAUFBSeffHJLz7HB30/QqyIUCnWSEwW0L8Mwhg0b1r9//8rKymyX5eh08kDDiDkA0BnQQgcA2ofv+08++WQ4HFZKlZaWZjw8rF+/vra2NhQKvfzyy+PGjUtfFAqF5s+f37Nnz/SeL57n9erVq7S01HXdcDgciURuu+2266+/fuLEifF4fPHixatWrQqaYPTs2TNjb++9917v3r0zHgZ83+/Zs2csFjsOVe+MevTo0aNHj2yX4lMsyzrrrLM2bdq0ZMmSaDSavshxnAEDBgwbNmzFihWRSGTVqlUPPvjg5MmT8/LyNm7cGOR3NE0zDCP9JbkQQtO0YPZix3GUUvv371+yZMmOHTtM04zH42effXbPnj1t2049yKWvn74fpVQkEhk4cCDZQHQxmqadfvrp2S5Fu+k8gWbjxo1bt27NCDRKKdM0+/TpcxyqDgBoRhdM6EgpTd30fd/13SOv3SE0TdM13fXcLjBOga7pmqY7rn2E1XTD1E3f9+wW1jR0U9d0KaQQwhe+49qpk3PMn6CUMmSEpZSWYyl17D0IpNTCZlgI4bi263s83KCNtm/fvm/fvmg0mkgk7rjjjoEDB6YvXb169c9//vNIJPLee+81NDSkD0ag6/q9996bcVucSCS+9rWvff7zn7/lllu++93vFhUVKaX++Mc/3nPPPUGDi0gk4rpu3759Bw0alL6hruu//e1vm77aTSQSt99++/jx49u52miz4Cp36aWXbt26tbq6On0Y0eB196xZszZs2JBMJk3TXLZsWTDUTpDK0XW9sbHxrLPOGjZsmOM4wfAZQgjTNHfu3Hn33XcHPwY9L3RdTyQSQ4cOnTlzZkbznIz1UxzH6du37y233BIKheiBBXRanSfQrF279jvf+U7TEpaWlj7wwAOkhgGgY3S11pJSSqHEuk3rlq9e0Unaguq6kbStDzeutx1H5Hh4CxmhxmR807aNrcdpXdN37d31xBNPrHx/paE1kzQ0dHNP9e63F7z9wksvvPjKi8tXLnddV0pNfIZPUErp++rNd9549tln44n4MX/6mqZZdvKpZ5587NFHP/p4s6nTBwGfaGxstG3btu1mk7OPPPKIECKZTPbp02fAgAEZS4OBCWzbdl137ty5GTsM2synMwwj+DMePHjwz372s2Qyadt20EbDNE0pZTweLy0tveOOO1J/7a3sjVlIssI5LPUHE8wUftlllymlLMtKH78maKRz9dVXFxQUJBIJIUQwxo2U0nVdy7ImTZp0+eWXK6WCvfm+H+zcdd3gl77vB2Pi6Lo+bdq0r3/963l5eamETtP10wXbZuMkAfiUTh5oHMcJ9ua6btNAo+t6J7n9BoATRFe7vzd184233lz8f0srzxowbtQ427eyWx5DN7d8vHne46+5jvfPt14thVQiV++YDd1c+f7KhU8uNrrrX//m1223xXNr6ObbL7+97Z0dH1ftGPiTQdFoJP2NkKGbGzdvfO6+uXajLQ83f+n2i9I+FX0c1z/mT9DQjS17tyx8ZIlQWnFx8dSpUy0/eQzVDOmh995f9sHcDXqeNuOCotz9vNDupJSTJ09OJBKO4zRNjriuG4lEpkyZYlnWBRdc0DTpaRjGN7/5zWXLlum6XlNTE7TICHbY7OEcx0m1Wp8wYcJDDz30+uuvv//+++vWrSsqKhoyZMi4ceMmTJiQKkmqeC2V33Gcbt26HWPlc5PneVmceEXTtJNOOikajfq+H/SPCH5vWdbo0aMvuOCCqqoqpVRBQUFqkW3bY8aMqaioWLBgwbp16xoaGpRShmH06NFj0qRJY8eODRrsCCGCDfv27ZtqqhP0dCgpKamoqBg+fHj//v2VUqlhL5qun8F13YqKCl6qo0v44iWSAAAgAElEQVTyfV9KmRN/3p080AghKioqJk+e3MqQW8XFxcdScwDAMelqCR0hZPXuaiWVEfqsN/FSakKoVt5YHnEFIYQmtb279tVsPVDSvzjoXtSG40oh5GfpMdTGnbRe/qZLNamtX7Xh4I668p7dWz+6Un6fwb33rtnfe/RJkbTHmNR+3p3/rtVom4Xa8Emn5BflN9Q0mKbpH1rtGD9B3/eL8oq6VZY21iQq+pZ7fjODgB7xtEipJazEqjdXK12NnjWyvKQi6bT4eIwTja7rN954Y0tLDcO49dZbW9/D9OnTp0+fnvpRStnKDjMUFhZecskll1xySdD+oukr0NaLdwJav379okWLZsyY0atXr44/uud5eXl53/zmN4MflVKpGcqDPMvs2bNnzZqVsUgIYdt2eXn5FVdcEY/Ha2trPc+LxWKFhYXBHOep5ja2bU+aNCljPJ3gkVXTtKCdTvqiZtdvyvd9+luhi3Fd98knnywqKjr33HM7/9TanTzQCCGGDRs2bNiwNu4QAHC8dZ2EjhIibISioagZNoQQmq5FzagmNSGE5Vq+8nVN0zXDV77nHXpjKaXUNUNK6Xqur/yQYerScH1XSqFLw7It0wgJTaQP7yKEkFIzDVMKadlWyAhJTTqenX4HLKVm6oYmdSGEoRuGaSitTa08dE039ZDv+7Zrh0MRJZTjOqnsg6Zphm4q5fu+r+tG0NjH89yMzIWuG6ZmuJ7r+37YjHrKdVwnOD9trKBpmLo0bMcSUguHQp5/aA9CCMPUlVRBUUNmWBOaL3zf913PSdXd0A0l1JQzpp566oj8vHwhRKoKwRg3ESNiu7b0xdjpYy678HLHs13fjdtx13Nb+QRbT07puqFJrVtR96u//RXLsQryChzPSc+ftX5uU0JGaNX6lfs/qg4VhMaMH+P4jgA6GaYiaqPNmzebpjlv3ryrrroqWyetpeRIetuZpoJFpmmWl5cHK/u+H0xhnrGTo+okdbTrA11DfX29bdt79uxZvXr16NGjs12c3ECgAYBc0XUSOoZuLKpaVLe/btfGPUr3d23c89zLz7qeZ2jGuNPHFuUX1zXWNiYaTdMsLeimlC+l9Dxv78F9yveKC0pj4diq91dt/2jHkOFDzJBRtXh5/e56M98cOvbkkaeMElIFD/+6pvu+v2L18vVrNzTujYcKzf5D+48eOToSiQR5Il3TlRIfbvpw6+ZtyleDhgz03ebni81gGmZ9vGHFioUfr//YbnDzyqJDhg8ePnS4rume70mpHag9uGfn7lh+rKx72aaPNiUaE5FopN+A/qWFJamBh0NGaHf1ntUrVu3atNt3VUnv4pFjRvTvPcD1HV3T21JBUw99tO2jNSvW1Hx8UNNF937dTh11ap+KPunjE+umnrDiaz94v3p/dWFBYZ+BfSpKKxzPDkYj3lOzS0kRnAqn3iopKA220jQtnkzMf3uB67v1u+qV7m9fv+PJuX9zXS8SiYw7bVxBLL+1TzCvqNlGN0IIKbX9tfscx1ZSaFJKqemGHjZDqUeX1s9t2n6k4zpVb60Qvhw8aVCP0h6WcyydtgB0BmVl/5+99w6L68jzvavqhM4N3dDkICQRBEgggiSUg5XlcdiR42g8O+uxx55ZT1rPzr37vu/c3Wefvb7vvTu79+473tm1ZxxmLI2jHCTZskAJBQQiGSQRBRiRaaDpfM6pqvePkttYggbbssC4Pn/B6VNVv6rq5/Q53/MLjsHBQUEQvqYqRnjRh8PhzBCWGDgUrsjhcDgcznxiHgk6SKw9VTd+2Yf1KhWps2tktM0FAIAUZuSmx0bGnbpwquL1i7EFUX/12F8pWhBB5Al4XvvNm/5R/72/ujN/UUHrR22tJ69ea+xx9o5ABVFEAaSdF7rH9o5t3rRZ0RQIkaZp775+qPVsOySQIgop7LrQ3Zbbfs8jd5sMRkKppmmH3jrcXN4KCIQUXhRqzdFGKkzzOCEIonPM+dbv3xludwIKAASAgrbTV1tXt39r7x4kCJIgdbReLX3hlM4mmSJMI12jgAKAqNlh3vadLVmLs4KaohPlpramI78/GhwLsvF6G/qbT7Rt+u764uXFAIBpJyiLclVtVdmLp4hCWHxYT11//XuXNn53bcnK6476FNHxPveL/99Lwy1jAFCAqGzWbX54Q8Gy5QDAtu7Wg88cpgIBiAKC4vKi2WoDACCAqqpWvlFNNUpkTEXac6W376MBQAEU4bL8ZZIgh9lBu8U+laAjCdI7r7w73DBGRUIRhRj9xd/emZWSzcaddm1DfjqSKLd0tPRc6hMNQmFJ4VTDcTgcDofD+bowsYbm7FrC4XA4HM4tZ/4IOhpWV25e4S3wNde0DF4dilnoyCrK1DRNgMhqsmKKWfoUiD7zcw4RAJBCACmlgoSISIZ7nFGp9qyiTILxR6cbvSO+6iP1ufm5UZHRIhLLyktbz7YjPSzaU5CantzfM1jxVmVPY1/5ifLde3aLEJadLm0+3UYFGr3YHpca2981MHzVGT55DoSQEvr+60eHrw5LEVLOmiVmq7mnvedqTWfr2fazCWe3bL6DUgoQpALxewIBdyAxL0EQUe+Vfvew+73/eN/6y4jEmMSR8ZH3X/owMB6IXxpfsHmZLOtqTtZ21nSfPHA6JTU50ZEUfoIOmyMQDFQdrSEazrszN2d5TiAYbKpuGmwfiomPJRQLUAQAAAjGe9wAwZSiRKyR3it9QV/g1KvlCxYsiI6M1un0kYssQKT+kWBgJDhxtQmlelm37qE1GGt15R+5+90puckLslM1TZNlnV7WKZoSZgfDlDCngNgT7aofU4LH+zyU0FC6opmsLXPDgRBSTGpO1QAMFqxMSXAkhOLIOJxvOO7guEVnnW0rOBwOhzNvGQ+6TLJZgHM9yRGHw+HMNeaPoIMJLlhWqJf0oyMjQy3OmAXRd2y6I6gFAaAqVqdKZHDD6xpIgcFuvO8H33bYYhBEcQvi3vk/hxSf0j/QHxcV73KPNZy6DCDd/J2Nd6zeqhK1KENGEJ166UxHbZd/q1/VlPqyRgpp9oasb93zLUEQMMaH3znSePxSGMtFQfy4/+Puj64BBLbt21K0tFgjGllH3jIcbC5vuXS2aeWqlRajBQAAKNAbdLse3ZGdvgQA2NLR/O5/HAqOq7WVtQvvXnipodE/HLAtjNz32MMRpkgIwOKU9N/1/oe713u15WpKTOo0E7THYUJYgJjOqE+LX6iX9VmpWd6A16A3aFgVPilALkrinh/uXJq5jFJaUXO+7MWTvjF/T981u9WeHJP82C8e1Ym6srKyc69VTpwmpUSW5TVrSnSi/mpbu+eaNzUreeIeqVj9AjsIAFA19a477xIFYdw9/uL//KPX6f1ca6vT6QghoiB+3NfdWfsxQHT5uuVIQIAnBuVwAAAA/Hvl/xn0DPxq/f8TbXLMti0cDofDmYeUth19r+ng3295JiUydbZt4XA4nK8T80fQAQCwNC7syZ8QEtSCYUprTw6BUQttDpvDr/gEJCTEJBisBt+IL+AOClAYcY/4RwNUpAPdA28efgNjIorIPeqhIvGP+70Bj8vr8o35RZ1QvK5IEAVFDeolfWJaQiMNJ+hAgAauDQIMbWkRSxYv8as+QohO0i8ryW0+2+pz+kbGRyLNNgAABMBsNy9OXawRjVK6ZFH2lRVXLpU2917tUzW1/9oARVQQhZPlJzVVAwCIkgAFSCEdHnBOO0FCqclgyl2ffe5AZeXrF9urrmavycrJzY2OjA6qny4jJDBqUWR2ek5QCyAkLMnMvmC/6Bny+McD4BPHZjJF6k1KqaIpAEBCKAAAYzxxj+CX2EFKCaGI3DToTNY2KTaJEIKAcLH8IlFo0vLEhclpqqZMOhCH8w3EKBlPXC2t6D7zi7X/dU/mXZIwed1rDofD4XC+GEbJ1NBfd+/+HXtzH3qq5BcGyTjbFnE4HM7Xg3kl6NwSLBYz/sQZhFJ63YUHAgSRL+jDGqYCbTh6BZLrrj0UUiBA1adhTMad45ACvVlvMVpYjmRC6UyS8LnH3IACQ5ROr9MH1AAAgFBsNBkFCWkK9gQ8rNgTG1DDmiRIlFJMcFxS/CXYpHm0oBJ0uccABENXh53No6GeqUAgQUogGPJFmmqCAAAVK2vWrDWZTVVHq50do+VXz1fZapZtyV23bi0KVfqkQNCLCCGKKSFEEiTZIId6ALNYSIVSACYZd9q1hQCJgtQ33Hv1YieFtHD9ckEQsfo5pUAOZz4DRSSKSHrm1D+8VPP8z9f+al3qRp6NgsPhcDi3Diog0SAZ3ms6WNp+9Gerf7ktfZeI+HMKh8PhTMM37kKJEEQwlGAFhT95IoQSvayHEAIIl+9earKYMCaABW1RKsmyzWLrl/opAJqiqUQDn4yC0I2jsHLplJJQ2l2j2QAgUNyaqmkAQkAphEhRFKwRQUQG2UA+LbAN4af2Q01VAQAAAgih2WSBdDh6UVT2imxVuZ7/BQmIqCRpYZI6g4wwTN8pKV6dvSSntaOl/nTDtcaeyjeqVVXduWPHxNNCkg2dQkb56kAIIShgos1QNpp2bQGgIhLrLtarbi12iSNjUWaoTDuHw5mIQTKMBUZ/fuRHa1LW/2Ltf5njjvGapvGiNhwOBwDALgX8gvC1QESiipW/P/53z1989tdb/nte3PLZtojD4XDmNPNQ0Ln+mA+hLMoUUAhAqKo3gFQZU1VNEwRRQmJQDSh+hc7sNTOhJMIYoTPrguOB6ATHplWbAmoAQqhhDQBAAQWARkZGIAEFPMGOq1cTitcqSNEJupC2EgJBNDg6YNAZzAYzJhgAGhUfBSAd7Rzr6unMTMtSiSohqam2GWCqjzREWmyYXr8LIYQISJBEiRCCILrW1QsoNEYZDTpDdHRUO+0kGi1ZVWLSmzSsQYgUNSCKkqIFZ1KziUlFAyMDjkhH8bIVRbnFZ6rKj79wqvls65q1q21W+0x6QEgQBREhgf0rCiKmmFJCCAl9ygZif2OKCcET1ZkwOyggwR/0j/vGHZExEH5aukJAgiCIgnD9+4yE6z0DCKZZW7MNQDg8NnTlbDOAYPmGPFmSebVyDicMFtlS01s59x3jU1NTvV6v1WqVJGm2beFwOLOGKIqZmZmBQGDRokWzbQtnphgkw4h/5LGD+zYt3PpUyS8SrEmzbRGHw+HMUeahoAMBoJD2NPVe6bgsydLI4EhWZhaE0Gq3UghGPh6rrr+Yl5sXwP6zJ84pAQWEr0H1CZhgu9W+uHjBpdLmU6+WS5K4IG2Bx+spP3I2Ns2xYd0GQml8VELM4uj+lsFTfy4PeIOOWMfoyOiFo5UUfapWSKJUWV154uVya4z53h/e7bDHqFhLjku2p9qdH48cfvn9wW2DEZGRne2ddaUfAQrTClJt5kiWVoZCMD44fuLkiYIVyxESLjdculrVAQDIWp5BAc1amlV9pM7ZNfrmgTc37Fovy3JzU3NzZeuOB7ZFR0ZPv24QAgBPnDzRdKK16M7l6VnpsigpigIoQDISJpT3DtODijWvx6UTZb/PDyDAijYy7gxqik6SDToDxtjtdQuCgBUNQOD3+dmnJoNJEsRPC4tOtoOCIEAIPX7PG78/ONQ6VHR3webNm1khKgjhuM9NCPF5vYQQAIHH7XGOD2OMzUZzclxKuLW1REKAPqpv8A8HIlOs2ZnZKubZcziccFBABSSaZct7TQePtb3/szW/2j4nHeNjY2NjY2Nn2woOhzPLIIRKSkpm2wrOF8EgGc90nTp+9diDy7775MqndKJ+ti3icDicOcecuwX/8sSnxF+hba6+8T//jzcgRvF5jvylyzWiLVi4QG/RBbyBD188XpNQH/QHvcNegAAkkFAKISQagRgS7VPZglKKFQwxpCyJLyBrt6zrbeofveY6/LujslFS/ArU0LWGnpzcnGi7QxDQ+rvWvvmbd4JetfzAWQoApJAiCgHEynUHGQSFS1WXiUrGrrm7P74WH50QxAGDzrDh3rXv/vawu89z/KVTlIlMFMQscmy8Y6NGtFCFKUxx9dt11YdqBVnQ/BhSGJ8bl7csz6/6EmMTV9xVdO7VC23nOtqqroqyqPk0qKHaBXXbd26fdoIQQKxpg+1DHqfn5Evlp/TlCCHsx4Cg7NWZJqOZUHq9B/Uzzj6hHmRBbhloPvib96AEFEWhIhhoGvqPv3+eqmDlXUWbNm8a9gz9+V9f97g8qqoCBGo+qGs4fomq4O6/2ZORnBnKfzzpDipaUBLkgZGBgSuDANEr55tZZh9KiSTIh998ta9+iApECaoAgQ+fL0PohMlieuCpvdE2R5i1JYB6fa6PTjUCCJZtzDUZzAHV/xV+OzlzCZ4FZoagKaJTRSRqRPuH43/3e+4Yz+FwOJMx1fWTcwNTpUEQkSgi8c1Lfz7W9v5PVz99x+IdfEk5HA5nIvNN0FGxmpefN3LnaFtVO1aJIAkZ+RkUEIy1KGvUtr/cXPbyKd+of6RrFMpgyfrMsTGX3+XXyTpMsDnaErHQao62sKQwFFAkCPa0SJ/LbzDpAaAYazar7b4f7T1/+vzV+k7Nq5ntprj0uKL1BfbIKIw1DEB6avq9P/3WhWOVzmujlNCoVHtsckx7Y3ukI5I9PBKKV25Zcbz/VESCJT09nfmYKJqStWiJ/DP5QlnlUKeTaEQ0CGl5C9ZuXGMxWUIlwyEF9gR7RkH6R2calXHFEmNaWJC2duNaSZIx1hSqrl+3LjIqsra8fqx3jGJiWWBesjKrsLhQI5oExfATxEQTJfHe795dteRi88Vmz5APAGCNteSsyl65aqWqqaIgsB4i422hvDkQAltKJNRBg0lPKIEQiDqRImLUGSGElFKCCYuzAgAgQdA7dNigmgQD+CQXD8RIEIRQh1PtIPsoyZGUvm5hf9Pgil2Fsix/kuyGIgEJsgAEJOklCCHBhBIqyiJCghp2bQWIGi83evo8hihDztJc7p7zzQFCgCkW59018KsgoAXCiF8hx/gNaVt+uvqXCdbE22nbNxMIoSiKhJA5khNEEISJcW0QwmAwSMg0Tp0zASGEENI07ct0IkkSpfRLdnJ7EARBEARVVW9nbQEIoSzLCKEvv2uSJEmShDEOBnlhAQAAgBAGtKBRMs22IV8DVKKG+aERkehTvf/12N+8dfm1p9f93SJ7+u20jcPhcOYy8NelvzrZUeZX/X+/5b/vyNhz2wamlDYM1GtEQ7f6JTmESBREj9etqposSwa9IZQ+Rhbl4bHhawPXMMExtpjEmCQKCL0uLFAIEYSAUjAxtuiTg/Qz6VqQ4Av4A4GAJIkmoxlCOLHKtSRKGBOP10MpsZgswvUkMjTUrSCIPr9PlmRBQBNvniRRpoS4fR5NVQ0Go1FvwAQz42VRV3mxsvSF4/YU+6M//75f9Y+7XVaz1WKyhM4BAEAIJUFSsebzeQkhRqNRJ+k1orJRZjJBhJCIpKAa9Hq9AACTyaSTZBVrrMm0PWBCAoFJEtDIkiTL8ieLfMOO0xsKY4XZQQgRoDQQDJiMZu2TNM8QQn/Az3JUTwRBqNfr2XCTri2hFGPtxf/98kjH2IpvF27bso2759xmCKUiEpfG5t02ZxkVq3e/ssOruCP1tvToTJWo08YSfsNBUGgZbvIqnmnP1IimYOXBZd99YuVT+s86xldeO//X7z0GANi3/Ps/XvWzr8rWL83g4ODcf+yHEEqS1NnZCSFMSkqadU1HFMW2trb6+npZvl7PXtO0NWvWxMTEfHkhRlXVoaGh6OjoL3yJkCSpu7tbUZQFCxbcEo3pqwMh5Ha7P/roo8zMTIfDcXt2lr16OX36tNPp3LFjh8lk+sKrJMtyTU1NRUVFXFzc7t27EUJfqSxFKY2Pj7+57sRcgFL68Ot/0Tt+DQCwyJ5u1UcQOie01zkLgkKv+9qAuz/8aRBAjah+zb8z/c6/Lvl5jDlu4qcBzb/1D2sFJCRYk17Z+yZ3wuXcNt59990XX3wRAPDrX/86Ly9vts3hfFPYX//S/z73vwySYR6+naaUqJpiMBiMBkgonZgMWNEUm9XmsMVAADWihTKwsHsOSgkA8Kb7D0opmHiQCSiSJOlkmQKq3VQ9StVUCKHZbIIAEkpUrISGuN4D1vQ6PQD0htsmpgqZjEYIIKFU0SbxFiGUKJpiNBhNBhOh+IZzKKWKpkAITabro4fimGY4QUKIQoIIwQirNTRc+B4mHhQFwWI232z2BA1okqLmN3c41Q5SSiCEBoNh4rJTSg1646Q/3KEVnnRtZVFXXVM91jouWsTlhfkq4cWtvkEQSur7aoKYv0aeHjizRGPMMf6tS6/+sfb3f7rvzeyY3K/asPB4PJ5r166ZTKbk5OTZteQWwn5N3njjjRMnTtx///0LFiyYdUEHAGA2m8+ePet0OpmDRjAYzMrKio+P/zKCjiiKHR0db731lizLTz31lKJ8EfdJWZbff//9Q4cO7dixIz09fS67jYii6HQ6//3f/31gYOCXv/wlQuj27KwkSVevXn3ttde8Xm9UVNS2bdsmfSszLQghn893+PDhK1eufPvb39br9XNqtTs6OoLBYGpqqsFguM1Dt4+00ttbDPRrykx+aEIZ3E52lL195Y3/tfPftqfvvg22cTgczlxmHgo6jKleMU30Z2F8tr7SNFrDhOMET/0DfYPLyWTdTvkGbCrLKaEQIxGJCEJCSJgebhj9ho+mPcIO4ineJk11/rRDh2k+KVOuw2RDUEpm0vENfWpEjY6L2vqTjWaLJdISifFcfzPPuYVAADElnuD0jicco2QUkTiTZxKVqJjg/2vzP84Ff/iKioqenh6M8b59++ZCoSv2uniqa2D4TyeepqrqpUuXfD6fIAhfuJ8vzM39a5qWkJDw4IMPdnR0+P3++vp6AEAYv4kZWigIwuXLl2tra4uLi7/wm3YI4aVLlzwejyjO6G7nlqzeF9toCKHP5xseHpZlOcx8p7Xw804BYxwREbFw4cKRkZEwDl/Tdsvccz7++OOUlJT169fPBZ0xhMvlOnHiBADA4/EUFRXdzqEhgF7VO5Myo5zP9UOjaMoPin9UkrL2NhjG4XA4c5x5K+jMMyggsk7K3ppRuLZQkEQeJHJLwIQsSl4sQOFmXyfOvIcA8od791t11tk25GvAb87+j7L2o7IghzmHUuJVvA/lPfL9oscj9bbbZlsYDAaDKIpfddxHGCCEOp2OZW9hiUUwxjqdTtO0ia4rLAENIURVVb1eTylVFOUGmwVBEEURQogQIoRIknSDYsLSoLDkNexTRVFmEjvD0vGwx3WmFiGEQkcIISFjwtipKEpxcfHatWu7uroaGhomXfAvYKEgCDeoG8ywUEIcZiohJLSeEEJWElHTNGYGG4vFqYUmpWnaxKHD2MaGYOewhpIkMSmNmaGqqizLoiiqqspGZ51ACG/YR1EUWRAZIUSv17O27COEkMFg0Ov1rGedTse+vRPPCdOcIUmSKIrBYJBN5+YTboatZ3R09E9+8hNFUaxW681NQt0ihJgBNztescmePXtWUZQVK1bExMR8MTefrwi2dGA2EuEHcfCFe/fzktsz4fXGAy/WPDftD41f8+9I3/PjVT+PMfMihhwOhwMAF3S+Lqiamp2dnbcsHwBwc5AX54sBAVA1ha/mNxNCSVJEsgAn8XHg3ECiJUkj2lT32ewOOy+u4O/veCbBMocyIhuNxlnMmSIIgsvlOnLkiMFgKCgoqK+vb25uVlU1KSlp3bp1DoeDPTlLkuTxeCoqKtrb2wOBQERExNKlS/Py8gRBCPk4yLLsdDobGxuHh4ejoqIyMjJuUHMEQSCEVFVVNTQ0jI2NGY3GzMzM4uJig8EQPugJQogxHhwcHB0dxRi73e6lS5cqilJTU9PX1yfL8sKFC/Py8kRRFEUxvJ2apjEZZarV+GIWTjRVEITBwcFAIIAQio2NZRlnxsfH9Xq93W6nlLLpDA0NaZpmt9t1Ol2oOUKora2toaEBY5ycnJyTk8PkkvC2YYw9Hs/Q0JDP51MURa/X5+Tk1NbWtra2er1eh8ORl5eXnJxcXV3d3t6el5cnSdK5c+eGh4eNRmN+fn5hYSEhhGk6siz39/dXVVV1dnYSQmJjY4uLixctWqSqKpvXoUOHvF4vO7m0tNRqtbK8P8uXL9c0LUzzkG7V3t5+8eLF/v5+llypsLAwOTk5jKcMhHBoaIgJQOwbJQgCkyBDJ4ii2NLScvHiRafTiRBKTU0tLi6Oi4u7IQJOluWGhoaWlha73b5q1ao55Z4DAAhld7r9go5GtIX2dIN0u+O8vo4ssi+e9ocmJTLtb9f/38WJK2+zbRwOhzOX4YLO1waEEJdyOJxbBySETBq0wrkBjWqTZjeAAPpUX7wl4Z/W/d3qlHVzLQPlbDnmMJjccPToUYPBUFVV1drayr5vDQ0NjY2NTz75pN1uhxA6nc7f//73zc3N7BkYQnjhwoWVK1c+9NBDTGiQZfny5ct/+tOfmE4BAIiNjZ341WVFoPbv319RUeH3+5lrRmVlZX19/fe//32j0Rjm6Roh5HK5/u3f/m1wcFCv1xNCduzYcfHixe7ubgCAJEkVFRUJCQlpaWkDAwPh7Qy/FF/YQgaEUK/Xl5eX79+/X1GU++67LzExUZKkY8eOvfrqq8uXL//Zz37GXEjGx8efffbZ3t7ep59+Ojs7mzWXJKmysvLQoUPj4+PMzWTZsmX79u1jCYDD2Gaz2Y4ePfr666+zxUlPT29oaCgrK1NVlTkrjYyMPPbYYw0NDSdOnGhvbx8YGHA6naxSVXV1tdPp3Llzp6IosixfunTp5ZdfHhgYAAAwFez8+fMPPPBASUkJQmhoaOjAgQMmk8lsNgMAysrKWKGoLVu2FBUVIYTCNGf9nzt37sCBA263m9UfqK6uLi0tvf/++zds2DCVn44sy3/84x8bGxv1ej3zwfn5z3+enRGkhcEAACAASURBVJ0dyn0jSVJpaenBgwdDSlNtbe3Zs2f37duXk5MzUdMhhJw+fdrn861ZsyYxMXFOZc8Bs3opgABiyqO5Z4SK1anS6AS1oFm2/GrDr7cu3iki/uTC4XA4n4FfFr82zO7DCYfD4UxEJaqC1afX/td7svdKwuxnqJmDMBnC7/f39/dv3bo1Nja2s7Ozrq6uu7u7vLz829/+tqIor7/+enNzs8PhKC4utlqtHR0d9fX1Z86ciY2N3bNnj6qqIyMj+/fvHxwctNlsS5YsoZRevnzZ7/eH5DNZlg8fPlxeXh4ZGblnz57Fixf39PR88MEH9fX1R48e3bt3LyFkqgwyLJ4oISFBr9ePj49rmvbhhx8aDIbt27dLknTmzBkWrEQICW9n+PiaaS0ML+iwyLWysrJXXnmFEPLAAw9s3ryZeaYw15IblERW6fyGHrq7u+Pj41esWDEyMtLS0lJdXR0ZGfnwww9LkhTGtoceeshqtaalpWmaNjY21tPTc/Xq1SVLlmRnZ1+6dKm5uZkF9ImiqNfrOzs7U1NTd+zYgTGuqKgYHBw8fvx4YWFhbGzsyMjIgQMHhoeH8/Ly1q1bp9PpTp8+XVdX99Zbb6WlpcXHx8fExDzyyCNer/fMmTMAgJ07d0ZERCiKwvJ5j46OhmkeFxfn9/tPnDjh8/l2795dUFAQCARqa2u7urri4+PDaG2U0piYmNTUVEEQRkZGbna6uXz58sGDBzHGy5cvz8rKCgQCVVVV/f39Bw4c+MUvfmG1WtnGybLc2tp65cqViIiIkpISfq/CuYWwYN4Hlu374cqnzPIkNTc4HA6HwwUdDofD4XwOKCUexbM396HHVvzIboiabXPmOpqm7dy5895778UYa5r27LPP1tbWtrW1UUqvXbt2+fJlg8Gwd+/ekpISlmTn5ZdfPn369MWLF9evXx8REVFZWdnX12e32x9//PGMjAwAQGtr63PPPed0OgEACKHR0dELFy4ghO69995du3apqlpSUiIIwp/+9KfLly97PB6EUF9f36T+UxBCu93+4x//WFGU3/zmN11dXTab7bHHHsvOzr569erJkycBAKIodnd3h7eTObBMOn2E0NjYWBgL3W53mObMgDNnzrzyyisAgO9973slJSXBYPBzqQaqqq5cuZK55FBK33333UOHDtXW1m7dutVisYSxbWRkZM2aNZs2bSovL3/ppZdUVd20adPevXvNZrPT6aytrQ3FixFCYmJiHn/8cRYLlpKS8p//+Z9MA0pOTq6tre3p6cnIyPjxj39ss9kAAFlZWf/0T//U1dXV3NwcHx8fFRV19913d3V1nTt3DgCwdu3a1NRUVVWZYhK+eWJiYiiLkMlkSk9P1+l0OTk5Xq83fESboigPPvigKIpjY2P/8i//4vF8JkM8c8Ly+Xx5eXlPPPGEXq9HCOXk5Pzud7/r6+v76KOPNm7cGHLXOnv2rNvtXrly5cKFC6dN3MPhzAQWY7U8vujXW/5pTgXzcjgczlzjGyToyJIOgU/f2hGKg5pyyyMEIISSIGFKpiqZBCGURR2EMKgG519uYwEJEPLQMA5nfsLusLMcOf94x/+bErlgts35eoAQysrK0jQtGAzq9fpFixYxIUBV1d7eXq/Xm56evnTpUr/fz5Ldrly5sqKiYnR0dGRkxGazsVit3NzczMxMv9+PEEpKSoqIiBgaGgIAMN+KsbExk8nU09Ozf/9+jLEgCGNjYzqdzu12+/3+kZGRZ555Rq/X32AYi+f6xS9+kZaWxmJkNE0rKirKzMxkJbSWLVsGADAYDE1NTWHsdDqdKSkpUyky01rocrlY6NOkzSVJ6urqamlpYbmH9Xo9S4r8ubaAUpqWlma1Wn0+nyRJq1evZh40PT09cXFx09rGSisSQmw22+bNmwVB8Pl8CQkJLEkNs5yV+oqJifH5fKIoJiUlRUZG9vX1eb1eAEB3dzeLwzp27FgodxJzL+rv72d7EQwGQ1KIqqqhfwVBCN+cEGI2m1etWnXt2rW33367vr6+uLi4sLAwOjp62tCn0NRuOI4Q8nq9vb29CKGVK1caDAa/3w8ASE9PT0tLczqdXV1d7ExZlj/++OO6ujqj0bh+/fpZzEE+E+aybZwQczyYl8PhcOYa3whBB0KkaerJcycCgSBEEABANGKPtRXlF9/aStUQQkBB89Vmr8e3LHfpzTdJEEJC6Olzp1wjrnUb1ptmNWfnLUcWZbffMzg8kJKQwm+bOJx5RlAL2g1R/+2OZzYs2IzglEWp5w7s6jq7+VkppQaDQafTMWNuuDCOjY1RSs1ms9FoZA/MGGP2r8vl8nq9gUDA7XYjhCbGzmCMJ6at9fl8Pp9Pr9d/+OGHIXcMhFCo2JMoihaLJZQXdqJtrKITe6pnB2NjY1kRLrvd/uijjwIAJElyOp3h7QxTpBwhFN7CaeOtXC6XzWaLj49va2t7//33MzIyZFn+vNvKvIrYHyaTyWKxDAwMqKo6E9vY4hBCIiIiTCYTq5C1YcOGTZs2TSywFREREdplQkiocBgAYGRkRBTFjo6OS5cuhUySZVlV1ZlUg5q2uaIoW7ZsMZvNZWVlra2tzc3NpaWl69at27JlC6sCFqbzqUqS+Xy+QCAAIYyKigr1ACFkLkLMQYwdqaioGBsby8/Pz8zMvCFua04xqXTFmWvwYF4Oh8P5vHwjBB1KiV42uEc9lw43UUSpQABG0UsjVy5fhcGtFHQkQTp56uS5A1XpG9IKlhUo5MaXY6Igdg12nXnpPKAoMsK2bt26IJlDpT2/DKIgfXTlo7NvVIjR6AdP/EDR5lZORA6H84Xxql6v6ntixV//ZeFjRsk42+bMFJa/pqSk5GYtY45gMpkAAMFgUFEU5njCyj8HAgGj0chS1QqCQCn1+Xwh0QRCGHplTSnV6/WsnNOuXbssFksoCoYQotPpzGaz1Wr9m7/5m6necttsthtqqId6Zl2JojitnWEU/GkttNls7AiTUULlxhnML+bRRx+VJOmf//mfWSGnDRs2TBR0Ji7IzSl1QsdDJ2OMmZ/LDG2bdOUJITNXBywWi6ZpGRkZhYWFrKoUM0lRlPT09GnFqWmbsx3ZsGFDfn7+5cuXz58/39TU9OabbyqKcs899zCRhZUJC21reCilOp1OkiRKqcfjmbikzOfIarUCAERRHBoaqq6ulmV5/fr1kiTNtXTIDLZWRqMxNzd3tm3hTEkQB8eD448s/ysezMvhcDifi3kr6ECImDcx+5dQvHbzGgEKFNCuyx+PdbtEXbi539B8xp/C4X4ngFSUJy+dQwixmqz2hTbviD8myUHo5PdVX3T0W3bCtEAIAYATQ8YQRM31LWM9rtj46C/cLYfDmYOsTFq1L+97Cdak2Tbk85GdnZ2WlsbEiLlJbGysLMss1W5OTg6rnVRXVxcIBBISEmw2myAIDoejubm5qanJ5/MZjUYAAPOgYT0wtxGLxTI0NJSQkLBt2zYWlsVOoJSyh/nExCkzUDDBQhTFkEzA6jeFhBVKaVxcXBg77XY7xpiVNg/pQYIgiKKIMZ6Jhaxol9/vd7vdDocDTHAb0TQtKSmJxaytWLGitLT0xIkT+fn5bCkAABBCv9+vqiozIBgMer3emzWdYDDIyj/pdLrW1tbh4WFJkqxWq9VqnXb1RFFkmg6EUJIkSZJYOqSZb3R8fDxzEdq4cSPz8UEIBYNBpoDc0BXznGJBVUx8mbY5U9kGBwejo6PXrFlTUlJy/PjxP/7xj7W1tZs2bWJCFUJocHDQYDCYzeaQpsO26YZdYy5IFovFZrN1dHTU1dUVFRXpdDpRFNl3gJVFZytTUVExMDCQmZmZnZ09Z7PniKL48MMPC4IgSdzjY+6SZlv43r5ji6MyZtsQDofD+Zox3wQdCJEkShBARVEkUYYIqlghhGCCzUbLzjt3yqL8Bn59rGt80uaiIIlIpJQG1aAkSgJCKlYx+VR2kURJRGJQUSBEkixpWGP5YigAOlE2yAZJJwIAkIAMsoFFJQS167lyBEGEAEZFRD/yk30BJWg1WxVNnXjXyfLvICgoalAQJAEJKlZmMnr4uc9kdgghAQkQQAAhpUTDmiRICAkQQEqpStRQbJqABEmQMcEYazrJQChWscpuvkVJoJCy3ljGIgIIO/NLbiuHw5lFNqbdMdsmfBEQQnNZzVFVdcGCBQsWLGhraztw4MCmTZtYxpzTp09TSrOzs5nvTH5+fmVlZVdX1x/+8IfVq1dDCGtrawcGBljhKoxxVFRUTk5OWVnZwYMHJUlavHixx+M5cuRISkrKtm3bAACU0qnUByYZeDyeYDDInvlHR0e7u7uDwaDdbtfpdKxtampqeDv9fr/X6xUEweVysW7dbrfT6VRV1WQyTWuhIAhut/sPf/hDe3v7rl27du7cOdFgZgPGePPmzfX19V1dXRcuXNi2bRulNDIyUhCEnp6eCxcuFBYW+v3+srIylgd64jRZWmVJkpKTk91ud2lpqc/nS05OZtmIwtvGYrKYSKSqak9PjyiKkiTZ7fYZvhQhhCxbtqy0tLSjo+PFF1/cs2ePLMuNjY01NTX3338/E7Am7ggrJsXmZbfb09LSwjdnfkMffPDB2bNnd+zYkZ2dzaKxwCcCDaVUluUzZ8689tprDofj0UcfZYF1bJsIIePj4yxGbOKuybJcVFT00Ucf1dbWvvzyy3l5eT6f7/Tp006nMyIigrm6hBJyr1mzxmg0ziR8bLa4OYcUZ66xLG75bJvA4XA4X0vmlaCDEAIE1F+qa7nU6h3wyRFSWuaCZUvz9Ho9xhqlRMUKc6WetDmEaMDZ39LU2tvdGxgK6qxyXFpcQcFyqzlCxSoEQBLkzu6OxrrGkWujQICO1KjcpbmJcUmYaKIgXqi94HKO97cPUIH0tw+8d/RdjLEAxYIVyyNMEYQSp2tI0VTwiU+4GBR0km5CKgQkQHSl7UpTQ9N4v1cyCKHRmWoTZvRp5x5+dphoHr9ndGzU5/ZjTRP1UtbCzIamxs72Tp/fG22PzsrNio2OJYRIouxyj9XX1/e09ap+bHIYsvOysxZlYvCp6iRIQiAYuNJ8eXjIabVaU9KSY2yxKp67cfUcDofzVUApDYX2hA4SQlRVZf4vJpPpzjvvfP755zs7O19++WWEEAufyczMZKIG0wKKiorOnTtXU1NTV1fHQmZ0Op2qquy3jBCyffv29vb2jo6O5557LiIiwu/3u1yu2NjY/Pz8mJiYML4kCKHx8fFnn32WVa0WRfGdd955++23g8Hg008/nZubGwwGCSEGgyGMnRDC4eHhZ599lpUSDwaDgiDs37+fOfs8+eSTKSkp4S0UBKG/v7+hoQFCePHixTvuuIMpMqG1AgBompaYmLh69eqDBw9++OGHy5Yti42NTU9Pj4qKcjqdf/7zn0+dOuX3+3t7eyVJUhRloo8Pxnh8fPz1119nMUSsjvvWrVutVquqqmFsS0pKOn78+JEjRyCEoij29fU988wzgUAgNzf36aefDoUXsRiuG0KZWN5r5uuUnJy8Y8eON9988+zZsw0NDZIkjY2NBQKB5ORkVv6MdWK32202m8vlOnz48JEjR1RVffrppyml4Zuzr1lXV1dvb+/LL78cERHBlDVCSEFBgcViCQaDCKGqqiqW5rmzszMxMVHTNFmWn3/++ebmZkmS/H6/KIr79+8HANhstieeeEKW5cLCwoaGhgsXLpw4caK8vJx992RZvuuuuxITExFCNTU1vb29ycnJ+fn5c9Y9h8PhcDic+c38EXQgRAST99441FzeBgmkiEIKO89/3LK0/d5H7jbqDRNdXW5GEqVLTZcO/fsHRCGQQooooKDzQndb1dX7f7jXbDQJSKiqvVj24kmiEAABoKCnpq/u3cZN3123akUJQqj6ZM34ZR/Wq1Skw50jI60uAACkMD1nsd1iF4D49v53hxvGqIApohCjv/jbb2WlZLNcMxBCAaJjH5ZePFQLMWT9d1Z2N59rvffxu6JtDgGiMKNjqoWfO0IozOzsVvvp46cr36whAoEURmXYWlNaLx9rAhRSRNvpx2PDrr+47y8oIn2DvQefe8fV4wYUAAgAAM0n2kq+vWLjhg3sX4roeJ/7xd++NNw8CgAFiOrM+i37NuTn5isa13Q4HM43BRY4w2KdmI7ADlosluTk5NjYWJaGJicn58knnzx27Fhvby/L27JkyZJt27ZZrVYmZCCEHnzwwejo6Lq6OhY3lJeX19/f39vbywowsQTGTz75ZGlpaVNTUyAQsFgsS5cu3bhxY3R09LSRQQghi8XCakiFDiqKMjEzzkzsFASBEIIQYq4QLMUMi+WZ1kJCSEpKyrp161paWrZs2cIcTEJr5XA4mCWapq1fv769vX1kZKSpqSkmJiY6Ovr+++9/7bXXhoeHm5ubrVbrhg0bnE6n0+lk7kUAAIfDkZCQkJ+f73K52traAAB2u33Tpk0FBQVMkQlvm16vt1gsOp0uVL9JUZSQSWxPbTZbcnKyzWYLHUQIxcXFMR8xJrhs3brVbreXl5cPDQ1RShcsWFBYWLh69eqQDkIIMZlM99133zvvvDM6OgoAiI2NDa1PmObsm/a9730vPT29traWtU1JSVmxYsWGDRtY1BjGeMuWLU6nMyYmJisrKzQoK54lSRJLJMTkJxZ/RykVBOE73/lOYmJiTU2Nz+eDEEZHR2/cuHH58uUYY5/Pd+7cOUrpihUrIiMjWbZsDofD4XA4t5n5I+jIonz8ZFlzeRvUgaLd+SnpKQM9gxVvV/Y09JafOL1r9+7wgg6lwGyxGEz6xFXxacsWmC3mvq6+ineqhq8662vrN67f4Av4qo5WEw0v25OTszw7EAg2VTcPXR12xDkIxYSQFZtXePO9zXUtQ1eHHQujMwsyMMYIIqvJqhFNRKItPlL1aIQSd7+HEgDBp+FWkiA1Nl26+F4tQDQ+N25hbpp7zP3RycaxzvFTh0/f/937/WFHlwT5eHm4uRNKwszujk13GCOMEQstAW/QN+Yb7nQ6W0dilkQvzF7Y3nB1qG0YCRBB6A+qH75R6uodF81iztolJqu5rb51oGW44tWqxVmLFiUtBgAACMZ73AB5kgoSiEb6mvsDPv/JP59O+WVKhDki/BZwOBzOLcTr9V67ds1kMrF8H7cZTdOio6Offvpp8MlzMgBAUZSSkpLVq1eHykUTQtLT0xctWuR2u1VVNRqNJpNpYooW5o9z9913b926ldVjYilRWA/scV3TNJvN9sADD7DCWKIospy10zpNsJJPP/rRj25OOkMImVixSFXVMHZGR0f/7Gc/m3QIo9HIzgljISug/p3vfCcQCJjNZnZw4lqFpmmxWH7yk5+wpWMHly9fnpiY2N3drWlabGxsSkoK+zTU6sEHHwQAsGJPLpeLUmq1WpkXT2inprJNUZTVq1evWbPmhkmFOmd27ty5c9euXaGDbFWfeOIJJouEDhYXFy9fvpxFOZnNZr1eH3KzCi1yRkbGT3/6U7fbDSE0m82hNDrhmzOJbfv27Rs2bHC73QAAJkIxuYf1nJubm5aWJsuyIAisT0VR7r//fhZ7NXF2EEKj0cjOkWV59+7dmzdvZrXMrFarKIpM76usrOzo6IiNjV21atXcd8/p7OwMBoOpqak89orD4XA484x5IugghMa94w0nLwNINz+8cevabSpR5SxZENCpl85ere3ybvaECsdOCiZarCP2kf+yzxHp0DSNAlqcsWJsyHX5WPNg7yAAABNCNAwAMFqMixLTdZIuK22JL+Az6A0sJKpgWYFBMoyNjQ63jMQucGzbsi2oBQGgKlYJIQpR7v7W3QISxz3jL/3PP3qd3s8MT0FdRR2kMGax46EfPGDUGykFMQkxoyNjGUsXK5pCKJ1qdELxTOYeZnaKphQVFq1ZufZC1YUPXywDkOZsXbL7zt1mvfmV0f3DV0awSkRB6h5o6b3SDxDY8p2Nq5aXYIqXLc89W3YudlGs1fKpWCNK4u7HdyzNWkYpraiuOP7SSe+ov6ev154ZxQUdDodz2zh//nxPTw/GeN++fbOVDPXmNCshV53QEfYwzJ7eJyoFIZh4odPpmNdMqGjRxE5Y0tzQOZ/3AXsm6WDC2CkIQkRExKStmLYyrYUsh0tI/Zlo1UTbJtZrZ38oihIVFRUXFwc+CX2a+ClrwtLfQAiZkTdoVeFtm3Rlbjh4s52h4xMdeViNMIvFwkK/Jy0IxeyMjIycuHQzac6OIIRYWfGb56hpmsFgmFi6mwX93azlTTyH9SOK4sRuEUJut/vYsWNer3f37t0Oh2OOu+eMj48fP34cAODxeAoLC2fbHA6Hw+FwbiXzRNARkDA6PuIb9VORDvYNvfX+mxgTQRDGR8epSPwuv8vritPHExCuyKhe1nf3fHzsg2PjPW5KqT3NprpViqjH4yaUmgymnPXZ5w9UVrxa1VbZkbMmKyc3xx4RFVSv31RpWA1CFHpdFtSCN5fuppPVlkIIubzjI51jANLMwgyDzuBX/ACAosJChBAFVNVUo9441eiiMP3c4w3xgixONTtwveQVpYACCnRG3eqNJaIg+FVfTEK0J98TmxxDKe3t6AWEWmIsGYsyAqofE2wxW/fcswdCqGKVUAIAgARGLYrMychVNAUhlJOVfcFW5R32+sfn9N0eh8OZfxgMBlaf6MtU9PuSzEQOYExbA/uGE75YJ5PyudZn0iHozIphT9U81MlU+lf4I0yOCXNOSHAJb+RUts1kfWZiJ5hijjefM5Wd0zYPP8ebJzjDL8zN3Wqatm3btq1bt2ZlZc3NUuUT4fWtOBwOhzOPmSeCDgTIG/RiDVOBNrx/GZLrb5wopECAqk/DGN/0FuozSIJ0ofrC8RdOUQwAolCAQ81OImEAIWEey1hZt2atyWSq+qB6uN15qv1sVVTNsi05a9asQYIwsYD3VFzXTMCNd2MQQIw1ggkAwGA0kFAqR6KFBKgwowuibpq5EywLujOV5WFmBz65+4QAGG1Go86kEY0QUlKyenXJagqAilVN0QAAskGSBIlcvz8mGlE/c39JgaAXEUIUE0KAKEg6o84LvCDs4nM4HM4tx2g0fjGBg8PhhIEQYjQaWc01ljZ7ti2ahlB+qJvdkTgcDofD+bozTwQdAKhe1kMIAYR5u3JNZhO7w2Ce4bIkR1ps2tSvrQQkjLnHzh+8QADN2LS4aE2BTtK5PK6LpdXd9b3XB6AUQLh6xeqc7Ozmq80Npy9du9RT8dpFVdG2b9/2JTP+QojYfYaqqqzYOQBARKIgiIRiVVMJpWiK0ffs2hN+7lHWqGHXcPjZTQQhCAFkKg0h+LpjPxKRgAAAWMWYEhECSgGESBIkCOHEIlY3OJnfLGBxOBzObWAWHXM4nPkNpXQuFym/AX4p4HA4HM48Zp4IOpjgCGOEzqwLjgdik2I2rtzkV/0IIg1rAAAKqIoVCAFCoiiIECEAAIRQFERMMaUEIeTyunxjfkFEm7dvTHIkB7VgppTVd7W/u/a65MEEl8GRgehIx8q8VcVLV5ypLD/x4ukrZ5pL1qwKvQq+ftsAoSzKFFAIQEjrEZAgCCJCAvsXCYIoiJhohFKL0WyKNnqdvquXrq5euVon6UUk1l6u6WjqzF6+JCk+mdVwnXT0NetW2yz2MHMHgHb1d4WfHUJIFEQ2CgBQFERJlDDBGGuhO6Go+CgKwPiQu2egJ3dxroZVf9D/3uEPHHHRmUuyoqxRX/0+czgcDofD4XA4HA6HwwFgPgk6dqt9YeGCK8ebT71aLsnSgtQFHp/nzJGzMWkx69euAwD4Aj5FVWRJVgMKgAAr2ojbyY6YDRaT3iyb5KA3WFlRRVZRSkh7y9Wa0jqKKLiu5sBTp05eOdlSvKdgceZiWZI1DQMKkIxYZVYGBIBC2tPc19R5RZbl4UFnVkYmO8Htd1NCPV4vIQRA4HV7R9xODWtGndGgM2YVZw42DXfWffz2229n5WaOjbrOvXc+MKA4e0b2Pf4whfTkyclHhxDaLLZwc4dw2tn5g36f3xfwBQAEmqb1j/SJsigKos18vQ6rRtQFKWnWWMv4oPvoKx+697hNRmNj9aXm8jaEUcTTEbG22NnZew6Hw+FwOBwOh8PhcL55zBNBBwCAAVl/x9repl5Xr/vQsx/ozHLQG4Qa+rj+WnbOkgRH4tFDH1453QIlEAwEqQj6m4b+8x9+T1WwZH3Gnrv2REVELVmXWX+ksfbd+poj9QAAqEAqUEghUTEEEGtaX+uge8hz/MVTJw3lgiAoXhUSlFWSYTKalU9SI8enxF+hba5e14FnXoMExS+Lyc/NV7SgLOoOvfFaX8MAQCAYUAACR58vRQiZreYHntqrk3WFBQUdDR3ddT2Xjl1pPHaFxXlLFnn9nWsFUQwE/FOObjBrRAsz92i7I/zsZEGuqaitfLcaA41C6up3/fEfD0CMHMtsP3jiByy1MyHEYjSv37vm8G+Puns9R//zGAUAAgApzNi4KH1BhopVohGIIVE/E9qGFQwJpIQ7PHM4HA6Hw+FwOBwOh3PLmEeCDtZsEfb7f3zf+VPnO+o7VZ9mspviFsUUbSi0R9oxwQABURQoIgaTASJICQWUQhEBBACgGtHu2H6HKAnNlW2qV0USWlSUZjQam2taI+IiMNFESbz3kburllQ1V7V4hrwAAFtqRPaqJSUlJap2vcSpitW8/HznnpG2ynaiUiSh9Lx0ej2zMUUIioJIBWKyGgEEBBNIARQgABATLMu6u79zd3lSeVv1Vc2nIQk5FkSXbF2ZlrRQUYPhRscqpSTc3LFGIAozO0KJZJR0DgmKMkTXw7QggZFxERMz4CiakpeVJ/1UunCsaqzHRQmVLfKSlRmr16wBkBKCzVHmiDRLxIRWEILI5EgoA71Jz5PpcDic28k3KnGGIAiCIKiq+o2aNYfzuZj7+Zs5d9OV0AAAIABJREFUHA6Hw/m8zB9BBwCgYdUWYdtz1x7fNl8gGJAkyWw0QwhVTVGxsmHz+tXrVt9Q4oBSIEmiilVKKUJo2/bta9ev8wd8sqyzGC0EkA2bNwBAVawCAHSyvHH9xpKSVR6vFwBgNpl0kk7FWqjEFaVEFMRdu3e5N7pVVZVl2aDXM7lHxerue/bgO28stgUhMhj0hBAAiFFv2LVrp3eTzx/wSaJkNpkhRCzfMCEk/Ohh5s4MCzM7b9BTXFRUXFR804rSG5I9K1jJXpydnpbh8bhZnQuDzqBijRBCANm8afPmTTDUilIiiMJ9+77NAtG+ZN5oDofD+VwIgqAoCkLok+xg8xaEkNvtbmhoSE9PdzgcM6wgzuF8Q4AQKooCANDr9bNtC4fD4XA4t5h5JegAADDWMACyLOt1Ogqohq/7zlBK9XqD0TBJxUpCKdNEKCWqpoTaMiVlYpFLQohCggihSGsEAIBQcrNIwToxGgzQYCSUhl4HUUpNRiO8qXw3BZ+egwnGBIcMIJRQ8ul9+bSjTzX3iYZNNTtK6QyreSqaAiG0WCwQQEI/I9NM3QnlL405HM5tZunSpYsXLxZFURTn2y/dRERRdDqdv/vd7/r7+3/5y18ihLigw+FMRJKkhx56CGNsNBpn2xYOh8PhcG4x8/M2l1KCbxIQJj04bdublQhKKabT3C5P6tY7Q1/f8HZOO/p0zaec3cw1l4mFyW/+aNojHA6HcxsQBMFsNs+2FZ8DprBPdc2c6lMIoc/nGxoakmUZhhXmw/fP4cxjDAbDbJvA4XA4HM5XwvwUdDgcDofDmV2YwoIxFkWRBX1QSnU6HYRQ0zQWAwIAQAiJosgCxNgJhJCJ2XAQQrIss4OsuaIo7A0BQshgMOj1elZLUafTGQwGURQ1TVPV606aEEJmSTAYlCQJITSxOXNfghASQjRNkyRJEITQv5qm3f5143A4HA6Hw+HMEC7ocDgcDodzK2E6TnV1dTAYXLBgQWVlZTAY3L59uyzLhw8fdjqdBQUFy5Yt0zSNySuNjY2tra39/f2U0sjIyIKCguzsbIwxpVQURb/ff/bs2ebmZq/XGxERkZWVlZ+fr9PpAABDQ0NHjhzxeDxM/SkrK4uIiFAUJTU1NT8/X9M0QRAIIdXV1Q0NDaOjoyaTKSMjo7i4WK/XY4y9Xu/w8LDX61UURa/XZ2dn19fXt7S0eL1eh8ORl5cXHx/PA7g4HA6Hw+Fw5ixc0OFwOBzOPMTr9fb09BiNxqSkpNs8NPNwOXTo0PDwcExMTFtbG0JoaGgIQnj+/HlZluvq6p566qn09HS/3//CCy/U1NQoiiJJEgtoraiouP/++zds2KBpmsfjeeGFF+rr6ymlsiwHg8Hy8vIlS5b84Ac/cDgcQ0NDr7zyislkYsFlpaWlGONgMLhly5aioiKMsaZpBw4cOH/+vN/vlyRJ07QLFy7U19f/5V/+ZWRk5NGjR9944w29Xk8ISU9Pb2xsLC0tZZYQQpxO5yOPPMIFHc48oLOzU1GUlJQUnheZw+FwOPMMLuhwOBwOZx5y/vz5a9euEUL27dsnSdLtN0CSJEVRvF7v5s2bGxoaGhsbRVHcunVre3t7T08PK0ql0+nMZnNKSsrKlSsTExMxxqdOnWpoaCgrK8vPz7fb7VVVVXV1dcnJyffee6/RaOzv7z99+nRKSopOp1NVNSYm5rvf/a7X6z179iwAYMeOHVarlT24svisw4cPnz59OjIycvfu3YsWLert7T169GhdXd2HH3744IMPWiyWlJQUjLHL5bp27Vp7e3tmZuaSJUuuXLnS3Nw876uDcb4hjI+PHz9+HACQl5dXWFg42+ZwOBwOh3Mr4YIOh8PhcOYhBoOBeZrMYhpgTdO2b9++a9euf/3Xf62oqCgoKHj88cdff/317u5uj8fDTvjWt75lsVgMBoOiKCaTKSEhoaOjw+VyjY6OOhwOllgHIZSYmJicnLx06dLCwkKWE0dV1aioqHvuuaerq+v8+fMAgHXr1qWmpqqqijEmhLhcrgsXLiCE7rnnnt27d2uaJsuyIAivvPLKpUuXRkZG1q5du2nTpjNnzrz00kuqqm7cuHHv3r1ms/m5556rra3lCXQ48wNBEGZF0uVwOBwO5zbABR0Oh8PhzEOMRuMMawt+pSQkJFBKWUhUcnIyAMButwMA3G43+ORRs6ysrKWlxe/3G43GxMREk8k0NDQUCAQIIbm5uampqR9//PEzzzyTl5e3cuXK9PR0QRCCwSAAgBASDAZD+Y9VVQ39K0mS0+kcGxszmUx9fX0HDhxg6ZlHR0d1Op3b7Xa5XCaTCQBAKSWE2Gy2LVu2sJQ98fHxBQUFSUlJc2EBOZwviSzL7I/wZeA4HA6Hw/k6wgUdDofD4cxD5kh9buYiFDIm9IeiKAghl8v13HPPNTY2AgCsVquqqtXV1WazGUJIKcUY22y2H/7wh++//35dXV1paen58+eXLFmyZ8+etLS0kI4zKQghn8/n8/n0ev3Ro0dD7jYIIVbHiiXHYfYQQiIiIkwmk6ZphJCNGzdu2rSJUhp+CA7na8EcuRRwOBwOh/NVwAUdDofD4XBuNxBCURTPnz/f2NiYkJCwe/fulJQURVFaW1uPHTvGHHAAAJqmJSQkfP/73+/q6rp48eLFixfr6ur6+vp++tOfOhyOMFFRrAI6K4a1c+dOs9nMFBwmFel0usjISIxxKFEOhDDkv0AIYad9tUvA4XA4HA6Hw/lycEGHw+FwOJzZoa+vj1Kam5u7Y8cOj8ej0+liYmJOnz4dinUSRdHlckmStHjx4sWLF2/duvW3v/1tS0tLfX399u3bJwo6lFJJkiRJYt43GOPIyEiLxTI0NJSYmLht2za/348QYk0opYqisP6ZpgMhZM1ZbSyu5nA4HA6Hw+HMfbigw+FwOBzO7GCz/f/s3Xl0VGWeP/67115JqioJWUlCElnCvkQJmwKtYAMKIo3doqitx7btZY7TfWa6bU9/Z7qdcxxnuqd3HRVtd0VAEMQFRCEIEZo9gSSQlZCQpVJVqaq7//54jvdXk80ASW5SvF9/cJK6z733c+8NVXU/93k+TxJN01VVVWVlZT6fz+/3f/LJJx0dHSzLUhTFsmxjY+NLL73k9Xpvu+22xMTEaDRK+s4YZUEMoih+9dVXHMddvHgxMTExMzPT6/VOnDhxz549W7ZsEQQhPz8/FArt3LkzOzt76dKlFEVFIpFIJBIOh0mJ5YsXL3Icx/N8UlISEjoAAAAAIx8SOgAAEIdMT0nEdnXRNI2UpyGBKYpCJqKaNWtWaWlpTU3Nf//3fzscjlAoRJI10WiUTG7V3Nzc1NRUWVl58uRJl8sVDodDoVB6evqkSZPIECpVVT0eT1JSUl1d3Y4dO3bu3CnL8hNPPMFxnKqqt956a3V1dU1NzfPPP5+QkBCJRPx+f2pq6tSpUzMzM/fs2bNr1y7SN6epqenpp58WRbGoqOiJJ54wxnwBxA0U+QYAgPiDhA4AAMQhlmVJ4WGjTMwwc7vdHo+H4zhd1+12u8fjsVqtJF/j8XhcLpcsyxkZGQ899ND777/f2tqqqmpeXt6cOXNOnjzZ3NwsCIIkSVOnTv3Rj370+eefX7hwQVEUh8MxceLEW2+91efzkYrFmqY5HI67775769atfr+foqjU1FSfz0dyRj6f7wc/+MHHH39cUVEhiqLD4Zg0adKiRYu8Xq+iKBaLxW63W61Wo3qOJEler9f0XBjAIKJpmgwwtFqtZscCAAAwyJDQAQCAODR58uT8/HyO4zhuuD/pNE3jOO6+++4jKZiurq5vfetbixYtslgsXV1dkyZNevLJJzmOk2VZ1/X8/Pwf//jHnZ2dmqa53W6LxTJv3jwqpsxNQUFBQUFBZ2enJEmCICQkJHSbf0qW5RtuuOGnP/1pMBikadrpdDIMQ/rvyLLs9XrvueeeUCgUjUY5jktISCCvS5I0d+7ckpKSnvGT/QLEB57n169fr2ma3W43OxYAAIBBhoQOAADEIZZlnU6niQGQ2cfJtOV2u93hcJCfBUEgXXXIABBZlmmaTkxMpChK0zRJkoz+MgTJ3Rhzmfc6lbgsywzDJCUlUV9PlG4sIlWQrVarzWbDTORwfUIqBwAA4hUSOgAAAIMvtmBH7M+6rpPuM3290uuIp28s/9FzswNZHaOrAAAAAEYvcyoLAAAAAAAAAADAVUNCBwAA4lA0Gq2srMS8NgBQX1/f2tpqdhQAAACDDwkdAACIQwcPHty/f/8nn3yCUUUA17NAIPDRRx9t3769paXF7FgAAAAGGRI6AAAQh3ieFwShqakJZYABrmcsywqCwHFcTU2N2bEAAAAMMiR0AAAgDpFZpRgGH3MA1zVBEMgPHIeZQAAAIN7gmy4AAMQhjLQCAApvBQAAENeQ0AEAAAAAAAAAGGWQ0AEAAAAAAAAAGGWQ0AEAAAAAAAAAGGWQ0AEAgDiEwhkAEEvTNLNDAAAAGGQo+A8AAHGIYRhJkhiGwURXANczmqYlSaIoymKxmB0LAADAIENCBwAA4tCUKVPy8/N5nsdcxQDXM57n169fr6qqw+EwOxYAAIBBhq+5AAAQh1iWdblcZkcBAOaz2+1mhwAAADAk0BEdAAAAAAAAAGCUQUIHAAAAAAAAAGCUQUIHAADik6ZpmOsKAHRdxxRXAAAQl1BDBwAA4lB5efmRI0ecTueKFStYljU7HAAwhyzLW7dujUaj8+bNy83NNTscAACAwYQeOgAAEIfq6uoYhgkGg6qqmh0LAJgmGAxGo1GKotra2syOBQAAYJCZ2UNH0RRFk2maNjEGMAvHcHbBQVGUqqldUsjscMAcGA4DQyc5ObmlpcXsKADAZE6nk/zAMHiKCQAA8ca8hA5NjU3M0XQMab4ecSxX31b3xubXKYrKGpu9euEaRVXMDgrMwdAMhaQuAAAAAADAFTItoUNTtNfuM2vvYDpLovXUjnKKonJW5SdZPWaHAwAAAAAAADCaoCgymISmNE6jKIoV0AUaAAAAAAAA4MrgXhoAAAAAAAAAYJRBQgcAAOIWCm8DAIEJ7wAAIP4goQMAAHFIVVVFUQRBYFnW7FgAwEzk3SApKcnsQAAAAAYZaugAAEAcys3N7ezsnDt3LhI6ANcznucLCwvdbnd+fr7ZsQAAAAwyJHQAACAO+Xy+JUuWmB0FAJiMpum5c+eaHQUAAMCQwJArAAAAAAAAAIBRBgkdAAAAAAAAAIBRBgkdAACIT5qmYZYrANB1XdM0s6MAAAAYfKihAwAAcaiiouKrr75yOp0rVqwYYF1kZH8A4o8sy1u3bo1Go/PmzcvNzTU7HAAAgMGEHjoAABCHamtrGYYJBoOqqg5wFZqmhzQkABhEA/wPGwwGo9EoRVFtbW1DHBEAAMBwQw8dAACIQ8nJyS0tLVe6yhAFAwCDboAJHafTSX5gGDzFBACAeIOEDgAAAEWhhw4AAAAAjCp4WAEAAAAAAAAAMMogoQMAAAAAAAAAMMogoQMAAAAAAAAAMMogoQMAAAAAAAAAMMqgKDIAAMQhRVEGPmE5AMQx8laANwQAAIg/SOgAAEAcysrK6uzsdLvdPM+bHQsAmIbjuHHjxkWj0dzcXLNjAQAAGGRI6AAAQBxKS0tLS0szOwoAMBnDMPPnzzc7CgAAgCGBGjoAAAAAAAAAAKMMEjoAAAAAAAAAAKMMEjoAABCfNE0zOwQAMJ+u62aHAAAAMCSQ0AEAgDhUXV39xhtvXLp0yexAAMBMiqJs2bLlk08+wSxXAAAQf5DQAQCAOFRVVUXT9IcffijLstmxAIBpAoFAV1dXY2PjqVOnzI4FAABgkCGhAwAAcSg5OVlVVZZlMdoC4HrmdDopimIYRlEUs2MBAAAYZEjoAAAAAECco2na7BAAAAAGGRI6AAAAAAAAAACjDGd2AHCdomk6EolQFIUihQAAAAAAAABXCgkdMIcsy8uXL6coKjs72+xYAAAAAAAAAEYZJHTAHG63+/HHHzc7CgAAiBOapum6TtM0w2A4OQAAAFwXkNABAIA4pCgKRnReJ06dOrVly5ampqZAIOB2u9PS0u68886ioqLYNtXV1XV1dSzLxr7IsqzL5crKykpKShrekGFYkbcCvCEAAED8QUIHAADiUFZWVkdHR0JCAs/zZscCQ+jFF1/cunWr0+nUNE1RFEVR/H5/WVnZHXfc8cADDxjNPvroo61bt9pstm6r67rOcdyGDRtWrVo1vIHDMOE4Li8vLxKJ5Obmmh0LAADAIENCBwAA4lBaWlpaWprZUcDQ+uyzz7Zt2+ZyuaLRaHJy8oQJE8rLyy9fvuxyubZt25aXl7do0SLS0ul0OhwOm80myzJFUZqm0TStqqrFYqFp+oUXXpg6dWpOTo6JxwJDhGGYBQsWmB0FAADAkEBCBwAAAEYfWZY3bdrkcDhEUVyzZs3dd9/NcZyiKFu2bHnrrbccDsemTZtKSkpiu2hJkvQf//EfY8aMIdV2IpHIH/7wh3PnzvE8v3fv3o0bN5p4OAAAAABXCgmdUamvceC9FoPUNK2jo0NRFJfLZbfbYxfJstze3k7TNMuySUlJZN1wOBwMBimKGur2FoslMTHRiFBVVZqmk5OTu8Xv9/tFUex1+xRFXbx48eTJkw0NDZqmZWZmTps2beDP5GVZPnnyZHV1dXt7uyAImZmZkyZNSk9P79bMONvdii9QX9fgpCiKYRiapge4XwAAuHbl5eWBQMBisaSkpKxbt468RXMct2bNms8//7y1tTUQCJSXl0+ZMsVYRVXVjIwMq9VKfnU4HD/5yU8efPBBq9V69OjR+++/H+/kAAAAMIogoTP6KIry2GOPdXV19VzkdDpTUlLuvPPO6dOnGy++/vrrW7ZsoSiqZ42AqqqqX/7ylxzHpaam/tu//VtCQgJFUR9//PErr7zCsmxubu6TTz7pdDqHoj1FUTNmzPjFL35BUVQwGPz1r3996dIlmqYfeuihpUuXxgb5pz/96ejRoz3j13X9vffee//990OhEMm5MAzjcrlWrlx55513fuMsJydPnnz11VfPnz+vqirJJbEs63Q6b7nllvXr1wuC0O1sS5L061//esKECbEbef3117du3UpR1E9/+tOSkpL+9wgAAIOosbGRoihRFFesWBGbcGcYZvny5c8//zxFUU1NTbEJHdIxJ3YjkUhE13Vd110uF7I5AAAAMLpgas9Ricze0lNnZ2dlZeVTTz318ssvG421r5G+JN0YS41XdF3XNI1l2bNnz77xxhtD1L7biyQ8TdNee+21urq6XrfQLf4XX3zxlVdeiUajHMcxDMMwDM/z0Wj0lVdeIQmjfhw5cuTpp5+urKw01mUYhuM4URQ3b978u9/9LrYPFDnbLMs++eSTfr+/W2zkzMceCwCMBIFAoLq6utfcN8QH4w25Z9fOlJQU8kN7e3vs64IglJWVnT9/vqqqqrq6+syZM3/5y18EQYhGo0jKxytd12traxsbG3v9FgQAADCqoYfOqEQG+JBniQzDkOKOuq6Hw2G73e5yuTZv3rxkyZKMjAyKooyWvaK/1vNFm8320UcfTZ48+cYbbxz09sa/sc04jgsEAi+88MIvf/lLo+pBr/GXlpbu3LnTbrcriuJ0OmfOnKmq6tGjRyORiNVqfe+998aPHx8bRqxAIPDiiy9KkmS1WiVJysvLy8/PD4fDx48fD4VCTqeztLR0wYIFxurGcCqWZf/4xz/+4he/MOIxYsNzXYCRZv/+/S0tLTRNf/e73+U4fNjFIUmSyA9Gn0qD8QlitCE4jvuv//qv2BS81WqladrlchnlkyHOdHR0fPLJJxRFFRcXd5vMHgAAYLTDd9xRTJKkZ599lhR3JK80Njb+8pe/JJmRY8eOkYTOVSNJik2bNhUUFHi93kFv3yur1XrixImtW7euXbu2rzaiKG7fvp2iKFVVk5KSnnjiicLCQoqijh8//uyzzwaDwcWLF2dnZ/e1+t69exsbG+12uyiKt99++7333ku++p87d+7ZZ5/t6Oiw2+3PPffc7NmzuxXN4Tjuq6+++uSTT7oNCgOAEWjMmDFtbW0URaEDXbwyqqpFo9Fui6LRKBld1bPyGukNyjCMzWYjz0IyMzP/9V//1eFwDEfQMOycTidJ+ZF6fAAAAPEEQ65GMVVVU1JSBEGwfC0vL6+kpIQ8kOzo6Lj2XfA839zc/OKLLw5R+15ZLJb33nvv1KlTfTW4cOHC+fPnBUFQFGXdunUkm0NR1NSpUx9++OEf/ehHP/7xj3vWNiZUVT18+DDLsrIs5+XlGdkciqIKCwvvueceMtjK7/c3NDR0W1fXdZLraW5uvpYDBACAa0fK6tM0XV1d3W3RoUOHyD08aWOQJOlXv/rV3/72t2effdbj8ei6LknSvHnzkpKShi1sMAv60gIAQPxBQmcU61nckaKoQCBAXrz2IQbkMabVaj148ODHH3886O17omlaVVWGYSRJ2rRpUygU6rXZ2bNnJUnSNC05OTm2/DNFUfPmzbv55pv72UV7e/vly5c5jlNVtbi4OHY6W4qipk2blpKSoigKRVEVFRXdYiPP+RmG+f3vf49n/gAA5po2bZqu6xaLZfv27aQ3FtHc3PzFF19wHKfr+rRp02JXUVV14sSJaWlp48aNe+CBB6LRqMViefPNN3v28QEAAAAY+ZDQGcUEQTh58uSlS5eampqampouXry4b9++Y8eO8Tyv63p+fv61bFxV1dTUVK/Xq6oqx3GvvfZac3OzxWIZrPZ9KSwsVFXVYrFUVVW9+eabVG+P1Orr60nqx+fzdXv6+o0CgUAgECBzYOXm5nZb6na7U1JSSCedzs7ObksnTZqk6zrHcefOnfv73/9OxZRpAACAYebz+fLy8sig46eeeurs2bPRaPTs2bO/+tWvOI7TNC0vL8/n83Vby6h5P2PGjNzcXNJJ59NPPx3u6AEAAACuGWrojGIcx/32t7+N7SpCigKQyjLdHkteKVmWMzMzZ82a9bvf/c5ut5NCwitXruxrOvArbd8rSZJWrVr17rvvVlZW2my23bt3z549u2dWiIwm0zTNbreT7be2tr7yyiuyLJNfJUkaN27cd77znZ67EEVRFEWbzUZRlMvl6raUpmmLxUJuDyKRSOwiTdO+//3v//73v6+pqSGDwpYsWcKyLCnBMPBjBACAQUHT9GOPPfajH/3I5XK1t7f/y7/8C8dxiqJYrVZd14PB4GOPPdb/nAAbN2781a9+ZbPZ3n777aVLl/YsrgwAAAAwkqGHzihGeovwPM/zvM1ms9vtVqtV0zSXy/XMM89c+5ArURQXLVo0f/58MnXU8ePHd+zY0c/33Stt35Oqqh6P58EHHxQEgWRJXnvttZaWlm7HYtQqNpJZkUjk0KFDB7924MCBM2fO9LoLUnKIbDwYDPZsEI1GyQ0ASfrEHl1SUtLPf/7zcDhMUZTD4fjP//zPsrKyq+iFBAAAgyIvL+83v/kNmXecZVlN01iWjUajPM//5je/ycvLM1oGg8FQKBQKhWKfghQVFaWnpweDwUuXLm3bts2MI4Dhg6cvAAAQf9BDZxTTdT0vL4/kHWpqakgmQtf1p59+OnaSKeMbTM8HlUb3GV3Xe37RIa/cf//9VVVVra2tPM8fPXq028RP19K+V6IoTpgwYfXq1a+99prdbq+rqyOTdpG6NkRqaipFUSzLdnR0RKNR8jBWVVVFUex2OxkG1ddgKLfb7XK5AoEARVF1dXUzZ86MXer3+0mFHVmWew7mUlU1MTHxsccee+655wRBQGlkgJFMURRVVXELF/emTp363HPPHT58uKKiIhKJ2Gy2wsLC4uJiq9Ua2+y73/3uqlWrqJi5sSiKomn6mWee6ejooGn6Sj+tYBQh4+xQ/A4AAOIPEjqjmCiKTz75JJlptays7Le//a3NZlMUpaqqKrZqgDEVa3t7e7cttLS0UBSl6zrP892++xq8Xu/GjRufeeYZXdcH8n33Stv36o477jh9+vTx48e7dZMhSNEEjuMuXrxYXV09adIkr9f7+OOP0zS9Z8+e06dPU//3K3ssj8fj9Xrb29sZhjl06NDtt98e24fo8OHDLS0tFotFFMWsrKxet7B06dK9e/deuHDhikaTAcAwS0tLa2tru+GGGzCOJu5ZLJb58+fPnz+/nzYJCQkJCQk9X7fb7X19XkB8YFk2Ozub5/nJkyebHQsAAMAgwx3p6GZ0upk5c2ZmZqau64IgvPTSS0bRR4qikpOTNU3jOO7LL788f/688brf79+9ezfLsoqipKam9pXQoShqzpw5y5cv71ZTph9X2r4nnucfeughj8cT2zHHMHnyZK/Xq2maoiivvvpqS0uLw+FYuHBhUVFRZ2cnmY4qOzu71y1zHDdr1ixVVQVBqKysfPPNN2VZJosqKys3b97Msqyu6z6fr6CgoNct0DT9i1/8wm6348k/wEiWlZW1bNmy2EE3AHAdYln2lltumT9/fj/fcwAAAEYp9NCJEwzDPPzww6S4Y2tr65EjR+bMmUMWTZ8+3el0KorS0dHx7//+71OmTHE6ndFotLKy8uLFizzPy7JcUlLS//bXr19fUVFRVVU1wJIxV9q+p8zMzHvvvfcPf/gDKTwcu8jn8y1atOjtt992Op2VlZX/7//9vylTpiiKcuLEifb2dpqm7Xb77Nmz+9rykiVLPv3008uXLwuCsH379oqKiry8vFAodOLEiVAoxHFcV1fX448/3k8RIqfT+ZOf/OTJJ590Op1I6wAAAAAAAMDwQw+d+FFUVERmYLVYLC+//LLRScflcn3ve9+LRCK6rnd1dX3++ec7duz49NNPm5qaGIYJBoMLFiy46aab+t+41Wp98MEHyRRaAwnmStv3atGiRQsXLuy1p8/q1aunTp1K8i8tLS07d+78+OOPSR2EcDh5Xi34AAAgAElEQVS8bNmynJycvjabmJh4//33cxwnSRLHcZWVlTt27Ni3b184HKZpOhQKFRcXFxcX9x/blClTVqxYIYriVR8dAAAAAAAAwFVDQmdUamlp6TlbB5mBta2tLRQKVVVVffbZZ8aiW2+9lYxgkiRJ0zRS/EUURYvFsnLlykceeSS2N4okSWTj3TIphYWFa9euDYVCwWAwHA4bPVOuvb2u6+FwmLzYLQG0YcOGzMxMv98fCoUkSTJet9vtP/vZz771rW8xDCOKIunCE4lEeJ5ft25drxOWxyouLv75z3+ek5MjSZIx2Xk4HBYEYcWKFT/+8Y9jq//0erZJbAkJCWTmlGsZXwYAAAAAAABwpTDkavRhWfavf/2rruuapnUr5VhUVLRp0ybyc+w0TzRNr1ixoqSk5OTJkzU1NeFwmOO4rKysiRMn9qw1M2fOnKSkJIqiYisrE9/+9rd9Pl84HI6tInnt7e12+wMPPED6EGVmZsZuITEx8Z//+Z/Pnj1L03S3ojYul+uHP/zhsmXLTp06Rao7p6WlFRUV9dM3J9b06dMnTJhw4sSJysrKQCDA8/yYMWN6rt7P2RYE4Y9//GNbWxtFUbHTigHASBCJRJqamux2+5gxY8yOBQDM1NDQIElSRkbGVQ8DBwAAGJmQ0Bl9aJpOS0vra1F6enpfK3o8noULFy5cuLD/7efk5PSVE2FZtme1nWtvLwhCP0V8xo4dO3bs2L6Wjhs3bty4cX0t7Z/Vap0zZ45RbKhX/ZxtiqJsNlu3DBQAjBClpaX19fWqqm7YsCE2wQ0A15VAILB7926KoqZPnz5jxgyzwwEAABhMSOgAAEAcslgsPM+TeevMjgUATMMwjCAIFEXhrQAAAOIPaugAAEAccjgc3epeAcB1yBhm1W3GTAAAgDiAhA4AAMQhPI0HAApvBQAAENeQ0AEAAAAAAAAAGGWQ0AEAAAAAAAAAGGWQ0AEAAAAAAAAAGGUwyxWYIxqNnj9/nqIot9uNmb8BYNCRwhmqqpodCACYT9d1RVHMjgIAAGCQIaED5tA07Re/+AVFUXfeeeeGDRvMDgcA4g3P85FIZNasWTzPmx0LAJiGYRhRFK1W66RJk8yOBQAAYJAhoQMAAHGoqKgoJyfH7XabHQgAmInjuPXr13McZ8xfDgAAEDeQ0AHT0DRt/AsAMLgYhkE2BwAoinI4HGaHAAAAMCRQFBkAAAAAAAAAYJRBQgcAAAAAAAAAYJRBQgcAAOJQJBK5cOFCc3Oz2YEAgMkaGxsvXLggiqLZgQAAAAwy1NABAIA4VFpaWl9fr6rqhg0bMNEVwHUrEAh8+OGHFEVNnz59xowZZocDAAAwmJDQAQCAOGSxWHieZ1lW13WzYwEA0zAMIwgCRVF4KwAAgPiDIVcAABCHHA6HpmlmRwEAJjNmK8esmgAAEH+Q0AEAgDiEp/EAQOGtAAAA4hqGXIE5jAdleGIGACOELMtmhwAAA6LrOhlIBQAAcD1DQgeGFnky1jNrI0kSeVGSpL5WRK4HAIZTW1uboihmRwEA30zX9YyMDIZBT3MAALiuIaEDQ+vDDz/ct2+fMYKdoGk6HA6TFw8cOFBXV9etRzRN05FI5KmnnrLb7cMaLgBcxxiGwf0hwKiAgVQAAAAUEjow1ObOnfvnP//Z6XT2XEQ64EQikbNnz3ZbJEnS7bffjmwOAFw13O8BQCy8JwAAQPzBo0gYWgkJCY8++qgsy3QPRpuerycmJt5zzz3mRQ0Aox5N06IoSpKETjcA1zPyViCKIs/zZscCAAAwyNBDB4bcbbfdtmPHjo6OjgHWxIlGo//0T/9ktVqHOjAAiGNTpkzJy8sTBIHj8EkHcP3ief473/mOoihut9vsWAAAAAYZnlvCkGMY5tFHH41GowNprOt6Xl7ezJkzhzoqAIhvHMclJiZi5CYAOJ3OxMREdNYDAID4g882GA5FRUXjx4//xuHrpFjyI488gm9dAAAAAAAAAP3AbTMMB5qmn3jiiUgk0v+oK0mSvvWtbxUWFg5bYAAAAAAAAACjERI6MEy8Xu/KlStFUeyrAU3Tqqp+73vfG86oACBeSZJUU1OjaZrZgQCAyZqamvx+v9lRAAAADD4kdGD4rF+/3ul09jXwShTFjRs3JiQkDHNUABCXDh48uGfPns8++wxzFQNcz4LB4M6dO7ds2dLa2mp2LAAAAIMMCR0YPjab7ZFHHum1OrKu6x6PZ/ny5cMfFQDEJYZhLBZLfX29LMtmxwIApqFpmsx2d/78ebNjAQAAGGRI6MCwKi4uzszM7PnAPBqNPvrooyzLmhIVAMQfp9OpaRoqrANc5ywWC/mB4zhzIwEAABh0+KYLw4phmB/84AfhcDi2OrKu6+PGjZs2bZqJgQFAnMFIKwCg8FYAAABxDQkdGG4TJky45ZZbJEkiv5Kpyn/2s5/1PwEWAAAAAAAAABiQ0AET3HfffYqikAyOJEm33357SkqK2UEBAAAAAAAAjBpI6IAJEhMT16xZI4oiTdM0Ta9fv97siAAAAAAAAABGEyR0wBx33XVXQkJCNBrduHGjy+UyOxwAiDconAEAsfCeAAAA8QcJHTCH1Wp98MEHrVbrrbfeanYsABCHaJoWRZH0BDQ7FgAwjfFWgFmuAAAg/uCzDUxTXFw8duxYTCoMAENhypQpeXl5PM/zPG92LABgGp7n161bp6qq2+02OxYAAIBBhoQOmIZl2YyMDLOjAID4xHFcYmKi2VEAgPkwshsAAOIVOkcAAAAAAAAAAIwySOgAAAAAAAAAAIwySOgAAEB8wqQ2AEBRlK7reDcAAIC4ZE4NHVEUm5ub//8gOC4tLc2YiESSpKampl7nJeF5Pi0tzfg1Eom0tLT02tJqtaakpHxjS13XU1JSbDab8UpLS0s0Gu25wZ4tm5qaZFnutWVaWpogCMavjY2NmqZ94+Fc+4Hruu7z+RwOh/FKOBy+fPnyQA58gIfTT8tBPxzK1OvIMExGRoaxr4Ffx0E5nG7XcdD/LPtpOQzXsaurq7W11WjZbSnAoDh37tyRI0fcbveyZctQfB3guqUoyvbt26PR6Ny5c8eOHWt2OAAAAIPJhISOruv79u1rbGw0vmErirJkyRLjU/bAgQO1tbW93hYqinLvvfcaN6WlpaX19fV9tdywYYMxuUlfLRVFmTJlyuzZs8mvwWBw+/btvU5s2a1lIBDYuXNnXy2nTp06a9YsY5u7d+/uq2Xs4Vz7gSuKUlRUVFxcbLxy4MCBxsbGbzzwgR9O/y0H93Aos69jbJADv46Dcjix13Eo/ixNvI66rn/wwQeRSCR26erVq5OSknquCHDVLly4oOt6W1uboiixqUwAuK4EAoFgMEhRVEtLCxI6AAAQZ0x4aKnrut/vt1qtgiCQez9d1y0Wi9HAZrP12g+CtIy9XbRYLP20jP21r5a6rsc+uWVZtq9Oud1achzXT8vYWXL732bs4Vz7gXcLkqIoQRAG0nLgh9N/y8E9HMrs6xgb5MCv44g9nBF1HckrHMcJgiAIQltbW68rAlw1n8+nqmqvGUYAuH44nU6apmmaZlnW7FgAAAAGmTlDrhiGUVWVZdmbb77ZarWyLBs7o+ScOXPGjx/f64ocx8XelN54441FRUW9tuR5foAtnU6n8bPdbl+/fn2v41B6tly3bp2qqr22dLvdxs8Oh+Puu+/u9Ua32+EMyoHHjtOhKGru3LlTp07tteXVHU4/LYficEy8jgzDxO564NdxUA4n9joOxZ+lideRpunly5d3dXVRFHXu3LnKykqKojAiBgYdUjkAAAAAEN/MSegQLMumpqb2/M7NMExiYuJAtsBx3KC37JYQ6UdsEqp/sTfS/RiKA+d5foAtB344A2x53V7H0XI4Jl5H488yNTX17NmzA1kFAAAAAAAAYpmT0JEkSdd1URS7DdkAgOuKLMuk01NfY7UAAAAAAACgVyYkdBiGmTNnzrlz5woLCzHOAuB6lp2dXVtbS34wOxYAAAAAAIDRxJweOvn5+fn5+absGgBGDkEQFi9ebHYUEM/6Kv4NANebvgrMAQAAjF7oIAMAAHFIVVVVVTmOw9Q2ANc5TdMURRlgITwAAIBRxMyiyAAAAEMkOzu7tbV1/vz5SOgAXM94ns/JyXG73YWFhWbHAgAAMMhMS+igHDIAUHgrgCGTmpq6bNkyc2NgWZb8eauq2m3wl7FI07SeRcE5juM4jpSZ03VdVVVFUbo1YximZx06Xdc1Tet1oFmv7WP1GgnAaEfT9MKFC82OAgAAYEiYk9Cpqan58ssvb7vttgFOcgwAcUlV1e3btycnJ8+dOxdpHYgzuq77/X5VVRmGIR92Rp6FpulAICDLMkVRNpvNarUai1iW5Tju4sWL1dXVzc3NsiwnJCRkZWXl5+dbrVZJkowtRCKRSCQS+x+HpmlBEMgGZVmOrRjSa/tu0XaLBAAAAABGOHMSOmfPnpVl+dSpU/PmzTMlAAAYCTo7OwOBQGdn5/Tp0+12u9nhAAwalmX9fv8f//jH1tZWmqbXrl27cOHCaDRKlgqC8Oqrr5aXl1MUtXLlymXLlomiSFEUx3GSJG3btq20tLSrq4v062EYhuf57OzslStXTpgwgbQUBOHTTz99//33LRaLsVOGYdxut8fjmTRp0pw5c1wuF2ncV/tYoijGRgIAAAAAI585RZF9Pp+iKLh/A7jOOZ1OmqbJ/arZsUAcMr2ziaIoiqLIsrxt27a6ujpBEIxFZBRV7EAqhmFkWX755Zd37twZjUZZlmW+RtN0dXX1X//61+PHjxsZGVLnlWxfFEVRFCORyKVLl06dOvXWW2/9/ve/r6qqit1jz/bdYA4giFe6rpv+bgAAADAUzEnoYGwFAMTCV20YdJWVlW+99dYHH3xgYl0YmqZpmuZ5PhgMvvvuu5IkGVVs6BjkFUEQ9u3bV1ZWZrfbNU3jeX7y5MklJSVZWVmKolgslmg0+u677/r9flLm2Vid4ziXy+V0Ol0ul8VioWnaYrHU1dU9//zzjY2NRra0Z/tYLpcrNvsDEDcURdm6deubb75ZV1dndiwAAACDDLNcAQBAHDp//rymaW1tbYqimJ6qsFgsZ86c+eijj1auXGkMvIrFsmxHR8cXX3whCIKqqi6Xa+PGjePHj9d1XRTFd999d//+/YIgNDU1ffnll8uWLTNyoJIkFRQUbNy4kWSLQqHQ3r17y8rKLBZLe3v7+++///DDD8c+RIltHxuArut2u73biwBxIBAIBINBiqKam5uzs7PNDgcAAGAwIaEDAABxyOfztbS0jJwOoYIgfPTRR/n5+RMnTuzZJY3juKqqqpaWFovFIori8uXLJ0+eHA6HdV23WCxr1qypqalpbGxkWfbEiRM333yz1WolK+q6zvN8amoqyROlpqaOHTuWpulDhw5ZLJbTp0+fP3++oKDA2JGu64IgpKenG7VySKUemqYxyxXEJTK2l6Io0rUNAAAgnoyOhI6u6y0tLRiUATAq0DSdkpIycm6k4fo0cv4CaZomc11JkrRly5bMzMxeZ3isra2lKEpVVa/XO2nSJFEUyaeeLMtOp3PKlCn19fUcx7W1tbW3t2dlZRkr6rquKAqpgKOqqiAIS5cuPXXqlCzLkiRVVlYWFhbGBiNJUktLC0noMAxj3O4CAAAAwOgyOhI6FEXpuo4nhwCjglElBACIrKys+vp6QRAuXLiwY8eO++67r2ebtrY2iqJUVU1KSkpISIgtUaxpGhkqwjBMV1dXV1dXPykYWZaTk5NTUlJqa2tpmm5qaopdKghCXV3dU089RVGUoig+n++HP/xhYmIiKiIDAAAAjDrm3HeReT0URTFl7wAwcmCUB8Q9WZaXLFmSlpYmy7LFYvn888+PHDnSc/rwUChEURQZY2WxWLp1SiXzQtI0TWak6iehQ6rhkMrKFEUFAoFuDTRNi53calCOEQAAAACGnzkJnYyMjOTk5NTUVFP2DgAjBMdxWVlZaWlpKG0AcYx0urnrrrtYliXTJ2/fvr2jo6Pbn73NZqMoiqZpMlSqW8omHA5TX1fA4Xm+nzHINE2T6cnJFshmY7Esa8xy5XA4MN4KAAAAYJQyZ8hVRkZGRkaGKbsGgJGDYZhbbrnF7CgAhpwoijNmzFi8ePGuXbusVmtjYyOZPjx2oJPP56MoimVZv98fCoXcbrfRj5VhmIaGBoqiNE0jiZh++rWRLbS1tbEsK8tySkpK7NLYWa50XWdZ1ujLAwAAAACjC0pdAABAHCJje0dOqkKSpGXLlhUWFoqiyDBMz34xGRkZJMPS2tpaXl5usVhIG47jgsHgsWPHWJbVNC0hISExMbHbcdFfYxjGYrF89dVXra2tLMsyDJOXlxfbksyKNWbMmJSUlDFjxvh8PtJRiKw+xOcAwBzkrQCFogAAIP4goQMAAHEoPT3d5/ONGzeO40ZE+X9N06xW69q1a10uV88bS1VVCwoKPB6Pqqo0TX/wwQdVVVUWi8XhcCiKsmPHjoaGBo7jFEWZNGmSw+GIHXJF0zTLsiR9o2naF198sWvXLp7nJUnKyMgoKCiQZbnb7sjq5F/2ayhnDnGJjO31+Xxjx441OxYAAIBBNiK+5gIAAAyuzMzMzMxMs6P4PyRJysvL+/a3v/3GG290K6CjKEpKSkpJScm2bdvsdnt7e/uf//zniRMn2u322tra8+fPC4Igy7LH45k7d66iKMbqPM83NTX99a9/JdV52tra6uvraZrWdZ2m6WXLljmdztjKx0b7bn18VFX1+Xy33347x3H9FOgBGHUwthcAAOKYOQmdaDTa3Nzs8/kcDocpAQDACNHU1KSqakZGBoZ7wPUgGo0uWLCgsrKyrKzMarXGLpIkafHixVVVVadPn7ZarV1dXQcOHNB1neM4juNkWWYYZs2aNSkpKaIoGgkdhmGCweDhw4fJr6S3jiRJVqt1xYoVM2bMkCQpdi/d2htkWc7Ozl6+fDlJBg3ZCQAAAACAQWNOQqe0tLS6unrq1Klz5swxJQAAGAmCweDOnTspirr33nsFQTA7HIDBpOt6JBIJh8OqqmqaRlKWpOPMnXfeWVNT09jYqKqqLMtkERmT9eCDD27ZsuXo0aPhcJiU2iHFgNLS0lasWDFz5kzS3YZMhkU2buyRpmlBECwWy4QJE5YsWTJ+/HhZlkl2ptf2sUiQw3FeAAAAAGCQmJPQ4XleEIQRUtcAAMxC7j/NjgLiFsmemLJrkp1ZtWpVNBrVdT0lJcUoZCPLstfrffDBB6uqqmiazsvLMxYpiuJwOO6999758+dXVFRcvnxZVVWHw5GVlVVUVOR2u43uNrIsT5o0yWazGV11SF8et9udnJw8ZswY0k/HiKdn+25UVXW5XAzDoHsOxB8jrWl2IAAAAIPMnJRK/1OuAsB1wmKxmB0CxK3KysojR464XK5ly5YNf7lfXdctFsuCBQvIrqPRaGzXGFmWc3NzCwsLKYqSJMmYnpyiKFIUOTc3Nz8/X1EUMu8VwzCSJMUmaFRVzc3NveGGG7rlX8hUPqTjT+zrfbU30DStaRpJPw3GCQAYKUhZ8UgkUlJSkp2dbXY4AAAAg8mchA6+LwIAhbcCGErnz5/XNK2trU1RFFM6gum6Ho1G+1oqy3LPyaeMFclS0qGgr0FSiqLEZoK+0ZW2B4gPgUAgEAhQFNXc3IyEDgAAxBnMUQoAAHHI5/OR3i5mB3L1yMRVZkcBMLo5nU6apkm9cLNjAQAAGGRI6AAAQBwa1akcABgseCsAAIA4hoQOAAAAAMQndHMDAIA4Zk5Ch3y44iMWAAAAAAAAAOAqmDZxuCiKmOgK4DpH07QoihS6xAMAAAAAAFwhcxI6U6dOzc3NdTqdpuwdAEYInufvvvtuTdN4njc7FgAAAAAAgNHEnIQOx3Eej8eUXQPAiOJ2u80OAeKToijoBwoAFEWRtwJVVc0OBAAAYJCZNuQKAABg6KSnp7e0tCQkJHAcPukArl8cx2VmZkYikbFjx5odCwAAwCDD11wAAIhDmZmZmZmZZkcBACZjGGbx4sVmRwEAADAkzJnlSpKkhoYGzHIFAM3NzcFg0OwoAEafkVNKnKZp9v8aObERIy2efjAMM/zRMgzDsuygbIfjuEHZFAAAAAyEOT10Dh48WFVVNWfOnMmTJ5sSAACMBKFQaMeOHYIgrFu3ThAEs8MBGB04jmMYRhTFkZCnIHPVaZpmBKPruiAIDHOtT4xomuZ5Xtd1SZKu+khZluU4LhqNjoRz1T+apgVBCIfDuq4P5zhB8rekKIrT6byWKjM0TcuyHAqFaJp2uVwj/4QDAADEAXMSOjRNcxwXiURM2TsAjBwkj4P+ejAUdF2Pv7tKmqZbW1u/+OKL3Nzc6dOny7Jsbjwcx5WXl7/11lscx9E0TdO0JEkbN27Mz8+XJOlatqzr+tmzZxsbG+fPn391bxEMw3R2dn722WfJycnz5s0z/Vz1g6ZpTdP2799fVlZ25513ZmVlKYoyDPtlWTYQCLzwwguXL19+6KGH8vPzr/osCYKwZcuWjz/+eNq0aY888oiu63hjBwAAGGrmDLlyuVyapqFQJcB1zmKxkB+u/WE+QDe1tbVvv/12a2ur2YEMJoZhFEV5+eWXt27d2tXVNRL+46iqWlhY6PF4mpub29rampubL126dC19aghBEMrKyp599tkjR45cdfc9nuffeuutzZs3d3Z2joRz1Q+O41paWt58883KykqSFxue/bIs297eXlFR0dDQUFNTc9WjpXieb2pqOnz4ME3TN910E+laNbihXjVVVbdv375v3z5MewcAAPHHnJTKyPmYBwATGW8FeE+AQVdRUaEoys6dO++55x6znh+wLKvruqZpDMOQ2iiapvUc1WIs1XVdVdVe/zuQBqSNKIo9xzSRQjakgaZpV3TvStIHJDwqpoyLpmmxwfQap6ZpPM9v2LAhGAxevnz5zTffVBSl13zEFUVI07Tf7ydHOvAD6SkajQqCQPZrXIKeZ7j/2GJHk5HtkJ9jT5fxM8MwfV1Ho1QN2YXRwNg7GSBGmpEGsZH0tbqxEbJ30mCAg6dkWc7IyLjrrrva2tpmzZrVs1NV7GZVVe3rqrEse+jQoba2tokTJ06aNOkaO2cNrs7Ozo6Ojvb2do/Hg5H+AAAQZ9BHBgAA4pDP52tpaTHutIefruvhcJiiKKfTKYri5cuXJUlKTk52u92yLBt34xaLJRKJtLe3h0KhxMREj8fDcVzssBdSWiUajYqiaLVaLRZLz24UPM+rqtra2ur3+51Op9frtVgsA7mppmnaarUqiqLrOknECILQ1dUViUQYhnE4HAzDkBPYT5yqqno8nvT0dKvV2lfXkquI0MgjGL9aLBaGYWRZliSJVOoRBEFV1Wg0Gns4DMNEo1GS0SBbYFmW5/lgMKhpmt1uZ1k2dtd9xUZ2wbKscX4EQdA0LRgMKopis9msVquqqpIkkUUWi6W9vb2jo8Nut6ekpJAVjeB5ng+FQpcvX1ZV1ev1JiQkGGkXVVW7urqMQj/RaLSrq0uWZY7jSC6y/9XJAZLxZW1tbTRNJycnu1wuVVX7T+uQc0XT9J133knTdFdXV7euVWSzfr+/vb2dZdnk5GSn0ynLcrf/U6SbT1lZGcMw8+fPt9lsxhUZCZxOpzEY0OxYAAAABhkSOgAAEIfMrZ7DcdylS5f+93//1+12z5kz54svvqivr6coKjExcenSpfPnzye3+haL5ciRI7t3725qalJV1Wq1FhQULFu2bOzYseTmk3T32Lt375EjR/x+v9vtnjp1qqqqsUcnCEJtbe2uXbvOnTsXDocFQcjOzr7tttuKioq+MWMSiUR2797d3Nys63ooFFq1alVNTc3BgwcvX74sCEJOTs7dd9+dmJjIcVz/cRp5jV53dNURGnie7+rq2rVrl9/vz8rKmjt3Ls/zZ86c+cc//pGRkbFw4UJFUcjhfPTRR52dnYsWLRozZoxxmJ2dnW+88cbp06c1TUtLS7v55psLCgrIrvuJTdO0M2fOHDlyRJKkaDSakZFRXFy8Y8eOCxcuRKPRxMTEW2655ZZbbnnnnXe+/PLLBQsWRCKRgwcPRiIRnucLCwvvuusun89HAtN1fffu3aWlpS0tLbquJyQkzJw5c/ny5VarlWXZysrKl156iWEYkn/ZtGkTSTnNnj179erVJJ3U1+qqqrIsGw6Hd+7cefTo0UAgQFGUx+OZMWPGwoULExMT+0pochz36aefNjc3k5yRoigLFiwYM2aMcRF5ng8EAjt27Dh+/HhXVxfJE910000333yzkeYzru/hw4cvXryYm5s7efLkkZY3Mf6zxF9FLQAAACR0AAAABhmZ8ae1tbW1tbWyslLTNKfTGY1GyaAkj8dTVFTEMMzhw4c3bdoUiURcLpfdbu/q6iorK6upqfnhD3+Ynp6uKArLsps3b969e7eiKBaLpbm5uaKiwuFwGJ10eJ5vaGj4y1/+0tLSkpCQMHbsWL/fX15e3tDQ8IMf/KCwsLCfu2uapqPR6O7duy9fvuxyuUiPkoqKCp7n7XZ7MBg8ffp0MBgcM2ZMaWlp/3H2cyquJUKC47hAIPDqq69+/vnnmZmZc+fOJUOTzp8/v3379pkzZy5evJh0LxJFcd++fQ0NDVOnTs3MzCTdoDiO++KLLwKBgM1mUxSlpqamvLz84Ycfnjhxoqqq/cQ2efLks2fPbtu2ze12kwzdP/7xj9raWo/Ho+t6bW1tVVXVkiVLAoHA5cuXP/nkk0Ag4Ha7rVZrV1fXV199pWnaI488QgZSbd68edeuXRzHjRkzhuf5xsbGnTt3BoPBDRs2kDxOZ2enMbiMZE9EUSR9dr5xdYZhtm7dumfPHo/Hk5eXp6pqfX39li1b7Hb7smXL+jq9HMft37//2LFjpKuRKIqTJ0/OzMwkV5NkxzZt2gppW/MAACAASURBVHTs2DGLxUImwGpoaHj77bcDgcCaNWuMhA7DMIFA4Msvv6Qo6qabbnK5XCOqew6FIb0AABDXzKyhg49YAACIV2Q+x3A4nJWVtXbtWo/HU1tb+9Zbb7W3tx88eHDatGkdHR07duyIRqMzZ868/fbb7XZ7bW3te++919zcvHPnzu9///uCIJw9e3bv3r0sy86ePXvu3Lm6rn/55ZcnTpyI3dHOnTsvXbo0efLk733veykpKX6/f9OmTSdOnPjoo4/GjRvHsqzVau31A5emaYfDsW7dulAo9MUXX/j9/nPnzs2ZM2fx4sXhcPiFF16gYrpp9BPnN56K/iMklWv6WpfjOFEUX3755bKysmnTpt17773p6emiKJLhSHa73WKxxBajsVqtdruddIohL5KRU6tXry4sLOzo6Ni9e3ddXd327dtzc3OtVms/sRUWFk6dOjUhIaGurq6srKytrc3pdD7wwAPjx4/fsWPH/v37jfFQJMhVq1YVFxerqrpr165Dhw6Vl5fX1dWNHz/+zJkze/bssdvtq1evLikp4TiutLT0rbfeOnz48I033jhp0qSsrKynnnrq0qVLL730EkVRGzduTEtLk2XZarVSFFVVVdXP6kVFRZ2dnZWVlQzD3H333QsWLOjq6jp79mxDQ0NJSUk/U1bJsrxs2bIbb7xRkqTPP/+8vb099qQJgrBv377jx48nJSXdcccdN9xwgyzLn3zyycGDB/fu3Ttt2jRjFjNBEL788su6urr09PSZM2eO5KnEAAAA4o9pPXREUcR0AwDXOfIUmkJPeIhfqqreeuutkydPDofD6enpVVVVu3fvbmtrUxSlvr6+qanJ6/WuXr06KytLkqSsrKxgMPj666/X1NS0tbWlpaUdOXIkHA4XFBTcd999drudpulx48Y1NTXV1dVRFMWy7KVLl6qrq+12+9KlS30+X1dXl9vtLikpOXPmzKVLl0KhkCiKe/bs6VkWWtd1lmUXLVq0ePHiaDR67Nix5ubmiRMnbty40el0VldXk+E/LMvW1tb2H2dSUlJftVpYlm1paeknQr/fn5iY2NfqpJ8IyeY4nc5169ZlZmZGIpErugSyLM+bN2/t2rWSJAmC4HQ6//a3v9XW1l68eNHj8fQTW1tbW0FBwZQpUz777LODBw/yPL9u3bqSkhKSISIjoYxd5Obmfvvb3yYdapYvX15eXt7R0XH58uWJEyeeOnUqHA7PmjWLZFhkWZ41a1ZpaWl5eXlNTc2kSZMEQSCVlcjWvF7vmDFjjFI1/a9eVFRks9kSExPr6+sPHDjgdDoLCgpmzJgxZcqUaDTaT6ZMVdXZs2cLgtDR0XH48OHYljRNK4py6tQpXddvvPHGxYsXi6LIsuzatWtra2tra2vLy8sLCgrIBQqHwwcOHFBVdebMmT6f70qvDgAAAFwLcxI6U6ZMycnJcblcpuwdAEYInufXrl2r6zrP82bHAjD4dF23WCxer1cURVVVZVlOTEw0Zom6dOmSLMtpaWljxowh5ZNFURw3bpzdbu/s7PT7/SkpKRcvXqQoauLEiXa7nRQqpmnamBOajHYJhUI8z2/evHnz5s0URdE0raoqqQEcjUY7Ojree+890tcjlqZpgiBMnz6d3ISTWZOKiorIiCG3233fffdRFJWUlHT69Ol+4uzo6PD5fP0kdPqPMBQKeTyevlbnOK62tvbcuXNkTNCJEydyc3Ov4kLYbDZZlkVRVBQlJycnJSWlpqamtbWV47hvjC0cDkuSpGma1+stKCgg52ru3Ln5+fkpKSlkgJKu68nJySzLRqNRlmUFQbDb7R0dHWRpc3OzIAgNDQ1PP/20MRlWMBhkWba1tZWsriiKcRJUVVUUxRjI1v/qJDG3cuVKv99/4sSJioqKvLy84uLi2bNnOxyO/vvLkBMSiUS65X3I9js6OliWnTBhghGPy+XKzs6uqalpbGwkLQVBOHHiRHV1dXJycv8dggAAAGAomJPQ4Xne6/WasmtD7ASl3b7KkEXU1zODxi4iPauNBmQKiZ7lA4yJS2Nf1L/WM5he2xvILC3o0ARxKSEhwewQID4pijIS3jYFQeA4znh7jw2JjFhhWZZlWXInTG7OOY4jkzSR6ZwYhrHZbMaKsZ8jpCeFoigcxwWDQaMBTdM2m41M55SQkLB48eKeOVOyL7vdHptMcTqd5OPGZrPNnj2biulG11ecfU1SPsAIBUHof/y1oijFxcUej2fXrl379u2bOXMmGY70Def9/zI+6HVd5ziO53kS88Bj03XdarXyPE/OT15eXkFBQew03rHj2oxrRPYiiiI5jWTmLPLdg2VZh8MxkCdb37i6LMvjxo376U9/Wlpaevjw4crKynPnzu3fv3/Dhg3Z2dlXl2Qx/vt0u0Ck0A+pkkPmjTpw4IAkSTNnzkxNTSV/KiMQOZYBTuUOAAAwilynRZF1Xe/s7NQ0jWEYt9tNxRT0oWmazEhKURSZIDZ2SLkoiufOnWtoaPD7/TzPp6amjhs3LrZrNPV1mUlj/lHjRZ7nbTYbmQw19jt9r+27RdstEgAA6F96enpLSwspZ2tiGH3l8SmK8nq9NE37/f5gMGiz2UjHkLa2tlAo5Ha7nU6nxWIhqZyWlhaO48iU0hzHGZN5k1rLDodDFMX7778/Ozub3PxzHEc+ZZxOJ8uyDz30UF/hdZvZOjYlQW7OSQ+jfuJ0u939JM6+McKEhATygUsyX6Qrk7G6oih5eXn33nuvoijHjx+vq6v77LPP7rnnnm7RGp+esdOcxzKexLAsS7re0DTNMMw3xkbmkOq5QTL0iZyfbsH05PP5SM7lu9/9LhkGRR4OSZLkcDi6FS0mgcUe1EBW1zQtJSVl1apVCxcuPHXq1J49eyorK7dt2/boo4+SBBCZ9F3TNJIV6ivU2KtG/vYuXrxIJiMjfZeam5spiiIziAmCUFFRUVFRkZiYOHfu3JGQP+0Vx3EZGRnRaDQ7O9vsWAAAAAbZ9ZjQYVnW7/f/6U9/am1tpWn67rvvnj9/vjEpgyAIf/vb3yoqKiiKWrFixW233Ua+1AqCcO7cuffff7+mpoY80yNf+5xO57x582677TaO48jXUEEQ9uzZs337dmPGCoqiGIZJSEggM5vMmjUr9jtcr+1jSZIUGwkAAHyjzMzMzMxMs6Pok67rGRkZLpfr4sWL+/fvX7JkCc/z7e3te/fuVVXV6/X6fD5N03Jyck6dOnXy5MlTp06NHz+eoqiGhobOzk5yz09aer3e8+fPnzp1atasWWQ0VnV1tcPh8Hq95P6/nzttUkWYjOQipWEcDofRRYiiKE3T+o/T6/Vqmma1WgVBMLIbgiDYbDYy1ZfH4+k/QoqiWJY9fvz4hQsXbrrpptgBXJqmud1um82m6/ott9zy97///fDhwyUlJWPHjqUoiud5hmHa2tr8fr/H4+E47uzZs+3t7d1SMDRN19bWBoNBq9VK0/ShQ4daW1sdDkdqampiYmL/sbEsa7PZyOsMw5AazLIsX9FETjk5OQzD1NbWdnR0kNnQA4FAXV1dQUFB7NMgkmchqSKHwxEKhaLRKJk8vv/VOY5rbW0tLy+fM2eOx+NZtmyZ1+t95plnLl26FAgEEhMTyZz0u3btSklJmTFjhhGYIAiCIJDnSeTq22w2iqIkSbJarVlZWefOnSstLZ04cWJqaiopyH3hwgWWZcnAN03T9u3bFwqFFi1aRIorDfycDCeGYZYsWWJ2FAAAAEPCtIQO6TZs1t4piiJd2Wma3rp1a05OTkZGhvFdRFEUkjoxvlNaLJaTJ0++8MIL4XBYEASGYYxnfeFwePv27S0tLRs2bGBZ1ujWSx70xX6T7urqamhoOHHixIEDB9avX5+bm2vssdf2BjLKfRjOCcDwix2YAHD9kGU5MzNz1qxZJKF/5syZxMTEurq6ixcvsiy7cOFCq9WqKMqcOXP279/f0dHxwgsvFBQUMAxTVVVlJHR0XXc4HAsWLKipqdm/f384HL7hhhv8fv/nn3+ekZHx8MMPk04WffXIICWHDx06FA6Hu7q6LBbL4cOHGxoaRFFcuHBhamqqoiiyLGdkZPQTp8PhaGtrO3bsmK7rfr+f5BeOHDlSX19PUdS0adO8Xm//EbIsW1dX98ILL3R2dtbV1ZFOJUaQZIiTLMvFxcUHDx6sqKjYu3fvfffdR9N0eno6z/NkJvji4uJIJLJ79+6en6E8z3/11VctLS1paWmhUKiyslKW5WnTppHV+4nN6XRWVVXV19fX1tYKgtDZ2fn222/rup6amrpgwYIBfi4rijJ16tS8vLzKysrnn3++pKTE4XCcPHmyoqJiw4YNxcXFJGCST2FZNhKJvPPOO8ePH7906dKCBQuKior6X52iKFEUX3/99WPHjh09enTixIk8z586dUpRFK/Xm5CQQIolvf/++59++qnVarXZbFOmTJEkiWXZI0eOdHR0SJIUjUZ5nidXjWXZadOm8Tw/b968r776qqam5n/+53/y8vIikUhVVVU4HC4sLJw8eTJFUbW1tadPn3Y6nSUlJVfzfwAAAACumTkJnaqqqsOHD8+aNauwsNCUAKivezVzHBcIBN59991HH32UYRjyvapbh2fSo+edd96JRCLk0dyYMWOys7Oj0ei5c+dEUbTb7YcPH87Jybn11luNgeXkgSfLsqRyARkAL4qiIAi1tbXPPffc448/bhQC6Nk+FhnwP8znB2AYKIrywQcfKIpyxx139DquAWD00jSNlBCOHZAry3JXVxf5pNA0bcWKFZ2dnSdPniQJEZZlXS7XrbfeSiaT1nU9MzNzzZo177zzTmtra3Nzs67rPp+PZdnOzk7SUVQUxRtvvPHy5ct79+4tLS0tLS0lFXB4npdlmXS46AsZ8Pvuu++2tLTYbDaGYQ4dOkQeaUycODEjI4PkLPqPU1VVv9//2muvkYmQyKfVhx9+qCiKxWLJyclJSkoaSIQk8WTUiDHOFXnaQVZZunTp2bNn9+3bN3369OnTp+fn5xcVFR09erSsrOzo0aNka7qud3V1aZpm1K/p6upKT0+vq6srLy///9i70+CozjNv+Gc/vaq1tHYBEpLQgjY2YRCLIcbg3WCwHQfjJXY8iWcm8ySpmrcqU5VM1VTNVE1qqp7Jh8RxnGA7XmIbYxYbsLENNhKLWSUsxCK0gPal1VJvZ38+3K9PdQnUEljoaPn/PlCo+yzXOael7nP1fV8XwzA8z+fm5j7yyCOjnj2SGXnnnXccDgfP811dXbt27YpEIhUVFWvXriUnh9SRCQaD5CsiciyGYYTD4WAwSCrROJ3OH/7wh3/729+am5vfe+89shiZSGXm2jRNS05Onj9//pEjRy5cuHD27FmbzbZhw4ZRVydVgcrLy9va2s6dO3fmzBmyQHp6+n333UdmZpmn1zwtFEXxPP/pp5+eO3fObrdzHEfT9P79+yVJSklJKSoqcjgcc+bM2bJly86dOzs6Oq5du0bTtCAIeXl5W7duJcOvampq/H7/4sWL8/LyUA4ZAADAEtYkdBobGxVF8fv9lux9GFEUv/3224MHDz744IM3HUTN8/zx48fb29vtdrssy8uWLduyZQsZo15fX799+/ZgMMhx3Ndff11ZWelyucwVZVnOy8t79tlnSVXLQCDw5Zdfnjp1ShTF3t7e3bt3v/jii9HfQ0YvHx0A+Q520g5mBrhtg4OD5O/ASIUqAKYoTdM8Hs/jjz9OfVeKhaIoRVGKi4ufeeYZj8fDMIyqqnFxcS+88EJdXV1LS4ssy263u6ioKDc312yJLUnS8uXLMzMz6+rqBgcHnU5naWlpT09Pf39/Tk4OuaVnGGbjxo1lZWUXLlwIBoMkYVFUVGROBB4JSV5s2rQpHA5H/wJqmkZqw5k/xo7T5XKtX79e0zSapsmbGkk0sCzrcrlI4ilGhLquZ2VlPf/881evXq2qqiLpG3Kunn322eTkZBIJSTM9//zzg4ODHMeRhMvWrVsTExMvXryoKMqsWbNWrVrl9/v9fr+51po1a0pKSvLz84PB4MWLFw3DSE9PX7BggdvtJgvEOHuSJJWWlpIxROabtaZpiYmJ5slRFKWyspJ8zUMeJBPQHn744UAgkJOTQ9pXZWdn//znP6+tre3o6CBbKC0tjT7JJIf1xBNPZGdnd3V1kfFH5CgMw4i9Ok3Ta9asKSoqqq+vJzVukpKSysrKUlNTyScHRVEeeeSR+Pj45OTkwsJCshapNj1nzhySzSExkPwRKYSsKAqZ3VZXVzcwMMAwTGZmZnl5Ofmcc/369VOnTtlstqqqKpZlMY4YAADAEtYkdLxeLxmtbcnebyQIwoEDB8hnuGFD08k3eOfOnSOfVzIyMjZv3my328lHtPLy8gceeODtt98WRbGrq+vKlSuLFy821yUjqNPT0yVJMgwjIyMjJyeHpumTJ0/abLbz5883NTXl5eVFLy+KYlZWllkrJ7qOwKQtNwhw21wuFyZbwR0SiUR6enrsdrvX6534veu67na77733XoqiJEkyZ+Pm5uYWFhbquk6q26iqyrJsZWVlZWWlrussy5LmVtGbkmV59uzZ2dnZpJC/rut5eXkMw8iybI6g0XU9Nzd33rx55hAMWZZH7elD3nTuvvvuYW0WycidYcWJR4qTpK42b958010oimLW4okRoaZpCxcuXLRokdk40jxXZEoy9V1rrVWrVjEMY9YkdrvdTz75JHmTJWWVSddIM/7KykrSnIum6YqKCoqiyKkzT3Lss0diGHZyzJBInCUlJRUVFaqqkuwJOaurV6+OvkaKojgcjlWrVpl9x8l0tmGvGUEQ1q5da05ENQsYx17dMAxZllNSUjIyMkjY5BNL9DHGxcVt3LiRpGnINlVVJZf+xleF2eJKluWMjIzZs2eTbJ156kRRrK6u7u7uLi8vLy0tnfxfOHV1dSmKkpqaivHOAAAwzViT0Jk8t3DkkxnDMJIk7dy5Mysra1gTZYZh+vv7+/r6yMejioqKuLi4cDhMnpUkaf78+YmJiYODgxRFtba2Rid0qO8+GJkfT0VRXL9+fX19Pangc/ny5fz8/OhgFEXp6ekhn41I/cXJc64Axh1e3nDn1NTUtLS06Lq+bds2S+7idF033yxMZibCZPaTIm8BN92UORDDvL2/6TIkbXFL/RANwxhjfd8YcZKEwqhbiB3hjVu46bkaFi1JNJDre9MwhjUTGGnvI8V2Yww3jfzGcbU3nlWSxYsRA1nGLKh3q6ub7Rqom71ChrUzM1cZ9QVjbtZcjGXZvr6+y5cvp6Sk3H333TzPT/KODUNDQ3v37qUoauHChQsWLLA6HAAAgPE0E7tcRaNpOisr6/r164IgXL169eOPP3766aejFyBTpYLBIPkWKysrK3qkjKZpCQkJXq/X5/NRFNXb2xt7d7IsJycnp6SktLS00DTd3t4e/Swpr/Pb3/6WoihSzvDll1+Oj48f9VtWgCnqlu48AW4Jz/OCIMQoCTzZjBrnWA5kAg72e+5i3COM0Rj+Vvc+MS+V73mhx/cQxrh89GKapjkcjn/+538mBYkmeTaHoihS/YeKqmYFAAAwbQwfajvTyLJ8zz33kInooigePnz4zJkzZuNVKqqYMfnWy+l0Rq9OxniT2eYURQUCgdi7MwzD4XA4HA7yqYKM64lGvtElbqkrKgAARHO5XLh/A7gTGIYhjeqtDmRMzA91GBMKAADTz0xP6JDigps3b2ZZlpQD3L1798DAQHR9H57neZ4nKZth4+fJFHezt0XsfiJE9KDoG5dnWdb5Hcy3AgC4bVNlYA7AVERqD02J37IpESQAAMDtsXLK1SR5i5UkacGCBWvXrt2/f7/NZrt+/TpN02ZzEF3XXS6Xy+UKBoMURXV2dkZXECQdzfv7+0mFnVFLb3Ic5/f7SUUeRVFSUlKinx3W5YrU0ME3zAAAAAAAAAAwjDUjdEib0ht7K1hFUZT77rsvLy9PkiSGYaLHxWiaFh8fT5rOMgxTW1sbDoc5jqO+m5X97bffkgQN6WN148bp7zAMI4riyZMne3t7WZZlGCYnJyd6STKBKyMjIz09PT09PSUlhQwUMhvBAkw/uq6TsqZWBwIAAAAAADCVWJNSmTVrVlpaWlFRkSV7v5Gu63a7/fHHH3e5XMMqEBuG4XQ6i4uLVVXleZ4UTialcGw225UrV/bv308auCYmJubn5w9bnaZp9juGYVRXV+/bt4/nedIKdN68eTe2ojC+Q1GUue7kSX4BjCOO42bNmrVw4UK0koXpjbwXfM/EJcMw5O0ACVAAAAAAoKyacpWWlvbAAw9YsuuRyLKcm5v74IMPvvvuu9EFdCiKUlV1xYoVx44d8/v9giB89tlnzc3Ns2fPDoVC58+fHxoa4jguFArdc889qampkUjEXJ3n+c7OzldffZXMM+/r62ttbaUoyjAMmqbvu+8+l8sV3R4ievlhAXi93vvuu4/juEkyTw1gXDAMs3btWqujgOmJ/LWcJF0CaZoeGhqy2+0Mw9zGn3HSTigcDpPW2jabjaZpTMgFGDvDMFRVtToKAACAcTbT25ZHi0Qiq1atunTp0qlTp2w2m/m4qqrJycmPPvroG2+8oSgKx3GXLl2qr68nU64YhgmFQsXFxevWrSO1b0wMwwwODtbU1JBvU8k3tKqqCoLwwAMPLFq0KPbyJlmW58yZs2HDBpqmkdABABgLlmXD4XBFRYXl478EQfjqq68+/PDDxYsXP/HEE7f6l5ymaVVVP//889raWtJLMT09fcuWLfHx8ZMkXQUwmZF2pYIgTJ6B4QAAAONlhiZ0DMMIh8OhUIhU8yEJFMMwGIbZtGlTS0tLe3u7pmnku1CKoiRJuuuuu1iW3bNnT1dXl1kASJIkm81WVVW1adMmh8NBvvyhaVpRFLJxc48k+yMIwrx589atW1dcXKwoCvlMf9Plo5FeEhNwWgAApo3S0tLZs2cnJCRYPkGJYZhvv/22s7Ozvr4+HA47HI5bSugIgnDgwIH33nuPFGJjWba/v3/9+vVJSUlI6ACMiuf5xx9/nOf5sbQiBQAAmFosS+iQaUeW7FrXdZvN9tBDD4XDYcMwkpOTzUI2iqJ4vd7nn3/+ypUrFEXl5eVFP1VZWTlv3rxvv/22paUlGAyyLOv1egsLC3Nzc6OH8iqKUlxc/KMf/cice2UYBsdxHo8nOTk5IyOD47josTk3Ln9jwG63+/YG6gMAzEwsyyYmJlodBUVRlKqq69ev53m+tLTU5XKZbxakGg7J1zMMQ/7Ia5oW/aee1M2pr683DKOoqGjjxo0Oh8Pv9yckJJhfIZAlyVpmhZ3oltJk42RkEL4hgBkoLi7O6hAAAADuCGsSOi0tLcePH1+/fr3H45n4vRuGIYri3XffTUbZRCKR6C85FUXJzc0tLCwk/zcTOoZhSJLkcrlWrFixfPlysgrP87qum2NtCE3TyBbMB82P0ZqmaZo2bKbVjcsPQz7xRyIRJHRgmtE0bd++fV6vd+nSpZYPowAYdyzL2mw2wzCKi4vnz5+vaRqZM0XIsqxpmiAIoij29/f7fD6Hw5GcnEwm51IUZRhGJBIhqRnDMAoLC3NycsLhcHx8PHlbsdvtZJypqqpkHGgoFAqHwwzDOJ1O8h4nCEIwGBwaGvL7/Xa7PSkpyW63D3sbAgAAAICpyJqEzoULFyRJqqurW7FihSUBkE/JIz0bnccZhmRkzDvPkTYSYwvjsjzA9OD3+/v7+3t7e8vKyhwOh9XhAIwnjuO6urq+/vprMvpS07TU1NSVK1eSZI0gCPv27Tt27NiqVasikUhNTU0oFBIEoaCg4LHHHktKSjIMw+/3//Wvf/X7/YFAwOVyffXVV998842qqvHx8c8//7woip999llXV5dhGIFA4KGHHmptba2pqenp6REEITs7+8knn6Qo6siRI3V1dZ2dnYqiMAyTmpq6YcOGxYsX400HAAAAYKqzJqGTnJzc0dExde/fMFIGYFy4XC5SLNzysrUw/UiS1NPTY7PZvF6vJQFwHNfT0/P3v/9dFEWe5w3DKCkpWbNmjTlVyu/3d3d3Hzx40O/3u91uURRDodCJEyc0TfvJT37CsizJ1Ph8PjJhKhKJSJKkqirHcQzDRCKRffv29fT0uN1ulmUVRWloaGBZ1uFwDA4Onj9/PhwOd3V1vfvuuy6XKzEx0e12k2aLb7zxRnx8fH5+PsbpwAzR1dWlKEpqaireawAAYJqxJqGDuRUAQN1Q/gNgHFVXV7e0tOi6vm3bNkvu4hRFSUtLe+GFF0RRbGhoOH36tCiKw+rjcBwXiUQefvjhpUuXkhmIJ06cqK+vb21tzc3NdTqdL730Esuyr7/++oULF+6///7Vq1dLkkRmcqmq+vjjjwcCgSNHjgwMDFy8eHHx4sVr164Nh8N/+ctfKIrSdT07O/vBBx8sKyvLzc0VRbG3t/ePf/xjY2PjuXPn5s2bN/HnBGDiDQ0N7d27l6KohQsXLliwwOpwAAAAxtMM7XIFAJMB8jhw53AcJwhCdG3gCaZpWmJi4kMPPSSKoq7r33zzzY3LKIpCci4kuXP//fc3NDT4fL6enp68vDyGYZKTk202GzkQl8uVnp4uSRKpnSwIwtq1a2VZPnfuXFdXV3Fx8fPPP+9yuRobG0mVN1VVExMTn3rqqYGBgZaWFsMwZs2aVVJS0tjY2N/fP+HnA8AapLwURVEoBw4AANMPEjoAADANud1uy+/fdF0PhUKapo1UsMYwjJSUFJ7nw+GwpmmiKDocDp/PZ3bC0jRNVVWSkyLFj82nDMMIh8OyLJOk1fz58202WzAYjIuL27ZtG0VRXq93cHBw586dZ86cCYVCuq7HxcW53W6e50Oh0IScAADriaJI/oPh4QAAMP0goQMAANPQVBn/ZbPZzMQT6WZF3dadJ0lg6bput9srKytpa/KJ9AAAIABJREFUmlZV9fXXX//qq6/cbndBQYHb7e7s7Ozq6qJpGne2MHNMlT8FAAAAtwEJHQAAAMuM192muR3DMCRJ4nm+s7Ozrq7O4XBs3bp1yZIluq7TNL1r167du3ePyx4BAAAAwFrWJHQ0TdN1nUzyB4CZzPJJMQB3DsMwoiiKoshxnGEYDMPY7XaGYcbYMpzU/iCrGIbBcRz5vyRJmqYxDGOz2UgDLMMwBEFwOp2kyjJ5e1UURdd1juPS09MdDoeqqpFIZGBgAMNzAAAAAKYHaxI6aWlp169ft6qVLABMEuRWU1VVlmWtjgVgnLEs29/ff+7cOVEUGxsbRVH0+XwHDhyQJCk7O7ugoCD26qRP+fHjx3Vd9/l8ZCNk9fLy8qSkpGAw+M033wSDwWAwKIriN998097eLknSypUrU1NTNU3zer1er7epqelvf/tbeXm5YRgNDQ2XL19G52YAAACA6cGahM6sWbNmzZplya4BYPJgGObee++1OgqYniwvnMHzfFdX12uvvSaKIsuyLMu2tra+9tprkiQ98cQTJSUlsiwHg0FZls0hM6TOcTAYJFnOSCTywQcfdHd3k4E5x48fr6mpkSTp3/7t3zIyMvr6+t577z3z2WPHjqmqKklSYWFhZmZmJBJxOp0PPfTQG2+80dDQcOHCBV3X4+Pjk5OTm5qaJEnCOB2YaSz/mwAAADDuUEPnjiAD4K2OgqIo6sbil2bRzclg8pyoUZEzOfHzg8h8iu8/P5EMgbGwhTPAxJMkibKutQ3pGv7ggw9yHDfs8dzcXEmSlixZkpKSMmfOHDIDS9d1m8324IMPBoPBnJwcWZbtdvvGjRvD4TDDMNGrp6amjvSspmlpaWlkg7Isl5eX/+M//mNtbW0gEBBFsbS0lOO4CxcupKSkjHHaF8BUR9M0+VOAoaAAADD9IKEzzjiOI1+rTpIvPyVJMgwjOhiO46I//d8emqbJLUr0d8u3ShRF0oJ3kpyrGMhJCwQCgiBM5H4ZhpFlWVVVp9P5fXI6NE0HAgFFUURRtNlsyOnATFBWVpadnS0IglUzjFRVTU5O/tGPfnTjU5qmRSKR0tLSBQsWqKoqyzJFUYZhiKK4Zs0a8osvy7L547DVI5FI7GfNPxeyLGdnZ+fm5pKaOyShX1BQoGkaucUFmPZ4nt+yZYuqqvHx8VbHAgAAMM6Q0BlPNE339/cfOXJk9uzZCxYssPz7T57nGxoa3n//fZJ8ITcJzzzzTF5eHrl/+D6uXLnS1tZWVVV1G9kBksGpra09f/78vffeGx8fP5krZDMM09XVdfDgQafTuXHjxgm7rCzLDg0N/eUvf+np6fnxj3+cm5t7e7vmeb6jo+P3v/99IBB46aWXyESPcY8WYLLheT4pKcnaGAzDuOmvLcmzk6zNsMcjkQj5PxnAaP44TOxnoymKoihK9HBIy9+bACaYx+OxOgQAAIA74vuO1Lg9kiRdu3YtHA5bsvc7hGEYVVW3b9++Y8eOYDD4/UfBfH+apuXn53s8nvb29p6eno6Ojvb29u8zpoYQBOGbb7753e9+980339zeiBWe51taWn7/+9+fPXv2+0QyMXie//zzz/ft2xcIBCbysrIs29fXV19f39ra2tTUdNtjxVmWra6ubm9vnzNnzrx581RVHd84v6fu7u6Ojg4MGoLpyrgZS8KY+J0CAAAAwB1lzQidmpqaK1eulJeXV1ZWWhIARVHkzlzXdYZhzDIlN1ZIMZ/VdX2k+iNkU2Q0eyQSEQRh2G3/WDYykuhimTRNky0bhhEdKnmcBEB2QR7XdV0QhG3btg0ODvb09Lz33nsjzW8aaQsjheTz+ciRjv1Ahm1BlmVN00RRNPdOjdDBOnZssc/PGK8yNfI1YhiGZFJIWVOy2I2hxr7E5rOGYWiaNsYXgKIomZmZGzdu7O/vX7Ro0Y3DasbyuuI4rru7+/Tp04IgrFy50mazjeUr/QkzNDS0Z88eiqKefvrpCZ7OBgAAAAAAMKVZk9BhWVYQhGF1IieSOVLd6XTKstzV1SXLstfrdbvdiqKYN8aiKEYikZ6enmAwGB8fn5CQwDBM9GB1mqYFQZAkSZIkm81G7vmjd8QwDM/zwWCwt7dX07TExMS4uDhd18cyw4jneZZlVVUlWQCe53VdJ91PyL7IRkiWwe/3+3w+lmW9Xq/T6VQUhWQcNE1LSkrKzMx0Op0jDcwhW/b5fAMDAy6XKzExURCE2LNyzLyG+aMoiuTkkBFANpuNYZjoUg48zwuCQCpHUFHVmsltfDgc5nnebrebkceOzTAMQRBinB+bzaYoyliucuxrJMsySZeQZFAkEiGFJ3ieJ/GPeolJwL29vYFAIC4ujhzCqNUryAmkaXrz5s0URYVCoWFDq0Z9cZon8OTJk52dnfn5+eXl5ZOtagb5DbI6CpieFEXp6elJT0+f/FW6AOCO6unpsdlsbrfb6kAAAADGmTUpFbfbPfHdgkwcx3V2dv7lL3+Ji4urrKz8+uuvr127ZhhGQkLCunXrqqqqyJwUURTPnDlz4MCB9vZ2TdNsNtu8efM2bNgwe/ZskuwgGY2vvvrq5MmTAwMDcXFx5eXlmqaZNw9kUMnBgwerq6u7u7sNw/B4PIsXL96wYYOZjokRZENDw+nTp2VZjkQi6enpS5cu/fjjj5uamiKRSHx8/Jo1a6qqqiiKGhoa+uSTT86ePRsIBGiaTklJWb58+apVqxiGMXM6siyPVDRBEITW1tb9+/dfvHiRZFXmzJmzYcOG4uLiMVZa4TguHA5/+umnAwMDmZmZVVVVkUjk4MGDg4ODq1atSk1NVVWV9FU5d+5cRkbGypUrzXUZhjlz5sy5c+f6+vqcTmdZWdnq1at5nicnJ0Zsuq7HPj/33HNPXl7eK6+8Evsqx75GLMu+9dZbjY2NkiQ5HI66urrm5mZN0wRBeO6559LS0si4mBiXmOf58+fP79+/v7W1ldQknjt37urVq4uLi6mRJ0FwHPfll192d3ezLEvTtKqqK1asIGeSLDDqi5NgWdbn89XU1DAMs3z5cofDMamG51AURYZoAdwJx44du3TpUn5+/sqVK5HTAZixAoHArl27OI575JFHEhISrA4HAABgPFmT0LF2Mj9N04qidHd3d3d3X7x4UdM0l8sViUQ6OzvfeeedhISE+fPn0zR98uTJv/71r6FQyOVy2Wy2YDB47Nix5ubml19+OT09XVVVlmV37ty5b98+VVVFUWxvb6+vr3c6neYgHbLAxx9/zLJsamoqqU27Z8+ewcHBrVu3xu7YTTIgH374odvt5jguPT39zJkzzc3NpEdDU1NTVlbW6tWrh4aGXn/9dTKhxuVyaZrW0tLS0tLi9/s3btw4ataM47i2trY//vGPHR0dHo8nMzNzYGDg/Pnz165d+9nPfpafnz9qTodkc956661Dhw5lZGQsWbKE47hIJPLll19ev369pKQkMzOTJHSuXLny0UcfLVq0aM2aNeTAWZb1+/1vvfWWqqpk0EpDQ0N7e/vTTz9N0zTLsjFiKykpqa+vj3F+rly5Mnfu3BhXmdQGjn2NSGervr4+Mo1OluX+/n4ykY1MXou9OikV9NprrwWDwfT0dLfb3dfXR8bL/OIXv0hISBgpqcdx3OHDh8+ePWu32202myzLxcXF5ExSFCWK4qgvTrIdnufPnj17/fr1WbNmLVy4cBJWQkVdD7hzSBfwpqamu+66CwPBAGYs0j+OoqjLly9bONMfAADgTpihXa5I1+1QKJSZmblly5bExMSWlpb33nvP5/MdPXq0vLx8YGBgz5494XB44cKF999/v8PhaGlp2blzZ2dn5yeffPLCCy8IgnDp0qXPP/+cZdlFixYtX77cMIxjx46dP3+e7ILn+fr6+s8//9xut2/cuHHFihUcx1VXV7///vvHjh1bunRpUVERGVtx03talmXLy8tdLte1a9dOnz7d29vrdDqfffbZwsLCjz/+uLq6muM4nuePHTt25syZhISEhx9+uLCwUJblgwcPHj9+/IsvvigvL8/NzY2dkaFp+pNPPmlvby8pKXnqqafS0tJ8Pt/27dvPnz//6aef5ubmjpp1kmX5jTfeOH78eFlZ2bZt20jSgUy5cjgcZPwLRVGGYfA873A4RFGM3qAsy/PmzVu5cqXT6Tx9+vTRo0ePHj1aUlJSWVmp63qM2MgEIrfbHeP8kAhHusqlpaU8zzc2Nsa4RsXFxU888QRFUbt37z569OiyZcseeeQRMvUpPj6epukrV67EWL28vLyxsdHn8xUUFPzqV7/iOG5gYODo0aPZ2dmxG3spirJhw4bKykpFUY4cOdLf32+eSZZlBwcHY784yUYYhgkGg0eOHDEMY+nSpfHx8ZNteA7AHUUmP06G+vQAYCGbzUb+Y+FMfwAAgDtkRr+3aZq2YcOG8vLycDiclZXV2Nj46aef9vb2qqra2tra0dGRlJS0adMmMo1lzpw5gUDgnXfeaWpq6uvrS09PP3nyZCgUysvLe/bZZ0mFmry8vN/97nfXrl2jKIqm6fPnzweDwUWLFq1atUpVVVmWly5deuzYsQsXLjQ1NZWWlnZ0dBw5cuTGTxiGYTAMs3bt2gULFnz++efHjx/nef6JJ55YsWIF+aKJlIBRVbWuro7crq9bt06SJI7jHn/88dbW1tbW1vr6+ry8vBiHz7JsT0/PlStX7Hb7vffem5aWFg6HExMTV65ceeHChY6OjoGBAY/HM1LegZTIIdkcl8v15JNPzpo1KxwOj70Zk67rcXFx27Zty8jI0DStuLjY5/OdPXv29OnTy5Yt6+rqihFbX1/fvHnzysvLDx06NNL5iX2VI5GI3W6PfY2Ki4uTkpJsNpvdbtd13W63Z2RkkDI0ZG5d7NUrKiqSkpI4juvp6fnss8+WLl2ampr66KOPSpIUe7CMpmlLly4VBMHn8508eTI6BcZxXEtLS+wXJxn7IwjCqVOnmpubk5OTFy9ePNmaWwHcaRj/BQAU/hQAAMC0NnMTOuTO3+v1SpKkqqqiKAkJCWYfos7OTlmW09LS0tPTQ6EQRVGSJOXm5jocDr/fPzAwkJKS0t7eTlFUcXGx0+kMh8OkTrAgCOZHh87OTkEQ2tvb/+u//stsuuT3+1mW7e3t5Tiut7f3/fffN787MpH2T+Xl5V6vlxTlTUpKmjdvXjgc1nV92bJlOTk5mZmZPp+PFEIuLi7WNE1VVVVV4+Li5syZ09LS0tbWFvsMkBlPgUBAFMWdO3fu3LmToihS+lcQhEAgMDQ0FHtaUEtLy8WLF202myRJ58+fnzt37q1eAlLYmNROttvtJSUl586dI9mWoaGhGLEFAoHExERSKvim52fWrFkkrRPjKo96jci1IHWXScDkJJuHEHt1RVGKi4t/8IMfHD58+L333vvyyy8rKiqWLVs2d+7c2EOfKIoiAYfD4RsXi/3i9Pl8Xq9X13VZlqurq0mOKS0tDcNzAAAAAAAAphMra+hYWBeZIJ22zBvm6HjITCWO41iWJYMpDMPgOI4UiCFjMWRZZhjG6XSaKxqGEX37LUkSTdPhcDgcDpsPsixrt9tJvRtS25jn+WGBGYbBsqzD4SBbNgzDZrORLk66rufm5s6bN4+iqO7ubrN4cPR+SbWIUW/gSbVdUuBmYGDA3II5YWrYZm+kKMqSJUsSExMPHDhw6NChRYsWkTrBsfc77Eijz7/dbjefGntsNz0/DMNcvXqVinmVqdGu0ajxx16djLR6/PHH58+f//XXXzc0NBw4cODYsWPr1q174IEHbrWBvWnUFydpHVVbW3v58uWkpKS77rprkg/PwdenAAAAAAAAt8qytuWSJCUnJ1uyd9Ow/Eu0pKQkmqb9fv/Q0JDdbiftivr7+4PBYFxcnNvtNqfhdHd3k1IypC5PdL0Gr9erKEppaekPf/hDs1c3WdjlcoVCobS0tJ/85CcjxTZSd3NFURRFoWna7XaTpE9HRwcp8UvGsHR3d1MUlZqaGvvwdV13uVxOp1OSpB//+MezZs0yMwUk62EOzyE5EUmSouNRVTUnJ2fbtm2aptXW1l67du3QoUNPPfVUdMbE7CxjNikfhpwQ8izLsn19fSQJQtO00+kcNbabTu8i58dMk8W4ytRo12hYBSLzKMzxNaOuToYILVq0qKSkpKWlpaam5ujRox9//PHcuXPJJaO+a/qu6/oYe4qP+uIkp6impiYUCi1btiwrK2uydSs30TQtSZLL5UJpAwAAAAAAgFtiTbXIkpKSLVu2zJkzx5K9j8owjIyMDLfb3d7eXlNTQ1EUz/M+n+/LL79UVTUpKSkpKckwjDlz5jAMU1dXV19fT1IeXV1dfr/fzOmQBVpaWoaGhvLz83Nzc5OTkwOBwKxZs8jwDZK1uSky5sJut/M8T3IcDofD6XSa87MMw7Db7VlZWYZh1NTUtLW18TzPcdyJEyeamppYls3JyaG+G9Jit9vN/tCCIJDeSbquJyYmJiUlRSKRCxcupKen5+bmzp07l8x+yszMJIV4WZatq6vbuXNnf39/dAJF13WPx+NwONxu99q1a1mWPXHiREtLC8/zpNm2YRitra2iKJKYGxsbh+V0SA+p69evMwzD83xnZ+fp06cpikpPTxcEISEhIXZsZCDMSOdnjEa9RubZpigqEomQ0s6appGkyaircxx38uRJ8gopLi5+8cUXCwoKJElqaWkhZ4OULt6zZ8+JEyeizw+5TKIokjNp/jjqi9Pr9bIs29jYWFdX5/F4qqqqJvP4F57nt2zZ8uijj6JyLYy7yfzKB4CJh78JAAAw/VjzrTjHcUlJSZbseiwURcnKylq4cOGhQ4d2795dX18fHx/f2tra1tbGsuyqVavsdruiKJWVlaQD0Z///OeCggKapi9fvmwmdFRVraioyM7ObmxsfPXVV1esWOFwOOrq6hoaGrZt27ZkyRJzOtVNY2BZ9urVq21tbc3NzYIg+P3+HTt2GIaRkpKyYsUKMoNG07QVK1acPHmyubn5f//3f/Py8kKh0KVLl4LBYF5eXmlpqaZpwWDw6NGjFEX5fD5d11mWPX36dHt7u2EYZWVlSUlJK1eubGpq+vrrr0OhUGFhoc/nO3z4cFZW1osvvmiz2ViWvXbt2p///OeBgYGWlpaXXnopOulAck+KoixduvTo0aMXL1788ssvn3nmGbfbnZSU1NbW9sUXX4iimJycfP78+fr6+mGTy8hkpddee62wsFAQhObm5o6ODpvNVllZSbqMx4jN6XQ2NjbGPj+jGuM1oihKFEWGYS5cuPDXv/6VjBJ67LHHRl2d47gzZ8688sorHo+HVETu7++/du0ay7KZmZlkyzzP7969++DBg3a7/eWXXy4tLSXN1E+fPu33+yVJIlkkctUYhikvLyc9yEd6cZJBWzU1NUNDQ8uXL587d+6oveet5fF4rA4Bpi0yNu2mwwMBYIYgQ0Epihp70wYAAICpYoZOc9B1nVSTNe/YaZpWFCUYDJKJM4ZhPPzww36///z586dPnyYDVVwu17333rts2TIylWbWrFmbNm364IMPenp6Ojs7dV33er2kJq6qqmRC01NPPfXmm2+2tra+88475KYiMTHxppVuh+F5vq6u7t1333U4HGTsz4cffhgOhysqKu6++26SsFAUJTs7e/PmzR999FFbW1traytN0zzPz5079+mnn3Y4HBRFDQwMvPnmm5IksSxL8in79u1TVVUUxV//+tcJCQmkn9Thw4ePHDlSXV1NOqnTNC3LMhntQioBk3/JaBHzXJEKMrquOxyOdevWXbp06fDhwwsWLFi8ePHKlSsbGhr6+vreeusthmEURXE6nSRDQc6DruvBYNDj8dA0XV1dbZYN2rBhQ0FBASkNEyO2+Pj4Uc/PqFd5jNdI1/Xy8vKamhqfz7dv375IJHLPPfeIohiJRGKvrut6Wlra/Pnz6+vrd+3axXGcqqo2m23FihWkxzzZPjm9mqaZe+R5/sCBA7W1tTabjUxJ27dvnyzLKSkp8+bNc7lcMV6cuq63tbWdPXvWbrdXVVVh5AvMWGVlZXPmzBFF8cY6ZQAwc/A8v3nzZlVVExISrI4FAABgnM3EhI6maR6P57HHHqMoymzLrShKUVHR1q1b4+PjGYZRVdXj8bz44ou1tbUtLS2kJEpxcXF+fr7Z80iSpBUrVmRmZtbW1g4NDTmdztLS0p6enr6+vuzsbFVVNU3Lycn5l3/5l7Nnz3Z0dJApTqWlpRkZGbG7VpN4SkpKtm3bFl1bRNO0pKSk6HUVRVm5cuWcOXPq6uoGBgYYhsnMzKyoqHC73YqikPv8devWkR7b5lpmCoDkaB577LGysrILFy6EQiGO4/Ly8oqLi3meJxOLsrKynnvuucbGxpUrV5IzQ87V008/nZKSQoKRZXn+/PnPPPPM4OAgaWdeUVHx3HPPHTp0qLe31+l0Llq0KDs7u6mpKTk5maySnJz85JNPejyeWbNm1dXV+f1+0uUqPz/fTG0wDDNSbJIkxT4/Y7nKhmHIsjzqNVIUJT8//+WXXz5z5gzJyFRUVJgHHnv11NTUl1566eLFi5cuXZIkSRCEvLy8+fPncxxnhvTII4/ExcWlpKQUFRWRtVRVXbJkSVZWVvSNKBm1JIpi7Bcnx3HV1dU+n6+srKygoGCSD88BuHN4nvd6vVZHAQDWi4+PtzoEAACAO4L+zcH/71DT52El/O8/+M8N8x6cmL1KktTT05OUlBTd1SgGwzC6urrGsSsWKUNLIjE3y/M86ZRk9ocitV0oiiKTlUgr6GGb4nmeYRhd18m/LMsyDCPLsjnrhwyNIWVxWJYd1vc6BhLPsAc1TbuxwC0pW0OyNmQ4jFm92Kw6PGwVc9wNWYYchaZpZEAHGYJkLiwIAim3bEZOYosOhhTrIUNgSM1mnudJLzCWZW02G6l6Y67CMAyp40N2Sk6gYRik17i56xixjXp+xniVqbFdI3ISzAsdnVaLvTrpOUVRFFn3xtPLsixJS0U/PqzA9o1X7aYvTo7jenp6/vu//9vn8/3sZz9bsmSJJd3KGYZJTU0d4zwX0qwtLS1tYubFKJry6FsbgvKQU3B/9KP9PIuxGxPhxPWj/7TnJxRFPb3g+X+86/9YHc6Iuru7J3lLOAAgDMNIT0+fnKNQDcP40fuPtQ9eDyvhz39c4xLcVkc0I0TU8Lq/rGAZNiMu660tOzDZFibM7t27t2/fTlHUb37zm/LycqvDgZni7XOv/9+a39l5uzUjdI4ePXr58uXy8vLKykpLAtB1PbrPNEEyEcMWM0swjDSmhjxutj26cTFN08wBMqMOzIkdT+wlyS6GTeYiKYCbrhVd8ZckqsyjGObGNNaNsRmGEX1KyTZJloe62YGb86GIkXYdI7ZRz88YrzI1tmsU4xTFXt0wDPNVdNNjJKsPe5AMnrpx4eiJYDe+OFmWPXfunCzLZWVl8+fPn/zDc4aGhvbs2UNR1NNPP03SXgAAAAAAADAW1iR0GIYhbaEs2fttGLXkzfdf4PsbaRdj3/W4Bxm7Zfgt7drCEzjGZcb9EG7j1EmStHz58mXLlnEcZ7Z4n+SQx4E7h9T8sjoKAAAAAIA7wpqUitvtnhK3mgBTjtnpfEr8it1qm3mAsTt79uyVK1fy8vLKy8uR1gGYscLh8IEDB3ieX7VqlduN2U8AADCtWDP3eAJGWwDMTCSVM1V+xaZKnDAV+Xy+SCRy9uzZW5rrCgDTjKqqg4ODfX19Fy5csDoWAACAcTYZi8kBAAB8T/Hx8aROudWBAICVSMcG0iPC6lgAAADGGRI6AAAwDWH8FwBQ+FMAAADTGhI6E4FhGFRwAAAAAAAAAIDxYmUNnZnwnQlN06IoapqGIg4AAAAAAAAAMF4sG6EjSZKmaVbtfWLQNK3r+rFjx/70pz/19PRg8jbAMDRNS5IkSZLVgQAAAAAAAEwx1qQYysrKZs2a5fF4LNn7hOE47vr162+99ZamaY888ghmXQEMw/P8Y489puu6IAhWxwLTzcwZCgoAYzHtv0cEAIAZyJqEDs/zKSkpluyaILkVwzBIdRvyHk/+P6zlM3mQYRjSDVrX9Rs3xbIsWTF6XbIW2QLLssx3DMOI3j5ZjDyuadqwew8zB2QYBv0dEsn4nxQAKyQkJFgdAkxPmqZJkuRyudDoCmCGI+NAp/33iAAAMAPN0ElAJG/CcVwoFDIMw+l00jQdCoVkWXa73STFw7KsIAihUGhoaGhwcNButycmJtpsNlmWze0IgqAoSk9PTyAQiIuLS0hI4HmeLKDreiQSURSFJGVkWSY/sixr3l3wPK/r+sDAgN/vdzqdCQkJgiCQ1XmeZ1lW0zRd1zVN43neMIxgMKiqqiiKpC6PBScOAGCKKC8vz8nJiY+PR0IHYCYTBGHTpk0Mw8THx1sdCwAAwDibcQkdhmEURdmxY0cgECgqKjp06FAkEvnhD38oiuLbb789ODi4cOHCzZs3i6I4MDBw/Pjx2trazs5OWZZZlk1NTd2wYcPChQtJhWOe5+vr6/fv39/S0qIoiiiKc+fOXb16dVFREc/zV65cef3118nIHYqitm/fzvO8JEmLFy9+9NFHZVnmef769ev79++/ePFiKBQSBGHOnDkbNmwoKirSdb2hoeHMmTMkDZSenr506dJPPvnk6tWr4XA4ISFhzZo1y5cvR6FlAICRiKKYnJxsdRQAYL3ExESrQwAAALgjLEvokDlEVu36ypUrnZ2d9fX1siwbhvH2229rmub3+zmOO3z4cF5e3t13333q1Km3337b4XAkJCR4vd7+/v7m5ubXX3/d4/Hk5uZSFNXa2vrnP/85EAikpaW5XK7+/v4TJ050dHT84he/SEtLIyN3RFEko4H8fj9FUZIkBYNBmqY5juvo6PjDH/7Q0dERFxeXkZExMDBQV1d37dq1n/3sZ/NkFtxwAAAgAElEQVTnz6+vr9+xY4fb7eY4Lj09/cyZM1evXiVfLl29ejUzM3PFihWWnD0AAAAAAAAAsJw1CZ2rV6+eOHFi0aJF+fn5lgQgCIKqqsXFxffcc8/7779//fr15OTkn//8519++eXp06ebm5s1TcvOzr7vvvtKS0vz8vJsNltPT88rr7xy9erVc+fOkbCvXLnS399fUFDwq1/9iuM4n89XU1NDRviHw+HZs2f/5je/6erq2r59O0VRzz77LMny2O12WZY5jvvkk0/a29vnz5//1FNPpaWl+Xy+7du3f/vttwcOHMjPzy8rK3M6ndevXz9z5kxvb6/T6XzmmWeKioo++eST6upqnuctOW8A40vTtE8++URV1YcffhjzYgAAAAAAAMbOmrblly5dkiRpYGDAkr0ThmGsXr36rrvuysnJURSloqLirrvuKi4uNgyDtFRPTEzcunVrdnZ2W1vblStX4uLiSktLKYrq7+8nqyclJXEc19PT8/nnn/t8vpSUlE2bNhUXF5PSyIIgZGVlJScnk0rGycnJmZmZmZmZCQkJDMP09PRcvnzZbrevX78+IyNDkiSv17tq1SqWZTs6Onp7ewsKCjZv3lxeXq4oCsMwjz/++P3335+TkyOKoqIoKKAD04Pf7/f5fENDQ3hJw52AFlcAQOCvAQAATEvWjNDxer0dHR2WfyFvs9kkSSI9quLi4mRZttlsFEX5/X6WZQcHB3fv3n3mzJlgMKjrusfjcblcPM8Hg0GKohRFKS4uXrt27eHDh999990vvviioqJi2bJlOTk5pBGVYRiqqpq3qZqmqaqqqipFUYIg+P3+QCAgiuJHH320a9cuMgFN0zRBEAKBQCAQSExMDAaDsizrup6UlFRQUBAOh3Vdv+uuu7Kzs9PS0simAKY0l8tl1dRLmPauXr16+vRpt9u9bt060nMQAGYgTdP27dsXDoeXL1+emZlpdTgAAADjyZqEziT5bE3KFZMvbaL/JRmZHTt2HD582OVy5eXlud3uzs7O7u5uMtyG+q7l+RNPPFFcXHzkyJGGhob9+/cfPXr03nvvvf/++4f1Ph+GpmmS3OE4rr+/P7rTuSiKDodDEATzQcMwbDYb6Yel63peXl5BQYGmaaiIDNMAsjlw55ChoKFQSFVVQRCsDgcArOH3+8nY6vb2diR0AABgmplxXa7GguO47u7u2tpau92+devWJUuWkPTKrl279u7day6m67ooikuWLCkrK2tubq6urj5+/PjHH3+ck5NTUlIS3d3cTAORf3Vdd7lcTqdTkqTnn39+1qxZZGGO40iOKSEhgfRNvzE2RVGQyoFpA2Pg4c7xer09PT23lDTECxJg+jGHglo+MBwAAGDcIaFzc6RODc/zmZmZLpdLURRJkgYHB6OX4Tju1KlTcXFxhYWF8+fPLykpGRgYOHnyZEtLC6m2Q313e0C25nQ6g8FgJBKhaToxMTExMbGpqenixYtLly7lOI6iqKamJqfTmZCQEIlEWJa12+08z5OhQA6Hg1TPiUQiE382AACmnNsYCioIgqZpGDgGMPnpuj7GX1X8RgMAwDSGhM5NaJqWlJTk9XpbWlreeuutiooKwzAuXLhw8eJFs72UIAhnzpx55ZVXPB7P0qVLU1NTfT7ftWvXOI7LyMgwN8XzPMuy4XB4x44d58+f7+zsrKqqKiwsdLlcK1eubG5u/uqrr0KhUGFh4cDAwKFDh7Kysl544QWHw9HU1NTe3t7U1EQK7uzcudMwjOTk5KqqKlTPAQC4ExISEqwOAQDGGUbeAQDANGZlQsfCt1hJkkiNYZqmFUUJh8OqqpKyxOFwOBKJuFyuhx566PXXX6+vr//2228Nw4iLi/N6vc3NzZIkkSI4qampRUVF9fX1H330EcdxqqqKolhVVVVUVERmRamqmpKSUlRUVF1dff78+VOnTomi+IMf/ICmaVmWly9f3tXVdfjw4a+//vrIkSOaptlstszMTEmS4uPja2tr3333XYfDwXFcV1fXBx98EA6HKyoqVq9ejYQOAAAAAAAAwAxnTUJH07Sxj5UdX2QGU2VlZU5OTnx8vCzLhYWFFEXNmTNHluX09PT169dnZWWR7ElcXNzZs2eDwaAgCGVlZRzH1dfXp6amkilUaWlp//AP/3DhwoXLly9LksTzfF5eXmlpKcdxpLmVWTh59uzZXV1dNE1nZmYmJycrikKe2rx5c1lZ2YULF4LBIMdxeXl5JSUlPM9LkjR//vytW7eSqVjmSfN6vSigA9MMqSCOIfEAAAAAAAC3xJqETlZWVkdHR1FR0cTvmmRS7r//fjI2JxKJVFZWLlu2TFXVSCSSk5OTn5+v6zoZBZOTk5OXl6dpGsMwpBN5cXGxqqqSJFEURdpULVy4cOHChWYNY1mWzVblFEWRcTfr168ndRnI2BwyNIncxxYWFhYXF5NdUN9V26EoKj8/v7i4eFjwmqaRXQNMD2SKYnJysjmZEQAA4E6I/ngGAAAwPViT0ElPT3/44Yct2TVB8jUksUKGC5lJFjJ8hixGWkqRLubmI9Hb0XWdZFjIJKyb7kvXdVIImbphlplhGKS/VfQuonc9DocKMIkxDLNu3Tqro4DpifxtZ1n2NqojA8B0Qj7muVwuqwMBAAAYZzO0KPKNiZWRnrrpI6Nu8FYXQMU+AIDxlZWV1dbWtmbNmui5qwAw05ChoB6Ph0yxBwAAmE7wMRcAAKah9PT0Rx991OooAMBiGAoKAADTmGUD0TEmBQAAAAAAAADg9liT0Ll69erf//73K1euWLJ3AJgkNE3bu3fvRx99hFqVAAAAAAAAt8SaKVeXLl2SJMnn81mydwCYJPx+f39/P0VRZp84AAAAAAAAGAtrRuh4vV7SfMSSvQPAJOFyuWiaJj3gAMZXW1vb+++/f+LECczwBZjJdF3/7LPPdu7cOTg4aHUsAAAA48yahA6ayAIARVFI5cCd097eHg6H6+vrMaEPYCZTVbWjo2NoaKi5udnqWAAAAMYZulwBgGUwdALuHJZlaZoWBAFfIQDMZORPAUVRHIcPvQAAMN3gvQ0AAKaz5uZmh8NB03RKSkr0oLDe3l5VVW9cnmGYlJQU80dVVXt7e2+6ZZ7nk5KSzB9lWe7r67vpuDNRFBMSEkZd0jCMpKQkQRDMR3w+nyRJN27wxiVHOhyKopKSknieN3/s7u7WdX3Uw/n+B24YRnx8vN1uNx+JRCI+n28sBz72wxlpyXE/HGpqXsdxOZxh1/FOHM64X0dzyUAgwDDMTc8VAADAVIeEDgAATENk/BdN00eOHDEMQ1XVFStWFBQUkGeHhoZ27dp102/sVVV9+umnzZvSmpqaxsbGmw7zUVV127Zt5k1pdXV1c3Pz91lSVdWysrIlS5aQHwOBwIcffjhSkNFLxj6cioqKRYsWmUvu2bNnpCWjg/z+B66qaklJydKlS81HqqurW1tbRz3wWzqcGEuO7+Hc0oFPnus4LocTfR3v0OGM+3Wsra09c+YMx3E0TfM8r+s6cjoAADD9IKEDAADTkCiKkiSZt3DD5vfRND3SjL9hj8eYsTXuSxqGET0+InaQY18yencTeeDDgqRGLps1JQ5n7EtO7+s4VQ7H3KZhGLIsK4ridrtHWhcAAGCKsiaho2marusoVAkA+MoU7pDi4uL09HTzBUbTdPR0DJfL9dhjj4005Sp6zshdd91ljusZhuO46Dkjy5cvLyoqumnOQhCEsSxpGEb0FBin07llyxZZlm/c4LAlYxwORVHDlty4ceNNf++GHc73P3DDMDweT/QjVVVVJSUlox74LR3OSEuO++FQU/M6jsvhRF/HO3Q4434dy8rKsrKyop+N3iMAAMD0YE1CJzU11ePxRH+2BoAZiOO41NRUVVVZlrU6FphuGIaJ/S4zxrs7juOSk5PHsiTP89HFd8ZlyWEJkRjGfrM6xjffO3HgoiiOccmxHw6uY2xT5XDG/TqyLDvGJQEAAKYuaxI6s2fPnj17tiW7BoDJg2GYDRs2WB0FAExbkUjk4sWLmZmZXq/X6lgAAAAAxhlq6AAAAMD0tGPHju3bt3s8nnfeeSd6Pg4AAADANDBibTkAAACAKU1VVVIKF2X7AAAAYPpBQgcAAACmJ9IUiWXZkRpsAQAAAExd1iR0wuFwR0fHSC0qAWCGMAyjq6srEAhYHQgAAAAAAMAUY01C59ChQx9//HF9fb0leweASWJgYGDPnj07duwYqa8tAAAAAAAA3JQ1CZ3k5GSWZcPhsCV7B4BJwul0iqLIMIyu61bHAgAAAAAAMJVYk9Ahc9rJvwAwY6GqBQAAAAAAwO1BSgUALINCWgAAAAAAALcHCR0AAAAAAAAAgCkGCR0AAAAAAAAAgCkGCR0AAAAAAAAAgCnGmoQOKZyBvjYAAAAAAAAAALfBsi5XkiQlJSVZsncAmCRompYkied5juOsjgUAAAAAAGAqseYmqrS0NCsry+v1WrJ3AJgkeJ5/7LHHbDYbw2D6JwAAAAAAwC2wJqHDcVxycrIluwaASSUhIcHqEAAAAAAAAKYefCsOAAAAAAAAADDFIKEDAAAAAAAAADDFWJPQkWW5o6MjEolYsncAmDx6e3u7u7utjgIAAAAAAGCKsSahU1NTs3fv3traWkv2DgCTRCAQ2LVr1549exRFsToWAAAAAACAqcSaosg0TQuCwLLs2FcxDOPOxQMA42jsv62GYQiCcEurAAAAAAAAAGVVQicuLk7XdZqmb2kt3PIBTAlj/9W22Wx3NBIAAAAAAIDpypqEzq2mZmiaTk1NvUPBAMC4G2NOB1laAAAAAACA22NNQuc2MAwacgEAAAAAAAAAUBTalgMAAAAAAAAATDlI6AAAAAAAAAAATDHWJHRI4QyUzwAAAAAAAAAAuA2WFUWWJEnTNEv2DgCTBE3TsixTt9IYCwAAAAAAACirEjplZWVZWVnx8fGW7B0AJgme5x999FFd13metzoWAAAAAACAqcSahI4gCGlpaZbsGgAmlaSkJKtDAAAAAAAAmHpQFBkAAAAAAAAAYIpBQgcAAAAAAAAAYIpBQgcAAAAAAAAAYIqxJqFTV1f34Ycf+v1+S/YOAJNEJBLZtWvXsWPHDMOwOhYAAAAAAICpxJqETm9v7+DgYENDgyV7B4BJQpZlv9/f0NCgKIrVsQAAAAAAAEwl1iR04uPjDcNAo2KAGc5ut9M0zbKs1YEAAAAAAABMMdYkdDC9AgAo/CkAAAAAAAC4XSiKDAAAAAAAAAAwxSChAwAAAAAAAAAwxSChAwAAAAAAAAAwxViZ0EH5DAAAAAAAAACA22BNQkfTNF3XGQbjg2YQ5O/gpgzD0DSNpmmrAwEAAAAAAJhKOEv2mpGRcf369YKCAkv2DhPp+vXre/fubWtr8/v9Ho8nMzPzwQcfzMrKil6mq6urt7d3WIKPYRiHw5GcnGyz2SY2ZJg4HMelpKSkpKTwPG91LAAAAAAAAFOJNQmdzMzMjRs3WrJrmEi7d+/+05/+5HK5dF3Xdb2zs/Py5ct79+79yU9+8vDDD5uL7dix46OPProxcWMYhsfj+elPf1pVVTWxgcMEYRhmw4YNVkcBAAAAAAAw9WDSE9wpp06devXVVz0ej6ZpPM8XFBTwPK9pmsfjefXVV0+dOmUu6Xa7XS6X2+1mWdZ8kGVZt9ut6/p//ud/dnR0WHEEAAAAAAAAAJOUNSN0YNrTNO2VV15xu92yLK9evfr55593OByhUOjNN988ePCg2+1+5ZVX/vCHP0RncBRF+e1vf5uenm4YBk3TwWDw97//fWdnpyAIX3zxxY9+9CMLDwcAAAAAAABgUsEIHbgjLl261NPTQ1GUy+V66aWXHA4HRVEOh+PHP/5xfHw8RVE9PT2XLl2KXkVRlMLCwpSUlNTU1JSUlJycnH/913+VJMlms33zzTeoqQwAAAAAAABgsiah09zc/MEHHzQ2Nlqyd5gAra2tNE1LkvToo49G17vlOO7BBx+UJImm6evXr8feCMuyuq6Tte5suGARTdP27du3Z88eTdOsjgUAAAAAAGAqseY+uaGhIRgM9vf35+bmWhIA3Gk+n4+iKMMwMjIyhj2VkZFBhtv09fVFP87z/MWLF9PT08mPiqK8+eabPM9HIpGqqiq0tZ6W/H5/d3c3RVGapkXPvwMAAAAAAIDYrEnoeL3ejo4O3L9NY5Ikkf+IojjsKfMRcxmC5/nf/OY3uq6TGjqGYdjtdpZlDcNYs2bNBMQME8/pdA5rVw8AAAAAAABjYU1CB6mcac9ut5P/DMvakEdIysZcJpphGCzLkqcMw4iPj//1r39Nyu7A9INsDgAAAAAAwO2xJqGDArfTnsfjIf9pbW1dsmRJ9FNnz57leV5VVXMZQlGUf/qnf0pNTQ2FQq+88kooFJJl+YEHHsjKypq4uGFi4U8BAAAAAADA7cHX43BHlJaWGoZhs9n27t0bCATMx/1+/8GDB3meNwyjtLQ0ehVFUVasWDF//vwlS5Zs27YtEokIgvDhhx8qijLh4QMAAAAAAABMakjowB2RlpaWlpZGUVQkEvmP//iPzs5OXdc7Ozv//d//nWEYwzDMBUw0TauqSv5fVVWVmppK0/TAwMCRI0csOAAAAAAAAACASQwJHbgjGIZ5+eWXh4aGaJpubW396U9/+tJLL/30pz/t7OykaXpoaOjll1+OUT+FZdnnnnsuEonYbLa3337bTPQAAAAAAAAAAGVVQkfTNF3XNU2zZO8wMUpKSn75y1/KsizLsiiKfr9fFEVZliVJ+uUvf1lSUmIuOTQ0FAgEAoGAruvmg4sWLYqLiwsEAi0tLZ9++qkVRwATwTAMVNIBAAAAAAC4VdYURU5OTna5XAkJCZbsHSbM3XffvWDBgs8//7yhoSEUCjkcjvz8/HXr1g3rWrVp06aVK1dSUb2xKIpiWfZ//ud/2traGIa5sfc5TA8syyYlJamqis53AAAAAAAAt8SahE52dnZ2drYlu4YJ5vF4Nm3aFHuZG+vpEImJiYmJiXcmLpgUWJZ94IEHrI4CAAAAAABg6kENHQAAAAAAAACAKQYJHQAAAAAAAACAKQYJHQAAAAAAAACAKcaahE5bW9uuXbsCgYAleweASULX9U8//fT06dNWBwIAAAAAADDFWJPQqaur8/v9586ds2TvADBJDAwMdHR01NbWhkIhq2MBAAAAAACYSqxJ6Hi9Xk3TontUA8AM5HQ6GYZhWZbneatjAQAAAAAAmEqsSeiwLGvJfgFgUmGY//9PkGEY1kYCAAAAAAAwtViT0MHNGwBQ+FMAAAAAAABwu9DlCgAAAAAAAABgikFCBwAAAAAAAABgikFCBwAAAAAAAABgiuEs2aumaYZhqKpqyd4BYPIwDEPXdaujAAAAAAAAmGKsSejEx8e7XK558+ZZsncAmCRYlnW73WlpaWhbDgAAAAAAcEusSejk5+fn5+dbsmsAmDxYlt24caPVUQAAAAAAAEw9qKEDAAAAAAAAADDFIKEDAAAAAAAAADDFIKEDAAAAAAAAADDFWJPQURSlq6tLkiRL9g4Ak0d/f39vb6/VUQAAAAAAAEwx1iR0ampqdu3ade7cOUv2DgCTRDAY/PDDDz/66CNZlq2OBQAAAAAAYCqxpssVRVGiKLIsa9XeAWAy0HVdFEWrowAAAAAAAJh6rBmh8//Yu/Pgqs4Dz/tnv5u2qwWBQEISiE0IZEAsDcbENl5i43anjR23HdudTtKVVJKut2sy806qpjJvzdS87Zl2Z9JT3ePE7sRxtz2xCTZtM8QL2BhsDMZCYhObEAgQaN91l7O+fzyv73tfAUKA8dGF7+cPF7r3Oed5zjnX5+r89Cw5OTmu68qy7EvtACaIYDDodxMAAAAAICP5E+h4nudLvQAmFG4FAAAAAHBtWOUKAAAAAAAgw/g2h87VchzH7yYAGC9myAIAAACAGyozAh3P8zo6OlzX9bshAK5MUZQpU6YwSRYAAAAA3Dj+BDpi4oyrmj5DURgdBmQG/m8FAAAAgBvNn0DHdd1kMskoKuAWJ8uyaZp+twIAAAAAMo8/gc6CBQtKSkry8/N9qR3ABKHr+kMPPeS6rq7rfrcFAAAAADKJP4FOIBCYOnWqL1UDmFCKior8bgIAAAAAZB6mugAAAAAAAMgwBDoAAAAAAAAZxp9Ax7bt7u7uq1rlCsBNqb+/Px6P+90KAAAAAMgw/gQ6e/bs2bRp07Fjx3ypHcAEEYvFfv/737/55puWZfndFgAAAADIJP4EOpZlGYbR39/vS+0AJgjbtgOBgOM4juP43RYAAAAAyCT+BDq5ubmO4wQCAV9qBzBBhEIh8Q9VVf1tCQAAAABkFn8CHTF7DnPoALe41E2AuwEAAAAAXBVWuQIAAAAAAMgwBDoAAAAAAAAZhkAHAAAAAAAgw/gZ6Liu62PtAAAAAAAAGcq3ZcuTyWRqgRsAt6xkMuk4jqLQWxAAAAAAroLmS60LFiwoLS2dMmWKL7UDmCB0XX/wwQcjkYim+XMvAgAAAIAM5c9DVCgUonsOAFmWJ0+e7HcrAAAAACDzMMwBAAAAAAAgwxDoAAAAAAAAZBgCHQAAAAAAgAzjT6Bz5syZN95449SpU77UDmCCcBznvffe27Jli+M4frcFAAAAADKJP4FOU1PT4OBgd3e3L7UDmCAGBgYuXLjQ1dVFoAMAAAAAV8WfQKegoMDzPFVVfakdwAQRiUQURVEUxn4CAAAAwNXx5zlK0/xZLh3AhEKUAwAAAADXxp+nKc/zfKkXwITCrQAAAAAArg1/HgcAAAAAAMgwBDoAAAAAAAAZhkAHAAAAAAAgw/gzObHjOJ7nsVAxAKbRAQAAAIBr4E+gU1hYGAqF8vLyfKkdwAShqmo0GrUsS1VVv9sCAAAAAJnEn0CnoqKivLxclmVfagcwQaiqum7dOs/zuBsAAAAAwFXxJ9CRJMn35zdF+X/nD3Jdd9RbsiyL5nmeN2o8iCzLmqapqqooihg1JlxuD+nEri45wOSS5Udty8gU3Kx8vxsAAAAAQMbxLdDxXTKZFP0CgsHgqETGsiyR8qiqmj4SRNd113VbW1vPnz8/ODioaVpRUdH06dPFmJH0YMi2bcdxUo+poiJN03RdV1XVNM1R6cyo8qN4njeqJQAAAAAA4FZ2KwY6qqoODAz86le/6u3tlWX50UcfraurSyQS4l3DMF566aVjx45JkvT1r3/9rrvuMk1TvH727NnNmzcfP348kUiYpqkoSiAQiEaja9asueOOO1RVFcGQYRjbtm3bsmVLIBAQ+xSJTF5eXmFh4fz58xcsWKDrumVZqRpHlR8lmUymtwQAAAAAANzi/Al0Lly4UF9f/7WvfS0SifjSAM/zhoaGBgYGJEnauHFjWVlZYWGhSFhkWR4ZGRFvJZNJ0WvGMIzm5uYXXniht7c3EAgoiqLrunirp6fnd7/7XXt7+2OPPSbLsuiMk0wmBwYGRECTGmnV3d19/PjxPXv2zJkz59FHH508eXKqxovLp0skEolEgmEpuPm4rvvBBx8UFhbW1tb63RYAAAAAyCSKL7Xu37+/t7e3oaHBl9oFMYgpEAh0d3dv3LjRdd1UYqIoinhXvKIoysjIyGuvvdbX1xcKhRzHycnJmT9//owZMxRFEYO2tm/fvmvXrlQXG1mW1S8YhqHreiAQED9qmnbo0KFf/vKX3d3dmqZdrnw6sa0vZwm4ofr7+9va2hobG2OxmN9tAQAAAIBM4k8PnYKCggsXLoTDYV9qHyUYDDY0NHz00Udr166Nx+MXFzAM4+OPP25tbQ0Gg6Zp1tbWPvroo9nZ2bIsNzY2vvrqq6Zpapq2ffv2RYsWBYPB1IaWZVVUVDz++ONifNbg4OD27dubmppCoVBbW9vbb7/9zDPPpFeUXj79dc/z8vLyUkO0gJtGJBIR05Pruu53WwAAAAAgk/gT6KR6pkwQmqZt3ry5srKyoqJi1FuyLJumuW/fPlmWbdueNGnS448/npeXJzKXFStW9Pb2bty4MRAInD9//uTJk+kjR1zXDQaDM2bMSCaTopbZs2e/+OKLhw4dCgQCjY2NZ86cmT59enr5UChUVVUlyktpK3A5jnPxalxApkstNscibgAAAABwVfwZcjWhHt5c11VVdXh4+I033kgkEqknTEFRlN7e3q6uLk3THMepra3Nz88XK2S5rptMJmtra/Py8kTgcvr06VE79zzP+kI8Hg+Hww888EAwGJRlOR6PHz9+fFR1juMMp0ltS5qDm9KEuhUAAAAAQAaZWD1lvnqKohQWFnZ2dgaDwaNHj7777ruPPvroqALDw8MjIyMieSkrK0vPVhzHiUajhYWFAwMDsix3d3ePXZ1pmpMnT540adLZs2cVRWlra0t/1zCM1tbWn/3sZ57n2bZdUFDw3e9+Nzc3d9Sq6gAAAAAA4BbnTw+dicOyrLVr1xYUFNi2bRjG+++/f/jw4fTlw2VZTl9kKjs7O31zz/OCwWAwGBQdDQYHB8euznXdcDiclZUlUiGxllZ6XbZt9/b29vf39/X1DQwM0H8BAAAAAABc7FYPdGzbnjx58p/8yZ9IkiTLsmVZmzZtGhoaSh8JpWlaatKf1Ow2KWJIlIh70pOgy3FdN9XjxjCMUe/KsixWuRL/vdbDAgAAAAAANzN/hlw5juN53gQZSZRMJpctW3b48OGPPvooGAyePn1almVd10V247puJBLJysoSyyp3dHSkZz2qqg4ODvb396uqatt2YWHh2HWJ8n19fZqmiSmW098Vq1x985vftCzL8zxN08LhMLPn4OZGNzQAAAAAuAb+9NApKCgIBoO5ubm+1D6KiJYeeuihsrIy0zRFX5sUx3Hy8vJycnIcx1EU5dChQ8lkUlVV8W4gEDh27FhXV5eqqp7nTZky5eL9y2mCweCBAwc6OjrEHsrLy9NLihwGUM0AACAASURBVFWxqqqqKisrZ86cOX36dE3TPM8b1STgpqGqam5ubiQSSf0/BQAAAAAYD38CncrKyscff3zWrFm+1H4xx3FycnLWr18fCARG9YjxPC87O3v27Nm2beu6fvz48a1bt4q+M6FQ6Ny5c3/4wx9kWXZdNzc3t6qqalS3I9HZR9A0rbGx8e2339Y0zbKs4uLiWbNm2bZ9cXtEgiO2FWOvGH6Fm5Kqqn/8x3/8jW98g0AHAAAAAK6Kb6tcTbReJ8lkct68effdd9+bb74ZDAbT37Jte9WqVXv27InH45qmbd68ubW1tbKycmRkZN++fV1dXbqux2KxVatWTZkyJb3/jqZpXV1dr7zyiuu6nud1dXU1NzdblqUoim3b99xzT25ubjKZTE3Qkyo/KhVyXTcaja5Zs0b0A/pqTgjwlZlodwMAAAAAmPhu9WXL0yWTybvvvvvEiROjFrqybbukpOSBBx547bXXPM9TVbWhoWHv3r1iAmNN0+LxeGVl5X333Tequ42qqn19fe+++26qx42maWL+oLVr1y5fvtw0zTHKp1iWVVZWtnr1ajEC60aeAwAAAAAAkAFu0UDH87xEIhGLxRzHcV1XBCiu6xqG8cgjj5w9e7a7u9u2bdu2xVumaa5Zs0ZRlC1btvT19UmSJLrVWJaladrChQsfe+yx3Nxcy7KkL1Yfj8ViqdFbogpVVWVZnj59+t1337148WLRbeeS5UelNqmSAAAAAAAAkl+BjmVZAwMDOTk5F6/b/RXwPC8QCKxZs2ZkZMTzvPz8/FTPGtM0S0pKnnrqqSNHjkiSVFlZKd7yPM+27TVr1sydO7ehoeHMmTOxWExV1fz8/Hnz5lVXV4tpccRObNuurKxct25d+rQgmqbl5eVNnjy5rKwsHA6bppnKaC5ZPp3runl5eYqiEOvg5jMwMCAGFfrdEAAAAADIJP4EOrt37z5y5Mhtt91WV1f31dcuFpNat26dWHkqkUikD5UyTbOmpmbRokXi36mYxvO8ZDJZWFh4//3327ZtWZYsy2JkVnoxSZJs2543b15tbe3FHW1c17VtWyyIfsXyo7ZNJBIEOrjJjIyMbNiwQZKkp556ypd4FwAAAAAylD+BjuM4wWBQUfxZY0uSJM/z4vH45d41TXPU7DYpqXFYYn7iUdFMimVZ6RHPFV1teeDm4DhO+nxVAAAAAIBx8ifQyc3NdRwnc5e28TyPzjLA9QuFQn43AQAAAAAykj99ZEhDAEjcCgAAAADgWvk26AkAAAAAAADXhkAHAAAAAAAgwxDoAAAAAAAAZBjm0AEAAAAAAMgw/qxy5XmeaZq2bftSO4AJQpZl0zT9bgUAAAAAZB5/Ap358+cXFxcXFBT4UjuACULX9QcffNBxHF3X/W4LAAAAAGQSfwKdYDBYWlrqS9UAJpTi4mK/mwAAAAAAmcefQAdfGVmWR70yoSYwkmV5QrVnbL60VlzB669XlmXR/gw64QAAAACAy2GVqy+ZoiiBQODiGMUvtm27/39f1p41TdN1/XrSAV3XNS0zIkVVVQ3DcBznK65XURRJklzXVVX1evYjy7LjOIlEgomrAAAAAODm4M/jtOM4AwMD+fn5vtR+48iyHIvFPvvss0mTJtXU1FiW5W97dF0/evTo5s2bxQQlsixblvXYY49VVFRcZ9sURTl//vz58+dvu+22a8t0FEU5derUwYMHV61alZub+yUmTV86RVH6+/t37NihadqDDz74lV1WRVHi8fgrr7zS2dn59NNPl5aWXlsco2lad3f3888/Pzg4+Mwzz8yfP39CzUM8ODhoGEYwGPS7IQAAAACQSfzpofPZZ5+98cYbx44d86X2G0R0gvjNb37z8ssv9/f3i74V/nIcp6KiwnXdI0eONDc3nzx58sSJE4lE4jrbput6Q0PDs88++9FHHxmGcQ17MAzjzJkzzz333CeffCJdalzYhKLr+nvvvbdhw4be3t6v8rJqmtbR0bF3796jR48ePXr0mnsz6br+6aefnjx5Mj8/v7KyckJ10onFYq+//vqmTZt8Tz8BAAAAILP400MnkUgYhtHX1+dL7UJqahJZllMDWy7ubCJmHlEURbx7yd4oYleKoliWNTg4qGnaqAEyY1dxVU2VvpjJZdR+FEUR76ZX4bpuJBJ55plnuru7e3t73377bdd1L5mejOcw0+vq6OgYGBi4tjRHVJdIJOLxuFjpTNQuXWammCu2bYzzM86rLF3+Gonabds2DEPTtMs19fo/RRezLKukpOTee+/t6em57bbbLo48xrNbVVV7enr27t2r6/rq1auzsrISicR4av9q2LYdCARM02ShKwAAAAC4Kv4EOnl5eadPnw4EAr7ULogxPoZhuK7b399vWVY0GhXPlqkyYtqUoaGhWCyWk5MTiUQ8z0vv4CDLsq7rjuPYtq1pWuqZf1QBy7J6e3sdx8nLywsGg2Jemyu2UNd1VVXFs7rjOKqqyrKcTCZd1xWzz4iWKIqiaVo8Hh8YGFBVNS8vzzAMy7LE471t2yUlJZWVla2trZs3b77kM79o88jIyODgYDgczs7OFuHUGG1TVTU9tJJlORAIKIriOE4ymUz9mEgkUkeq67o4V8lkUkpLQMRhWpYl5qkxTTO9kWO0bTznZzxXeexr5HmeSMFETpSahyh1la94icVMQ4ODgyMjI9nZ2VlZWWLs29hXPxAIqKoaDoefeuop13VN0xQnNlXgih/OVO379u07f/58eXn5bbfdNqEGW0mSFAqFJEmSZfk6JwkCAAAAgFuNP4GOeGL3a7UdTdM6OztfeeWV7Ozs5cuXf/zxx6dOnXJdt7Cw8J577lm0aJF42A4EAseOHXvvvffOnj1rWVY4HJ43b97dd99dVFQkCoin0H379n3++ee9vb3RaHTBggXpXWBEZrF79+5PPvnk/PnznudFo9GlS5euWbNGJBFjNFJV1ZaWlsOHDyeTyUQiUVRUtHTp0vfff//EiRPxeDw/P/+OO+5YtGiRJEmJROKdd975/PPPh4aGZFmeMmXKypUr6+rqUl1FbNtOJpOXSxB0Xe/q6tq6dWtTU9Pw8HAgEKisrLznnnsqKirG+fAv4piPPvpocHCwsLBw0aJFpmnu3r17eHh4yZIl+fn5Im05efLk8ePHi4qKRLNT2x47duzQoUNdXV1ZWVkLFy5cunSp6HIydtscxxn7/Nx5552lpaW//e1vx77KY18jVVV/97vfnT59enBwMBKJHD58+LnnnhN9Sb75zW8WFxc7jjP2JdZ1/dSpU++9915LS4tpmqFQqKqq6vbbbxdD4cY4pZ999llvb69IqRzHqa2tLSgoSM3KfMUPp6AoytDQkBjXtnz58pycnHg8Pp5r+pVJ3QRYewsAAAAArkpmrDH05RL9OE6dOqWq6uHDh4eHh8PhsBgt9dJLL2VnZ1dVVcmyfOjQoRdffLG/vz8YDIoM6Pz58ydOnPjBD35QUFBg27au6++8886mTZuSyaR4eq+vrw+Hw6m+Brqu/+EPf3jzzTcdx4lGo7qunzlz5vTp0/39/evXrx870NF1ff/+/SJ1UlV12rRpDQ0NTU1NWVlZYkLi/Pz8ZcuWxWKxV1999ZNPPlFVNRgMuq7b1NR0/Pjxvr6++++//4qJjJgu93/+z/95+vTpUCgUjUaHhoZ2797d0tLygx/8oKys7IodSUSa8/vf//6dd96JRqPf/e53dV0fGBh46623zp07V1ZWJlIPXdebmpr+5V/+ZcmSJcuWLRNP76qqDgwMvPTSSyMjI7qu27bd0NBw9uzZRx991PM8VVXHaFtVVdXY52fSpEklJSVjX2XLssa+RqqqXrhw4cSJE+FwWIQj/f39nueJnkSib87Ym58/f/7555/v6ekpKCiIRqP9/f0ffPBBc3PzX//1X0ej0cstmyU+Wo2NjaFQSPQnmjp16uTJk0V5wzCu+OEU+zEM4/PPPz99+vSUKVPq6uomWvccAAAAAMA1uxUDHUmSZFk2DCMWixUVFT311FOFhYWnTp166623BgcHP/7447lz5w4ODr755psDAwPV1dX33ntvVlbWqVOntmzZ0traumXLlqefflr0vNiyZYvneTU1NcuXL/c877PPPjt58qSoQtf1EydObNmyRdO0Bx544I477tB1fceOHZs3b/7oo48WLVo0c+ZMx3GCweAlp1xRVXXOnDnf/OY3Ozs7m5qaurq6dF1fv359dXX11q1b9+zZI0YV7d2799NPP83JyVm7du28efNM09y2bdv+/fv/8Ic/zJs374qJjKIoW7ZsOXXq1MyZMx977LFp06Z1d3f/8z//84kTJ955553vfe97YpzR5TYXMdbvfve7Dz/8cObMmU899dTMmTMty5JlORQKRSIRRVFSvbF0XY9EIoFAIH2HiUSipKRkxYoVWVlZDQ0N+/fv3759+9y5cxcuXChJ0hhtq6iomD179tjnR5KkMa7ynDlzJEkSF/Ry12jWrFnr16//xje+IfpALVmy5P777xcHWFhYKMvy2JtXV1cfP368s7Nz1qxZP/7xj3Vd7+3t3blzZ2VlZW5u7hiLoNu2ffvtt8+ePVuEXAMDA6kzqSjKyMjI2B/O1KcoHo/v3LnTdd2lS5cWFBRMqNlzAAAAAADX4xYNdATHcb7+9a+vXLkyHo9XVVWdO3fugw8+6OjosG377Nmz586di0aj69evr6qqSiaTc+bMSSaTGzduPH78eG9v76RJk/bu3Ts0NFReXv7d735XLMFeU1Pz3HPPtbW1SZIky/KBAweGhoZuu+22hx56SDyN33PPPfv37z927FhLS8vcuXO7u7v37dt38ewhnucpirJs2bLly5eLgEbTtPXr1991112yLH/yySeJRMJxHNd1GxsbXdddsmTJww8/bNu2qqqTJ09ub29va2s7fPhweXn5GIcvusAcPXo0GAw+9NBD8+bNi8fjM2bMuPvuu1taWs6dO9ff35+Tk3O53EFMFfzaa69t3749KyvrW9/61qxZs2Kx2PgnQ3FdNy8v79vf/nZ5ebnruosWLfr7v//7w4cPf/7554sXL25vbx+jbT09PTU1NcuWLfvwww8vd37GvsrxeDwUCo19jWbNmjV16tRQKLRr1y7HcXJycsSHQZIk27aveInnz58vOhD19fU1Njbedttt06dPLy0ttSxr7KDNtu0777zTMIze3t5jx46lTx8ugsKxP5wiLTIMY9++fWJxq6VLl46RHwEAAAAAMo6fc+j4zjCMyZMnJxIJMSNvUVGR6JDiOM6FCxeSyWRVVVVpaenIyIhYJmnOnDnBYHBgYKCvr6+oqOjs2bOSJFVXV+fl5Y2MjCiKYhhGeo+bCxcuGIbR3d3985//XDxOq6ra39+vaVpXV5emae3t7f/0T/8UDAZHNcx13UAgMGPGjPz8fNM0XdfNz8+fP39+PB73PG/x4sVFRUXl5eV9fX09PT2Kooi5e8SAmvz8/PLy8nPnzolcaQyiMUNDQ8Fg8J133nnvvffEYVqWFQgEhoeHh4aG8vLyxhgWdOrUqSNHjui6LoawVVVVXdX59zwvGAyGQqF4PO44TigUWrhwYVNTU3t7eyKRGBwcvGLbRkZGLnd+ZsyYIUYejXGVr3iNJEmybVtUIa7LqCxm7M1t254/f/4f/dEf7d69+9e//vW0adMWL168bNmyKVOmjN31SZIk0WBxRKPeuuKHMz8/33Vdx3F27tyZSCTuuOOOqVOn0j0HAAAAAG4mvgU6pmlevCLPV9yGQCCgaVpqTFD6pDbi6dcwDDG3i/TFoKFAIDA4OGhZVjKZTCaTiqLk5OSkNhy1ZHUsFpNlub+/v7u7O/WiWNRcrLuUnZ29dOnSi1drFjPIBAKB1EJL4XBYbOK67rx58xYsWOB5Xmdnp+gnEgqF0usVKwcNDw+PfQZkWTZN0zRNVVVbW1tTRyFWQBdrSI29h2QyWV1dnZ+fv2PHjq1bty5cuLCwsHA8C3ilH2n62YtEIqm3xt+2S54fWZZbWlrGvsrSla7RFdt/xUus6/q3vvWtuXPnfvzxxydPnnzjjTd27Njx9a9//Wtf+9o1f/7H/nCKxbB0XT969OixY8fy8vJWrFgxYbvniA+h360AAAAAgMzjT6Azf/78SZMmFRYW+lJ7iud5l+slEY1GZVkeHBwcHh4W60NrmjYwMCBWnhZzwYjApaenJxUuqKoqluIWCgoKLMuaP3/+ww8/nEwmxUAqVVVN04xGo7FYrKSk5Ec/+tEYLbzkc7joJKIoSlZWVigUcl23s7Nz3rx5kiTJsuy6rggXJk2aNPbhu66blZUViUQsy/rWt741ZcoU8WitaZrruoqi5Ofni7xAzNcjVgRPbW7bdllZ2be//W0xE3N7e/vOnTv/9E//NL1M+oJf6UtupxdIP3tiymFRMhKJXLFtl8xcxPlJxWRjXGXpStdo1MCo9MMR+7zi5qKz1R133LFkyZITJ058/PHHjY2NGzdunDZt2uzZs8VBKYoSCAQcxxlntDH2hzM7O1sstfbpp58ODw+vXr26vLx8woYmuq4/8MADYtpsv9sCAAAAAJlEuXKRGyAYDJaVlYXDYV9qvyLP86ZMmRKJRNra2j7//HPR90HML2tZVn5+fkFBgSRJpaWliqIcPHhQLMMUCAQGBgaGh4dTj/2lpaWyLJ8/f94wjIULF9bU1MyYMSMUCs2dO1cMipEkSb0MRVF0XQ8Gg7qui5ggFAqFw+FAICB27rpuKBSaMmWK53mffvppb29vIBAIBoMHDhxoaWlRVVVMoCPLsng9lX2I3Yo0KhqNRqPReDze1tY2e/bsmpqampqavLy8KVOmzJgxQ1VV0Vfo5MmT27ZtGx4eTu8XIwY65eXlRaPRNWvWKIqya9eutrY2TdNEPxrP88SIJMMwFEU5c+bMqExHluVYLNbT0yOGqomJZiRJmjRpkmEYYs9jtE0s7HW58zNO47lG0heDBMWAL/G5Fa9ccXNN05qamlpaWiKRyJIlS/7qr/5qzpw5sVisublZnA2x5tr27dubmprS08DUZRLFUj+O58OpKMrp06cbGhqysrJWrVp1VSfkqzd58uSpU6deMu8DAAAAAFzOLT0p8uVYllVWVlZTU7N79+6NGzceO3YsGo22tLS0tLTIsrxixYpIJGLbdl1d3SeffNLd3f3LX/6ypqZGluUjR4709vaK1MO27dra2g8//PDs2bPPP//8XXfdJabgPXTo0FNPPbVgwQLR++ZyA5QURTl37lx3d3dLS4uu60NDQ++//74kSfn5+bfddpvY1vO8lStX1tfXNzc3//3f/71ICg4ePDg8PFxaWlpTU+M4TjweP3DggCzLPT09Ip05evTo0NCQ67pVVVXRaHTFihWtra3btm1LJpNz587t7+9///33y8rKxEpeiqJcuHDh+eef7+rqWrVq1Z//+Z+nP3iLiVosy1q5cqVY4eujjz76sz/7s+zs7Ly8vLa2tm3btuXk5BQUFDQ1NR08eFDTtFHHODIy8uKLL9bU1BiGceLEidbWVsMw6urqXNfNyckZo22BQOCK5+eKHMcZzzWSJEkM8mpqatqwYYOu64lE4utf//oVL7GiKIcOHXr++efz8vJuv/324uLivr6+jo4OVVWLi4vFng3DePPNN7ds2ZKVlfXDH/5wzpw5pmkqinL06NHh4eFEIiHGnYmrJstyVVXV2B/OrKwsz/N27949MDBQV1cn1h27yv8DAAAAAAAT3S0a6LiuG4/HpbQ8RazZFIvFxAQlsiw//PDDfX19J06c2Llzp3glFAqtXbv2jjvuME3T87zKysoHHnjgX//1X9va2s6cOSMyCFmWR0ZGxBJUeXl5jz322Msvv3z69OkXX3xRURTbtrOysjo6Oq7YQrFE0WuvvRYKhVRVbW9v/+1vf5tIJGpra1MrFpmmWVVVtW7dus2bN588efLEiROSJGmaVlJS8uSTT+bk5Hie19vb+6tf/UqEAiJp2rRpk1gC6d//+3+fm5u7evXq8+fP79q169133926davjOKqqZmdnDw8P5+fnK4qSTCbFdDxiPFT6uRLTtYjJgO68887m5uYPPvigtrZ24cKFK1asOHr0aGdn5z/90z9pmjYyMhIMBuPxuNhEnPlYLJadnT0y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" alt="Decision workflow" />
</figure>

<div class="formalpara">

<div class="title">

Example: Machine config pool based matching

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: openshift-node-custom
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom OpenShift node profile with an additional kernel parameter
      include=openshift-node
      [bootloader]
      cmdline_openshift_node_custom=+skew_tick=1
    name: openshift-node-custom

  recommend:
  - machineConfigLabels:
      machineconfiguration.openshift.io/role: "worker-custom"
    priority: 20
    profile: openshift-node-custom
```

</div>

To minimize node reboots, label the target nodes with a label the machine config pool’s node selector will match, then create the Tuned CR above and finally create the custom machine config pool itself.

**Cloud provider-specific TuneD profiles**

With this functionality, all Cloud provider-specific nodes can conveniently be assigned a TuneD profile specifically tailored to a given Cloud provider on a OpenShift Container Platform cluster. This can be accomplished without adding additional node labels or grouping nodes into machine config pools.

This functionality takes advantage of `spec.providerID` node object values in the form of `<cloud-provider>://<cloud-provider-specific-id>` and writes the file `/var/lib/ocp-tuned/provider` with the value `<cloud-provider>` in NTO operand containers. The content of this file is then used by TuneD to load `provider-<cloud-provider>` profile if such profile exists.

The `openshift` profile that both `openshift-control-plane` and `openshift-node` profiles inherit settings from is now updated to use this functionality through the use of conditional profile loading. Neither NTO nor TuneD currently include any Cloud provider-specific profiles. However, it is possible to create a custom profile `provider-<cloud-provider>` that will be applied to all Cloud provider-specific cluster nodes.

<div class="formalpara">

<div class="title">

Example GCE Cloud provider profile

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: provider-gce
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=GCE Cloud provider-specific profile
      # Your tuning for GCE Cloud provider goes here.
    name: provider-gce
```

</div>

> [!NOTE]
> Due to profile inheritance, any setting specified in the `provider-<cloud-provider>` profile will be overwritten by the `openshift` profile and its child profiles.

# Custom tuning examples

The following examples demonstrate custom tuning configurations for OpenShift Container Platform nodes using the Node Tuning Operator.

**Using TuneD profiles from the default CR**

The following CR applies custom node-level tuning for OpenShift Container Platform nodes with label `tuned.openshift.io/ingress-node-label` set to any value.

<div class="formalpara">

<div class="title">

Example: custom tuning using the openshift-control-plane TuneD profile

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: ingress
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=A custom OpenShift ingress profile
      include=openshift-control-plane
      [sysctl]
      net.ipv4.ip_local_port_range="1024 65535"
      net.ipv4.tcp_tw_reuse=1
    name: openshift-ingress
  recommend:
  - match:
    - label: tuned.openshift.io/ingress-node-label
    priority: 10
    profile: openshift-ingress
```

</div>

> [!IMPORTANT]
> Custom profile writers are strongly encouraged to include the default TuneD daemon profiles shipped within the default Tuned CR. The example above uses the default `openshift-control-plane` profile to accomplish this.

**Using built-in TuneD profiles**

Given the successful rollout of the NTO-managed daemon set, the TuneD operands all manage the same version of the TuneD daemon. To list the built-in TuneD profiles supported by the daemon, query any TuneD pod in the following way:

``` terminal
$ oc exec $tuned_pod -n openshift-cluster-node-tuning-operator -- find /usr/lib/tuned/ -name tuned.conf -printf '%h\n' | sed 's|^.*/||'
```

You can use the profile names retrieved by this in your custom tuning specification.

<div class="formalpara">

<div class="title">

Example: using built-in hpc-compute TuneD profile

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: openshift-node-hpc-compute
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom OpenShift node profile for HPC compute workloads
      include=openshift-node,hpc-compute
    name: openshift-node-hpc-compute

  recommend:
  - match:
    - label: tuned.openshift.io/openshift-node-hpc-compute
    priority: 20
    profile: openshift-node-hpc-compute
```

</div>

In addition to the built-in `hpc-compute` profile, the example above includes the `openshift-node` TuneD daemon profile shipped within the default Tuned CR to use OpenShift-specific tuning for compute nodes.

**Overriding host-level sysctls**

Various kernel parameters can be changed at runtime by using `/run/sysctl.d/`, `/etc/sysctl.d/`, and `/etc/sysctl.conf` host configuration files. OpenShift Container Platform adds several host configuration files which set kernel parameters at runtime; for example, `net.ipv[4-6].`, `fs.inotify.`, and `vm.max_map_count`. These runtime parameters provide basic functional tuning for the system prior to the kubelet and the Operator start.

The Operator does not override these settings unless the `reapply_sysctl` option is set to `false`. Setting this option to `false` results in `TuneD` not applying the settings from the host configuration files after it applies its custom profile.

<div class="formalpara">

<div class="title">

Example: overriding host-level sysctls

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: openshift-no-reapply-sysctl
  namespace: openshift-cluster-node-tuning-operator
spec:
  profile:
  - data: |
      [main]
      summary=Custom OpenShift profile
      include=openshift-node
      [sysctl]
      vm.max_map_count=>524288
    name: openshift-no-reapply-sysctl
  recommend:
  - match:
    - label: tuned.openshift.io/openshift-no-reapply-sysctl
    priority: 15
    profile: openshift-no-reapply-sysctl
    operand:
      tunedConfig:
        reapply_sysctl: false
```

</div>

# Deferring application of tuning changes

As an administrator, use the Node Tuning Operator (NTO) to update custom resources (CRs) on a running system and make tuning changes. For example, they can update or add a sysctl parameter to the \[sysctl\] section of the tuned object. When administrators apply a tuning change, the NTO prompts TuneD to reprocess all configurations, causing the tuned process to roll back all tuning and then reapply it.

Latency-sensitive applications may not tolerate the removal and reapplication of the tuned profile, as it can briefly disrupt performance. This is particularly critical for configurations that partition CPUs and manage process or interrupt affinity using the performance profile. To avoid this issue, OpenShift Container Platform introduced new methods for applying tuning changes. Before OpenShift Container Platform 4.17, the only available method, immediate, applied changes instantly, often triggering a tuned restart.

The following additional methods are supported:

- `always`: Every change is applied at the next node restart.

- `update`: When a tuning change modifies a tuned profile, it is applied immediately by default and takes effect as soon as possible. When a tuning change does not cause a tuned profile to change and its values are modified in place, it is treated as always.

Enable this feature by adding the annotation `tuned.openshift.io/deferred`. The following table summarizes the possible values for the annotation:

| Annotation value | Description |
|----|----|
| missing | The change is applied immediately. |
| always | The change is applied at the next node restart. |
| update | The change is applied immediately if it causes a profile change, otherwise at the next node restart. |

The following example demonstrates how to apply a change to the `kernel.shmmni` sysctl parameter by using the `always` method:

<div class="formalpara">

<div class="title">

Example

</div>

``` yaml
apiVersion: tuned.openshift.io/v1
kind: Tuned
metadata:
  name: performance-patch
  namespace: openshift-cluster-node-tuning-operator
  annotations:
    tuned.openshift.io/deferred: "always"
spec:
  profile:
    - name: performance-patch
      data: |
        [main]
        summary=Configuration changes profile inherited from performance created tuned
        include=openshift-node-performance-performance
        [sysctl]
        kernel.shmmni=8192
  recommend:
    - machineConfigLabels:
        machineconfiguration.openshift.io/role: worker-cnf
      priority: 19
      profile: performance-patch
```

</div>

where:

- The `include` directive is used to inherit the `openshift-node-performance-performance` profile. This is a best practice to ensure that the profile is not missing any required settings.

- The `kernel.shmmni` sysctl parameter is being changed to `8192`.

- The `machineConfigLabels` field is used to target the `worker-cnf` role. Configure a `MachineConfigPool` resource to ensure the profile is applied only to the correct nodes.

> [!NOTE]
> You can use Topology Aware Lifecycle Manager to perform a controlled reboot across a fleet of spoke clusters to apply a deferred tuning change. For more information about coordinated reboots, see "Coordinating reboots for configuration changes".

<div>

<div class="title">

Additional resources

</div>

- [Coordinating reboots for configuration changes](../edge_computing/policygenerator_for_ztp/ztp-configuring-managed-clusters-policygenerator.md#ztp-coordinating-reboots-for-config-changes_ztp-configuring-managed-clusters-policygenerator)

</div>

## Deferring application of tuning changes: An example

The following worked example describes how to defer the application of tuning changes by using the Node Tuning Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have `cluster-admin` role access.

- You have applied a performance profile to your cluster.

- A `MachineConfigPool` resource, for example, `worker-cnf` is configured to ensure that the profile is only applied to the designated nodes.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check what profiles are currently applied to your cluster by running the following command:

    ``` shell
    $ oc -n openshift-cluster-node-tuning-operator get tuned
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` shell
    NAME                                     AGE
    default                                  63m
    openshift-node-performance-performance   21m
    ```

    </div>

2.  Check the machine config pools in your cluster by running the following command:

    ``` shell
    $ oc get mcp
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` shell
    NAME         CONFIG                                                 UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT   DEGRADEDMACHINECOUNT   AGE
    master       rendered-master-79a26af9f78ced61fa8ccd309d3c859c       True      False      False      3              3                   3                     0                      157m
    worker       rendered-worker-d9352e91a1b14de7ef453fa54480ce0e       True      False      False      2              2                   2                     0                      157m
    worker-cnf   rendered-worker-cnf-f398fc4fcb2b20104a51e744b8247272   True      False      False      1              1                   1                     0                      92m
    ```

    </div>

3.  Describe the current applied performance profile by running the following command:

    ``` shell
    $ oc describe performanceprofile performance | grep Tuned
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` shell
    Tuned:                   openshift-cluster-node-tuning-operator/openshift-node-performance-performance
    ```

    </div>

4.  Verify the existing value of the `kernel.shmmni` sysctl parameter:

    1.  Run the following command to display the node names:

        ``` shell
        $ oc get nodes
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` shell
        NAME                          STATUS   ROLES                  AGE    VERSION
        ip-10-0-26-151.ec2.internal   Ready    worker,worker-cnf      116m   v1.30.6
        ip-10-0-46-60.ec2.internal    Ready    worker                 115m   v1.30.6
        ip-10-0-52-141.ec2.internal   Ready    control-plane,master   123m   v1.30.6
        ip-10-0-6-97.ec2.internal     Ready    control-plane,master   121m   v1.30.6
        ip-10-0-86-145.ec2.internal   Ready    worker                 117m   v1.30.6
        ip-10-0-92-228.ec2.internal   Ready    control-plane,master   123m   v1.30.6
        ```

        </div>

    2.  Run the following command to display the current value of the `kernel.shmmni` sysctl parameters on the node `ip-10-0-32-74.ec2.internal`:

        ``` shell
        $ oc debug node/ip-10-0-26-151.ec2.internal  -q -- chroot host sysctl kernel.shmmni
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` shell
        kernel.shmmni = 4096
        ```

        </div>

5.  Create a profile patch, for example, `perf-patch.yaml` that changes the `kernel.shmmni` sysctl parameter to `8192`. Defer the application of the change to a new manual restart by using the `always` method by applying the following configuration:

    ``` yaml
    apiVersion: tuned.openshift.io/v1
    kind: Tuned
    metadata:
      name: performance-patch
      namespace: openshift-cluster-node-tuning-operator
      annotations:
        tuned.openshift.io/deferred: "always"
    spec:
      profile:
        - name: performance-patch
          data: |
            [main]
            summary=Configuration changes profile inherited from performance created tuned
            include=openshift-node-performance-performance
            [sysctl]
            kernel.shmmni=8192
      recommend:
        - machineConfigLabels:
            machineconfiguration.openshift.io/role: worker-cnf
          priority: 19
          profile: performance-patch
    ```

    where:

    - The `include` directive is used to inherit the `openshift-node-performance-performance` profile. This is a best practice to ensure that the profile is not missing any required settings.

    - The `kernel.shmmni` sysctl parameter is being changed to `8192`.

    - The `machineConfigLabels` field is used to target the `worker-cnf` role.

6.  Apply the profile patch by running the following command:

    ``` shell
    $ oc apply -f perf-patch.yaml
    ```

7.  Run the following command to verify that the profile patch is waiting for the next node restart:

    ``` shell
    $ oc -n openshift-cluster-node-tuning-operator get profile
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` shell
    NAME                          TUNED                     APPLIED   DEGRADED   MESSAGE                                                                            AGE
    ip-10-0-26-151.ec2.internal   performance-patch         False     True       The TuneD daemon profile is waiting for the next node restart: performance-patch   126m
    ip-10-0-46-60.ec2.internal    openshift-node            True      False      TuneD profile applied.                                                             125m
    ip-10-0-52-141.ec2.internal   openshift-control-plane   True      False      TuneD profile applied.                                                             130m
    ip-10-0-6-97.ec2.internal     openshift-control-plane   True      False      TuneD profile applied.                                                             130m
    ip-10-0-86-145.ec2.internal   openshift-node            True      False      TuneD profile applied.                                                             126m
    ip-10-0-92-228.ec2.internal   openshift-control-plane   True      False      TuneD profile applied.                                                             130m
    ```

    </div>

8.  Confirm the value of the `kernel.shmmni` sysctl parameter remain unchanged before a restart:

    1.  Run the following command to confirm that the application of the `performance-patch` change to the `kernel.shmmni` sysctl parameter on the node `ip-10-0-26-151.ec2.internal` is not applied:

        ``` shell
        $ oc debug node/ip-10-0-26-151.ec2.internal  -q -- chroot host sysctl kernel.shmmni
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` shell
        kernel.shmmni = 4096
        ```

        </div>

9.  Restart the node `ip-10-0-26-151.ec2.internal` to apply the required changes by running the following command:

    ``` shell
    $ oc debug node/ip-10-0-26-151.ec2.internal  -q -- chroot host reboot&
    ```

10. In another terminal window, run the following command to verify that the node has restarted:

    ``` shell
    $ watch oc get nodes
    ```

    Wait for the node `ip-10-0-26-151.ec2.internal` to transition back to the `Ready` state.

11. Run the following command to verify that the profile patch is waiting for the next node restart:

    ``` shell
    $ oc -n openshift-cluster-node-tuning-operator get profile
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` shell
    NAME                          TUNED                     APPLIED   DEGRADED   MESSAGE                                                                            AGE
    ip-10-0-20-251.ec2.internal   performance-patch         True      False      TuneD profile applied.                                                             3h3m
    ip-10-0-30-148.ec2.internal   openshift-control-plane   True      False      TuneD profile applied.                                                             3h8m
    ip-10-0-32-74.ec2.internal    openshift-node            True      True       TuneD profile applied.                                                             179m
    ip-10-0-33-49.ec2.internal    openshift-control-plane   True      False      TuneD profile applied.                                                             3h8m
    ip-10-0-84-72.ec2.internal    openshift-control-plane   True      False      TuneD profile applied.                                                             3h8m
    ip-10-0-93-89.ec2.internal    openshift-node            True      False      TuneD profile applied.                                                             179m
    ```

    </div>

12. Check that the value of the `kernel.shmmni` sysctl parameter have changed after the restart:

    1.  Run the following command to verify that the `kernel.shmmni` sysctl parameter change has been applied on the node `ip-10-0-32-74.ec2.internal`:

        ``` shell
        $ oc debug node/ip-10-0-32-74.ec2.internal  -q -- chroot host sysctl kernel.shmmni
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` shell
        kernel.shmmni = 8192
        ```

        </div>

        > [!NOTE]
        > An additional restart results in the restoration of the original value of the `kernel.shmmni` sysctl parameter.

</div>

# Supported TuneD daemon plugins

Excluding the `[main]` section, the following TuneD plugins are supported when using custom profiles defined in the `profile:` section of the Tuned CR:

- audio

- cpu

- disk

- eeepc_she

- modules

- mounts

- net

- scheduler

- scsi_host

- selinux

- sysctl

- sysfs

- usb

- video

- vm

- bootloader

There is some dynamic tuning functionality provided by some of these plugins that is not supported. The following TuneD plugins are currently not supported:

- script

- systemd

> [!NOTE]
> The TuneD bootloader plugin only supports Red Hat Enterprise Linux CoreOS (RHCOS) worker nodes.

<div>

<div class="title">

Additional resources

</div>

- [Available TuneD Plugins](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/customizing-tuned-profiles_monitoring-and-managing-system-status-and-performance#available-tuned-plug-ins_customizing-tuned-profiles)

- [Getting Started with TuneD](https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/monitoring_and_managing_system_status_and_performance/getting-started-with-tuned_monitoring-and-managing-system-status-and-performance)

</div>

# Configuring node tuning in a hosted cluster

To set node-level tuning on the nodes in your hosted cluster, you can use the Node Tuning Operator. In hosted control planes, you can configure node tuning by creating config maps that contain `Tuned` objects and referencing those config maps in your node pools.

<div>

<div class="title">

Procedure

</div>

1.  Create a config map that contains a valid tuned manifest, and reference the manifest in a node pool. In the following example, a `Tuned` manifest defines a profile that sets `vm.dirty_ratio` to 55 on nodes that contain the `tuned-1-node-label` node label with any value. Save the following `ConfigMap` manifest in a file named `tuned-1.yaml`:

    ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: tuned-1
          namespace: clusters
        data:
          tuning: |
            apiVersion: tuned.openshift.io/v1
            kind: Tuned
            metadata:
              name: tuned-1
              namespace: openshift-cluster-node-tuning-operator
            spec:
              profile:
              - data: |
                  [main]
                  summary=Custom OpenShift profile
                  include=openshift-node
                  [sysctl]
                  vm.dirty_ratio="55"
                name: tuned-1-profile
              recommend:
              - priority: 20
                profile: tuned-1-profile
    ```

    > [!NOTE]
    > If you do not add any labels to an entry in the `spec.recommend` section of the Tuned spec, node-pool-based matching is assumed, so the highest priority profile in the `spec.recommend` section is applied to nodes in the pool. Although you can achieve more fine-grained node-label-based matching by setting a label value in the Tuned `.spec.recommend.match` section, node labels will not persist during an upgrade unless you set the `.spec.management.upgradeType` value of the node pool to `InPlace`.

2.  Create the `ConfigMap` object in the management cluster:

    ``` terminal
    $ oc --kubeconfig="$MGMT_KUBECONFIG" create -f tuned-1.yaml
    ```

3.  Reference the `ConfigMap` object in the `spec.tuningConfig` field of the node pool, either by editing a node pool or creating one. In this example, assume that you have only one `NodePool`, named `nodepool-1`, which contains 2 nodes.

    ``` yaml
        apiVersion: hypershift.openshift.io/v1alpha1
        kind: NodePool
        metadata:
          ...
          name: nodepool-1
          namespace: clusters
        ...
        spec:
          ...
          tuningConfig:
          - name: tuned-1
        status:
        ...
    ```

    > [!NOTE]
    > You can reference the same config map in multiple node pools. In hosted control planes, the Node Tuning Operator appends a hash of the node pool name and namespace to the name of the Tuned CRs to distinguish them. Outside of this case, do not create multiple TuneD profiles of the same name in different Tuned CRs for the same hosted cluster.

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

Now that you have created the `ConfigMap` object that contains a `Tuned` manifest and referenced it in a `NodePool`, the Node Tuning Operator syncs the `Tuned` objects into the hosted cluster. You can verify which `Tuned` objects are defined and which TuneD profiles are applied to each node.

</div>

1.  List the `Tuned` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" get tuned.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       AGE
    default    7m36s
    rendered   7m36s
    tuned-1    65s
    ```

    </div>

2.  List the `Profile` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" get profile.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           TUNED            APPLIED   DEGRADED   AGE
    nodepool-1-worker-1            tuned-1-profile  True      False      7m43s
    nodepool-1-worker-2            tuned-1-profile  True      False      7m14s
    ```

    </div>

    > [!NOTE]
    > If no custom profiles are created, the `openshift-node` profile is applied by default.

3.  To confirm that the tuning was applied correctly, start a debug shell on a node and check the sysctl values:

    ``` terminal
    $ oc --kubeconfig="$HC_KUBECONFIG" \
      debug node/nodepool-1-worker-1 -- chroot /host sysctl vm.dirty_ratio
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    vm.dirty_ratio = 55
    ```

    </div>

# Advanced node tuning for hosted clusters by setting kernel boot parameters

For more advanced tuning in hosted control planes, which requires setting kernel boot parameters, you can also use the Node Tuning Operator. The following example shows how you can create a node pool with huge pages reserved.

<div>

<div class="title">

Procedure

</div>

1.  Create a `ConfigMap` object that contains a `Tuned` object manifest for creating 10 huge pages that are 2 MB in size. Save this `ConfigMap` manifest in a file named `tuned-hugepages.yaml`:

    ``` yaml
        apiVersion: v1
        kind: ConfigMap
        metadata:
          name: tuned-hugepages
          namespace: clusters
        data:
          tuning: |
            apiVersion: tuned.openshift.io/v1
            kind: Tuned
            metadata:
              name: hugepages
              namespace: openshift-cluster-node-tuning-operator
            spec:
              profile:
              - data: |
                  [main]
                  summary=Boot time configuration for hugepages
                  include=openshift-node
                  [bootloader]
                  cmdline_openshift_node_hugepages=hugepagesz=2M hugepages=50
                name: openshift-node-hugepages
              recommend:
              - priority: 20
                profile: openshift-node-hugepages
    ```

    > [!NOTE]
    > The `.spec.recommend.match` field is intentionally left blank. In this case, this `Tuned` object is applied to all nodes in the node pool where this `ConfigMap` object is referenced. Group nodes with the same hardware configuration into the same node pool. Otherwise, TuneD operands can calculate conflicting kernel parameters for two or more nodes that share the same node pool.

2.  Create the `ConfigMap` object in the management cluster:

    ``` terminal
    $ oc --kubeconfig="<management_cluster_kubeconfig>" create -f tuned-hugepages.yaml
    ```

    Replace `<management_cluster_kubeconfig>` with the name of your management cluster `kubeconfig` file.

3.  Create a `NodePool` manifest YAML file, customize the upgrade type of the `NodePool`, and reference the `ConfigMap` object that you created in the `spec.tuningConfig` section. Create the `NodePool` manifest and save it in a file named `hugepages-nodepool.yaml` by using the `hcp` CLI:

    ``` terminal
    $ hcp create nodepool aws \
      --cluster-name <hosted_cluster_name> \
      --name <nodepool_name> \
      --node-count <nodepool_replicas> \
      --instance-type <instance_type> \
      --render > hugepages-nodepool.yaml
    ```

    where:

    - `<hosted_cluster_name>`: The name of your hosted cluster.

    - `<nodepool_name>`: The name of your node pool.

    - `<nodepool_replicas>`: The number of your node pool replicas, for example, `2`.

    - `<instance_type>`: The instance type, for example, `m5.2xlarge`.

    > [!NOTE]
    > The `--render` flag in the `hcp create` command does not render the secrets. To render the secrets, you must use both the `--render` and the `--render-sensitive` flags in the `hcp create` command.

4.  In the `hugepages-nodepool.yaml` file, set `.spec.management.upgradeType` to `InPlace`, and set `.spec.tuningConfig` to reference the `tuned-hugepages` `ConfigMap` object that you created.

    ``` yaml
        apiVersion: hypershift.openshift.io/v1alpha1
        kind: NodePool
        metadata:
          name: hugepages-nodepool
          namespace: clusters
          ...
        spec:
          management:
            ...
            upgradeType: InPlace
          ...
          tuningConfig:
          - name: tuned-hugepages
    ```

    > [!NOTE]
    > To avoid the unnecessary re-creation of nodes when you apply the new `MachineConfig` objects, set `.spec.management.upgradeType` to `InPlace`. If you use the `Replace` upgrade type, nodes are fully deleted and new nodes can replace them when you apply the new kernel boot parameters that the TuneD operand calculated.

5.  Create the `NodePool` in the management cluster:

    ``` terminal
    $ oc --kubeconfig="<management_cluster_kubeconfig>" create -f hugepages-nodepool.yaml
    ```

</div>

<div class="formalpara">

<div class="title">

Verification

</div>

After the nodes are available, the containerized TuneD daemon calculates the required kernel boot parameters based on the applied TuneD profile. After the nodes are ready and reboot once to apply the generated `MachineConfig` object, you can verify that the TuneD profile is applied and that the kernel boot parameters are set.

</div>

1.  List the `Tuned` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="<hosted_cluster_kubeconfig>" get tuned.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                 AGE
    default              123m
    hugepages-8dfb1fed   1m23s
    rendered             123m
    ```

    </div>

2.  List the `Profile` objects in the hosted cluster:

    ``` terminal
    $ oc --kubeconfig="<hosted_cluster_kubeconfig>" get profile.tuned.openshift.io \
      -n openshift-cluster-node-tuning-operator
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                           TUNED                      APPLIED   DEGRADED   AGE
    nodepool-1-worker-1            openshift-node             True      False      132m
    nodepool-1-worker-2            openshift-node             True      False      131m
    hugepages-nodepool-worker-1    openshift-node-hugepages   True      False      4m8s
    hugepages-nodepool-worker-2    openshift-node-hugepages   True      False      3m57s
    ```

    </div>

    Both of the worker nodes in the new `NodePool` have the `openshift-node-hugepages` profile applied.

3.  To confirm that the tuning was applied correctly, start a debug shell on a node and check `/proc/cmdline`.

    ``` terminal
    $ oc --kubeconfig="<hosted_cluster_kubeconfig>" \
      debug node/nodepool-1-worker-1 -- chroot /host cat /proc/cmdline
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    BOOT_IMAGE=(hd0,gpt3)/ostree/rhcos-... hugepagesz=2M hugepages=50
    ```

    </div>

<div>

<div class="title">

Additional resources

</div>

- [Hosted control planes overview](../hosted_control_planes/index.md#hosted-control-planes-overview)

</div>
