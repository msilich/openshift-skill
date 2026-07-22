<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

If you use a firewall, you must configure your allowlist for the firewall to ensure OpenShift Container Platform has access to the URLs it requires to pull container images and access Red Hat services. Additional URLs are required for features such as Telemetry, Red Hat Lightspeed, cloud provider integrations, or certain build strategies.

# Configuring your firewall for OpenShift Container Platform

Before you install OpenShift Container Platform, you must configure your firewall to grant access to the sites that OpenShift Container Platform requires.

There are no special configuration considerations for services running on only controller nodes compared to compute nodes.

> [!NOTE]
> If your environment has a dedicated load balancer in front of your OpenShift Container Platform cluster, review the allowlists between your firewall and load balancer to prevent unwanted network restrictions to your cluster.

<div>

<div class="title">

Procedure

</div>

1.  Allowlist the following container registry URLs for cluster installation and upgrades:

    | URL | Port | Function |
    |----|----|----|
    | `registry.redhat.io` | 443 | Provides core container images |
    | `access.redhat.com` | 443 | Hosts a signature store that a container client requires for verifying images pulled from `registry.access.redhat.com`. In a firewall environment, ensure that this resource is on the allowlist. |
    | `registry.access.redhat.com` | 443 | Hosts all the container images that are stored on the Red Hat Ecosystem Catalog, including core container images. |
    | `quay.io` | 443 | Provides core container images |
    | `cdn.quay.io` | 443 | Provides core container images |
    | `cdn01.quay.io` | 443 | Provides core container images |
    | `cdn02.quay.io` | 443 | Provides core container images |
    | `cdn03.quay.io` | 443 | Provides core container images |
    | `cdn04.quay.io` | 443 | Provides core container images |
    | `cdn05.quay.io` | 443 | Provides core container images |
    | `cdn06.quay.io` | 443 | Provides core container images |
    | `icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |
    | `cp.icr.io` | 443 | Provides IBM Cloud Pak container images. This domain is only required if you use IBM Cloud Paks. |

    - You can use the wildcard `*.quay.io` instead of `cdn.quay.io` and `cdn0[1-6].quay.io` in your allowlist.

    - You can use the wildcard `*.access.redhat.com` to simplify the configuration and ensure that all subdomains, including `registry.access.redhat.com`, are allowed.

    - When adding a site such as `quay.io` to your allowlist, do not add a wildcard entry such as `*.quay.io` to your denylist. In most cases, image registries use a content delivery network (CDN) to serve images. If a firewall blocks access, image downloads are denied when the initial download request redirects to a hostname such as `cdn01.quay.io`.

2.  Allowlist the following URLs to enable cluster access, authentication, and updates:

    | URL | Port | Function |
    |----|----|----|
    | `*.apps.<cluster_name>.<base_domain>` | 443 | Allowlist these URLs to enable cluster access, authentication, and updates. |
    | `api.openshift.com` | 443 | API endpoint for cluster tokens and update checks. |
    | `console.redhat.com` | 443 | Authentication service for cluster tokens. |
    | `sso.redhat.com` | 443 | The `https://console.redhat.com` site uses authentication from `sso.redhat.com` |

    For egress traffic, Operators require route access to perform health checks to establish a connection for reaching endpoints. The authentication and web console Operators connect to two routes to verify functionality. Cluster administrators who do not want to allow `*.apps.<cluster_name>.<base_domain>`, must allow the following routes:

    - `oauth-openshift.apps.<cluster_name>.<base_domain>`

    - `canary-openshift-ingress-canary.apps.<cluster_name>.<base_domain>`

    - `console-openshift-console.apps.<cluster_name>.<base_domain>`, or the hostname that is specified in the `spec.route.hostname` field of the `consoles.operator/cluster` object if the field is not empty.

