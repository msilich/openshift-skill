<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# com.coreos.monitoring.v1.AlertmanagerList schema

Description
AlertmanagerList is a list of Alertmanager

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Alertmanager)`](../monitoring_apis/alertmanager-monitoring-coreos-com-v1.md#alertmanager-monitoring-coreos-com-v1) | List of alertmanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.PodMonitorList schema

Description
PodMonitorList is a list of PodMonitor

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodMonitor)`](../monitoring_apis/podmonitor-monitoring-coreos-com-v1.md#podmonitor-monitoring-coreos-com-v1) | List of podmonitors. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.ProbeList schema

Description
ProbeList is a list of Probe

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Probe)`](../monitoring_apis/probe-monitoring-coreos-com-v1.md#probe-monitoring-coreos-com-v1) | List of probes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.PrometheusList schema

Description
PrometheusList is a list of Prometheus

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Prometheus)`](../monitoring_apis/prometheus-monitoring-coreos-com-v1.md#prometheus-monitoring-coreos-com-v1) | List of prometheuses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.PrometheusRuleList schema

Description
PrometheusRuleList is a list of PrometheusRule

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PrometheusRule)`](../monitoring_apis/prometheusrule-monitoring-coreos-com-v1.md#prometheusrule-monitoring-coreos-com-v1) | List of prometheusrules. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.ServiceMonitorList schema

Description
ServiceMonitorList is a list of ServiceMonitor

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceMonitor)`](../monitoring_apis/servicemonitor-monitoring-coreos-com-v1.md#servicemonitor-monitoring-coreos-com-v1) | List of servicemonitors. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1.ThanosRulerList schema

Description
ThanosRulerList is a list of ThanosRuler

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ThanosRuler)`](../monitoring_apis/thanosruler-monitoring-coreos-com-v1.md#thanosruler-monitoring-coreos-com-v1) | List of thanosrulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.monitoring.v1beta1.AlertmanagerConfigList schema

Description
AlertmanagerConfigList is a list of AlertmanagerConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertmanagerConfig)`](../monitoring_apis/alertmanagerconfig-monitoring-coreos-com-v1beta1.md#alertmanagerconfig-monitoring-coreos-com-v1beta1) | List of alertmanagerconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1.OLMConfigList schema

Description
OLMConfigList is a list of OLMConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OLMConfig)`](../operatorhub_apis/olmconfig-operators-coreos-com-v1.md#olmconfig-operators-coreos-com-v1) | List of olmconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1.OperatorGroupList schema

Description
OperatorGroupList is a list of OperatorGroup

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorGroup)`](../operatorhub_apis/operatorgroup-operators-coreos-com-v1.md#operatorgroup-operators-coreos-com-v1) | List of operatorgroups. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1.OperatorList schema

Description
OperatorList is a list of Operator

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Operator)`](../operatorhub_apis/operator-operators-coreos-com-v1.md#operator-operators-coreos-com-v1) | List of operators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1alpha1.CatalogSourceList schema

Description
CatalogSourceList is a list of CatalogSource

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CatalogSource)`](../operatorhub_apis/catalogsource-operators-coreos-com-v1alpha1.md#catalogsource-operators-coreos-com-v1alpha1) | List of catalogsources. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1alpha1.ClusterServiceVersionList schema

Description
ClusterServiceVersionList is a list of ClusterServiceVersion

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterServiceVersion)`](../operatorhub_apis/clusterserviceversion-operators-coreos-com-v1alpha1.md#clusterserviceversion-operators-coreos-com-v1alpha1) | List of clusterserviceversions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1alpha1.InstallPlanList schema

Description
InstallPlanList is a list of InstallPlan

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (InstallPlan)`](../operatorhub_apis/installplan-operators-coreos-com-v1alpha1.md#installplan-operators-coreos-com-v1alpha1) | List of installplans. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v1alpha1.SubscriptionList schema

Description
SubscriptionList is a list of Subscription

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Subscription)`](../operatorhub_apis/subscription-operators-coreos-com-v1alpha1.md#subscription-operators-coreos-com-v1alpha1) | List of subscriptions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.coreos.operators.v2.OperatorConditionList schema

Description
OperatorConditionList is a list of OperatorCondition

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorCondition)`](../operatorhub_apis/operatorcondition-operators-coreos-com-v2.md#operatorcondition-operators-coreos-com-v2) | List of operatorconditions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# com.github.openshift.api.apps.v1.DeploymentConfigList schema

Description
DeploymentConfigList is a collection of deployment configs.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DeploymentConfig)`](../workloads_apis/deploymentconfig-apps-openshift-io-v1.md#deploymentconfig-apps-openshift-io-v1) | Items is a list of deployment configs |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.authorization.v1.ClusterRoleBindingList schema

Description
ClusterRoleBindingList is a collection of ClusterRoleBindings

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRoleBinding)`](../role_apis/clusterrolebinding-authorization-openshift-io-v1.md#clusterrolebinding-authorization-openshift-io-v1) | Items is a list of ClusterRoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.authorization.v1.ClusterRoleList schema

Description
ClusterRoleList is a collection of ClusterRoles

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRole)`](../role_apis/clusterrole-authorization-openshift-io-v1.md#clusterrole-authorization-openshift-io-v1) | Items is a list of ClusterRoles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.authorization.v1.RoleBindingList schema

Description
RoleBindingList is a collection of RoleBindings

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBinding)`](../role_apis/rolebinding-authorization-openshift-io-v1.md#rolebinding-authorization-openshift-io-v1) | Items is a list of RoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.authorization.v1.RoleList schema

Description
RoleList is a collection of Roles

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Role)`](../role_apis/role-authorization-openshift-io-v1.md#role-authorization-openshift-io-v1) | Items is a list of Roles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.build.v1.BuildConfigList schema

Description
BuildConfigList is a collection of BuildConfigs.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BuildConfig)`](../workloads_apis/buildconfig-build-openshift-io-v1.md#buildconfig-build-openshift-io-v1) | items is a list of build configs |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.build.v1.BuildList schema

Description
BuildList is a collection of Builds.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Build)`](../workloads_apis/build-build-openshift-io-v1.md#build-build-openshift-io-v1) | items is a list of builds |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.image.v1.ImageList schema

Description
ImageList is a list of Image objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Image)`](../image_apis/image-image-openshift-io-v1.md#image-image-openshift-io-v1) | Items is a list of images |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.image.v1.ImageStreamList schema

Description
ImageStreamList is a list of ImageStream objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageStream)`](../image_apis/imagestream-image-openshift-io-v1.md#imagestream-image-openshift-io-v1) | Items is a list of imageStreams |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.image.v1.ImageStreamTagList schema

Description
ImageStreamTagList is a list of ImageStreamTag objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageStreamTag)`](../image_apis/imagestreamtag-image-openshift-io-v1.md#imagestreamtag-image-openshift-io-v1) | Items is the list of image stream tags |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.image.v1.ImageTagList schema

Description
ImageTagList is a list of ImageTag objects. When listing image tags, the image field is not populated. Tags are returned in alphabetical order by image stream and then tag.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageTag)`](../image_apis/imagetag-image-openshift-io-v1.md#imagetag-image-openshift-io-v1) | Items is the list of image stream tags |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.oauth.v1.OAuthAccessTokenList schema

Description
OAuthAccessTokenList is a collection of OAuth access tokens

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthAccessToken)`](../oauth_apis/oauthaccesstoken-oauth-openshift-io-v1.md#oauthaccesstoken-oauth-openshift-io-v1) | items is the list of OAuth access tokens |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.oauth.v1.OAuthAuthorizeTokenList schema

Description
OAuthAuthorizeTokenList is a collection of OAuth authorization tokens

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthAuthorizeToken)`](../oauth_apis/oauthauthorizetoken-oauth-openshift-io-v1.md#oauthauthorizetoken-oauth-openshift-io-v1) | items is the list of OAuth authorization tokens |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.oauth.v1.OAuthClientAuthorizationList schema

Description
OAuthClientAuthorizationList is a collection of OAuth client authorizations

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthClientAuthorization)`](../oauth_apis/oauthclientauthorization-oauth-openshift-io-v1.md#oauthclientauthorization-oauth-openshift-io-v1) | items is the list of OAuth client authorizations |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.oauth.v1.OAuthClientList schema

Description
OAuthClientList is a collection of OAuth clients

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuthClient)`](../oauth_apis/oauthclient-oauth-openshift-io-v1.md#oauthclient-oauth-openshift-io-v1) | items is the list of OAuth clients |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.oauth.v1.UserOAuthAccessTokenList schema

Description
UserOAuthAccessTokenList is a collection of access tokens issued on behalf of the requesting user

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (UserOAuthAccessToken)`](../oauth_apis/useroauthaccesstoken-oauth-openshift-io-v1.md#useroauthaccesstoken-oauth-openshift-io-v1) |  |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.project.v1.ProjectList schema

Description
ProjectList is a list of Project objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Project)`](../project_apis/project-project-openshift-io-v1.md#project-project-openshift-io-v1) | Items is the list of projects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.quota.v1.AppliedClusterResourceQuotaList schema

Description
AppliedClusterResourceQuotaList is a collection of AppliedClusterResourceQuotas

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AppliedClusterResourceQuota)`](../schedule_and_quota_apis/appliedclusterresourcequota-quota-openshift-io-v1.md#appliedclusterresourcequota-quota-openshift-io-v1) | Items is a list of AppliedClusterResourceQuota |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.route.v1.RouteList schema

Description
RouteList is a collection of Routes.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Route)`](../network_apis/route-route-openshift-io-v1.md#route-route-openshift-io-v1) | items is a list of routes |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.security.v1.RangeAllocationList schema

Description
RangeAllocationList is a list of RangeAllocations objects

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RangeAllocation)`](../security_apis/rangeallocation-security-openshift-io-v1.md#rangeallocation-security-openshift-io-v1) | List of RangeAllocations. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.template.v1.BrokerTemplateInstanceList schema

Description
BrokerTemplateInstanceList is a list of BrokerTemplateInstance objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BrokerTemplateInstance)`](../template_apis/brokertemplateinstance-template-openshift-io-v1.md#brokertemplateinstance-template-openshift-io-v1) | items is a list of BrokerTemplateInstances |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.template.v1.TemplateInstanceList schema

Description
TemplateInstanceList is a list of TemplateInstance objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (TemplateInstance)`](../template_apis/templateinstance-template-openshift-io-v1.md#templateinstance-template-openshift-io-v1) | items is a list of Templateinstances |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.template.v1.TemplateList schema

Description
TemplateList is a list of Template objects.

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Template)`](../template_apis/template-template-openshift-io-v1.md#template-template-openshift-io-v1) | Items is a list of templates |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.user.v1.GroupList schema

Description
GroupList is a collection of Groups

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Group)`](../user_and_group_apis/group-user-openshift-io-v1.md#group-user-openshift-io-v1) | items is the list of groups |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.user.v1.IdentityList schema

Description
IdentityList is a collection of Identities

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Identity)`](../user_and_group_apis/identity-user-openshift-io-v1.md#identity-user-openshift-io-v1) | items is the list of identities |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.openshift.api.user.v1.UserList schema

Description
UserList is a collection of Users

Compatibility level 1: Stable within a major release for a minimum of 12 months or 3 minor releases (whichever is longer).

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (User)`](../user_and_group_apis/user-user-openshift-io-v1.md#user-user-openshift-io-v1) | items is the list of users |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# com.github.operator-framework.api.pkg.lib.version.OperatorVersion schema

Description
OperatorVersion is a wrapper around semver.Version which supports correct marshaling to YAML and JSON.

Type
`string`

# com.github.operator-framework.api.pkg.operators.v1alpha1.APIServiceDefinitions schema

Description
APIServiceDefinitions declares all of the extension apis managed or required by an operator being ran by ClusterServiceVersion.

Type
`object`

## Schema

| Property   | Type                            | Description |
|------------|---------------------------------|-------------|
| `owned`    | `array (APIServiceDescription)` |             |
| `required` | `array (APIServiceDescription)` |             |

# com.github.operator-framework.api.pkg.operators.v1alpha1.CustomResourceDefinitions schema

Description
CustomResourceDefinitions declares all of the CRDs managed or required by an operator being ran by ClusterServiceVersion.

If the CRD is present in the Owned list, it is implicitly required.

Type
`object`

## Schema

| Property   | Type                     | Description |
|------------|--------------------------|-------------|
| `owned`    | `array (CRDDescription)` |             |
| `required` | `array (CRDDescription)` |             |

# com.github.operator-framework.api.pkg.operators.v1alpha1.InstallMode schema

Description
InstallMode associates an InstallModeType with a flag representing if the CSV supports it

Type
`object`

Required
- `type`

- `supported`

## Schema

| Property    | Type      | Description |
|-------------|-----------|-------------|
| `supported` | `boolean` |             |
| `type`      | `string`  |             |

# com.github.operator-framework.operator-lifecycle-manager.pkg.package-server.apis.operators.v1.PackageManifestList schema

Description
PackageManifestList is a list of PackageManifest objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PackageManifest)`](../operatorhub_apis/packagemanifest-packages-operators-coreos-com-v1.md#packagemanifest-packages-operators-coreos-com-v1) |  |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) |  |

# io.cncf.cni.k8s.v1.NetworkAttachmentDefinitionList schema

Description
NetworkAttachmentDefinitionList is a list of NetworkAttachmentDefinition

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NetworkAttachmentDefinition)`](../network_apis/networkattachmentdefinition-k8s-cni-cncf-io-v1.md#networkattachmentdefinition-k8s-cni-cncf-io-v1) | List of network-attachment-definitions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.cncf.cni.k8s.v1alpha1.IPAMClaimList schema

Description
IPAMClaimList is a list of IPAMClaim

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAMClaim)`](../network_apis/ipamclaim-k8s-cni-cncf-io-v1alpha1.md#ipamclaim-k8s-cni-cncf-io-v1alpha1) | List of ipamclaims. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.cncf.cni.k8s.v1beta1.MultiNetworkPolicyList schema

Description
MultiNetworkPolicyList is a list of MultiNetworkPolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MultiNetworkPolicy)`](../network_apis/multinetworkpolicy-k8s-cni-cncf-io-v1beta1.md#multinetworkpolicy-k8s-cni-cncf-io-v1beta1) | List of multi-networkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.cncf.cni.whereabouts.v1alpha1.IPPoolList schema

Description
IPPoolList is a list of IPPool

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPPool)`](../network_apis/ippool-whereabouts-cni-cncf-io-v1alpha1.md#ippool-whereabouts-cni-cncf-io-v1alpha1) | List of ippools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.cncf.cni.whereabouts.v1alpha1.NodeSlicePoolList schema

Description
NodeSlicePoolList is a list of NodeSlicePool

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NodeSlicePool)`](../network_apis/nodeslicepool-whereabouts-cni-cncf-io-v1alpha1.md#nodeslicepool-whereabouts-cni-cncf-io-v1alpha1) | List of nodeslicepools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.cncf.cni.whereabouts.v1alpha1.OverlappingRangeIPReservationList schema

Description
OverlappingRangeIPReservationList is a list of OverlappingRangeIPReservation

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OverlappingRangeIPReservation)`](../network_apis/overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1.md#overlappingrangeipreservation-whereabouts-cni-cncf-io-v1alpha1) | List of overlappingrangeipreservations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.admissionregistration.v1.MutatingWebhookConfigurationList schema

Description
MutatingWebhookConfigurationList is a list of MutatingWebhookConfiguration.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MutatingWebhookConfiguration)`](../extension_apis/mutatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#mutatingwebhookconfiguration-admissionregistration-k8s-io-v1) | List of MutatingWebhookConfiguration. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyBindingList schema

Description
ValidatingAdmissionPolicyBindingList is a list of ValidatingAdmissionPolicyBinding.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingAdmissionPolicyBinding)`](../extension_apis/validatingadmissionpolicybinding-admissionregistration-k8s-io-v1.md#validatingadmissionpolicybinding-admissionregistration-k8s-io-v1) | List of PolicyBinding. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.admissionregistration.v1.ValidatingAdmissionPolicyList schema

Description
ValidatingAdmissionPolicyList is a list of ValidatingAdmissionPolicy.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingAdmissionPolicy)`](../extension_apis/validatingadmissionpolicy-admissionregistration-k8s-io-v1.md#validatingadmissionpolicy-admissionregistration-k8s-io-v1) | List of ValidatingAdmissionPolicy. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.admissionregistration.v1.ValidatingWebhookConfigurationList schema

Description
ValidatingWebhookConfigurationList is a list of ValidatingWebhookConfiguration.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ValidatingWebhookConfiguration)`](../extension_apis/validatingwebhookconfiguration-admissionregistration-k8s-io-v1.md#validatingwebhookconfiguration-admissionregistration-k8s-io-v1) | List of ValidatingWebhookConfiguration. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.apps.v1.ControllerRevisionList schema

Description
ControllerRevisionList is a resource containing a list of ControllerRevision objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControllerRevision)`](../metadata_apis/controllerrevision-apps-v1.md#controllerrevision-apps-v1) | Items is the list of ControllerRevisions |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.apps.v1.DaemonSetList schema

Description
DaemonSetList is a collection of daemon sets.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DaemonSet)`](../workloads_apis/daemonset-apps-v1.md#daemonset-apps-v1) | A list of daemon sets. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.apps.v1.DeploymentList schema

Description
DeploymentList is a list of Deployments.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Deployment)`](../workloads_apis/deployment-apps-v1.md#deployment-apps-v1) | Items is the list of Deployments. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. |

# io.k8s.api.apps.v1.ReplicaSetList schema

Description
ReplicaSetList is a collection of ReplicaSets.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReplicaSet)`](../workloads_apis/replicaset-apps-v1.md#replicaset-apps-v1) | List of ReplicaSets. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicaset> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.apps.v1.StatefulSetList schema

Description
StatefulSetList is a collection of StatefulSets.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StatefulSet)`](../workloads_apis/statefulset-apps-v1.md#statefulset-apps-v1) | Items is the list of stateful sets. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.autoscaling.v2.HorizontalPodAutoscalerList schema

Description
HorizontalPodAutoscalerList is a list of horizontal pod autoscaler objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HorizontalPodAutoscaler)`](../autoscale_apis/horizontalpodautoscaler-autoscaling-v2.md#horizontalpodautoscaler-autoscaling-v2) | items is the list of horizontal pod autoscaler objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | metadata is the standard list metadata. |

# io.k8s.api.batch.v1.CronJobList schema

Description
CronJobList is a collection of cron jobs.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CronJob)`](../workloads_apis/cronjob-batch-v1.md#cronjob-batch-v1) | items is the list of CronJobs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.batch.v1.JobList schema

Description
JobList is a collection of jobs.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Job)`](../workloads_apis/job-batch-v1.md#job-batch-v1) | items is the list of Jobs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.certificates.v1.CertificateSigningRequestList schema

Description
CertificateSigningRequestList is a collection of CertificateSigningRequest objects

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CertificateSigningRequest)`](../security_apis/certificatesigningrequest-certificates-k8s-io-v1.md#certificatesigningrequest-certificates-k8s-io-v1) | items is a collection of CertificateSigningRequest objects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) |  |

# io.k8s.api.coordination.v1.LeaseList schema

Description
LeaseList is a list of Lease objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Lease)`](../metadata_apis/lease-coordination-k8s-io-v1.md#lease-coordination-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.core.v1.ComponentStatusList schema

Description
Status of all the conditions for the component as a list of ComponentStatus objects. Deprecated: This API is deprecated in v1.19+

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ComponentStatus)`](../metadata_apis/componentstatus-v1.md#componentstatus-v1) | List of ComponentStatus objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.ConfigMapList schema

Description
ConfigMapList is a resource containing a list of ConfigMap objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConfigMap)`](../metadata_apis/configmap-v1.md#configmap-v1) | Items is the list of ConfigMaps. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.core.v1.ConfigMapVolumeSource_v2 schema

Description
Adapts a ConfigMap into a volume.

The contents of the target ConfigMap’s Data field will be presented in a volume as files using the keys in the Data field as the file names, unless the items element is populated with specific mappings of keys to paths. ConfigMap volumes support ownership management and SELinux relabeling.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array (KeyToPath)` | items if unspecified, each key-value pair in the Data field of the referenced ConfigMap will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the ConfigMap, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `optional` | `boolean` | optional specify whether the ConfigMap or its keys must be defined |

