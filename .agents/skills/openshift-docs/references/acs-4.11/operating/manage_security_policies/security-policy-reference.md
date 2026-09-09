<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use policy categories to manage your policies. Security criteria are available to use in building custom policies. Different criteria are available, depending on the policy lifecycle stage. Lists of default security policies, or policies that are included in the system by default, are provided and organized by severity.

<a id="con-policy-categories_security-policy-reference"></a>

# Policy categories

RHACS uses policy categories to group policies by type and function. You can use these categories to organize and search for policies.

RHACS provides the following default policy categories:

- Anomalous Activity

- Cryptocurrency Mining

- DevOps Best Practices

- Docker Center for Internet Security (CIS)

- File Activity Monitoring

- Kubernetes

- Kubernetes Events

- Network Tools

- Package Management

- Privileges

- Security Best Practices

- Supply Chain Security

- System Modification

- Vulnerability Management

- Zero Trust

You can view existing categories and create your own policy categories in the RHACS portal by using the **Policy Categories** tab in the **Policy Management** window.

<a id="policy-criteria_security-policy-reference"></a>

# Policy criteria

You can set up rules in RHACS and configure the data on which you want to trigger a policy. This data is also referred to as *policy criteria* or *policy fields*.

You can configure the policy based on the attributes listed in the following table.

In this table:

- The **Regular expressions**, **AND, OR**, and **NOT** columns indicate whether you can use regular expressions and other logical operators along with the specific attribute.

  - `!` for **Regex** (Regular expressions) indicates that you can only use regular expressions for the listed fields.

  - `!` for **AND**, or **OR** indicates that you can only use the mentioned logical operator for the attribute.

  - ✕ in the **Regex** / **NOT** / **AND, OR** column indicates that the attribute does not support any of those (regex, negation, logical operators).

- The **RHACS version** column indicates the version of Red Hat Advanced Cluster Security for Kubernetes that you must have to use the attribute.

- You cannot use logical combination operators `AND` and `OR` for attributes that have:

  - Boolean values `true` and `false`

  - Minimum-value semantics, for example:

    - **Minimum RBAC permissions**

    - **Days since image was created**

- You cannot use the `NOT` logical operator for attributes that have:

  - Boolean values `true` and `false`

  - Numeric values that already use comparison, such as the `<`, `>`, `<=`, `>=` operators.

  - Compound criteria that can have multiple values, for example:

    - **Dockerfile line**, which includes both instructions and arguments.

    - **Environment variable**, which consists of both name and value.

  - Other meanings, including **Add capabilities**, **Drop capabilities**, **Days since image was created**, and **Days since image was last scanned**.

<a id="reference-image-criteria_security-policy-reference"></a>

## Image criteria

Image registry  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Image registry</p></td>
<td style="text-align: left;"><p>The name of the image registry.</p></td>
<td style="text-align: left;"><p>Image Registry</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image name</p></td>
<td style="text-align: left;"><p>The full name of the image in registry, for example <code>library/nginx</code>.</p></td>
<td style="text-align: left;"><p>Image Remote</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image tag</p></td>
<td style="text-align: left;"><p>Identifier for an image.</p></td>
<td style="text-align: left;"><p>Image Tag</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Require image signature</p></td>
<td style="text-align: left;"><p>The list of signature integrations you can use to verify an image’s signature. Create alerts on images that either do not have a signature or their signature is not verifiable by at least one of the provided signature integrations.</p></td>
<td style="text-align: left;"><p>Image Signature Verified By</p></td>
<td style="text-align: left;"><p>A valid ID of an already configured image signature integration</p></td>
<td style="text-align: center;"><p>! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

Image contents  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Image age</p></td>
<td style="text-align: left;"><p>The minimum number of days from image creation date.</p></td>
<td style="text-align: left;"><p>Image Age</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image user</p></td>
<td style="text-align: left;"><p>Matches the USER directive in the Dockerfile. See <a href="https://docs.docker.com/engine/reference/builder/#user">https://docs.docker.com/engine/reference/builder/#user</a> for details .</p></td>
<td style="text-align: left;"><p>Image User</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Dockerfile line</p></td>
<td style="text-align: left;"><p>A specific line in the Dockerfile, including both instructions and arguments.</p></td>
<td style="text-align: left;"><p>Dockerfile Line</p></td>
<td style="text-align: left;"><p>One of: LABEL, RUN, CMD, EXPOSE, ENV, ADD, COPY, ENTRYPOINT, VOLUME, USER, WORKDIR, ONBUILD</p></td>
<td style="text-align: center;"><p>! Regex only for values,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image component</p></td>
<td style="text-align: left;"><p>Name and version number of a specific software component present in an image.</p></td>
<td style="text-align: left;"><p>Image Component</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image OS</p></td>
<td style="text-align: left;"><p>Name and version number of the base operating system of the image. For example, <code>alpine:3.17.3</code></p></td>
<td style="text-align: left;"><p>Image OS</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Require image label</p></td>
<td style="text-align: left;"><p>Ensure the presence of a Docker image label. The policy triggers if any image in the deployment does not have the specified label. You can use regular expressions for both key and value fields to match labels. The <code>Require Image Label</code> policy criteria only works when you integrate with a Docker registry. For details about Docker labels see Docker documentation, <a href="https://docs.docker.com/config/labels-custom-metadata/">https://docs.docker.com/config/labels-custom-metadata/</a>.</p></td>
<td style="text-align: left;"><p>Required Image Label</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Disallow image label</p></td>
<td style="text-align: left;"><p>Ensure that a particular Docker image label is NOT used. The policy triggers if any image in the deployment has the specified label. You can use regular expressions for both key and value fields to match labels. The 'Disallow Image Label policy' criteria only works when you integrate with a Docker registry. For details about Docker labels see Docker documentation, <a href="https://docs.docker.com/config/labels-custom-metadata/">https://docs.docker.com/config/labels-custom-metadata/</a>.</p></td>
<td style="text-align: left;"><p>Disallowed Image Label</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

