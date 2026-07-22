<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Install the OpenShift API for Data Protection (OADP) Operator on OpenShift Container Platform 4.17 by using Operator Lifecycle Manager (OLM).

The OADP Operator installs [Velero 1.16](https://velero.io/docs/v1.16/).

# Installing the OADP Operator

Install the OADP Operator by using the OpenShift Container Platform web console.

<div>

<div class="title">

Prerequisites

</div>

- You must be logged in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

2.  Use the **Filter by keyword** field to find the **OADP Operator**.

3.  Select the **OADP Operator** and click **Install**.

4.  Click **Install** to install the Operator in the `openshift-adp` project.

5.  Click **Ecosystem** → **Installed Operators** to verify the installation.

</div>

# OADP-Velero-OpenShift Container Platform version relationship

Review the version relationship between OADP, Velero, and OpenShift Container Platform to decide compatible version combinations. This helps you select the appropriate OADP version for your cluster environment.

| OADP version | Velero version | OpenShift Container Platform version |
|--------------|----------------|--------------------------------------|
| 1.3.0        | 1.12           | 4.12-4.15                            |
| 1.3.1        | 1.12           | 4.12-4.15                            |
| 1.3.2        | 1.12           | 4.12-4.15                            |
| 1.3.3        | 1.12           | 4.12-4.15                            |
| 1.3.4        | 1.12           | 4.12-4.15                            |
| 1.3.5        | 1.12           | 4.12-4.15                            |
| 1.4.0        | 1.14           | 4.14-4.18                            |
| 1.4.1        | 1.14           | 4.14-4.18                            |
| 1.4.2        | 1.14           | 4.14-4.18                            |
| 1.4.3        | 1.14           | 4.14-4.18                            |
| 1.5.0        | 1.16           | 4.19                                 |

## Additional resources

- [Velero 1.12 documentation](https://velero.io/docs/v1.12/)

- [Velero 1.14 documentation](https://velero.io/docs/v1.14/)

- [Velero 1.16 documentation](https://velero.io/docs/v1.16/)
