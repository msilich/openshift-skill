<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use OpenShift API for Data Protection (OADP) to safeguard applications, application-related cluster resources, persistent volumes, and internal images on OpenShift Container Platform. OADP backs up containerized applications and virtual machines (VMs). This helps you ensure disaster recovery.

However, OADP does not serve as a disaster recovery solution for `etcd` or OpenShift Operators.

> [!IMPORTANT]
> OADP support is applicable to customer workload namespaces and cluster scope resources.
>
> Full cluster `backup` and `restore` are not supported.

# OpenShift API for Data Protection APIs

OADP provides APIs that enable multiple approaches to customizing backups and preventing the inclusion of unnecessary or inappropriate resources.

OADP provides the following APIs. See the *Additional resources* section for more details.

- `Backup`

- `Restore`

- `Schedule`

- `BackupStorageLocation`

- `VolumeSnapshotLocation`

## Support for OpenShift API for Data Protection

Review the OADP support matrix for version compatibility with OpenShift Container Platform releases and lifecycle policy information, including Extended Update Support (EUS) options.

<table>
<caption>Supported versions of OADP</caption>
<colgroup>
<col style="width: 10%" />
<col style="width: 12%" />
<col style="width: 12%" />
<col style="width: 13%" />
<col style="width: 13%" />
<col style="width: 20%" />
<col style="width: 20%" />
</colgroup>
<tbody>
<tr>
<td style="text-align: left;"><p>Version</p></td>
<td style="text-align: left;"><p>OpenShift Container Platform version</p></td>
<td style="text-align: left;"><p>General availability</p></td>
<td style="text-align: left;"><p>Full support ends</p></td>
<td style="text-align: left;"><p>Maintenance ends</p></td>
<td style="text-align: left;"><p>Extended Update Support (EUS)</p></td>
<td style="text-align: left;"><p>Extended Update Support Term 2 (EUS Term 2)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>1.5</p></td>
<td style="text-align: left;"><ul>
<li><p>4.19</p></li>
<li><p>4.20</p></li>
<li><p>4.21</p></li>
</ul></td>
<td style="text-align: left;"><p>17 June 2025</p></td>
<td style="text-align: left;"><p>Release of 1.6</p></td>
<td style="text-align: left;"><p>Release of 1.7</p></td>
<td style="text-align: left;"><p>EUS must be on OpenShift Container Platform 4.21</p></td>
<td style="text-align: left;"><p>EUS Term 2 must be on OpenShift Container Platform 4.21</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>1.4</p></td>
<td style="text-align: left;"><ul>
<li><p>4.14</p></li>
<li><p>4.15</p></li>
<li><p>4.16</p></li>
<li><p>4.17</p></li>
<li><p>4.18</p></li>
</ul></td>
<td style="text-align: left;"><p>10 Jul 2024</p></td>
<td style="text-align: left;"><p>Release of 1.5</p></td>
<td style="text-align: left;"><p>Release of 1.6</p></td>
<td style="text-align: left;"><p>27 Jun 2026</p>
<p>EUS must be on OpenShift Container Platform 4.16</p></td>
<td style="text-align: left;"><p>27 Jun 2027</p>
<p>EUS Term 2 must be on OpenShift Container Platform 4.16</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>1.3</p></td>
<td style="text-align: left;"><ul>
<li><p>4.12</p></li>
<li><p>4.13</p></li>
<li><p>4.14</p></li>
<li><p>4.15</p></li>
</ul></td>
<td style="text-align: left;"><p>29 Nov 2023</p></td>
<td style="text-align: left;"><p>10 Jul 2024</p></td>
<td style="text-align: left;"><p>Release of 1.5</p></td>
<td style="text-align: left;"><p>31 Oct 2025</p>
<p>EUS must be on OpenShift Container Platform 4.14</p></td>
<td style="text-align: left;"><p>31 Oct 2026</p>
<p>EUS Term 2 must be on OpenShift Container Platform 4.14</p></td>
</tr>
</tbody>
</table>

### Unsupported versions of the OADP Operator

|         |                      |                    |                   |
|---------|----------------------|--------------------|-------------------|
| Version | General availability | Full support ended | Maintenance ended |
| 1.2     | 14 Jun 2023          | 29 Nov 2023        | 10 Jul 2024       |
| 1.1     | 01 Sep 2022          | 14 Jun 2023        | 29 Nov 2023       |
| 1.0     | 09 Feb 2022          | 01 Sep 2022        | 14 Jun 2023       |

Previous versions of the OADP Operator which are no longer supported

For more details about EUS, see [Extended Update Support](https://access.redhat.com/support/policy/updates/openshift#eus).

For more details about EUS Term 2, see [Extended Update Support Term 2](https://access.redhat.com/support/policy/updates/openshift#eust2).

<div>

<div class="title">

Additional resources

</div>

- [Backup](backing_up_and_restoring/backing-up-applications.md#backing-up-applications)

- [Restore](backing_up_and_restoring/restoring-applications.md#restoring-applications)

- [Schedule](backing_up_and_restoring/oadp-scheduling-backups-doc.md#oadp-scheduling-backups-doc)

- [BackupStorageLocation](installing/installing-oadp-aws.md#oadp-about-backup-snapshot-locations_installing-oadp-aws)

- [VolumeSnapshotLocation](backing_up_and_restoring/oadp-backing-up-pvs-csi-doc.md#oadp-backing-up-pvs-csi-doc)

- [Backing up etcd](../control_plane_backup_and_restore/backing-up-etcd.md#backup-etcd)

</div>
