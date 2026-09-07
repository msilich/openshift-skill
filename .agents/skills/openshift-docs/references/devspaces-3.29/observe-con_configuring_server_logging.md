> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-con_configuring_server_logging). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How server logging works

Fine-tune the log levels of individual loggers available in the OpenShift Dev Spaces server to control output verbosity and isolate issues during troubleshooting.

The log level of the whole OpenShift Dev Spaces server is configured globally using the `cheLogLevel` configuration property of the Operator. For the full list of CheCluster Custom Resource fields, see Additional resources. To set the global log level in installations not managed by the Operator, specify the `CHE_LOG_LEVEL` environment variable in the `che` ConfigMap.

It is possible to configure the log levels of the individual loggers in the OpenShift Dev Spaces server using the `CHE_LOGGER_CONFIG` environment variable.

The names of the loggers follow the class names of the internal server classes that use those loggers.

**Related information**  

- [CheCluster Custom Resource fields reference](configure-ref_checluster_custom_resource_fields.md)