Image scanning  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Image scan age</p></td>
<td style="text-align: left;"><p>The minimum number of days since the image was last scanned.</p></td>
<td style="text-align: left;"><p>Image Scan Age</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Image scan status</p></td>
<td style="text-align: left;"><p>Check if an image was scanned.</p></td>
<td style="text-align: left;"><p>Unscanned Image</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Common Vulnerability Scoring System (CVSS)</p></td>
<td style="text-align: left;"><p>CVSS: Use it to match images with vulnerabilities whose scores are greater than <code>&gt;</code>, less than <code>&lt;</code>, or equal to <code>=</code> the specified CVSS.</p></td>
<td style="text-align: left;"><p>CVSS</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, &lt;=, &gt;= or nothing (which implies equal to)  — and —  a decimal (a number with an optional fractional value).</p>
<p>Examples: &gt;=5, or 9.5</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>National Vulnerability Database (NVD) CVSS</p></td>
<td style="text-align: left;"><p>Requires Scanner V4. NVD CVSS: Use it to match images with vulnerabilities reported by NVD whose scores are greater than <code>&gt;</code>, less than <code>&lt;</code>, or equal to <code>=</code> the specified CVSS.</p></td>
<td style="text-align: left;"><p>CVSS</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, &lt;=, &gt;= or nothing (which implies equal to)  — and —  a decimal (a number with an optional fractional value).</p>
<p>Examples: &gt;=5, or 9.5</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Severity</p></td>
<td style="text-align: left;"><p>The severity of the vulnerability based on the CVSS or the vendor. Can be one of Low, Moderate, Important or Critical.</p></td>
<td style="text-align: left;"><p>Severity</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, ⇐, &gt;= or nothing (which implies equal to)  — and —  One of: UNKNOWN LOW MODERATE IMPORTANT CRITICAL</p>
<p>Examples: &gt;=IMPORTANT, or CRITICAL</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Fixable</p></td>
<td style="text-align: left;"><p>This criterion results in a violation only if the image in the deployment you are evaluating has a fixable CVE.</p></td>
<td style="text-align: left;"><p>Fixable</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Fixed by</p></td>
<td style="text-align: left;"><p>The version string of a package that fixes a flagged vulnerability in an image. This criterion may be used in addition to other criteria that identify a vulnerability, for example using the CVE criterion.</p></td>
<td style="text-align: left;"><p>Fixed By</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>CVE</p></td>
<td style="text-align: left;"><p>Common Vulnerabilities and Exposures, use it with specific CVE numbers.</p></td>
<td style="text-align: left;"><p>CVE</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex, NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Days since CVE was published</p></td>
<td style="text-align: left;"><p>This criterion results in a violation only if it has been more than a specified number of days since RHACS was first published.</p></td>
<td style="text-align: left;"><p>Days Since CVE Was First Published</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Days since CVE was first discovered in image</p></td>
<td style="text-align: left;"><p>This criterion results in a violation only if it has been more than a specified number of days since RHACS discovered the CVE in a specific image.</p></td>
<td style="text-align: left;"><p>Days Since CVE Was First Discovered In Image</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Days since CVE was first discovered in system</p></td>
<td style="text-align: left;"><p>This criterion results in a violation only if it has been more than a specified number of days since RHACS discovered the CVE across all deployed images in all clusters that RHACS monitors.</p></td>
<td style="text-align: left;"><p>Days Since CVE Was First Discovered In System</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Build</strong>,<br />
<strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Days since CVE fix was available</p></td>
<td style="text-align: left;"><p>This criterion results in a violation if it has been more than a specified number of days since the date when the CVE fix became available. Use this criterion to create a custom grace period for fixing vulnerabilities. For vulnerabilities that are associated with Red Hat packages, CVE fix dates are included in the vulnerability information. For non Red Hat packages, the fix date is approximated as follows:</p>
<ul>
<li><p>For existing CVEs, RHACS records the date that the status changed from <code>not fixable</code> to <code>fixable</code>.</p></li>
<li><p>For new and fixable CVEs, RHACS records the date that the CVE was discovered in RHACS.</p></li>
</ul></td>
<td style="text-align: left;"><p>Days Since CVE Fix Was Available</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>X</p></td>
<td style="text-align: left;"><p><strong>Build</strong>, <strong>Deploy</strong>, <strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

<a id="workload-config-criteria_security-policy-reference"></a>

## Workload configuration criteria

