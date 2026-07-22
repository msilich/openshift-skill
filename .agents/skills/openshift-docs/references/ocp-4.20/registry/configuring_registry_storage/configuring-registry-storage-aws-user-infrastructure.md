<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Save your container images to a durable storage location by configuring the built-in image registry to use dedicated AWS storage. This setup provides persistent scalable storage for your registry, separate from ephemeral cluster storage.

# Configuring a secret for the Image Registry Operator

In addition to the `configs.imageregistry.operator.openshift.io` and ConfigMap resources, configuration is provided to the Operator by a separate secret resource located within the `openshift-image-registry` namespace.

The `image-registry-private-configuration-user` secret provides credentials needed for storage access and management. It overrides the default credentials used by the Operator, if default credentials were found.

For S3 on AWS storage, the secret is expected to contain two keys:

- `REGISTRY_STORAGE_S3_ACCESSKEY`

- `REGISTRY_STORAGE_S3_SECRETKEY`

<div>

<div class="title">

Procedure

</div>

- Create an OpenShift Container Platform secret that contains the required keys.

  ``` terminal
  $ oc create secret generic image-registry-private-configuration-user --from-literal=REGISTRY_STORAGE_S3_ACCESSKEY=myaccesskey --from-literal=REGISTRY_STORAGE_S3_SECRETKEY=mysecretkey --namespace openshift-image-registry
  ```

</div>

# Configuring registry storage for AWS with user-provisioned infrastructure

During installation, your cloud credentials are sufficient to create an Amazon S3 bucket and the Registry Operator will automatically configure storage.

If the Registry Operator cannot create an S3 bucket and automatically configure storage, you can create an S3 bucket and configure storage with the following procedure.

> [!WARNING]
> To secure your registry images in AWS, [block public access](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-s3-bucket-publicaccessblockconfiguration.html) to the S3 bucket.

<div>

<div class="title">

Prerequisites

</div>

- You have a cluster on AWS with user-provisioned infrastructure.

- For Amazon S3 storage, the secret is expected to contain two keys:

  - `REGISTRY_STORAGE_S3_ACCESSKEY`

  - `REGISTRY_STORAGE_S3_SECRETKEY`

</div>

<div>

<div class="title">

Procedure

</div>

1.  Set up a [Bucket Lifecycle Policy](https://docs.aws.amazon.com/AmazonS3/latest/dev/mpuoverview.html#mpu-abort-incomplete-mpu-lifecycle-config) to abort incomplete multipart uploads that are one day old.

2.  Fill in the storage configuration in `configs.imageregistry.operator.openshift.io/cluster`:

    ``` terminal
    $ oc edit configs.imageregistry.operator.openshift.io/cluster
    ```

    <div class="formalpara">

    <div class="title">

    Example configuration

    </div>

    ``` yaml
    apiVersion: imageregistry.operator.openshift.io/v1
    kind: Config
    metadata:
      name: cluster
    spec:
      storage:
        s3:
          bucket: <bucket_name>
          region: <region_name>
    ```

    </div>

</div>

# Image Registry Operator configuration parameters for AWS S3

The following configuration parameters are available for AWS S3 registry storage.

The image registry `spec.storage.s3` configuration parameter holds the information to configure the registry to use the AWS S3 service for back-end storage. See the [S3 storage driver documentation](https://docs.docker.com/registry/storage-drivers/s3/) for more information.

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
<td style="text-align: left;"><p><code>bucket</code></p></td>
<td style="text-align: left;"><p>Bucket is the bucket name in which you want to store the registry’s data. It is optional and is generated if not provided.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>chunkSizeMiB</code></p></td>
<td style="text-align: left;"><p>ChunkSizeMiB is the size of the multipart upload chunks of the S3 API. The default is <code>10</code> MiB with a minimum of <code>5</code> MiB.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>region</code></p></td>
<td style="text-align: left;"><p>Region is the AWS region in which your bucket exists. It is optional and is set based on the installed AWS Region.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>regionEndpoint</code></p></td>
<td style="text-align: left;"><p>RegionEndpoint is the endpoint for S3 compatible storage services. It is optional and defaults based on the Region that is provided.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>virtualHostedStyle</code></p></td>
<td style="text-align: left;"><p>VirtualHostedStyle enables using S3 virtual hosted style bucket paths with a custom RegionEndpoint. It is optional and defaults to false.</p>
<p>Set this parameter to deploy OpenShift Container Platform to hidden regions.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>encrypt</code></p></td>
<td style="text-align: left;"><p>Encrypt specifies whether or not the registry stores the image in encrypted format. It is optional and defaults to false.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>keyID</code></p></td>
<td style="text-align: left;"><p>KeyID is the KMS key ID to use for encryption. It is optional. Encrypt must be true, or this parameter is ignored.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>cloudFront</code></p></td>
<td style="text-align: left;"><p>CloudFront configures Amazon Cloudfront as the storage middleware in a registry. It is optional.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>trustedCA</code></p></td>
<td style="text-align: left;"><p>The namespace for the config map referenced by <code>trustedCA</code> is <code>openshift-config</code>. The key for the bundle in the config map is <code>ca-bundle.crt</code>. It is optional.</p></td>
</tr>
</tbody>
</table>

> [!NOTE]
> When the value of the `regionEndpoint` parameter is configured to a URL of a Rados Gateway, an explicit port must not be specified. For example:
>
> ``` yaml
> regionEndpoint: http://rook-ceph-rgw-ocs-storagecluster-cephobjectstore.openshift-storage.svc.cluster.local
> ```
