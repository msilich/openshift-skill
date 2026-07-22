<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use a CLI configuration file to create different profiles, or contexts, for use with the OpenShift CLI (`oc`). A context consists of user authentication and a OpenShift Container Platform server information associated with a *nickname*.

# About switching between CLI profiles

You can use contexts to easily switch between users across multiple OpenShift Container Platform clusters when using the OpenShift CLI (`oc`). You specify a nickname to make managing CLI configurations easier by providing short-hand references to contexts, user credentials, and cluster details.

After a user logs in with the `oc` CLI for the first time, OpenShift Container Platform creates a `~/.kube/config` file if one does not already exist. As more authentication and connection details are provided to the CLI, the updated information is stored in the configuration file:

<div class="formalpara">

<div class="title">

CLI configuration file

</div>

``` yaml
apiVersion: v1
clusters:
- cluster:
    insecure-skip-tls-verify: true
    server: https://openshift1.example.com:8443
  name: openshift1.example.com:8443
- cluster:
    insecure-skip-tls-verify: true
    server: https://openshift2.example.com:8443
  name: openshift2.example.com:8443
contexts:
- context:
    cluster: openshift1.example.com:8443
    namespace: alice-project
    user: alice/openshift1.example.com:8443
  name: alice-project/openshift1.example.com:8443/alice
- context:
    cluster: openshift1.example.com:8443
    namespace: joe-project
    user: alice/openshift1.example.com:8443
  name: joe-project/openshift1/alice
current-context: joe-project/openshift1.example.com:8443/alice
kind: Config
preferences: {}
users:
- name: alice/openshift1.example.com:8443
  user:
    token: xZHd2piv5_9vQrg-SKXRJ2Dsl9SceNJdhNTljEKTb8k
```

</div>

where:

`clusters`
Specifies connection details for OpenShift Container Platform clusters, including the address for their master server. In this example, one cluster is nicknamed `openshift1.example.com:8443` and another is nicknamed `openshift2.example.com:8443`.

`contexts`
Specifies two contexts: one nicknamed `alice-project/openshift1.example.com:8443/alice`, using the `alice-project` project, `openshift1.example.com:8443` cluster, and `alice` user, and another nicknamed `joe-project/openshift1.example.com:8443/alice`, using the `joe-project` project, `openshift1.example.com:8443` cluster and `alice` user.

`current-context`
Specifies that the `joe-project/openshift1.example.com:8443/alice` context is currently in use, allowing the `alice` user to work in the `joe-project` project on the `openshift1.example.com:8443` cluster.

`users`
Specifies user credentials. In this example, the user nickname `alice/openshift1.example.com:8443` uses an access token.

The CLI can support multiple configuration files which are loaded at runtime and merged together along with any override options specified from the command line. After you are logged in, you can use the `oc status` or `oc project` command to verify your current working environment:

<div class="formalpara">

<div class="title">

Verify the current working environment

</div>

``` terminal
$ oc status
```

</div>

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
In project Joe's Project (joe-project)

service database (172.30.43.12:5434 -> 3306)
  database deploys docker.io/openshift/mysql-55-centos7:latest
    #1 deployed 25 minutes ago - 1 pod

service frontend (172.30.159.137:5432 -> 8080)
  frontend deploys origin-ruby-sample:latest <-
    builds https://github.com/openshift/ruby-hello-world with joe-project/ruby-20-centos7:latest
    #1 deployed 22 minutes ago - 2 pods

To see more information about a service or deployment, use 'oc describe service <name>' or 'oc describe dc <name>'.
You can use 'oc get all' to see lists of each of the types described in this example.
```

</div>

<div class="formalpara">

<div class="title">

List the current project

</div>

``` terminal
$ oc project
```

</div>

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Using project "joe-project" from context named "joe-project/openshift1.example.com:8443/alice" on server "https://openshift1.example.com:8443".
```

</div>

You can run the `oc login` command again and supply the required information during the interactive process, to log in using any other combination of user credentials and cluster details. A context is constructed based on the supplied information if one does not already exist. If you are already logged in and want to switch to another project the current user already has access to, use the `oc project` command and enter the name of the project:

``` terminal
$ oc project alice-project
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
Now using project "alice-project" on server "https://openshift1.example.com:8443".
```

</div>

At any time, you can use the `oc config view` command to view your current CLI configuration, as seen in the output. Additional CLI configuration commands are also available for more advanced usage.

> [!NOTE]
> If you have access to administrator credentials but are not logged in as the default system user `system:admin`, you can log back in as this user as long as the credentials are present in your CLI configuration file.
>
> The following command logs in and switches to the default project:
>
> ``` terminal
> $ oc login -u system:admin -n default
> ```

# Manually configuring CLI profiles

If you want to manually configure your CLI configuration files, you can use the `oc config` command instead of directly modifying the files.

> [!NOTE]
> This section covers more advanced usage of CLI configurations. In most situations, you can use the `oc login` and `oc project` commands to log in and switch between contexts and projects.

For more details on the available `oc config` subcommands, see the "CLI configuration subcommands" table.

<div>

<div class="title">

Procedure

</div>

1.  Log in as a user that uses an access token. This token is used by the `alice` user:

    ``` terminal
    $ oc login https://openshift1.example.com --token=ns7yVhuRNpDM9cgzfhhxQ7bM5s7N2ZVrkZepSRf4LC0
    ```