Container configuration  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Environment variable</p></td>
<td style="text-align: left;"><p>Check environment variables by name or value. When you create a policy that includes the environment variable attribute, you can choose which types of environment variables the policy should match. For example, you can specify raw values, which are provided directly in the deployment YAML, or you can specify references to values from config maps, secrets, fields, or resource requests or limits. For any type other than a raw value specified directly in the deployment YAML, the corresponding <code>value</code> attribute of the policy rule is ignored. In this case, the policy match is evaluated on the existence of the specified environment variable type. Additionally, this criteria disallows the creation of policies with a non-empty <code>value</code> attribute for types other than raw values.</p></td>
<td style="text-align: left;"><p>Environment Variable</p></td>
<td style="text-align: left;"><p>RAW=key=value to match an environment variable as directly specified in the deployment YAML with a specific key and value. You can omit the <code>value</code> attribute to match on only the key.</p>
<p>If the environment variable is not defined in the configuration YAML, then you can use the format <code>SOURCE=KEY</code>, where <code>SOURCE</code> is one of the following objects:</p>
<ul>
<li><p>SECRET_KEY (SecretKeyRef)</p></li>
<li><p>CONFIG_MAP_KEY (ConfigMapRef)</p></li>
<li><p>FIELD (FieldRef)</p></li>
<li><p>RESOURCE_FIELD (ResourceFieldRef)</p></li>
</ul>
<p>The preceding list provides the API object label first, and then provides the user interface label in parentheses.</p></td>
<td style="text-align: center;"><p>! Regex only for key and value (if using RAW)<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Container CPU request</p></td>
<td style="text-align: left;"><p>Check for the number of cores reserved for a given resource.</p></td>
<td style="text-align: left;"><p>Container CPU Request</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, ⇐, &gt;= or nothing (which implies equal to)  — and —  A decimal (a number with an optional fractional value)</p>
<p>Examples: &gt;=5, or 9.5</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Container CPU limit</p></td>
<td style="text-align: left;"><p>Check for the maximum number of cores a resource is allowed to use.</p></td>
<td style="text-align: left;"><p>Container CPU Limit</p></td>
<td style="text-align: left;"><p>(Same as Container CPU Request)</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Container memory request</p></td>
<td style="text-align: left;"><p>Number, including fraction, of MB requested.</p></td>
<td style="text-align: left;"><p>Container Memory Request</p></td>
<td style="text-align: left;"><p>(Same as Container CPU Request)</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Container memory limit</p></td>
<td style="text-align: left;"><p>Check for the maximum amount of memory a resource is allowed to use.</p></td>
<td style="text-align: left;"><p>Container Memory Limit</p></td>
<td style="text-align: left;"><p>(Same as Container CPU Request)</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Privileged container</p></td>
<td style="text-align: left;"><p>Check if a deployment is configured in privileged mode. This criterion only checks the value of the <code>privileged</code> field in the respective <a href="https://kubernetes.io/docs/reference/generated/kubernetes-api/v1.28/#securitycontext-v1-core">Pod Security Context</a>.</p></td>
<td style="text-align: left;"><p>Privileged Container</p></td>
<td style="text-align: left;"><p>Boolean: <code>true</code> when the value of the <code>privileged</code> field in the respective <code>PodSecurityContext</code> is set to <code>true</code></p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Root filesystem writeability</p></td>
<td style="text-align: left;"><p>Check if a deployment is configured in the <code>readOnlyFilesystem</code> mode.</p></td>
<td style="text-align: left;"><p>Read-Only Root Filesystem</p></td>
<td style="text-align: left;"><p>Boolean: <code>true</code> when the value of the <code>readOnlyRootFilesystem</code> field in the respective <code>PodSecurityContext</code> is set to <code>true</code></p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Seccomp profile type</p></td>
<td style="text-align: left;"><p>The type of <code>seccomp</code> profile defined for the deployment. If <code>seccomp</code> options are provided at both the pod and container level, the container options override the pod options. See <a href="https://kubernetes.io/docs/reference/kubernetes-api/workload-resources/pod-v1/#security-context-1">Security Context</a>.</p></td>
<td style="text-align: left;"><p>Seccomp Profile Type</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>UNCONFINED RUNTIME_DEFAULT LOCALHOST</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Privilege escalation</p></td>
<td style="text-align: left;"><p>Provides alerts when a deployment allows a container process to gain more privileges than its parent process.</p></td>
<td style="text-align: left;"><p>Allow Privilege Escalation</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Drop capabilities</p></td>
<td style="text-align: left;"><p>Linux capabilities that must be dropped from the container. Provides alerts when the specified capabilities are not dropped. For example, if configured with <code>SYS_ADMIN</code> AND <code>SYS_BOOT</code>, and the deployment drops only <em>one</em> or <em>neither</em> of these two capabilities, the alert occurs.</p></td>
<td style="text-align: left;"><p>Drop Capabilities</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>ALL AUDIT_CONTROL AUDIT_READ AUDIT_WRITE BLOCK_SUSPEND CHOWN DAC_OVERRIDE DAC_READ_SEARCH FOWNER FSETID IPC_LOCK IPC_OWNER KILL LEASE LINUX_IMMUTABLE MAC_ADMIN MAC_OVERRIDE MKNOD NET_ADMIN NET_BIND_SERVICE NET_BROADCAST NET_RAW SETGID SETFCAP SETPCAP SETUID SYS_ADMIN SYS_BOOT SYS_CHROOT SYS_MODULE SYS_NICE SYS_PACCT SYS_PTRACE SYS_RAWIO SYS_RESOURCE SYS_TIME SYS_TTY_CONFIG SYSLOG WAKE_ALARM</p></td>
<td style="text-align: center;"><p>AND</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Add capabilities</p></td>
<td style="text-align: left;"><p>Linux capabilities that must not be added to the container, such as the ability to send raw packets or override file permissions. Provides alerts when the specified capabilities are added. For example, if configured with <code>NET_ADMIN</code> or <code>NET_RAW</code>, and the deployment manifest YAML file includes at least one of these two capabilities, the alert occurs.</p></td>
<td style="text-align: left;"><p>Add Capabilities</p></td>
<td style="text-align: left;"><p>AUDIT_CONTROL<br />
AUDIT_READ<br />
AUDIT_WRITE<br />
BLOCK_SUSPEND<br />
CHOWN<br />
DAC_OVERRIDE<br />
DAC_READ_SEARCH<br />
FOWNER<br />
FSETID<br />
IPC_LOCK<br />
IPC_OWNER<br />
KILL<br />
LEASE<br />
LINUX_IMMUTABLE<br />
MAC_ADMIN<br />
MAC_OVERRIDE<br />
MKNOD<br />
NET_ADMIN<br />
NET_BIND_SERVICE<br />
NET_BROADCAST<br />
NET_RAW<br />
SETGID<br />
SETFCAP<br />
SETPCAP<br />
SETUID<br />
SYS_ADMIN<br />
SYS_BOOT<br />
SYS_CHROOT<br />
SYS_MODULE<br />
SYS_PACCT<br />
SYS_PTRACE<br />
SYS_RAWIO<br />
SYS_RESOURCE<br />
SYS_TIME<br />
SYS_TTY_CONFIG<br />
SYSLOG<br />
WAKE_ALARM<br />
</p></td>
<td style="text-align: center;"><p>OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Container name</p></td>
<td style="text-align: left;"><p>The name of the container.</p></td>
<td style="text-align: left;"><p>Container Name</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>AppArmor profile</p></td>
<td style="text-align: left;"><p>The Application Armor ("AppArmor") profile used in the container.</p></td>
<td style="text-align: left;"><p>AppArmor Profile</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Liveness probe</p></td>
<td style="text-align: left;"><p>Whether the container defines a liveness probe.</p></td>
<td style="text-align: left;"><p>Liveness Probe</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Readiness probe</p></td>
<td style="text-align: left;"><p>Whether the container defines a readiness probe.</p></td>
<td style="text-align: left;"><p>Readiness Probe</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

