<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Use the `roxctl declarative-config` command to manage declarative configurations. This reference covers the command syntax, available subcommands, and configuration options.

<a id="roxctl-declarative-config-overview_roxctl-declarative-config"></a>

# roxctl declarative-config

Manage the declarative configuration.

<a id="roxctl-declarative-config-usage_roxctl-declarative-config"></a>

## roxctl declarative-config usage

Usage syntax for the `roxctl declarative-config` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config [command] [flags]
```

</div>

<a id="roxctl-declarative-config-available-commands_roxctl-declarative-config"></a>

## Available commands

Available commands for the `roxctl declarative-config` command.

| Command  | Description                                           |
|----------|-------------------------------------------------------|
| `create` | Create declarative configurations.                    |
| `lint`   | Lint an existing declarative configuration YAML file. |

<a id="options-inherited-from-the-parent-command_roxctl-declarative-config"></a>

# roxctl declarative-config command options inherited from the parent command

The `roxctl declarative-config` command supports the following options inherited from the parent `roxctl` command:

| Option | Description |
|----|----|
| `--ca string` | Specify a custom CA certificate file path for secure connections. Alternatively, you can specify the file path by using the `ROX_CA_CERT_FILE` environment variable. |
| `--direct-grpc` | Set `--direct-grpc` for improved connection performance. Alternatively, by setting the `ROX_DIRECT_GRPC_CLIENT` environment variable to `true`, you can enable direct gRPC . The default value is `false`. |
| `-e`, `--endpoint string` | Set the endpoint for the service to contact. Alternatively, you can set the endpoint by using the `ROX_ENDPOINT` environment variable. The default value is `localhost:8443`. |
| `--force-http1` | Force the use of HTTP/1 for all connections. Alternatively, by setting the `ROX_CLIENT_FORCE_HTTP1` environment variable to `true`, you can force the use of HTTP/1. The default value is `false`. |
| `--insecure` | Enable insecure connection options. Alternatively, by setting the `ROX_INSECURE_CLIENT` environment variable to `true`, you can enable insecure connection options. The default value is `false`. |
| `--insecure-skip-tls-verify` | Skip the TLS certificate validation. Alternatively, by setting the `ROX_INSECURE_CLIENT_SKIP_TLS_VERIFY` environment variable to `true`, you can skip the TLS certificate validation. The default value is `false`. |
| `--no-color` | Disable the color output. Alternatively, by setting the `ROX_NO_COLOR environment variable` to `true`, you can disable the color output. The default value is `false`. |
| `-p`, `--password string` | Specify the password for basic authentication. Alternatively, you can set the password by using the `ROX_ADMIN_PASSWORD` environment variable. |
| `--plaintext` | Use an unencrypted connection. Alternatively, by setting the `ROX_PLAINTEXT` environment variable to `true`, you can enable an unencrypted connection. The default value is `false`. |
| `-s`, `--server-name string` | Set the TLS server name to use for SNI. Alternatively, you can set the server name by using the `ROX_SERVER_NAME` environment variable. |
| `--token-file string` | Use the API token provided in the specified file for authentication. Alternatively, you can set the token by using the `ROX_API_TOKEN` environment variable. |

> [!NOTE]
> These options are applicable to all the sub-commands of the `roxctl declarative-config` command.

<a id="roxctl-declarative-config-lint_roxctl-declarative-config"></a>

# roxctl declarative-config lint

Lint an existing declarative configuration YAML file.

<a id="roxctl-declarative-config-lint-usage_roxctl-declarative-config"></a>

## roxctl declarative-config lint usage

Usage syntax for the `roxctl declarative-config lint` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config lint [flags]
```

</div>

<a id="roxctl-declarative-config-lint-options_roxctl-declarative-config"></a>

## Options

Options for the `roxctl declarative-config lint` command.

| Option | Description |
|----|----|
| `--config-map string` | Read the declarative configuration from the `--config-map string`. If not specified, the command reads the configuration from the YAML file specified by using the `--file` flag. |
| `-f`, `--file string` | File containing the declarative configuration in YAML format. |
| `--namespace string` | Read the declarative configuration from the `--namespace string` of the config map. If not specified, the command uses the namespace specified in the current Kubernetes configuration context. |
| `--secret string` | Read the declarative configuration from the specified `--secret string`. If not specified, the command reads the configuration from the YAML file specified by using the `--file` flag. |

