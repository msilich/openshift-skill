> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_implementing_telemetry_backend_event_handlers). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Implement and test telemetry backend event handlers

Implement the `AnalyticsManager` event handling methods in your telemetry backend and test the backend in a running Dev Workspace to verify that events are received from the front-end plugin.

## Before you begin

- You have a running instance of Red Hat OpenShift Dev Spaces.
- You have a telemetry backend project created. See [Create a telemetry backend](extend-proc_creating_a_telemetry_backend.md "Create a Quarkus-based telemetry backend that extends the OpenShift Dev Spaces telemetry client and implements custom event handling logic.").

## Procedure

1.  Set the `DEVWORKSPACE_TELEMETRY_BACKEND_PORT` environment variable in the Dev Workspace. Here, the value is set to `4167`.

    ``` yaml
    spec:
      template:
        attributes:
          workspaceEnv:
            - name: DEVWORKSPACE_TELEMETRY_BACKEND_PORT
              value: '4167'
    ```

2.  Restart the Dev Workspace from the Red Hat OpenShift Dev Spaces dashboard.

3.  Run the following command within a Dev Workspace’s terminal window to start the application. Use the `--settings` flag to specify the path to the `settings.xml` file that contains the GitHub access token.

    ``` bash
    $ mvn --settings=settings.xml quarkus:dev -Dquarkus.http.port=${DEVWORKSPACE_TELEMETRY_BACKEND_PORT}
    ```

    The application now receives telemetry events through port `4167` from the front-end plugin. Verify that the following output is logged:

    ``` shell-session
    INFO  [org.ecl.che.inc.AnalyticsManager] (Quarkus Main Thread) No welcome message provided
    INFO  [io.quarkus] (Quarkus Main Thread) devworkspace-telemetry-example-plugin 1.0.0-SNAPSHOT on JVM (powered by Quarkus 2.7.2.Final) started in 0.323s. Listening on: http://localhost:4167
    INFO  [io.quarkus] (Quarkus Main Thread) Profile dev activated. Live Coding activated.
    INFO  [io.quarkus] (Quarkus Main Thread) Installed features: [cdi, kubernetes-client, rest-client, rest-client-jackson, resteasy, resteasy-jsonb, smallrye-context-propagation, smallrye-openapi, swagger-ui, vertx]
    ```

4.  Customize `isEnabled()` in `AnalyticsManager.java`. For this example, the method always returns `true`:

    ``` plaintext
    @Override
    public boolean isEnabled() {
        return true;
    }
    ```

    The [hosted OpenShift Dev Spaces Woopra backend](https://github.com/che-incubator/devworkspace-telemetry-woopra-plugin/blob/main/src/main/java/com/redhat/devworkspace/services/telemetry/woopra/AnalyticsManager.java) demonstrates a more advanced `isEnabled()` implementation that checks for a configuration property before enabling the backend.

5.  Implement `onEvent()` to send events to the telemetry server. For the example application, it sends an HTTP POST payload to the `/event` endpoint.
    1.  Configure the RESTEasy REST Client by creating a `TelemetryService.java` interface:

        ``` plaintext
        package org.my.group;

        import java.util.Map;

        import javax.ws.rs.Consumes;
        import javax.ws.rs.POST;
        import javax.ws.rs.Path;
        import javax.ws.rs.core.MediaType;
        import javax.ws.rs.core.Response;

        import org.eclipse.microprofile.rest.client.inject.RegisterRestClient;

        @RegisterRestClient
        public interface TelemetryService {
            @POST
            @Path("/event")
            @Consumes(MediaType.APPLICATION_JSON)
            Response sendEvent(Map<String, Object> payload);
        }
        ```

        where:

        `@Path("/event")`  
        The endpoint to make the `POST` request to.

    2.  Specify the base URL for `TelemetryService` in `src/main/resources/application.properties`:

        ``` plaintext
        org.my.group.TelemetryService/mp-rest/url=http://little-telemetry-server-che.apps-crc.testing
        ```

    3.  Inject `TelemetryService` into `AnalyticsManager.java` and send a `POST` request in `onEvent()`:

        ``` plaintext
        @Dependent
        @Alternative
        public class AnalyticsManager extends AbstractAnalyticsManager {
            @Inject
            @RestClient
            TelemetryService telemetryService;

        ...

        @Override
        public void onEvent(AnalyticsEvent event, String ownerId, String ip, String userAgent, String resolution, Map<String, Object> properties) {
            Map<String, Object> payload = new HashMap<String, Object>(properties);
            payload.put("event", event);
            telemetryService.sendEvent(payload);
        }
        ```

        This sends an HTTP request to the telemetry server and automatically delays identical events for a small period of time. The default duration is 1500 milliseconds.

6.  Implement `increaseDuration()` in `AnalyticsManager.java`. Many telemetry systems recognize event duration. The `AbstractAnalyticsManager` merges similar events that happen in the same frame of time into one event. This implementation is a no-op:

    ``` plaintext
    @Override
    public void increaseDuration(AnalyticsEvent event, Map<String, Object> properties) {}
    ```

7.  Implement `onActivity()` in `AnalyticsManager.java`. Set an inactive timeout limit and send a `WORKSPACE_INACTIVE` event if the last event time exceeds the timeout:

    ``` plaintext
    public class AnalyticsManager extends AbstractAnalyticsManager {

        ...

        private long inactiveTimeLimit = 60000 * 3;

        ...

        @Override
        public void onActivity() {
            if (System.currentTimeMillis() - lastEventTime >= inactiveTimeLimit) {
                onEvent(WORKSPACE_INACTIVE, lastOwnerId, lastIp, lastUserAgent, lastResolution, commonProperties);
            }
        }
    ```

8.  Implement `destroy()` in `AnalyticsManager.java`. When called, send a `WORKSPACE_STOPPED` event and shut down any resources such as connection pools:

    ``` plaintext
    @Override
    public void destroy() {
        onEvent(WORKSPACE_STOPPED, lastOwnerId, lastIp, lastUserAgent, lastResolution, commonProperties);
    }
    ```

## Results

1.  To verify that the `onEvent()` method receives events from the front-end plugin, press the l key to disable Quarkus live coding and edit any file within the IDE. The following output should be logged:

    ``` shell-session
    INFO  [io.qua.dep.dev.RuntimeUpdatesProcessor] (Aesh InputStream Reader) Live reload disabled
    INFO  [org.ecl.che.inc.AnalyticsManager] (executor-thread-2) The received event is: Edit Workspace File in Che
    ```

2.  Stop the application with Ctrl+C and verify that a `WORKSPACE_STOPPED` event is sent to the server.

**Related concepts**  

- [How telemetry plugins work](extend-con_telemetry_plugin_overview.md "A telemetry plugin for OpenShift Dev Spaces collects workspace usage data and sends it to your analytics backend. The plugin extends the AbstractAnalyticsManager class with methods for event handling, activity tracking, and shutdown.")

**Related tasks**  

- [Deploy a telemetry plugin](extend-proc_deploying_a_telemetry_plugin.md "Deploy the telemetry backend as a container image, create a devfile v2 plugin, and host the plugin on a web server so that Dev Workspaces can load it.")

**Related information**  

- [How server logging works](observe-con_configuring_server_logging.md)