# io.k8s.api.core.v1.CSIVolumeSource schema

Description
Represents a source location of a volume to mount, managed by an external CSI driver

Type
`object`

Required
- `driver`

## Schema

| Property | Type | Description |
|----|----|----|
| `driver` | `string` | driver is the name of the CSI driver that handles this volume. Consult with your admin for the correct name as registered in the cluster. |
| `fsType` | `string` | fsType to mount. Ex. "ext4", "xfs", "ntfs". If not provided, the empty value is passed to the associated CSI driver which will determine the default filesystem to apply. |
| `nodePublishSecretRef` | `LocalObjectReference` | nodePublishSecretRef is a reference to the secret object containing sensitive information to pass to the CSI driver to complete the CSI NodePublishVolume and NodeUnpublishVolume calls. This field is optional, and may be empty if no secret is required. If the secret object contains more than one secret, all secret references are passed. |
| `readOnly` | `boolean` | readOnly specifies a read-only configuration for the volume. Defaults to false (read/write). |
| `volumeAttributes` | `object (string)` | volumeAttributes stores driver-specific properties that are passed to the CSI driver. Consult your driver’s documentation for supported values. |

# io.k8s.api.core.v1.EndpointsList schema

Description
EndpointsList is a list of endpoints. Deprecated: This API is deprecated in v1.33+.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Endpoints)`](../network_apis/endpoints-v1.md#endpoints-v1) | List of endpoints. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.EnvVar schema

Description
EnvVar represents an environment variable present in a Container.

Type
`object`

Required
- `name`

## Schema

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the environment variable. Must be a C_IDENTIFIER. |
| `value` | `string` | Variable references \$(VAR_NAME) are expanded using the previously defined environment variables in the container and any service environment variables. If a variable cannot be resolved, the reference in the input string will be unchanged. Double are reduced to a single \$, which allows for escaping the \$(VAR_NAME) syntax: i.e. "(VAR_NAME)" will produce the string literal "\$(VAR_NAME)". Escaped references will never be expanded, regardless of whether the variable exists or not. Defaults to "". |
| `valueFrom` | `EnvVarSource` | Source for the environment variable’s value. Cannot be used if value is not empty. |

# io.k8s.api.core.v1.EventList schema

Description
EventList is a list of events.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Event)`](../metadata_apis/event-v1.md#event-v1) | List of events |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.EventSource schema

Description
EventSource contains information for an event.

Type
`object`

## Schema

| Property    | Type     | Description                                  |
|-------------|----------|----------------------------------------------|
| `component` | `string` | Component from which the event is generated. |
| `host`      | `string` | Node name on which the event is generated.   |

# io.k8s.api.core.v1.LimitRangeList schema

Description
LimitRangeList is a list of LimitRange items.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (LimitRange)`](../schedule_and_quota_apis/limitrange-v1.md#limitrange-v1) | Items is a list of LimitRange objects. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.LocalObjectReference_v2 schema

Description
LocalObjectReference contains enough information to let you locate the referenced object inside the same namespace.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |

# io.k8s.api.core.v1.NamespaceCondition_v2 schema

Description
NamespaceCondition contains details about state of namespace.

Type
`object`

Required
- `type`

- `status`

## Schema

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) |  |
| `message` | `string` |  |
| `reason` | `string` |  |
| `status` | `string` | Status of the condition, one of True, False, Unknown. |
| `type` | `string` | Type of namespace controller condition. |

# io.k8s.api.core.v1.NamespaceList schema

Description
NamespaceList is a list of Namespaces.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Namespace)`](../metadata_apis/namespace-v1.md#namespace-v1) | Items is the list of Namespace objects in the list. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.NodeList schema

Description
NodeList is the whole list of all Nodes which have been registered with master.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Node)`](../node_apis/node-v1.md#node-v1) | List of nodes |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.ObjectReference schema

Description
ObjectReference contains enough information to let you inspect or modify the referred object.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | API version of the referent. |
| `fieldPath` | `string` | If referring to a piece of an object instead of an entire object, this string should contain a valid JSON/Go field access statement, such as desiredState.manifest.containers\[2\]. For example, if the object reference is to a container within a pod, this would take on a value like: "spec.containers{name}" (where "name" refers to the name of the container that triggered the event) or if no container name is specified "spec.containers\[2\]" (container with index 2 in this pod). This syntax is chosen only to have some well-defined way of referencing a part of an object. |
| `kind` | `string` | Kind of the referent. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `name` | `string` | Name of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#names> |
| `namespace` | `string` | Namespace of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/> |
| `resourceVersion` | `string` | Specific resourceVersion to which this reference is made, if any. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `uid` | `string` | UID of the referent. More info: <https://kubernetes.io/docs/concepts/overview/working-with-objects/names/#uids> |

# io.k8s.api.core.v1.PersistentVolumeClaim schema

Description
PersistentVolumeClaim is a user’s request for and claim to a persistent volume

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `object` | PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes |
| `status` | `object` | PersistentVolumeClaimStatus is the current status of a persistent volume claim. |

Description
PersistentVolumeClaimSpec describes the common attributes of storage devices and allows a Source for provider-specific attributes

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessModes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>accessModes contains the desired access modes the volume should have. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSource</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dataSourceRef</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>TypedObjectReference contains enough information to let you locate the typed referenced object</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resources</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>VolumeResourceRequirements describes the storage resource requirements for a volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selector</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelector"><code>LabelSelector</code></a></p></td>
<td style="text-align: left;"><p>selector is a label query over volumes to consider for binding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>storageClassName is the name of the StorageClass required by the claim. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#class-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeAttributesClassName may be used to set the VolumeAttributesClass used by this claim. If specified, the CSI driver will create or update the volume with the attributes defined in the corresponding VolumeAttributesClass. This has a different purpose than storageClassName, it can be changed after the claim is created. An empty string value means that no VolumeAttributesClass will be applied to the claim but it’s not allowed to reset this field to empty string once it is set. If unspecified and the PersistentVolumeClaim is unbound, the default VolumeAttributesClass will be set by the persistentvolume controller if it exists. If the resource referred to by volumeAttributesClass does not exist, this PersistentVolumeClaim will be set to a Pending state, as reflected by the modifyVolumeStatus field, until such as a resource exists. More info: <a href="https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/">https://kubernetes.io/docs/concepts/storage/volume-attributes-classes/</a> (Beta) Using this field requires the VolumeAttributesClass feature gate to be enabled (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeMode defines what type of volume is required by the claim. Value of Filesystem is implied when not included in claim spec.</p>
<p>Possible enum values: - <code>"Block"</code> means the volume will not be formatted with a filesystem and will remain a raw block device. - <code>"Filesystem"</code> means the volume will be or is formatted with a filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeName is the binding reference to the PersistentVolume backing this claim.</p></td>
</tr>
</tbody>
</table>

Description
TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

Description
TypedObjectReference contains enough information to let you locate the typed referenced object

Type
`object`

Required
- `kind`

- `name`

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |
| `namespace` | `string` | Namespace is the namespace of resource being referenced Note that when a namespace is specified, a gateway.networking.k8s.io/ReferenceGrant object is required in the referent namespace to allow that namespace’s owner to accept the reference. See the ReferenceGrant documentation for details. (Alpha) This field requires the CrossNamespaceVolumeDataSource feature gate to be enabled. |

Description
VolumeResourceRequirements describes the storage resource requirements for a volume.

Type
`object`

| Property | Type | Description |
|----|----|----|
| `limits` | [`object (Quantity)`](index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Limits describes the maximum amount of compute resources allowed. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |
| `requests` | [`object (Quantity)`](index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/> |

Description
PersistentVolumeClaimStatus is the current status of a persistent volume claim.

Type
`object`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessModes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>accessModes contains the actual access modes the volume backing the PVC has. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes-1</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allocatedResourceStatuses</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>allocatedResourceStatuses stores status of resource being resized for the given PVC. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.</p>
<p>ClaimResourceStatus can be in any of following states: - ControllerResizeInProgress: State set when resize controller starts resizing the volume in control-plane. - ControllerResizeFailed: State set when resize has failed in resize controller with a terminal error. - NodeResizePending: State set when resize controller has finished resizing the volume but further resizing of volume is needed on the node. - NodeResizeInProgress: State set when kubelet starts resizing the volume. - NodeResizeFailed: State set when resizing has failed in kubelet with a terminal error. Transient errors don’t set NodeResizeFailed. For example: if expanding a PVC for more capacity - this field can be one of the following states: - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "ControllerResizeFailed" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizePending" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeInProgress" - pvc.status.allocatedResourceStatus['storage'] = "NodeResizeFailed" When this field is not set, it means that no resize operation is in progress for the given PVC.</p>
<p>A controller that receives PVC update with previously unknown resourceName or ClaimResourceStatus should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.</p>
<p>This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allocatedResources</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>allocatedResources tracks the resources allocated to a PVC including its capacity. Key names follow standard Kubernetes label syntax. Valid values are either: * Un-prefixed keys: - storage - the capacity of the volume. * Custom resources must use implementation-defined prefixed names such as "example.com/my-custom-resource" Apart from above values - keys that are unprefixed or have kubernetes.io prefix are considered reserved and hence may not be used.</p>
<p>Capacity reported here may be larger than the actual capacity when a volume expansion operation is requested. For storage quota, the larger value from allocatedResources and PVC.spec.resources is used. If allocatedResources is not set, PVC.spec.resources alone is used for quota calculation. If a volume expansion capacity request is lowered, allocatedResources is only lowered if there are no expansion operations in progress and if the actual volume capacity is equal or lower than the requested capacity.</p>
<p>A controller that receives PVC update with previously unknown resourceName should ignore the update for the purpose it was designed. For example - a controller that only is responsible for resizing capacity of the volume, should ignore PVC updates that change other valid resources associated with PVC.</p>
<p>This is an alpha field and requires enabling RecoverVolumeExpansionFailure feature.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>capacity represents the actual resources of the underlying volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions</code></p></td>
<td style="text-align: left;"><p><code>array</code></p></td>
<td style="text-align: left;"><p>conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>conditions[]</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>PersistentVolumeClaimCondition contains details about state of pvc</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>currentVolumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>currentVolumeAttributesClassName is the current name of the VolumeAttributesClass the PVC is using. When unset, there is no VolumeAttributeClass applied to this PersistentVolumeClaim This is a beta field and requires enabling VolumeAttributesClass feature (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>modifyVolumeStatus</code></p></td>
<td style="text-align: left;"><p><code>object</code></p></td>
<td style="text-align: left;"><p>ModifyVolumeStatus represents the status object of ControllerModifyVolume operation</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phase</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>phase represents the current phase of PersistentVolumeClaim.</p>
<p>Possible enum values: - <code>"Bound"</code> used for PersistentVolumeClaims that are bound - <code>"Lost"</code> used for PersistentVolumeClaims that lost their underlying PersistentVolume. The claim was bound to a PersistentVolume and this volume does not exist any longer and all data on it was lost. - <code>"Pending"</code> used for PersistentVolumeClaims that are not yet bound</p></td>
</tr>
</tbody>
</table>

Description
conditions is the current Condition of persistent volume claim. If underlying persistent volume is being resized then the Condition will be set to 'Resizing'.

Type
`array`

<!-- -->

Description
PersistentVolumeClaimCondition contains details about state of pvc

Type
`object`

Required
- `type`

- `status`

| Property | Type | Description |
|----|----|----|
| `lastProbeTime` | [`Time`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastProbeTime is the time we probed the condition. |
| `lastTransitionTime` | [`Time`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastTransitionTime is the time the condition transitioned from one status to another. |
| `message` | `string` | message is the human-readable message indicating details about last transition. |
| `reason` | `string` | reason is a unique, this should be a short, machine understandable string that gives the reason for condition’s last transition. If it reports "Resizing" that means the underlying persistent volume is being resized. |
| `status` | `string` | Status is the status of the condition. Can be True, False, Unknown. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=state%20of%20pvc-,conditions.status,-(string)%2C%20required> |
| `type` | `string` | Type is the type of the condition. More info: <https://kubernetes.io/docs/reference/kubernetes-api/config-and-storage-resources/persistent-volume-claim-v1/#:~:text=set%20to%20%27ResizeStarted%27.-,PersistentVolumeClaimCondition,-contains%20details%20about> |

Description
ModifyVolumeStatus represents the status object of ControllerModifyVolume operation

Type
`object`

Required
- `status`

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>status</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>status is the status of the ControllerModifyVolume operation. It can be in any of following states: - Pending Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing. - InProgress InProgress indicates that the volume is being modified. - Infeasible Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified. Note: New statuses can be added in the future. Consumers should check for unknown statuses and fail appropriately.</p>
<p>Possible enum values: - <code>"InProgress"</code> InProgress indicates that the volume is being modified - <code>"Infeasible"</code> Infeasible indicates that the request has been rejected as invalid by the CSI driver. To resolve the error, a valid VolumeAttributesClass needs to be specified - <code>"Pending"</code> Pending indicates that the PersistentVolumeClaim cannot be modified due to unmet requirements, such as the specified VolumeAttributesClass not existing</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>targetVolumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>targetVolumeAttributesClassName is the name of the VolumeAttributesClass the PVC currently being reconciled</p></td>
</tr>
</tbody>
</table>

# io.k8s.api.core.v1.PersistentVolumeClaimList schema

Description
PersistentVolumeClaimList is a list of PersistentVolumeClaim items.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PersistentVolumeClaim)`](../storage_apis/persistentvolumeclaim-v1.md#persistentvolumeclaim-v1) | items is a list of persistent volume claims. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes#persistentvolumeclaims> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.PersistentVolumeList schema

Description
PersistentVolumeList is a list of PersistentVolume items.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PersistentVolume)`](../storage_apis/persistentvolume-v1.md#persistentvolume-v1) | items is a list of persistent volumes. More info: <https://kubernetes.io/docs/concepts/storage/persistent-volumes> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.PersistentVolumeSpec schema

Description
PersistentVolumeSpec is the specification of a persistent volume.

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>accessModes</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>accessModes contains all ways the volume can be mounted. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes">https://kubernetes.io/docs/concepts/storage/persistent-volumes#access-modes</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>awsElasticBlockStore</code></p></td>
<td style="text-align: left;"><p><code>AWSElasticBlockStoreVolumeSource</code></p></td>
<td style="text-align: left;"><p>awsElasticBlockStore represents an AWS Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Deprecated: AWSElasticBlockStore is deprecated. All operations for the in-tree awsElasticBlockStore type are redirected to the ebs.csi.aws.com CSI driver. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore">https://kubernetes.io/docs/concepts/storage/volumes#awselasticblockstore</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureDisk</code></p></td>
<td style="text-align: left;"><p><code>AzureDiskVolumeSource</code></p></td>
<td style="text-align: left;"><p>azureDisk represents an Azure Data Disk mount on the host and bind mount to the pod. Deprecated: AzureDisk is deprecated. All operations for the in-tree azureDisk type are redirected to the disk.csi.azure.com CSI driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>azureFile</code></p></td>
<td style="text-align: left;"><p><code>AzureFilePersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>azureFile represents an Azure File Service mount on the host and bind mount to the pod. Deprecated: AzureFile is deprecated. All operations for the in-tree azureFile type are redirected to the file.csi.azure.com CSI driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>capacity</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>capacity is the description of the persistent volume’s resources and capacity. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity">https://kubernetes.io/docs/concepts/storage/persistent-volumes#capacity</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cephfs</code></p></td>
<td style="text-align: left;"><p><code>CephFSPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>cephFS represents a Ceph FS mount on the host that shares a pod’s lifetime. Deprecated: CephFS is deprecated and the in-tree cephfs type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cinder</code></p></td>
<td style="text-align: left;"><p><code>CinderPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>cinder represents a cinder volume attached and mounted on kubelets host machine. Deprecated: Cinder is deprecated. All operations for the in-tree cinder type are redirected to the cinder.csi.openstack.org CSI driver. More info: <a href="https://examples.k8s.io/mysql-cinder-pd/README.md">https://examples.k8s.io/mysql-cinder-pd/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimRef</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-api-core-v1-ObjectReference"><code>ObjectReference</code></a></p></td>
<td style="text-align: left;"><p>claimRef is part of a bi-directional binding between PersistentVolume and PersistentVolumeClaim. Expected to be non-nil when bound. claim.VolumeName is the authoritative bind between PV and PVC. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding">https://kubernetes.io/docs/concepts/storage/persistent-volumes#binding</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>csi</code></p></td>
<td style="text-align: left;"><p><code>CSIPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>csi represents storage that is handled by an external CSI driver.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>fc</code></p></td>
<td style="text-align: left;"><p><code>FCVolumeSource</code></p></td>
<td style="text-align: left;"><p>fc represents a Fibre Channel resource that is attached to a kubelet’s host machine and then exposed to the pod.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flexVolume</code></p></td>
<td style="text-align: left;"><p><code>FlexPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>flexVolume represents a generic volume resource that is provisioned/attached using an exec based plugin. Deprecated: FlexVolume is deprecated. Consider using a CSIDriver instead.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>flocker</code></p></td>
<td style="text-align: left;"><p><code>FlockerVolumeSource</code></p></td>
<td style="text-align: left;"><p>flocker represents a Flocker volume attached to a kubelet’s host machine and exposed to the pod for its usage. This depends on the Flocker control service being running. Deprecated: Flocker is deprecated and the in-tree flocker type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>gcePersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>GCEPersistentDiskVolumeSource</code></p></td>
<td style="text-align: left;"><p>gcePersistentDisk represents a GCE Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Provisioned by an admin. Deprecated: GCEPersistentDisk is deprecated. All operations for the in-tree gcePersistentDisk type are redirected to the pd.csi.storage.gke.io CSI driver. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk">https://kubernetes.io/docs/concepts/storage/volumes#gcepersistentdisk</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>glusterfs</code></p></td>
<td style="text-align: left;"><p><code>GlusterfsPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>glusterfs represents a Glusterfs volume that is attached to a host and exposed to the pod. Provisioned by an admin. Deprecated: Glusterfs is deprecated and the in-tree glusterfs type is no longer supported. More info: <a href="https://examples.k8s.io/volumes/glusterfs/README.md">https://examples.k8s.io/volumes/glusterfs/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>hostPath</code></p></td>
<td style="text-align: left;"><p><code>HostPathVolumeSource</code></p></td>
<td style="text-align: left;"><p>hostPath represents a directory on the host. Provisioned by a developer or tester. This is useful for single-node development and testing only! On-host storage is not supported in any way and WILL NOT WORK in a multi-node cluster. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#hostpath">https://kubernetes.io/docs/concepts/storage/volumes#hostpath</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>iscsi</code></p></td>
<td style="text-align: left;"><p><code>ISCSIPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>iscsi represents an ISCSI Disk resource that is attached to a kubelet’s host machine and then exposed to the pod. Provisioned by an admin.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>local</code></p></td>
<td style="text-align: left;"><p><code>LocalVolumeSource</code></p></td>
<td style="text-align: left;"><p>local represents directly-attached storage with node affinity</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>mountOptions</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>mountOptions is the list of mount options, e.g. ["ro", "soft"]. Not validated - mount will simply fail if one is invalid. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options">https://kubernetes.io/docs/concepts/storage/persistent-volumes/#mount-options</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nfs</code></p></td>
<td style="text-align: left;"><p><code>NFSVolumeSource</code></p></td>
<td style="text-align: left;"><p>nfs represents an NFS mount on the host. Provisioned by an admin. More info: <a href="https://kubernetes.io/docs/concepts/storage/volumes#nfs">https://kubernetes.io/docs/concepts/storage/volumes#nfs</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nodeAffinity</code></p></td>
<td style="text-align: left;"><p><code>VolumeNodeAffinity</code></p></td>
<td style="text-align: left;"><p>nodeAffinity defines constraints that limit what nodes this volume can be accessed from. This field influences the scheduling of pods that use this volume.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>persistentVolumeReclaimPolicy</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>persistentVolumeReclaimPolicy defines what happens to a persistent volume when released from its claim. Valid options are Retain (default for manually created PersistentVolumes), Delete (default for dynamically provisioned PersistentVolumes), and Recycle (deprecated). Recycle must be supported by the volume plugin underlying this PersistentVolume. More info: <a href="https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming">https://kubernetes.io/docs/concepts/storage/persistent-volumes#reclaiming</a></p>
<p>Possible enum values: - <code>"Delete"</code> means the volume will be deleted from Kubernetes on release from its claim. The volume plugin must support Deletion. - <code>"Recycle"</code> means the volume will be recycled back into the pool of unbound persistent volumes on release from its claim. The volume plugin must support Recycling. - <code>"Retain"</code> means the volume will be left in its current phase (Released) for manual reclamation by the administrator. The default policy is Retain.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>photonPersistentDisk</code></p></td>
<td style="text-align: left;"><p><code>PhotonPersistentDiskVolumeSource</code></p></td>
<td style="text-align: left;"><p>photonPersistentDisk represents a PhotonController persistent disk attached and mounted on kubelets host machine. Deprecated: PhotonPersistentDisk is deprecated and the in-tree photonPersistentDisk type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>portworxVolume</code></p></td>
<td style="text-align: left;"><p><code>PortworxVolumeSource</code></p></td>
<td style="text-align: left;"><p>portworxVolume represents a portworx volume attached and mounted on kubelets host machine. Deprecated: PortworxVolume is deprecated. All operations for the in-tree portworxVolume type are redirected to the pxd.portworx.com CSI driver when the CSIMigrationPortworx feature-gate is on.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>quobyte</code></p></td>
<td style="text-align: left;"><p><code>QuobyteVolumeSource</code></p></td>
<td style="text-align: left;"><p>quobyte represents a Quobyte mount on the host that shares a pod’s lifetime. Deprecated: Quobyte is deprecated and the in-tree quobyte type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>rbd</code></p></td>
<td style="text-align: left;"><p><code>RBDPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>rbd represents a Rados Block Device mount on the host that shares a pod’s lifetime. Deprecated: RBD is deprecated and the in-tree rbd type is no longer supported. More info: <a href="https://examples.k8s.io/volumes/rbd/README.md">https://examples.k8s.io/volumes/rbd/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>scaleIO</code></p></td>
<td style="text-align: left;"><p><code>ScaleIOPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>scaleIO represents a ScaleIO persistent volume attached and mounted on Kubernetes nodes. Deprecated: ScaleIO is deprecated and the in-tree scaleIO type is no longer supported.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>storageClassName is the name of StorageClass to which this persistent volume belongs. Empty value means that this volume does not belong to any StorageClass.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>storageos</code></p></td>
<td style="text-align: left;"><p><code>StorageOSPersistentVolumeSource</code></p></td>
<td style="text-align: left;"><p>storageOS represents a StorageOS volume that is attached to the kubelet’s host machine and mounted into the pod. Deprecated: StorageOS is deprecated and the in-tree storageos type is no longer supported. More info: <a href="https://examples.k8s.io/volumes/storageos/README.md">https://examples.k8s.io/volumes/storageos/README.md</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeAttributesClassName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of VolumeAttributesClass to which this persistent volume belongs. Empty value is not allowed. When this field is not set, it indicates that this volume does not belong to any VolumeAttributesClass. This field is mutable and can be changed by the CSI driver after a volume has been updated successfully to a new class. For an unbound PersistentVolume, the volumeAttributesClassName will be matched with unbound PersistentVolumeClaims during the binding process. This is a beta field and requires enabling VolumeAttributesClass feature (off by default).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>volumeMode</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>volumeMode defines if a volume is intended to be used with a formatted filesystem or to remain in raw block state. Value of Filesystem is implied when not included in spec.</p>
<p>Possible enum values: - <code>"Block"</code> means the volume will not be formatted with a filesystem and will remain a raw block device. - <code>"Filesystem"</code> means the volume will be or is formatted with a filesystem.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>vsphereVolume</code></p></td>
<td style="text-align: left;"><p><code>VsphereVirtualDiskVolumeSource</code></p></td>
<td style="text-align: left;"><p>vsphereVolume represents a vSphere volume attached and mounted on kubelets host machine. Deprecated: VsphereVolume is deprecated. All operations for the in-tree vsphereVolume type are redirected to the csi.vsphere.vmware.com CSI driver.</p></td>
</tr>
</tbody>
</table>

# io.k8s.api.core.v1.PodList schema

Description
PodList is a list of Pods.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Pod)`](../workloads_apis/pod-v1.md#pod-v1) | List of pods. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.PodTemplateList schema

Description
PodTemplateList is a list of PodTemplates.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodTemplate)`](../template_apis/podtemplate-v1.md#podtemplate-v1) | List of pod templates |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.PodTemplateSpec schema

Description
PodTemplateSpec describes the data a pod should have when created from a template

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `metadata` | [`ObjectMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `spec` | `PodSpec` | Specification of the desired behavior of the pod. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.api.core.v1.ReplicationControllerList schema