3.  Allowlist the following registry URLs that host related artifacts for cluster installation and upgrades, such as installation content, release images, and client tools:

    | URL | Port | Function |
    |----|----|----|
    | `mirror.openshift.com` | 443 | Required to access mirrored installation content and images. This site is also a source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |
    | `quayio-production-s3.s3.amazonaws.com` | 443 | Required to access Quay image content in AWS. |
    | `rhcos.mirror.openshift.com` | 443 | Required to download Red Hat Enterprise Linux CoreOS (RHCOS) images. |
    | `storage.googleapis.com/openshift-release` | 443 | A source of release image signatures, although the Cluster Version Operator needs only a single functioning source. |

4.  Set your firewall’s allowlist to include any site that provides resources for a language or framework that your builds require.

5.  If you do not disable Telemetry, you must grant access to the following URLs to access Telemetry and Red Hat Lightspeed:

    | URL | Port | Function |
    |----|----|----|
    | `cert-api.access.redhat.com` | 443 | Required for Telemetry |
    | `api.access.redhat.com` | 443 | Required for Telemetry |
    | `infogw.api.openshift.com` | 443 | Required for Telemetry |
    | `console.redhat.com` | 443 | Required for Telemetry and for `insights-operator` |

6.  If you use Alibaba Cloud, Amazon Web Services (AWS), Microsoft Azure, or Google Cloud to host your cluster, you must grant access to the URLs that offer the cloud provider API and DNS for that cloud:

    <table>
    <colgroup>
    <col style="width: 10%" />
    <col style="width: 40%" />
    <col style="width: 10%" />
    <col style="width: 40%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Cloud</th>
    <th style="text-align: left;">URL</th>
    <th style="text-align: left;">Port</th>
    <th style="text-align: left;">Function</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Alibaba</p></td>
    <td style="text-align: left;"><p><code>*.aliyuncs.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Alibaba Cloud services and resources. Review the <a href="https://github.com/aliyun/alibaba-cloud-sdk-go/blob/master/sdk/endpoints/endpoints_config.go?spm=a2c4g.11186623.0.0.47875873ciGnC8&amp;file=endpoints_config.go">Alibaba endpoints_config.go file</a> to find the exact endpoints to allow for the regions that you use.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>AWS</p></td>
    <td style="text-align: left;"><p><code>aws.amazon.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.amazonaws.com</code></p>
    <p>Alternatively, if you choose to not use a wildcard for AWS APIs, you must include the following URLs in your allowlist:</p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access AWS services and resources. Review the <a href="https://docs.aws.amazon.com/general/latest/gr/rande.html">AWS Service Endpoints</a> in the AWS documentation to find the exact endpoints to allow for the regions that you use.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>ec2.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>events.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>iam.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>route53.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.s3.dualstack.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>sts.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>sts.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>tagging.us-east-1.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment. This endpoint is always <code>us-east-1</code>, regardless of the region the cluster is deployed in.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>ec2.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>elasticloadbalancing.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to install and manage clusters in an AWS environment.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>servicequotas.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required. Used to confirm quotas for deploying the service.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>tagging.&lt;aws_region&gt;.amazonaws.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Allows the assignment of metadata about AWS resources in the form of tags.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.cloudfront.net</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Used to provide access to CloudFront. If you use the AWS Security Token Service (STS) and the private S3 bucket, you must provide access to CloudFront.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>GCP</p></td>
    <td style="text-align: left;"><p><code>*.googleapis.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Google Cloud services and resources. Review <a href="https://cloud.google.com/endpoints/">Cloud Endpoints</a> in the Google Cloud documentation to find the endpoints to allow for your APIs.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>accounts.google.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access your Google Cloud account.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Microsoft Azure</p></td>
    <td style="text-align: left;"><p><code>management.azure.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Microsoft Azure services and resources. Review the <a href="https://docs.microsoft.com/en-us/rest/api/azure/">Microsoft Azure REST API reference</a> in the Microsoft Azure documentation to find the endpoints to allow for your APIs.</p></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>*.blob.core.windows.net</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to download Ignition files.</p></td>
    <td></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p><code>login.microsoftonline.com</code></p></td>
    <td style="text-align: left;"><p>443</p></td>
    <td style="text-align: left;"><p>Required to access Microsoft Azure services and resources. Review the <a href="https://docs.microsoft.com/en-us/rest/api/azure/">Azure REST API reference</a> in the Microsoft Azure documentation to find the endpoints to allow for your APIs.</p></td>
    <td></td>
    </tr>
    </tbody>
    </table>

