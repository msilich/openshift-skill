<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can configure advanced direct authentication fields in the `authentications.config.openshift.io` custom resource definition (CRD) to enable enhanced OIDC configurations, security enforcement, and flexible token validation for standalone and hosted control plane (HCP) clusters.

> [!IMPORTANT]
> Advanced direct authentication fields is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

# About advanced direct authentication fields

Advanced direct authentication fields provide flexibility and security for OIDC-based authentication in OpenShift Container Platform. You can configure advanced OIDC settings, implement custom token validation logic, and enforce security policies on usernames and groups.

The following capabilities are available:

Custom OIDC discovery URL
Specify a custom OIDC discovery endpoint when your identity provider does not use the standard discovery URL format. Useful for complex networking setups or non-standard identity providers.

CEL-based claim mapping
Use Common Expression Language (CEL) expressions to construct usernames and groups from JWT token claims with fallback logic. This addresses scenarios where different user types require varying claim mappings.

Claim validation rules
Use CEL expressions to implement advanced token validation logic, such as enforcing maximum token lifetimes, validating multiple claims, or implementing custom security policies.

User validation rules
Enforce security policies on usernames and groups extracted from tokens to prevent privilege escalation by blocking reserved system usernames and group prefixes.

These fields extend the base OIDC authentication configuration introduced in OpenShift Container Platform 4.14. You must first configure an external OIDC identity provider before using these advanced fields.

These fields require the `TechPreviewNoUpgrade` feature set to be enabled. They are available on standalone OpenShift Container Platform clusters and hosted control plane (HCP) environments.

> [!IMPORTANT]
> These advanced authentication fields are available as a Technology Preview feature. Ensure you have a backup authentication method, such as a certificate-based kubeconfig file, before configuring these fields.

# Configuring a custom OIDC discovery URL

Configure a custom OIDC discovery URL when your identity provider does not follow the standard discovery endpoint format.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an external OIDC identity provider for direct authentication.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `authentication-discovery-url.yaml` with your custom discovery URL configuration:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Authentication
    metadata:
      name: cluster
    spec:
      type: OIDC
      oidcProviders:
      - name: my-oidc-provider
        issuer:
          issuerURL: https://idp.example.com
          discoveryURL: https://custom-discovery.example.com/.well-known/openid-configuration
          audiences:
          - my-audience
        claimMappings:
          username:
            claim: email
    ```

    where:

    `issuerURL`
    Specifies the issuer URL displayed in JWT token `iss` claim.

    `discoveryURL`
    Specifies the custom OIDC discovery endpoint URL. Must differ from `issuerURL`, use HTTPS, and must not contain query parameters, fragments, or user info. Maximum length: 2048 characters.

    > [!NOTE]
    > Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `https://custom-discovery.example.com/.well-known/openid-configuration`, `my-audience`) with your actual OIDC provider configuration.

