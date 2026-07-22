<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The release notes for Migration Toolkit for Containers (MTC) describe new features and enhancements, deprecated features, and known issues.

The MTC enables you to migrate application workloads between OpenShift Container Platform clusters at the granularity of a namespace.

You can migrate from [OpenShift Container Platform 3 to 4.17](../../migrating_from_ocp_3_to_4/about-migrating-from-3-to-4.md#about-migrating-from-3-to-4) and between OpenShift Container Platform 4 clusters.

MTC provides a web console and an API, based on Kubernetes custom resources, to help you control the migration and minimize application downtime.

For information on the support policy for MTC, see [OpenShift Application and Cluster Migration Solutions](https://access.redhat.com/support/policy/updates/openshift#app_migration), part of the *Red Hat OpenShift Container Platform Life Cycle Policy*.

# Migration Toolkit for Containers 1.7.17 release notes

Migration Toolkit for Containers (MTC) 1.7.17 is a Container Grade Only (CGO) release, released to refresh the health grades of the containers, with no changes to any code in the product itself compared to that of MTC 1.7.16.

# Migration Toolkit for Containers 1.7.16 release notes

## Resolved issues

This release has the following resolved issues:

<div class="formalpara">

<div class="title">

CVE-2023-45290: Golang: `net/http`: Memory exhaustion in the `Request.ParseMultipartForm` method

</div>

A flaw was found in the `net/http` Golang standard library package, which impacts earlier versions of MTC. When parsing a `multipart` form, either explicitly with `Request.ParseMultipartForm` or implicitly with `Request.FormValue`, `Request.PostFormValue`, or `Request.FormFile` methods, limits on the total size of the parsed form are not applied to the memory consumed while reading a single form line. This permits a maliciously crafted input containing long lines to cause the allocation of arbitrarily large amounts of memory, potentially leading to memory exhaustion.

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2023-45290](https://access.redhat.com/security/cve/CVE-2023-45290)

<div class="formalpara">

<div class="title">

CVE-2024-24783: Golang: `crypto/x509`: Verify panics on certificates with an unknown public key algorithm

</div>

A flaw was found in the `crypto/x509` Golang standard library package, which impacts earlier versions of MTC. Verifying a certificate chain that contains a certificate with an unknown public key algorithm causes `Certificate.Verify` to panic. This affects all `crypto/tls` clients and servers that set `Config.ClientAuth` to `VerifyClientCertIfGiven` or `RequireAndVerifyClientCert`. The default behavior is for TLS servers to not verify client certificates.

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2024-24783](https://access.redhat.com/security/cve/cve-2024-24783).

<div class="formalpara">

<div class="title">

CVE-2024-24784: Golang: `net/mail`: Comments in display names are incorrectly handled

</div>

A flaw was found in the `net/mail` Golang standard library package, which impacts earlier versions of MTC. The `ParseAddressList` function incorrectly handles comments, text in parentheses, and display names. As this is a misalignment with conforming address parsers, it can result in different trust decisions being made by programs using different parsers.

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2024-24784](https://access.redhat.com/security/cve/cve-2024-24784).

<div class="formalpara">

<div class="title">

CVE-2024-24785: Golang: `html/template`: Errors returned from `MarshalJSON` methods may break template escaping

</div>

A flaw was found in the `html/template` Golang standard library package, which impacts earlier versions of MTC. If errors returned from `MarshalJSON` methods contain user-controlled data, they could be used to break the contextual auto-escaping behavior of the `html/template` package, allowing subsequent actions to inject unexpected content into templates.

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2024-24785](https://access.redhat.com/security/cve/cve-2024-24785).

<div class="formalpara">

<div class="title">

CVE-2024-29180: `webpack-dev-middleware`: Lack of URL validation may lead to file leak

</div>

A flaw was found in the `webpack-dev-middleware package`, which impacts earlier versions of MTC. This flaw fails to validate the supplied URL address sufficiently before returning local files, which could allow an attacker to craft URLs to return arbitrary local files from the developer’s machine.

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2024-29180](https://access.redhat.com/security/cve/cve-2024-29180).

<div class="formalpara">

<div class="title">

CVE-2024-30255: `envoy`: HTTP/2 CPU exhaustion due to CONTINUATION frame flood

</div>

A flaw was found in how the `envoy` proxy implements the HTTP/2 codec, which impacts earlier versions of MTC. There are insufficient limitations placed on the number of `CONTINUATION` frames that can be sent within a single stream, even after exceeding the header map limits of `envoy`. This flaw could allow an unauthenticated remote attacker to send packets to vulnerable servers. These packets could consume compute resources and cause a denial of service (DoS).

</div>

To resolve this issue, upgrade to MTC 1.7.16.

For more details, see [CVE-2024-30255](https://access.redhat.com/security/cve/cve-2024-30255).

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Direct Volume Migration is failing as the Rsync pod on the source cluster goes into an `Error` state

</div>

On migrating any application with a Persistent Volume Claim (PVC), the `Stage` migration operation succeeds with warnings, but the Direct Volume Migration (DVM) fails with the `rsync` pod on the source namespace moving into an `error` state. [(BZ#2256141)](https://bugzilla.redhat.com/show_bug.cgi?id=2256141)

</div>

<div class="formalpara">

<div class="title">

The conflict condition is briefly cleared after it is created

</div>

When creating a new state migration plan that returns a conflict error message, the error message is cleared very shortly after it is displayed. [(BZ#2144299)](https://bugzilla.redhat.com/show_bug.cgi?id=2144299)

</div>

<div class="formalpara">

<div class="title">

Migration fails when there are multiple Volume Snapshot Locations of different provider types configured in a cluster

</div>

When there are multiple Volume Snapshot Locations (VSLs) in a cluster with different provider types, but you have not set any of them as the default VSL, Velero results in a validation error that causes migration operations to fail. [(BZ#2180565)](https://bugzilla.redhat.com/show_bug.cgi?id=2180565)

</div>

# Migration Toolkit for Containers 1.7.15 release notes

## Resolved issues

This release has the following resolved issues:

<div class="formalpara">

<div class="title">

CVE-2024-24786: A flaw was found in Golang’s protobuf module, where the unmarshal function can enter an infinite loop

</div>

A flaw was found in the `protojson.Unmarshal` function that could cause the function to enter an infinite loop when unmarshaling certain forms of invalid JSON messages. This condition could occur when unmarshaling into a message that contained a `google.protobuf.Any` value or when the `UnmarshalOptions.DiscardUnknown` option was set in a JSON-formatted message.

</div>

To resolve this issue, upgrade to MTC 1.7.15.

For more details, see [(CVE-2024-24786)](https://access.redhat.com/security/cve/CVE-2024-24786).

<div class="formalpara">

<div class="title">

CVE-2024-28180: `jose-go` improper handling of highly compressed data

</div>

A vulnerability was found in Jose due to improper handling of highly compressed data. An attacker could send a JSON Web Encryption (JWE) encrypted message that contained compressed data that used large amounts of memory and CPU when decompressed by the `Decrypt` or `DecryptMulti` functions.

</div>

To resolve this issue, upgrade to MTC 1.7.15.

For more details, see [(CVE-2024-28180)](https://access.redhat.com/security/cve/CVE-2024-28180).

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Direct Volume Migration is failing as the Rsync pod on the source cluster goes into an `Error` state

</div>

On migrating any application with Persistent Volume Claim (PVC), the `Stage` migration operation succeeds with warnings, and Direct Volume Migration (DVM) fails with the `rsync` pod on the source namespace going into an `error` state. [(BZ#2256141)](https://bugzilla.redhat.com/show_bug.cgi?id=2256141)

</div>

<div class="formalpara">

<div class="title">

The conflict condition is briefly cleared after it is created

</div>

When creating a new state migration plan that results in a conflict error message, the error message is cleared shortly after it is displayed. [(BZ#2144299)](https://bugzilla.redhat.com/show_bug.cgi?id=2144299)

</div>

<div class="formalpara">

<div class="title">

Migration fails when there are multiple Volume Snapshot Locations (VSLs) of different provider types configured in a cluster with no specified default VSL.

</div>

When there are multiple VSLs in a cluster with different provider types, and you set none of them as the default VSL, Velero results in a validation error that causes migration operations to fail. [(BZ#2180565)](https://bugzilla.redhat.com/show_bug.cgi?id=2180565)

</div>

# Migration Toolkit for Containers 1.7.14 release notes

## Resolved issues

This release has the following resolved issues:

<div class="formalpara">

<div class="title">

CVE-2023-39325 CVE-2023-44487: various flaws

</div>

A flaw was found in the handling of multiplexed streams in the HTTP/2 protocol, which is utilized by Migration Toolkit for Containers (MTC). A client could repeatedly make a request for a new multiplex stream then immediately send an `RST_STREAM` frame to cancel those requests. This activity created additional workloads for the server in terms of setting up and dismantling streams, but avoided any server-side limitations on the maximum number of active streams per connection. As a result, a denial of service occurred due to server resource consumption.

</div>

- [(BZ#2243564)](https://bugzilla.redhat.com/show_bug.cgi?id=2243564)

- [(BZ#2244013)](https://bugzilla.redhat.com/show_bug.cgi?id=2244013)

- [(BZ#2244014)](https://bugzilla.redhat.com/show_bug.cgi?id=2244014)

- [(BZ#2244015)](https://bugzilla.redhat.com/show_bug.cgi?id=2244015)

- [(BZ#2244016)](https://bugzilla.redhat.com/show_bug.cgi?id=2244016)

- [(BZ#2244017)](https://bugzilla.redhat.com/show_bug.cgi?id=2244017)

To resolve this issue, upgrade to MTC 1.7.14.

For more details, see [(CVE-2023-44487)](https://access.redhat.com/security/cve/cve-2023-44487) and [(CVE-2023-39325)](https://access.redhat.com/security/cve/cve-2023-39325).

<div>

<div class="title">

CVE-2023-39318 CVE-2023-39319 CVE-2023-39321: various flaws

</div>

- [(CVE-2023-39318)](https://access.redhat.com/security/cve/cve-2023-39318): A flaw was discovered in Golang, utilized by MTC. The `html/template` package did not properly handle HTML-like `""` comment tokens, or the hashbang `"#!"` comment tokens, in `<script>` contexts. This flaw could cause the template parser to improperly interpret the contents of `<script>` contexts, causing actions to be improperly escaped.

  - [(BZ#2238062)](https://bugzilla.redhat.com/show_bug.cgi?id=2238062)

  - [(BZ#2238088)](https://bugzilla.redhat.com/show_bug.cgi?id=2238088)

- [(CVE-2023-39319)](https://access.redhat.com/security/cve/cve-2023-39319): A flaw was discovered in Golang, utilized by MTC. The `html/template` package did not apply the proper rules for handling occurrences of `"<script"`, `"<!--"`, and `"</script"` within JavaScript literals in \<script\> contexts. This could cause the template parser to improperly consider script contexts to be terminated early, causing actions to be improperly escaped.

  - [(BZ#2238062)](https://bugzilla.redhat.com/show_bug.cgi?id=2238062)

  - [(BZ#2238088)](https://bugzilla.redhat.com/show_bug.cgi?id=2238088)

- [(CVE-2023-39321)](https://access.redhat.com/security/cve/cve-2023-39321): A flaw was discovered in Golang, utilized by MTC. Processing an incomplete post-handshake message for a QUIC connection could cause a panic.

  - [(BZ#2238062)](https://bugzilla.redhat.com/show_bug.cgi?id=2238062)

  - [(BZ#2238088)](https://bugzilla.redhat.com/show_bug.cgi?id=2238088)

- [(CVE-2023-3932)](https://access.redhat.com/security/cve/cve-2023-39322): A flaw was discovered in Golang, utilized by MTC. Connections using the QUIC transport protocol did not set an upper bound on the amount of data buffered when reading post-handshake messages, allowing a malicious QUIC connection to cause unbounded memory growth.

  - [(BZ#2238088)](https://bugzilla.redhat.com/show_bug.cgi?id=2238088)

</div>

To resolve these issues, upgrade to MTC 1.7.14.

For more details, see [(CVE-2023-39318)](https://access.redhat.com/security/cve/cve-2023-39318), [(CVE-2023-39319)](https://access.redhat.com/security/cve/cve-2023-39319), and [(CVE-2023-39321)](https://access.redhat.com/security/cve/cve-2023-39321).

## Known issues

There are no major known issues in this release.

# Migration Toolkit for Containers 1.7.13 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

There are no major known issues in this release.

# Migration Toolkit for Containers 1.7.12 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Error code 504 is displayed on the Migration details page

</div>

On the **Migration details** page, at first, the `migration details` are displayed without any issues. However, after sometime, the details disappear, and a `504` error is returned. ([**BZ#2231106**](https://bugzilla.redhat.com/show_bug.cgi?id=2231106))

</div>

<div class="formalpara">

<div class="title">

Old restic pods are not removed when upgrading Migration Toolkit for Containers 1.7.x to Migration Toolkit for Containers 1.8

</div>

On upgrading the Migration Toolkit for Containers (MTC) operator from 1.7.x to 1.8.x, the old restic pods are not removed. After the upgrade, both restic and node-agent pods are visible in the namespace. ([**BZ#2236829**](https://bugzilla.redhat.com/show_bug.cgi?id=2236829))

</div>

# Migration Toolkit for Containers 1.7.11 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

There are no known issues in this release.

# Migration Toolkit for Containers 1.7.10 release notes

## Resolved issues

This release has the following major resolved issue:

<div class="formalpara">

<div class="title">

Adjust rsync options in DVM

</div>

In this release, you can prevent absolute symlinks from being manipulated by Rsync in the course of direct volume migration (DVM). Running DVM in privileged mode preserves absolute symlinks inside the persistent volume claims (PVCs). To switch to privileged mode, in the `MigrationController` CR, set the `migration_rsync_privileged` spec to `true`. ([**BZ#2204461**](https://bugzilla.redhat.com/show_bug.cgi?id=2204461))

</div>

## Known issues

There are no known issues in this release.

# Migration Toolkit for Containers 1.7.9 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

This release has the following known issue:

<div class="formalpara">

<div class="title">

Adjust rsync options in DVM

</div>

In this release, users are unable to prevent absolute symlinks from being manipulated by rsync during direct volume migration (DVM). ([**BZ#2204461**](https://bugzilla.redhat.com/show_bug.cgi?id=2204461))

</div>

# Migration Toolkit for Containers 1.7.8 release notes

## Resolved issues

This release has the following major resolved issues:

<div class="formalpara">

<div class="title">

Velero image cannot be overridden in the Migration Toolkit for Containers (MTC) operator

</div>

In previous releases, it was not possible to override the velero image using the `velero_image_fqin` parameter in the `MigrationController` Custom Resource (CR). ([**BZ#2143389**](https://bugzilla.redhat.com/show_bug.cgi?id=2143389))

</div>

<div class="formalpara">

<div class="title">

Adding a MigCluster from the UI fails when the domain name has more than six characters

</div>

In previous releases, adding a MigCluster from the UI failed when the domain name had more than six characters. The UI code expected a domain name of between two and six characters. ([**BZ#2152149**](https://bugzilla.redhat.com/show_bug.cgi?id=2152149))

</div>

<div class="formalpara">

<div class="title">

UI fails to render the Migrations' page: Cannot read properties of undefined (reading 'name')

</div>

In previous releases, the UI failed to render the Migrations' page, returning `Cannot read properties of undefined (reading 'name')`. ([**BZ#2163485**](https://bugzilla.redhat.com/show_bug.cgi?id=2163485))

</div>

<div class="formalpara">

<div class="title">

Creating DPA resource fails on Red Hat OpenShift Container Platform 4.6 clusters

</div>

In previous releases, when deploying MTC on an OpenShift Container Platform 4.6 cluster, the DPA failed to be created according to the logs, which resulted in some pods missing. From the logs in the migration-controller in the OpenShift Container Platform 4.6 cluster, it indicated that an unexpected `null` value was passed, which caused the error. ([**BZ#2173742**](https://bugzilla.redhat.com/show_bug.cgi?id=2173742))

</div>

## Known issues

There are no known issues in this release.

# Migration Toolkit for Containers 1.7.7 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

There are no known issues in this release.

# Migration Toolkit for Containers 1.7.6 release notes

## New features

<div class="formalpara">

<div class="title">

Implement proposed changes for DVM support with PSA in Red Hat OpenShift Container Platform 4.12

</div>

With the incoming enforcement of Pod Security Admission (PSA) in OpenShift Container Platform 4.12 the default pod would run with a `restricted` profile. This `restricted` profile would mean workloads to migrate would be in violation of this policy and no longer work as of now. The following enhancement outlines the changes that would be required to remain compatible with OCP 4.12. ([**MIG-1240**](https://issues.redhat.com/browse/MIG-1240))

</div>

## Resolved issues

This release has the following major resolved issues:

<div class="formalpara">

<div class="title">

Unable to create Storage Class Conversion plan due to missing cronjob error in Red Hat OpenShift Platform 4.12

</div>

In previous releases, on the persistent volumes page, an error is thrown that a CronJob is not available in version `batch/v1beta1`, and when clicking on cancel, the migplan is created with status `Not ready`. ([**BZ#2143628**](https://bugzilla.redhat.com/show_bug.cgi?id=2143628))

</div>

## Known issues

This release has the following known issue:

<div class="formalpara">

<div class="title">

Conflict conditions are cleared briefly after they are created

</div>

When creating a new state migration plan that will result in a conflict error, that error is cleared shorty after it is displayed. ([**BZ#2144299**](https://bugzilla.redhat.com/show_bug.cgi?id=2144299))

</div>

# Migration Toolkit for Containers 1.7.5 release notes

## Resolved issues

This release has the following major resolved issue:

<div class="formalpara">

<div class="title">

Direct Volume Migration is failing as rsync pod on source cluster move into Error state

</div>

In previous release, migration succeeded with warnings but Direct Volume Migration failed with rsync pod on source namespace going into error state. ([**\*BZ#2132978**](https://bugzilla.redhat.com/show_bug.cgi?id=2132978))

</div>

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Velero image cannot be overridden in the Migration Toolkit for Containers (MTC) operator

</div>

In previous releases, it was not possible to override the velero image using the `velero_image_fqin` parameter in the `MigrationController` Custom Resource (CR). ([**BZ#2143389**](https://bugzilla.redhat.com/show_bug.cgi?id=2143389))

</div>

<div class="formalpara">

<div class="title">

When editing a MigHook in the UI, the page might fail to reload

</div>

The UI might fail to reload when editing a hook if there is a network connection issue. After the network connection is restored, the page will fail to reload until the cache is cleared. ([**BZ#2140208**](https://bugzilla.redhat.com/show_bug.cgi?id=2140208))

</div>

# Migration Toolkit for Containers 1.7.4 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

<div class="formalpara">

<div class="title">

Rollback missing out deletion of some resources from the target cluster

</div>

On performing the roll back of an application from the Migration Toolkit for Containers (MTC) UI, some resources are not being deleted from the target cluster and the roll back is showing a status as successfully completed. ([**BZ#2126880**](https://bugzilla.redhat.com/show_bug.cgi?id=2126880))

</div>

# Migration Toolkit for Containers 1.7.3 release notes

## Resolved issues

This release has the following major resolved issues:

<div class="formalpara">

<div class="title">

Correct DNS validation for destination namespace

</div>

In previous releases, the MigPlan could not be validated if the destination namespace started with a non-alphabetic character. ([**BZ#2102231**](https://bugzilla.redhat.com/show_bug.cgi?id=2102231))

</div>

<div class="formalpara">

<div class="title">

Deselecting all PVCs from UI still results in an attempted PVC transfer

</div>

In previous releases, while doing a full migration, unselecting the persistent volume claims (PVCs) would not skip selecting the PVCs and still try to migrate them. ([**BZ#2106073**](https://bugzilla.redhat.com/show_bug.cgi?id=2106073))

</div>

<div class="formalpara">

<div class="title">

Incorrect DNS validation for destination namespace

</div>

In previous releases, MigPlan could not be validated because the destination namespace started with a non-alphabetic character. ([**BZ#2102231**](https://bugzilla.redhat.com/show_bug.cgi?id=2102231))

</div>

## Known issues

There are no known issues in this release.

# Migration Toolkit for Containers 1.7.2 release notes

## Resolved issues

This release has the following major resolved issues:

<div class="formalpara">

<div class="title">

MTC UI does not display logs correctly

</div>

In previous releases, the Migration Toolkit for Containers (MTC) UI did not display logs correctly. ([**BZ#2062266**](https://bugzilla.redhat.com/show_bug.cgi?id=2062266))

</div>

<div class="formalpara">

<div class="title">

StorageClass conversion plan adding migstorage reference in migplan

</div>

In previous releases, StorageClass conversion plans had a `migstorage` reference even though it was not being used. ([**BZ#2078459**](https://bugzilla.redhat.com/show_bug.cgi?id=2078459))

</div>

<div class="formalpara">

<div class="title">

Velero pod log missing from downloaded logs

</div>

In previous releases, when downloading a compressed (.zip) folder for all logs, the velero pod was missing. ([**BZ#2076599**](https://bugzilla.redhat.com/show_bug.cgi?id=2076599))

</div>

<div class="formalpara">

<div class="title">

Velero pod log missing from UI drop down

</div>

In previous releases, after a migration was performed, the velero pod log was not included in the logs provided in the dropdown list. ([**BZ#2076593**](https://bugzilla.redhat.com/show_bug.cgi?id=2076593))

</div>

<div class="formalpara">

<div class="title">

Rsync options logs not visible in log-reader pod

</div>

In previous releases, when trying to set any valid or invalid rsync options in the `migrationcontroller`, the log-reader was not showing any logs regarding the invalid options or about the rsync command being used. ([**BZ#2079252**](https://bugzilla.redhat.com/show_bug.cgi?id=2079252))

</div>

<div class="formalpara">

<div class="title">

Default CPU requests on Velero/Restic are too demanding and fail in certain environments

</div>

In previous releases, the default CPU requests on Velero/Restic were too demanding and fail in certain environments. Default CPU requests for Velero and Restic Pods are set to 500m. These values were high. ([**BZ#2088022**](https://bugzilla.redhat.com/show_bug.cgi?id=2088022))

</div>

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Updating the replication repository to a different storage provider type is not respected by the UI

</div>

After updating the replication repository to a different type and clicking **Update Repository**, it shows connection successful, but the UI is not updated with the correct details. When clicking on the **Edit** button again, it still shows the old replication repository information.

</div>

Furthermore, when trying to update the replication repository again, it still shows the old replication details. When selecting the new repository, it also shows all the information you entered previously and the **Update repository** is not enabled, as if there are no changes to be submitted. ([**BZ#2102020**](https://bugzilla.redhat.com/show_bug.cgi?id=2102020))

<div class="formalpara">

<div class="title">

Migrations fails because the backup is not found

</div>

Migration fails at the restore stage because of initial backup has not been found. ([**BZ#2104874**](https://bugzilla.redhat.com/show_bug.cgi?id=2104874))

</div>

<div class="formalpara">

<div class="title">

Update Cluster button is not enabled when updating Azure resource group

</div>

When updating the remote cluster, selecting the **Azure resource group** checkbox, and adding a resource group does not enable the **Update cluster** option. ([**BZ#2098594**](https://bugzilla.redhat.com/show_bug.cgi?id=2098594))

</div>

<div class="formalpara">

<div class="title">

Error pop-up in UI on deleting migstorage resource

</div>

When creating a `backupStorage` credential secret in OpenShift Container Platform, if the `migstorage` is removed from the UI, a 404 error is returned and the underlying secret is not removed. ([**BZ#2100828**](https://bugzilla.redhat.com/show_bug.cgi?id=2100828))

</div>

<div class="formalpara">

<div class="title">

Miganalytic resource displaying resource count as 0 in UI

</div>

After creating a migplan from backend, the Miganalytic resource displays the resource count as `0` in UI. ([**BZ#2102139**](https://bugzilla.redhat.com/show_bug.cgi?id=2102139))

</div>

<div class="formalpara">

<div class="title">

Registry validation fails when two trailing slashes are added to the Exposed route host to image registry

</div>

After adding two trailing slashes, meaning `//`, to the exposed registry route, the MigCluster resource is showing the status as `connected`. When creating a migplan from backend with DIM, the plans move to the `unready` status. ([**BZ#2104864**](https://bugzilla.redhat.com/show_bug.cgi?id=2104864))

</div>

<div class="formalpara">

<div class="title">

Service Account Token not visible while editing source cluster

</div>

When editing the source cluster that has been added and is in **Connected** state, in the UI, the service account token is not visible in the field. To save the wizard, you have to fetch the token again and provide details inside the field. ([**BZ#2097668**](https://bugzilla.redhat.com/show_bug.cgi?id=2097668))

</div>

# Migration Toolkit for Containers 1.7.1 release notes

## Resolved issues

There are no major resolved issues in this release.

## Known issues

This release has the following known issues:

<div class="formalpara">

<div class="title">

Incorrect DNS validation for destination namespace

</div>

MigPlan cannot be validated because the destination namespace starts with a non-alphabetic character. ([**BZ#2102231**](https://bugzilla.redhat.com/show_bug.cgi?id=2102231))

</div>

<div class="formalpara">

<div class="title">

Cloud propagation phase in migration controller is not functioning due to missing labels on Velero pods

</div>

The Cloud propagation phase in the migration controller is not functioning due to missing labels on Velero pods. The `EnsureCloudSecretPropagated` phase in the migration controller waits until replication repository secrets are propagated on both sides. As this label is missing on Velero pods, the phase is not functioning as expected. ([**BZ#2088026**](https://bugzilla.redhat.com/show_bug.cgi?id=2088026))

</div>

<div class="formalpara">

<div class="title">

Default CPU requests on Velero/Restic are too demanding when making scheduling fail in certain environments

</div>

Default CPU requests on Velero/Restic are too demanding when making scheduling fail in certain environments. Default CPU requests for Velero and Restic Pods are set to 500m. These values are high. The resources can be configured in DPA using the `podConfig` field for Velero and Restic. Migration operator should set CPU requests to a lower value, such as 100m, so that Velero and Restic pods can be scheduled in resource constrained environments Migration Toolkit for Containers (MTC) often operates in. ([**BZ#2088022**](https://bugzilla.redhat.com/show_bug.cgi?id=2088022))

</div>

<div class="formalpara">

<div class="title">

Warning is displayed on persistentVolumes page after editing storage class conversion plan

</div>

A warning is displayed on the **persistentVolumes** page after editing the storage class conversion plan. When editing the existing migration plan, a warning is displayed on the UI `At least one PVC must be selected for Storage Class Conversion`. ([**BZ#2079549**](https://bugzilla.redhat.com/show_bug.cgi?id=2079549))

</div>

<div class="formalpara">

<div class="title">

Velero pod log missing from downloaded logs

</div>

When downloading a compressed (.zip) folder for all logs, the velero pod is missing. ([**BZ#2076599**](https://bugzilla.redhat.com/show_bug.cgi?id=2076599))

</div>

<div class="formalpara">

<div class="title">

Velero pod log missing from UI drop down

</div>

After a migration is performed, the velero pod log is not included in the logs provided in the dropdown list. ([**BZ#2076593**](https://bugzilla.redhat.com/show_bug.cgi?id=2076593))

</div>

# Migration Toolkit for Containers 1.7.0 release notes

## New features and enhancements

This release has the following new features and enhancements:

- The Migration Toolkit for Containers (MTC) Operator now depends upon the OpenShift API for Data Protection (OADP) Operator. When you install the MTC Operator, the Operator Lifecycle Manager (OLM) automatically installs the OADP Operator in the same namespace.

- You can migrate from a source cluster that is behind a firewall to a cloud-based destination cluster by establishing a network tunnel between the two clusters by using the `crane tunnel-api` command.

- Converting storage classes in the MTC web console: You can convert the storage class of a persistent volume (PV) by migrating it within the same cluster.

## Known issues

This release has the following known issues:

- `MigPlan` custom resource does not display a warning when an AWS gp2 PVC has no available space. ([**BZ#1963927**](https://bugzilla.redhat.com/show_bug.cgi?id=1963927))

- Direct and indirect data transfers do not work if the destination storage is a PV that is dynamically provisioned by the AWS Elastic File System (EFS). This is due to limitations of the AWS EFS Container Storage Interface (CSI) driver. ([**BZ#2085097**](https://bugzilla.redhat.com/show_bug.cgi?id=2085097))

- Block storage for IBM Cloud must be in the same availability zone. See the [IBM FAQ for block storage for virtual private cloud](https://cloud.ibm.com/docs/vpc?topic=vpc-block-storage-vpc-faq).

- MTC 1.7.6 cannot migrate cron jobs from source clusters that support `v1beta1` cron jobs to clusters of OpenShift Container Platform 4.12 and later, which do not support `v1beta1` cron jobs. ([**BZ#2149119**](https://bugzilla.redhat.com/show_bug.cgi?id=2149119))