2.  View the cluster entry automatically created:

    ``` terminal
    $ oc config view
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    apiVersion: v1
    clusters:
    - cluster:
        insecure-skip-tls-verify: true
        server: https://openshift1.example.com
      name: openshift1-example-com
    contexts:
    - context:
        cluster: openshift1-example-com
        namespace: default
        user: alice/openshift1-example-com
      name: default/openshift1-example-com/alice
    current-context: default/openshift1-example-com/alice
    kind: Config
    preferences: {}
    users:
    - name: alice/openshift1.example.com
      user:
        token: ns7yVhuRNpDM9cgzfhhxQ7bM5s7N2ZVrkZepSRf4LC0
    ```

    </div>

3.  Update the current context to have users log in to the desired namespace:

    ``` terminal
    $ oc config set-context `oc config current-context` --namespace=<project_name>
    ```

4.  Examine the current context, to confirm that the changes are implemented:

    ``` terminal
    $ oc whoami -c
    ```

    All subsequent CLI operations uses the new context, unless otherwise specified by overriding CLI options or until the context is switched.

</div>

## Manual configuration of CLI profiles

You can manually configure CLI profiles by using `oc config` subcommands to set clusters, contexts, and individual configuration values.

<table>
<caption>CLI configuration subcommands</caption>
<colgroup>
<col style="width: 11%" />
<col style="width: 88%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Subcommand</th>
<th style="text-align: left;">Usage</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>set-cluster</code></p></td>
<td style="text-align: left;"><p>Sets a cluster entry in the CLI configuration file. If the referenced cluster nickname already exists, the specified information is merged in.</p>
<pre class="terminal"><code>$ oc config set-cluster &lt;cluster_nickname&gt; [--server=&lt;master_ip_or_fqdn&gt;]
[--certificate-authority=&lt;path/to/certificate/authority&gt;]
[--api-version=&lt;apiversion&gt;] [--insecure-skip-tls-verify=true]</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set-context</code></p></td>
<td style="text-align: left;"><p>Sets a context entry in the CLI configuration file. If the referenced context nickname already exists, the specified information is merged in.</p>
<pre class="terminal"><code>$ oc config set-context &lt;context_nickname&gt; [--cluster=&lt;cluster_nickname&gt;]
[--user=&lt;user_nickname&gt;] [--namespace=&lt;namespace&gt;]</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>use-context</code></p></td>
<td style="text-align: left;"><p>Sets the current context using the specified context nickname.</p>
<pre class="terminal"><code>$ oc config use-context &lt;context_nickname&gt;</code></pre></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>set</code></p></td>
<td style="text-align: left;"><p>Sets an individual value in the CLI configuration file.</p>
<pre class="terminal"><code>$ oc config set &lt;property_name&gt; &lt;property_value&gt;</code></pre>
<p>The <code>&lt;property_name&gt;</code> is a dot-delimited name where each token represents either an attribute name or a map key. The <code>&lt;property_value&gt;</code> is the new value being set.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>unset</code></p></td>
<td style="text-align: left;"><p>Unsets individual values in the CLI configuration file.</p>
<pre class="terminal"><code>$ oc config unset &lt;property_name&gt;</code></pre>
<p>The <code>&lt;property_name&gt;</code> is a dot-delimited name where each token represents either an attribute name or a map key.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>view</code></p></td>
<td style="text-align: left;"><p>Displays the merged CLI configuration currently in use.</p>
<pre class="terminal"><code>$ oc config view</code></pre>
<p>Displays the result of the specified CLI configuration file.</p>
<pre class="terminal"><code>$ oc config view --config=&lt;specific_filename&gt;</code></pre></td>
</tr>
</tbody>
</table>

# Load and merge rules

Review the rules that OpenShift CLI (`oc`) uses for the loading and merging order for the CLI configuration.

- CLI configuration files are retrieved from your workstation, using the following hierarchy and merge rules:

  - If the `--config` option is set, then only that file is loaded. The flag is set once and no merging takes place.

  - If the `$KUBECONFIG` environment variable is set, then it is used. The variable can be a list of paths, and if so the paths are merged together. When a value is modified, it is modified in the file that defines the stanza. When a value is created, it is created in the first file that exists. If no files in the chain exist, then it creates the last file in the list.

  - Otherwise, the `~/.kube/config` file is used and no merging takes place.

- The context to use is determined based on the first match in the following flow:

  - The value of the `--context` option.

  - The `current-context` value from the CLI configuration file.

  - An empty value is allowed at this stage.

- The user and cluster to use is determined. At this point, you may or may not have a context; they are built based on the first match in the following flow, which is run once for the user and once for the cluster:

  - The value of the `--user` for user name and `--cluster` option for cluster name.

  - If the `--context` option is present, then use the context’s value.

  - An empty value is allowed at this stage.

- The actual cluster information to use is determined. At this point, you may or may not have cluster information. Each piece of the cluster information is built based on the first match in the following flow:

  - The values of any of the following command-line options:

    - `--server`,

    - `--api-version`

    - `--certificate-authority`

    - `--insecure-skip-tls-verify`

  - If cluster information and a value for the attribute is present, then use it.

  - If you do not have a server location, then there is an error.

- The actual user information to use is determined. Users are built using the same rules as clusters, except that you can only have one authentication technique per user; conflicting techniques cause the operation to fail. Command-line options take precedence over configuration file values. Valid command-line options are:

  - `--auth-path`

  - `--client-certificate`

  - `--client-key`

  - `--token`

- For any information that is still missing, default values are used and prompts are given for additional information.

# Additional resources

- [CLI tools overview](../index.md#cli-tools-overview)

- [Understanding authentication](../../authentication/understanding-authentication.md#understanding-authentication)
