<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review control plane certificate namespaces and automatic rotation in OpenShift Container Platform to plan maintenance and recover from expiration.

# Location

Control plane certificates are included in these namespaces:

- `openshift-config-managed`

- `openshift-kube-apiserver`

- `openshift-kube-apiserver-operator`

- `openshift-kube-controller-manager`

- `openshift-kube-controller-manager-operator`

- `openshift-kube-scheduler`

# Management

Control plane certificates are managed by the system and rotated automatically.

If control plane certificates expire, see "Recovering from expired control plane certificates".

# Additional resources

- [Recovering from expired control plane certificates](../../backup_and_restore/control_plane_backup_and_restore/disaster_recovery/scenario-3-expired-certs.md#dr-recovering-expired-certs)
