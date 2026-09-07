<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Eviction \[policy/v1\]

Description
Eviction evicts a pod from its node subject to certain policies and safety constraints. This is a subresource of Pod. A request to cause such an eviction is created by POSTing to …​/pods/\<pod name\>/evictions.

Type
`object`

# PodDisruptionBudget \[policy/v1\]

Description
PodDisruptionBudget is an object to define the max disruption that can be caused to a collection of pods

Type
`object`
