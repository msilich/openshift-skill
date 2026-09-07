> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/configure-con_understanding_the_checluster_custom_resource). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How the central configuration works

Understand how OpenShift Dev Spaces behavior is controlled through the `CheCluster` Custom Resource, the single configuration object parameterized by the Red Hat OpenShift Dev Spaces Operator.

The `CheCluster` Custom Resource is a Kubernetes object. You can configure it by editing the `CheCluster` Custom Resource YAML file. This file contains sections to configure each component: `devWorkspace`, `cheServer`, `pluginRegistry`, `devfileRegistry`, `dashboard` and `imagePuller`.

The Red Hat OpenShift Dev Spaces Operator translates the `CheCluster` Custom Resource into a config map usable by each component of the OpenShift Dev Spaces installation.

The OpenShift platform applies the configuration to each component, and creates the necessary Pods. When OpenShift detects changes in the configuration of a component, it restarts the Pods accordingly. For background on OpenShift Operators and Custom Resources, see Additional resources.

When an administrator modifies the `CheCluster` Custom Resource, the configuration flows through the system as follows:

1.  The administrator applies the `CheCluster` Custom Resource YAML file with modifications in the `cheServer` component section.
2.  The Operator generates the `cheConfigMap`.
3.  OpenShift detects changes in the `ConfigMap` and triggers a restart of the OpenShift Dev Spaces Pod.

**Related information**  

- [Understanding Operators](https://docs.openshift.com/container-platform/4.22/operators/understanding/olm-what-operators-are.html)
- [Understanding Custom Resources](https://docs.openshift.com/container-platform/4.22/operators/understanding/crds/crd-managing-resources-from-crds.html)