<a id="roxctl-declarative-config-create_roxctl-declarative-config"></a>

# roxctl declarative-config create

Create declarative configurations.

<a id="roxctl-declarative-config-create-usage_roxctl-declarative-config"></a>

## roxctl declarative-config create usage

Usage syntax for the `roxctl declarative-config create` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create [flags]
```

</div>

<a id="roxctl-declarative-config-create-options_roxctl-declarative-config"></a>

## Options

Options for the `roxctl declarative-config create` command.

| Option | Description |
|----|----|
| `--config-map string` | Write the declarative configuration YAML in the config map. If not specified and the `--secret` flag is also not specified, the command prints the generated YAML in the standard output format. |
| `--namespace string` | Required if you want to write the declarative configuration YAML to a config map or secret. If not specified, the command uses the default namespace in the current Kubernetes configuration. |
| `--secret string` | Write the declarative configuration YAML in the Secret. You must use secrets for sensitive data. If not specified and the `--config-map` flag is also not specified, the command prints the generated YAML in the standard output format. |

<a id="roxctl-declarative-config-create-role_roxctl-declarative-config"></a>

## roxctl declarative-config create role

Create a declarative configuration for a role.

<a id="roxctl-declarative-config-create-role-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create role usage

Usage syntax for the `roxctl declarative-config create role` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create role [flags]
```

</div>

<a id="roxctl-declarative-config-create-role-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create role` command.

| Option | Description |
|----|----|
| `--access-scope string` | By providing the name, you can specify the referenced access scope. |
| `--description string` | Set a description for the role. |
| `--name string` | Specify the name of the role. |
| `--permission-set string` | By providing the name, you can specify the referenced permission set. |

<a id="roxctl-declarative-config-create-notifier_roxctl-declarative-config"></a>

## roxctl declarative-config create notifier

Create a declarative configuration for a notifier.

<a id="roxctl-declarative-config-create-notifier-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create notifier usage

Usage syntax for the `roxctl declarative-config create notifier` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create notifier [flags]
```

</div>

<a id="roxctl-declarative-config-create-notifier-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create notifier` command.

| Option          | Description                       |
|-----------------|-----------------------------------|
| `--name string` | Specify the name of the notifier. |

<a id="roxctl-declarative-config-create-access-scope_roxctl-declarative-config"></a>

## roxctl declarative-config create access-scope

Create a declarative configuration for an access scope.

<a id="roxctl-declarative-config-create-access-scope-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create access-scope usage

Usage syntax for the `roxctl declarative-config create access-scope` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create access-scope [flags]
```

</div>

<a id="roxctl-declarative-config-create-access-scope-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create access-scope` command.

| Option | Description |
|----|----|
| `--cluster-label-selector requirement` | Specify the criteria for creating a label selector based on the cluster’s labels. The key-value pairs represent requirements, and you can use this flag many times to create a combination of requirements. The default value is `[ [ ] ]`. For more details, run the `roxctl declarative-config create access-scope --help` command. |
| `--description string` | Set a description for the access scope. |
| `--included included-object` | Specify a list of clusters and their namespaces that you want to include in the access scope. The default value is `[null]`. |
| `--name string` | Specify the name of the access scope. |
| `--namespace-label-selector requirement` | Specify the criteria for creating a label selector based on the namespace’s labels. Similar to the cluster-label-selector, you can use this flag many times for the combination of requirements. For more details, run the `roxctl declarative-config create access-scope --help` command. |

<a id="roxctl-declarative-config-create-auth-provider_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider

Create a declarative configuration for an authentication provider.

<a id="roxctl-declarative-config-create-auth-provider-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider usage

