<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure the Cluster Samples Operator to manage the installation and updates of Red Hat Enterprise Linux (RHEL)-based OpenShift Container Platform image streams and templates in the `openshift` namespace.

<div class="important">

<div class="title">

</div>

- The Cluster Samples Operator is deprecated. No new templates, samples, or non-Source-to-Image (Non-S2I) image streams are added to the Cluster Samples Operator. However, the existing S2I builder image streams and templates will continue to receive updates until the Cluster Samples Operator is removed in a future release. S2I image streams and templates include:

  - Ruby

  - Python

  - Node.js

  - Perl

  - PHP

  - HTTPD

  - Nginx

  - EAP

  - Java

  - Webserver

  - .NET

  - Go

- The Cluster Samples Operator will stop managing and providing support to the non-S2I samples (image streams and templates). You can contact the image stream or template owner for any requirements and future plans. In addition, refer to the following link:

  - [List of the repositories hosting the image stream or templates](https://github.com/openshift/library/blob/master/official.yaml)

</div>

# Understanding the Cluster Samples Operator

During installation, the Operator creates the default configuration object for itself and then creates the sample image streams and templates, including quick start templates.

> [!NOTE]
> To facilitate image stream imports from other registries that require credentials, a cluster administrator can create any additional secrets that contain the content of a Docker `config.json` file in the `openshift` namespace needed for image import.

The Cluster Samples Operator configuration is a cluster-wide resource. The deployment of the Operator is within the `openshift-cluster-samples-operator` namespace.

The image for the Cluster Samples Operator has image stream and template definitions for the associated OpenShift Container Platform release. When each sample is created or updated, the Cluster Samples Operator includes an annotation that denotes the version of OpenShift Container Platform. The Operator uses this annotation to ensure that each sample matches the release version. Samples outside of its inventory are ignored, as are skipped samples. Modifications to any samples that are managed by the Operator, where that version annotation is modified or deleted, are reverted automatically.

> [!NOTE]
> The Jenkins images are part of the image payload from installation and are tagged into the image streams directly.

The Cluster Samples Operator configuration resource includes a finalizer which cleans up the following upon deletion:

- Operator managed image streams.

- Operator managed templates.

- Operator generated configuration resources.

- Cluster status resources.

Upon deletion of the samples resource, the Cluster Samples Operator recreates the resource by using the default configuration.

If the Cluster Samples Operator is removed during installation, you can use the Cluster Samples Operator with an alternate registry so that content can be imported. Then you can set the Cluster Samples Operator to `Managed` to get the samples. Use the following instructions:

- [Using the Cluster Samples Operator with an alternate registry](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/samples-operator-alt-registry)

For more information about configuring credentials, see the following link:

- [Using image pull secrets](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/managing-images#using-image-pull-secrets)

# Cluster Samples Operator use of management state

The Cluster Samples Operator is bootstrapped as `Managed` by default or if global proxy is configured.

In the `Managed` state, the Cluster Samples Operator is actively managing its resources and keeping the component active to pull sample image streams and images from the registry and ensure that the requisite sample templates are installed.

Certain circumstances result in the Cluster Samples Operator bootstrapping itself as `Removed` including:

- If the Cluster Samples Operator cannot reach the registry after three minutes on initial startup after a clean installation.

- If the Cluster Samples Operator detects that it is on an IPv6 network.

- If the image controller configuration parameters prevent the creation of image streams by using the default image registry, or by using the image registry specified by `samplesRegistry` setting. For more information, see the following links:

  - [Image controller configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/image-configuration-classic#images-configuration-parameters_image-configuration)

  - [Cluster Samples Operator configuration parameters](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/configuring-samples-operator#samples-operator-configuration_configuring-samples-operator)

> [!NOTE]
> For OpenShift Container Platform, the default image registry is `registry.redhat.io`.

However, if the Cluster Samples Operator detects that it is on an IPv6 network and an OpenShift Container Platform global proxy is configured, then the IPv6 check supersedes all the checks. As a result, the Cluster Samples Operator bootstraps itself as `Removed`.

> [!IMPORTANT]
> IPv6 installations are not currently supported by the registry. The Cluster Samples Operator pulls most of the sample image streams and images from the registry.

## Restricted network installation

The Cluster Samples Operator boostrapping itself as `Removed` when unable to access `registry.redhat.io` facilitates restricted network installations when the network restriction is already in place.

As a cluster administrator, you have more time to decide if samples are needed when the Operator is boostrapped `Removed`. This is because the Cluster Samples Operator does not submit alerts that sample image stream imports are failing when the management state is `Removed`. When the Cluster Samples Operator management state is `Managed`, and the Operator attempts to install sample image streams, failing-import alerts start two hours after initial installation.

## Restricted network installation with initial network access

If a cluster that eventually runs on a restricted network is first installed while network access exists, the Cluster Samples Operator installs content from `registry.redhat.io`.

In this case, you can defer samples installation until you have decided which samples are needed by overriding the default configuration of `Managed` for a connected installation.

If you want the Cluster Samples Operator to bootstrap with the management state as `Removed` during an installation that has initial network access, override the Cluster Samples Operator default configuration by using the following instructions:

- [Customizing nodes](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/installation_configuration/installing-customizing)

To host samples in your restricted environment, use the following instructions:

- [Using the Cluster Samples Operator with an alternate registry](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/images/samples-operator-alt-registry)

You must also put the following additional YAML file in the `openshift` directory created by the `openshift-install create manifest` process:

<div class="formalpara">

<div class="title">

Example Cluster Samples Operator YAML file with `managementState: Removed`

</div>

``` yaml
apiVersion: samples.operator.openshift.io/v1
kind: Config
metadata:
  name: cluster
spec:
  architectures:
  - x86_64
  managementState: Removed
```

</div>

# Cluster Samples Operator tracking and error recovery of image stream imports

After creation or update of a samples image stream, the Cluster Samples Operator monitors the progress of each image stream tag’s image import.

If an import fails, the Cluster Samples Operator retries the import through the image stream image import API at a rate of about every 15 minutes until either one of the following occurs:

- The import succeeds.

- The Cluster Samples Operator configuration is changed such that either the image stream is added to the `skippedImagestreams` list, or the management state is changed to `Removed`.

## Cluster Samples Operator assistance for mirroring

During installation, OpenShift Container Platform creates a config map named `imagestreamtag-to-image` in the `openshift-cluster-samples-operator` namespace.

The `imagestreamtag-to-image` config map contains an entry, the populating image, for each image stream tag.

The format of the key for each entry in the data field in the config map is `<image_stream_name>_<image_stream_tag_name>`.

During a disconnected installation of OpenShift Container Platform, the status of the Cluster Samples Operator is set to `Removed`. If you choose to change it to `Managed`, it installs samples.

> [!NOTE]
> The use of samples in a network-restricted or discontinued environment might require access to services external to your network. Some example services include: Github, Maven Central, npm, RubyGems, PyPi and others. There might be additional steps to take that allow the Cluster Samples Operators objects to reach the services they require.

Use the following principles to determine which images you need to mirror for your image streams to import:

- While the Cluster Samples Operator is set to `Removed`, you can create your mirrored registry, or determine which existing mirrored registry you want to use.

- Mirror the samples you want to the mirrored registry using the new config map as your guide.

- Add any of the image streams you did not mirror to the `skippedImagestreams` list of the Cluster Samples Operator configuration object.

- Set `samplesRegistry` of the Cluster Samples Operator configuration object to the mirrored registry.

- Then set the Cluster Samples Operator to `Managed` to install the image streams you have mirrored.

# Cluster Samples Operator configuration parameters

The samples resource offers the following configuration fields:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>managementState</code></p></td>
<td style="text-align: left;"><p><code>Managed</code>: The Cluster Samples Operator updates the samples as the configuration dictates.</p>
<p><code>Unmanaged</code>: The Cluster Samples Operator ignores updates to its configuration resource object and any image streams or templates in the <code>openshift</code> namespace.</p>
<p><code>Removed</code>: The Cluster Samples Operator removes the set of <code>Managed</code> image streams and templates in the <code>openshift</code> namespace. It ignores new samples created by the cluster administrator or any samples in the skipped lists. After the removals are complete, the Cluster Samples Operator works like it is in the <code>Unmanaged</code> state and ignores any watch events on the sample resources, image streams, or templates.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>samplesRegistry</code></p></td>
<td style="text-align: left;"><p>Allows you to specify which registry is accessed by image streams for their image content. <code>samplesRegistry</code> defaults to <code>registry.redhat.io</code> for OpenShift Container Platform.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Creation or update of RHEL content does not commence if the secret for pull access is not in place when either <code>Samples Registry</code> is not explicitly set, leaving an empty string, or when it is set to registry.redhat.io. In both cases, image imports work off of registry.redhat.io, which requires credentials.</p>
<p>Creation or update of RHEL content is not gated by the existence of the pull secret if the <code>Samples Registry</code> is overridden to a value other than the empty string or registry.redhat.io.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>architectures</code></p></td>
<td style="text-align: left;"><p>Placeholder to choose an architecture type.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>skippedImagestreams</code></p></td>
<td style="text-align: left;"><p>Image streams that are in the Cluster Samples Operator’s inventory but that the cluster administrator wants the Operator to ignore or not manage. You can add a list of image stream names to this parameter. For example, <code>["httpd","perl"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>skippedTemplates</code></p></td>
<td style="text-align: left;"><p>Templates that are in the Cluster Samples Operator’s inventory, but that the cluster administrator wants the Operator to ignore or not manage.</p></td>
</tr>
</tbody>
</table>

Secret, image stream, and template watch events can come in before the initial samples resource object is created, the Cluster Samples Operator detects and re-queues the event.

## Configuration restrictions

When the Cluster Samples Operator starts supporting multiple architectures, you cannot change the architecture list while the Operator is in the `Managed` state.

To change the architectures values, a cluster administrator must:

- Mark the `Management State` as `Removed`, saving the change.

- In a subsequent change, edit the architecture and change the `Management State` back to `Managed`.

The Cluster Samples Operator still processes secrets while in `Removed` state. You can create the secret before switching to `Removed`, while in `Removed` before switching to `Managed`, or after switching to `Managed` state. There are delays in creating the samples until the secret event is processed if you create the secret after switching to `Managed`. This helps facilitate the changing of the registry, where you choose to remove all the samples before switching to ensure a clean slate. Removing all samples before switching is not required.

## Samples resource conditions

The samples resource maintains the following conditions in its status:

<table>
<colgroup>
<col style="width: 27%" />
<col style="width: 72%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Condition</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>SamplesExists</code></p></td>
<td style="text-align: left;"><p>Indicates the samples are created in the <code>openshift</code> namespace.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ImageChangesInProgress</code></p></td>
<td style="text-align: left;"><p><code>True</code> when image streams are created or updated, but not all of the tag spec generations and tag status generations match.</p>
<p><code>False</code> when all of the generations match, or unrecoverable errors occurred during import, the last seen error is in the message field. The list of pending image streams is in the reason field.</p>
<p>This condition is deprecated in OpenShift Container Platform.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ConfigurationValid</code></p></td>
<td style="text-align: left;"><p><code>True</code> or <code>False</code> based on whether any of the restricted changes noted previously are submitted.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>RemovePending</code></p></td>
<td style="text-align: left;"><p>Indicator that there is a <code>Management State: Removed</code> setting pending, but the Cluster Samples Operator is waiting for the deletions to complete.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ImportImageErrorsExist</code></p></td>
<td style="text-align: left;"><p>Indicator of which image streams had errors during the image import phase for one of their tags.</p>
<p><code>True</code> when an error has occurred. The list of image streams with an error is in the reason field. The details of each error reported are in the message field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>MigrationInProgress</code></p></td>
<td style="text-align: left;"><p><code>True</code> when the Cluster Samples Operator detects that the version is different from the Cluster Samples Operator version with which the current samples set are installed.</p>
<p>This condition is deprecated in OpenShift Container Platform.</p></td>
</tr>
</tbody>
</table>

# Accessing the Cluster Samples Operator configuration

You can configure the Cluster Samples Operator by editing the file with the provided parameters.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Access the Cluster Samples Operator configuration by running the following command:

  ``` terminal
  $ oc edit configs.samples.operator.openshift.io/cluster
  ```

  The Cluster Samples Operator configuration resembles the following example:

  ``` yaml
  apiVersion: samples.operator.openshift.io/v1
  kind: Config
  # ...
  ```

</div>

# Removing deprecated image stream tags from the Cluster Samples Operator

The Cluster Samples Operator leaves deprecated image stream tags in an image stream because users can have deployments that use the deprecated image stream tags.

You can remove deprecated image stream tags by editing the image stream with the `oc tag` command.

> [!NOTE]
> Deprecated image stream tags that the samples providers have removed from their image streams are not included on initial installations.

<div>

<div class="title">

Prerequisites

</div>

- You installed the OpenShift CLI (`oc`).

</div>

<div>

<div class="title">

Procedure

</div>

- Remove deprecated image stream tags by editing the image stream with the following `oc tag` command:

  ``` terminal
  $ oc tag -d <image_stream_name:tag>
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  Deleted tag default/<image_stream_name:tag>.
  ```

  </div>

</div>
