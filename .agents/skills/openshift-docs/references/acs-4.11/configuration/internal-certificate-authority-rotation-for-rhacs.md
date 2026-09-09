<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Certificate authority (CA) rotation is important in Red Hat Advanced Cluster Security for Kubernetes (RHACS) to ensure that Central and secured clusters can communicate. RHACS has an internal CA that is valid for 5 years. Central and secured cluster service certificates depend on this CA. If the CA expires, RHACS stops working.

Previously, if the internal CA expired, you had to delete the `central-tls` secret and manually reregister all the secured clusters. Starting with RHACS 4.9, the Operator manages CA rotation. Central simultaneously trusts two CAs, enabling overlap and providing a smoother migration.

<a id="ca-rotation-support-for-different-installation-methods_internal-certificate-authority-rotation-for-rhacs"></a>

# CA rotation support for different installation methods

The following table shows the level of certificate authority (CA) rotation support based on the installation method you use for Central and secured clusters:

| Component | Installation method | CA rotation support | Notes |
|----|----|----|----|
| Central | Operator-installed | Full support | Migration is fully automated. |
| Central | Helm or manifest | Not supported | Use the Operator for automatic CA rotation. |
| Secured cluster | Operator-installed | Full support | Migration is fully automated if the connected Central instance is also Operator-installed. |
| Secured cluster | Helm or manifest | Partial support | Connect to Central that has rotated its CA, but cannot rotate its own service certificates to the new CA. Manual re-registration is required before the old CA expires. |

Installation methods and CA rotation support

<a id="preparing-for-deployments-and-upgrades_internal-certificate-authority-rotation-for-rhacs"></a>

# Preparing for deployments and upgrades

The following table lists the actions you must take for each deployment scenario during certificate authority (CA) rotation or upgrades:

<table>
<caption>Required user actions</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Deployment scenario</th>
<th style="text-align: left;">What you must do</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Operator-managed secured clusters</p></td>
<td style="text-align: left;"><p>You do not need to take any action if Central is also Operator-managed. The Operator automates rotation.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Helm-managed secured clusters</p></td>
<td style="text-align: left;"><p>Remove the cluster and reregister it with a new cluster registration secret (CRS) or init bundle before the 5-year CA expires. Follow these steps:</p>
<ol type="1">
<li><p>Delete the cluster from Central.</p></li>
<li><p>Remove the Secured Cluster CR (or delete all the <code>tls-cert-*</code> certificates and redeploy the cluster.</p></li>
<li><p>Register the secured cluster with a new CRS.</p></li>
</ol></td>
</tr>
<tr>
<td style="text-align: left;"><p>Upgrading a Central instance older than 4 years to Red Hat Advanced Cluster Security for Kubernetes (RHACS) 4.9</p></td>
<td style="text-align: left;"><div class="note">
<div class="title">
&#10;</div>
<p>Central switches to certificates signed by the new CA and secured clusters older than version 4.9 cannot trust the certificates.</p>
</div>
<p>You can do any of the following tasks:</p>
<ul>
<li><p>Upgrade all secured clusters to RHACS 4.9.</p></li>
<li><p>Reregister any secured clusters that you cannot upgrade.</p></li>
</ul>
<p>Secured clusters for RHACS 4.9 and later versions automatically trust the new CA if the old CA is still valid.</p></td>
</tr>
</tbody>
</table>
