<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This section lists the basic GitOps `argocd` CLI commands.

# Basic syntax

The GitOps `argocd` CLI is a tool for configuring and managing Red Hat OpenShift GitOps and Argo CD resources from the command line.

## Default mode

In the default mode, the `argocd` CLI client communicates with the Argo CD server component through API requests. To run commands, you must log in to the Argo CD server by using your Argo CD credentials and remain logged in throughout the session. If the login session times out, you can use the `relogin` command to log in again. When done using the `argocd` commands, you can log out using the `logout` command.

**Command syntax:** `argocd [command or options] [arguments…​]`

## Core mode

In this mode, the CLI communicates directly with the Kubernetes API server through the credentials set in the `kubeconfig` file. The default `kubeconfig` file is available at the `$HOME/.kube/config` location. You can customize this file by using the `KUBECONFIG` environment variable. To run commands in the `core` mode, you can use the `--core` argument and do not need to log in to the Argo CD server for user authentication.

To specify the Repo server component name in the `<argocd-instance-name>-repo-server` format, you can either use the `--repo-server-name` command line option or set the `ARGOCD_REPO_SERVER_NAME` environment variable.

**Command syntax:** `KUBECONFIG=~/.kube/config argocd --core [command or options] [arguments…​]`

You can choose one of the following options to run `argocd` commands in the `core` mode:

> [!NOTE]
> If multiple Argo CD instances are in use, set the default namespace of the current context to the namespace of the ArgoCD instance you want to interact with.

- Default `kubeconfig` file with the default context:

  `argocd --core [command or options] [arguments…​]`

  **Example 1: Display a list of applications:**

  ``` terminal
  $ argocd --core app list --repo-server-name openshift-gitops-repo-server
  ```

  **Example 2: Display a list of applications:**

  ``` terminal
  $ ARGOCD_REPO_SERVER_NAME=openshift-gitops-repo-server argocd --core app list
  ```

- Default `kubeconfig` file with a custom context:

  `argocd --core --kube-context [context] [command or options] [arguments…​]`

  **Example 1: Display a list of applications:**

  ``` terminal
  $ argocd --core --kube-context kubeadmin-local app list --repo-server-name openshift-gitops-repo-server
  ```

  **Example 2: Display a list of applications:**

  ``` terminal
  $ ARGOCD_REPO_SERVER_NAME=openshift-gitops-repo-server argocd --core --kube-context kubeadmin-local app list
  ```

- A custom `kubeconfig` file with the default context:

  `KUBECONFIG=~/.kube/custom_config argocd --core [command or options] [arguments…​]`

  **Example: Display a list of applications:**

  ``` terminal
  $ KUBECONFIG=~/.kube/custom_config argocd --core app list --repo-server-name openshift-gitops-repo-server
  ```

- A custom `kubeconfig` file with a custom context:

  `KUBECONFIG=~/.kube/custom_config argocd --core --kube-context [context] [command or options] [arguments…​]`

  **Example: Display a list of applications:**

  ``` terminal
  $ KUBECONFIG=~/.kube/custom_config argocd --kube-context kubeadmin-local --core app list --repo-server-name openshift-gitops-repo-server
  ```

# Global options

Global options are applicable to all the subcommands of the `argocd`.

