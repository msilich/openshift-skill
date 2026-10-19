<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use the Collector runtime configuration to change some collector behaviors without restarting Collector by using a `ConfigMap` object called `collector-config`.

<a id="collector-runtime-configuration-overview_{context}"></a>

# Collector runtime configuration settings

Set the Collector runtime configuration by using a `ConfigMap` object called `collector-config`. When you create or update the `ConfigMap` object, Collector refreshes the runtime configuration. When you delete the `ConfigMap` object, the settings revert to the default runtime configuration values.

You can control the following settings by using the Collector runtime configuration:

- `networking.externalIps.enabled` controls whether to enable or disable the visualizing external entities feature. The default is `DISABLED`. In release 4.6, this setting was `networking.externalIps.enable` and was a boolean. For more information, see "Visualizing external entities".

- `networking.externalIps.direction` specifies the direction for collecting external IPs. The values are `INGRESS`, `EGRESS`, or `BOTH` (default). For example, when you select `EGRESS`, it provides details for all outgoing connections while aggregating the incoming ones.

- `networking.maxConnectionsPerMinute` is the maximum number of open networking connections reported by Collector per container per minute. The default value is 2048.

<div>

<div class="title">

Additional resources

</div>

- [Visualizing external entities](visualizing-external-entities.md)

</div>

<a id="collector-runtime-configuration-example_{context}"></a>

## Collector runtime configuration example

The following example enables the visualizing external entities for outgoing connections only and sets `maxConnectionsPerMinute` to 2048.

``` yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: collector-config
  namespace: stackrox
data:
  runtime_config.yaml: |
    networking:
      externalIps:
        enabled: ENABLED
        direction: EGRESS
      maxConnectionsPerMinute: 2048
```

where:

`data.runtime_config.yaml`  
Specifies whether RHACS mounts this file at `/etc/stackrox/runtime_config.yaml`.

`data.runtime_config.yaml.networking.externalIps.direction`  
Specifies whether to collect ingress connections, egress connections, or both. If you do not specify a value, it defaults to `BOTH`.