Description
ReplicationControllerList is a collection of replication controllers.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReplicationController)`](../workloads_apis/replicationcontroller-v1.md#replicationcontroller-v1) | List of replication controllers. More info: <https://kubernetes.io/docs/concepts/workloads/controllers/replicationcontroller> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.ResourceQuotaList schema

Description
ResourceQuotaList is a list of ResourceQuota items.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ResourceQuota)`](../schedule_and_quota_apis/resourcequota-v1.md#resourcequota-v1) | Items is a list of ResourceQuota objects. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.ResourceQuotaSpec_v2 schema

Description
ResourceQuotaSpec defines the desired hard limits to enforce for Quota.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `hard` | [`object (Quantity)`](index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | hard is the set of desired hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `scopeSelector` | `ScopeSelector_v2` | scopeSelector is also a collection of filters like scopes that must match each object tracked by a quota but expressed using ScopeSelectorOperator in combination with possible values. For a resource to match, both scopes AND scopeSelector (if specified in spec), must be matched. |
| `scopes` | `array (string)` | A collection of filters that must match each object tracked by a quota. If not specified, the quota matches all objects. |

# io.k8s.api.core.v1.ResourceQuotaStatus schema

Description
ResourceQuotaStatus defines the enforced hard limits and observed use.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `hard` | [`object (Quantity)`](index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Hard is the set of enforced hard limits for each named resource. More info: <https://kubernetes.io/docs/concepts/policy/resource-quotas/> |
| `used` | [`object (Quantity)`](index.md#io-k8s-apimachinery-pkg-api-resource-Quantity) | Used is the current observed total usage of the resource in the namespace. |

# io.k8s.api.core.v1.ResourceRequirements schema

Description
ResourceRequirements describes the compute resource requirements.

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>claims</code></p></td>
<td style="text-align: left;"><p><code>array (ResourceClaim)</code></p></td>
<td style="text-align: left;"><p>Claims lists the names of resources, defined in spec.resourceClaims, that are used by this container.</p>
<p>This is an alpha field and requires enabling the DynamicResourceAllocation feature gate.</p>
<p>This field is immutable. It can only be set for containers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>limits</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Limits describes the maximum amount of compute resources allowed. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>requests</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-api-resource-Quantity"><code>object (Quantity)</code></a></p></td>
<td style="text-align: left;"><p>Requests describes the minimum amount of compute resources required. If Requests is omitted for a container, it defaults to Limits if that is explicitly specified, otherwise to an implementation-defined value. Requests cannot exceed Limits. More info: <a href="https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/">https://kubernetes.io/docs/concepts/configuration/manage-resources-containers/</a></p></td>
</tr>
</tbody>
</table>

# io.k8s.api.core.v1.Secret schema

Description
Secret holds secret data of a certain type. The total bytes of the values in the Data field must be less than MaxSecretSize bytes.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `data` | `object (string)` | Data contains the secret data. Each key must consist of alphanumeric characters, '-', '\_' or '.'. The serialized form of the secret data is a base64 encoded string, representing the arbitrary (possibly non-string) data value here. Described in <https://tools.ietf.org/html/rfc4648#section-4> |
| `immutable` | `boolean` | Immutable, if set to true, ensures that data stored in the Secret cannot be updated (only object metadata can be modified). If not set to true, the field can be modified at any time. Defaulted to nil. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ObjectMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ObjectMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |
| `stringData` | `object (string)` | stringData allows specifying non-binary secret data in string form. It is provided as a write-only input field for convenience. All keys and values are merged into the data field on write, overwriting any existing values. The stringData field is never output when reading from the API. |
| `type` | `string` | Used to facilitate programmatic handling of secret data. More info: <https://kubernetes.io/docs/concepts/configuration/secret/#secret-types> |

# io.k8s.api.core.v1.SecretList schema

Description
SecretList is a list of Secret.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Secret)`](../security_apis/secret-v1.md#secret-v1) | Items is a list of secret objects. More info: <https://kubernetes.io/docs/concepts/configuration/secret> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.SecretVolumeSource_v2 schema

Description
Adapts a Secret into a volume.

The contents of the target Secret’s Data field will be presented in a volume as files using the keys in the Data field as the file names. Secret volumes support ownership management and SELinux relabeling.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `defaultMode` | `integer` | defaultMode is Optional: mode bits used to set permissions on created files by default. Must be an octal value between 0000 and 0777 or a decimal value between 0 and 511. YAML accepts both octal and decimal values, JSON requires decimal values for mode bits. Defaults to 0644. Directories within the path are not affected by this setting. This might be in conflict with other options that affect the file mode, like fsGroup, and the result can be other mode bits set. |
| `items` | `array (KeyToPath)` | items If unspecified, each key-value pair in the Data field of the referenced Secret will be projected into the volume as a file whose name is the key and content is the value. If specified, the listed keys will be projected into the specified paths, and unlisted keys will not be present. If a key is specified which is not present in the Secret, the volume setup will error unless it is marked optional. Paths must be relative and may not contain the '..' path or start with '..'. |
| `optional` | `boolean` | optional field specify whether the Secret or its keys must be defined |
| `secretName` | `string` | secretName is the name of the secret in the pod’s namespace to use. More info: <https://kubernetes.io/docs/concepts/storage/volumes#secret> |

# io.k8s.api.core.v1.ServiceAccountList schema

Description
ServiceAccountList is a list of ServiceAccount objects

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceAccount)`](../security_apis/serviceaccount-v1.md#serviceaccount-v1) | List of ServiceAccounts. More info: <https://kubernetes.io/docs/tasks/configure-pod-container/configure-service-account/> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.ServiceList schema

Description
ServiceList holds a list of services.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Service)`](../network_apis/service-v1.md#service-v1) | List of services |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.api.core.v1.Toleration schema

Description
The pod this Toleration is attached to tolerates any taint that matches the triple \<key,value,effect\> using the matching operator \<operator\>.

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>effect</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Effect indicates the taint effect to match. Empty means match all taint effects. When specified, allowed values are NoSchedule, PreferNoSchedule and NoExecute.</p>
<p>Possible enum values: - <code>"NoExecute"</code> Evict any already-running pods that do not tolerate the taint. Currently enforced by NodeController. - <code>"NoSchedule"</code> Do not allow new pods to schedule onto the node unless they tolerate the taint, but allow all pods submitted to Kubelet without going through the scheduler to start, and allow all already-running pods to continue running. Enforced by the scheduler. - <code>"PreferNoSchedule"</code> Like TaintEffectNoSchedule, but the scheduler tries not to schedule new pods onto the node, rather than prohibiting new pods from scheduling onto the node entirely. Enforced by the scheduler.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Key is the taint key that the toleration applies to. Empty means match all taint keys. If the key is empty, operator must be Exists; this combination means to match all values and all keys.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>operator</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Operator represents a key’s relationship to the value. Valid operators are Exists and Equal. Defaults to Equal. Exists is equivalent to wildcard for value, so that a pod can tolerate all taints of a particular category.</p>
<p>Possible enum values: - <code>"Equal"</code> - <code>"Exists"</code></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tolerationSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>TolerationSeconds represents the period of time the toleration (which must be of effect NoExecute, otherwise this field is ignored) tolerates the taint. By default, it is not set, which means tolerate the taint forever (do not evict). Zero and negative values will be treated as 0 (evict immediately) by the system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>value</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Value is the taint value the toleration matches to. If the operator is Exists, the value should be empty, otherwise just a regular string.</p></td>
</tr>
</tbody>
</table>

# io.k8s.api.core.v1.TopologySelectorTerm schema

Description
A topology selector term represents the result of label queries. A null or empty topology selector term matches no objects. The requirements of them are ANDed. It provides a subset of functionality as NodeSelectorTerm. This is an alpha feature and may change in the future.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `matchLabelExpressions` | `array (TopologySelectorLabelRequirement)` | A list of topology selector requirements by labels. |

# io.k8s.api.core.v1.TypedLocalObjectReference schema

Description
TypedLocalObjectReference contains enough information to let you locate the typed referenced object inside the same namespace.

Type
`object`

Required
- `kind`

- `name`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiGroup` | `string` | APIGroup is the group for the resource being referenced. If APIGroup is not specified, the specified Kind must be in the core API group. For any other third-party types, APIGroup is required. |
| `kind` | `string` | Kind is the type of resource being referenced |
| `name` | `string` | Name is the name of resource being referenced |

# io.k8s.api.discovery.v1.EndpointSliceList schema

Description
EndpointSliceList represents a list of endpoint slices

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EndpointSlice)`](../network_apis/endpointslice-discovery-k8s-io-v1.md#endpointslice-discovery-k8s-io-v1) | items is the list of endpoint slices |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. |

# io.k8s.api.events.v1.EventList schema

Description
EventList is a list of Event objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Event)`](../metadata_apis/event-events-k8s-io-v1.md#event-events-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.flowcontrol.v1.FlowSchemaList schema

Description
FlowSchemaList is a list of FlowSchema objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FlowSchema)`](../schedule_and_quota_apis/flowschema-flowcontrol-apiserver-k8s-io-v1.md#flowschema-flowcontrol-apiserver-k8s-io-v1) | `items` is a list of FlowSchemas. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | `metadata` is the standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.flowcontrol.v1.PriorityLevelConfigurationList schema

Description
PriorityLevelConfigurationList is a list of PriorityLevelConfiguration objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PriorityLevelConfiguration)`](../schedule_and_quota_apis/prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1.md#prioritylevelconfiguration-flowcontrol-apiserver-k8s-io-v1) | `items` is a list of request-priorities. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | `metadata` is the standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.networking.v1.IngressClassList schema

Description
IngressClassList is a collection of IngressClasses.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IngressClass)`](../network_apis/ingressclass-networking-k8s-io-v1.md#ingressclass-networking-k8s-io-v1) | items is the list of IngressClasses. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. |

# io.k8s.api.networking.v1.IngressList schema

Description
IngressList is a collection of Ingress.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Ingress)`](../network_apis/ingress-networking-k8s-io-v1.md#ingress-networking-k8s-io-v1) | items is the list of Ingress. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.networking.v1.IPAddressList schema

Description
IPAddressList contains a list of IPAddress.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAddress)`](../network_apis/ipaddress-networking-k8s-io-v1.md#ipaddress-networking-k8s-io-v1) | items is the list of IPAddresses. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.networking.v1.NetworkPolicyList schema

Description
NetworkPolicyList is a list of NetworkPolicy objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NetworkPolicy)`](../network_apis/networkpolicy-networking-k8s-io-v1.md#networkpolicy-networking-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.networking.v1.ServiceCIDRList schema

Description
ServiceCIDRList contains a list of ServiceCIDR objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceCIDR)`](../network_apis/servicecidr-networking-k8s-io-v1.md#servicecidr-networking-k8s-io-v1) | items is the list of ServiceCIDRs. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.node.v1.RuntimeClassList schema

Description
RuntimeClassList is a list of RuntimeClass objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RuntimeClass)`](../node_apis/runtimeclass-node-k8s-io-v1.md#runtimeclass-node-k8s-io-v1) | items is a list of schema objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.policy.v1.PodDisruptionBudgetList schema

Description
PodDisruptionBudgetList is a collection of PodDisruptionBudgets.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodDisruptionBudget)`](../policy_apis/poddisruptionbudget-policy-v1.md#poddisruptionbudget-policy-v1) | Items is a list of PodDisruptionBudgets |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.rbac.v1.AggregationRule_v2 schema

Description
AggregationRule describes how to locate ClusterRoles to aggregate into the ClusterRole

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `clusterRoleSelectors` | `array (LabelSelector_v3)` | ClusterRoleSelectors holds a list of selectors which will be used to find ClusterRoles and create the rules. If any of the selectors match, then the ClusterRole’s permissions will be added |

# io.k8s.api.rbac.v1.ClusterRoleBindingList schema

Description
ClusterRoleBindingList is a collection of ClusterRoleBindings

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRoleBinding)`](../rbac_apis/clusterrolebinding-rbac-authorization-k8s-io-v1.md#clusterrolebinding-rbac-authorization-k8s-io-v1) | Items is a list of ClusterRoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. |

# io.k8s.api.rbac.v1.ClusterRoleList schema

Description
ClusterRoleList is a collection of ClusterRoles

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterRole)`](../rbac_apis/clusterrole-rbac-authorization-k8s-io-v1.md#clusterrole-rbac-authorization-k8s-io-v1) | Items is a list of ClusterRoles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. |

# io.k8s.api.rbac.v1.RoleBindingList schema

Description
RoleBindingList is a collection of RoleBindings

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBinding)`](../rbac_apis/rolebinding-rbac-authorization-k8s-io-v1.md#rolebinding-rbac-authorization-k8s-io-v1) | Items is a list of RoleBindings |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. |

# io.k8s.api.rbac.v1.RoleList schema

Description
RoleList is a collection of Roles

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Role)`](../rbac_apis/role-rbac-authorization-k8s-io-v1.md#role-rbac-authorization-k8s-io-v1) | Items is a list of Roles |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata. |

# io.k8s.api.scheduling.v1.PriorityClassList schema

Description
PriorityClassList is a collection of priority classes.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PriorityClass)`](../schedule_and_quota_apis/priorityclass-scheduling-k8s-io-v1.md#priorityclass-scheduling-k8s-io-v1) | items is the list of PriorityClasses |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.storage.v1.CSIDriverList schema

Description
CSIDriverList is a collection of CSIDriver objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSIDriver)`](../storage_apis/csidriver-storage-k8s-io-v1.md#csidriver-storage-k8s-io-v1) | items is the list of CSIDriver |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.storage.v1.CSINodeList schema

Description
CSINodeList is a collection of CSINode objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSINode)`](../storage_apis/csinode-storage-k8s-io-v1.md#csinode-storage-k8s-io-v1) | items is the list of CSINode |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.storage.v1.CSIStorageCapacityList schema

Description
CSIStorageCapacityList is a collection of CSIStorageCapacity objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSIStorageCapacity)`](../storage_apis/csistoragecapacity-storage-k8s-io-v1.md#csistoragecapacity-storage-k8s-io-v1) | items is the list of CSIStorageCapacity objects. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.storage.v1.StorageClassList schema

Description
StorageClassList is a collection of storage classes.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageClass)`](../storage_apis/storageclass-storage-k8s-io-v1.md#storageclass-storage-k8s-io-v1) | items is the list of StorageClasses |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.api.storage.v1.VolumeAttachmentList schema

Description
VolumeAttachmentList is a collection of VolumeAttachment objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeAttachment)`](../storage_apis/volumeattachment-storage-k8s-io-v1.md#volumeattachment-storage-k8s-io-v1) | items is the list of VolumeAttachments |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.CustomResourceDefinitionList schema

Description
CustomResourceDefinitionList is a list of CustomResourceDefinition objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CustomResourceDefinition)`](../extension_apis/customresourcedefinition-apiextensions-k8s-io-v1.md#customresourcedefinition-apiextensions-k8s-io-v1) | items list individual CustomResourceDefinition objects |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard object’s metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.apiextensions-apiserver.pkg.apis.apiextensions.v1.JSONSchemaProps schema

Description
JSONSchemaProps is a JSON-Schema following Specification Draft 4 (<http://json-schema.org/>).

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>$ref</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>$schema</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalItems</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>additionalProperties</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>allOf</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>array (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>anyOf</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>array (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>default</code></p></td>
<td style="text-align: left;"><p><code>JSON</code></p></td>
<td style="text-align: left;"><p>default is a default value for undefined object fields. Defaulting is a beta feature under the CustomResourceDefaulting feature gate. Defaulting requires spec.preserveUnknownFields to be false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>definitions</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>object (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>dependencies</code></p></td>
<td style="text-align: left;"><p><code>object (undefined)</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>description</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>enum</code></p></td>
<td style="text-align: left;"><p><code>array (JSON)</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>example</code></p></td>
<td style="text-align: left;"><p><code>JSON</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exclusiveMaximum</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>exclusiveMinimum</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>externalDocs</code></p></td>
<td style="text-align: left;"><p><code>ExternalDocumentation</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>format</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>format is an OpenAPI v3 format string. Unknown formats are ignored. The following formats are validated:</p>
<p>- bsonobjectid: a bson object ID, i.e. a 24 characters hex string - uri: an URI as parsed by Golang net/url.ParseRequestURI - email: an email address as parsed by Golang net/mail.ParseAddress - hostname: a valid representation for an Internet host name, as defined by RFC 1034, section 3.1 [RFC1034]. - ipv4: an IPv4 IP as parsed by Golang net.ParseIP - ipv6: an IPv6 IP as parsed by Golang net.ParseIP - cidr: a CIDR as parsed by Golang net.ParseCIDR - mac: a MAC address as parsed by Golang net.ParseMAC - uuid: an UUID that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid3: an UUID3 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?3[0-9a-f]{3}-?[0-9a-f]{4}-?[0-9a-f]{12}$ - uuid4: an UUID4 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?4[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - uuid5: an UUID5 that allows uppercase defined by the regex (?i)^[0-9a-f]{8}-?[0-9a-f]{4}-?5[0-9a-f]{3}-?[89ab][0-9a-f]{3}-?[0-9a-f]{12}$ - isbn: an ISBN10 or ISBN13 number string like "0321751043" or "978-0321751041" - isbn10: an ISBN10 number string like "0321751043" - isbn13: an ISBN13 number string like "978-0321751041" - creditcard: a credit card number defined by the regex ^(?:4[0-9]{12}(?:[0-9]{3})?|5[1-5][0-9]{14}|6(?:011|5[0-9][0-9])[0-9]{12}|3[47][0-9]{13}|3(?:0[0-5]|[68][0-9])[0-9]{11}|(?:2131|1800|35\\d{3})\\d{11})$ with any non digit characters mixed in - ssn: a U.S. social security number following the regex ^\\d{3}[- ]?\\d{2}[- ]?\\d{4}$ - hexcolor: an hexadecimal color code like "<em>FFFFFF: following the regex ^</em>?([0-9a-fA-F]{3}|[0-9a-fA-F]{6})$ - rgbcolor: an RGB color code like rgb like "rgb(255,255,2559" - byte: base64 encoded binary data - password: any kind of string - date: a date string like "2006-01-02" as defined by full-date in RFC3339 - duration: a duration string like "22 ns" as parsed by Golang time.ParseDuration or compatible with Scala duration format - datetime: a date time string like "2014-12-15T19:30:20.000Z" as defined by date-time in RFC3339.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>id</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>items</code></p></td>
<td style="text-align: left;"><p>``</p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxItems</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxLength</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maxProperties</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>maximum</code></p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minItems</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minLength</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minProperties</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>minimum</code></p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>multipleOf</code></p></td>
<td style="text-align: left;"><p><code>number</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>not</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps">``</a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>nullable</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>oneOf</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>array (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>pattern</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>patternProperties</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>object (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>properties</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apiextensions-apiserver-pkg-apis-apiextensions-v1-JSONSchemaProps"><code>object (undefined)</code></a></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>required</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>title</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uniqueItems</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-embedded-resource</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-embedded-resource defines that the value is an embedded Kubernetes runtime.Object, with TypeMeta and ObjectMeta. The type must be object. It is allowed to further restrict the embedded object. kind, apiVersion and metadata are validated automatically. x-kubernetes-preserve-unknown-fields is allowed to be true, but does not have to be if the object is fully specified (up to kind, apiVersion, metadata).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-int-or-string</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-int-or-string specifies that this value is either an integer or a string. If this is true, an empty type is allowed and type as child of anyOf is permitted if following one of the following patterns:</p>
<p>1) anyOf: - type: integer - type: string 2) allOf: - anyOf: - type: integer - type: string - …​ zero or more</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-list-map-keys</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-list-map-keys annotates an array with the x-kubernetes-list-type <code>map</code> by specifying the keys used as the index of the map.</p>
<p>This tag MUST only be used on lists that have the "x-kubernetes-list-type" extension set to "map". Also, the values specified for this attribute must be a scalar typed field of the child structure (no nesting is supported).</p>
<p>The properties specified must either be required or have a default value, to ensure those properties are present for all list items.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-list-type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-list-type annotates an array to further describe its topology. This extension must only be used on lists and may have 3 possible values:</p>
<p>1) <code>atomic</code>: the list is treated as a single entity, like a scalar. Atomic lists will be entirely replaced when updated. This extension may be used on any type of list (struct, scalar, …​). 2) <code>set</code>: Sets are lists that must not have multiple items with the same value. Each value must be a scalar, an object with x-kubernetes-map-type <code>atomic</code> or an array with x-kubernetes-list-type <code>atomic</code>. 3) <code>map</code>: These lists are like maps in that their elements have a non-index key used to identify them. Order is preserved upon merge. The map tag must only be used on a list with elements of type object. Defaults to atomic for arrays.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-map-type</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-map-type annotates an object to further describe its topology. This extension must only be used when type is object and may have 2 possible values:</p>
<p>1) <code>granular</code>: These maps are actual maps (key-value pairs) and each fields are independent from each other (they can each be manipulated by separate actors). This is the default behaviour for all maps. 2) <code>atomic</code>: the list is treated as a single entity, like a scalar. Atomic maps will be entirely replaced when updated.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-preserve-unknown-fields</code></p></td>
<td style="text-align: left;"><p><code>boolean</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-preserve-unknown-fields stops the API server decoding step from pruning fields which are not specified in the validation schema. This affects fields recursively, but switches back to normal pruning behaviour if nested properties or additionalProperties are specified in the schema. This can either be true or undefined. False is forbidden.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>x-kubernetes-validations</code></p></td>
<td style="text-align: left;"><p><code>array (ValidationRule)</code></p></td>
<td style="text-align: left;"><p>x-kubernetes-validations describes a list of validation rules written in the CEL expression language.</p></td>
</tr>
</tbody>
</table>

