<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To troubleshoot some issues with nodes, establish the kubelet’s log level verbosity depending on the issue to be tracked.

# Modifying the kubelet as a one-time scenario

To modify the kubelet in a one-time scenario without rebooting the node due to the change of `machine-config(spec":{"paused":false}})`, allowing you to modify the kubelet without affecting the service, follow this procedure.

<div>

<div class="title">

Procedure

</div>

1.  Connect to the node in debug mode:

    ``` terminal
    $ oc debug node/<node>
    ```

    ``` terminal
    $ chroot /host
    ```

    Alternatively, it is possible to SSH to the node and become root.

2.  After access is established, check the default log level:

    ``` terminal
    $ systemctl cat kubelet
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    # /etc/systemd/system/kubelet.service.d/20-logging.conf
    [Service]
    Environment="KUBELET_LOG_LEVEL=2"
    ```

    </div>

3.  Define the new verbosity required in a new `/etc/systemd/system/kubelet.service.d/30-logging.conf` file, which overrides `/etc/systemd/system/kubelet.service.d/20-logging.conf`. In this example, the verbosity is changed from `2` to `8`:

    ``` terminal
    $ echo -e "[Service]\nEnvironment=\"KUBELET_LOG_LEVEL=8\"" > /etc/systemd/system/kubelet.service.d/30-logging.conf
    ```

4.  Reload systemd and restart the service:

    ``` terminal
    $ systemctl daemon-reload
    ```

    ``` terminal
    $ systemctl restart kubelet
    ```

5.  Gather the logs, and then revert the log level increase:

    ``` terminal
    $ rm -f /etc/systemd/system/kubelet.service.d/30-logging.conf
    ```

    ``` terminal
    $ systemctl daemon-reload
    ```

    ``` terminal
    $ systemctl restart kubelet
    ```

</div>

# Persistent kubelet log level configuration

<div>

<div class="title">

Procedure

</div>

- Use the following `MachineConfig` object for persistent kubelet log level configuration:

  ``` yaml
   apiVersion: machineconfiguration.openshift.io/v1
   kind: MachineConfig
   metadata:
     labels:
       machineconfiguration.openshift.io/role: master
     name: 99-master-kubelet-loglevel
   spec:
     config:
       ignition:
         version: 3.2.0
       systemd:
         units:
           - name: kubelet.service
             enabled: true
             dropins:
               - name: 30-logging.conf
                 contents: |
                   [Service]
                   Environment="KUBELET_LOG_LEVEL=2"
  ```

  Generally, it is recommended to apply `0-4` as debug-level logs and `5-8` as trace-level logs.

</div>

# Log verbosity descriptions

| Log verbosity | Description |
|----|----|
| `--v=0` | Always visible to an Operator. |
| `--v=1` | A reasonable default log level if you do not want verbosity. |
| `--v=2` | Useful steady state information about the service and important log messages that might correlate to significant changes in the system. This is the recommended default log level. |
| `--v=3` | Extended information about changes. |
| `--v=4` | Debug level verbosity. |
| `--v=6` | Display requested resources. |
| `--v=7` | Display HTTP request headers. |
| `--v=8` | Display HTTP request contents. |

# Gathering kubelet logs

<div>

<div class="title">

Procedure

</div>

- After the kubelet’s log level verbosity is configured properly, you can gather logs by running the following commands:

  ``` terminal
  $ oc adm node-logs --role master -u kubelet
  ```

  ``` terminal
  $ oc adm node-logs --role worker -u kubelet
  ```

  Alternatively, inside the node, run the following command:

  ``` terminal
  $ journalctl -b -f -u kubelet.service
  ```

- To collect master container logs, run the following command:

  ``` terminal
  $ sudo tail -f /var/log/containers/*
  ```

- To directly gather the logs of all nodes, run the following command:

  ``` terminal
  - for n in $(oc get node --no-headers | awk '{print $1}'); do oc adm node-logs $n | gzip > $n.log.gz; done
  ```

</div>
