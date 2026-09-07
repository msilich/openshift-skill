<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Review aggregated API client certificate validity and automatic rotation in OpenShift Container Platform to plan maintenance for extension API server authentication.

# Purpose

Aggregated API client certificates are used to authenticate the `KubeAPIServer` when connecting to the aggregated API servers.

# Management

These certificates are managed by the system and not the user.

# Expiration

This certificate authority (CA) is valid for 30 days.

The managed client certificates are valid for 30 days.

CA and client certificates are rotated automatically through the use of controllers.

# Customization

You cannot customize the aggregated API server certificates.