# io.k8s.apimachinery.pkg.api.resource.Quantity schema

Description
Quantity is a fixed-point representation of a number. It provides convenient marshaling/unmarshaling in JSON and YAML, in addition to String() and AsInt64() accessors.

The serialization format is:

    <quantity>        ::= <signedNumber><suffix>

    (Note that <suffix> may be empty, from the "" case in <decimalSI>.)

\<digit\> ::= 0 \\ 1 \\ …​ \\ 9 \<digits\> ::= \<digit\> \\ \<digit\>\<digits\> \<number\> ::= \<digits\> \\ \<digits\>.\<digits\> \\ \<digits\>. \\ .\<digits\> \<sign\> ::= "+" \\ "-" \<signedNumber\> ::= \<number\> \\ \<sign\>\<number\> \<suffix\> ::= \<binarySI\> \\ \<decimalExponent\> \\ \<decimalSI\> \<binarySI\> ::= Ki \\ Mi \\ Gi \\ Ti \\ Pi \\ Ei

    (International System of units; See: http://physics.nist.gov/cuu/Units/binary.html)

\<decimalSI\> ::= m \\ "" \\ k \\ M \\ G \\ T \\ P \\ E

    (Note that 1024 = 1Ki but 1000 = 1k; I didn't choose the capitalization.)

\<decimalExponent\> ::= "e" \<signedNumber\> \\ "E" \<signedNumber\>

No matter which of the three exponent forms is used, no quantity may represent a number greater than 2^63-1 in magnitude, nor may it have more than 3 decimal places. Numbers larger or more precise will be capped or rounded up. (E.g.: 0.1m will rounded up to 1m.) This may be extended in the future if we require larger or smaller quantities.

When a Quantity is parsed from a string, it will remember the type of suffix it had, and will use the same type again when it is serialized.

Before serializing, Quantity will be put in "canonical form". This means that Exponent/suffix will be adjusted up or down (with a corresponding increase or decrease in Mantissa) such that:

- No precision is lost - No fractional digits will be emitted - The exponent (or suffix) is as large as possible.

The sign will be omitted unless the number is negative.

Examples:

- 1.5 will be serialized as "1500m" - 1.5Gi will be serialized as "1536Mi"

Note that the quantity will NEVER be internally represented by a floating point number. That is the whole point of this exercise.

Non-canonical values will still parse as long as they are well formed, but will be re-emitted in their canonical form. (So always use canonical form, or don’t diff.)

This format is intended to make it difficult to use these numbers without writing some sort of special handling code in the hopes that that will cause implementors to also use a fixed point implementation.

Type
`string`

# io.k8s.apimachinery.pkg.apis.meta.v1.Condition schema

Description
Condition contains details for one aspect of the current state of this API Resource.

Type
`object`

Required
- `type`

- `status`

- `lastTransitionTime`

- `reason`

- `message`

## Schema

| Property | Type | Description |
|----|----|----|
| `lastTransitionTime` | [`Time`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-Time) | lastTransitionTime is the last time the condition transitioned from one status to another. This should be when the underlying condition changed. If that is not known, then using the time when the API field changed is acceptable. |
| `message` | `string` | message is a human readable message indicating details about the transition. This may be an empty string. |
| `observedGeneration` | `integer` | observedGeneration represents the .metadata.generation that the condition was set based upon. For instance, if .metadata.generation is currently 12, but the .status.conditions\[x\].observedGeneration is 9, the condition is out of date with respect to the current state of the instance. |
| `reason` | `string` | reason contains a programmatic identifier indicating the reason for the condition’s last transition. Producers of specific condition types may define expected values and meanings for this field, and whether the values are considered a guaranteed API. The value should be a CamelCase string. This field may not be empty. |
| `status` | `string` | status of the condition, one of True, False, Unknown. |
| `type` | `string` | type of condition in CamelCase or in foo.example.com/CamelCase. |

# io.k8s.apimachinery.pkg.apis.meta.v1.DeleteOptions schema

Description
DeleteOptions may be provided when deleting an API object.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `dryRun` | `array (string)` | When present, indicates that modifications should not be persisted. An invalid or unrecognized dryRun directive will result in an error response and no further processing of the request. Valid values are: - All: all dry run stages will be processed |
| `gracePeriodSeconds` | `integer` | The duration in seconds before the object should be deleted. Value must be non-negative integer. The value zero indicates delete immediately. If this value is nil, the default grace period for the specified type will be used. Defaults to a per object value if not specified. zero means delete immediately. |
| `ignoreStoreReadErrorWithClusterBreakingPotential` | `boolean` | if set to true, it will trigger an unsafe deletion of the resource in case the normal deletion flow fails with a corrupt object error. A resource is considered corrupt if it can not be retrieved from the underlying storage successfully because of a) its data can not be transformed e.g. decryption failure, or b) it fails to decode into an object. NOTE: unsafe deletion ignores finalizer constraints, skips precondition checks, and removes the object from the storage. WARNING: This may potentially break the cluster if the workload associated with the resource being unsafe-deleted relies on normal deletion flow. Use only if you REALLY know what you are doing. The default value is false, and the user must opt in to enable it |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `orphanDependents` | `boolean` | Deprecated: please use the PropagationPolicy, this field will be deprecated in 1.7. Should the dependent objects be orphaned. If true/false, the "orphan" finalizer will be added to/removed from the object’s finalizers list. Either this field or PropagationPolicy may be set, but not both. |
| `preconditions` | `Preconditions` | Must be fulfilled before a deletion is carried out. If not possible, a 409 Conflict status will be returned. |
| `propagationPolicy` | `string` | Whether and how garbage collection will be performed. Either this field or OrphanDependents may be set, but not both. The default policy is decided by the existing finalizer set in the metadata.finalizers and the resource-specific default policy. Acceptable values are: 'Orphan' - orphan the dependents; 'Background' - allow the garbage collector to delete the dependents in the background; 'Foreground' - a cascading policy that deletes all dependents in the foreground. |

