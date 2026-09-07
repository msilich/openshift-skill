> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/observe-ref_collecting_logs_using_dsc). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Collect logs with dsc

The `dsc` management tool provides commands to collect OpenShift Dev Spaces logs for troubleshooting and diagnostics. These commands automate log collection from the multiple containers that comprise a Red Hat OpenShift Dev Spaces installation in the OpenShift cluster.

`dsc server:logs`  
Collects existing Red Hat OpenShift Dev Spaces server logs and stores them in a directory on the local machine. By default, logs are downloaded to a temporary directory on the machine. However, this can be overwritten by specifying the `-d` parameter. For example, to download OpenShift Dev Spaces logs to the `/home/user/che-logs/` directory, use the command

``` bash
dsc server:logs -d /home/user/che-logs/
```

When run, `dsc server:logs` prints a message in the console specifying the directory that stores the log files:

``` shell-session
Red Hat OpenShift Dev Spaces logs will be available in '/tmp/chectl-logs/1648575098344'
```

If Red Hat OpenShift Dev Spaces is installed in a non-default project, `dsc server:logs` requires the `-n <NAMESPACE>` parameter. `<NAMESPACE>` is the project in which Red Hat OpenShift Dev Spaces was installed. For example, to get logs from OpenShift Dev Spaces in the `my-namespace` project, use the command

``` bash
dsc server:logs -n my-namespace
```

`dsc server:deploy`  
Logs are automatically collected during the OpenShift Dev Spaces installation when installed using `dsc`. As with `dsc server:logs`, the directory logs are stored in can be specified using the `-d` parameter.

**Related information**  

- [dsc reference documentation](https://github.com/redhat-developer/devspaces-chectl)
