> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_creating_a_telemetry_backend). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a telemetry backend

Create a Quarkus-based telemetry backend that extends the OpenShift Dev Spaces telemetry client and implements custom event handling logic.

## Before you begin

- You have a running instance of Red Hat OpenShift Dev Spaces.
- You have a telemetry server deployed to receive events. See [Create a telemetry server](extend-proc_creating_a_telemetry_server.md "Create a server that receives telemetry events from the OpenShift Dev Spaces telemetry plugin and writes them to standard output. For production, consider integrating with a third-party telemetry system such as Segment or Woopra.").

## About this task

Note

For fast feedback when developing, develop inside a Dev Workspace. This way, you can run the application in a cluster and receive events from the front-end telemetry plugin.

## Procedure

1.  Create a Maven Quarkus project:

    ``` bash
    mvn io.quarkus:quarkus-maven-plugin:2.7.1.Final:create \
        -DprojectGroupId=mygroup -DprojectArtifactId=devworkspace-telemetry-example-plugin \
    -DprojectVersion=1.0.0-SNAPSHOT
    ```

2.  Remove the files under `src/main/java/mygroup` and `src/test/java/mygroup`.

3.  Consult the [GitHub packages](https://github.com/che-incubator/che-workspace-telemetry-client/packages) for the latest version of `backend-base` and add the following dependencies to your `pom.xml`:

    ``` plaintext
    <!-- Required -->
    <dependency>
        <groupId>org.eclipse.che.incubator.workspace-telemetry</groupId>
        <artifactId>backend-base</artifactId>
        <version><latest_version></version>
    </dependency>


    <!-- Used to make http requests to the telemetry server -->
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-rest-client</artifactId>
    </dependency>
    <dependency>
        <groupId>io.quarkus</groupId>
        <artifactId>quarkus-rest-client-jackson</artifactId>
    </dependency>
    ```

4.  Create a personal access token with `read:packages` permissions from [GitHub packages](https://docs.github.com/en/packages/learn-github-packages/introduction-to-github-packages) and add your GitHub username, the token, and `che-incubator` repository details in your `~/.m2/settings.xml` file:

    ``` plaintext
    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
    http://maven.apache.org/xsd/settings-1.0.0.xsd">
       <servers>
          <server>
             <id>che-incubator</id>
             <username><github_username></username>
             <password><github_token></password>
          </server>
       </servers>

       <profiles>
          <profile>
             <id>github</id>
             <activation>
                <activeByDefault>true</activeByDefault>
             </activation>
             <repositories>
                <repository>
                   <id>central</id>
                   <url>https://repo1.maven.org/maven2</url>
                   <releases><enabled>true</enabled></releases>
                   <snapshots><enabled>false</enabled></snapshots>
                   </repository>
                   <repository>
                   <id>che-incubator</id>
                   <url>https://maven.pkg.github.com/che-incubator/che-workspace-telemetry-client</url>
                </repository>
             </repositories>
          </profile>
       </profiles>
    </settings>
    ```

5.  Create `MainConfiguration.java` under `src/main/java/mygroup`. This file contains configuration provided to `AnalyticsManager`:

    ``` plaintext
    package org.my.group;

    import java.util.Optional;

    import javax.enterprise.context.Dependent;
    import javax.enterprise.inject.Alternative;

    import org.eclipse.che.incubator.workspace.telemetry.base.BaseConfiguration;
    import org.eclipse.microprofile.config.inject.ConfigProperty;

    @Dependent
    @Alternative
    public class MainConfiguration extends BaseConfiguration {
        @ConfigProperty(name = "welcome.message")
        Optional<String> welcomeMessage;
    }
    ```

    where:

    `@ConfigProperty(name = "welcome.message")`  
    A MicroProfile configuration annotation that injects the `welcome.message` configuration. For more details on how to set configuration properties specific to your backend, see the Quarkus Configuration Reference Guide.

6.  Create `AnalyticsManager.java` under `src/main/java/mygroup`. This file contains logic specific to the telemetry system:

    ``` plaintext
    package org.my.group;

    import java.util.HashMap;
    import java.util.Map;

    import javax.enterprise.context.Dependent;
    import javax.enterprise.inject.Alternative;
    import javax.inject.Inject;

    import org.eclipse.che.incubator.workspace.telemetry.base.AbstractAnalyticsManager;
    import org.eclipse.che.incubator.workspace.telemetry.base.AnalyticsEvent;
    import org.eclipse.che.incubator.workspace.telemetry.finder.DevWorkspaceFinder;
    import org.eclipse.che.incubator.workspace.telemetry.finder.UsernameFinder;
    import org.eclipse.microprofile.rest.client.inject.RestClient;
    import org.slf4j.Logger;

    import static org.slf4j.LoggerFactory.getLogger;

    @Dependent
    @Alternative
    public class AnalyticsManager extends AbstractAnalyticsManager {

        private static final Logger LOG = getLogger(AbstractAnalyticsManager.class);

        public AnalyticsManager(MainConfiguration mainConfiguration, DevWorkspaceFinder devworkspaceFinder, UsernameFinder usernameFinder) {
            super(mainConfiguration, devworkspaceFinder, usernameFinder);

            mainConfiguration.welcomeMessage.ifPresentOrElse(
                (str) -> LOG.info("The welcome message is: {}", str),
                () -> LOG.info("No welcome message provided")
            );
        }

        @Override
        public boolean isEnabled() {
            return true;
        }

        @Override
        public void destroy() {}

        @Override
        public void onEvent(AnalyticsEvent event, String ownerId, String ip, String userAgent, String resolution, Map<String, Object> properties) {
            LOG.info("The received event is: {}", event);
        }

        @Override
        public void increaseDuration(AnalyticsEvent event, Map<String, Object> properties) { }

        @Override
        public void onActivity() {}
    }
    ```

    where:

    `ifPresentOrElse()`  
    Log the welcome message if it was provided.

    `LOG.info("The received event is: {}", event)`  
    Log the event received from the front-end plugin.

7.  Add the `quarkus.arc.selected-alternatives` property to `src/main/resources/application.properties` to specify the alternative beans `org.my.group.AnalyticsManager` and `org.my.group.MainConfiguration`:

    ``` plaintext
    quarkus.arc.selected-alternatives=MainConfiguration,AnalyticsManager
    ```

## Results

- Run the Quarkus application and verify that it starts without errors:

  ``` bash
  mvn quarkus:dev
  ```

**Related concepts**  

- [How telemetry plugins work](extend-con_telemetry_plugin_overview.md "A telemetry plugin for OpenShift Dev Spaces collects workspace usage data and sends it to your analytics backend. The plugin extends the AbstractAnalyticsManager class with methods for event handling, activity tracking, and shutdown.")

**Related tasks**  

- [Implement and test telemetry backend event handlers](extend-proc_implementing_telemetry_backend_event_handlers.md "Implement the AnalyticsManager event handling methods in your telemetry backend and test the backend in a running Dev Workspace to verify that events are received from the front-end plugin.")

**Related information**  

- [Quarkus Configuration Reference Guide](https://quarkus.io/guides/config-reference)
- [How server logging works](observe-con_configuring_server_logging.md)
- [What DevWorkspace Operator metrics reveal](observe-con_monitoring_devworkspace_operator.md)