# io.k8s.apimachinery.pkg.apis.meta.v1.Duration schema

Description
Duration is a wrapper around time.Duration which supports correct marshaling to YAML and JSON. In particular, it marshals into strings, which can be used as map keys in json.

Type
`string`

# io.k8s.apimachinery.pkg.apis.meta.v1.FieldSelectorRequirement schema

Description
FieldSelectorRequirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

## Schema

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the field selector key that the requirement applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists, DoesNotExist. The list of operators may grow in the future. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. |

# io.k8s.apimachinery.pkg.apis.meta.v1.GroupVersionKind schema

Description
GroupVersionKind unambiguously identifies a kind. It doesn’t anonymously include GroupVersion to avoid automatic coercion. It doesn’t use a GroupVersion to avoid custom marshalling

Type
`object`

Required
- `group`

- `version`

- `kind`

## Schema

| Property  | Type     | Description |
|-----------|----------|-------------|
| `group`   | `string` |             |
| `kind`    | `string` |             |
| `version` | `string` |             |

# io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector schema

Description
A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | [`array (LabelSelectorRequirement)`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-LabelSelectorRequirement) | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

# io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelector_v4 schema

Description
A label selector is a label query over a set of resources. The result of matchLabels and matchExpressions are ANDed. An empty label selector matches all objects. A null label selector matches no objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `matchExpressions` | `array (LabelSelectorRequirement_v2)` | matchExpressions is a list of label selector requirements. The requirements are ANDed. |
| `matchLabels` | `object (string)` | matchLabels is a map of {key,value} pairs. A single {key,value} in the matchLabels map is equivalent to an element of matchExpressions, whose key field is "key", the operator is "In", and the values array contains only "value". The requirements are ANDed. |

# io.k8s.apimachinery.pkg.apis.meta.v1.LabelSelectorRequirement schema

Description
A label selector requirement is a selector that contains values, a key, and an operator that relates the key and values.

Type
`object`

Required
- `key`

- `operator`

## Schema

| Property | Type | Description |
|----|----|----|
| `key` | `string` | key is the label key that the selector applies to. |
| `operator` | `string` | operator represents a key’s relationship to a set of values. Valid operators are In, NotIn, Exists and DoesNotExist. |
| `values` | `array (string)` | values is an array of string values. If the operator is In or NotIn, the values array must be non-empty. If the operator is Exists or DoesNotExist, the values array must be empty. This array is replaced during a strategic merge patch. |

# io.k8s.apimachinery.pkg.apis.meta.v1.ListMeta schema

Description
ListMeta describes metadata that synthetic resources must have, including lists and various status objects. A resource may have only one of {ObjectMeta, ListMeta}.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `continue` | `string` | continue may be set if the user set a limit on the number of items returned, and indicates that the server has more data available. The value is opaque and may be used to issue another request to the endpoint that served this list to retrieve the next set of available objects. Continuing a consistent list may not be possible if the server configuration has changed or more than a few minutes have passed. The resourceVersion field returned when using this continue value will be identical to the value in the first response, unless you have received this token from an error message. |
| `remainingItemCount` | `integer` | remainingItemCount is the number of subsequent items in the list which are not included in this list response. If the list request contained label or field selectors, then the number of remaining items is unknown and the field will be left unset and omitted during serialization. If the list is complete (either because it is not chunking or because this is the last chunk), then there are no more remaining items and this field will be left unset and omitted during serialization. Servers older than v1.15 do not set this field. The intended use of the remainingItemCount is **estimating** the size of a collection. Clients should not rely on the remainingItemCount to be set or to be exact. |
| `resourceVersion` | `string` | String that identifies the server’s internal version of this object that can be used by clients to determine when objects have changed. Value must be treated as opaque by clients and passed unmodified back to the server. Populated by the system. Read-only. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency> |
| `selfLink` | `string` | Deprecated: selfLink is a legacy read-only field that is no longer populated by the system. |