Usage syntax for the `roxctl declarative-config create auth-provider` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create auth-provider` command.

| Option | Description |
|----|----|
| `--extra-ui-endpoints strings` | Specify additional user interface (UI) endpoints where you use the authentication provider. The expected format is `<endpoint>:<port>`. |
| `--groups-key strings` | Set the keys of the groups that you want to add within the authentication provider. The tuples of key, value and role should have the same length. For more details, run the `roxctl declarative-config create auth-provider --help` command. |
| `--groups-role strings` | Set the role of the groups that you want to add within the authentication provider. The tuples of key, value and role should have the same length. For more details, run the `roxctl declarative-config create auth-provider --help` command. |
| `--groups-value strings` | Set the values of the groups that you want to add within the authentication provider. The tuples of key, value and role should have the same length. For more details, run the `roxctl declarative-config create auth-provider --help` command. |
| `--minimum-access-role string` | Set the minimum access role of the authentication provider. You can leave this field empty if you do not want to configure the minimum access role by using the declarative configuration. |
| `--name string` | Specify the name of the authentication provider. |
| `--required-attributes stringToString` | Set a list of attributes that the authentication provider must return during authentication. The default value is `[]`. |
| `--ui-endpoint string` | Set the UI endpoint where you use the authentication provider. This is usually the public endpoint where RHACS is available. The expected format is `<endpoint>:<port>`. |

<a id="roxctl-declarative-config-create-permission-set_roxctl-declarative-config"></a>

## roxctl declarative-config create permission-set

Create a declarative configuration for a permission set.

<a id="roxctl-declarative-config-create-permission-set-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create permission-set usage

Usage syntax for the `roxctl declarative-config create permission-set` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create permission-set [flags]
```

</div>

<a id="roxctl-declarative-config-create-permission-set-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create permission-set` command.

| Option | Description |
|----|----|
| `--description string` | Set the description of the permission set. |
| `--name string` | Specify the name of the permission set. |
| `--resource-with-access stringToString` | Set a list of resources with their respective access levels. The default value is `[]`. For more details, run the `roxctl declarative-config create permission-set --help` command. |

<a id="roxctl-declarative-config-create-notifier-splunk_roxctl-declarative-config"></a>

## roxctl declarative-config create notifier splunk

Create a declarative configuration for a splunk notifier.

<a id="roxctl-declarative-config-create-notifier-splunk-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create notifier splunk usage

Usage syntax for the `roxctl declarative-config create notifier splunk` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create notifier splunk [flags]
```

</div>

<a id="roxctl-declarative-config-create-notifier-splunk-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create notifier splunk` command.

| Option | Description |
|----|----|
| `--audit-logging` | Enable audit logging. The default value is `false`. |
| `--source-types stringToString` | Specify Splunk source types as comma-separated `key=value` pairs. The default value is `[]`. |
| `--splunk-endpoint string` | Specify the Splunk HTTP endpoint. This is a mandatory option. |
| `--splunk-skip-tls-verify` | Use an insecure connection to Splunk. The default value is `false`. |
| `--splunk-token string` | Specify the Splunk HTTP token. This is a mandatory option. |
| `--truncate int` | Specify the Splunk truncate limit. The default value is `10000`. |

<a id="roxctl-declarative-config-create-notifier-generic_roxctl-declarative-config"></a>

## roxctl declarative-config create notifier generic

Create a declarative configuration for a generic notifier.

<a id="roxctl-declarative-config-create-notifier-generic-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create notifier generic usage

Usage syntax for the `roxctl declarative-config create notifier generic` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create notifier generic [flags]
```

</div>

<a id="roxctl-declarative-config-create-notifier-generic-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create notifier generic` command.

| Option | Description |
|----|----|
| `--audit-logging` | Enable audit logging. The default value is `false`. |
| `--extra-fields stringToString` | Specify additional fields as comma-separated `key=value` pairs. The default value is `[]`. |
| `--headers stringToString` | Specify headers as comma-separated `key=value` pairs. The default value is `[]`. |
| `--webhook-cacert-file string` | Specify the file name of the endpoint CA certificate in PEM format. |
| `--webhook-endpoint string` | Specify the URL of the webhook endpoint. |
| `--webhook-password string` | Specify the password for Basic HTTP authentication of the webhook endpoint. No authentication if not specified. Requires `--webhook-username`. |
| `--webhook-skip-tls-verify` | Skip webhook TLS verification. The default value is `false`. |
| `--webhook-username string` | Specify the username for Basic HTTP authentication of the webhook endpoint. No authentication occurs if not specified. Requires `--webhook-password`. |