<table>
<caption>Global options</caption>
<colgroup>
<col style="width: 33%" />
<col style="width: 33%" />
<col style="width: 33%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">Option</th>
<th style="text-align: left;">Argument type</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>--auth-token</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Authentication token.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--client-crt</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Client certificate file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--client-crt-key</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Client certificate key file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--config</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Path to Argo CD configuration file. Defaults to the <code>/home/user/.config/argocd/config</code> path.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--controller-name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Argo CD Application Controller component with <code>argocd-application-controller</code> as the default label.</p>
<p>If the label of this component’s name differs from the default, for example, when you are installing it through the Helm chart, set either the <code>--controller-name</code> option or the <code>ARGOCD_APPLICATION_CONTROLLER_NAME</code> environment variable to specify the name of the component.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--core</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>If set to <code>true</code>, the CLI communicates directly with the Kubernetes API server instead of using the Argo CD API server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--grpc-web</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Enable the gRPC-Web protocol for the Argo CD server. This is useful if, for example, the server is behind a proxy that does not support the HTTP/2 protocol.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--grpc-web-root-path</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Enable the gRPC-Web protocol for the Argo CD server. This is useful if, for example, the server is behind a proxy that does not support the HTTP/2 protocol. Set web root.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-H, --header</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Configure an additional header to all requests made by the GitOps <code>argocd</code> CLI. You can add multiple headers by setting this option multiple times. This option also supports comma-separated headers.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>-h, --help</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Help for the GitOps <code>argocd</code> CLI.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--http-retry-max</code></p></td>
<td style="text-align: left;"><p><code>integer</code></p></td>
<td style="text-align: left;"><p>Set the maximum number of retries to establish an HTTP connection to the Argo CD server.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--insecure</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Skip server certificate and domain verification.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--kube-context</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Direct the command to the given kube context.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--logformat</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Set the logging format to either text or JSON. Defaults to <code>text</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--loglevel</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Set the logging level. Defaults to <code>info</code>. The <code>debug</code>, <code>info</code>, <code>warn</code>, and <code>error</code> levels are available. The logging levels are listed in decreasing order of verbosity.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--plaintext</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Disable Transport Layer Security (TLS) protocols.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--port-forward</code></p></td>
<td style="text-align: left;"><p>N/A</p></td>
<td style="text-align: left;"><p>Connect to a random Argo CD server port using port forwarding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--port-forward-namespace</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Namespace name to be used for port forwarding.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--redis-haproxy-name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Redis HA Proxy deployment with <code>argocd-redis-ha-haproxy</code> as the default label.</p>
<p>If the label of this deployment’s name differs from the default, for example, when you are installing HAProxy through the Helm chart, set either the <code>--redis-haproxy-name</code> option or the <code>ARGOCD_REDIS_HAPROXY_NAME</code> environment variable to specify the name of the deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--redis-name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Redis deployment with <code>argocd-redis</code> as the default label.</p>
<p>If the label of this deployment’s name differs from the default, for example, when you are installing it through the Helm chart, set either the <code>--redis-name</code> option or the <code>ARGOCD_REDIS_NAME</code> environment variable to specify the name of the deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--repo-server-name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Argo CD Repo server with <code>argocd-repo-server</code> as the default label.</p>
<p>If the label of this Repo server’s name differs from the default, for example, when you are installing it through the Helm chart, set either the <code>--repo-server-name</code> option or the <code>ARGOCD_REPO_SERVER_NAME</code> environment variable to specify the name of the deployment.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--server</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Argo CD server address.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--server-crt</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Server certificate file.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>--server-name</code></p></td>
<td style="text-align: left;"><p><code>string</code></p></td>
<td style="text-align: left;"><p>Name of the Argo CD API server with <code>argocd-server</code> as the default label.</p>
<p>If the label of this Argo CD API server’s name differs from the default, for example, when you are installing it through the Helm chart, set either the <code>--server-name</code> option or the <code>ARGOCD_SERVER_NAME</code> environment variable to specify the name of the deployment.</p></td>
</tr>
</tbody>
</table>

# Utility commands

The following list describes the utility commands for the `argocd` CLI.

## argocd

Parent command for GitOps `argocd` CLI.

**Example: Display all options:**

``` terminal
$ argocd
```

## version

Print version information of the CLI.

**Command syntax:** `argocd version [flags]`

**Example: Print the full version of client and server to stdout:**

``` terminal
$ argocd version
```

**Example: Print only full version of the client, no connection to server will be made:**

``` terminal
$ argocd version --client
```

**Example: Print only full version of the server:**

``` terminal
$ argocd version --server <server_url>
```

**Example: Print the full version of client and server in JSON format:**

``` terminal
$ argocd version -o json
```

**Example: Print only client and server core version strings in YAML format:**

``` terminal
$ argocd version --short -o yaml
```

## help

Print the help message about any command in the application.

**Command syntax:** `argocd help [command] [flags]`

**Example: Get the help text for all the available commands:**

``` terminal
$ argocd help
```

**Example: Get the help text for `admin` subcommand:**

``` terminal
$ argocd help admin
```

## completion

Write `bash` or `zsh` shell completion code to standard output.

**Command syntax:** `argocd completion SHELL [flags]`

For `bash`, ensure you have Bash completions installed and enabled. Alternatively, write it to a file and source it in your `.bash_profile`.

**Example: Access completion in your current shell:**

``` terminal
# source <(argocd completion bash)
```

For `zsh`, ensure you have Bash completions installed and enabled.

**Example: Add to your `~/.zshrc` file and access completion in your current shell:**

``` terminal
source <(argocd completion zsh)
compdef _argocd argocd
```

# Additional resources

- [Installing the GitOps CLI](../installing_gitops/installing-argocd-gitops-cli.md#installing-argocd-gitops-cli)

- [Configuring the GitOps CLI](configuring-argocd-gitops-cli.md#configuring-argocd-gitops-cli)

- [Logging in to the Argo CD server in the default mode](logging-in-to-argocd-server-in-default-mode.md#logging-in-to-argocd-server-in-default-mode)

- [OpenShift GitOps CLI User Guide](https://github.com/redhat-developer/gitops-operator/blob/7ac4b2ce179c167b39be259b8d9be37dc280f689/docs/OpenShift%20GitOps%20CLI%20User%20Guide.md#login-related-commands)

- [`argocd` Command Reference](https://argo-cd.readthedocs.io/en/release-3.0/user-guide/commands/argocd/)
