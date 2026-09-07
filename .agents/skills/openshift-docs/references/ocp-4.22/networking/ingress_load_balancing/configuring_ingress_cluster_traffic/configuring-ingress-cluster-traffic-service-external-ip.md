<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use either a MetalLB implementation or an IP failover deployment to attach an ExternalIP resource to a service so that the service is available to traffic outside your OpenShift Container Platform cluster.

Hosting an external IP address in this way is only applicable for a cluster installed on bare-metal hardware.

You must ensure that you correctly configure the external network infrastructure to route traffic to the service.

Before you begin the procedure, ensure that you meet the following prerequisite:

- You configured your cluster with ExternalIPs enabled. For more information, see "Configuring ExternalIPs for services" in the *Additional resources* section.

> [!NOTE]
> Do not use the same ExternalIP for the egress IP.

# Attaching an ExternalIP to a service

You can attach an ExternalIP resource to a service. If you configured your cluster to automatically attach the resource to a service, you might not need to manually attach an ExternalIP to the service.

The examples in the procedure use a scenario that manually attaches an ExternalIP resource to a service in a cluster with an IP failover configuration.

<div>

<div class="title">

Procedure

</div>

1.  Confirm compatible IP address ranges for the ExternalIP resource by entering the following command in your CLI:

    ``` terminal
    $ oc get networks.config cluster -o jsonpath='{.spec.externalIP}{"\n"}'
    ```

    > [!NOTE]
    > If `autoAssignCIDRs` is set and you did not specify a value for `spec.externalIPs` in the ExternalIP resource, OpenShift Container Platform automatically assigns ExternalIP to a new `Service` object.

2.  Choose one of the following options to attach an ExternalIP resource to the service:

    1.  If you are creating a new service, specify a value in the `spec.externalIPs` parameter and array of one or more valid IP addresses in the `allowedCIDRs` parameter.

        <div class="formalpara">

        <div class="title">

        Example of service YAML configuration file that supports an ExternalIP resource

        </div>

        ``` yaml
        apiVersion: v1
        kind: Service
        metadata:
          name: svc-with-externalip
        spec:
          externalIPs:
            policy:
              allowedCIDRs:
              - 192.168.123.0/28
        # ...
        ```

        </div>

    2.  If you are attaching an ExternalIP to an existing service, enter the following command. Replace `<name>` with the service name. Replace `<ip_address>` with a valid ExternalIP address. You can provide multiple IP addresses separated by commas.

        ``` terminal
        $ oc patch svc <name> -p \
          '{
            "spec": {
              "externalIPs": [ "<ip_address>" ]
            }
          }'
        ```

        For example:

        ``` terminal
        $ oc patch svc mysql-55-rhel7 -p '{"spec":{"externalIPs":["192.174.120.10"]}}'
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        "mysql-55-rhel7" patched
        ```

        </div>

3.  To confirm that an ExternalIP address is attached to the service, enter the following command. If you specified an ExternalIP for a new service, you must create the service first.

    ``` terminal
    $ oc get svc
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME               CLUSTER-IP      EXTERNAL-IP     PORT(S)    AGE
    mysql-55-rhel7     172.30.131.89   192.174.120.10  3306/TCP   13m
    ```

    </div>

</div>

# Additional resources

[Configuring ExternalIPs for services](configuring-externalip.md#configuring-externalip)

- [About MetalLB and the MetalLB Operator](../../networking_operators/metallb-operator/about-metallb.md#about-metallb)

- [Configuring IP failover](../../configuring_network_settings/configuring-ipfailover.md#configuring-ipfailover)

- [Configuring ExternalIPs for services](configuring-externalip.md#configuring-externalip)
