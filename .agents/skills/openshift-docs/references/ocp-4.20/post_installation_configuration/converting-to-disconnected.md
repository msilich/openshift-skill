<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

There might be some scenarios where you need to convert your OpenShift Container Platform cluster from a connected cluster to a disconnected cluster.

A disconnected cluster, also known as a restricted cluster, does not have an active connection to the internet. As such, you must mirror the contents of your registries and installation media. You can create this mirror registry on a host that can access both the internet and your closed network, or copy images to a device that you can move across network boundaries.

For information on how to convert your cluster, see the [Converting a connected cluster to a disconnected cluster](../disconnected/connected-to-disconnected.md#converting-to-disconnected) procedure in the Disconnected environments section.