2.  Apply the configuration:

    ``` terminal
    $ oc apply -f authentication-discovery-url.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Monitor the cluster authentication Operator status to ensure the configuration is applied successfully:

  ``` terminal
  $ oc get clusteroperator authentication
  ```

  The Operator should report `Available=True` and `Degraded=False`.

- Check the cluster authentication Operator logs for any errors:

  ``` terminal
  $ oc logs -n openshift-authentication-operator deployments/authentication-operator
  ```

- Verify the kube-apiserver is using the custom discovery URL by checking the authentication configuration:

  ``` terminal
  $ oc get configmap kube-apiserver-to-kubelet-client-ca -n openshift-kube-apiserver -o yaml
  ```

  ``` terminal
  $ oc get authentication.config.openshift.io/cluster -o jsonpath='{.spec.oidcProviders[0].issuer.discoveryURL}'
  ```

  The output should display your custom discovery URL.

</div>

# Configuring CEL expressions for username and groups claim mapping

You can use Common Expression Language (CEL) expressions to construct usernames and groups from JWT token claims. This provides flexible claim mapping, including fallback logic when specific claims are not present.

<div>

<div class="title">

Prerequisites

</div>

- You have configured an external OIDC identity provider for direct authentication.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.

- You are familiar with CEL expression syntax.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `authentication-cel-mapping.yaml` with your CEL expression configuration:

    > [!IMPORTANT]
    > When using `expression`, do not set the `claim` field. You must use either `claim` or `expression`, but not both. Setting both will result in a validation error. Additionally, when using `expression`, do not set `prefixPolicy` to `Prefix`. Prefix policies are only compatible with `claim`-based mappings.

    > [!NOTE]
    > When using the `email` claim in CEL expressions, you must also validate `email_verified` to ensure the email address has been verified by the identity provider.

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Authentication
    metadata:
      name: cluster
    spec:
      type: OIDC
      oidcProviders:
      - name: my-oidc-provider
        issuer:
          issuerURL: https://idp.example.com
          audiences:
          - my-audience
        claimMappings:
          username:
            expression: 'claims.?upn.orValue(claims.?oid.orValue(claims.sub))'
          groups:
            expression: 'claims.?groups.orValue([])'
    # ...
    ```

    where:

    `username.expression`
    Specifies the fallback logic for username: `upn` if present, else `oid`, else `sub`.

    `groups.expression`
    Specifies that the `groups` claim is used if present, else an empty array.

    > [!NOTE]
    > Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`) with your actual OIDC provider configuration.

2.  Apply the configuration:

    ``` terminal
    $ oc apply -f authentication-cel-mapping.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the authentication configuration is applied successfully:

  ``` terminal
  $ oc get authentication.config.openshift.io/cluster -o yaml
  ```

- Authenticate with a user account and verify the username is constructed correctly:

  ``` terminal
  $ oc whoami
  ```

- Monitor the cluster authentication Operator status:

  ``` terminal
  $ oc get clusteroperator authentication
  ```

  The Operator should report `Available=True` and `Degraded=False`.

</div>

> [!NOTE]
> CEL expressions have access to standard CEL string functions (`lowerAscii()`, `upperAscii()`, `contains()`, `startsWith()`, `endsWith()`, `matches()`, `split()`), operators (`+`, `?`, `has()`, ternary `? :`), and the `orValue()` method for optional chaining. See the CEL specification link in Additional resources for the complete function reference.

You can use the following CEL expression patterns for claim mapping:

Use the optional chaining Operator `?` to safely access claims that might not exist
``` yaml
username:
  expression: 'claims.email_verified ? claims.email : claims.sub'
```

Uses `email` if verified, otherwise `sub`. When using the `email` claim, you must also check `email_verified`.

Concatenate multiple claims
``` yaml
username:
  expression: 'claims.givenname + "." + claims.surname'
```

Combines given name and surname claims.

Transform claim values
``` yaml
username:
  expression: 'claims.email.lowerAscii()'
```

Converts email to lowercase.

Conditional logic for different user types
``` yaml
username:
  expression: 'has(claims.upn) ? claims.upn : claims.oid'
```

Uses `upn` for regular users, `oid` for service principals.

Extract domain from email
``` yaml
groups:
  expression: 'claims.?email.orValue("").split("@").size() > 1 ? [claims.email.split("@")[1]] : []'
```

Safely extracts domain from email address for group assignment, returning an empty array if email is missing or malformed.

Combine group sources
``` yaml
groups:
  expression: 'claims.?groups.orValue([]) + claims.?roles.orValue([])'
```

Combines `groups` and `roles` claims.

# Configuring claim validation rules

Use Common Expression Language (CEL) expressions to define custom validation rules for JWT token claims and enforce advanced security policies such as maximum token lifetimes.

> [!WARNING]
> All claim validation rules must pass for authentication to succeed. Incorrectly configured validation rules can lock all users out of the cluster. Ensure you complete the following tasks:
>
> - Have a backup authentication method, such as a certificate-based kubeconfig file, before applying these rules
>
> - Test validation rules in a non-production environment first
>
> - Verify your CEL expressions are correct to avoid blocking valid users from accessing the cluster

