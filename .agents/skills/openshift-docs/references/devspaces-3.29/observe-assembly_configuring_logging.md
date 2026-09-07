> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-assembly_configuring_logging). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Configure logging to isolate issues

Configure OpenShift Dev Spaces server log levels, log HTTP traffic for debugging, and collect diagnostic logs with dsc.

- **[How server logging works](observe-con_configuring_server_logging.md)**  
  Fine-tune the log levels of individual loggers available in the OpenShift Dev Spaces server to control output verbosity and isolate issues during troubleshooting.
- **[Configure log levels](observe-proc_configuring_log_levels.md)**  
  Configure the log levels of individual loggers in the OpenShift Dev Spaces server using the `CHE_LOGGER_CONFIG` environment variable to control log verbosity and simplify troubleshooting.
- **[Log HTTP traffic](observe-proc_logging_http_traffic.md)**  
  Log the HTTP traffic between the OpenShift Dev Spaces server and the API server of the Kubernetes or OpenShift cluster to troubleshoot communication issues and debug API errors.
- **[Collect logs with dsc](observe-ref_collecting_logs_using_dsc.md)**  
  The `dsc` management tool provides commands to collect OpenShift Dev Spaces logs for troubleshooting and diagnostics. These commands automate log collection from the multiple containers that comprise a Red Hat OpenShift Dev Spaces installation in the OpenShift cluster.

**Related information**  

- [Monitor platform health](observe-assembly_monitoring_platform_health.md)