Deployment metadata  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Disallowed annotation</p></td>
<td style="text-align: left;"><p>An annotation which is not allowed to be present on Kubernetes resources in a specified environment.</p></td>
<td style="text-align: left;"><p>Disallowed Annotation</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Required label</p></td>
<td style="text-align: left;"><p>Check for the presence of a required label in Kubernetes.</p></td>
<td style="text-align: left;"><p>Required Label</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Required annotation</p></td>
<td style="text-align: left;"><p>Check for the presence of a required annotation in Kubernetes.</p></td>
<td style="text-align: left;"><p>Required Annotation</p></td>
<td style="text-align: left;"><p>key=value</p>
<p>Value is optional.</p>
<p>If value is missing, it must be in format "key=".</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime class</p></td>
<td style="text-align: left;"><p>The <code>RuntimeClass</code> of the deployment.</p></td>
<td style="text-align: left;"><p>Runtime Class</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Host network</p></td>
<td style="text-align: left;"><p>Check if <code>HostNetwork</code> is enabled which means that the container is not placed inside a separate network stack (for example, the container’s networking is not containerized). This implies that the container has full access to the host’s network interfaces.</p></td>
<td style="text-align: left;"><p>Host Network</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Host PID</p></td>
<td style="text-align: left;"><p>Check if the Process ID (PID) namespace is isolated between the containers and the host. This allows for processes in different PID namespaces to have the same PID.</p></td>
<td style="text-align: left;"><p>Host PID</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Host IPC</p></td>
<td style="text-align: left;"><p>Check if the IPC (POSIX/SysV IPC) namespace (which provides separation of named shared memory segments, semaphores and message queues) on the host is shared with containers.</p></td>
<td style="text-align: left;"><p>Host IPC</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Namespace</p></td>
<td style="text-align: left;"><p>The name of the namespace the deployment belongs to.</p></td>
<td style="text-align: left;"><p>Namespace</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Replicas</p></td>
<td style="text-align: left;"><p>The number of deployment replicas. If you use <code>oc scale</code> to scale the deployment replicas from 0 to a number, then the admission controller blocks this action if the deployment violates a policy.</p></td>
<td style="text-align: left;"><p>Replicas</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, ⇐, &gt;= or nothing (which implies equal to)  — and —  a decimal (a number with an optional fractional value).</p>
<p>Examples: &gt;=5, or 9.5</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

Storage  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Volume name</p></td>
<td style="text-align: left;"><p>Name of the storage.</p></td>
<td style="text-align: left;"><p>Volume Name</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Volume source path</p></td>
<td style="text-align: left;"><p>The volume’s path on the host.</p></td>
<td style="text-align: left;"><p>Volume Source</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Volume destination path</p></td>
<td style="text-align: left;"><p>The path where the volume is mounted.</p></td>
<td style="text-align: left;"><p>Volume Destination</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Volume type</p></td>
<td style="text-align: left;"><p>Indicates the form in which the volume is provisioned. For example, <code>persistentVolumeClaim</code> or <code>hostPath</code>.</p></td>
<td style="text-align: left;"><p>Volume Type</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Mounted volume writability</p></td>
<td style="text-align: left;"><p>Volumes that are mounted as writable.</p></td>
<td style="text-align: left;"><p>Writable Mounted Volume</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Mount propagation</p></td>
<td style="text-align: left;"><p>Check if container is mounting volumes in <code>Bidirectional</code>, <code>Host to Container</code>, or <code>None</code> modes.</p></td>
<td style="text-align: left;"><p>Mount Propagation</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>NONE HOSTTOCONTAINER BIDIRECTIONAL</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Host mount writability</p></td>
<td style="text-align: left;"><p>Resource has mounted a path on the host with write permissions.</p></td>
<td style="text-align: left;"><p>Writable Host Mount</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td colspan="6" style="text-align: left;"><p><strong>Section: Networking</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Exposed port protocol</p></td>
<td style="text-align: left;"><p>Protocol, such as TCP or UDP, that is used by the exposed port.</p></td>
<td style="text-align: left;"><p>Exposed Port Protocol</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Exposed node port</p></td>
<td style="text-align: left;"><p>Port numbers exposed externally by a deployment.</p></td>
<td style="text-align: left;"><p>Exposed Node Port</p></td>
<td style="text-align: left;"><p>(Same as Exposed Port)</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Exposed port</p></td>
<td style="text-align: left;"><p>Port numbers exposed by a deployment.</p></td>
<td style="text-align: left;"><p>Exposed Port</p></td>
<td style="text-align: left;"><p>&lt;, &gt;, ⇐, &gt;= or nothing (which implies equal to)  — and —  an integer.</p>
<p>Examples: &gt;=1024, or 22</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Port exposure method</p></td>
<td style="text-align: left;"><p>Exposure method of the service, for example, load balancer or node port.</p></td>
<td style="text-align: left;"><p>Port Exposure Method</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>Route LoadBalancer NodePort HostPort Exposure type is not set</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Ingress network policy</p></td>
<td style="text-align: left;"><p>Check the presence or absence of ingress Kubernetes network policies.</p></td>
<td style="text-align: left;"><p>Has Ingress Network Policy</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Egress network policy</p></td>
<td style="text-align: left;"><p>Check the presence or absence of egress Kubernetes network policies.</p></td>
<td style="text-align: left;"><p>Has Egress Network Policy</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>Regex, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

Access control  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Service account</p></td>
<td style="text-align: left;"><p>The name of the service account.</p></td>
<td style="text-align: left;"><p>Service Account</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Automount service account token</p></td>
<td style="text-align: left;"><p>Check if the deployment configuration automatically mounts the service account token.</p></td>
<td style="text-align: left;"><p>Automount Service Account Token</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Minimum RBAC permissions</p></td>
<td style="text-align: left;"><p>Match if the deployment’s Kubernetes service account has Kubernetes RBAC permission level equal to <code>=</code> or greater than <code>&gt;</code> the specified level.</p></td>
<td style="text-align: left;"><p>Minimum RBAC Permissions</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>DEFAULT ELEVATED_IN_NAMESPACE ELEVATED_CLUSTER_WIDE CLUSTER_ADMIN</p></td>
<td style="text-align: center;"><p>NOT</p></td>
<td style="text-align: left;"><p><strong>Deploy</strong>,<br />
<strong>Runtime</strong> (when used with a Runtime criterion)</p></td>
</tr>
</tbody>
</table>

<a id="reference-workload-activity-criteria_security-policy-reference"></a>

## Workload activity criteria

Process activity  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Process name</p></td>
<td style="text-align: left;"><p>Name of the process executed in a deployment.</p></td>
<td style="text-align: left;"><p>Process Name</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Process</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Process ancestor</p></td>
<td style="text-align: left;"><p>Name of any parent process for a process executed in a deployment.</p></td>
<td style="text-align: left;"><p>Process Ancestor</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Process</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Process arguments</p></td>
<td style="text-align: left;"><p>Command arguments for a process executed in a deployment.</p></td>
<td style="text-align: left;"><p>Process Arguments</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Process</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Process UID</p></td>
<td style="text-align: left;"><p>Unix user ID for a process executed in a deployment.</p></td>
<td style="text-align: left;"><p>Process UID</p></td>
<td style="text-align: left;"><p>Integer</p></td>
<td style="text-align: center;"><p>NOT, AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Process</p></td>
</tr>
</tbody>
</table>

Baseline deviation  