# io.k8s.apimachinery.pkg.apis.meta.v1.MicroTime schema

Description
MicroTime is version of Time with microsecond level precision.

Type
`string`

# io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta schema

Description
ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations">https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>creationTimestamp</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.</p>
<p>Populated by the system. Read-only. Null for lists. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deletionGracePeriodSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deletionTimestamp</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.</p>
<p>Populated by the system when a graceful deletion is requested. Read-only. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>finalizers</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.</p>
<p>If this field is specified and the generated name exists, the server will return a 409.</p>
<p>Applied only if Name is not specified. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generation</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels">https://kubernetes.io/docs/concepts/overview/working-with-objects/labels</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedFields</code></p></td>
<td style="text-align: left;"><p><code>array (ManagedFieldsEntry)</code></p></td>
<td style="text-align: left;"><p>ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn’t need to set or understand this field. A workflow can be the user’s name, a controller’s name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names">https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.</p>
<p>Must be a DNS_LABEL. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces">https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences</code></p></td>
<td style="text-align: left;"><p><code>array (OwnerReference)</code></p></td>
<td style="text-align: left;"><p>List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.</p>
<p>Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selfLink</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uid</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.</p>
<p>Populated by the system. Read-only. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids">https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids</a></p></td>
</tr>
</tbody>
</table>

# io.k8s.apimachinery.pkg.apis.meta.v1.ObjectMeta_v2 schema

Description
ObjectMeta is metadata that all persisted resources must have, which includes all objects users must create.

Type
`object`

## Schema

<table>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Property</th>
<th style="text-align: left;">Type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>annotations</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Annotations is an unstructured key value map stored with a resource that may be set by external tools to store and retrieve arbitrary metadata. They are not queryable and should be preserved when modifying objects. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations">https://kubernetes.io/docs/concepts/overview/working-with-objects/annotations</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>creationTimestamp</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>CreationTimestamp is a timestamp representing the server time when this object was created. It is not guaranteed to be set in happens-before order across separate operations. Clients may not set this value. It is represented in RFC3339 form and is in UTC.</p>
<p>Populated by the system. Read-only. Null for lists. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deletionGracePeriodSeconds</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Number of seconds allowed for this object to gracefully terminate before it will be removed from the system. Only set when deletionTimestamp is also set. May only be shortened. Read-only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>deletionTimestamp</code></p></td>
<td style="text-align: left;"><p><a href="../objects/index.xml#io-k8s-apimachinery-pkg-apis-meta-v1-Time"><code>Time</code></a></p></td>
<td style="text-align: left;"><p>DeletionTimestamp is RFC 3339 date and time at which this resource will be deleted. This field is set by the server when a graceful deletion is requested by the user, and is not directly settable by a client. The resource is expected to be deleted (no longer visible from resource lists, and not reachable by name) after the time in this field, once the finalizers list is empty. As long as the finalizers list contains items, deletion is blocked. Once the deletionTimestamp is set, this value may not be unset or be set further into the future, although it may be shortened or the resource may be deleted prior to this time. For example, a user may request that a pod is deleted in 30 seconds. The Kubelet will react by sending a graceful termination signal to the containers in the pod. After that 30 seconds, the Kubelet will send a hard termination signal (SIGKILL) to the container and after cleanup, remove the pod from the API. In the presence of network partitions, this object may still exist after this timestamp, until an administrator or automated process can determine the resource is fully terminated. If not set, graceful deletion of the object has not been requested.</p>
<p>Populated by the system when a graceful deletion is requested. Read-only. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>finalizers</code></p></td>
<td style="text-align: left;"><p><code>array (string)</code></p></td>
<td style="text-align: left;"><p>Must be empty before the object is deleted from the registry. Each entry is an identifier for the responsible component that will remove the entry from the list. If the deletionTimestamp of the object is non-nil, entries in this list can only be removed. Finalizers may be processed and removed in any order. Order is NOT enforced because it introduces significant risk of stuck finalizers. finalizers is a shared field, any actor with permission can reorder it. If the finalizer list is processed in order, then this can lead to a situation in which the component responsible for the first finalizer in the list is waiting for a signal (field value, external system, or other) produced by a component responsible for a finalizer later in the list, resulting in a deadlock. Without enforced ordering finalizers are free to order amongst themselves and are not vulnerable to ordering changes in the list.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generateName</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>GenerateName is an optional prefix, used by the server, to generate a unique name ONLY IF the Name field has not been provided. If this field is used, the name returned to the client will be different than the name passed. This value will also be combined with a unique suffix. The provided value has the same validation rules as the Name field, and may be truncated by the length of the suffix required to make the value unique on the server.</p>
<p>If this field is specified and the generated name exists, the server will return a 409.</p>
<p>Applied only if Name is not specified. More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#idempotency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>generation</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>A sequence number representing a specific generation of the desired state. Populated by the system. Read-only.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>labels</code></p></td>
<td style="text-align: left;"><p><code>object (string)</code></p></td>
<td style="text-align: left;"><p>Map of string keys and values that can be used to organize and categorize (scope and select) objects. May match selectors of replication controllers and services. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/labels">https://kubernetes.io/docs/concepts/overview/working-with-objects/labels</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>managedFields</code></p></td>
<td style="text-align: left;"><p><code>array (ManagedFieldsEntry)</code></p></td>
<td style="text-align: left;"><p>ManagedFields maps workflow-id and version to the set of fields that are managed by that workflow. This is mostly for internal housekeeping, and users typically shouldn’t need to set or understand this field. A workflow can be the user’s name, a controller’s name, or the name of a specific apply path like "ci-cd". The set of fields is always in the version that the workflow used when modifying the object.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name must be unique within a namespace. Is required when creating resources, although some resources may allow a client to request the generation of an appropriate name automatically. Name is primarily intended for creation idempotence and configuration definition. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names">https://kubernetes.io/docs/concepts/overview/working-with-objects/names#names</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace defines the space within which each name must be unique. An empty namespace is equivalent to the "default" namespace, but "default" is the canonical representation. Not all objects are required to be scoped to a namespace - the value of this field for those objects will be empty.</p>
<p>Must be a DNS_LABEL. Cannot be updated. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces">https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ownerReferences</code></p></td>
<td style="text-align: left;"><p><code>array (OwnerReference)</code></p></td>
<td style="text-align: left;"><p>List of objects depended by this object. If ALL objects in the list have been deleted, this object will be garbage collected. If this object is managed by a controller, then an entry in this list will point to this controller, with the controller field set to true. There cannot be more than one managing controller.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>resourceVersion</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>An opaque value that represents the internal version of this object that can be used by clients to determine when objects have changed. May be used for optimistic concurrency, change detection, and the watch operation on a resource or set of resources. Clients must treat these values as opaque and passed unmodified back to the server. They may only be valid for a particular resource or set of resources.</p>
<p>Populated by the system. Read-only. Value must be treated as opaque by clients and . More info: <a href="https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency">https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#concurrency-control-and-consistency</a></p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>selfLink</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Deprecated: selfLink is a legacy read-only field that is no longer populated by the system.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>uid</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>UID is the unique in time and space value for this object. It is typically generated by the server on successful creation of a resource and is not allowed to change on PUT operations.</p>
<p>Populated by the system. Read-only. More info: <a href="https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids">https://kubernetes.io/docs/concepts/overview/working-with-objects/names#uids</a></p></td>
</tr>
</tbody>
</table>

# io.k8s.apimachinery.pkg.apis.meta.v1.Status schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v2 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v3 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v4 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v5 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v6 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v7 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v8 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Status_v9 schema

Description
Status is a return value for calls that don’t return other objects.

Type
`object`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `code` | `integer` | Suggested HTTP return code for this status, 0 if not set. |
| `details` | `StatusDetails_v2` | Extended data associated with the reason. Each reason may define its own extended details. This field is optional and the data returned is not guaranteed to conform to any schema except that defined by the reason type. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `message` | `string` | A human-readable description of the status of this operation. |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `reason` | `string` | A machine-readable description of why this operation is in the "Failure" status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |
| `status` | `string` | Status of the operation. One of: "Success" or "Failure". More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#spec-and-status> |

# io.k8s.apimachinery.pkg.apis.meta.v1.Time schema

Description
Time is a wrapper around time.Time which supports correct marshaling to YAML and JSON. Wrappers are provided for many of the factory methods that the time package offers.

Type
`string`

# io.k8s.apimachinery.pkg.apis.meta.v1.WatchEvent schema

Description
Event represents a single event to a watched resource.

Type
`object`

Required
- `type`

- `object`

## Schema

