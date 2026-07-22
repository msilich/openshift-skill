<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

A disconnected environment is an environment that does not have full access to the internet.

OpenShift Container Platform is designed to perform many automatic functions that depend on an internet connection, such as retrieving release images from a registry or retrieving update paths and recommendations for the cluster. Without a direct internet connection, you must perform additional setup and configuration for your cluster to maintain full functionality in the disconnected environment.

# Glossary of disconnected environment terms

Although it is used throughout the OpenShift Container Platform documentation, *disconnected environment* is a broad term that can refer to environments with various levels of internet connectivity. Other terms are sometimes used to refer to a specific level of internet connectivity, and these environments might require additional unique configurations.

The following table describes the different terms used to refer to environments without a full internet connection:

<table>
<caption>Disconnected environment terms</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Term</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Air-gapped network</p></td>
<td style="text-align: left;"><p>An environment or network that is completely isolated from an external network.</p>
<p>This isolation depends on a physical separation, or an "air gap", between machines on the internal network and any other part of an external network. Air-gapped environments are often used in industries with strict security or regulatory requirements.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Disconnected environment</p></td>
<td style="text-align: left;"><p>An environment or network that has some level of isolation from an external network.</p>
<p>This isolation could be enabled by physical or logical separation between machines on the internal network and an external network. Regardless of the level of isolation from the external network, a cluster in a disconnected environment does not have access to public services hosted by Red Hat and requires additional setup to maintain full cluster functionality.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Restricted Network</p></td>
<td style="text-align: left;"><p>An environment or network with limited connection to an external network.</p>
<p>A physical connection may exist between machines on the internal network and an external network, but network traffic is limited by additional configurations, such as with firewalls and proxies.</p></td>
</tr>
</tbody>
</table>

# Preferred methods for working with disconnected environments

You can choose between multiple options for most aspects of managing a cluster in a disconnected environment. For example, when mirroring images you can choose between using the oc-mirror OpenShift CLI (`oc`) plugin or using the `oc adm` command.

However, some options provide a simpler and more convenient user experience for disconnected environments, and are the preferred method over their alternatives.

Unless your organizational needs require you to choose another option, use the following methods for mirroring images, installing your cluster, and updating your cluster:

- Mirror your images using the [oc-mirror plugin v2](about-installing-oc-mirror-v2.md#about-installing-oc-mirror-v2).

- Install your cluster using the [Agent-based Installer](../installing/installing_with_agent_based_installer/installing-with-agent-based-installer.md#installing-with-agent-based-installer).

- Update your cluster using a [local OpenShift Update Service instance](updating/disconnected-update-osus.md#updating-disconnected-cluster-osus).
