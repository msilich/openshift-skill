<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The **Vulnerability Management** functions provide methods to view and manage vulnerabilities discovered by RHACS. Common vulnerability management tasks involve identifying and prioritizing vulnerabilities, remedying them, and monitoring for new threats.

For information about the sources used for identifying vulnerabilities, see [Vulnerability data sources](../../architecture/acs-architecture.md#con-vuln-sources_acs-architecture).

Historically, RHACS provided a view of vulnerabilities discovered in your system in the vulnerability management dashboard. The dashboard is deprecated in RHACS 4.5 and will be removed in a future release.

For more information about the dashboard, see [Using the vulnerability management dashboard](vulnerability-management-dashboard.md).

Currently, vulnerability information is provided in pages that are accessed by selecting **Vulnerability Management** → **Results**. You can select different views based on whether you want to view vulnerabilities discovered in your workloads, vulnerabilities discovered in platform components, such as OpenShift, or node vulnerabilities. Depending on the view, you can filter results based on specific criteria: for example, you can display vulnerabilities of different severity, vulnerabilities in deployments with specific annotations, or vulnerabilities in images that are based on a specific operating system.

<a id="vuln-management-components-portal_common-vuln-management-tasks"></a>

# Viewing vulnerability management data in the RHACS portal

Beginning with release 4.7, RHACS has reorganized data for vulnerabilities it discovers and separated vulnerability data by category, such as vulnerabilities in user workloads and nodes, and platform vulnerabilities.

In the **Vulnerability Management** menu, the **Results** page provides vulnerability data. You can view vulnerability data by category by clicking the tabs at the top of the page. The tabs include the following categories:

User workloads  
This tab provides information about vulnerabilities that affect workloads and images in your system that you have deployed. Because these workloads are deployed and managed by you, they are called *user workloads*.

Platform  
This tab provides information about vulnerabilities that RHACS identifies as related to the *platform*, for example, vulnerabilities in workloads and images that the OpenShift platform and layered services deploy. RHACS uses a regular expression pattern to examine the namespaces of workloads and identify workloads that belong to platform components. For example, currently, RHACS identifies vulnerabilities in the following namespaces as belonging to the platform:

- OpenShift Container Platform: Namespace starts with `openshift-` or `kube-`

- Layered products:

  - Namespace starts with rhacs-operator

  - Namespace starts with open-cluster-management

  - Namespace is `stackrox`, `multicluster-engine`, `aap`, or `hive`

- Third-party partners: Namespace is `nvidia-gpu-operator`

Nodes  
This tab provides a view of vulnerabilities across nodes, including user-managed and platform workloads and images.

Virtual machines  
This tab displays all virtual machines (VMs) and vulnerabilities discovered for them.

More views  
This menu provides access to additional ways to view vulnerability information, including the following views:

- All vulnerable images

- Inactive images

- Images without CVEs

- Kubernetes components

<a id="vulnerability-management20-view-workload-cve_common-vuln-management-tasks"></a>

## Viewing user workload vulnerabilities

In the **Vulnerability Management** → **Results** page, you can get information about the vulnerabilities in applications running on clusters in your system. With this information, you can prioritize and manage vulnerabilities across images and deployments.

In the **User workload vulnerabilities** page, you can view images and deployments with vulnerabilities and filter by image, deployment, namespace, cluster, CVE, component, and component source.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Select the **User Workloads** tab. By default, the **Observed** tab is selected.

3.  Optional: You can choose to view observed vulnerabilities or those that have been deferred or marked as false positives. Click one of the following tabs:

    - **Observed**: Lists vulnerabilities that RHACS observed in your user workloads.

    - **Deferred**: Lists vulnerabilities that have been observed but had a deferral request submitted and approved in the exception management workflow.

    - **False positives**: Lists vulnerabilities that have been observed but were identified as false positives in the exception management workflow.

4.  Optional: You can select the following options to refine the list of results:

    - **Prioritize by namespace view**: Displays a list of namespaces sorted according to the risk priority. You can use this view to quickly identify and address the most critical areas. In this view, click **\<number\> deployments** in a table row to return to the vulnerability findings view, with filters applied to show only deployments for the selected namespace.

    - **Default filters**: You can select filters for CVE severity and CVE status that are automatically applied across all views on this page. These filters are applied when you visit the page from another section of the RHACS web portal or from a bookmarked URL. They are saved in the local storage of your browser.

5.  To filter the list of results by entity, for example, to search for a specific named CVE, select the appropriate filters and attributes.

    To select multiple entities and attributes, click the right arrow icon to add another criteria. Depending on your choices, enter the appropriate information such as text, or select a date or object.

    The filter entities and attributes are listed in the following table.

    > [!NOTE]
    > The **Filtered view** icon indicates that the displayed results were filtered based on the criteria that you selected. You can click **Clear filters** to remove all filters, or remove individual filters by clicking on them.

    <table>
    <caption>Filter options</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Entity</th>
    <th style="text-align: left;">Attributes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Image</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image.</p></li>
    <li><p><strong>Operating system</strong>: The operating system of the image.</p></li>
    <li><p><strong>Tag</strong>: The tag for the image.</p></li>
    <li><p><strong>Label</strong>: The label for the image.</p></li>
    <li><p><strong>Registry</strong>: The registry where the image is located.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>CVE</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the CVE.</p></li>
    <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
    <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
    <p>The following values are associated with the severity level for the CVE:</p>
    <ul>
    <li><p><strong>is greater than</strong></p></li>
    <li><p><strong>is greater than or equal to</strong></p></li>
    <li><p><strong>is equal to</strong></p></li>
    <li><p><strong>is less than or equal to</strong></p></li>
    <li><p><strong>is less than</strong></p></li>
    </ul></li>
    <li><p><strong>EPSS probability</strong>: The likelihood that the vulnerability could be exploited according to the <a href="https://www.first.org/epss/">Exploit Prediction Scoring System (EPSS)</a>. This EPSS data provides a percentage estimate of the probability that exploitation of this vulnerability will be observed in the next 30 days. The EPSS collects data of observed exploitation activity from partners, and exploitation activity does not mean that an attempted exploitation was successful. The EPSS score should be used as a single data point <em>along with other information</em>, such as the age of the CVE, to help you prioritize the vulnerabilities to address. For more information, see <a href="https://access.redhat.com/articles/7106599">RHACS and EPSS</a>.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Image Component</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image component, for example, <code>activerecord-sql-server-adapter</code></p></li>
    <li><p><strong>Source</strong>:</p>
    <ul>
    <li><p>OS</p></li>
    <li><p>Python</p></li>
    <li><p>Java</p></li>
    <li><p>Ruby</p></li>
    <li><p>Node.js</p></li>
    <li><p>Go</p></li>
    <li><p>Dotnet Core Runtime</p></li>
    <li><p>Infrastructure</p></li>
    </ul></li>
    <li><p><strong>Version</strong>: Version of the image component; for example, <code>3.4.21</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
    <li><p><strong>Layer type</strong>: Indicates whether the layer belongs to the application or the base image. Base image layers are shown only for images that are detected as being built from known base images. These base images are configured under <strong>Platform Configuration</strong> → <strong>Base Images</strong>.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Deployment</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: Name of the deployment.</p></li>
    <li><p><strong>Label</strong>: Label for the deployment.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the deployment.</p></li>
    <li><p><strong>Status</strong>: Whether the deployment is inactive or active.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Namespace</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The <code>metadata.uid</code> of the namespace that is created by Kubernetes.</p></li>
    <li><p><strong>Name</strong>: The name of the namespace.</p></li>
    <li><p><strong>Label</strong>: The label for the namespace.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the namespace.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Cluster</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
    <li><p><strong>Name</strong>: The name of the cluster.</p></li>
    <li><p><strong>Label</strong>: The label for the cluster.</p></li>
    <li><p><strong>Type</strong>: The cluster type, for example, OCP.</p></li>
    <li><p><strong>Platform type</strong>: The platform type, for example, OpenShift 4 cluster.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    - **CVE severity**: You can select one or more levels.

    - **CVE status**: You can select **Fixable** or **Not fixable**.

6.  Click one of the following tabs to view the data that you want:

    - **\<number\> CVEs**: Displays vulnerabilities organized by CVE

    - **\<number\> Images**: Displays images that contain discovered vulnerabilities.

    - **\<number\> Deployments**: Displays deployments that contain discovered vulnerabilities.

7.  Optional: Choose the appropriate method to view the component and advisory data associated with a CVE:

    - To view the component and advisory data associated with a CVE from the list of CVEs, complete the following steps:

      1.  Click the **\<number\> CVEs** tab.

      2.  In the list of CVEs, click a CVE to do any of the following tasks:

          - To view the component and advisory data associated with an image:

            1.  Click the **\<number\> Images** tab.

            2.  Expand the image.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

          - To view the component and advisory data associated with a deployment:

            1.  Click the **\<number\> Deployments** tab.

            2.  Expand the deployment.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of images, complete the following steps:

      1.  Click the **\<number\> Images** tab.

      2.  In the list of images, click an image.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of deployments, complete the following steps:

      1.  Click the **\<number\> Deployments** tab.

      2.  In the list of deployments, click a deployment.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

8.  Optional: Choose the appropriate method to re-organize the information in the **User Workloads** tab:

    - To sort the table in ascending or descending order, select a column heading.

    - To select the categories that you want to display in the table, perform the following steps:

      1.  Click **Columns**.

      2.  Choose the appropriate method to manage the columns:

          - To view all the categories, click **Select all**.

          - To reset to the default categories, click **Reset to default**.

          - To view only the selected categories, select the one or more categories that you want to view, and then click **Save**.

9.  In the list of results, click a CVE, image name, or deployment name to view more information about the item. For example, depending on the item type, you can view the following information:

    - Whether a CVE is fixable

    - Whether an image is active

    - The Dockerfile line in the image that contains the CVE

    - External links to information about the CVE in Red Hat and other CVE databases

</div>

<a id="vulnerability-management20-view-platform-cve_vulns-platforms"></a>

## Viewing platform vulnerabilities

The **Platform vulnerabilities** page provides information about vulnerabilities that RHACS identifies as related to the *platform*, for example, vulnerabilities in workloads and images that are used by the OpenShift Platform and layered services.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Select the **Platform** tab. By default, the **Observed** tab is selected.

3.  Optional: You can choose to view observed vulnerabilities or those that have been deferred or marked as false positives. Click one of the following tabs:

    - **Observed**: Lists vulnerabilities that RHACS observed in platform workloads and images.

    - **Deferred**: Lists vulnerabilities that have been observed but had a deferral request submitted and approved in the exception management workflow.

    - **False positives**: Lists vulnerabilities that have been observed but were identified as false positives in the exception management workflow.

4.  Optional: You can select the following options to refine the list of results:

    - **Prioritize by namespace view**: Displays a list of namespaces sorted according to the risk priority. You can use this view to quickly identify and address the most critical areas. In this view, click **\<number\> deployments** in a table row to return to the platform vulnerabilities view, with filters applied to show only deployments for the selected namespace.

    - **Default filters**: You can select filters for CVE severity and CVE status that are automatically applied across all views on this page. These filters are applied when you visit the page from another section of the RHACS web portal or from a bookmarked URL. They are saved in the local storage of your browser.

5.  To filter the list of results by entity, for example, to search for a specific named CVE, select the appropriate filters and attributes.

    To select multiple entities and attributes, click the right arrow icon to add another criteria. Depending on your choices, enter the appropriate information such as text, or select a date or object.

    The filter entities and attributes are listed in the following table.

    > [!NOTE]
    > The **Filtered view** icon indicates that the displayed results were filtered based on the criteria that you selected. You can click **Clear filters** to remove all filters, or remove individual filters by clicking on them.

    <table>
    <caption>Filter options</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Entity</th>
    <th style="text-align: left;">Attributes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Image</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image.</p></li>
    <li><p><strong>Operating system</strong>: The operating system of the image.</p></li>
    <li><p><strong>Tag</strong>: The tag for the image.</p></li>
    <li><p><strong>Label</strong>: The label for the image.</p></li>
    <li><p><strong>Registry</strong>: The registry where the image is located.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>CVE</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the CVE.</p></li>
    <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
    <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
    <p>The following values are associated with the severity level for the CVE:</p>
    <ul>
    <li><p><strong>is greater than</strong></p></li>
    <li><p><strong>is greater than or equal to</strong></p></li>
    <li><p><strong>is equal to</strong></p></li>
    <li><p><strong>is less than or equal to</strong></p></li>
    <li><p><strong>is less than</strong></p></li>
    </ul></li>
    <li><p><strong>EPSS probability</strong>: The likelihood that the vulnerability could be exploited according to the <a href="https://www.first.org/epss/">Exploit Prediction Scoring System (EPSS)</a>. This EPSS data provides a percentage estimate of the probability that exploitation of this vulnerability will be observed in the next 30 days. The EPSS collects data of observed exploitation activity from partners, and exploitation activity does not mean that an attempted exploitation was successful. The EPSS score should be used as a single data point <em>along with other information</em>, such as the age of the CVE, to help you prioritize the vulnerabilities to address. For more information, see <a href="https://access.redhat.com/articles/7106599">RHACS and EPSS</a>.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Image Component</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image component, for example, <code>activerecord-sql-server-adapter</code></p></li>
    <li><p><strong>Source</strong>:</p>
    <ul>
    <li><p>OS</p></li>
    <li><p>Python</p></li>
    <li><p>Java</p></li>
    <li><p>Ruby</p></li>
    <li><p>Node.js</p></li>
    <li><p>Go</p></li>
    <li><p>Dotnet Core Runtime</p></li>
    <li><p>Infrastructure</p></li>
    </ul></li>
    <li><p><strong>Version</strong>: Version of the image component; for example, <code>3.4.21</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Deployment</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: Name of the deployment.</p></li>
    <li><p><strong>Label</strong>: Label for the deployment.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the deployment.</p></li>
    <li><p><strong>Status</strong>: Whether the deployment is inactive or active.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Namespace</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The <code>metadata.uid</code> of the namespace that is created by Kubernetes.</p></li>
    <li><p><strong>Name</strong>: The name of the namespace.</p></li>
    <li><p><strong>Label</strong>: The label for the namespace.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the namespace.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Cluster</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
    <li><p><strong>Name</strong>: The name of the cluster.</p></li>
    <li><p><strong>Label</strong>: The label for the cluster.</p></li>
    <li><p><strong>Type</strong>: The cluster type, for example, OCP.</p></li>
    <li><p><strong>Platform type</strong>: The platform type, for example, OpenShift 4 cluster.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    - **CVE severity**: You can select one or more levels.

    - **CVE status**: You can select **Fixable** or **Not fixable**.

6.  Click one of the following tabs to view the data that you want:

    - **\<number\> CVEs**: Displays vulnerabilities organized by CVE

    - **\<number\> Images**: Displays images that contain discovered vulnerabilities.

    - **\<number\> Deployments**: Displays deployments that contain discovered vulnerabilities.

7.  Optional: Choose the appropriate method to view the component and advisory data associated with a CVE:

    - To view the component and advisory data associated with a CVE from the list of CVEs, complete the following steps:

      1.  Click the **\<number\> CVEs** tab.

      2.  In the list of CVEs, click a CVE to do any of the following tasks:

          - To view the component and advisory data associated with an image:

            1.  Click the **\<number\> Images** tab.

            2.  Expand the image.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

          - To view the component and advisory data associated with a deployment:

            1.  Click the **\<number\> Deployments** tab.

            2.  Expand the deployment.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of images, complete the following steps:

      1.  Click the **\<number\> Images** tab.

      2.  In the list of images, click an image.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of deployments, complete the following steps:

      1.  Click the **\<number\> Deployments** tab.

      2.  In the list of deployments, click a deployment.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

8.  Optional: Choose the appropriate method to re-organize the information in the **User Workloads** tab:

    - To sort the table in ascending or descending order, select a column heading.

    - To select the categories that you want to display in the table, perform the following steps:

      1.  Click **Columns**.

      2.  Choose the appropriate method to manage the columns:

          - To view all the categories, click **Select all**.

          - To reset to the default categories, click **Reset to default**.

          - To view only the selected categories, select the one or more categories that you want to view, and then click **Save**.

9.  In the list of results, click a CVE, image name, or deployment name to view more information about the item. For example, depending on the item type, you can view the following information:

    - Whether a CVE is fixable

    - Whether an image is active

    - The Dockerfile line in the image that contains the CVE

    - External links to information about the CVE in Red Hat and other CVE databases

</div>

<a id="viewing-node-cves_vulns-nodes"></a>

## Viewing vulnerabilities in nodes

You can identify vulnerabilities in your nodes by using RHACS. The vulnerabilities that are identified include the following:

- Vulnerabilities in core Kubernetes components

- Vulnerabilities in container runtimes such as Docker, CRI-O, runC, and containerd

For more information about operating systems that RHACS can scan, see "Supported operating systems".

RHACS currently supports scanning nodes with the StackRox scanner and Scanner V4. Depending on which scanner is configured, different results might appear in the list of vulnerabilities. For more information, see "Understanding differences in scanning results between the StackRox Scanner and Scanner V4".

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Select the **Nodes** tab.

3.  Optional: The page defaults to a list of observed CVEs. Click **Show snoozed CVEs** to view them.

4.  Optional: To filter CVEs according to entity, select the appropriate filters and attributes. To add more filtering criteria, follow these steps:

    1.  Select the entity or attribute from the list.

    2.  Depending on your choices, enter the appropriate information such as text, or select a date or object.

    3.  Click the right arrow icon.

    4.  Optional: Select additional entities and attributes, and then click the right arrow icon to add them. The filter entities and attributes are listed in the following table.

        <table>
        <caption>Filter options</caption>
        <colgroup>
        <col style="width: 50%" />
        <col style="width: 50%" />
        </colgroup>
        <thead>
        <tr>
        <th style="text-align: left;">Entity</th>
        <th style="text-align: left;">Attributes</th>
        </tr>
        </thead>
        <tbody>
        <tr>
        <td style="text-align: left;"><p>Node</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the node.</p></li>
        <li><p><strong>Operating system</strong>: The operating system of the node, for example, Red Hat Enterprise Linux (RHEL).</p></li>
        <li><p><strong>Label</strong>: The label of the node.</p></li>
        <li><p><strong>Annotation</strong>: The annotation for the node.</p></li>
        <li><p><strong>Scan time</strong>: The scan date of the node.</p></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>CVE</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the CVE.</p></li>
        <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
        <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
        <p>The following values are associated with the severity level for the CVE:</p>
        <ul>
        <li><p><strong>is greater than</strong></p></li>
        <li><p><strong>is greater than or equal to</strong></p></li>
        <li><p><strong>is equal to</strong></p></li>
        <li><p><strong>is less than or equal to</strong></p></li>
        <li><p><strong>is less than</strong></p></li>
        </ul></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>Node Component</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>Name</strong>: The name of the component.</p></li>
        <li><p><strong>Version</strong>: The version of the component, for example, <code>4.15.0-2024</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
        </ul></td>
        </tr>
        <tr>
        <td style="text-align: left;"><p>Cluster</p></td>
        <td style="text-align: left;"><ul>
        <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
        <li><p><strong>Name</strong>: The name of the cluster.</p></li>
        <li><p><strong>Label</strong>: The label for the cluster.</p></li>
        <li><p><strong>Type</strong>: The type of cluster, for example, OCP.</p></li>
        <li><p><strong>Platform type</strong>: The type of platform, for example, OpenShift 4 cluster.</p></li>
        </ul></td>
        </tr>
        </tbody>
        </table>

5.  Optional: To refine the list of results, do any of the following tasks:

    - Click **CVE severity**, and then select one or more levels.

    - Click **CVE status**, and then select **Fixable** or **Not fixable**.

6.  To view the data, click one of the following tabs:

    - **\<number\> CVEs**: Displays a list of all the CVEs affecting all of your nodes.

    - **\<number\> Nodes**: Displays a list of nodes that contain CVEs.

7.  To view the details of the node and information about the CVEs according to the CVSS score and fixable CVEs for that node, click a node name in the list of nodes.

</div>

<a id="disable-identify-vulnerabilities-in-nodes_vulns-nodes"></a>

### Disabling identifying vulnerabilities in nodes

Identifying vulnerabilities in nodes is enabled by default. You can disable it from the RHACS portal.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under **Image Integrations**, select **StackRox Scanner**.

3.  From the list of scanners, select **StackRox Scanner** to view its details.

4.  Click **Edit**.

5.  To use only the image scanner and not the node scanner, click **Image Scanner**.

6.  Click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Understanding differences in scanning results between the StackRox Scanner and Scanner V4](scan-rhcos-node-host.md#understanding-node-cves-scanner-v4_scan-rhcos-node-host)

- [Supported operating systems](../examine-images-for-vulnerabilities.md#supported-operating-systems_examine-images-for-vulnerabilities)

</div>

<a id="vview-vms-cves_vms"></a>

## Viewing vulnerabilities in virtual machines

In the **Vulnerability Management** → **Results** page, you can get information about the vulnerabilities in virtual machines (VMs).

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Select the **Virtual Machines** tab. The table displays all VMs and the vulnerabilities found. The **Scanned packages** column indicates if `roxagent` is running, and if the packages have been indexed correctly.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Scanning virtual machines](../examine-images-for-vulnerabilities.md#scanning-virtual-machines_examine-images-for-vulnerabilities)

</div>

<a id="vulnerability-management-accessing-additional-views_more-views"></a>

## Accessing additional views in vulnerability management

The **More views** tab provides additional ways to view vulnerabilities in your system, including the following views:

- All vulnerable images: Displays vulnerabilities for user workloads, platform vulnerabilities, and vulnerabilities for inactive images in the same page.

- Inactive images: Displays vulnerabilities for watched images and images that are not currently deployed as workloads. Vulnerabilities are reported for images based on your image retention settings.

- Images without CVEs: Shows images and workloads without observed CVEs. See "Analyze images and deployments without observed CVEs".

- Kubernetes components: Displays vulnerabilities affecting the underlying Kubernetes structure.

<a id="vulnerability-management-more-views-all-vuln-images_more-views"></a>

### Viewing all vulnerable images

You can view a list of vulnerabilities for user workloads, platform vulnerabilities, and inactive images on the same page.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Click **More Views** and select **All vulnerable images**.

3.  Optional: You can choose to view observed vulnerabilities or those that have been deferred or marked as false positives. Click one of the following tabs:

    - **Observed**: Lists vulnerabilities that RHACS observed across all images and workloads.

    - **Deferred**: Lists vulnerabilities that have been observed but had a deferral request submitted and approved in the exception management workflow.

    - **False positives**: Lists vulnerabilities that have been observed but were identified as false positives in the exception management workflow.

4.  Optional: You can select the following options to refine the list of results:

    - **Prioritize by namespace view**: Displays a list of namespaces sorted according to the risk priority. You can use this view to quickly identify and address the most critical areas. In this view, click **\<number\> deployments** in a table row to return to the all vulnerable images view, with filters applied to show only deployments for the selected namespace.

    - **Default filters**: You can select filters for CVE severity and CVE status that are automatically applied across all views on this page. These filters are applied when you visit the page from another section of the RHACS web portal or from a bookmarked URL. They are saved in the local storage of your browser.

5.  Click one of the following tabs to view the data that you want:

    - **\<number\> CVEs**: Displays vulnerabilities organized by CVE

    - **\<number\> Images**: Displays images that contain discovered vulnerabilities.

    - **\<number\> Deployments**: Displays deployments that contain discovered vulnerabilities.

6.  Optional: Choose the appropriate method to view the component and advisory data associated with a CVE:

    - To view the component and advisory data associated with a CVE from the list of CVEs, complete the following steps:

      1.  Click the **\<number\> CVEs** tab.

      2.  In the list of CVEs, click a CVE to do any of the following tasks:

          - To view the component and advisory data associated with an image:

            1.  Click the **\<number\> Images** tab.

            2.  Expand the image.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

          - To view the component and advisory data associated with a deployment:

            1.  Click the **\<number\> Deployments** tab.

            2.  Expand the deployment.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of images, complete the following steps:

      1.  Click the **\<number\> Images** tab.

      2.  In the list of images, click an image.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of deployments, complete the following steps:

      1.  Click the **\<number\> Deployments** tab.

      2.  In the list of deployments, click a deployment.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

7.  Optional: Choose the appropriate method to re-organize the information in the **User Workloads** tab:

    - To sort the table in ascending or descending order, select a column heading.

    - To filter the table, use the filter bar.

    - To select the categories that you want to display in the table, perform the following steps:

      1.  Click **Columns**.

      2.  Choose the appropriate method to manage the columns:

          - To view all the categories, click **Select all**.

          - To reset to the default categories, click **Reset to default**.

          - To view only the selected categories, select the one or more categories that you want to view, and then click **Save**.

8.  To filter the list of results by entity, for example, to search for a specific named CVE, select the appropriate filters and attributes.

    To select multiple entities and attributes, click the right arrow icon to add another criteria. Depending on your choices, enter the appropriate information such as text, or select a date or object.

    The filter entities and attributes are listed in the following table.

    <table>
    <caption>CVE filtering</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Entity</th>
    <th style="text-align: left;">Attributes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Image</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image.</p></li>
    <li><p><strong>Operating system</strong>: The operating system of the image.</p></li>
    <li><p><strong>Tag</strong>: The tag for the image.</p></li>
    <li><p><strong>Label</strong>: The label for the image.</p></li>
    <li><p><strong>Registry</strong>: The registry where the image is located.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>CVE</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the CVE.</p></li>
    <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
    <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
    <p>The following values are associated with the severity level for the CVE:</p>
    <ul>
    <li><p><strong>is greater than</strong></p></li>
    <li><p><strong>is greater than or equal to</strong></p></li>
    <li><p><strong>is equal to</strong></p></li>
    <li><p><strong>is less than or equal to</strong></p></li>
    <li><p><strong>is less than</strong></p></li>
    </ul></li>
    <li><p><strong>EPSS probability</strong>: The likelihood that the vulnerability could be exploited according to the <a href="https://www.first.org/epss/">Exploit Prediction Scoring System (EPSS)</a>. This EPSS data provides a percentage estimate of the probability that exploitation of this vulnerability will be observed in the next 30 days. The EPSS collects data of observed exploitation activity from partners, and exploitation activity does not mean that an attempted exploitation was successful. The EPSS score should be used as a single data point <em>along with other information</em>, such as the age of the CVE, to help you prioritize the vulnerabilities to address. For more information, see <a href="https://access.redhat.com/articles/7106599">RHACS and EPSS</a>.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Image Component</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image component, for example, <code>activerecord-sql-server-adapter</code></p></li>
    <li><p><strong>Source</strong>:</p>
    <ul>
    <li><p>OS</p></li>
    <li><p>Python</p></li>
    <li><p>Java</p></li>
    <li><p>Ruby</p></li>
    <li><p>Node.js</p></li>
    <li><p>Go</p></li>
    <li><p>Dotnet Core Runtime</p></li>
    <li><p>Infrastructure</p></li>
    </ul></li>
    <li><p><strong>Version</strong>: Version of the image component; for example, <code>3.4.21</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Deployment</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: Name of the deployment.</p></li>
    <li><p><strong>Label</strong>: Label for the deployment.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the deployment.</p></li>
    <li><p><strong>Status</strong>: Whether the deployment is inactive or active.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Namespace</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The <code>metadata.uid</code> of the namespace that is created by Kubernetes.</p></li>
    <li><p><strong>Name</strong>: The name of the namespace.</p></li>
    <li><p><strong>Label</strong>: The label for the namespace.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the namespace.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Cluster</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
    <li><p><strong>Name</strong>: The name of the cluster.</p></li>
    <li><p><strong>Label</strong>: The label for the cluster.</p></li>
    <li><p><strong>Type</strong>: The cluster type, for example, OCP.</p></li>
    <li><p><strong>Platform type</strong>: The platform type, for example, OpenShift 4 cluster.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

    - **CVE severity**: You can select one or more levels.

    - **CVE status**: You can select **Fixable** or **Not fixable**.

</div>

> [!NOTE]
> The **Filtered view** icon indicates that the displayed results were filtered based on the criteria that you selected. You can click **Clear filters** to remove all filters, or remove individual filters by clicking on them.

In the list of results, click a CVE, image name, or deployment name to view more information about the item. For example, depending on the item type, you can view the following information:

- Whether a CVE is fixable

- Whether an image is active

- The Dockerfile line in the image that contains the CVE

- External links to information about the CVE in Red Hat and other CVE databases

<a id="scan-inactive-images_more-views"></a>

### Scanning inactive images

Red Hat Advanced Cluster Security for Kubernetes (RHACS) scans all active (deployed) images every 4 hours and updates the image scan results to reflect the latest vulnerability definitions.

You can also configure RHACS to scan inactive (not deployed) images automatically.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click **More Views** → **Inactive images**.

3.  Optional: Choose the appropriate method to view the component and advisory data associated with a CVE:

    - To view the component and advisory data associated with a CVE from the list of CVEs, complete the following steps:

      1.  Click the **\<number\> CVEs** tab.

      2.  In the list of CVEs, click a CVE to do any of the following tasks:

          - To view the component and advisory data associated with an image:

            1.  Click the **\<number\> Images** tab.

            2.  Expand the image.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

          - To view the component and advisory data associated with a deployment:

            1.  Click the **\<number\> Deployments** tab.

            2.  Expand the deployment.

                You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of images, complete the following steps:

      1.  Click the **\<number\> Images** tab.

      2.  In the list of images, click an image.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

    - To view the component and advisory data associated with a CVE from the list of deployments, complete the following steps:

      1.  Click the **\<number\> Deployments** tab.

      2.  In the list of deployments, click a deployment.

      3.  To view the component and advisory data associated with a CVE, expand the CVE.

          You can find the component data in the **Component** column, and you can find the advisory data in the **Advisory** column.

4.  Click **Manage watched images**.

5.  In the **Image name** field, enter the fully-qualified image name that begins with the registry and ends with the image tag, for example, `docker.io/library/nginx:latest`.

6.  Click **Add image to watch list**.

7.  Optional: To remove a watched image, locate the image in the **Manage watched images** window, and click **Remove watch**.

    > [!IMPORTANT]
    > In the RHACS portal, click **Platform Configuration** → **System Configuration** to view the data retention configuration.
    >
    > All the data related to the image removed from the watched image list continues to appear in the RHACS portal for the number of days mentioned on the **System Configuration** page and is only removed after that period is over.

8.  Click **Close** to return to the **Inactive images** page.

</div>

<a id="analyze-images-and-deployments-without-observed-cves_more-views"></a>

### Analyze images and deployments without observed CVEs

When you view the list of images without vulnerabilities, RHACS shows the images that meet at least one of the following conditions:

- Images that do not have CVEs

- Images that report a scanner error that may result in a false negative of no CVEs

> [!NOTE]
> An image that actually contains vulnerabilities can appear in this list inadvertently. For example, if Scanner was able to scan the image and it is known to Red Hat Advanced Cluster Security for Kubernetes (RHACS), but the scan was not successfully completed, RHACS cannot detect vulnerabilities.
>
> This scenario occurs if an image has an operating system that RHACS Scanner does not support. RHACS displays scan errors when you hover over an image in the image list or click the image name for more information.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Vulnerability Management** → **Results**.

2.  Click **More Views** and select **Images without CVEs**.

3.  To filter the list of results by entity, for example, to search for a specific image, select the appropriate filters and attributes.

    To select multiple entities and attributes, click the right arrow icon to add another criteria. Depending on your choices, enter the appropriate information such as text, or select a date or object.

    The filter entities and attributes are listed in the following table.

    > [!NOTE]
    > The **Filtered view** icon indicates that the displayed results were filtered based on the criteria that you selected. You can click **Clear filters** to remove all filters, or remove individual filters by clicking on them.

    <table>
    <caption>Filter options</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Entity</th>
    <th style="text-align: left;">Attributes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Image</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image.</p></li>
    <li><p><strong>Operating system</strong>: The operating system of the image.</p></li>
    <li><p><strong>Tag</strong>: The tag for the image.</p></li>
    <li><p><strong>Label</strong>: The label for the image.</p></li>
    <li><p><strong>Registry</strong>: The registry where the image is located.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Image Component</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the image component, for example, <code>activerecord-sql-server-adapter</code></p></li>
    <li><p><strong>Source</strong>:</p>
    <ul>
    <li><p>OS</p></li>
    <li><p>Python</p></li>
    <li><p>Java</p></li>
    <li><p>Ruby</p></li>
    <li><p>Node.js</p></li>
    <li><p>Go</p></li>
    <li><p>Dotnet Core Runtime</p></li>
    <li><p>Infrastructure</p></li>
    </ul></li>
    <li><p><strong>Version</strong>: Version of the image component; for example, <code>3.4.21</code>. You can use this to search for a specific version of a component, for example, in conjunction with a component name.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Deployment</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: Name of the deployment.</p></li>
    <li><p><strong>Label</strong>: Label for the deployment.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the deployment.</p></li>
    <li><p><strong>Status</strong>: Whether the deployment is inactive or active.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Namespace</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The <code>metadata.uid</code> of the namespace that is created by Kubernetes.</p></li>
    <li><p><strong>Name</strong>: The name of the namespace.</p></li>
    <li><p><strong>Label</strong>: The label for the namespace.</p></li>
    <li><p><strong>Annotation</strong>: The annotation for the namespace.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>Cluster</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
    <li><p><strong>Name</strong>: The name of the cluster.</p></li>
    <li><p><strong>Label</strong>: The label for the cluster.</p></li>
    <li><p><strong>Type</strong>: The cluster type, for example, OCP.</p></li>
    <li><p><strong>Platform type</strong>: The platform type, for example, OpenShift 4 cluster.</p></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

4.  Click one of the following tabs to view the data that you want:

    - **\<number\> Images**: Displays images that contain discovered vulnerabilities.

    - **\<number\> Deployments**: Displays deployments that contain discovered vulnerabilities.

5.  Optional: Choose the appropriate method to re-organize the information in the page:

    - To select the categories that you want to display in the table, perform the following steps:

      1.  Click **Columns**.

      2.  Choose the appropriate method to manage the columns:

          - To view all the categories, click **Select all**.

          - To reset to the default categories, click **Reset to default**.

          - To view only the selected categories, select the one or more categories that you want to view, and then click **Save**.

          - To sort the table in ascending or descending order, select a column heading.

6.  In the list of results, click an image name or deployment name to view more information about the item.

</div>

<a id="vulnerability-management-viewing-kubernetes-vulnerabilities_more-views"></a>

### Viewing Kubernetes vulnerabilities

You can view vulnerabilities in your clusters that affect the underlying Kubernetes structure.

<div>

<div class="title">

Procedure

</div>

1.  Go to **Vulnerability Management** → **Results**.

2.  Click **More Views** and select **Kubernetes components**.

3.  Click the **\<number\> CVEs** or **\<number\> Clusters** to display by CVE or cluster.

4.  Optional: Within the results list, you can filter results by cluster and CVE. To filter vulnerabilities based on an entity, select the appropriate filters and attributes.

    To select multiple entities and attributes, click the right arrow icon to add another criteria. Depending on your choices, enter the appropriate information such as text, or select a date or object.

    The filter entities and attributes are listed in the following table.

    <table>
    <caption>Filter options</caption>
    <colgroup>
    <col style="width: 50%" />
    <col style="width: 50%" />
    </colgroup>
    <thead>
    <tr>
    <th style="text-align: left;">Entity</th>
    <th style="text-align: left;">Attributes</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td style="text-align: left;"><p>Cluster</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>ID</strong>: The alphanumeric ID for the cluster. This is an internal identifier that RHACS assigns for tracking purposes.</p></li>
    <li><p><strong>Name</strong>: The name of the cluster.</p></li>
    <li><p><strong>Label</strong>: The label for the cluster.</p></li>
    <li><p><strong>Type</strong>: The cluster type, for example, OCP.</p></li>
    <li><p><strong>Platform type</strong>: The platform type, for example, OpenShift 4 cluster.</p></li>
    </ul></td>
    </tr>
    <tr>
    <td style="text-align: left;"><p>CVE</p></td>
    <td style="text-align: left;"><ul>
    <li><p><strong>Name</strong>: The name of the CVE.</p></li>
    <li><p><strong>Discovered time</strong>: The date when RHACS discovered the CVE.</p></li>
    <li><p><strong>CVSS</strong>: The severity level for the CVE.</p>
    <p>The following values are associated with the severity level for the CVE:</p>
    <ul>
    <li><p><strong>is greater than</strong></p></li>
    <li><p><strong>is greater than or equal to</strong></p></li>
    <li><p><strong>is equal to</strong></p></li>
    <li><p><strong>is less than or equal to</strong></p></li>
    <li><p><strong>is less than</strong></p></li>
    </ul></li>
    <li><p><strong>Type</strong>: The type of CVE:</p>
    <ul>
    <li><p>Kubernetes</p></li>
    <li><p>Istio</p></li>
    <li><p>OpenShift</p></li>
    </ul></li>
    </ul></td>
    </tr>
    </tbody>
    </table>

5.  Optional: To filter the table based on the status of a CVE, from the **CVE status** drop-down list, select one or more statuses.

    The following values are associated with the status of a CVE:

    - `Fixable`

    - `Not fixable`

</div>

> [!NOTE]
> The **Filtered view** icon indicates that the displayed results were filtered based on the criteria that you selected. You can click **Clear filters** to remove all filters, or remove individual filters by clicking on them.

In the list of results, click a CVE or cluster name to view more information about the item. For example, depending on the item type, you can view the following information:

- First discovered date

- Whether a CVE is fixable

- External links to information about the CVE in Red Hat and other CVE databases

<a id="cves-tab_vulnerability-tabs"></a>

## CVEs tab

The CVEs view organizes information into various groups.

The information available includes the following components:

- **CVE**: Displays a unique identifier for Common Vulnerabilities and Exposures (CVE), each representing a specific vulnerability, to track and analyze it in detail.

- **Images by severity**: Groups images based on the severity level of the associated vulnerabilities.

- **Top CVSS**: Displays the highest CVSS score for each CVE across images to highlight the vulnerabilities with the most severe impact.

- **Top NVD CVSS**: Shows the highest severity scores from the National Vulnerability Database (NVD) to enable standardized impact assessments. This information is only visible when using Scanner V4.

- **EPSS probability**: The likelihood that the vulnerability could be exploited according to the [Exploit Prediction Scoring System (EPSS)](https://www.first.org/epss/). This EPSS data provides a percentage estimate of the probability that exploitation of this vulnerability will be observed in the next 30 days. The EPSS collects data of observed exploitation activity from partners, and exploitation activity does not mean that an attempted exploitation was successful. The EPSS score should be used as a single data point *along with other information*, such as the age of the CVE, to help you prioritize the vulnerabilities to address. For more information, see [RHACS and EPSS](https://access.redhat.com/articles/7106599). This information is visible only when using Scanner V4.

- **Affected images**: Displays the number of container images affected by specific CVEs to assess the scope of vulnerabilities.

- **First discovered**: Shows the date each vulnerability was first discovered in the environment to measure the duration of its exposure.

- **Published**: Indicates when the CVE was publicly disclosed.

To review and triage the details associated with a CVE, click on the CVE.

A window opens with information about the vulnerabilities associated with the CVE.

<a id="images-tab_vulnerability-tabs"></a>

## Images tab

The images view organizes the information into the following groups:

- **Image**: Displays the name or identifier of each container image.

- **Operating system**: Highlights the operating system that the image uses and helps identify potential vulnerabilities specific to that operating system.

- **Deployments**: Shows all deployments where the image is actively running so you can assess the impact and prioritize remediation based on usage.

- **Age**: Shows how long the image has been in use and provides information about potential risks associated with outdated images.

- **Scan time**: Shows the timestamp of the last scan.

To review and triage the details associated with an image, click on the image.

A window opens with information about the vulnerabilities associated with the image.

<a id="deployments-tab_vulnerability-tabs"></a>

## Deployments tab

The deployments view organizes information into various groups.

Deployment information available includes the following components:

- **Deployment**: Indicates the name or identifier of each deployment.

- **Cluster**: Displays the cluster in which each deployment is located.

- **Namespace**: Displays the namespace of each deployment.

- **Images**: Displays the container images that the deployment uses.

- **First discovered**: Shows the date on which the vulnerabilities associated with a deployment were first discovered.

To review and triage the details associated with a deployment, click on the deployment.

A window opens with information about the vulnerabilities associated with the deployment.

<a id="excluding-CVEs_excluding-cves"></a>

# Excluding CVEs

You can exclude or ignore CVEs in RHACS by snoozing node and platform CVEs and deferring or marking node, platform, and image CVEs as false positives. You might want to exclude CVEs if you know that the CVE is a false positive or you have already taken steps to mitigate the CVE. Snoozed CVEs do not appear in vulnerability reports or trigger policy violations.

You can snooze a CVE to ignore it globally for a specified period of time. Snoozing a CVE does not require approval.

> [!NOTE]
> Snoozing node and platform CVEs requires that the `ROX_VULN_MGMT_LEGACY_SNOOZE` environment variable is set to `true`.

Deferring or marking a CVE as a false positive is done through the exception management workflow. This workflow provides the ability to view pending, approved, and denied deferral and false positive requests. You can scope the CVE exception to a single image, all tags for a single image, or globally for all images.

When approving or denying a request, you must add a comment. A CVE remains in the observed status until the exception request is approved. A pending request for deferral that is denied by another user is still visible in reports, policy violations, and other places in the system, but is indicated by a **Pending exception** label next to the CVE when visiting the following pages after going to **Vulnerability Management** → **Results**:

- User workloads

- Platform

- All vulnerable images

- Inactive images

An approved exception for a deferral or false positive has the following effects:

- Removes the CVE from the **Observed** tab in the **User Workloads** tab to either the **Deferred** or **False positive** tab

- Prevents the CVE from triggering policy violations that are related to the CVE

- Prevents the CVE from showing up in automatically generated vulnerability reports

<a id="snooze-cves-vm20_snoozing-cves"></a>

## Snoozing platform and node CVEs

You can snooze platform and node CVEs that do not relate to your infrastructure. You can snooze CVEs for 1 day, 1 week, 2 weeks, 1 month, or indefinitely, until you unsnooze them. Snoozing a CVE takes effect immediately and does not require an additional approval step.

> [!NOTE]
> The ability to snooze a CVE is not enabled by default in the web portal or in the API. To enable the ability to snooze CVEs, set the runtime environment variable `ROX_VULN_MGMT_LEGACY_SNOOZE` to `true`.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, do any of the following tasks:

    - To view platform CVEs, click **Vulnerability Management** → **Platform CVEs**.

    - To view node CVEs, click **Vulnerability Management** → **Node CVEs**.

2.  Select one or more CVEs.

3.  Select the appropriate method to snooze the CVE:

    - If you selected a single CVE, click the overflow menu, ![kebab](../../images/kebab.png), and then select **Snooze CVE**.

    - If you selected multiple CVEs, click **Bulk actions** → **Snooze CVEs**.

4.  Select the duration of time to snooze.

5.  Click **Snooze CVEs**.

    You receive a confirmation that you have requested to snooze the CVEs.

</div>

<a id="unsnooze-cves-vm20_snoozing-cves"></a>

## Unsnoozing platform and node CVEs

You can unsnooze platform and node CVEs that you have previously snoozed.

> [!NOTE]
> The ability to snooze a CVE is not enabled by default in the web portal or in the API. To enable the ability to snooze CVEs, set the runtime environment variable `ROX_VULN_MGMT_LEGACY_SNOOZE` to `true`.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, do any of the following tasks:

    - To view the list of platform CVEs, click **Vulnerability Management** → **Platform CVEs**.

    - To view the list of node CVEs, click **Vulnerability Management** → **Node CVEs**.

2.  To view the list of snoozed CVEs, click **Show snoozed CVEs** in the header view.

3.  Select one or more CVEs from the list of snoozed CVEs.

4.  Select the appropriate method to unsnooze the CVE:

    - If you selected a single CVE, click the overflow menu, ![kebab](../../images/kebab.png), and then select **Unsnooze CVE**.

    - If you selected multiple CVEs, click **Bulk actions** → **Unsnooze CVEs**.

5.  Click **Unsnooze CVEs** again.

    You receive a confirmation that you have requested to unsnooze the CVEs.

</div>

<a id="viewing-snoozed-cves_snoozing-cves"></a>

## Viewing snoozed CVEs

You can view a list of platform and node CVEs that have been snoozed.

> [!NOTE]
> The ability to snooze a CVE is not enabled by default in the web portal or in the API. To enable the ability to snooze CVEs, set the runtime environment variable `ROX_VULN_MGMT_LEGACY_SNOOZE` to `true`.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, do any of the following tasks:

    - To view the list of platform CVEs, click **Vulnerability Management** → **Platform CVEs**.

    - To view the list of node CVEs, click **Vulnerability Management** → **Node CVEs**.

2.  Click **Show snoozed CVEs** to view the list.

</div>

<a id="vulnerability-management-mark-false-positive_marking"></a>

## Marking a vulnerability as a false positive globally

You can create an exception for a vulnerability by marking it as a false positive globally, or across all images. You must get requests to mark a vulnerability as a false positive approved in the exception management workflow.

<div>

<div class="title">

Prerequisites

</div>

- You have the `write` permission for the `VulnerabilityManagementRequests` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click **User Workloads**.

3.  Choose the appropriate method to mark the CVEs:

    - If you want to mark a single CVE, perform the following steps:

      1.  Find the row which contains the CVE that you want to take action on.

      2.  Click the overflow menu, ![kebab](../../images/kebab.png), for the CVE that you identified, and then select **Mark as false positive**.

    - If you want to mark multiple CVEs, perform the following steps:

      1.  Select each CVE.

      2.  From the **Bulk actions** drop-down list, select **Mark as false positives**.

4.  Enter a rationale for requesting the exception.

5.  Optional: To review the CVEs that are included in the exception request, click **CVE selections**.

6.  Click **Submit request**.

    You receive a confirmation that you have requested an exception.

7.  Optional: To copy the approval link and share it with your organization’s exception approver, click the copy icon.

8.  Click **Close**.

</div>

<a id="vulnerability-management-mark-false-positive-image_marking"></a>

## Marking a vulnerability as a false positive for an image or image tag

To create an exception for a vulnerability, you can mark it as a false positive for a single image, or across all tags associated with an image. You must get requests to mark a vulnerability as a false positive approved in the exception management workflow.

<div>

<div class="title">

Prerequisites

</div>

- You have the `write` permission for the `VulnerabilityManagementRequests` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click the **User Workloads** tab.

3.  To view the list of images, click **\<number\> Images**.

4.  Find the row that lists the image that you want to mark as a false positive, and click the image name.

5.  Choose the appropriate method to mark the CVEs:

    - If you want to mark a single CVE, perform the following steps:

      1.  Find the row which contains the CVE that you want to take action on.

      2.  Click the overflow menu, ![kebab](../../images/kebab.png), for the CVE that you identified, and then select **Mark as false positive**.

    - If you want to mark multiple CVEs, perform the following steps:

      1.  Select each CVE.

      2.  From the **Bulk actions** drop-down list, select **Mark as false positives**.

6.  Select the scope. You can select either all tags associated with the image or only the image.

7.  Enter a rationale for requesting the exception.

8.  Optional: To review the CVEs that are included in the exception request, click **CVE selections**.

9.  Click **Submit request**.

    You receive a confirmation that you have requested an exception.

10. Optional: To copy the approval link and share it with your organization’s exception approver, click the copy icon.

11. Click **Close**.

</div>

<a id="vulnerability-management-review-deferred_deferring"></a>

## Viewing deferred and false positive CVEs

You can view the CVEs that have been deferred or marked as false positives by using the **User Workloads** page.

<div>

<div class="title">

Procedure

</div>

1.  To see CVEs that have been deferred or marked as false positives, with the exceptions approved by an approver, click **Vulnerability Management** → **Results**.

2.  Click the **User Workloads** tab.

3.  Complete any of the following actions:

    - To see CVEs that have been deferred, click the **Deferred** tab.

    - To see CVEs that have been marked as false positives, click the **False positives** tab.

      > [!NOTE]
      > To approve, deny, or change deferred or false positive CVEs, click **Vulnerability Management** → **Exception Management**.

4.  Optional: To view additional information about the deferral or false positive, click **View** in the **Request details** column. The **Exception Management** page is displayed.

</div>

<a id="vulnerability-management-accept-risks_deferring"></a>

## Deferring CVEs

You can accept risk with or without mitigation and defer CVEs. You must get deferral requests approved in the exception management workflow.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `VulnerabilityManagementRequests` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click the **User Workloads** tab.

3.  Choose the appropriate method to defer a CVE:

    - If you want to defer a single CVE, perform the following steps:

      1.  Find the row which contains the CVE that you want to mark as a false positive.

      2.  Click the overflow menu, ![kebab](../../images/kebab.png), for the CVE that you identified, and then click **Defer CVE**.

    - If you want to defer multiple CVEs, perform the following steps:

      1.  Select each CVE.

      2.  Click **Bulk actions** → **Defer CVEs**.

4.  Select the time period for the deferral.

5.  Enter a rationale for requesting the exception.

6.  Optional: To review the CVEs that are included in the exception menu, click **CVE selections**.

7.  Click **Submit request**.

    You receive a confirmation that you have requested a deferral.

8.  Optional: To copy the approval link to share it with your organization’s exception approver, click the copy icon.

9.  Click **Close**.

</div>

<a id="vulnerability-management-exception-time-config_deferring"></a>

### Configuring vulnerability exception expiration periods

You can configure the time periods available for vulnerability management exceptions. These options are available when users request to defer a CVE.

<div>

<div class="title">

Prerequisites

</div>

- You have `write` permission for the `VulnerabilityManagementRequests` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Exception Configuration**.

2.  You can configure expiration times that users can select when they request to defer a CVE. Enabling a time period makes it available to users and disabling it removes it from the user interface.

</div>

<a id="vulnerability-management-review-accept-deferrals-false-positives_approving"></a>

## Reviewing and managing an exception request to defer or mark a CVE as false positive

You can review, update, approve, or deny an exception requests for deferring and marking CVEs as false positives.

<div>

<div class="title">

Prerequisites

</div>

- You have the `write` permission for the `VulnerabilityManagementRequests` resource.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To view the list of pending requests, do any of the following tasks:

    - Paste the approval link into your browser.

    - Click **Vulnerability Management** → **Exception Management**, and then click the request name in the **Pending requests** tab.

2.  Review the scope of the vulnerability and decide whether or not to approve it.

3.  Choose the appropriate option to manage a pending request:

    - If you want to deny the request and return the CVE to observed status, click **Deny request**.

      Enter a rationale for the denial, and click **Deny**.

    - If you want to approve the request, click **Approve request**.

      Enter a rationale for the approval, and click **Approve**.

4.  To cancel a request that you have created and return the CVE to observed status, click **Cancel request**. You can only cancel requests that you have created.

5.  To update the deferral time period or rationale for a request that you have created, click **Update request**. You can only update requests that you have created.

    After you make changes, click **Submit request**.

    You receive a confirmation that you have submitted a request.

</div>

<a id="identify-dockerfile-line-component-cve_other"></a>

# Identifying Dockerfile lines in images that introduced components with CVEs

You can identify specific Dockerfile lines in an image that introduced components with CVEs.

<div class="formalpara">

<div class="title">

Procedure

</div>

To view a problematic line:

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click **User Workloads**.

3.  Click the tab to view the type of CVEs. The following tabs are available:

    - **Observed**

    - **Deferred**

    - **False positives**

4.  In the list of CVEs, click the CVE name to open the page containing the CVE details. The **Affected components** column lists the components that include the CVE.

5.  Expand the CVE to display additional information, including the Dockerfile line that introduced the component.

<a id="base-image-vulnerabilities_other"></a>

# Viewing vulnerabilities from base images

You can use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to identify the base images used by the container applications that your developers build. RHACS then reports vulnerabilities in both base image layers and application layers so that you can route remediation work to the teams responsible for each layer.

Because RHACS can separate base image layers from application layers, you can generate reports that list vulnerabilities that are specific to base or application images. Developers can then prioritize images to update or replace to maintain a secure and trusted supply chain. Developers can also focus on fixing vulnerabilities in application layers instead of vulnerabilities in the base layers.

<div>

<div class="title">

Additional resources

</div>

- [Defining base images used in application development](../examine-images-for-vulnerabilities.md#base-images_examine-images-for-vulnerabilities)

</div>

<a id="view-base-imageinfo-portal_other"></a>

## Viewing base image information for an image in the RHACS portal

RHACS can provide information about the base images identified in your application, such as the base image name, digest, and age. You can use the RHACS portal to view this information.

<div>

<div class="title">

Procedure

</div>

1.  Select **Vulnerability Management** → **Results**.

2.  Click **\<number\> Images**.

3.  Optional: To filter the display to only show base images, take the following actions:

    1.  In the filter bar, select **Image component** and **Layer type**.

    2.  In the filter bar, click **Filter by Layer type** and click **Base image**.

4.  Click the name of the image that you want to examine.

5.  Click the arrow to expand **Base image assessment**. The image name, digest, and image age are shown.

    > [!NOTE]
    > RHACS only displays this information when a base image was detected. To view vulnerabilities by application layer, you must use the filter bar to filter CVEs by layer type. See "View vulnerabilities in a base image layer". If the system did not detect any base image, all layers are considered application layers.

</div>

<a id="view-base-image-vuln_other"></a>

### Viewing vulnerabilities in a base image layer

You can view vulnerabilities by layer in an image and filter vulnerabilities to show only the vulnerabilities that exist in the base image layer.

<div>

<div class="title">

Prerequisite

</div>

- A user with the `ImageAdministration` permission must configure the base image repository under **Platform Configuration** → **Base Images** so that the system can identify and detect base images.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Vulnerability Management** → **Results**.

2.  Click **\<number\> Images**.

3.  Click the name of the image that you want to examine.

4.  To display the CVEs only in the base image layer, take the following actions:

    1.  In the **Observed** tab, in the filter bar, select **Image component** and **Layer type**.

    2.  In the filter bar, click **Filter by Layer type** and click **Base image**. The display is filtered to only show CVEs contained in the base image layer.

</div>

<a id="base-image-vulnreport_other"></a>

### Create a report of vulnerabilities in a base image

You can create a report of vulnerabilities in layers that are identified as the base image layers for an image.

<div>

<div class="title">

Prerequisite

</div>

- A user with the `ImageAdministration` permission must configure the base image repository under **Platform Configuration** → **Base Images** so that the system can identify and detect base images.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Select **Vulnerability Management** → **Results**.

2.  Click **\<number\> Images**.

3.  Click the name of the image that you want to examine. You must select an image that has been configured as a base image in **Platform Configuration** → **Base Images**.

4.  To display the common vulnerabilities and exposures (CVEs) only in the base layer, take the following actions:

    1.  In the **Observed** tab, in the filter bar, select **Image component** and **Layer type**.

    2.  In the filter bar, click **Filter by Layer type** and click **Base image**. The display is filtered to show only CVEs that are contained in the base layer.

5.  In the top menu, click **Create report** and select **Export report as CSV**.

6.  Click **Generate report**.

7.  Click **View status in reports table**.

8.  Click **Report ready for download** to download the file. The report includes CVEs affecting the base image layer by component, and some CVEs might affect multiple components. Therefore, the report totals can differ from the number of CVEs for an image shown in the RHACS portal when results have been filtered by using the **Base image** layer type.

</div>

<a id="vulnerability-management-upgrade-component_other"></a>

# Finding a new component version

The following procedure finds a new component version to upgrade to.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Vulnerability Management** → **Results**.

2.  Click the **User Workloads** tab.

3.  Click **\<number\> Images** and select an image.

4.  To view additional information, locate the CVE and click the expand icon.

    The additional information includes the component that the CVE is in and the version in which the CVE is fixed, if it is fixable.

5.  Update your image to a later version.

</div>

<a id="vulnerability-management-export-workloads_other"></a>

# Exporting workload vulnerabilities by using the API

You can export workload vulnerabilities in Red Hat Advanced Cluster Security for Kubernetes by using the API.

For these examples, workloads are composed of deployments and their associated images. The export uses the `/v1/export/vuln-mgmt/workloads` streaming API. It allows the combined export of deployments and images. The `images` payload contains the full vulnerability information. The output is streamed and has the following schema:

``` json
{"result": {"deployment": {...}, "images": [...]}}
...
{"result": {"deployment": {...}, "images": [...]}}
```

The following examples assume that these environment variables have been set:

- `ROX_API_TOKEN`: API token with `view` permissions for the `Deployment` and `Image` resources

- `ROX_ENDPOINT`: Endpoint under which Central’s API is available

- To export all workloads, enter the following command:

  ``` terminal
  $ curl -H "Authorization: Bearer $ROX_API_TOKEN" $ROX_ENDPOINT/v1/export/vuln-mgmt/workloads
  ```

- To export all workloads with a query timeout of 60 seconds, enter the following command:

  ``` terminal
  $ curl -H "Authorization: Bearer $ROX_API_TOKEN" $ROX_ENDPOINT/v1/export/vuln-mgmt/workloads?timeout=60
  ```

- To export all workloads matching the query `Deployment:app Namespace:default`, enter the following command:

  ``` terminal
  $ curl -H "Authorization: Bearer $ROX_API_TOKEN" $ROX_ENDPOINT/v1/export/vuln-mgmt/workloads?query=Deployment%3Aapp%2BNamespace%3Adefault
  ```

<div>

<div class="title">

Additional resources

</div>

- [Searching and filtering](../search-filter.md)

</div>
