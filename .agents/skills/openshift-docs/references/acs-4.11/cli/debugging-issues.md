<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Central saves information to its container logs.

<a id="setting-up-environment-variables_debugging-issues"></a>

# Prerequisites

Configure the `ROX_ENDPOINT` environment variable to specify the host and port information for Central.

<div>

<div class="title">

Procedure

</div>

- To configure the `ROX_ENDPOINT` environment variable, run the following command:

  ``` terminal
  $ export ROX_ENDPOINT=<host:port>
  ```

  where:

  `<host:port>`  
  Specifies the host and port information that you want to store in the `ROX_ENDPOINT` environment variable.

</div>

<a id="viewing-the-logs_debugging-issues"></a>

# Viewing the logs

You can use either the `oc` or `kubectl` command to view the logs for the Central pod.

<div>

<div class="title">

Procedure

</div>

- To view the logs for the Central pod by using `kubectl`, run the following command :

  ``` terminal
  $ kubectl logs -n stackrox <central_pod>
  ```

- To view the logs for the Central pod by using `oc`, run the following command :

  ``` terminal
  $ oc logs -n stackrox <central_pod>
  ```

</div>

<a id="viewing-the-current-log-level_debugging-issues"></a>

# Viewing the current log level

You can change the log level to see more or less information in Central logs.

<div>

<div class="title">

Procedure

</div>

- Run the following command to view the current log level:

  ``` terminal
  $ roxctl central debug log
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl central debug](command-reference/roxctl-central.md#roxctl-central-debug_roxctl-central)

</div>

<a id="changing-the-log-level_debugging-issues"></a>

# Changing the log level

Change the log level to adjust the verbosity of Central logs.

<div>

<div class="title">

Procedure

</div>

- Run the following command to change the log level:

  ``` terminal
  $ roxctl central debug log --level=<log_level>
  ```

  where:

  `<log_level>`  
  Specifies the log level. The accepted values for the log level are `Panic`, `Fatal`, `Error`, `Warn`, `Info`, and `Debug`.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl central debug](command-reference/roxctl-central.md#roxctl-central-debug_roxctl-central)

</div>

<a id="retrieving-debugging-information_debugging-issues"></a>

# Retrieving debugging information

Gather debugging information to investigate issues with RHACS.

<div>

<div class="title">

Procedure

</div>

- Run the following command to gather the debugging information for investigating issues:

  ``` terminal
  $ roxctl central debug dump
  ```

- To generate a diagnostic bundle with the RHACS administrator password or API token and central address, use the `roxctl` CLI.

</div>

<div>

<div class="title">

Additional resources

</div>

- [roxctl central debug](command-reference/roxctl-central.md#roxctl-central-debug_roxctl-central)

- [Generating a diagnostic bundle by using the roxctl CLI](../support/getting-support.md#generate-diagnostic-bundle-using-roxctl-cli_getting-support)

</div>
