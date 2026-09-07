<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Operator Lifecycle Manager (OLM) v1 uses two key microservice components, Operator Controller and Catalogd, to unpack content and manage extensions on your cluster.

Operator Controller
Extends Kubernetes with an API to install and manage Operators and extensions using metadata from Catalogd.

Catalogd
Unpacks file-based catalog (FBC) content and hosts metadata so users can discover installable extensions.

# Additional resources

- [Operator Controller](operator-controller.md#operator-controller)

- [Catalogd](catalogd.md#catalogd)
