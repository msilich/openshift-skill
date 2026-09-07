> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-assembly_building_telemetry_plugin). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Build a custom telemetry plugin

Build a custom telemetry plugin that collects workspace activity events and sends them to your organization’s analytics backend.

- **[How telemetry plugins work](extend-con_telemetry_plugin_overview.md)**  
  A telemetry plugin for OpenShift Dev Spaces collects workspace usage data and sends it to your analytics backend. The plugin extends the `AbstractAnalyticsManager` class with methods for event handling, activity tracking, and shutdown.
- **[Create a telemetry server](extend-proc_creating_a_telemetry_server.md)**  
  Create a server that receives telemetry events from the OpenShift Dev Spaces telemetry plugin and writes them to standard output. For production, consider integrating with a third-party telemetry system such as Segment or Woopra.
- **[Create a telemetry backend](extend-proc_creating_a_telemetry_backend.md)**  
  Create a Quarkus-based telemetry backend that extends the OpenShift Dev Spaces telemetry client and implements custom event handling logic.
- **[Implement and test telemetry backend event handlers](extend-proc_implementing_telemetry_backend_event_handlers.md)**  
  Implement the `AnalyticsManager` event handling methods in your telemetry backend and test the backend in a running Dev Workspace to verify that events are received from the front-end plugin.
- **[Deploy a telemetry plugin](extend-proc_deploying_a_telemetry_plugin.md)**  
  Deploy the telemetry backend as a container image, create a devfile v2 plugin, and host the plugin on a web server so that Dev Workspaces can load it.
- **[Configure workspaces to load a telemetry plugin](extend-proc_configuring_workspaces_to_load_telemetry_plugin.md)**  
  Configure Dev Workspaces to load the telemetry plugin so that workspace activity events are sent to your telemetry backend for collection and analysis.

**Related information**  

- [Monitor platform health](observe-con_observing_devspaces.md)
- [Customize workspace tooling](extend-con_extending_devspaces.md)