<div>

<div class="title">

Prerequisites

</div>

- You have configured an external OIDC identity provider for direct authentication.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.

- You are familiar with CEL expression syntax.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `authentication-claim-validation.yaml` with your claim validation rules:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Authentication
    metadata:
      name: cluster
    spec:
      type: OIDC
      oidcProviders:
      - name: my-oidc-provider
        issuer:
          issuerURL: https://idp.example.com
          audiences:
          - my-audience
        claimMappings:
          username:
            claim: email
        claimValidationRules:
        - type: CEL
          cel:
            expression: 'claims.exp - claims.nbf <= 86400'
            message: 'Total token lifetime must not exceed 24 hours'
        - type: CEL
          cel:
            expression: 'has(claims.email) && claims.email_verified && claims.email.contains("@example.com")'
            message: 'Email claim must be verified and from example.com domain'
    ```

    where:

    `claimValidationRules`
    Specifies an array of validation rules. All must pass for authentication.

    `type`
    Specifies the validation type. Set to `CEL` for CEL-based validation.

    `cel.expression`
    Specifies the CEL expression that must evaluate to `true`.

    `cel.message`
    Specifies the error message displayed when validation fails.

    > [!NOTE]
    > Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`, `@example.com`) with your actual OIDC provider configuration and validation requirements.

2.  Apply the configuration:

    ``` terminal
    $ oc apply -f authentication-claim-validation.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the authentication configuration is applied successfully:

  ``` terminal
  $ oc get authentication.config.openshift.io/cluster -o yaml
  ```

- Authenticate with a token that matches your validation rules to confirm they are enforced correctly.

- Check the cluster authentication Operator logs for validation errors:

  ``` terminal
  $ oc logs -n openshift-authentication-operator deployments/authentication-operator
  ```

</div>

When writing CEL expressions for claim validation:

- Access claims using `claims` variable (for example, `claims.sub` or `claims.foo.bar` for nested claims)

- Expressions must evaluate to boolean values

- Use `has()` to check claim existence

- Standard CEL operators and functions available: `&&`, `||`, `!`, `contains()`, `startsWith()`, `endsWith()`

Common use cases include:

Enforce maximum token lifetime
``` yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.exp - claims.nbf <= 86400'
    message: 'Token lifetime must not exceed 24 hours'
```

Require specific claim values
``` yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'claims.tenant == "production"'
    message: 'Only production tenant tokens are allowed'
```

Validate email domain
``` yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.email) && claims.email_verified && claims.email.endsWith("@trusted-domain.com")'
    message: 'Email must be verified and from trusted-domain.com'
```

When using the `email` claim, you must also check `email_verified` to ensure the email address has been verified by the identity provider.

Combine conditions
``` yaml
claimValidationRules:
- type: CEL
  cel:
    expression: 'has(claims.role) && (claims.role == "admin" || claims.role == "developer")'
    message: 'User must have admin or developer role'