| Property | Type | Description |
|----|----|----|
| `object` | [`RawExtension`](index.md#io-k8s-apimachinery-pkg-runtime-RawExtension) | Object is: \* If Type is Added or Modified: the new state of the object. \* If Type is Deleted: the state of the object immediately before deletion. \* If Type is Error: \*Status is recommended; other types may make sense depending on context. |
| `type` | `string` |  |

# io.k8s.apimachinery.pkg.runtime.RawExtension schema

Description
RawExtension is used to hold extensions in external versions.

To use this, make a field which has RawExtension as its type in your external, versioned struct, and Object in your internal struct. You also need to register your various plugin types.

    type MyAPIObject struct {
        runtime.TypeMeta `json:",inline"`
        MyPlugin runtime.Object `json:"myPlugin"`
    }

    type PluginA struct {
        AOption string `json:"aOption"`
    }

    type MyAPIObject struct {
        runtime.TypeMeta `json:",inline"`
        MyPlugin runtime.RawExtension `json:"myPlugin"`
    }

    type PluginA struct {
        AOption string `json:"aOption"`
    }

    {
        "kind":"MyAPIObject",
        "apiVersion":"v1",
        "myPlugin": {
            "kind":"PluginA",
            "aOption":"foo",
        },
    }

So what happens? Decode first uses json or yaml to unmarshal the serialized data into your external MyAPIObject. That causes the raw JSON to be stored, but not unpacked. The next step is to copy (using pkg/conversion) into the internal struct. The runtime package’s DefaultScheme has conversion functions installed which will unpack the JSON stored in RawExtension, turning it into the correct object type, and storing it in the Object. (TODO: In the case where the object is of an unknown type, a runtime.Unknown object will be created and stored.)

Type
`object`

# io.k8s.apimachinery.pkg.util.intstr.IntOrString schema

Description
IntOrString is a type that can hold an int32 or a string. When used in JSON or YAML marshalling and unmarshalling, it produces or consumes the inner type. This allows you to have, for example, a JSON field that can accept a name or number.

Type
`string`

# io.k8s.kube-aggregator.pkg.apis.apiregistration.v1.APIServiceList schema

Description
APIServiceList is a list of APIService objects.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIService)`](../extension_apis/apiservice-apiregistration-k8s-io-v1.md#apiservice-apiregistration-k8s-io-v1) | Items is the list of APIService |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#metadata> |

# io.k8s.metrics.pkg.apis.metrics.v1beta1.NodeMetricsList schema

Description
NodeMetricsList is a list of NodeMetrics.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (NodeMetrics)`](../monitoring_apis/nodemetrics-metrics-k8s-io-v1beta1.md#nodemetrics-metrics-k8s-io-v1beta1) | List of node metrics. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.metrics.pkg.apis.metrics.v1beta1.PodMetricsList schema

Description
PodMetricsList is a list of PodMetrics.

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodMetrics)`](../monitoring_apis/podmetrics-metrics-k8s-io-v1beta1.md#podmetrics-metrics-k8s-io-v1beta1) | List of pod metrics. |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.migration.v1alpha1.StorageStateList schema

Description
StorageStateList is a list of StorageState

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageState)`](../storage_apis/storagestate-migration-k8s-io-v1alpha1.md#storagestate-migration-k8s-io-v1alpha1) | List of storagestates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.migration.v1alpha1.StorageVersionMigrationList schema

Description
StorageVersionMigrationList is a list of StorageVersionMigration

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (StorageVersionMigration)`](../storage_apis/storageversionmigration-migration-k8s-io-v1alpha1.md#storageversionmigration-migration-k8s-io-v1alpha1) | List of storageversionmigrations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.gateway.v1.GatewayClassList schema

Description
GatewayClassList is a list of GatewayClass

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (GatewayClass)`](../network_apis/gatewayclass-gateway-networking-k8s-io-v1.md#gatewayclass-gateway-networking-k8s-io-v1) | List of gatewayclasses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.gateway.v1.GatewayList schema

Description
GatewayList is a list of Gateway

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Gateway)`](../network_apis/gateway-gateway-networking-k8s-io-v1.md#gateway-gateway-networking-k8s-io-v1) | List of gateways. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.gateway.v1.GRPCRouteList schema

Description
GRPCRouteList is a list of GRPCRoute

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (GRPCRoute)`](../network_apis/grpcroute-gateway-networking-k8s-io-v1.md#grpcroute-gateway-networking-k8s-io-v1) | List of grpcroutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.gateway.v1.HTTPRouteList schema

Description
HTTPRouteList is a list of HTTPRoute

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HTTPRoute)`](../network_apis/httproute-gateway-networking-k8s-io-v1.md#httproute-gateway-networking-k8s-io-v1) | List of httproutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.gateway.v1beta1.ReferenceGrantList schema

Description
ReferenceGrantList is a list of ReferenceGrant

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ReferenceGrant)`](../network_apis/referencegrant-gateway-networking-k8s-io-v1beta1.md#referencegrant-gateway-networking-k8s-io-v1beta1) | List of referencegrants. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.policy.v1alpha1.AdminNetworkPolicyList schema

Description
AdminNetworkPolicyList is a list of AdminNetworkPolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AdminNetworkPolicy)`](../network_apis/adminnetworkpolicy-policy-networking-k8s-io-v1alpha1.md#adminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | List of adminnetworkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.networking.policy.v1alpha1.BaselineAdminNetworkPolicyList schema

Description
BaselineAdminNetworkPolicyList is a list of BaselineAdminNetworkPolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BaselineAdminNetworkPolicy)`](../network_apis/baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1.md#baselineadminnetworkpolicy-policy-networking-k8s-io-v1alpha1) | List of baselineadminnetworkpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.storage.populator.v1beta1.VolumePopulatorList schema

Description
VolumePopulatorList is a list of VolumePopulator

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumePopulator)`](../storage_apis/volumepopulator-populator-storage-k8s-io-v1beta1.md#volumepopulator-populator-storage-k8s-io-v1beta1) | List of volumepopulators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.storage.snapshot.v1.VolumeSnapshotClassList schema

Description
VolumeSnapshotClassList is a list of VolumeSnapshotClass

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshotClass)`](../storage_apis/volumesnapshotclass-snapshot-storage-k8s-io-v1.md#volumesnapshotclass-snapshot-storage-k8s-io-v1) | List of volumesnapshotclasses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.storage.snapshot.v1.VolumeSnapshotContentList schema

Description
VolumeSnapshotContentList is a list of VolumeSnapshotContent

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshotContent)`](../storage_apis/volumesnapshotcontent-snapshot-storage-k8s-io-v1.md#volumesnapshotcontent-snapshot-storage-k8s-io-v1) | List of volumesnapshotcontents. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.k8s.storage.snapshot.v1.VolumeSnapshotList schema

Description
VolumeSnapshotList is a list of VolumeSnapshot

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (VolumeSnapshot)`](../storage_apis/volumesnapshot-snapshot-storage-k8s-io-v1.md#volumesnapshot-snapshot-storage-k8s-io-v1) | List of volumesnapshots. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.BareMetalHostList schema

Description
BareMetalHostList is a list of BareMetalHost

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BareMetalHost)`](../provisioning_apis/baremetalhost-metal3-io-v1alpha1.md#baremetalhost-metal3-io-v1alpha1) | List of baremetalhosts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.BMCEventSubscriptionList schema

Description
BMCEventSubscriptionList is a list of BMCEventSubscription

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (BMCEventSubscription)`](../provisioning_apis/bmceventsubscription-metal3-io-v1alpha1.md#bmceventsubscription-metal3-io-v1alpha1) | List of bmceventsubscriptions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.DataImageList schema

Description
DataImageList is a list of DataImage

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DataImage)`](../provisioning_apis/dataimage-metal3-io-v1alpha1.md#dataimage-metal3-io-v1alpha1) | List of dataimages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.FirmwareSchemaList schema

Description
FirmwareSchemaList is a list of FirmwareSchema

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FirmwareSchema)`](../provisioning_apis/firmwareschema-metal3-io-v1alpha1.md#firmwareschema-metal3-io-v1alpha1) | List of firmwareschemas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.HardwareDataList schema

Description
HardwareDataList is a list of HardwareData

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HardwareData)`](../provisioning_apis/hardwaredata-metal3-io-v1alpha1.md#hardwaredata-metal3-io-v1alpha1) | List of hardwaredata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.HostFirmwareComponentsList schema

Description
HostFirmwareComponentsList is a list of HostFirmwareComponents

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostFirmwareComponents)`](../provisioning_apis/hostfirmwarecomponents-metal3-io-v1alpha1.md#hostfirmwarecomponents-metal3-io-v1alpha1) | List of hostfirmwarecomponents. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.HostFirmwareSettingsList schema

Description
HostFirmwareSettingsList is a list of HostFirmwareSettings

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostFirmwareSettings)`](../provisioning_apis/hostfirmwaresettings-metal3-io-v1alpha1.md#hostfirmwaresettings-metal3-io-v1alpha1) | List of hostfirmwaresettings. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.HostUpdatePolicyList schema

Description
HostUpdatePolicyList is a list of HostUpdatePolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HostUpdatePolicy)`](../provisioning_apis/hostupdatepolicy-metal3-io-v1alpha1.md#hostupdatepolicy-metal3-io-v1alpha1) | List of hostupdatepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.PreprovisioningImageList schema

Description
PreprovisioningImageList is a list of PreprovisioningImage

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PreprovisioningImage)`](../provisioning_apis/preprovisioningimage-metal3-io-v1alpha1.md#preprovisioningimage-metal3-io-v1alpha1) | List of preprovisioningimages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.metal3.v1alpha1.ProvisioningList schema

Description
ProvisioningList is a list of Provisioning

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Provisioning)`](../provisioning_apis/provisioning-metal3-io-v1alpha1.md#provisioning-metal3-io-v1alpha1) | List of provisionings. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.apiserver.v1.APIRequestCountList schema

Description
APIRequestCountList is a list of APIRequestCount

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIRequestCount)`](../metadata_apis/apirequestcount-apiserver-openshift-io-v1.md#apirequestcount-apiserver-openshift-io-v1) | List of apirequestcounts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.authorization.v1.RoleBindingRestrictionList schema

Description
RoleBindingRestrictionList is a list of RoleBindingRestriction

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (RoleBindingRestriction)`](../role_apis/rolebindingrestriction-authorization-openshift-io-v1.md#rolebindingrestriction-authorization-openshift-io-v1) | List of rolebindingrestrictions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.autoscaling.v1.ClusterAutoscalerList schema

Description
ClusterAutoscalerList is a list of ClusterAutoscaler

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterAutoscaler)`](../autoscale_apis/clusterautoscaler-autoscaling-openshift-io-v1.md#clusterautoscaler-autoscaling-openshift-io-v1) | List of clusterautoscalers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.autoscaling.v1beta1.MachineAutoscalerList schema

Description
MachineAutoscalerList is a list of MachineAutoscaler

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineAutoscaler)`](../autoscale_apis/machineautoscaler-autoscaling-openshift-io-v1beta1.md#machineautoscaler-autoscaling-openshift-io-v1beta1) | List of machineautoscalers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.cloudcredential.v1.CredentialsRequestList schema

Description
CredentialsRequestList is a list of CredentialsRequest

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CredentialsRequest)`](../security_apis/credentialsrequest-cloudcredential-openshift-io-v1.md#credentialsrequest-cloudcredential-openshift-io-v1) | List of credentialsrequests. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.APIServerList schema

Description
APIServerList is a list of APIServer

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (APIServer)`](../config_apis/apiserver-config-openshift-io-v1.md#apiserver-config-openshift-io-v1) | List of apiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.AuthenticationList schema

Description
AuthenticationList is a list of Authentication

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Authentication)`](../config_apis/authentication-config-openshift-io-v1.md#authentication-config-openshift-io-v1) | List of authentications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.BuildList schema

Description
BuildList is a list of Build

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Build)`](../config_apis/build-config-openshift-io-v1.md#build-config-openshift-io-v1) | List of builds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ClusterImagePolicyList schema

Description
ClusterImagePolicyList is a list of ClusterImagePolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterImagePolicy)`](../config_apis/clusterimagepolicy-config-openshift-io-v1.md#clusterimagepolicy-config-openshift-io-v1) | List of clusterimagepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ClusterOperatorList schema

Description
ClusterOperatorList is a list of ClusterOperator

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterOperator)`](../config_apis/clusteroperator-config-openshift-io-v1.md#clusteroperator-config-openshift-io-v1) | List of clusteroperators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ClusterVersionList schema

Description
ClusterVersionList is a list of ClusterVersion

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterVersion)`](../config_apis/clusterversion-config-openshift-io-v1.md#clusterversion-config-openshift-io-v1) | List of clusterversions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ConsoleList schema

Description
ConsoleList is a list of Console

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Console)`](../config_apis/console-config-openshift-io-v1.md#console-config-openshift-io-v1) | List of consoles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.DNSList schema

Description
DNSList is a list of DNS

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNS)`](../config_apis/dns-config-openshift-io-v1.md#dns-config-openshift-io-v1) | List of dnses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.FeatureGateList schema

Description
FeatureGateList is a list of FeatureGate

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (FeatureGate)`](../config_apis/featuregate-config-openshift-io-v1.md#featuregate-config-openshift-io-v1) | List of featuregates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ImageContentPolicyList schema

Description
ImageContentPolicyList is a list of ImageContentPolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageContentPolicy)`](../config_apis/imagecontentpolicy-config-openshift-io-v1.md#imagecontentpolicy-config-openshift-io-v1) | List of imagecontentpolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ImageDigestMirrorSetList schema

Description
ImageDigestMirrorSetList is a list of ImageDigestMirrorSet

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageDigestMirrorSet)`](../config_apis/imagedigestmirrorset-config-openshift-io-v1.md#imagedigestmirrorset-config-openshift-io-v1) | List of imagedigestmirrorsets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ImageList schema

Description
ImageList is a list of Image

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Image)`](../config_apis/image-config-openshift-io-v1.md#image-config-openshift-io-v1) | List of images. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ImagePolicyList schema

Description
ImagePolicyList is a list of ImagePolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImagePolicy)`](../config_apis/imagepolicy-config-openshift-io-v1.md#imagepolicy-config-openshift-io-v1) | List of imagepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ImageTagMirrorSetList schema

Description
ImageTagMirrorSetList is a list of ImageTagMirrorSet

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageTagMirrorSet)`](../config_apis/imagetagmirrorset-config-openshift-io-v1.md#imagetagmirrorset-config-openshift-io-v1) | List of imagetagmirrorsets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.InfrastructureList schema

Description
InfrastructureList is a list of Infrastructure

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Infrastructure)`](../config_apis/infrastructure-config-openshift-io-v1.md#infrastructure-config-openshift-io-v1) | List of infrastructures. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.IngressList schema

Description
IngressList is a list of Ingress

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Ingress)`](../config_apis/ingress-config-openshift-io-v1.md#ingress-config-openshift-io-v1) | List of ingresses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.NetworkList schema

Description
NetworkList is a list of Network

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Network)`](../config_apis/network-config-openshift-io-v1.md#network-config-openshift-io-v1) | List of networks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.NodeList schema

Description
NodeList is a list of Node

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Node)`](../config_apis/node-config-openshift-io-v1.md#node-config-openshift-io-v1) | List of nodes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.OAuthList schema

Description
OAuthList is a list of OAuth

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OAuth)`](../config_apis/oauth-config-openshift-io-v1.md#oauth-config-openshift-io-v1) | List of oauths. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.OperatorHubList schema

Description
OperatorHubList is a list of OperatorHub

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorHub)`](../config_apis/operatorhub-config-openshift-io-v1.md#operatorhub-config-openshift-io-v1) | List of operatorhubs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ProjectList schema

Description
ProjectList is a list of Project

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Project)`](../config_apis/project-config-openshift-io-v1.md#project-config-openshift-io-v1) | List of projects. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.ProxyList schema

Description
ProxyList is a list of Proxy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Proxy)`](../config_apis/proxy-config-openshift-io-v1.md#proxy-config-openshift-io-v1) | List of proxies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.config.v1.SchedulerList schema

Description
SchedulerList is a list of Scheduler

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Scheduler)`](../config_apis/scheduler-config-openshift-io-v1.md#scheduler-config-openshift-io-v1) | List of schedulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleCLIDownloadList schema

Description
ConsoleCLIDownloadList is a list of ConsoleCLIDownload

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleCLIDownload)`](../console_apis/consoleclidownload-console-openshift-io-v1.md#consoleclidownload-console-openshift-io-v1) | List of consoleclidownloads. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleExternalLogLinkList schema

Description
ConsoleExternalLogLinkList is a list of ConsoleExternalLogLink

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleExternalLogLink)`](../console_apis/consoleexternalloglink-console-openshift-io-v1.md#consoleexternalloglink-console-openshift-io-v1) | List of consoleexternalloglinks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleLinkList schema

Description
ConsoleLinkList is a list of ConsoleLink

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleLink)`](../console_apis/consolelink-console-openshift-io-v1.md#consolelink-console-openshift-io-v1) | List of consolelinks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleNotificationList schema

Description
ConsoleNotificationList is a list of ConsoleNotification

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleNotification)`](../console_apis/consolenotification-console-openshift-io-v1.md#consolenotification-console-openshift-io-v1) | List of consolenotifications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsolePluginList schema

Description
ConsolePluginList is a list of ConsolePlugin

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsolePlugin)`](../console_apis/consoleplugin-console-openshift-io-v1.md#consoleplugin-console-openshift-io-v1) | List of consoleplugins. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleQuickStartList schema

Description
ConsoleQuickStartList is a list of ConsoleQuickStart

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleQuickStart)`](../console_apis/consolequickstart-console-openshift-io-v1.md#consolequickstart-console-openshift-io-v1) | List of consolequickstarts. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleSampleList schema

Description
ConsoleSampleList is a list of ConsoleSample

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleSample)`](../console_apis/consolesample-console-openshift-io-v1.md#consolesample-console-openshift-io-v1) | List of consolesamples. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.console.v1.ConsoleYAMLSampleList schema

Description
ConsoleYAMLSampleList is a list of ConsoleYAMLSample

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ConsoleYAMLSample)`](../console_apis/consoleyamlsample-console-openshift-io-v1.md#consoleyamlsample-console-openshift-io-v1) | List of consoleyamlsamples. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.helm.v1beta1.HelmChartRepositoryList schema

Description
HelmChartRepositoryList is a list of HelmChartRepository

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (HelmChartRepository)`](../config_apis/helmchartrepository-helm-openshift-io-v1beta1.md#helmchartrepository-helm-openshift-io-v1beta1) | List of helmchartrepositories. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.helm.v1beta1.ProjectHelmChartRepositoryList schema

Description
ProjectHelmChartRepositoryList is a list of ProjectHelmChartRepository

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ProjectHelmChartRepository)`](../config_apis/projecthelmchartrepository-helm-openshift-io-v1beta1.md#projecthelmchartrepository-helm-openshift-io-v1beta1) | List of projecthelmchartrepositories. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machine.v1.ControlPlaneMachineSetList schema

Description
ControlPlaneMachineSetList is a list of ControlPlaneMachineSet

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControlPlaneMachineSet)`](../machine_apis/controlplanemachineset-machine-openshift-io-v1.md#controlplanemachineset-machine-openshift-io-v1) | List of controlplanemachinesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machine.v1beta1.MachineHealthCheckList schema

Description
MachineHealthCheckList is a list of MachineHealthCheck

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineHealthCheck)`](../machine_apis/machinehealthcheck-machine-openshift-io-v1beta1.md#machinehealthcheck-machine-openshift-io-v1beta1) | List of machinehealthchecks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machine.v1beta1.MachineList schema

Description
MachineList is a list of Machine

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Machine)`](../machine_apis/machine-machine-openshift-io-v1beta1.md#machine-machine-openshift-io-v1beta1) | List of machines. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machine.v1beta1.MachineSetList schema

Description
MachineSetList is a list of MachineSet

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineSet)`](../machine_apis/machineset-machine-openshift-io-v1beta1.md#machineset-machine-openshift-io-v1beta1) | List of machinesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.ContainerRuntimeConfigList schema

Description
ContainerRuntimeConfigList is a list of ContainerRuntimeConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ContainerRuntimeConfig)`](../machine_apis/containerruntimeconfig-machineconfiguration-openshift-io-v1.md#containerruntimeconfig-machineconfiguration-openshift-io-v1) | List of containerruntimeconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.ControllerConfigList schema

Description
ControllerConfigList is a list of ControllerConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ControllerConfig)`](../machine_apis/controllerconfig-machineconfiguration-openshift-io-v1.md#controllerconfig-machineconfiguration-openshift-io-v1) | List of controllerconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.KubeletConfigList schema

Description
KubeletConfigList is a list of KubeletConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeletConfig)`](../machine_apis/kubeletconfig-machineconfiguration-openshift-io-v1.md#kubeletconfig-machineconfiguration-openshift-io-v1) | List of kubeletconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.MachineConfigList schema

Description
MachineConfigList is a list of MachineConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfig)`](../machine_apis/machineconfig-machineconfiguration-openshift-io-v1.md#machineconfig-machineconfiguration-openshift-io-v1) | List of machineconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.MachineConfigNodeList schema

Description
MachineConfigNodeList is a list of MachineConfigNode

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfigNode)`](../machine_apis/machineconfignode-machineconfiguration-openshift-io-v1.md#machineconfignode-machineconfiguration-openshift-io-v1) | List of machineconfignodes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.MachineConfigPoolList schema

Description
MachineConfigPoolList is a list of MachineConfigPool

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfigPool)`](../machine_apis/machineconfigpool-machineconfiguration-openshift-io-v1.md#machineconfigpool-machineconfiguration-openshift-io-v1) | List of machineconfigpools. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.MachineOSBuildList schema

Description
MachineOSBuildList is a list of MachineOSBuild

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineOSBuild)`](../machine_apis/machineosbuild-machineconfiguration-openshift-io-v1.md#machineosbuild-machineconfiguration-openshift-io-v1) | List of machineosbuilds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.MachineOSConfigList schema

Description
MachineOSConfigList is a list of MachineOSConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineOSConfig)`](../machine_apis/machineosconfig-machineconfiguration-openshift-io-v1.md#machineosconfig-machineconfiguration-openshift-io-v1) | List of machineosconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.machineconfiguration.v1.PinnedImageSetList schema

Description
PinnedImageSetList is a list of PinnedImageSet

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PinnedImageSet)`](../machine_apis/pinnedimageset-machineconfiguration-openshift-io-v1.md#pinnedimageset-machineconfiguration-openshift-io-v1) | List of pinnedimagesets. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.monitoring.v1.AlertingRuleList schema

Description
AlertingRuleList is a list of AlertingRule

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertingRule)`](../monitoring_apis/alertingrule-monitoring-openshift-io-v1.md#alertingrule-monitoring-openshift-io-v1) | List of alertingrules. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.monitoring.v1.AlertRelabelConfigList schema

Description
AlertRelabelConfigList is a list of AlertRelabelConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AlertRelabelConfig)`](../monitoring_apis/alertrelabelconfig-monitoring-openshift-io-v1.md#alertrelabelconfig-monitoring-openshift-io-v1) | List of alertrelabelconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.network.cloud.v1.CloudPrivateIPConfigList schema

Description
CloudPrivateIPConfigList is a list of CloudPrivateIPConfig

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CloudPrivateIPConfig)`](../network_apis/cloudprivateipconfig-cloud-network-openshift-io-v1.md#cloudprivateipconfig-cloud-network-openshift-io-v1) | List of cloudprivateipconfigs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.controlplane.v1alpha1.PodNetworkConnectivityCheckList schema

Description
PodNetworkConnectivityCheckList is a list of PodNetworkConnectivityCheck

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PodNetworkConnectivityCheck)`](../network_apis/podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1.md#podnetworkconnectivitycheck-controlplane-operator-openshift-io-v1alpha1) | List of podnetworkconnectivitychecks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.imageregistry.v1.ConfigList schema

Description
ConfigList is a list of Config

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](../operator_apis/config-imageregistry-operator-openshift-io-v1.md#config-imageregistry-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.imageregistry.v1.ImagePrunerList schema

Description
ImagePrunerList is a list of ImagePruner

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImagePruner)`](../operator_apis/imagepruner-imageregistry-operator-openshift-io-v1.md#imagepruner-imageregistry-operator-openshift-io-v1) | List of imagepruners. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.ingress.v1.DNSRecordList schema

Description
DNSRecordList is a list of DNSRecord

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNSRecord)`](../operator_apis/dnsrecord-ingress-operator-openshift-io-v1.md#dnsrecord-ingress-operator-openshift-io-v1) | List of dnsrecords. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.network.v1.EgressRouterList schema

Description
EgressRouterList is a list of EgressRouter

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressRouter)`](../network_apis/egressrouter-network-operator-openshift-io-v1.md#egressrouter-network-operator-openshift-io-v1) | List of egressrouters. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.network.v1.OperatorPKIList schema

Description
OperatorPKIList is a list of OperatorPKI

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OperatorPKI)`](../operator_apis/operatorpki-network-operator-openshift-io-v1.md#operatorpki-network-operator-openshift-io-v1) | List of operatorpkis. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.samples.v1.ConfigList schema

Description
ConfigList is a list of Config

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](../operator_apis/config-samples-operator-openshift-io-v1.md#config-samples-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.AuthenticationList schema

Description
AuthenticationList is a list of Authentication

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Authentication)`](../operator_apis/authentication-operator-openshift-io-v1.md#authentication-operator-openshift-io-v1) | List of authentications. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.CloudCredentialList schema

Description
CloudCredentialList is a list of CloudCredential

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CloudCredential)`](../operator_apis/cloudcredential-operator-openshift-io-v1.md#cloudcredential-operator-openshift-io-v1) | List of cloudcredentials. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.ClusterCSIDriverList schema

Description
ClusterCSIDriverList is a list of ClusterCSIDriver

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterCSIDriver)`](../operator_apis/clustercsidriver-operator-openshift-io-v1.md#clustercsidriver-operator-openshift-io-v1) | List of clustercsidrivers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.ConfigList schema

Description
ConfigList is a list of Config

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Config)`](../operator_apis/config-operator-openshift-io-v1.md#config-operator-openshift-io-v1) | List of configs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.ConsoleList schema

Description
ConsoleList is a list of Console

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Console)`](../operator_apis/console-operator-openshift-io-v1.md#console-operator-openshift-io-v1) | List of consoles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.CSISnapshotControllerList schema

Description
CSISnapshotControllerList is a list of CSISnapshotController

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (CSISnapshotController)`](../operator_apis/csisnapshotcontroller-operator-openshift-io-v1.md#csisnapshotcontroller-operator-openshift-io-v1) | List of csisnapshotcontrollers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.DNSList schema

Description
DNSList is a list of DNS

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (DNS)`](../operator_apis/dns-operator-openshift-io-v1.md#dns-operator-openshift-io-v1) | List of dnses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.EtcdList schema

Description
EtcdList is a list of Etcd

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Etcd)`](../operator_apis/etcd-operator-openshift-io-v1.md#etcd-operator-openshift-io-v1) | List of etcds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.IngressControllerList schema

Description
IngressControllerList is a list of IngressController

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IngressController)`](../operator_apis/ingresscontroller-operator-openshift-io-v1.md#ingresscontroller-operator-openshift-io-v1) | List of ingresscontrollers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.InsightsOperatorList schema

Description
InsightsOperatorList is a list of InsightsOperator

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (InsightsOperator)`](../operator_apis/insightsoperator-operator-openshift-io-v1.md#insightsoperator-operator-openshift-io-v1) | List of insightsoperators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.KubeAPIServerList schema

Description
KubeAPIServerList is a list of KubeAPIServer

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeAPIServer)`](../operator_apis/kubeapiserver-operator-openshift-io-v1.md#kubeapiserver-operator-openshift-io-v1) | List of kubeapiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.KubeControllerManagerList schema

Description
KubeControllerManagerList is a list of KubeControllerManager

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeControllerManager)`](../operator_apis/kubecontrollermanager-operator-openshift-io-v1.md#kubecontrollermanager-operator-openshift-io-v1) | List of kubecontrollermanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.KubeSchedulerList schema

Description
KubeSchedulerList is a list of KubeScheduler

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeScheduler)`](../operator_apis/kubescheduler-operator-openshift-io-v1.md#kubescheduler-operator-openshift-io-v1) | List of kubeschedulers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.KubeStorageVersionMigratorList schema

Description
KubeStorageVersionMigratorList is a list of KubeStorageVersionMigrator

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (KubeStorageVersionMigrator)`](../operator_apis/kubestorageversionmigrator-operator-openshift-io-v1.md#kubestorageversionmigrator-operator-openshift-io-v1) | List of kubestorageversionmigrators. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.MachineConfigurationList schema

Description
MachineConfigurationList is a list of MachineConfiguration

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (MachineConfiguration)`](../operator_apis/machineconfiguration-operator-openshift-io-v1.md#machineconfiguration-operator-openshift-io-v1) | List of machineconfigurations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.NetworkList schema

Description
NetworkList is a list of Network

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Network)`](../operator_apis/network-operator-openshift-io-v1.md#network-operator-openshift-io-v1) | List of networks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.OpenShiftAPIServerList schema

Description
OpenShiftAPIServerList is a list of OpenShiftAPIServer

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OpenShiftAPIServer)`](../operator_apis/openshiftapiserver-operator-openshift-io-v1.md#openshiftapiserver-operator-openshift-io-v1) | List of openshiftapiservers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.OpenShiftControllerManagerList schema

Description
OpenShiftControllerManagerList is a list of OpenShiftControllerManager

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (OpenShiftControllerManager)`](../operator_apis/openshiftcontrollermanager-operator-openshift-io-v1.md#openshiftcontrollermanager-operator-openshift-io-v1) | List of openshiftcontrollermanagers. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.ServiceCAList schema

Description
ServiceCAList is a list of ServiceCA

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ServiceCA)`](../operator_apis/serviceca-operator-openshift-io-v1.md#serviceca-operator-openshift-io-v1) | List of servicecas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1.StorageList schema

Description
StorageList is a list of Storage

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Storage)`](../operator_apis/storage-operator-openshift-io-v1.md#storage-operator-openshift-io-v1) | List of storages. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.operator.v1alpha1.ImageContentSourcePolicyList schema

Description
ImageContentSourcePolicyList is a list of ImageContentSourcePolicy

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ImageContentSourcePolicy)`](../operator_apis/imagecontentsourcepolicy-operator-openshift-io-v1alpha1.md#imagecontentsourcepolicy-operator-openshift-io-v1alpha1) | List of imagecontentsourcepolicies. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.performance.v2.PerformanceProfileList schema

Description
PerformanceProfileList is a list of PerformanceProfile

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (PerformanceProfile)`](../node_apis/performanceprofile-performance-openshift-io-v2.md#performanceprofile-performance-openshift-io-v2) | List of performanceprofiles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.quota.v1.ClusterResourceQuotaList schema

Description
ClusterResourceQuotaList is a list of ClusterResourceQuota

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterResourceQuota)`](../schedule_and_quota_apis/clusterresourcequota-quota-openshift-io-v1.md#clusterresourcequota-quota-openshift-io-v1) | List of clusterresourcequotas. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.security.v1.SecurityContextConstraintsList schema

Description
SecurityContextConstraintsList is a list of SecurityContextConstraints

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (SecurityContextConstraints)`](../security_apis/securitycontextconstraints-security-openshift-io-v1.md#securitycontextconstraints-security-openshift-io-v1) | List of securitycontextconstraints. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.tuned.v1.ProfileList schema

Description
ProfileList is a list of Profile

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Profile)`](../node_apis/profile-tuned-openshift-io-v1.md#profile-tuned-openshift-io-v1) | List of profiles. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.openshift.tuned.v1.TunedList schema

Description
TunedList is a list of Tuned

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Tuned)`](../node_apis/tuned-tuned-openshift-io-v1.md#tuned-tuned-openshift-io-v1) | List of tuneds. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.operatorframework.olm.v1.ClusterCatalogList schema

Description
ClusterCatalogList is a list of ClusterCatalog

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterCatalog)`](../operatorhub_apis/clustercatalog-olm-operatorframework-io-v1.md#clustercatalog-olm-operatorframework-io-v1) | List of clustercatalogs. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.operatorframework.olm.v1.ClusterExtensionList schema

Description
ClusterExtensionList is a list of ClusterExtension

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterExtension)`](../operatorhub_apis/clusterextension-olm-operatorframework-io-v1.md#clusterextension-olm-operatorframework-io-v1) | List of clusterextensions. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.x-k8s.cluster.infrastructure.v1beta1.Metal3RemediationList schema

Description
Metal3RemediationList is a list of Metal3Remediation

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Metal3Remediation)`](../provisioning_apis/metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediation-infrastructure-cluster-x-k8s-io-v1beta1) | List of metal3remediations. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.x-k8s.cluster.infrastructure.v1beta1.Metal3RemediationTemplateList schema