7.  Allowlist the following URL for optional third-party content:

    | URL | Port | Function |
    |----|----|----|
    | `registry.connect.redhat.com` | 443 | Required for all third-party images and certified operators. |

8.  If you use a default Red Hat Network Time Protocol (NTP) server, allow the following URLs. NTP operates on User Datagram Protocol (UDP) port 123, so this port must be opened on the firewall.

    | URL                   | Port | Function                                        |
    |-----------------------|------|-------------------------------------------------|
    | `1.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |
    | `2.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |
    | `3.rhel.pool.ntp.org` | 123  | Provides NTP services for time synchronization. |

    > [!NOTE]
    > If you do not use a default Red Hat NTP server, verify the NTP server for your platform and allow it in your firewall.

</div>

<div>

<div class="title">

Additional resources

</div>

- [OpenID Connect requirements for AWS STS](../../authentication/managing_cloud_provider_credentials/cco-short-term-creds.md#cco-short-term-creds-auth-flow-aws-oidc_cco-short-term-creds)

</div>

# OpenShift Container Platform network flow matrix

You can use the information in the appropriate network flow matrix to manage ingress traffic for your specific environment. You can restrict ingress traffic to essential flows to improve network security.

The following network flow matrixes describe the ingress flows to OpenShift Container Platform services for the following environments:

- OpenShift Container Platform on bare metal

- Single-node OpenShift with other platforms

- OpenShift Container Platform on Amazon Web Services (AWS)

- Single-node OpenShift on AWS

Use the information in the appropriate network flow matrix to help you manage ingress traffic for your specific environment. You can restrict ingress traffic to essential flows to improve network security.

Additionally, consider the following dynamic port ranges when managing ingress traffic for both bare metal and cloud environments:

- `9000-9999`: Reserved for internal OpenShift Container Platform components. Do not assign user workloads or services to ports in this range.

- `30000-32767`: Kubernetes `NodePort` service ports. These ports are required only if you expose services by using the `NodePort` service type. If `NodePort` services are not used, you can block this port range.

To view or download the complete raw CSV content for an environment, see the following resources:

- [OpenShift Container Platform on bare metal](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/raw/bm.csv)

- [Single-node OpenShift with other platforms](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/raw/none-sno.csv)

- [OpenShift Container Platform on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/raw/aws.csv)

- [Single-node OpenShift on AWS](https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/raw/aws-sno.csv)

> [!NOTE]
> The network flow matrixes describe ingress traffic flows for a base OpenShift Container Platform or single-node OpenShift installation. The matrixes do not apply for hosted control planes, Red Hat build of MicroShift, or standalone clusters.

## Base network flows

The following matrixes describe the base ingress flows to OpenShift Container Platform services.

> [!NOTE]
> For base ingress flows to single-node OpenShift clusters, see the *Control plane node base flows* matrix only.

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/common-master.csv> |
|----|

Control plane node base flows {#network-flow-matrix-control_configuring-firewall}

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/common-worker.csv> |
|----|

Worker node base flows {#network-flow-matrix-worker_configuring-firewall}

## Additional network flows for OpenShift Container Platform on bare metal

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on bare metal.

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/bm.csv> |
|----|

OpenShift Container Platform on bare metal

## Additional network flows for single-node OpenShift with other platforms

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift configured with `platform: none` in the installation manifest.

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/none-sno.csv> |
|----|

Single-node OpenShift with other platforms

## Additional network flows for OpenShift Container Platform on AWS

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to OpenShift Container Platform on AWS.

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/aws.csv> |
|----|

OpenShift Container Platform on AWS

## Additional network flows for single-node OpenShift on AWS

In addition to the base network flows, the following matrix describes the ingress flows to OpenShift Container Platform services that are specific to single-node OpenShift on AWS.

| <https://raw.githubusercontent.com/openshift-kni/commatrix/release-4.20/docs/stable/unique/aws-sno.csv> |
|----|

Single-node OpenShift on AWS