```

<!-- -->

If authentication fails after the configuration is applied
Even if your claim validation rules pass the configuration validation gates, runtime authentication errors can occur. Check the kube-apiserver logs for detailed error messages explaining why authentication failed:

``` terminal
$ oc logs -n openshift-kube-apiserver -l app=openshift-kube-apiserver | grep -i auth
```

These log messages will indicate which validation rule failed and include the custom `message` you specified in the CEL expression.

If you incorrectly configure validation rules and lock users out of the cluster
1.  Use your certificate-based kubeconfig to authenticate as `cluster-admin`.

2.  Edit the Authentication custom resource to remove or fix invalid rules:

    ``` terminal
    $ oc edit authentication.config.openshift.io/cluster
    ```

3.  Monitor the cluster authentication Operator to confirm it returns to `Available` status:

    ``` terminal
    $ oc get clusteroperator authentication
    ```

# Configuring user validation rules

You can define validation rules to enforce security policies on the user object created from an authenticated token. This helps prevent privilege escalation by blocking reserved usernames and group prefixes.

> [!NOTE]
> User validation rules are evaluated after claim mapping is complete, including all prefix transformations. Your CEL expressions must validate the final username and group names as they will appear in RBAC policies, not the raw claim values from the JWT token.

> [!WARNING]
> All user validation rules must pass for authentication to succeed. Incorrectly configured validation rules can lock all users out of the cluster. Ensure you:
>
> - Have a backup authentication method, such as a certificate-based kubeconfig file, before applying these rules
>
> - Test validation rules in a non-production environment first
>
> - Verify your CEL expressions correctly validate the final username and groups to avoid blocking valid users or allowing unauthorized access

<div>

<div class="title">

Prerequisites

</div>

- You have configured an external OIDC identity provider for direct authentication.

- You have access to the cluster as a user with the `cluster-admin` role.

- You have access to a long-lived authentication method, such as a certificate-based kubeconfig file.

- You are familiar with CEL expression syntax.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a YAML file named `authentication-user-validation.yaml` with your user validation rules:

    ``` yaml
    apiVersion: config.openshift.io/v1
    kind: Authentication
    metadata:
      name: cluster
    spec:
      type: OIDC
      oidcProviders:
      - name: my-oidc-provider
        issuer:
          issuerURL: https://idp.example.com
          audiences:
          - my-audience
        claimMappings:
          username:
            claim: email
          groups:
            claim: groups
        userValidationRules:
        - expression: "!user.username.startsWith('system:')"
          message: 'Username cannot use reserved system: prefix'
        - expression: "!user.groups.exists(g, g.startsWith('system:'))"
          message: 'Groups cannot use reserved system: prefix'
    ```

    where:

    `userValidationRules`
    Specifies an array of validation rules. All must pass for authentication.

    `expression`
    Specifies the CEL expression that must evaluate to `true`.

    `message`
    Specifies the error message displayed when validation fails.

    > [!NOTE]
    > Replace the placeholder values (`my-oidc-provider`, `https://idp.example.com`, `my-audience`) with your actual OIDC provider configuration.

2.  Apply the configuration:

    ``` terminal
    $ oc apply -f authentication-user-validation.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the authentication configuration is applied successfully:

  ``` terminal
  $ oc get authentication.config.openshift.io/cluster -o yaml
  ```

- Authenticate with credentials that would create a user matching your validation rules to confirm they are enforced correctly.

- Check the cluster authentication Operator logs for validation errors:

  ``` terminal
  $ oc logs -n openshift-authentication-operator deployments/authentication-operator
  ```

</div>

When writing CEL expressions for user validation:

- Access user fields: `user.username`, `user.groups` (array), `user.uid`, `user.extra` (map)

- Expressions must evaluate to boolean values

- Use `startsWith()`, `endsWith()`, `contains()` for string matching

- Use `exists()` for array checks (for example, `user.groups.exists(g, g == "admin")`)

Common use cases include:

Prevent reserved username prefixes
``` yaml
userValidationRules:
- expression: "!user.username.startsWith('system:')"
  message: 'Username cannot use reserved system: prefix'
```

Prevent reserved group prefixes
``` yaml
userValidationRules:
- expression: "!user.groups.exists(g, g.startsWith('system:'))"
  message: 'Groups cannot use reserved system: prefix'
```

Require username format
``` yaml
userValidationRules:
- expression: "user.username.matches('^[a-z0-9]([-a-z0-9]*[a-z0-9])?$')"
  message: 'Username must be a valid DNS subdomain'
```

Validate group membership
``` yaml
userValidationRules:
- expression: "user.groups.exists(g, g == 'verified-users')"
  message: 'User must be a member of verified-users group'
```

Combine conditions
``` yaml
userValidationRules:
- expression: "!user.username.startsWith('system:') && !user.username.startsWith('kube:')"
  message: 'Username cannot use reserved system: or kube: prefixes'