Description
Metal3RemediationTemplateList is a list of Metal3RemediationTemplate

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (Metal3RemediationTemplate)`](../provisioning_apis/metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1.md#metal3remediationtemplate-infrastructure-cluster-x-k8s-io-v1beta1) | List of metal3remediationtemplates. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.x-k8s.cluster.ipam.v1beta1.IPAddressClaimList schema

Description
IPAddressClaimList is a list of IPAddressClaim

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAddressClaim)`](../network_apis/ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1.md#ipaddressclaim-ipam-cluster-x-k8s-io-v1beta1) | List of ipaddressclaims. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# io.x-k8s.cluster.ipam.v1beta1.IPAddressList schema

Description
IPAddressList is a list of IPAddress

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (IPAddress)`](../cluster_apis/ipaddress-ipam-cluster-x-k8s-io-v1beta1.md#ipaddress-ipam-cluster-x-k8s-io-v1beta1) | List of ipaddresses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.AdminPolicyBasedExternalRouteList schema

Description
AdminPolicyBasedExternalRouteList is a list of AdminPolicyBasedExternalRoute

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (AdminPolicyBasedExternalRoute)`](../network_apis/adminpolicybasedexternalroute-k8s-ovn-org-v1.md#adminpolicybasedexternalroute-k8s-ovn-org-v1) | List of adminpolicybasedexternalroutes. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.ClusterUserDefinedNetworkList schema

Description
ClusterUserDefinedNetworkList is a list of ClusterUserDefinedNetwork

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (ClusterUserDefinedNetwork)`](../network_apis/clusteruserdefinednetwork-k8s-ovn-org-v1.md#clusteruserdefinednetwork-k8s-ovn-org-v1) | List of clusteruserdefinednetworks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.EgressFirewallList schema

Description
EgressFirewallList is a list of EgressFirewall

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressFirewall)`](../network_apis/egressfirewall-k8s-ovn-org-v1.md#egressfirewall-k8s-ovn-org-v1) | List of egressfirewalls. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.EgressIPList schema

Description
EgressIPList is a list of EgressIP

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressIP)`](../network_apis/egressip-k8s-ovn-org-v1.md#egressip-k8s-ovn-org-v1) | List of egressips. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.EgressQoSList schema

Description
EgressQoSList is a list of EgressQoS

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressQoS)`](../network_apis/egressqos-k8s-ovn-org-v1.md#egressqos-k8s-ovn-org-v1) | List of egressqoses. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.EgressServiceList schema

Description
EgressServiceList is a list of EgressService

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (EgressService)`](../network_apis/egressservice-k8s-ovn-org-v1.md#egressservice-k8s-ovn-org-v1) | List of egressservices. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |

# org.ovn.k8s.v1.UserDefinedNetworkList schema

Description
UserDefinedNetworkList is a list of UserDefinedNetwork

Type
`object`

Required
- `items`

## Schema

| Property | Type | Description |
|----|----|----|
| `apiVersion` | `string` | APIVersion defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#resources> |
| `items` | [`array (UserDefinedNetwork)`](../network_apis/userdefinednetwork-k8s-ovn-org-v1.md#userdefinednetwork-k8s-ovn-org-v1) | List of userdefinednetworks. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md> |
| `kind` | `string` | Kind is a string value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
| `metadata` | [`ListMeta`](index.md#io-k8s-apimachinery-pkg-apis-meta-v1-ListMeta) | Standard list metadata. More info: <https://git.k8s.io/community/contributors/devel/sig-architecture/api-conventions.md#types-kinds> |
