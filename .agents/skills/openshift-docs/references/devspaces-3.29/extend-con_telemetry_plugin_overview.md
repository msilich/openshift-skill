> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-con_telemetry_plugin_overview). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# How telemetry plugins work

A telemetry plugin for OpenShift Dev Spaces collects workspace usage data and sends it to your analytics backend. The plugin extends the `AbstractAnalyticsManager` class with methods for event handling, activity tracking, and shutdown.

The `AbstractAnalyticsManager` class requires the following method implementations:

- `isEnabled()` - determines whether the telemetry backend is functioning correctly. This can mean always returning `true`, or have more complex checks, for example, returning `false` when a connection property is missing.
- `destroy()` - cleanup method that is run before shutting down the telemetry backend. This method sends the `WORKSPACE_STOPPED` event.
- `onActivity()` - notifies that some activity is still happening for a given user. This is mainly used to send `WORKSPACE_INACTIVE` events.
- `onEvent()` - submits telemetry events to the telemetry server, such as `WORKSPACE_USED` or `WORKSPACE_STARTED`.
- `increaseDuration()` - increases the duration of a current event rather than sending many events in a small frame of time.

A finished example of the telemetry backend is available in the devworkspace-telemetry-example-plugin repository. For procedures to implement each method and the complete example code, see Additional resources.

**Related tasks**  

- [Create a telemetry server](extend-proc_creating_a_telemetry_server.md "Create a server that receives telemetry events from the OpenShift Dev Spaces telemetry plugin and writes them to standard output. For production, consider integrating with a third-party telemetry system such as Segment or Woopra.")
- [Create a telemetry backend](extend-proc_creating_a_telemetry_backend.md "Create a Quarkus-based telemetry backend that extends the OpenShift Dev Spaces telemetry client and implements custom event handling logic.")
- [Implement and test telemetry backend event handlers](extend-proc_implementing_telemetry_backend_event_handlers.md "Implement the AnalyticsManager event handling methods in your telemetry backend and test the backend in a running Dev Workspace to verify that events are received from the front-end plugin.")
- [Deploy a telemetry plugin](extend-proc_deploying_a_telemetry_plugin.md "Deploy the telemetry backend as a container image, create a devfile v2 plugin, and host the plugin on a web server so that Dev Workspaces can load it.")
- [Configure workspaces to load a telemetry plugin](extend-proc_configuring_workspaces_to_load_telemetry_plugin.md "Configure Dev Workspaces to load the telemetry plugin so that workspace activity events are sent to your telemetry backend for collection and analysis.")

**Related information**  

- [devworkspace-telemetry-example-plugin](https://github.com/che-incubator/devworkspace-telemetry-example-plugin)