```

<div class="formalpara">

<div class="title">

Troubleshooting

</div>

If you incorrectly configure validation rules and lock users out of the cluster:

</div>

1.  Use your certificate-based kubeconfig to authenticate as `cluster-admin`.

2.  Edit the Authentication custom resource to remove or fix invalid rules:

    ``` terminal
    $ oc edit authentication.config.openshift.io/cluster
    ```

3.  Monitor the cluster authentication Operator to confirm it returns to `Available` status:

    ``` terminal
    $ oc get clusteroperator authentication
    ```

# Advanced authentication field reference

The following table describes the advanced authentication configuration fields available as Technology Preview in OpenShift Container Platform.

<table>
<caption>Advanced <code>oidcProviders</code> configuration fields</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 66%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Parameter</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>issuer.discoveryURL</code></p></td>
<td style="text-align: left;"><p>Optional parameter. Custom OIDC discovery endpoint URL for retrieving identity provider metadata from a non-standard location.</p>
<p>Requirements:</p>
<ul>
<li><p>Must be a valid HTTPS URL</p></li>
<li><p>Must differ from <code>issuer.issuerURL</code></p></li>
</ul>
<p>When not specified, OpenShift Container Platform constructs the discovery URL by using the standard OIDC format: <code>{issuerURL}/.well-known/openid-configuration</code>.</p>
<p><strong>Example:</strong></p>
<div class="sourceCode" id="cb1"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb1-1"><a href="#cb1-1" aria-hidden="true" tabindex="-1"></a><span class="fu">issuer</span><span class="kw">:</span></span>
<span id="cb1-2"><a href="#cb1-2" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">issuerURL</span><span class="kw">:</span><span class="at"> https://idp.example.com</span></span>
<span id="cb1-3"><a href="#cb1-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">discoveryURL</span><span class="kw">:</span><span class="at"> https://custom-discovery.example.com/.well-known/openid-configuration</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules</code></p></td>
<td style="text-align: left;"><p>Optional parameter. Array of validation rules for JWT token claims using Common Expression Language (CEL) expressions. All rules must evaluate to <code>true</code> for authentication to succeed (AND operation).</p>
<p>Each rule has:</p>
<ul>
<li><p><code>type</code>: Set to <code>CEL</code> for CEL-based validation</p></li>
<li><p><code>cel</code>: Object with <code>expression</code> (must evaluate to <code>true</code>) and <code>message</code> (error text)</p></li>
</ul>
<p>CEL expressions access claims by using <code>claims</code> variable (for example, <code>claims.sub</code>).</p>
<p><strong>Example:</strong></p>
<div class="sourceCode" id="cb2"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb2-1"><a href="#cb2-1" aria-hidden="true" tabindex="-1"></a><span class="fu">claimValidationRules</span><span class="kw">:</span></span>
<span id="cb2-2"><a href="#cb2-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">type</span><span class="kw">:</span><span class="at"> CEL</span></span>
<span id="cb2-3"><a href="#cb2-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">cel</span><span class="kw">:</span></span>
<span id="cb2-4"><a href="#cb2-4" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">expression</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;claims.exp - claims.nbf &lt;= 86400&#39;</span></span>
<span id="cb2-5"><a href="#cb2-5" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">message</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;Total token lifetime must not exceed 24 hours&#39;</span></span>
<span id="cb2-6"><a href="#cb2-6" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">type</span><span class="kw">:</span><span class="at"> CEL</span></span>
<span id="cb2-7"><a href="#cb2-7" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">cel</span><span class="kw">:</span></span>
<span id="cb2-8"><a href="#cb2-8" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">expression</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;has(claims.email) &amp;&amp; claims.email.contains(&quot;@example.com&quot;)&#39;</span></span>
<span id="cb2-9"><a href="#cb2-9" aria-hidden="true" tabindex="-1"></a><span class="at">    </span><span class="fu">message</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;Email claim must be present and from example.com domain&#39;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules[].type</code></p></td>
<td style="text-align: left;"><p>Required. Validation rule type. Set to <code>CEL</code> for CEL-based validation. Requires <code>cel</code> field.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules[].cel</code></p></td>
<td style="text-align: left;"><p>Required when <code>type</code> is <code>CEL</code>. Contains <code>expression</code> (CEL expression to evaluate) and <code>message</code> (error text).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules[].cel.expression</code></p></td>
<td style="text-align: left;"><p>Required. CEL expression that validates token claims. Must evaluate to <code>true</code> for authentication to succeed.</p>
<p>Constraints: 1-1024 characters, must evaluate to boolean.</p>
<p>Access claims by using <code>claims</code> variable: <code>claims.sub</code>, <code>claims.foo.bar</code> (nested), <code>has(claims.email)</code> (existence check).</p>
<div class="note">
<div class="title">
&#10;</div>
<p>When using the <code>email</code> claim in CEL expressions, you must also validate the <code>email_verified</code> claim to ensure the email address has been verified by the identity provider. For example: <code>claims.email_verified &amp;&amp; claims.email.endsWith("@example.com")</code>.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>claimValidationRules[].cel.message</code></p></td>
<td style="text-align: left;"><p>Required. Error message displayed when validation fails. Constraints: 1-256 characters.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>userValidationRules</code></p></td>
<td style="text-align: left;"><p>Optional parameter. Array of validation rules for user objects by using CEL expressions. All rules must evaluate to <code>true</code> for authentication to succeed (AND operation).</p>
<p>Each rule has <code>expression</code> (must evaluate to <code>true</code>) and <code>message</code> (error text).</p>
<p>CEL expressions access user object by using <code>user</code> variable: <code>user.username</code> (string), <code>user.groups</code> (array), <code>user.uid</code> (string), <code>user.extra</code> (map).</p>
<p><strong>Example:</strong></p>
<div class="sourceCode" id="cb3"><pre class="sourceCode yaml"><code class="sourceCode yaml"><span id="cb3-1"><a href="#cb3-1" aria-hidden="true" tabindex="-1"></a><span class="fu">userValidationRules</span><span class="kw">:</span></span>
<span id="cb3-2"><a href="#cb3-2" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">expression</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;!user.username.startsWith(&#39;system:&#39;)&quot;</span></span>
<span id="cb3-3"><a href="#cb3-3" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">message</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;Username cannot use reserved system: prefix&#39;</span></span>
<span id="cb3-4"><a href="#cb3-4" aria-hidden="true" tabindex="-1"></a><span class="kw">-</span><span class="at"> </span><span class="fu">expression</span><span class="kw">:</span><span class="at"> </span><span class="st">&quot;!user.groups.exists(g, g.startsWith(&#39;system:&#39;))&quot;</span></span>
<span id="cb3-5"><a href="#cb3-5" aria-hidden="true" tabindex="-1"></a><span class="at">  </span><span class="fu">message</span><span class="kw">:</span><span class="at"> </span><span class="st">&#39;Groups cannot use reserved system: prefix&#39;</span></span></code></pre></div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>userValidationRules[].expression</code></p></td>
<td style="text-align: left;"><p>Required. CEL expression that validates the user object. Must evaluate to <code>true</code> for authentication to succeed.</p>
<p>Constraints: 1-1024 characters, must evaluate to boolean.</p>
<p>Access user fields: <code>user.username.startsWith('system:')</code>, <code>user.groups.exists(g, g == "admin")</code>, <code>user.extra["example.com/role"]</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>userValidationRules[].message</code></p></td>
<td style="text-align: left;"><p>Required. Error message displayed when validation fails. Must not be empty.</p></td>
</tr>
</tbody>
</table>

<div>

<div class="title">

Additional resources

</div>

- [Enabling direct authentication with an external OIDC identity provider](external-auth.md#external-auth)

- [Common Expression Language (CEL) specification](https://cel.dev/)

- [Common Expression Language in Kubernetes](https://kubernetes.io/docs/reference/using-api/cel/)

</div>