| **Attribute** | **Description** | **JSON Attribute** | **Allowed Values** | **Regex**, **NOT**, **AND, OR** | **Phase** |
|----|----|----|----|----|----|
| Unexpected network flow detected | Check if the detected network traffic is part of the network baseline for the deployment. | Unexpected Network Flow Detected | Boolean | ✕ | **Runtime** ONLY - Network |
| Unexpected process executed | Check deployments for which process executions are not listed in the deployment’s locked process baseline. | Unexpected Process Executed | Boolean | ✕ | **Runtime** ONLY - Process |

User issued container commands  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Kubernetes action</p></td>
<td style="text-align: left;"><p>The name of the Kubernetes action, such as <code>Pod Exec</code>.</p></td>
<td style="text-align: left;"><p>Kubernetes Resource</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>PODS_ATTACH PODS_EXEC PODS_PORTFORWARD</p></td>
<td style="text-align: center;"><p>! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Kubernetes Events</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes API verb</p></td>
<td style="text-align: left;"><p>Do not use; not valid for runtime policies.</p></td>
<td style="text-align: left;"><p>Kubernetes API Verb</p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: center;"><p>N/A</p></td>
<td style="text-align: left;"><p>N/A</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes user name</p></td>
<td style="text-align: left;"><p>The name of the user who accessed the resource.</p></td>
<td style="text-align: left;"><p>Kubernetes User Name</p></td>
<td style="text-align: left;"><p>Alphanumeric with hyphens (-) and colon (:) only</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Kubernetes Events</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes user group</p></td>
<td style="text-align: left;"><p>The name of the group to which the user who accessed the resource belongs to.</p></td>
<td style="text-align: left;"><p>Kubernetes User Groups</p></td>
<td style="text-align: left;"><p>Alphanumeric with hyphens (-) and colon (:) only</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Kubernetes Events</p></td>
</tr>
</tbody>
</table>

File activity  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Effective path</p></td>
<td style="text-align: left;"><p>The file path as it appears to the process inside the container.</p></td>
<td style="text-align: left;"><p>Effective Path</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>/etc/passwd /etc/ssh/sshd_config /etc/shadow /etc/sudoers</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Actual path</p></td>
<td style="text-align: left;"><p>The physical location of the file on the file system of the node.</p></td>
<td style="text-align: left;"><p>Actual Path</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>/etc/passwd /etc/ssh/sshd_config /etc/shadow /etc/sudoers</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>File operation</p></td>
<td style="text-align: left;"><p>The specific action performed on the file, such as creating, deleting, or modifying permissions and ownership. When using the File operation criteria, you must specify at least one value for either Effective path or Actual path.</p></td>
<td style="text-align: left;"><p>File Operation</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>Open (Writable) Create Delete Permission change Ownership change</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong></p></td>
</tr>
</tbody>
</table>

<a id="kube-resource-operations_security-policy-reference"></a>

## Audit log: Kubernetes resource operations

You can also use cluster and namespace label scoping; see "Configuring policy resources" for more information.

Resource operation (Required)  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Kubernetes API verb</p></td>
<td style="text-align: left;"><p>The Kubernetes API verb that is used to access the resource, such as <code>GET</code> or <code>POST</code>.</p></td>
<td style="text-align: left;"><p>Kubernetes API Verb</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>CREATE DELETE GET PATCH UPDATE</p></td>
<td style="text-align: center;"><p>! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes resource type</p></td>
<td style="text-align: left;"><p>Type of the accessed Kubernetes resource.</p></td>
<td style="text-align: left;"><p>Kubernetes Resource</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>CONFIGMAPS SECRETS CLUSTERROLES CLUSTERROLEBINDINGS NETWORKPOLICIES SECURITYCONTEXTCONSTRAINTS EGRESSFIREWALLS</p></td>
<td style="text-align: center;"><p>! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
</tbody>
</table>

Resource attributes  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Kubernetes resource name</p></td>
<td style="text-align: left;"><p>The name of the accessed Kubernetes resource.</p></td>
<td style="text-align: left;"><p>Kubernetes Resource Name</p></td>
<td style="text-align: left;"><p>Alphanumeric with hyphens (-) and colon (:) only</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes user name</p></td>
<td style="text-align: left;"><p>The name of the user who accessed the resource.</p></td>
<td style="text-align: left;"><p>Kubernetes User Name</p></td>
<td style="text-align: left;"><p>Alphanumeric with hyphens (-) and colon (:) only</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Kubernetes Events</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Kubernetes user groups</p></td>
<td style="text-align: left;"><p>The name of the group to which the user who accessed the resource belongs to.</p></td>
<td style="text-align: left;"><p>Kubernetes User Groups</p></td>
<td style="text-align: left;"><p>Alphanumeric with hyphens (-) and colon (:) only</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Kubernetes Events</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>User agent</p></td>
<td style="text-align: left;"><p>The user agent that the user used to access the resource. For example <code>oc</code>, or <code>kubectl</code>.</p></td>
<td style="text-align: left;"><p>User Agent</p></td>
<td style="text-align: left;"><p>String</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Source IP address</p></td>
<td style="text-align: left;"><p>The IP address from which the user accessed the resource.</p></td>
<td style="text-align: left;"><p>Source IP Address</p></td>
<td style="text-align: left;"><p>IPV4 or IPV6 address</p></td>
<td style="text-align: center;"><p>Regex,<br />
NOT,<br />
! <code>OR</code> only</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Is impersonated user</p></td>
<td style="text-align: left;"><p>Check if the request was made by a user that is impersonated by a service account or some other account.</p></td>
<td style="text-align: left;"><p>Is Impersonated User</p></td>
<td style="text-align: left;"><p>Boolean</p></td>
<td style="text-align: center;"><p>✕</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong> ONLY - Audit Log</p></td>
</tr>
</tbody>
</table>

<a id="node-activity-criteria_security-policy-reference"></a>

## Node activity criteria

File activity  

