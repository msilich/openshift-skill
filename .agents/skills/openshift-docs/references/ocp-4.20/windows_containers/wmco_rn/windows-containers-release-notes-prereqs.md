<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The following information details the supported platform versions, Windows Server versions, and networking configurations for the Windows Machine Config Operator (WMCO). See the vSphere documentation for any information that is relevant to only that platform.

# WMCO supported installation method

The WMCO fully supports installing Windows nodes into installer-provisioned infrastructure (IPI) clusters. This is the preferred OpenShift Container Platform installation method.

For user-provisioned infrastructure (UPI) clusters, the WMCO supports installing Windows nodes only into a UPI cluster installed with the `platform: none` field set in the `install-config.yaml` file (bare-metal or provider-agnostic) and only for the [BYOH (Bring Your Own Host)](../byoh-windows-instance.md#byoh-windows-instance) use case. UPI is not supported for any other platform.

# WMCO supported platforms and Windows Server versions

The following table lists the [Windows Server versions](https://docs.microsoft.com/en-us/windows/release-health/windows-server-release-info) that are supported by WMCO 10.20.0, based on the applicable platform. Windows Server versions not listed are not supported and attempting to use them will cause errors. To prevent these errors, use only an appropriate version for your platform.

<table>
<colgroup>
<col style="width: 30%" />
<col style="width: 70%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Platform</th>
<th style="text-align: left;">Supported Windows Server version</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Amazon Web Services (AWS)</p></td>
<td style="text-align: left;"><ul>
<li><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later <sup>[1]</sup></p></li>
<li><p>Windows Server 2019, version 1809</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Microsoft Azure</p></td>
<td style="text-align: left;"><ul>
<li><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></li>
<li><p>Windows Server 2019, version 1809</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>VMware vSphere</p></td>
<td style="text-align: left;"><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Google Cloud</p></td>
<td style="text-align: left;"><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Nutanix</p></td>
<td style="text-align: left;"><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Bare metal or provider agnostic</p></td>
<td style="text-align: left;"><ul>
<li><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></li>
<li><p>Windows Server 2019, version 1809</p></li>
</ul></td>
</tr>
</tbody>
</table>

1.  For disconnected clusters, the Windows AMI must have the EC2LaunchV2 agent version 2.0.2107 or later installed. For more information, see the [Install the latest version of EC2Launch v2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2launch-v2-install.html) in the AWS documentation.

# Supported networking

Hybrid networking with OVN-Kubernetes is the only supported networking configuration. See the additional resources below for more information on this functionality. The following tables outline the type of networking configuration and Windows Server versions to use based on your platform. You must specify the network configuration when you install the cluster.

<div class="note">

<div class="title">

</div>

- The WMCO does not support OVN-Kubernetes without hybrid networking or OpenShift SDN.

- Dual NIC is not supported on WMCO-managed Windows instances.

</div>

| Platform | Supported networking |
|----|----|
| Amazon Web Services (AWS) | Hybrid networking with OVN-Kubernetes |
| Microsoft Azure | Hybrid networking with OVN-Kubernetes |
| VMware vSphere | Hybrid networking with OVN-Kubernetes with a custom VXLAN port |
| Google Cloud | Hybrid networking with OVN-Kubernetes |
| Nutanix | Hybrid networking with OVN-Kubernetes |
| Bare metal or provider agnostic | Hybrid networking with OVN-Kubernetes |

Platform networking support

<table>
<caption>Hybrid OVN-Kubernetes Windows Server support</caption>
<colgroup>
<col style="width: 50%" />
<col style="width: 50%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Hybrid networking with OVN-Kubernetes</th>
<th style="text-align: left;">Supported Windows Server version</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Default VXLAN port</p></td>
<td style="text-align: left;"><ul>
<li><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></li>
<li><p>Windows Server 2019, version 1809</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p>Custom VXLAN port</p></td>
<td style="text-align: left;"><p>Windows Server 2022, OS Build <a href="https://support.microsoft.com/en-us/topic/april-25-2022-kb5012637-os-build-20348-681-preview-2233d69c-d4a5-4be9-8c24-04a450861a8d">20348.681</a> or later</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Hybrid networking](../../networking/ovn_kubernetes_network_provider/configuring-hybrid-networking.md#configuring-hybrid-networking)

</div>