<a id="roxctl-declarative-config-create-auth-provider-iap_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider iap

Create a declarative configuration for an authentication provider with the identity-aware proxy (IAP) identifier.

<a id="roxctl-declarative-config-create-auth-provider-iap-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider iap usage

Usage syntax for the `roxctl declarative-config create auth-provider iap` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider iap [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-iap-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create auth-provider iap` command.

| Option              | Description                                         |
|---------------------|-----------------------------------------------------|
| `--audience string` | Specify the target group that you want to validate. |

<a id="roxctl-declarative-config-create-auth-provider-oidc_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider oidc

Create a declarative configuration for an OpenID Connect (OIDC) authentication provider.

<a id="roxctl-declarative-config-create-auth-provider-oidc-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider oidc usage

Usage syntax for the `roxctl declarative-config create auth-provider oidc` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider oidc [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-oidc-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create auth-provider oidc` command.

| Option | Description |
|----|----|
| `--claim-mappings stringToString` | Specify a list of non-standard claims from the identity provider (IdP) token that you want to include in the authentication provider’s rules. The default value is `[]`. |
| `--client-id string` | Specify the client ID of the OIDC client. |
| `--client-secret string` | Specify the client secret of the OIDC client. |
| `--disable-offline-access` | Disable the request for the offline_access from the OIDC IdP. You need to use this option if the OIDC IdP limits the number of sessions with the `offline_access` scope. The default value is `false`. |
| `--issuer string` | Specify the issuer of the OIDC client. |
| `--mode string` | Specify the callback mode that you want to use. Valid values include `auto`, `post`, `query` and `fragment`. The default value is `auto`. |

<a id="roxctl-declarative-config-create-auth-provider-saml_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider saml

Create a declarative configuration for a Security Assertion Markup Language (SAML) authentication provider.

<a id="roxctl-declarative-config-create-auth-provider-saml-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider saml usage

Usage syntax for the `roxctl declarative-config create auth-provider saml` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider saml [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-saml-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create auth-provider saml` command.

| Option | Description |
|----|----|
| `--idp-cert string` | Specify the file containing the SAML identity provider (IdP) certificate in PEM format. |
| `--idp-issuer string` | Specify the issuer of the IdP. |
| `--metadata-url string` | Specify the metadata URL of the service provider. |
| `--name-id-format string` | Specify the format of the name ID. |
| `--sp-issuer string` | Specify the issuer of the service provider. |
| `--sso-url string` | Specify the URL of the IdP for single sign-on (SSO). |

<a id="roxctl-declarative-config-create-auth-provider-userpki_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider userpki

Create a declarative configuration for a user Public Key Infrastructure (PKI) authentication provider.

<a id="roxctl-declarative-config-create-auth-provider-userpki-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider userpki usage

Usage syntax for the `roxctl declarative-config create auth-provider userpki` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider userpki [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-userpki-options_roxctl-declarative-config"></a>

### Options

Options for the `roxctl declarative-config create auth-provider userpki` command.

| Option | Description |
|----|----|
| `--ca-file string` | Specify the file containing the certification authorities in PEM format. |

<a id="roxctl-declarative-config-create-auth-provider-openshift-auth_roxctl-declarative-config"></a>

## roxctl declarative-config create auth-provider openshift-auth

Create a declarative configuration for an OpenShift Container Platform OAuth authentication provider.

<a id="roxctl-declarative-config-create-auth-provider-openshift-auth-usage_roxctl-declarative-config"></a>

### roxctl declarative-config create auth-provider openshift-auth usage

Usage syntax for the `roxctl declarative-config create auth-provider openshift-auth` command.

<div class="formalpara">

<div class="title">

Usage

</div>

``` terminal
$ roxctl declarative-config create auth-provider openshift-auth [flags]
```

</div>

<a id="roxctl-declarative-config-create-auth-provider-openshift-auth-options_roxctl-declarative-config"></a>

### Options

This command has no options.