<table style="width:100%;">
<colgroup>
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
<col style="width: 16%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;"><strong>Attribute</strong></th>
<th style="text-align: left;"><strong>Description</strong></th>
<th style="text-align: left;"><strong>JSON Attribute</strong></th>
<th style="text-align: left;"><strong>Allowed Values</strong></th>
<th style="text-align: center;"><strong>Regex</strong>, <strong>NOT</strong>, <strong>AND, OR</strong></th>
<th style="text-align: left;"><strong>Phase</strong></th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Actual path</p></td>
<td style="text-align: left;"><p>The physical location of the file on the file system of the node or the underlying mount.</p></td>
<td style="text-align: left;"><p>Actual Path</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>/etc/passwd /etc/ssh/sshd_config /etc/shadow /etc/sudoers</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong></p></td>
</tr>
<tr>
<td style="text-align: left;"><p>File operation</p></td>
<td style="text-align: left;"><p>The specific action performed on the file, such as creating, deleting, or modifying permissions and ownership. When using the File operation criteria, you must specify at least one value for the Actual path.</p></td>
<td style="text-align: left;"><p>File Operation</p></td>
<td style="text-align: left;"><p>One of:</p>
<p>Open (Writable) Create Delete Permission change Ownership change</p></td>
<td style="text-align: center;"><p>AND, OR</p></td>
<td style="text-align: left;"><p><strong>Runtime</strong></p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Configuring policy rules](custom-security-policies.md#configure-policy-rules_custom-security-policies)

</div>

<a id="default-security-policies_security-policy-reference"></a>

# Default security policies

The default security policies in Red Hat Advanced Cluster Security for Kubernetes provide broad coverage to identify security issues and ensure best practices for security in your environment. By configuring those policies, you can automatically prevent high-risk service deployments in your environment and respond to runtime security incidents.

> [!NOTE]
> The severity levels for policies in Red Hat Advanced Cluster Security for Kubernetes are different from the severity levels that Red Hat Product Security assigns.
>
> The Red Hat Advanced Cluster Security for Kubernetes policy severity levels are Critical, High, Medium, and Low. Red Hat Product Security rates vulnerability severity levels as Critical, Important, Moderate, and Low.
>
> While a policy’s severity level and the Red Hat Product Security severity levels can interact, it is important to distinguish between them. For more information about the Red Hat Product Security severity levels, see [Severity Ratings](https://access.redhat.com/security/updates/classification).

<a id="critical-sev-security-policies_security-policy-reference"></a>

## Critical severity security policies

The following table lists the default security policies in Red Hat Advanced Cluster Security for Kubernetes that are of critical severity. The policies are organized by lifecycle stage.

| Life cycle stage | Name | Description | Status |
|----|----|----|----|
| Build or Deploy | Apache Struts: CVE-2017-5638 | Alerts when deployments have images that contain the CVE-2017-5638 Apache Struts vulnerability. | Enabled |
| Build or Deploy | Log4Shell: log4j Remote Code Execution vulnerability | Alerts when deployments include images that contain the CVE-2021-44228 and CVE-2021-45046 Log4Shell vulnerabilities. Flaws exist in the Apache Log4j Java logging library in versions 2.0-beta9 - 2.15.0, excluding version 2.12.2. | Enabled |
| Build or Deploy | Spring4Shell (Spring Framework Remote Code Execution) and Spring Cloud Function vulnerabilities | Alerts when deployments include images that contain either the CVE-2022-22965 vulnerability, which affects Spring MVC, and the CVE-2022-22963 vulnerability, which affects Spring Cloud. In versions 3.16, 3.2.2, and older unsupported versions, Spring Cloud contains flaws. Flaws exist in Spring Framework in versions 5.3.0 - 5.3.17, versions 5.2.0 - 5.2.19, and in older unsupported versions. | Enabled |
| Runtime | Iptables Executed in Privileged Container | Alerts when privileged pods run iptables. | Enabled |

Critical severity security policies

<a id="high-sev-security-policies_security-policy-reference"></a>

## High severity security policies

The following table lists the default security policies in Red Hat Advanced Cluster Security for Kubernetes that are of high severity. The policies are organized by lifecycle stage.

<table>
<caption>High severity security policies</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
<col style="width: 25%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Life cycle stage</th>
<th style="text-align: left;">Name</th>
<th style="text-align: left;">Description</th>
<th style="text-align: left;">Status</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p>Build or Deploy</p></td>
<td style="text-align: left;"><p>Fixable Common Vulnerability Scoring System (CVSS) &gt;= 7</p></td>
<td style="text-align: left;"><p>Alerts when deployments with fixable vulnerabilities have a CVSS of at least 7. However, Red Hat recommends that you create policies using Common Vulnerabilities and Exposures (CVE) severity instead of CVSS score.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Build or Deploy</p></td>
<td style="text-align: left;"><p>Fixable Severity at least Important</p></td>
<td style="text-align: left;"><p>Alerts when deployments with fixable vulnerabilities have a severity rating of at least Important.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Build or Deploy</p></td>
<td style="text-align: left;"><p>Rapid Reset: Denial of Service Vulnerability in HTTP/2 Protocol</p></td>
<td style="text-align: left;"><p>Alerts on deployments with images containing components that are susceptible to a Denial of Service (DoS) vulnerability for HTTP/2 servers. This addresses a flaw in the handling of multiplexed streams in HTTP/2. A client can rapidly create a request and immediately reset them, which creates extra work for the server while avoiding hitting any server-side limits, resulting in a denial of service attack. To use this policy, consider cloning the policy and adding the <code>Fixable</code> policy criteria before enabling it.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Build or Deploy</p></td>
<td style="text-align: left;"><p>Secure Shell (ssh) Port Exposed in Image</p></td>
<td style="text-align: left;"><p>Alerts when deployments expose port 22, which is commonly reserved for SSH access.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Build or Deploy</p></td>
<td style="text-align: left;"><p>Red Hat Images must be signed by the Red Hat Release Key</p></td>
<td style="text-align: left;"><p>Alerts when a Red Hat image is not signed by the official <a href="https://access.redhat.com/security/team/key">Red Hat product signing key, "Release Key 3"</a>. These alerts apply to images from the following registries and remotes:</p>
<ul>
<li><p><code>registry.redhat.io</code></p></li>
<li><p><code>registry.access.redhat.com</code></p></li>
<li><p><code>quay.io/openshift-release-dev/ocp-release</code></p></li>
<li><p><code>quay.io/openshift-release-dev/ocp-v4.0-art-dev</code></p></li>
</ul></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Emergency Deployment Annotation</p></td>
<td style="text-align: left;"><p>Alerts when deployments use the emergency annotation, such as "admission.stackrox.io/break-glass":"ticket-1234" to circumvent StackRox Admission controller checks.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Environment Variable Contains Secret</p></td>
<td style="text-align: left;"><p>Alerts when deployments have environment variables that contain 'SECRET'.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Fixable CVSS &gt;= 6 and Privileged</p></td>
<td style="text-align: left;"><p>Alerts when deployments run in privileged mode with fixable vulnerabilities that have a CVSS of at least 6. However, Red Hat recommends that you create policies using CVE severity instead of CVSS score.</p></td>
<td style="text-align: left;"><p>Disabled by default in version 3.72.0 and later</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Privileged Containers with Important and Critical Fixable CVEs</p></td>
<td style="text-align: left;"><p>Alerts when containers that run in privileged mode have important or critical fixable vulnerabilities.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Secret Mounted as Environment Variable</p></td>
<td style="text-align: left;"><p>Alerts when a deployment has a Kubernetes secret that is mounted as an environment variable.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Deploy</p></td>
<td style="text-align: left;"><p>Secure Shell (ssh) Port Exposed</p></td>
<td style="text-align: left;"><p>Alerts when deployments expose port 22, which is commonly reserved for SSH access.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Cryptocurrency Mining Process Execution</p></td>
<td style="text-align: left;"><p>Spawns the crypto-currency mining process.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>iptables Execution</p></td>
<td style="text-align: left;"><p>Detects when someone runs iptables, which is a deprecated way of managing network states in containers.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Kubernetes Actions: Attach to Pod</p></td>
<td style="text-align: left;"><p>Alerts when the Kubernetes API receives a request to attach to a container.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Kubernetes Actions: Exec into Pod</p></td>
<td style="text-align: left;"><p>Alerts when the Kubernetes API receives a request to run a command in a container.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Linux Group Add Execution</p></td>
<td style="text-align: left;"><p>Detects when someone runs the addgroup or groupadd binary to add a Linux group.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Linux User Add Execution</p></td>
<td style="text-align: left;"><p>Detects when someone runs the useradd or adduser binary to add a Linux user.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Login Binaries</p></td>
<td style="text-align: left;"><p>Indicates when someone tries to log in.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Network Management Execution</p></td>
<td style="text-align: left;"><p>Detects when someone runs binary files that can manipulate network configuration and management.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>nmap Execution</p></td>
<td style="text-align: left;"><p>Alerts when someone starts the nmap process in a container during run time.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>OpenShift: Kubeadmin Secret Accessed</p></td>
<td style="text-align: left;"><p>Alerts when someone accesses the kubeadmin secret.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Password Binaries</p></td>
<td style="text-align: left;"><p>Indicates when someone attempts to change a password.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Process Targeting Cluster Kubelet Endpoint</p></td>
<td style="text-align: left;"><p>Detects the misuse of the healthz, kubelet API, or heapster endpoint.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Process Targeting Cluster Kubernetes Docker Stats Endpoint</p></td>
<td style="text-align: left;"><p>Detects the misuse of the Kubernetes docker stats endpoint.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Process Targeting Kubernetes Service Endpoint</p></td>
<td style="text-align: left;"><p>Detects the misuse of the Kubernetes Service API endpoint.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Process with UID 0</p></td>
<td style="text-align: left;"><p>Alerts when deployments contain processes that run with UID 0.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Secure Shell Server (sshd) Execution</p></td>
<td style="text-align: left;"><p>Detects containers that run the SSH daemon.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>SetUID Processes</p></td>
<td style="text-align: left;"><p>Use setuid binary files, which permit people to run certain programs with escalated privileges.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Shadow File Modification</p></td>
<td style="text-align: left;"><p>Indicates when someone tries to modify shadow files.</p></td>
<td style="text-align: left;"><p>Disabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Shell Spawned by Java Application</p></td>
<td style="text-align: left;"><p>Detects when a shell, such as bash, csh, sh, or zsh, is run as a subprocess of a Java application.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Unauthorized Network Flow</p></td>
<td style="text-align: left;"><p>Generates a violation for any network flows that fall outside of the baselines of the "alert on anomalous violations" setting.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
<tr>
<td style="text-align: left;"><p>Runtime</p></td>
<td style="text-align: left;"><p>Unauthorized Processed Execution</p></td>
<td style="text-align: left;"><p>Generates a violation for any process execution that is not explicitly allowed by a locked process baseline for a container specification in a Kubernetes deployment.</p></td>
<td style="text-align: left;"><p>Enabled</p></td>
</tr>
</tbody>
</table>

<a id="medium-sev-security-policies_security-policy-reference"></a>

## Medium severity security policies

The following table lists the default security policies in Red Hat Advanced Cluster Security for Kubernetes that are of medium severity. The policies are organized by lifecycle stage.

| Life cycle stage | Name | Description | Status |
|----|----|----|----|
| Build | Docker CIS 4.4: Ensure images are scanned and rebuilt to include security patches | Alerts when images are not scanned and rebuilt to include security patches. It is important to scan images often to find vulnerabilities, rebuild the images to include security patches, and then instantiate containers for the images. | Disabled |
| Deploy | 30-Day Scan Age | Alerts when a deployment has not been scanned in 30 days. | Enabled |
| Deploy | CAP_SYS_ADMIN capability added | Alerts when a deployment includes containers that are escalating with CAP_SYS_ADMIN. | Enabled |
| Deploy | Container using read-write root filesystem | Alerts when a deployment includes containers that have read-write root file systems. | Disabled |
| Deploy | Container with privilege escalation allowed | Alerts when a container might be running with unintended privileges, creating a security risk. This situation can happen when a container process that has more privileges than its parent process allows the container to run with unintended privileges. | Enabled |
| Deploy | Deployments should have at least one Ingress Network Policy | Alerts if deployments are missing an Ingress Network Policy. | Disabled |
| Deploy | Deployments with externally exposed endpoints | Detects if a deployment has any service that is externally exposed through any methods. Deployments with services exposed outside of the cluster are at a higher risk of attempted intrusions because they are reachable outside of the cluster. This policy provides an alert so that you can verify that service exposure outside of the cluster is required. If the service is only needed for intra-cluster communication, use service type ClusterIP. | Disabled |
| Deploy | Docker CIS 5.1: Ensure that, if applicable, an AppArmor profile is enabled | Uses AppArmor to protect the Linux operating system and applications by enforcing a security policy that is known as an AppArmor profile. AppArmor is a Linux application security system that is available on some Linux distributions by default, such as Debian and Ubuntu. | Enabled |
| Deploy | Docker CIS 5.15: Ensure that the host’s process namespace is not shared | Creates process-level isolation between the containers and the host. The Process ID (PID) namespace isolates the process ID space, which means that processes in different PID namespaces can have the same PID. | Enabled |
| Deploy | Docker CIS 5.16: Ensure that the host’s IPC namespace is not shared | Alerts when the IPC namespace on the host is shared with containers. The IPC (POSIX/SysV IPC) namespace separates named shared memory segments, semaphores, and message queues. | Enabled |
| Deploy | Docker CIS 5.19: Ensure mount propagation mode is not enabled | Alerts when mount propagation mode is enabled. When mount propagation mode is enabled, you can mount container volumes in Bidirectional, Host to Container, and None modes. Do not use Bidirectional mount propagation mode unless it is explicitly needed. | Enabled |
| Deploy | Docker CIS 5.21: Ensure the default seccomp profile is not disabled | Alerts when the seccomp profile is disabled. The seccomp profile uses an allowlist to permit common system calls and blocks all others. | Disabled |
| Deploy | Docker CIS 5.7: Ensure privileged ports are not mapped within containers | Alerts when privileged ports are mapped within containers. The TCP/IP port numbers that are lower than 1024 are privileged ports. Normal users and processes can not use them for security reasons, but containers might map their ports to privileged ports. | Enabled |
| Deploy | Docker CIS 5.9 and 5.20: Ensure that the host’s network namespace is not shared | Alerts when the host’s network namespace is shared. When HostNetwork is enabled, the container is not placed inside a separate network stack, and the container’s networking is not containerized. As a result, the container has full access to the host’s network interfaces, and a shared UTS namespace is enabled. The UTS namespace provides isolation between the hostname and the NIS domain name, and it sets the hostname and the domain, which are visible to running processes in that namespace. Processes that run within containers do not typically require to know the hostname or the domain name, so the UTS namespace should not be shared with the host. | Enabled |
| Deploy | Images with no scans | Alerts when a deployment includes images that were not scanned. | Disabled |
| Runtime | Kubernetes Actions: Port Forward to Pod | Alerts when the Kubernetes API receives a port forward request. | Enabled |
| Deploy | Mount Container Runtime Socket | Alerts when a deployment has a volume mount on the container runtime socket. | Enabled |
| Deploy | Mounting Sensitive Host Directories | Alerts when a deployment mounts sensitive host directories. | Enabled |
| Deploy | No resource requests or limits specified | Alerts when a deployment includes containers that do not have resource requests and limits. | Enabled |
| Deploy | Pod Service Account Token Automatically Mounted | Protects pod default service account tokens from being compromised by minimizing the mounting of the default service account token to only those pods whose applications require interaction with the Kubernetes API. | Enabled |
| Deploy | Privileged Container | Alerts when a deployment includes containers that run in privileged mode. | Enabled |
| Runtime | crontab Execution | Detects the usage of the crontab scheduled jobs editor. | Enabled |
| Runtime | Netcat Execution Detected | Detects when netcat runs in a container. | Enabled |
| Runtime | OpenShift: Advanced Cluster Security Central Admin Secret Accessed | Alerts when someone accesses the Red Hat Advanced Cluster Security Central secret. | Enabled |
| Runtime | OpenShift: Kubernetes Secret Accessed by an Impersonated User | Alerts when someone impersonates a user to access a secret in the cluster. | Enabled |
| Runtime | Remote File Copy Binary Execution | Alerts when a deployment runs a remote file copy tool. | Enabled |

Medium severity security policies

<a id="low-sev-security-policies_security-policy-reference"></a>

## Low severity security policies

The following table lists the default security policies in Red Hat Advanced Cluster Security for Kubernetes that are of low severity. The policies are organized by lifecycle stage.

| Life cycle stage | Name | Description | Status |
|----|----|----|----|
| Build or Deploy | 90-Day Image Age | Alerts when a deployment has not been updated in 90 days. | Enabled |
| Build or Deploy | ADD Command used instead of COPY | Alerts when an image was built by using an `ADD` command. | Disabled |
| Build or Deploy | Alpine Linux Package Manager (apk) in Image | Alerts when a deployment includes the Alpine Linux package manager (apk). | Enabled |
| Build or Deploy | Curl in Image | Alerts when a deployment includes curl. | Disabled |
| Build or Deploy | Docker CIS 4.1: Ensure That a User for the Container Has Been Created | Ensures that containers are running as non-root users. | Enabled |
| Build or Deploy | Docker CIS 4.7: Alert on Update Instruction | Ensures that update instructions are not used alone in the Dockerfile. | Enabled |
| Build or Deploy | Insecure specified in CMD | Alerts when a deployment uses 'insecure' in the command. | Enabled |
| Build or Deploy | Latest tag | Alerts when a deployment includes images that use the 'latest' tag. | Enabled |
| Build or Deploy | Red Hat Package Manager in Image | Alerts when a deployment includes components of the Red Hat, Fedora, or CentOS package management system. | Enabled |
| Build or Deploy | Required Image Label | Alerts when a deployment includes images that are missing the specified label. | Disabled |
| Build or Deploy | Ubuntu Package Manager Execution | Detects the usage of the Ubuntu package management system. | Enabled |
| Build or Deploy | Ubuntu Package Manager in Image | Alerts when a deployment includes components of the Debian or Ubuntu package management system in the image. | Enabled |
| Build or Deploy | Wget in Image | Alerts when a deployment includes wget. | Disabled |
| Deploy | Drop All Capabilities | Alerts when a deployment does not drop all capabilities. | Disabled |
| Deploy | Improper Usage of Orchestrator Secrets Volume | Alerts when a deployment uses a Dockerfile with 'VOLUME /run/secrets'. | Enabled |
| Deploy | Kubernetes Dashboard Deployed | Alerts when a Kubernetes dashboard service is detected. | Enabled |
| Deploy | Required Annotation: Email | Alerts when a deployment is missing the 'email' annotation. | Disabled |
| Deploy | Required Annotation: Owner/Team | Alerts when a deployment is missing the 'owner' or 'team' annotation. | Disabled |
| Deploy | Required Label: Owner/Team | Alerts when a deployment is missing the 'owner' or 'team' label. | Disabled |
| Runtime | Alpine Linux Package Manager Execution | Alerts when the Alpine Linux package manager (apk) is run at run time. | Enabled |
| Runtime | chkconfig Execution | Detects the usage of the ckconfig service manager, which is typically not used in a container. | Enabled |
| Runtime | Compiler Tool Execution | Alerts when binary files that compile software are run at run time. | Enabled |
| Runtime | Red Hat Package Manager Execution | Alerts when Red Hat, Fedora, or CentOS package manager programs are run at run time. | Enabled |
| Runtime | Shell Management | Alerts when commands are run to add or remove a shell. | Disabled |
| Runtime | systemctl Execution | Detects the usage of the systemctl service manager. | Enabled |
| Runtime | systemd Execution | Detects the usage of the systemd service manager. | Enabled |

Low severity security policies
