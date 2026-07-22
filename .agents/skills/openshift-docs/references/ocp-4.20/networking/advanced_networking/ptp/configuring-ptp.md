<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The PTP Operator adds the `NodePtpDevice.ptp.openshift.io` custom resource definition (CRD) to OpenShift Container Platform.

When installed, the PTP Operator searches your cluster for Precision Time Protocol (PTP) capable network devices on each node. The Operator creates and updates a `NodePtpDevice` custom resource (CR) object for each node that provides a compatible PTP-capable network device.

Network interface controller (NIC) hardware with built-in PTP capabilities sometimes require a device-specific configuration. You can use hardware-specific NIC features for supported hardware with the PTP Operator by configuring a plugin in the `PtpConfig` custom resource (CR). The `linuxptp-daemon` service uses the named parameters in the `plugin` stanza to start `linuxptp` processes, `ptp4l` and `phc2sys`, based on the specific hardware configuration.

> [!IMPORTANT]
> In OpenShift Container Platform 4.17, the Intel E810 NIC is supported with a `PtpConfig` plugin.

# Installing the PTP Operator using the CLI

As a cluster administrator, you can install the Operator by using the CLI.

<div>

<div class="title">

Prerequisites

</div>

- A cluster installed on bare-metal hardware with nodes that have hardware that supports PTP.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a namespace for the PTP Operator.

    1.  Save the following YAML in the `ptp-namespace.yaml` file:

        ``` yaml
        apiVersion: v1
        kind: Namespace
        metadata:
          name: openshift-ptp
          annotations:
            workload.openshift.io/allowed: management
          labels:
            name: openshift-ptp
            openshift.io/cluster-monitoring: "true"
        ```

    2.  Create the `Namespace` CR:

        ``` terminal
        $ oc create -f ptp-namespace.yaml
        ```

2.  Create an Operator group for the PTP Operator.

    1.  Save the following YAML in the `ptp-operatorgroup.yaml` file:

        ``` yaml
        apiVersion: operators.coreos.com/v1
        kind: OperatorGroup
        metadata:
          name: ptp-operators
          namespace: openshift-ptp
        spec:
          targetNamespaces:
          - openshift-ptp
        ```

    2.  Create the `OperatorGroup` CR:

        ``` terminal
        $ oc create -f ptp-operatorgroup.yaml
        ```

3.  Subscribe to the PTP Operator.

    1.  Save the following YAML in the `ptp-sub.yaml` file:

        ``` yaml
        apiVersion: operators.coreos.com/v1alpha1
        kind: Subscription
        metadata:
          name: ptp-operator-subscription
          namespace: openshift-ptp
        spec:
          channel: "stable"
          name: ptp-operator
          source: redhat-operators
          sourceNamespace: openshift-marketplace
        ```

    2.  Create the `Subscription` CR:

        ``` terminal
        $ oc create -f ptp-sub.yaml
        ```

4.  To verify that the Operator is installed, enter the following command:

    ``` terminal
    $ oc get csv -n openshift-ptp -o custom-columns=Name:.metadata.name,Phase:.status.phase
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Name                         Phase
    4.17.0-202301261535          Succeeded
    ```

    </div>

</div>

# Installing the PTP Operator by using the web console

As a cluster administrator, you can install the PTP Operator by using the web console.

> [!NOTE]
> If you are installing by using the CLI, you must create the namespace and Operator group before installing the Operator. If you are installing by using the web console, the Operator Lifecycle Manager (OLM) automatically creates the namespace.

<div>

<div class="title">

Procedure

</div>

1.  Install the PTP Operator using the OpenShift Container Platform web console:

    1.  In the OpenShift Container Platform web console, click **Ecosystem** → **Software Catalog**.

    2.  Type `ptp` in the **Filter by keyword** box to find the PTP Operator.

    3.  Click the **PTP Operator** tile, and then click **Install**.

    4.  On the **Install Operator** page, ensure that **A specific namespace on the cluster** is selected and the **Operator recommended Namespace** `openshift-ptp` is shown. Click **Install**.

    5.  Wait for the installation to complete and then click **View installed Operators**.

2.  Optional: Verify that the PTP Operator installed successfully:

    1.  Navigate to **Ecosystem** → **Installed Operators**.

    2.  Ensure that **PTP Operator** is listed in the **openshift-ptp** project with a **Status** of **Succeeded**.

        > [!NOTE]
        > During installation an Operator might display a **Failed** status. If the installation later succeeds with an **Succeeded** message, you can ignore the **Failed** message.

        If the Operator does not appear as installed, to troubleshoot further:

        - Go to the **Ecosystem** → **Installed Operators** page and inspect the **Operator Subscriptions** and **Install Plans** tabs for any failure or errors under **Status**.

        - Go to the **Workloads** → **Pods** page and check the logs for pods in the `openshift-ptp` project.

</div>

# Discovering PTP-capable network devices in your cluster

Identify PTP-capable network devices that exist in your cluster so that you can configure them

<div>

<div class="title">

Prerequisites

</div>

- You installed the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

- To return a complete list of PTP capable network devices in your cluster, run the following command:

  ``` terminal
  $ oc get NodePtpDevice -n openshift-ptp -o yaml
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  apiVersion: v1
  items:
  - apiVersion: ptp.openshift.io/v1
    kind: NodePtpDevice
    metadata:
      creationTimestamp: "2022-01-27T15:16:28Z"
      generation: 1
      name: dev-worker-0
      namespace: openshift-ptp
      resourceVersion: "6538103"
      uid: d42fc9ad-bcbf-4590-b6d8-b676c642781a
    spec: {}
    status:
      devices:
      - name: eno1
      - name: eno2
      - name: eno3
      - name: eno4
      - name: enp5s0f0
      - name: enp5s0f1
  ...
  ```

  </div>

  where:

  `-worker-0`
  The value for the `name` parameter is the same as the name of the parent node.

  `devices`
  The `devices` collection includes a list of the PTP capable devices that the PTP Operator discovers for the node.

</div>

# Configuring linuxptp services as a grandmaster clock

You can configure the `linuxptp` services (`ptp4l`, `phc2sys`, `ts2phc`) as grandmaster clock (T-GM) by creating a `PtpConfig` custom resource (CR) that configures the host NIC.

The `ts2phc` utility allows you to synchronize the system clock with the PTP grandmaster clock so that the node can stream precision clock signal to downstream PTP ordinary clocks and boundary clocks.

> [!NOTE]
> Use the following example `PtpConfig` CR as the basis to configure `linuxptp` services as T-GM for an Intel Westport Channel E810-XXVDA4T network interface.
>
> To configure PTP fast events, set appropriate values for `ptp4lOpts`, `ptp4lConf`, and `ptpClockThreshold`. `ptpClockThreshold` is used only when events are enabled. See "Configuring the PTP fast event notifications publisher" for more information.

<div>

<div class="title">

Prerequisites

</div>

- For T-GM clocks in production environments, install an Intel E810 Westport Channel NIC in the bare-metal cluster host.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `PtpConfig` CR. For example:

    1.  Depending on your requirements, use one of the following T-GM configurations for your deployment. Save the YAML in the `grandmaster-clock-ptp-config.yaml` file:

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: grandmaster
          namespace: openshift-ptp
          annotations: {}
        spec:
          profile:
            - name: "grandmaster"
              ptp4lOpts: "-2 --summary_interval -4"
              phc2sysOpts: -r -u 0 -m -N 8 -R 16 -s $iface_master -n 24
              ptpSchedulingPolicy: SCHED_FIFO
              ptpSchedulingPriority: 10
              ptpSettings:
                logReduce: "true"
              plugins:
                e810:
                  enableDefaultConfig: false
                  settings:
                    LocalMaxHoldoverOffSet: 1500
                    LocalHoldoverTimeout: 14400
                    MaxInSpecOffset: 1500
                  pins: $e810_pins
                  #  "$iface_master":
                  #    "U.FL2": "0 2"
                  #    "U.FL1": "0 1"
                  #    "SMA2": "0 2"
                  #    "SMA1": "0 1"
                  ublxCmds:
                    - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                        - "-P"
                        - "29.20"
                        - "-z"
                        - "CFG-HW-ANT_CFG_VOLTCTRL,1"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -e GPS
                        - "-P"
                        - "29.20"
                        - "-e"
                        - "GPS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d Galileo
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "Galileo"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d GLONASS
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "GLONASS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d BeiDou
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "BeiDou"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d SBAS
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "SBAS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                        - "-P"
                        - "29.20"
                        - "-t"
                        - "-w"
                        - "5"
                        - "-v"
                        - "1"
                        - "-e"
                        - "SURVEYIN,600,50000"
                      reportOutput: true
                    - args: #ubxtool -P 29.20 -p MON-HW
                        - "-P"
                        - "29.20"
                        - "-p"
                        - "MON-HW"
                      reportOutput: true
                    - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                        - "-P"
                        - "29.20"
                        - "-p"
                        - "CFG-MSG,1,38,248"
                      reportOutput: true
              ts2phcOpts: " "
              ts2phcConf: |
                [nmea]
                ts2phc.master 1
                [global]
                use_syslog  0
                verbose 1
                logging_level 7
                ts2phc.pulsewidth 100000000
                #cat /dev/GNSS to find available serial port
                #example value of gnss_serialport is /dev/ttyGNSS_1700_0
                ts2phc.nmea_serialport $gnss_serialport
                [$iface_master]
                ts2phc.extts_polarity rising
                ts2phc.extts_correction 0
              ptp4lConf: |
                [$iface_master]
                masterOnly 1
                [$iface_master_1]
                masterOnly 1
                [$iface_master_2]
                masterOnly 1
                [$iface_master_3]
                masterOnly 1
                [global]
                #
                # Default Data Set
                #
                twoStepFlag 1
                priority1 128
                priority2 128
                domainNumber 24
                #utc_offset 37
                clockClass 6
                clockAccuracy 0x27
                offsetScaledLogVariance 0xFFFF
                free_running 0
                freq_est_interval 1
                dscp_event 0
                dscp_general 0
                dataset_comparison G.8275.x
                G.8275.defaultDS.localPriority 128
                #
                # Port Data Set
                #
                logAnnounceInterval -3
                logSyncInterval -4
                logMinDelayReqInterval -4
                logMinPdelayReqInterval 0
                announceReceiptTimeout 3
                syncReceiptTimeout 0
                delayAsymmetry 0
                fault_reset_interval -4
                neighborPropDelayThresh 20000000
                masterOnly 0
                G.8275.portDS.localPriority 128
                #
                # Run time options
                #
                assume_two_step 0
                logging_level 6
                path_trace_enabled 0
                follow_up_info 0
                hybrid_e2e 0
                inhibit_multicast_service 0
                net_sync_monitor 0
                tc_spanning_tree 0
                tx_timestamp_timeout 50
                unicast_listen 0
                unicast_master_table 0
                unicast_req_duration 3600
                use_syslog 1
                verbose 0
                summary_interval -4
                kernel_leap 1
                check_fup_sync 0
                clock_class_threshold 7
                #
                # Servo Options
                #
                pi_proportional_const 0.0
                pi_integral_const 0.0
                pi_proportional_scale 0.0
                pi_proportional_exponent -0.3
                pi_proportional_norm_max 0.7
                pi_integral_scale 0.0
                pi_integral_exponent 0.4
                pi_integral_norm_max 0.3
                step_threshold 2.0
                first_step_threshold 0.00002
                clock_servo pi
                sanity_freq_limit  200000000
                ntpshm_segment 0
                #
                # Transport options
                #
                transportSpecific 0x0
                ptp_dst_mac 01:1B:19:00:00:00
                p2p_dst_mac 01:80:C2:00:00:0E
                udp_ttl 1
                udp6_scope 0x0E
                uds_address /var/run/ptp4l
                #
                # Default interface options
                #
                clock_type BC
                network_transport L2
                delay_mechanism E2E
                time_stamping hardware
                tsproc_mode filter
                delay_filter moving_median
                delay_filter_length 10
                egressLatency 0
                ingressLatency 0
                boundary_clock_jbod 0
                #
                # Clock description
                #
                productDescription ;;
                revisionData ;;
                manufacturerIdentity 00:00:00
                userDescription ;
                timeSource 0x20
          recommend:
            - profile: "grandmaster"
              priority: 4
              match:
                - nodeLabel: "node-role.kubernetes.io/$mcp"
        ```

        > [!NOTE]
        > For E810 Westport Channel NICs, set the value for `ts2phc.nmea_serialport` to `/dev/gnss0`.

    2.  Create the CR by running the following command:

        ``` terminal
        $ oc create -f grandmaster-clock-ptp-config.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                          READY   STATUS    RESTARTS   AGE     IP             NODE
        linuxptp-daemon-74m2g         3/3     Running   3          4d15h   10.16.230.7    compute-1.example.com
        ptp-operator-5f4f48d7c-x7zkf  1/1     Running   1          4d15h   10.128.1.145   compute-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile. Run the following command:

        ``` terminal
        $ oc logs linuxptp-daemon-74m2g -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ts2phc[94980.334]: [ts2phc.0.config] nmea delay: 98690975 ns
        ts2phc[94980.334]: [ts2phc.0.config] ens3f0 extts index 0 at 1676577329.999999999 corr 0 src 1676577330.901342528 diff -1
        ts2phc[94980.334]: [ts2phc.0.config] ens3f0 master offset         -1 s2 freq      -1
        ts2phc[94980.441]: [ts2phc.0.config] nmea sentence: GNRMC,195453.00,A,4233.24427,N,07126.64420,W,0.008,,160223,,,A,V
        phc2sys[94980.450]: [ptp4l.0.config] CLOCK_REALTIME phc offset       943 s2 freq  -89604 delay    504
        phc2sys[94980.512]: [ptp4l.0.config] CLOCK_REALTIME phc offset      1000 s2 freq  -89264 delay    474
        ```

        </div>

</div>

## Configuring linuxptp services as a grandmaster clock for 2 E810 NICs

You can configure the `linuxptp` services (`ptp4l`, `phc2sys`, `ts2phc`) as a grandmaster clock (T-GM) for 2 E810 NICs by creating a `PtpConfig` custom resource (CR) that configures the NICs.

You can configure the `linuxptp` services as a T-GM for the following E810 NICs:

- Intel E810-XXVDA4T Westport Channel NIC

- Intel E810-CQDA2T Logan Beach NIC

For distributed RAN (D-RAN) use cases, you can configure PTP for 2 NICs as follows:

- NIC 1 is synced to the global navigation satellite system (GNSS) time source.

- NIC 2 is synced to the 1PPS timing output provided by NIC one. This configuration is provided by the PTP hardware plugin in the `PtpConfig` CR.

The 2-card PTP T-GM configuration uses one instance of `ptp4l` and one instance of `ts2phc`. The `ptp4l` and `ts2phc` programs are each configured to operate on two PTP hardware clocks (PHCs), one for each NIC. The host system clock is synchronized from the NIC that is connected to the GNSS time source.

> [!NOTE]
> Use the following example `PtpConfig` CR as the basis to configure `linuxptp` services as T-GM for dual Intel E810 network interfaces.
>
> To configure PTP fast events, set appropriate values for `ptp4lOpts`, `ptp4lConf`, and `ptpClockThreshold`. `ptpClockThreshold` is used only when events are enabled. See "Configuring the PTP fast event notifications publisher" for more information.

<div>

<div class="title">

Prerequisites

</div>

- For T-GM clocks in production environments, install two Intel E810 NICs in the bare-metal cluster host.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `PtpConfig` CR. For example:

    1.  Save the following YAML in the `grandmaster-clock-ptp-config-dual-nics.yaml` file:

        ``` yaml
        # In this example two cards $iface_nic1 and $iface_nic2 are connected via
        # SMA1 ports by a cable and $iface_nic2 receives 1PPS signals from $iface_nic1
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: grandmaster
          namespace: openshift-ptp
          annotations: {}
        spec:
          profile:
            - name: "grandmaster"
              ptp4lOpts: "-2 --summary_interval -4"
              phc2sysOpts: -r -u 0 -m -N 8 -R 16 -s $iface_nic1 -n 24
              ptpSchedulingPolicy: SCHED_FIFO
              ptpSchedulingPriority: 10
              ptpSettings:
                logReduce: "true"
              plugins:
                e810:
                  enableDefaultConfig: false
                  settings:
                    LocalMaxHoldoverOffSet: 1500
                    LocalHoldoverTimeout: 14400
                    MaxInSpecOffset: 1500
                  pins: $e810_pins
                  #  "$iface_nic1":
                  #    "U.FL2": "0 2"
                  #    "U.FL1": "0 1"
                  #    "SMA2": "0 2"
                  #    "SMA1": "2 1"
                  #  "$iface_nic2":
                  #    "U.FL2": "0 2"
                  #    "U.FL1": "0 1"
                  #    "SMA2": "0 2"
                  #    "SMA1": "1 1"
                  ublxCmds:
                    - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                        - "-P"
                        - "29.20"
                        - "-z"
                        - "CFG-HW-ANT_CFG_VOLTCTRL,1"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -e GPS
                        - "-P"
                        - "29.20"
                        - "-e"
                        - "GPS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d Galileo
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "Galileo"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d GLONASS
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "GLONASS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d BeiDou
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "BeiDou"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -d SBAS
                        - "-P"
                        - "29.20"
                        - "-d"
                        - "SBAS"
                      reportOutput: false
                    - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                        - "-P"
                        - "29.20"
                        - "-t"
                        - "-w"
                        - "5"
                        - "-v"
                        - "1"
                        - "-e"
                        - "SURVEYIN,600,50000"
                      reportOutput: true
                    - args: #ubxtool -P 29.20 -p MON-HW
                        - "-P"
                        - "29.20"
                        - "-p"
                        - "MON-HW"
                      reportOutput: true
                    - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                        - "-P"
                        - "29.20"
                        - "-p"
                        - "CFG-MSG,1,38,248"
                      reportOutput: true
              ts2phcOpts: " "
              ts2phcConf: |
                [nmea]
                ts2phc.master 1
                [global]
                use_syslog  0
                verbose 1
                logging_level 7
                ts2phc.pulsewidth 100000000
                #cat /dev/GNSS to find available serial port
                #example value of gnss_serialport is /dev/ttyGNSS_1700_0
                ts2phc.nmea_serialport $gnss_serialport
                [$iface_nic1]
                ts2phc.extts_polarity rising
                ts2phc.extts_correction 0
                [$iface_nic2]
                ts2phc.master 0
                ts2phc.extts_polarity rising
                #this is a measured value in nanoseconds to compensate for SMA cable delay
                ts2phc.extts_correction -10
              ptp4lConf: |
                [$iface_nic1]
                masterOnly 1
                [$iface_nic1_1]
                masterOnly 1
                [$iface_nic1_2]
                masterOnly 1
                [$iface_nic1_3]
                masterOnly 1
                [$iface_nic2]
                masterOnly 1
                [$iface_nic2_1]
                masterOnly 1
                [$iface_nic2_2]
                masterOnly 1
                [$iface_nic2_3]
                masterOnly 1
                [global]
                #
                # Default Data Set
                #
                twoStepFlag 1
                priority1 128
                priority2 128
                domainNumber 24
                #utc_offset 37
                clockClass 6
                clockAccuracy 0x27
                offsetScaledLogVariance 0xFFFF
                free_running 0
                freq_est_interval 1
                dscp_event 0
                dscp_general 0
                dataset_comparison G.8275.x
                G.8275.defaultDS.localPriority 128
                #
                # Port Data Set
                #
                logAnnounceInterval -3
                logSyncInterval -4
                logMinDelayReqInterval -4
                logMinPdelayReqInterval 0
                announceReceiptTimeout 3
                syncReceiptTimeout 0
                delayAsymmetry 0
                fault_reset_interval -4
                neighborPropDelayThresh 20000000
                masterOnly 0
                G.8275.portDS.localPriority 128
                #
                # Run time options
                #
                assume_two_step 0
                logging_level 6
                path_trace_enabled 0
                follow_up_info 0
                hybrid_e2e 0
                inhibit_multicast_service 0
                net_sync_monitor 0
                tc_spanning_tree 0
                tx_timestamp_timeout 50
                unicast_listen 0
                unicast_master_table 0
                unicast_req_duration 3600
                use_syslog 1
                verbose 0
                summary_interval -4
                kernel_leap 1
                check_fup_sync 0
                clock_class_threshold 7
                #
                # Servo Options
                #
                pi_proportional_const 0.0
                pi_integral_const 0.0
                pi_proportional_scale 0.0
                pi_proportional_exponent -0.3
                pi_proportional_norm_max 0.7
                pi_integral_scale 0.0
                pi_integral_exponent 0.4
                pi_integral_norm_max 0.3
                step_threshold 2.0
                first_step_threshold 0.00002
                clock_servo pi
                sanity_freq_limit  200000000
                ntpshm_segment 0
                #
                # Transport options
                #
                transportSpecific 0x0
                ptp_dst_mac 01:1B:19:00:00:00
                p2p_dst_mac 01:80:C2:00:00:0E
                udp_ttl 1
                udp6_scope 0x0E
                uds_address /var/run/ptp4l
                #
                # Default interface options
                #
                clock_type BC
                network_transport L2
                delay_mechanism E2E
                time_stamping hardware
                tsproc_mode filter
                delay_filter moving_median
                delay_filter_length 10
                egressLatency 0
                ingressLatency 0
                boundary_clock_jbod 1
                #
                # Clock description
                #
                productDescription ;;
                revisionData ;;
                manufacturerIdentity 00:00:00
                userDescription ;
                timeSource 0x20
          recommend:
            - profile: "grandmaster"
              priority: 4
              match:
                - nodeLabel: "node-role.kubernetes.io/$mcp"
        ```

        > [!NOTE]
        > Set the value for `ts2phc.nmea_serialport` to `/dev/gnss0`.

    2.  Create the CR by running the following command:

        ``` terminal
        $ oc create -f grandmaster-clock-ptp-config-dual-nics.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                          READY   STATUS    RESTARTS   AGE     IP             NODE
        linuxptp-daemon-74m2g         3/3     Running   3          4d15h   10.16.230.7    compute-1.example.com
        ptp-operator-5f4f48d7c-x7zkf  1/1     Running   1          4d15h   10.128.1.145   compute-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile. Run the following command:

        ``` terminal
        $ oc logs linuxptp-daemon-74m2g -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ts2phc[509863.660]: [ts2phc.0.config] nmea delay: 347527248 ns
        ts2phc[509863.660]: [ts2phc.0.config] ens2f0 extts index 0 at 1705516553.000000000 corr 0 src 1705516553.652499081 diff 0
        ts2phc[509863.660]: [ts2phc.0.config] ens2f0 master offset          0 s2 freq      -0
        I0117 18:35:16.000146 1633226 stats.go:57] state updated for ts2phc =s2
        I0117 18:35:16.000163 1633226 event.go:417] dpll State s2, gnss State s2, tsphc state s2, gm state s2,
        ts2phc[1705516516]:[ts2phc.0.config] ens2f0 nmea_status 1 offset 0 s2
        GM[1705516516]:[ts2phc.0.config] ens2f0 T-GM-STATUS s2
        ts2phc[509863.677]: [ts2phc.0.config] ens7f0 extts index 0 at 1705516553.000000010 corr -10 src 1705516553.652499081 diff 0
        ts2phc[509863.677]: [ts2phc.0.config] ens7f0 master offset          0 s2 freq      -0
        I0117 18:35:16.016597 1633226 stats.go:57] state updated for ts2phc =s2
        phc2sys[509863.719]: [ptp4l.0.config] CLOCK_REALTIME phc offset        -6 s2 freq  +15441 delay    510
        phc2sys[509863.782]: [ptp4l.0.config] CLOCK_REALTIME phc offset        -7 s2 freq  +15438 delay    502
        ```

        </div>

</div>

## Configuring linuxptp services as a grandmaster clock for 3 E810 NICs

You can configure the `linuxptp` services (`ptp4l`, `phc2sys`, `ts2phc`) as a grandmaster clock (T-GM) for 3 E810 NICs by creating a `PtpConfig` custom resource (CR) that configures the NICs.

You can configure the `linuxptp` services as a T-GM with 3 NICs for the following E810 NICs:

- Intel E810-XXVDA4T Westport Channel NIC

- Intel E810-CQDA2T Logan Beach NIC

For distributed RAN (D-RAN) use cases, you can configure PTP for 3 NICs as follows:

- NIC 1 is synced to the Global Navigation Satellite System (GNSS)

- NICs 2 and 3 are synced to NIC 1 with 1PPS faceplate connections

Use the following example `PtpConfig` CRs as the basis to configure `linuxptp` services as a 3-card Intel E810 T-GM.

<div>

<div class="title">

Prerequisites

</div>

- For T-GM clocks in production environments, install 3 Intel E810 NICs in the bare-metal cluster host.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the `PtpConfig` CR. For example:

    1.  Save the following YAML in the `three-nic-grandmaster-clock-ptp-config.yaml` file:

        ``` yaml
        # In this example, the three cards are connected via SMA cables:
        # - $iface_timeTx1 has the GNSS signal input
        # - $iface_timeTx2 SMA1 is connected to $iface_timeTx1 SMA1
        # - $iface_timeTx3 SMA1 is connected to $iface_timeTx1 SMA2
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: gm-3card
          namespace: openshift-ptp
          annotations:
            ran.openshift.io/ztp-deploy-wave: "10"
        spec:
          profile:
          - name: grandmaster
            ptp4lOpts: -2 --summary_interval -4
            phc2sysOpts: -r -u 0 -m -N 8 -R 16 -s $iface_timeTx1 -n 24
            ptpSchedulingPolicy: SCHED_FIFO
            ptpSchedulingPriority: 10
            ptpSettings:
              logReduce: "true"
            plugins:
              e810:
                enableDefaultConfig: false
                settings:
                  LocalHoldoverTimeout: 14400
                  LocalMaxHoldoverOffSet: 1500
                  MaxInSpecOffset: 1500
                pins:
                  # Syntax guide:
                  # - The 1st number in each pair must be one of:
                  #    0 - Disabled
                  #    1 - RX
                  #    2 - TX
                  # - The 2nd number in each pair must match the channel number
                  $iface_timeTx1:
                    SMA1: 2 1
                    SMA2: 2 2
                    U.FL1: 0 1
                    U.FL2: 0 2
                  $iface_timeTx2:
                    SMA1: 1 1
                    SMA2: 0 2
                    U.FL1: 0 1
                    U.FL2: 0 2
                  $iface_timeTx3:
                    SMA1: 1 1
                    SMA2: 0 2
                    U.FL1: 0 1
                    U.FL2: 0 2
                ublxCmds:
                  - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                      - "-P"
                      - "29.20"
                      - "-z"
                      - "CFG-HW-ANT_CFG_VOLTCTRL,1"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -e GPS
                      - "-P"
                      - "29.20"
                      - "-e"
                      - "GPS"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -d Galileo
                      - "-P"
                      - "29.20"
                      - "-d"
                      - "Galileo"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -d GLONASS
                      - "-P"
                      - "29.20"
                      - "-d"
                      - "GLONASS"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -d BeiDou
                      - "-P"
                      - "29.20"
                      - "-d"
                      - "BeiDou"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -d SBAS
                      - "-P"
                      - "29.20"
                      - "-d"
                      - "SBAS"
                    reportOutput: false
                  - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                      - "-P"
                      - "29.20"
                      - "-t"
                      - "-w"
                      - "5"
                      - "-v"
                      - "1"
                      - "-e"
                      - "SURVEYIN,600,50000"
                    reportOutput: true
                  - args: #ubxtool -P 29.20 -p MON-HW
                      - "-P"
                      - "29.20"
                      - "-p"
                      - "MON-HW"
                    reportOutput: true
                  - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                      - "-P"
                      - "29.20"
                      - "-p"
                      - "CFG-MSG,1,38,248"
                    reportOutput: true
            ts2phcOpts: " "
            ts2phcConf: |
              [nmea]
              ts2phc.master 1
              [global]
              use_syslog  0
              verbose 1
              logging_level 7
              ts2phc.pulsewidth 100000000
              #example value of nmea_serialport is /dev/gnss0
              ts2phc.nmea_serialport (?<gnss_serialport>[/\w\s/]+)
              leapfile /usr/share/zoneinfo/leap-seconds.list
              [$iface_timeTx1]
              ts2phc.extts_polarity rising
              ts2phc.extts_correction 0
              [$iface_timeTx2]
              ts2phc.master 0
              ts2phc.extts_polarity rising
              #this is a measured value in nanoseconds to compensate for SMA cable delay
              ts2phc.extts_correction -10
              [$iface_timeTx3]
              ts2phc.master 0
              ts2phc.extts_polarity rising
              #this is a measured value in nanoseconds to compensate for SMA cable delay
              ts2phc.extts_correction -10
            ptp4lConf: |
              [$iface_timeTx1]
              masterOnly 1
              [$iface_timeTx1_1]
              masterOnly 1
              [$iface_timeTx1_2]
              masterOnly 1
              [$iface_timeTx1_3]
              masterOnly 1
              [$iface_timeTx2]
              masterOnly 1
              [$iface_timeTx2_1]
              masterOnly 1
              [$iface_timeTx2_2]
              masterOnly 1
              [$iface_timeTx2_3]
              masterOnly 1
              [$iface_timeTx3]
              masterOnly 1
              [$iface_timeTx3_1]
              masterOnly 1
              [$iface_timeTx3_2]
              masterOnly 1
              [$iface_timeTx3_3]
              masterOnly 1
              [global]
              #
              # Default Data Set
              #
              twoStepFlag 1
              priority1 128
              priority2 128
              domainNumber 24
              #utc_offset 37
              clockClass 6
              clockAccuracy 0x27
              offsetScaledLogVariance 0xFFFF
              free_running 0
              freq_est_interval 1
              dscp_event 0
              dscp_general 0
              dataset_comparison G.8275.x
              G.8275.defaultDS.localPriority 128
              #
              # Port Data Set
              #
              logAnnounceInterval -3
              logSyncInterval -4
              logMinDelayReqInterval -4
              logMinPdelayReqInterval 0
              announceReceiptTimeout 3
              syncReceiptTimeout 0
              delayAsymmetry 0
              fault_reset_interval -4
              neighborPropDelayThresh 20000000
              masterOnly 0
              G.8275.portDS.localPriority 128
              #
              # Run time options
              #
              assume_two_step 0
              logging_level 6
              path_trace_enabled 0
              follow_up_info 0
              hybrid_e2e 0
              inhibit_multicast_service 0
              net_sync_monitor 0
              tc_spanning_tree 0
              tx_timestamp_timeout 50
              unicast_listen 0
              unicast_master_table 0
              unicast_req_duration 3600
              use_syslog 1
              verbose 0
              summary_interval -4
              kernel_leap 1
              check_fup_sync 0
              clock_class_threshold 7
              #
              # Servo Options
              #
              pi_proportional_const 0.0
              pi_integral_const 0.0
              pi_proportional_scale 0.0
              pi_proportional_exponent -0.3
              pi_proportional_norm_max 0.7
              pi_integral_scale 0.0
              pi_integral_exponent 0.4
              pi_integral_norm_max 0.3
              step_threshold 2.0
              first_step_threshold 0.00002
              clock_servo pi
              sanity_freq_limit 200000000
              ntpshm_segment 0
              #
              # Transport options
              #
              transportSpecific 0x0
              ptp_dst_mac 01:1B:19:00:00:00
              p2p_dst_mac 01:80:C2:00:00:0E
              udp_ttl 1
              udp6_scope 0x0E
              uds_address /var/run/ptp4l
              #
              # Default interface options
              #
              clock_type BC
              network_transport L2
              delay_mechanism E2E
              time_stamping hardware
              tsproc_mode filter
              delay_filter moving_median
              delay_filter_length 10
              egressLatency 0
              ingressLatency 0
              boundary_clock_jbod 1
              #
              # Clock description
              #
              productDescription ;;
              revisionData ;;
              manufacturerIdentity 00:00:00
              userDescription ;
              timeSource 0x20
            ptpClockThreshold:
              holdOverTimeout: 5
              maxOffsetThreshold: 1500
              minOffsetThreshold: -1500
          recommend:
          - profile: grandmaster
            priority: 4
            match:
            - nodeLabel: node-role.kubernetes.io/$mcp
        ```

        > [!NOTE]
        > Set the value for `ts2phc.nmea_serialport` to `/dev/gnss0`.

    2.  Create the CR by running the following command:

        ``` terminal
        $ oc create -f three-nic-grandmaster-clock-ptp-config.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                          READY   STATUS    RESTARTS   AGE     IP             NODE
        linuxptp-daemon-74m3q         3/3     Running   3          4d15h   10.16.230.7    compute-1.example.com
        ptp-operator-5f4f48d7c-x6zkn  1/1     Running   1          4d15h   10.128.1.145   compute-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Run the following command, and examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile:

        ``` terminal
        $ oc logs linuxptp-daemon-74m3q -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        ts2phc[2527.586]: [ts2phc.0.config:7] adding tstamp 1742826342.000000000 to clock /dev/ptp11
        ts2phc[2527.586]: [ts2phc.0.config:7] adding tstamp 1742826342.000000000 to clock /dev/ptp7
        ts2phc[2527.586]: [ts2phc.0.config:7] adding tstamp 1742826342.000000000 to clock /dev/ptp14
        ts2phc[2527.586]: [ts2phc.0.config:7] nmea delay: 56308811 ns
        ts2phc[2527.586]: [ts2phc.0.config:6] /dev/ptp14 offset          0 s2 freq      +0
        ts2phc[2527.587]: [ts2phc.0.config:6] /dev/ptp7 offset          0 s2 freq      +0
        ts2phc[2527.587]: [ts2phc.0.config:6] /dev/ptp11 offset          0 s2 freq      -0
        I0324 14:25:05.000439  106907 stats.go:61] state updated for ts2phc =s2
        I0324 14:25:05.000504  106907 event.go:419] dpll State s2, gnss State s2, tsphc state s2, gm state s2,
        I0324 14:25:05.000906  106907 stats.go:61] state updated for ts2phc =s2
        I0324 14:25:05.001059  106907 stats.go:61] state updated for ts2phc =s2
        ts2phc[1742826305]:[ts2phc.0.config] ens4f0 nmea_status 1 offset 0 s2
        GM[1742826305]:[ts2phc.0.config] ens4f0 T-GM-STATUS s2
        ```

        </div>

        where:

        `adding tstamp <timestamp> to clock /dev/ptp<N>`
        Indicates `ts2phc` is actively synchronizing the PTP hardware clock (PHC) by applying a specific timestamp.

        `/dev/ptp<N> offset 0 s2 freq +0`
        Displays the estimated offset between the PTP device and the reference; an offset of 0 and state `s2` signifies full synchronization.

        `T-GM-STATUS s2`
        Confirms the Telecom Grandmaster (T-GM) is in a locked state (`s2`), providing a stable time reference for the network.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring the PTP fast event notifications publisher](ptp-cloud-events-consumer-dev-reference-v2.md#cnf-configuring-the-ptp-fast-event-publisher-v2_ptp-consumer)

</div>

# Grandmaster clock PtpConfig configuration reference

The following reference information describes the configuration options for the `PtpConfig` custom resource (CR) that configures the `linuxptp` services (`ptp4l`, `phc2sys`, `ts2phc`) as a grandmaster clock.

<table>
<caption>PtpConfig configuration options for PTP Grandmaster clock</caption>
<colgroup>
<col style="width: 25%" />
<col style="width: 75%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">PtpConfig CR field</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>plugins</code></p></td>
<td style="text-align: left;"><p>Specify an array of <code>.exec.cmdline</code> options that configure the NIC for grandmaster clock operation. Grandmaster clock configuration requires certain PTP pins to be disabled.</p>
<p>The plugin mechanism allows the PTP Operator to do automated hardware configuration. For the Intel Westport Channel NIC or the Intel Logan Beach NIC, when the <code>enableDefaultConfig</code> field is set to <code>true</code>, the PTP Operator runs a hard-coded script to do the required configuration for the NIC.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ptp4lOpts</code></p></td>
<td style="text-align: left;"><p>Specify system configuration options for the <code>ptp4l</code> service. The options should not include the network interface name <code>-i &lt;interface&gt;</code> and service config file <code>-f /etc/ptp4l.conf</code> because the network interface name and the service config file are automatically appended.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ptp4lConf</code></p></td>
<td style="text-align: left;"><p>Specify the required configuration to start <code>ptp4l</code> as a grandmaster clock. For example, the <code>ens2f1</code> interface synchronizes downstream connected devices. For grandmaster clocks, set <code>clockClass</code> to <code>6</code> and set <code>clockAccuracy</code> to <code>0x27</code>. Set <code>timeSource</code> to <code>0x20</code> for when receiving the timing signal from a Global navigation satellite system (GNSS).</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>tx_timestamp_timeout</code></p></td>
<td style="text-align: left;"><p>Specify the maximum amount of time to wait for the transmit (TX) timestamp from the sender before discarding the data.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>boundary_clock_jbod</code></p></td>
<td style="text-align: left;"><p>Specify the JBOD boundary clock time delay value. This value is used to correct the time values that are passed between the network time devices.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>phc2sysOpts</code></p></td>
<td style="text-align: left;"><p>Specify system config options for the <code>phc2sys</code> service. If this field is empty the PTP Operator does not start the <code>phc2sys</code> service.</p>
<div class="note">
<div class="title">
&#10;</div>
<p>Ensure that the network interface listed here is configured as grandmaster and is referenced as required in the <code>ts2phcConf</code> and <code>ptp4lConf</code> fields.</p>
</div></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ptpSchedulingPolicy</code></p></td>
<td style="text-align: left;"><p>Configure the scheduling policy for <code>ptp4l</code> and <code>phc2sys</code> processes. Default value is <code>SCHED_OTHER</code>. Use <code>SCHED_FIFO</code> on systems that support FIFO scheduling.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ptpSchedulingPriority</code></p></td>
<td style="text-align: left;"><p>Set an integer value from 1-65 to configure FIFO priority for <code>ptp4l</code> and <code>phc2sys</code> processes when <code>ptpSchedulingPolicy</code> is set to <code>SCHED_FIFO</code>. The <code>ptpSchedulingPriority</code> field is not used when <code>ptpSchedulingPolicy</code> is set to <code>SCHED_OTHER</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ptpClockThreshold</code></p></td>
<td style="text-align: left;"><p>Optional. If <code>ptpClockThreshold</code> stanza is not present, default values are used for <code>ptpClockThreshold</code> fields. Stanza shows default <code>ptpClockThreshold</code> values. <code>ptpClockThreshold</code> values configure how long after the PTP master clock is disconnected before PTP events are triggered. <code>holdOverTimeout</code> is the time value in seconds before the PTP clock event state changes to <code>FREERUN</code> when the PTP master clock is disconnected. The <code>maxOffsetThreshold</code> and <code>minOffsetThreshold</code> settings configure offset values in nanoseconds that compare against the values for <code>CLOCK_REALTIME</code> (<code>phc2sys</code>) or master offset (<code>ptp4l</code>). When the <code>ptp4l</code> or <code>phc2sys</code> offset value is outside this range, the PTP clock state is set to <code>FREERUN</code>. When the offset value is within this range, the PTP clock state is set to <code>LOCKED</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ts2phcConf</code></p></td>
<td style="text-align: left;"><p>Sets the configuration for the <code>ts2phc</code> command.</p>
<p><code>leapfile</code> is the default path to the current leap seconds definition file in the PTP Operator container image.</p>
<p><code>ts2phc.nmea_serialport</code> is the serial port device that is connected to the NMEA GPS clock source. When configured, the GNSS receiver is accessible on <code>/dev/gnss&lt;id&gt;</code>. If the host has multiple GNSS receivers, you can find the correct device by enumerating either of the following devices:</p>
<ul>
<li><p><code>/sys/class/net/&lt;eth_port&gt;/device/gnss/</code></p></li>
<li><p><code>/sys/class/gnss/gnss&lt;id&gt;/device/</code></p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>ts2phcOpts</code></p></td>
<td style="text-align: left;"><p>Set options for the <code>ts2phc</code> command.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>recommend</code></p></td>
<td style="text-align: left;"><p>Specify an array of one or more <code>recommend</code> objects that define rules on how the <code>profile</code> should be applied to nodes.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>.recommend.profile</code></p></td>
<td style="text-align: left;"><p>Specify the <code>.recommend.profile</code> object name that is defined in the <code>profile</code> section.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>.recommend.priority</code></p></td>
<td style="text-align: left;"><p>Specify the <code>priority</code> with an integer value between <code>0</code> and <code>99</code>. A larger number gets lower priority, so a priority of <code>99</code> is lower than a priority of <code>10</code>. If a node can be matched with multiple profiles according to rules defined in the <code>match</code> field, the profile with the higher priority is applied to that node.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>.recommend.match</code></p></td>
<td style="text-align: left;"><p>Specify <code>.recommend.match</code> rules with <code>nodeLabel</code> or <code>nodeName</code> values.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>.recommend.match.nodeLabel</code></p></td>
<td style="text-align: left;"><p>Set <code>nodeLabel</code> with the <code>key</code> of the <code>node.Labels</code> field from the node object by using the <code>oc get nodes --show-labels</code> command. For example, <code>node-role.kubernetes.io/worker</code>.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>.recommend.match.nodeName</code></p></td>
<td style="text-align: left;"><p>Set <code>nodeName</code> with the value of the <code>node.Name</code> field from the node object by using the <code>oc get nodes</code> command. For example, <code>compute-1.example.com</code>.</p></td>
</tr>
</tbody>
</table>

## Grandmaster clock class sync state reference

The following table describes the PTP grandmaster clock (T-GM) `gm.ClockClass` states.

Clock class states categorize T-GM clocks based on their accuracy and stability with regard to the Primary Reference Time Clock (PRTC) or other timing source.

Holdover specification is the amount of time a PTP clock can maintain synchronization without receiving updates from the primary time source.

| Clock class state | Description |
|----|----|
| `gm.ClockClass 6` | T-GM clock is connected to a PRTC in `LOCKED` mode. For example, the PRTC is traceable to a GNSS time source. |
| `gm.ClockClass 7` | T-GM clock is in `HOLDOVER` mode, and within holdover specification. The clock source might not be traceable to a category 1 frequency source. |
| `gm.ClockClass 248` | T-GM clock is in `FREERUN` mode. |

T-GM clock class states

For more information, see ["Phase/time traceability information", ITU-T G.8275.1/Y.1369.1 Recommendations](https://www.itu.int/rec/T-REC-G.8275.1-202211-I/en).

## Intel E810 NIC hardware configuration reference

Use this information to understand how to use the [Intel E810 hardware plugin](https://github.com/openshift/linuxptp-daemon/blob/release-4.16/addons/intel/e810.go) to configure the E810 network interface as PTP grandmaster clock.

Hardware pin configuration determines how the network interface interacts with other components and devices in the system. The Intel E810 NIC has four connectors for external 1PPS signals: `SMA1`, `SMA2`, `U.FL1`, and `U.FL2`.

| Hardware pin | Recommended setting | Description |
|----|----|----|
| `U.FL1` | `0 1` | Disables the `U.FL1` connector input. The `U.FL1` connector is output-only. |
| `U.FL2` | `0 2` | Disables the `U.FL2` connector output. The `U.FL2` connector is input-only. |
| `SMA1` | `0 1` | Disables the `SMA1` connector input. The `SMA1` connector is bidirectional. |
| `SMA2` | `0 2` | Disables the `SMA2` connector output. The `SMA2` connector is bidirectional. |

Intel E810 NIC hardware connectors configuration

You can set the pin configuration on the Intel E810 NIC by using the `spec.profile.plugins.e810.pins` parameters as shown in the following example:

``` yaml
pins:
      <interface_name>:
        <connector_name>: <function> <channel_number>
```

Where:

`<function>`: Specifies the role of the pin. The following values are associated with the pin role:

- `0`: Disabled

- `1`: Rx (Receive timestamping)

- `2`: Tx (Transmit timestamping)

`<channel number>`: A number associated with the physical connector. The following channel numbers are associated with the physical connectors:

- `1`: `SMA1` or `U.FL1`

- `2`: `SMA2` or `U.FL2`

Examples:

- `0 1`: Disables the pin mapped to `SMA1` or `U.FL1`.

- `1 2`: Assigns the Rx function to `SMA2` or `U.FL2`.

> [!NOTE]
> `SMA1` and `U.FL1` connectors share channel one. `SMA2` and `U.FL2` connectors share channel two.

Set `spec.profile.plugins.e810.ublxCmds` parameters to configure the GNSS clock in the `PtpConfig` custom resource (CR).

> [!IMPORTANT]
> You must configure an offset value to compensate for T-GM GPS antenna cable signal delay. To configure the optimal T-GM antenna offset value, make precise measurements of the GNSS antenna cable signal delay. Red Hat cannot assist in this measurement or provide any values for the required delay offsets.

Each of these `ublxCmds` stanzas correspond to a configuration that is applied to the host NIC by using `ubxtool` commands. For example:

``` yaml
ublxCmds:
  - args:
      - "-P"
      - "29.20"
      - "-z"
      - "CFG-HW-ANT_CFG_VOLTCTRL,1"
      - "-z"
      - "CFG-TP-ANT_CABLEDELAY,<antenna_delay_offset>"
    reportOutput: false
```

where:

`"CFG-TP-ANT_CABLEDELAY,<antenna_delay_offset>"`
Measured T-GM antenna delay offset in nanoseconds. To get the required delay offset value, you must measure the cable delay using external test equipment.

The following table describes the equivalent `ubxtool` commands:

| ubxtool command | Description |
|----|----|
| `ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1 -z CFG-TP-ANT_CABLEDELAY,<antenna_delay_offset>` | Enables antenna voltage control, allows antenna status to be reported in the `UBX-MON-RF` and `UBX-INF-NOTICE` log messages, and sets a `<antenna_delay_offset>` value in nanoseconds that offsets the GPS antenna cable signal delay. |
| `ubxtool -P 29.20 -e GPS` | Enables the antenna to receive GPS signals. |
| `ubxtool -P 29.20 -d Galileo` | Configures the antenna to receive signal from the Galileo GPS satellite. |
| `ubxtool -P 29.20 -d GLONASS` | Disables the antenna from receiving signal from the GLONASS GPS satellite. |
| `ubxtool -P 29.20 -d BeiDou` | Disables the antenna from receiving signal from the BeiDou GPS satellite. |
| `ubxtool -P 29.20 -d SBAS` | Disables the antenna from receiving signal from the SBAS GPS satellite. |
| `ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000` | Configures the GNSS receiver survey-in process to improve its initial position estimate. This can take up to 24 hours to achieve an optimal result. |
| `ubxtool -P 29.20 -p MON-HW` | Runs a single automated scan of the hardware and reports on the NIC state and configuration settings. |

Intel E810 ublxCmds configuration

## Dual E810 NIC configuration reference

Use this information to understand how to use the [Intel E810 hardware plugin](https://github.com/openshift/linuxptp-daemon/blob/release-4.14/addons/intel/e810.go) to configure a pair of E810 network interfaces as PTP grandmaster clock (T-GM).

Before you configure the dual-NIC cluster host, you must connect the two NICs with an SMA1 cable using the 1PPS faceplace connections.

When you configure a dual-NIC T-GM, you need to compensate for the 1PPS signal delay that occurs when you connect the NICs using the SMA1 connection ports. Various factors such as cable length, ambient temperature, and component and manufacturing tolerances can affect the signal delay. To compensate for the delay, you must calculate the specific value that you use to offset the signal delay.

<table style="width:90%;">
<caption>E810 dual-NIC T-GM PtpConfig CR reference</caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">PtpConfig field</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>spec.profile.plugins.e810.pins</code></p></td>
<td style="text-align: left;"><p>Configure the E810 hardware pins using the PTP Operator E810 hardware plugin.</p>
<ul>
<li><p>Pin <code>2 1</code> enables the <code>1PPS OUT</code> connection for <code>SMA1</code> on NIC one.</p></li>
<li><p>Pin <code>1 1</code> enables the <code>1PPS IN</code> connection for <code>SMA1</code> on NIC two.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.profile.ts2phcConf</code></p></td>
<td style="text-align: left;"><p>Use the <code>ts2phcConf</code> field to configure parameters for NIC one and NIC two. Set <code>ts2phc.master 0</code> for NIC two. This configures the timing source for NIC two from the 1PPS input, not GNSS. Configure the <code>ts2phc.extts_correction</code> value for NIC two to compensate for the delay that is incurred for the specific SMA cable and cable length that you use. The value that you configure depends on your specific measurements and SMA1 cable length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.profile.ptp4lConf</code></p></td>
<td style="text-align: left;"><p>Set the value of <code>boundary_clock_jbod</code> to 1 to enable support for multiple NICs.</p></td>
</tr>
</tbody>
</table>

Each value in the `spec.profile.plugins.e810.pins` list follows the `<function>` `<channel_number>` format.

Where:

`<function>`: Specifies the pin role. The following values are associated with the pin role:

- `0`: Disabled

- `1`: Receive (Rx) – for 1PPS IN

- `2`: Transmit (Tx) – for 1PPS OUT

`<channel_number>`: A number associated with the physical connector. The following channel numbers are associated with the physical connectors:

- `1`: `SMA1` or `U.FL1`

- `2`: `SMA2` or `U.FL2`

Examples:

- `2 1`: Enables `1PPS OUT` (Tx) on `SMA1`.

- `1 1`: Enables `1PPS IN` (Rx) on `SMA1`.

The PTP Operator passes these values to the Intel E810 hardware plugin and writes them to the sysfs pin configuration interface on each NIC.

## 3-card E810 NIC configuration reference

Use this information to understand how to configure 3 E810 NICs as PTP grandmaster clock (T-GM).

Before you configure the 3-card cluster host, you must connect the 3 NICs by using the 1PPS faceplate connections. The primary NIC `1PPS_out` outputs feed the other 2 NICs.

When you configure a 3-card T-GM, you need to compensate for the 1PPS signal delay that occurs when you connect the NICs by using the SMA1 connection ports. Various factors such as cable length, ambient temperature, and component and manufacturing tolerances can affect the signal delay. To compensate for the delay, you must calculate the specific value that you use to offset the signal delay.

<table style="width:90%;">
<caption>3-card E810 T-GM PtpConfig CR reference</caption>
<colgroup>
<col style="width: 29%" />
<col style="width: 60%" />
</colgroup>
<thead>
<tr>
<th style="text-align: left;">PtpConfig field</th>
<th style="text-align: left;">Description</th>
</tr>
</thead>
<tbody>
<tr>
<td style="text-align: left;"><p><code>spec.profile.plugins.e810.pins</code></p></td>
<td style="text-align: left;"><p>Configure the E810 hardware pins with the PTP Operator E810 hardware plugin.</p>
<ul>
<li><p><code>$iface_timeTx1.SMA1</code> enables the <code>1PPS OUT</code> connection for <code>SMA1</code> on NIC 1.</p></li>
<li><p><code>$iface_timeTx1.SMA2</code> enables the <code>1PPS OUT</code> connection for <code>SMA2</code> on NIC 1.</p></li>
<li><p><code>$iface_timeTx2.SMA1</code> and <code>$iface_timeTx3.SMA1</code> enables the <code>1PPS IN</code> connection for <code>SMA1</code> on NIC 2 and NIC 3.</p></li>
<li><p><code>$iface_timeTx2.SMA2</code> and <code>$iface_timeTx3.SMA2</code> disables the <code>SMA2</code> connection on NIC 2 and NIC 3.</p></li>
</ul></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.profile.ts2phcConf</code></p></td>
<td style="text-align: left;"><p>Use the <code>ts2phcConf</code> field to configure parameters for the NICs. Set <code>ts2phc.master 0</code> for NIC 2 and NIC 3. This configures the timing source for NIC 2 and NIC 3 from the 1PPS input, not GNSS. Configure the <code>ts2phc.extts_correction</code> value for NIC 2 and NIC 3 to compensate for the delay that is incurred for the specific SMA cable and cable length that you use. The value that you configure depends on your specific measurements and SMA1 cable length.</p></td>
</tr>
<tr>
<td style="text-align: left;"><p><code>spec.profile.ptp4lConf</code></p></td>
<td style="text-align: left;"><p>Set the value of <code>boundary_clock_jbod</code> to 1 to enable support for multiple NICs.</p></td>
</tr>
</tbody>
</table>

# Holdover in a grandmaster clock with GNSS as the source

Holdover allows the grandmaster (T-GM) clock to maintain synchronization performance when the global navigation satellite system (GNSS) source is unavailable. During this period, the T-GM clock relies on its internal oscillator and holdover parameters to reduce timing disruptions.

You can define the holdover behavior by configuring the following holdover parameters in the `PTPConfig` custom resource (CR):

`MaxInSpecOffset`
Specifies the maximum allowed offset in nanoseconds. If the T-GM clock exceeds the `MaxInSpecOffset` value, it transitions to the `FREERUN` state (clock class state `gm.ClockClass 248`).

`LocalHoldoverTimeout`
Specifies the maximum duration, in seconds, for which the T-GM clock remains in the holdover state before transitioning to the `FREERUN` state.

`LocalMaxHoldoverOffSet`
Specifies the maximum offset that the T-GM clock can reach during the holdover state in nanoseconds.

If the `MaxInSpecOffset` value is less than the `LocalMaxHoldoverOffset` value, and the T-GM clock exceeds the maximum offset value, the T-GM clock transitions from the holdover state to the `FREERUN` state.

> [!IMPORTANT]
> If the `LocalMaxHoldoverOffSet` value is less than the `MaxInSpecOffset` value, the holdover timeout occurs before the clock reaches the maximum offset. To resolve this issue, set the `MaxInSpecOffset` field and the `LocalMaxHoldoverOffset` field to the same value.

For information about clock class states, see "Grandmaster clock class sync state reference" document.

The T-GM clock uses the holdover parameters `LocalMaxHoldoverOffSet` and `LocalHoldoverTimeout` to calculate the slope. Slope is the rate at which the phase offset changes over time. It is measured in nanoseconds per second, where the set value indicates how much the offset increases over a given time period.

The T-GM clock uses the slope value to predict and compensate for time drift, so reducing timing disruptions during holdover. The T-GM clock uses the following formula to calculate the slope:

- Slope = `localMaxHoldoverOffSet` / `localHoldoverTimeout`

  For example, if the `LocalHoldOverTimeout` parameter is set to 60 seconds, and the `LocalMaxHoldoverOffset` parameter is set to 3000 nanoseconds, the slope is calculated as follows:

  Slope = 3000 nanoseconds / 60 seconds = 50 nanoseconds per second

  The T-GM clock reaches the maximum offset in 60 seconds.

> [!NOTE]
> The phase offset is converted from picoseconds to nanoseconds. As a result, the calculated phase offset during holdover is expressed in nanoseconds, and the resulting slope is expressed in nanoseconds per second.

The following figure illustrates the holdover behavior in a T-GM clock with GNSS as the source:

<figure>
<img src="data:image/png;base64,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WjV98cUXGXpMAED2QYgGAAA5Vu3atfXVV1+ZfuXVg3h5eemzzz5T3rx5M+R4AIDshxANAAByLJvNpri4OHXs2FGFCxd+rGPVq1dPf/nLX7R582alpqZmWI8AgOyFEA0AAHKsVatW6fDhw3rnnXe0evVqdevWTRaL5aGO4ePjo/fee0+LFi1S//79denSJW3evDnTegYAZG2EaAAAkCMdO3ZMq1atUpcuXVS+fHmVKFFC3377rVatWqWePXvK19f3vvtXrFhRw4YN044dO/TGG2/Iw8NDfn5+atasmX7++WfFxsY+sc8CAMg6eMUVAADIcWJiYjR9+nQFBgaqcePGhm01a9bUmDFjlJycrF27dunMmTO6dOmSbty4oSJFisjPz081atTQ008/ne6xW7durb1792rJkiXq16/fE/pEAICsghANAABylOTkZE2ZMkU+Pj7q2bPnPce5ubmpQYMGatCgwUMd393dXaGhoZo4caLq1q2rqlWrZkDXAIDsgsu5AQBAjrJw4UJFR0frxRdflIeHR6bUqFy5smrWrKkFCxbIarVmSg0AQNZEiAYAADnGtm3btH37dr3wwguP/TTuB+nWrZtu3rypNWvWZGodAEDWQogGAAA5woULF7Ro0SK1atVKNWrUyPR63t7eatu2rdatW6fLly9nej0AQNZAiAYAANleQkKCpkyZonLlyqlNmzZPrG5wcLBKliyp+fPny2azPbG6AADnIUQDAIBszWazaebMmUpNTVW/fv3k4vLkTm8sFou6deum06dPa9euXU+sLgDAeQjRAAAgW1uxYoWOHz+u/v37y8vL64nXL1WqlBo3bqwlS5YoPj7+idcHADxZhGgAAJBtHTp0SKtXr1a3bt1UunRpp/Xx/PPPy83NTT/99JPTegAAPBmEaAAAkC1dvXpVc+bMUZ06dR76Xc8ZzdPTU506ddL27dt14sQJp/YCAMhchGgAAJDtJCcna8qUKcqfP7969Ojh7HYkSbVq1VKVKlW0cOFCpaSkOLsdAEAmIUQDAIBsZ/78+bp69apefPFFubu7O7sdu9DQUF29elW//vqrs1sBAGQSQjQAAMhWNm/erJ07dyosLEyFChVydjsGvr6+atmypVauXKkrV644ux0AQCYgRAMAgGzjzJkzWrx4sUJCQlSlShVnt5OuFi1aqFChQlqwYIGzWwEAZAJC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ZVk0bdpUSJIk9u3bV+rzry2iL1++LLp37y4kSVL+CwsLEx988IHymq1bt4q6des6PSchIUEZ6KZOnSpCQkKUY+Hh4eLNN98s8fu//fbbQpIkpUBMS0sT586du+HAVhGNGTNGSJIkPv7441KfW1IR/cILL4jq1as7/Zv0799fmWAuXLggOnbs6HS8RYsWYvv27UIIIdasWSMiIyOdjvft27fEguxG8SclJZX7HPwbnT17VgQHB4t69eqVWCxd69oieu/evaJVq1ZO/25RUVFi9erVymvmzp3rlBvVqlUTo0ePFna7XeTn54v+/fs7vb5evXpiyZIlJX7/hIQEUb16dZGbmyvsdrs4e/asUhCQ63Tq1ElIkiQ2bdpU6nOvLaItFot45JFHnMbg0NBQpzF47969olGjRk7/7l27dhUnT54UQggxa9YsERYW5jQHvPjii0KW5VLjsdvtIjY2Vtx9990lfmBTkcmyLBo3biwkSRIHDhwo9fnXFtGXLl0S3bp1Kzb/fvTRR8prNm/eXGz+feSRR5Rz/dZbbxWbfydPnlzmn+H7778XkiSJL7/80unxGTNmCEmSxDvvvCOEEMWKaCGE6Nq1q6hXr544c+aMcj7GjRsngoODxc6dO8scA1VMV3IrISGhTM+/tohesmSJqFevnlPut2zZUhw7dkyIwrFn9OjRTsdr164t/ve//wlR+OFS27ZtnY63adNG7Nmzp9j3zs/PFxEREaJr167K16dOnSrTPE3kKbic+xrp6ek4e/YswsLC0KRJk5t+fUBAAJo1a4a+ffuiUaNGuHjxIiZNmoR33nkH3bt3R7169fDyyy8jMDAQP/74I3x8fLBt2zYcOHAAkiTh6NGj+OCDD9C/f39MnDgR6enp+P777697v15ycjIAwGAwoGfPnti1axcAICwsDK+++ip69+59i2fkzli42wSLVSDM3xs9Ghhv+vX79u0DAHTt2rVc379JkyYIDQ1FmzZt4OXlhRkzZuCXX37BggULMGTIEHz88cc4cuQIli1bhujoaOzfvx/ffvst6tevDwCYMGECatasic8//xwovGfp1KlTqFKl9KYpycnJSExMRGxsLFq2bFnq881WgUW7TQCABqF6tI3wLdfPXBHs378fQgjcd9998PO7+QZr9erVQ0xMDCZMmICIiAgcOnQIEydOxNixY3H48GFkZ2fj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" alt="Holdover in a T-GM clock with GNSS as the source" />
<figcaption aria-hidden="true">Holdover in a T-GM clock with GNSS as the source</figcaption>
</figure>

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6NUNCQ0YxRUFERUUxMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6NUNCQ0YxRUJERUUxMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDo1Q0JDRjFFOERFRTExMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDo1Q0JDRjFFOURFRTExMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PgvcXgoAAAO7SURBVHjavJfLK7xRGMdnjnGdkmsWYqUIJXciuQsbOwplYWGvUAopKzZyWWBDkstCKLnkUlbyH7gl11zK9ec6+H3MOzEm3jljpnk2M7095/2+z/N8z/d8j/b9/V1jLW5vb9fX15eXl9fW1ra3tw0Gg1arfXt78/Pzi4+Pz83NTUlJiYqKsvoerTrY7u7u+Pj4wsICGA8PD2D8mBYUFARqWVlZVlaWu7u7zWBnZ2ednZ1DQ0MXFxeurq684jckglofHx91Ol1SUlJtbW1hYaENYJOTk83NzZubm15eXrxCIxe8iupdXFwqKira2tp8fHysg7W3t5PKSDw8PDS2Bwvv7u4osa+vLyIiQg2MggDz9PTkAzV2BHhhYWEjIyPR0dE/gwHT1NSk1+uFEBr7ggGDFx4ePjU1FRISYgk2MzNDr5mQnTWZ411fXxcVFY2NjUExnpgqOD09bWxsBNhRSApfvL29Z2dnu7u7lScmsK6uLrj3N0aoB+MHbH9/3wS2t7c3ODgIyyXJBr//GYO9pbL5lKCBR0dH/f39JjA04vz83Op+UjjNn8zMzIGBgcXFxY6ODoBlihsdHWVSOmY4Nzfn5uZmFQkRKS0traysTE5OVgqi7WiHVTCKOzw8XFpa0m1sbKB7KoKmxPPzc2RkZE9Pj/lDmTaaqCHEysqKQMtVFNY8FKLyZWi/rTRhRltbW4KVMkhkX11d1dTUpKenDw8P/wHsY2YASmYfHByQ/PLywsBtBaMrl5eX4vX1VXIBfbfpELAIgITkhB2iXgJOOwcM9RL+/v5OQKIkRiDi4uKcAMbAAgMDBd7ICWBwODg4WKSlpeGNZFTHzsoSEhIEhyk/CI/8nD/ZjzbK2E5yyCwoKNDBSOR1YmJC/nyan5/f2dnhPyIus8GRw4yMDMjxYQsoi8MbRZZZyccxgKenJ0UXWKJenOLvcAbFxcVC6UZDQwMCIbPnlDbqjSHTRs7YnJwcevhlC/Ly8srLy/H0Diehr69va2urMmbx2RweJSYmchY7SsDoE6cgfjcmJuab4SECAgI47HGWDsED6f7+vq6urqqq6kvKzTNwy3hYNsPNzY2d3YMU9fX1+Otv54ZFHm6ZW0V+fj54rPmD2tIYZBD7ZoH06y2GXpON48CFQW7Fz8pcYeh/dnZ2S0tLbGysbZdBboK9vb3T09N4I96iM4a5ZWatwRioEZYpNTW1urq6pKTkt6uC1upGOT4+Xl1dxRthmU9OTlANZYkiQmh5aGgodXAB/FA/1RvJfwEGAEOvDVF4OcCIAAAAAElFTkSuQmCC) The GNSS signal is lost, causing the T-GM clock to enter the `HOLDOVER` mode. The T-GM clock maintains time accuracy by using its internal clock.

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MzYwQjc3OUJERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MzYwQjc3OUNERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoyN0IxQkJCRURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDozNjBCNzc5QURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Pjt4Q14AAASGSURBVHjarJdZKPVdFMad45jlNebCkAshY2ZSQoZwQ1EylAvKhTtFUki54oJMZbhAxkIoSZlyQyiSFMIrQ4bMn3n4fvz1fvjYjpd1w3+fvfez117PetbasoeHB5XP7PT0dGJiYmhoaGxsbHl5+fb2ViaT3d/fGxoauru7BwcH+/j4ODg4fLqPTAy2srLS3t4+MDAAxsXFBRjvTjM1NQU1Li4uMDBQQ0Pjy2C7u7ulpaUNDQ37+/tqamps8REShq+Xl5cKhcLLyysjIyM8PPwLYF1dXXl5eYuLi9ra2myhopyxFd6rqqomJiYWFhbq6+t/DlZUVMRUQqKpqanydWPh2dkZLlZXV9vZ2YnAcAgwLS0tDqjyDQPP2tq6ubnZ0dHxfTBgcnNzdXR05HK5yveMAINna2vb3d1tYWHxFqy3t5e7JkLf9Okl3vHxcURERFtbGxRj5NmDnZ2dnJwcgH8KSeKLnp5eX19feXm5NPIMVlZWBvf+jhFiI/yAra+vP4Otra3V19fDcmWY/c9rI8PEq7jAzc3Nmpoa/n/MITRib28PlwVrrq+vAfP19UUjoDXn3draGh0dJdIHBwd8CpSIX1tbW9PT02VHR0fR0dFTU1OCO7y7u0OQsrOz4+Pj3wR1bm4uNTV1YWFBoFKSutbV1cknJyfRPcFUkhSK1tbWJiUlSUgo2fb2tvSrk5MTqsZBmSYAI5eGh4flaLlAYaV56F5jY6MUXfwICgoKCAjgWogZg56enkBeXV0JwDju0tKSgqohQJJMXV29paUFLkxPT8/PzxMDBquqqvDV29ub0xBvsWeAkV2PgMqkJ3gEmTW/fv1iBJ9cXV2trKwkZYLZYr3m/g8PDxUE/1PP/pBKAj4/Pzc3Nyd7YA0jTU1NyuToI5CJicmXFAifUFgApNIM+6EoUVemEsnFd/0uElouISGyhI1BZZBIRLmRkZHyKi4h2dvbM9LZ2ZmSkoLUEk5lihwKJXdzc1MSydnZGf0G6ebmpqSkBJ8QBCiKZ4yIA0/AiJeC3mhwcFAMRg55eHgQJ3jB5+rqKoxITk6WCgcws7OzMzMzgsvkNGZmZgo/Pz9IhVYKpiKMaWlpEhJmY2NTWVn5ckJxcfH4+Liurq7AM44rp5jyB40QO/ed6gM1WB4WFvZYqfv7+2NiYgQlhnNxJimr3rXfT/ZR4SUv/f39e3p6HsFwi+KNIktp+y5BmCMoXepP9m6VkaogzIqMjHzuQeh5Y2NjCfj3W53/t1khISEdHR1w4nlrvhMSEqg6P4sECQ0MDAoKCiT2yf9cFEMUCw6ipFQqk8jQmH7XxcXlVcODGRsbUyHRiB/BAwleZGZmko7/aePLGXTLqBHEOzk5+ebtQYqsrCz661dC/GYe3TKvitDQUPBY8xcpxcWQRRSgN0gfvmK4a2ZXVFSgLOSDJEvKNHrcP01Dfn4+pfVrj0FegsgSybixscEuiid7mbmsvX0ysp6WiUaPOhAVFfVR/sg+febSH46MjNAbIb40VdQUaYkkQmi5paUlfvAAfFQ/YZr+K8AAzKChL/a5vucAAAAASUVORK5CYII=) The GNSS signal is restored and the T-GM clock re-enters the `LOCKED` mode. When the GNSS signal is restored, the T-GM clock re-enters the `LOCKED` mode only after all dependent components in the synchronization chain, such as `ts2phc` offset, digital phase-locked loop (DPLL) phase offset, and GNSS offset, reach a stable `LOCKED` mode.

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MjdCMUJCQkNERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MjdCMUJCQkRERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoyN0IxQkJCQURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoyN0IxQkJCQkRFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PqtGIf0AAATpSURBVHjarJdJLJ1vFMZd91I0ZipCiaBEJWIeI2qsKUotJCwsmoiwk5akianRDRvjoiUNCynRiDEqMUWlhL1QQ2NqDDFU/6ih/r/bTxSp91LOxvV97/s+7znnOc85n+z4+FhNlW1vb4+MjPT29g4ODk5NTR0eHspksl+/fhkZGbm7u4eGhvr4+Dx8+FDlOTIx2MzMTGNjY3d3Nxi7u7tg/HWZmZkZqElJSY8ePbpz5861wVZWVkpLS+vq6tbW1jQ0NDjiMiQMX/f29hQKhZeXV1ZWVmRk5DXAmpub8/LyJicndXR0OELtasZReC+Xy1NSUoqKigwMDFSDFRcXs5SUaGlpqV3f2Pjjxw9cfPPmjaOjowgMhwDT1tbmgmo3MPDs7Ozq6+udnZ3/DgZMbm7u3bt31dXV1W5mJBg8BweHlpaW+/fvXwRra2sj1mTohj6dxdva2oqKimpoaIBiPDnxYHl5+eXLlwDfFpLEFz09vc7OzoqKCunJCVh5eTnc+zdGiI30AzY3N3cC9vXr19raWliukmY7Ozv/nbejoyPxLgK4uLj49u1bfitrCI1YXV3FZcEeYCBObGxsSEgIaYdBaEp/f39XVxevCIlAiXDu/fv3mZmZss3Nzfj4+LGxMUEMDw4O/Pz8IKq3t/eFV58/f87IyEDVNDU1xepaU1Mj56bv3r3jXpep0c+fP11dXTs6OqysrKQnS0tL6BP35Te0fvDgQVNTk+y3CfRMV1dXbmlpiaIL1hGxjY0NtBFpHx4eTktLQzPJMe56enrylhM+fvy4sLAgEDacwXVZQEDAxMSEOMmwAHbExcV9+vQJtwDe39/HM25pa2vLgoSEBPBIquCEe/fuKb58+aKSvhQfHnz48IHbcSKMYDP5MzY2lqI6Pj4uzhknEB4F2wQxPCsHuIJDNjY2JSUlOOfk5KSvrz89Pf38+XPIrbJGAVJcBensBiokKChI+nd+fr6goACdA/Uq15Vz36vjkWfCCP0kOkCNx48fgzQwMECcxecoCc9OoqnyUhQA9CN6RJ+cwRcqob293d7engVwhwlFKobL1EfZTNzc3FQiUZIse/XqFYzit7QZ+NM11tbWYt3irampqYLZqKenR7COTh8TE0Pbpc0/ffoUFWcqIXP0DsktFlB/UhMRaJCFhYXC39+f2Qg6CUqSfOCK5EF6evqFt69fv4b6ghhKnnl4eKijqvxhNrpsHZxGq5jRKisr0UCER3q+vr4+NDSUnJxcVlYm5j3UYEFERISyU6PciYmJ4haz/9vMzc1xDvoB+e3bt9nZWTKnks8QKjAwsLW1VQmGWyRgdHRUHApJT4k+IeV0wk6eVJaNNN8xGURHR6tLgcrJyTlNjMAA4EKQmDAohfUKBUqDpbEQwz9jQVhYGNGXaH2LRhgMDQ0LCwsl9qmfFhOPaBnMX9cSMPEYQZqZd11cXM4NPJiJiUl1dTWT5a3gSQPLixcvUlNT/5TQ2RVMy8ywFMP3799vGD1IkZ2dzXx9rl4vrGNa5qsiPDwcPPb8w6xIYKAP49sFpEu/Yog1q6lilAX6iaXoLMWJf3BwcH5+PmPL9T4G0YuqqiqKkYYiFdaF4Zy9h78NNaIh+Pr6Pnv27MmTJ5d9KshUfubS9ZkP+/r6GJlRDcZ3aYskQmg5vQY/+ABUqp/wi+R/AQYAqG28UENgFyQAAAAASUVORK5CYII=) The GNSS signal is lost again, and the T-GM clock re-enters the `HOLDOVER` mode. The time error begins to increase.

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MjdCMUJCQjhERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MjdCMUJCQjlERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoyN0IxQkJCNkRFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoyN0IxQkJCN0RFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PiJoNJoAAARoSURBVHjarJdJKP1tFMfdn2uWEEmGIiGUjBGReVzYUSwshIUdoRRSbFiQKcMGJcNCKOHNUIokG7IwJhkyRIbXPLwffve9L/d1f/feP2dx/X6P53m+v3Oe7/me88je3t70NNn19fXi4uL09PTc3NzW1tbz87NMJnt9fbW2tg4ICIiNjQ0JCfH29ta4j0wabGdnZ2BgYHJyEoy7uzswvp1mZ2cHakZGRlRUlJGRkc5gJycnDQ0N3d3dZ2dnBgYGbKEOCcPX+/t7uVweHBxcWFiYlJSkA9jQ0FBFRcXGxoapqSlb6GlnbIX3+vr6WVlZ1dXVlpaWmsFqa2uZypEYGxvr6W4svLm5wcX29nZPT08pMBwCzMTEhA/U+4GB5+bm1tvb6+Pj8z0YMOXl5WZmZoIg6P3MOGDwPDw8hoeHnZycVMFGR0eJNSf0Q58+411eXiYnJ/f390MxRhQeHB8fl5WVAfxbSCJfLCwsxsbGmpqaxBEFWGNjI9z7M0ZIG8cP2N7engJsd3e3q6sLlmsfn6enp7//NTJMIgUJ4MHBQUdHhwIMjTg9PdU+nwBAnEZGRv76sLq6OtJL2rm+vj5OSs4Zjo+PGxoaaon08PBgb29PDnl5eYkjBB8FkViCc/v7+1NTU8LS0hK6JyFoKrIEgzhgJRImHUYFNQRhZmZGQMslFFaFXbhVVVWVmJjI68rKivY04Yw2NzcFqoY2SGKhycvLKygo4Lmnp6etrU0nMM5MAFAb+oEUHx9fU1PD6+rqKtKuTSFUGsG/uLgQXl5eNE69vb2Ffi0tLXAB3uIfv1oes9IAEjTGEFJYWVm1trY6Ojoid/n5+QsLCyIvlLvwNWL5lg6PPkkgMentw+rr6xMSEnhdXl5eX18PDw/38/OLjIwUFZ0EB4lf6q2EgrOPzN3dnWhK+E4RmJ2ddXV1lQ5AUVERcTY3N1dX5N6Lib+/v0bG/1yd+WhbW1s5vRG5LZGMxCc3N1dFOUnN1NRUMQ3W1tYgJwLIiajbh00cHBzkYWFh9EZM/VYbxZZtfn6eXxV+uri4iM/n5+cTExOQCFlSlw94FhgYKFBM+aOkljolNftq4oj4X/GVb1WHxDg5A8XkfHt6evrg4KCuVQpvtre3eUbKJQIoxjwiIgJyvLcFuEXxRpGl1/y/pCGVojqwUMItwOgMUlJSBLFGlJaWwgWVg5GmKHETQ8pyCemi+MXExIhpqsjBuLi4zMxMBPB3ewK8hzgUCpF9gjIsDAUFBSFIWhYBbbrVx8dH+l1fX98vDQ9mY2PT2dlJZ/kreCCRHsXFxdnZ2f9l7ecZdMv0sCTD1dXVD6MHKUpKSuivv0iEyjy0lVsFpQs81vxBr0hgkBvaNxUktbcYYs3s5uZmUYTEflabKwzxj46OrqyspCzodhnkJoiQ07LRG7GL/MM+izJrnz8MNaKWhoaG5uTkpKWlqSs0Mo3V/fDwkBJDb0TLfHR0hF6IS0QRQsudnZ3xgwvgu/pJ3kj+EWAADf+G+FiHwc4AAAAASUVORK5CYII=) The time error exceeds the `MaxInSpecOffset` threshold due to prolonged loss of traceability.

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MjdCMUJCQjRERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MjdCMUJCQjVERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoxNTNCNzkyOURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoxNTNCNzkyQURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/PrRS/SAAAASsSURBVHjarJdZKKV/GMed41jHvl4MihShZI2ULMNkq/8FpbiQ3Ch3hFJIKVkuZMsSjSTmhjHIkqVc/JM7F8qSLctYMg0GY/1/znl15oy/8zvH8Fy8nfO+v9/7/T3L9/s8r+zh4cFAl52dnc3Pz09PT8/Nza2trd3e3spksvv7ezs7u6CgoA8fPoSFhfn6+up8j0wMtr6+/vnz54mJCTAuLy/BeHaZs7MzqOnp6dHR0SYmJi8GOzw8rK+v7+7uPj4+NjIy4hXakDB8vbq6UigUoaGh+fn5CQkJLwAbGBgoKytbWVkxNzfnFQb6Ga/Ce0NDw8zMzMrKShsbG91gNTU1LCUlpqamBi83Np6fn+NiW1ubt7e3CAyHADMzM+OABq8w8Dw9PXt7e/38/J4HA6a0tPTdu3dyudzgdUaCwfPy8vry5Yurq+tTsK9fvxJrMvRKnzTxfvz4kZiY2N/fT4lx59GDg4ODkpISgN8KSaoXKyur0dHRxsZG6c4jWENDA7X3dxUhNtIP2Pb29iPY5ubmp0+fqHJxjf3UYhcXFwJlIIC7u7vt7e38VnIIjTg6OsJlbRuur68prdraWmNj4/8/hfUFBQVctTES5/r6+vLy8hTkcGxs7Nm3aLpFiUZFRT37FCKjL2LndnZ2pqamFAsLC+ieQNCkVHPqm5sbtn379u3k5ESTG0SFRwIxU2ZLLp+ZmVGg5QKFVXtmbW0tlW9dXV1nZ6c6wWzkKMRZrGo8XV1dVdA1xEhqPOkHFYFnXNUhIgU6CQMY7FIC6lPBalV1cXHJzc2lgQGwtLQ0OTnJlRIQn5jF379/V9zd3enjmaOjo/SjqKhI0w8aSnV1dUtLC/6J3wOQXB8k0ru/v09xS137X5Wdnp7yl2ZdVVUVGxtLP9OpXjJ7e3t9ZJecoac+Pj6EnbhRFAEBAa2trdI0gPplZ2dDD3FJG/IKnYeSDK4sLi7iGRkiaMvLy6RdasqICBokIKvEVHlgYKA+SBwoJycnJSWFCeBcZVBTvXdra0u8nYSRdQWzEdwWL/316xfdB7Fmz8jICAnjTkxMDNjSgsHBQXHuYf379+8VERERzEZopTZWEgHilpycLFfZPyrTXMAhhoeHWSP2LDg4WDn+kVsybGFhIYg4QcvKykpLS/Pw8JAkm2pE57q6unp6ejiEgNeUBsEfHx9Xig1CnJqaKm4xHA1Vs7S0dHd3d3Jykma9jY0N6oXMi2NI+URGRg4NDSnBSD7NG0UWh0JykegDLIkCWqWTNtJ8R+SSkpKUS2nQxcXFbFMLoIDdxNNcZfzQh6CoKJT/+PHj77EgLi4uIyODmLztTEAYbG1tKyoqpOqTq7WEWyEhIRBIHwHTc1ql9TDv+vv7/zHwYA4ODh0dHbT/N8EDibooLCykhn9nQXMF0zIzLJOlJLKviR5FQX9gvv4j5U/WMS3zVREfHw8ee/5iViQwlA/j2xMkrV8xxJrVTU1NKAt8kAYCfUqc+CNj5eXl9ISXfQzyJdjc3AwZ0XveolCZplJI0oDBPJgQHh6OWCNm2igh0/mZu7e3Nzs7y2zEyEwLZfSTtnCFoGi5m5sbftBrUD8x8/4TYAC4V7bro2fEGgAAAABJRU5ErkJggg==) The GNSS signal is restored, and the T-GM clock resumes synchronization. The time error starts to decrease.

![20](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACQAAAAkCAIAAABuYg/PAAAAGXRFWHRTb2Z0d2FyZQBBZG9iZSBJbWFnZVJlYWR5ccllPAAAAyhpVFh0WE1MOmNvbS5hZG9iZS54bXAAAAAAADw/eHBhY2tldCBiZWdpbj0i77u/IiBpZD0iVzVNME1wQ2VoaUh6cmVTek5UY3prYzlkIj8+IDx4OnhtcG1ldGEgeG1sbnM6eD0iYWRvYmU6bnM6bWV0YS8iIHg6eG1wdGs9IkFkb2JlIFhNUCBDb3JlIDUuNi1jMTQ1IDc5LjE2MzQ5OSwgMjAxOC8wOC8xMy0xNjo0MDoyMiAgICAgICAgIj4gPHJkZjpSREYgeG1sbnM6cmRmPSJodHRwOi8vd3d3LnczLm9yZy8xOTk5LzAyLzIyLXJkZi1zeW50YXgtbnMjIj4gPHJkZjpEZXNjcmlwdGlvbiByZGY6YWJvdXQ9IiIgeG1sbnM6eG1wPSJodHRwOi8vbnMuYWRvYmUuY29tL3hhcC8xLjAvIiB4bWxuczp4bXBNTT0iaHR0cDovL25zLmFkb2JlLmNvbS94YXAvMS4wL21tLyIgeG1sbnM6c3RSZWY9Imh0dHA6Ly9ucy5hZG9iZS5jb20veGFwLzEuMC9zVHlwZS9SZXNvdXJjZVJlZiMiIHhtcDpDcmVhdG9yVG9vbD0iQWRvYmUgUGhvdG9zaG9wIENDIDIwMTkgKE1hY2ludG9zaCkiIHhtcE1NOkluc3RhbmNlSUQ9InhtcC5paWQ6MTUzQjc5MjdERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiIHhtcE1NOkRvY3VtZW50SUQ9InhtcC5kaWQ6MTUzQjc5MjhERUUyMTFFOTkxNEQ5Mjc1OTRERjU1NjIiPiA8eG1wTU06RGVyaXZlZEZyb20gc3RSZWY6aW5zdGFuY2VJRD0ieG1wLmlpZDoxNTNCNzkyNURFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIgc3RSZWY6ZG9jdW1lbnRJRD0ieG1wLmRpZDoxNTNCNzkyNkRFRTIxMUU5OTE0RDkyNzU5NERGNTU2MiIvPiA8L3JkZjpEZXNjcmlwdGlvbj4gPC9yZGY6UkRGPiA8L3g6eG1wbWV0YT4gPD94cGFja2V0IGVuZD0iciI/Puet9qQAAATKSURBVHjarJdbKKZdFMe9r9dpSI7JCAlRlBzjhpxDaRSlHDNzhSsKIaRcSJEcLhgX40IOF0JNmsLghpDLcR6MQ87Hz2EYvp9vawbf2C9j9tXz7nft57/XWv/1X+tRXF9fa6hbR0dHo6Oj/f39w8PDc3Nzl5eXCoXi6urKxMTE09MzJCTE19fXxcVF7XsUcrCFhYX29vZPnz6BcXp6CsZvzSwsLECNj48PDAzU0dF5Ntjm5mZ1dXVzc/P29raWlhaveAyJha9nZ2cqlcrHxyc7OzsiIuIZYJ2dncXFxTMzM69eveIVGk9bvArvNTU1ExMTy8rKjIyM1INVVFRgSkp0dXU1nr84eHx8jIsNDQ3Ozs4yMBwCTE9PjwtqvGCB5+Dg0NLS4urq+nswYIqKivT19ZVKpcbLFgkGz8nJqaury9ra+iFYT08PsSZDL/TpLt7BwUFkZGRbWxsUY+fWg42NjYKCAoD/FpLgi6Gh4cePH2tra8XOLVhNTQ3c+zNGyBfpB2x5efkWbHFx8cOHD7D8KYepp3/uL4pMYk8AV1dXGxsbeb6pITRia2sLl+UwP378OD8/9/DwoGZhNldeWloaHBzs6+vjuLa2tsS51tbWzMxMxf7+fkxMzPj4uDyGXJ/XFRYWpqWlPYgBF09ISJicnJQIFera1NSkGhsbQ/ckdiLVgFEYb9++FTu4cnFx8fr1a565LvySM4taGhgYUKHlEoUVC4Po6GiBRCQpfOoEpaCMkpOTq6qqvn37Jk85FTU7O6uia8iRRD389An/ysvLRd3Mz89zX26NDsi7B2B4r6A7cEeJ3ffv321sbAiAmZnZzs4O1CAB0IQcky3uCwzPavsid1LBMblnGFhaWtIneZ6amrKzs8MzupfI1tDQUGlp6fT0NGGU4/EepRxJqLiBgYFQS1ykTkDCXX7SRMglamRrayt25OqllMdQGJ2cnIhnJBXnIEVAQAB9+cuXL2za29tTDxBHrXqpTE1N9/b25LldX1/HxtjY+PDw8N27dwQNRoyMjHAet7BhBpFHCJdumgmplt8I4n39+pWq5xmVwQl2KDIo6ujoKGx2d3fVqo+5ubmK2Qi9kYcRU5Q6NDSUn4wYZAhe0BWTkpKETW9vr9wzLmdlZaUg7nFxcZBYMmsQLlKSlZVVUlLy/387OjrS09OxkbRcqiU/P1+JCnh5eaHlcucQxsrKypSUlImJCQRF7BNeppWMjIwbWj+OJAoxPDz8plMThNjYWLUtBktoSZ65HwVOcwGMkKgdWDjl7+/f3d19A4ZbNG8UmWNPGZ4oKeEKTFE76In5DtJGRUXd+I6PeXl5HFZbc0J1sMc/bvaUkZIABAcHE8NfYwFMoyeRxr87E0BCqhM9E9dS/qQAW97e3sxfagXs6dMqAYdBbm5u9wYeFjl///49k+VfwQMJXuTk5KSmpv5KwV0LpmVmWMiGLL0wepAiNzeXNnsv3w/s0AW+KsLCwsDjzB/MigSGKmJ8e4D06FcMsca6rq5OlJHoy0+hOPEPCgpCaNzd3Z/3MciXYH19PcW4srLCW1T/rbv1KwYhFmXHyOTn50dPePPmzWNqolDbztfW1j5//syswchMr2F8F0eECKHldFT8YJhE9uRfJP8KMADiYdQcFOG/8gAAAABJRU5ErkJggg==) The time error decreases and falls back within the `MaxInSpecOffset` threshold.

# Applying unassisted holdover for boundary clocks and time slave clocks

The unassisted holdover feature enables an Intel E810-XXVDA4T NIC, configured as a PTP boundary clock (T-BC) or telecom time synchronous clock (T-TSC), to maintain time synchronization when the upstream timing source becomes unavailable.

The `ts2phc` service monitors the `ptp4l` instance bound to the timing receiver (TR) port. If, for example, the TR port stops operating as the time receiver, the upstream grandmaster clock (T-GM) deteriorates in quality or the link disconnects, the system enters holdover mode and reconfigures itself dynamically.

> [!IMPORTANT]
> Applying unassisted holdover for T-BC and T-TSC is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

- An Intel E810-XXVDA4T NIC.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure the triple port T-BC NIC. See the example below where the `PtpConfig` resource contains two profiles, one for time transmitter ports (00-tbc-tt) and one to configure all the hardware, the TR port, and `ts2phc` and `phc2sys` processes:

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: t-bc
      namespace: openshift-ptp
    spec:
      profile:
      - name: 00-tbc-tt
        ptp4lConf: |
          [ens4f0]
          masterOnly 1
          [ens8f0]
          masterOnly 1
          [ens1f0]
          masterOnly 1
          [global]
          #
          # Default Data Set
          #
          twoStepFlag 1
          slaveOnly 0
          priority1 128
          priority2 128
          domainNumber 25
          clockClass 248
          clockAccuracy 0xFE
          offsetScaledLogVariance 0xFFFF
          free_running 0
          freq_est_interval 1
          dscp_event 0
          dscp_general 0
          dataset_comparison G.8275.x
          G.8275.defaultDS.localPriority 128
          #
          # Port Data Set
          #
          logAnnounceInterval -3
          logSyncInterval -4
          logMinDelayReqInterval -4
          logMinPdelayReqInterval -4
          announceReceiptTimeout 3
          syncReceiptTimeout 0
          delayAsymmetry 0
          fault_reset_interval -4
          neighborPropDelayThresh 20000000
          masterOnly 0
          G.8275.portDS.localPriority 128
          #
          # Run time options
          #
          assume_two_step 0
          logging_level 6
          path_trace_enabled 0
          follow_up_info 0
          hybrid_e2e 0
          inhibit_multicast_service 0
          net_sync_monitor 0
          tc_spanning_tree 0
          tx_timestamp_timeout 50
          unicast_listen 0
          unicast_master_table 0
          unicast_req_duration 3600
          use_syslog 1
          verbose 0
          summary_interval 0
          kernel_leap 1
          check_fup_sync 0
          clock_class_threshold 135
          #
          # Servo Options
          #
          pi_proportional_const 0.60
          pi_integral_const 0.001
          pi_proportional_scale 0.0
          pi_proportional_exponent -0.3
          pi_proportional_norm_max 0.7
          pi_integral_scale 0.0
          pi_integral_exponent 0.4
          pi_integral_norm_max 0.3
          step_threshold 2.0
          first_step_threshold 0.00002
          max_frequency 900000000
          clock_servo pi
          sanity_freq_limit 200000000
          ntpshm_segment 0
          #
          # Transport options
          #
          transportSpecific 0x0
          ptp_dst_mac AA:BB:CC:DD:EE:FF
          p2p_dst_mac BB:CC:DD:EE:FF:GG
          udp_ttl 1
          udp6_scope 0x0E
          uds_address /var/run/ptp4l
          #
          # Default interface options
          #
          clock_type BC
          network_transport L2
          delay_mechanism E2E
          time_stamping hardware
          tsproc_mode filter
          delay_filter moving_median
          delay_filter_length 10
          egressLatency 0
          ingressLatency 0
          boundary_clock_jbod 1
          #
          # Clock description
          #
          productDescription ;;
          revisionData ;;
          manufacturerIdentity 00:00:00
          userDescription ;
          timeSource 0xA0
        ptp4lOpts: -2 --summary_interval -4
        ptpSchedulingPolicy: SCHED_FIFO
        ptpSchedulingPriority: 10
        ptpSettings:
          controllingProfile: 01-tbc-tr
          logReduce: "false"
      - name: 01-tbc-tr
        phc2sysOpts: -r -n 25 -N 8 -R 16 -u 0 -m -s ens4f1
        plugins:
          e810:
            enableDefaultConfig: false
            interconnections:
            - gnssInput: false
              id: ens4f0
              part: E810-XXVDA4T
              phaseOutputConnectors:
              - SMA1
              - SMA2
              upstreamPort: ens4f1
            - id: ens1f0
              inputConnector:
                connector: SMA1
              part: E810-XXVDA4T
            - id: ens8f0
              inputConnector:
                connector: SMA1
              part: E810-XXVDA4T
            pins:
              ens4f0:
                SMA1: 2 1
                SMA2: 2 2
                U.FL1: 0 1
                U.FL2: 0 2
              ens1f0:
                SMA1: 1 1
                SMA2: 0 2
                U.FL1: 0 1
                U.FL2: 0 2
              ens8f0:
                SMA1: 1 1
                SMA2: 0 2
                U.FL1: 0 1
                U.FL2: 0 2
            settings:
              LocalHoldoverTimeout: 14400
              LocalMaxHoldoverOffSet: 1500
              MaxInSpecOffset: 100
        ptp4lConf: |
          # The interface name is hardware-specific
          [ens4f1]
          masterOnly 0
          [global]
          #
          # Default Data Set
          #
          twoStepFlag 1
          slaveOnly 0
          priority1 128
          priority2 128
          domainNumber 25
          clockClass 248
          clockAccuracy 0xFE
          offsetScaledLogVariance 0xFFFF
          free_running 0
          freq_est_interval 1
          dscp_event 0
          dscp_general 0
          dataset_comparison G.8275.x
          G.8275.defaultDS.localPriority 128
          #
          # Port Data Set
          #
          logAnnounceInterval -3
          logSyncInterval -4
          logMinDelayReqInterval -4
          logMinPdelayReqInterval -4
          announceReceiptTimeout 3
          syncReceiptTimeout 0
          delayAsymmetry 0
          fault_reset_interval -4
          neighborPropDelayThresh 20000000
          masterOnly 0
          G.8275.portDS.localPriority 128
          #
          # Run time options
          #
          assume_two_step 0
          logging_level 6
          path_trace_enabled 0
          follow_up_info 0
          hybrid_e2e 0
          inhibit_multicast_service 0
          net_sync_monitor 0
          tc_spanning_tree 0
          tx_timestamp_timeout 50
          unicast_listen 0
          unicast_master_table 0
          unicast_req_duration 3600
          use_syslog 1
          verbose 0
          summary_interval 0
          kernel_leap 1
          check_fup_sync 0
          clock_class_threshold 135
          #
          # Servo Options
          #
          pi_proportional_const 0.60
          pi_integral_const 0.001
          pi_proportional_scale 0.0
          pi_proportional_exponent -0.3
          pi_proportional_norm_max 0.7
          pi_integral_scale 0.0
          pi_integral_exponent 0.4
          pi_integral_norm_max 0.3
          step_threshold 2.0
          first_step_threshold 0.00002
          max_frequency 900000000
          clock_servo pi
          sanity_freq_limit 200000000
          ntpshm_segment 0
          #
          # Transport options
          #
          transportSpecific 0x0
          ptp_dst_mac AA:BB:CC:DD:EE:HH
          p2p_dst_mac BB:CC:DD:EE:FF:II
          udp_ttl 1
          udp6_scope 0x0E
          uds_address /var/run/ptp4l
          #
          # Default interface options
          #
          clock_type OC
          network_transport L2
          delay_mechanism E2E
          time_stamping hardware
          tsproc_mode filter
          delay_filter moving_median
          delay_filter_length 10
          egressLatency 0
          ingressLatency 0
          boundary_clock_jbod 1
          #
          # Clock description
          #
          productDescription ;;
          revisionData ;;
          manufacturerIdentity 00:00:00
          userDescription ;
          timeSource 0xA0
        ptp4lOpts: -2 --summary_interval -4
        ptpSchedulingPolicy: SCHED_FIFO
        ptpSchedulingPriority: 10
        ptpSettings:
          inSyncConditionThreshold: "10"
          inSyncConditionTimes: "12"
          logReduce: "false"
        ts2phcConf: |
          [global]
          use_syslog  0
          verbose 1
          logging_level 7
          ts2phc.pulsewidth 100000000
          leapfile  /usr/share/zoneinfo/leap-seconds.list
          domainNumber 25
          uds_address /var/run/ptp4l.0.socket
          [ens4f0]
          ts2phc.extts_polarity rising
          ts2phc.extts_correction -10
          ts2phc.master 0
          [ens1f0]
          ts2phc.extts_polarity rising
          ts2phc.extts_correction -27
          ts2phc.master 0
          [ens8f0]
          ts2phc.extts_polarity rising
          ts2phc.extts_correction -27
          ts2phc.master 0
        ts2phcOpts: -s generic -a --ts2phc.rh_external_pps 1
      recommend:
      - match:
        - nodeLabel: node-role.kubernetes.io/master
        priority: 4
        profile: 00-tbc-tt
      - match:
        - nodeLabel: node-role.kubernetes.io/master
        priority: 4
        profile: 01-tbc-tr
    ```

    - All TT ports have the `masterOnly` set to 1.

    - The `phc2sysOpts` setting in the TR profile specifies the upstream port `ens4f1` as the source of the node time synchronization.

    - The TR profile contains the hardware plugin section.

    - The interconnections section in the hardware plugin has three NICs: `ens4f0`, `ens1f0`, and `ens8f0`. The leading NIC, `ens4f0`, is the only one with the `gnnsInput` field, set to `false`, and the `upstreamPort` field that specifies the TR port. It also has a list of `phaseOutputConnectors`, `SMA1` and `SMA2`. The following NICs have the `inputConnector` field. Set the time receiver NIC `ens4f0` and the specific TR port. that is `upstreamPort: ens4f1`, for both T-BC and T-TSC configurations.

    - The `ts2phc` configuration contains the `domainNumber` of the upstream PTP domain.

    - The `ts2phc` configuration contains the `uds_address`. Its value is not important because the daemon patches it with the correct address.

    - The `ts2phc` configuration must include all NICs participating in this setup (`ens4f0`, `ens1f0`, and `ens8f0`).

    - `ts2phcOpts` sets the source as generic with `-s generic` and automatic with `-a`. The last option, `--ts2phc.rh_external_pps 1`, configures it to operate with external phase source, the digital phase-locked loop (DPLL).

      > [!NOTE]
      > In the single-NIC case, disable all pins or enable outputs if using for 1PPS measurements.

</div>

> [!NOTE]
> To render this configuration for T-TSC operation, remove the `00-tbc-tt` profile and adjust the `ts2phcConf` section to list only the TR NIC.

<div class="formalpara">

<div class="title">

Verification

</div>

To get the T-BC status, run the following command:

</div>

``` terminal
$ oc -linuxptp-daemon-container logs ds/linuxptp-daemon --since=1s -f |grep T-BC
```

<div class="formalpara">

<div class="title">

Example output

</div>

``` terminal
T-BC[1760525446]:[ts2phc.1.config] ens4f0 offset 1 T-BC-STATUS s2
T-BC[1760525447]:[ts2phc.1.config] ens4f0 offset 1 T-BC-STATUS s2
T-BC[1760525448]:[ts2phc.1.config] ens4f0 offset -1 T-BC-STATUS s2
```

</div>

This is reported every second, where `s2` indicates it is locked, `s1` indicates holdover is activated, and `s0`, unlocked.

<div>

<div class="title">

Additional resources

</div>

- [Grandmaster clock class sync state reference](configuring-ptp.md#nw-ptp-grandmaster-clock-class-reference_configuring-ptp)

</div>

# Configuring dynamic leap seconds handling for PTP grandmaster clocks

The PTP Operator container image includes the latest `leap-seconds.list` file that is available at the time of release.

You can configure the PTP Operator to automatically update the leap second file by using Global Positioning System (GPS) announcements.

Leap second information is stored in an automatically generated `ConfigMap` resource named `leap-configmap` in the `openshift-ptp` namespace. The PTP Operator mounts the `leap-configmap` resource as a volume in the `linuxptp-daemon` pod that is accessible by the `ts2phc` process.

If the GPS satellite broadcasts new leap second data, the PTP Operator updates the `leap-configmap` resource with the new data. The `ts2phc` process picks up the changes automatically.

> [!NOTE]
> The following procedure is provided as reference. The 4.17 version of the PTP Operator enables automatic leap second management by default.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have installed the PTP Operator and configured a PTP grandmaster clock (T-GM) in the cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Configure automatic leap second handling in the `phc2sysOpts` section of the `PtpConfig` CR. Set the following options:

    ``` yaml
    phc2sysOpts: -r -u 0 -m -N 8 -R 16 -S 2 -s ens2f0 -n 24
    ```

    > [!NOTE]
    > Previously, the T-GM required an offset adjustment in the `phc2sys` configuration (`-O -37`) to account for historical leap seconds. This is no longer needed.

2.  Configure the Intel e810 NIC to enable periodical reporting of `NAV-TIMELS` messages by the GPS receiver in the `spec.profile.plugins.e810.ublxCmds` section of the `PtpConfig` CR. For example:

    ``` yaml
    - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
        - "-P"
        - "29.20"
        - "-p"
        - "CFG-MSG,1,38,248"
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Validate that the configured T-GM is receiving `NAV-TIMELS` messages from the connected GPS. Run the following command:

    ``` terminal
    $ oc -n openshift-ptp -c linuxptp-daemon-container exec -it $(oc -n openshift-ptp get pods -o name | grep daemon) -- ubxtool -t -p NAV-TIMELS -P 29.20
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    1722509534.4417
    UBX-NAV-STATUS:
      iTOW 384752000 gpsFix 5 flags 0xdd fixStat 0x0 flags2 0x8
      ttff 18261, msss 1367642864

    1722509534.4419
    UBX-NAV-TIMELS:
      iTOW 384752000 version 0 reserved2 0 0 0 srcOfCurrLs 2
      currLs 18 srcOfLsChange 2 lsChange 0 timeToLsEvent 70376866
      dateOfLsGpsWn 2441 dateOfLsGpsDn 7 reserved2 0 0 0
      valid x3

    1722509534.4421
    UBX-NAV-CLOCK:
      iTOW 384752000 clkB 784281 clkD 435 tAcc 3 fAcc 215

    1722509535.4477
    UBX-NAV-STATUS:
      iTOW 384753000 gpsFix 5 flags 0xdd fixStat 0x0 flags2 0x8
      ttff 18261, msss 1367643864

    1722509535.4479
    UBX-NAV-CLOCK:
      iTOW 384753000 clkB 784716 clkD 435 tAcc 3 fAcc 218
    ```

    </div>

2.  Validate that the `leap-configmap` resource has been successfully generated by the PTP Operator and is up to date with the latest version of the [leap-seconds.list](https://hpiers.obspm.fr/iers/bul/bulc/ntp/leap-seconds.list). Run the following command:

    ``` terminal
    $ oc -n openshift-ptp get configmap leap-configmap -o jsonpath='{.data.<node_name>}'
    ```

    Replace `<node_name>` with the node where you have installed and configured the PTP T-GM clock with automatic leap second management. Escape special characters in the node name. For example, `node-1\.example\.com`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    # Do not edit
    # This file is generated automatically by linuxptp-daemon
    #$  3913697179
    #@  4291747200
    2272060800     10    # 1 Jan 1972
    2287785600     11    # 1 Jul 1972
    2303683200     12    # 1 Jan 1973
    2335219200     13    # 1 Jan 1974
    2366755200     14    # 1 Jan 1975
    2398291200     15    # 1 Jan 1976
    2429913600     16    # 1 Jan 1977
    2461449600     17    # 1 Jan 1978
    2492985600     18    # 1 Jan 1979
    2524521600     19    # 1 Jan 1980
    2571782400     20    # 1 Jul 1981
    2603318400     21    # 1 Jul 1982
    2634854400     22    # 1 Jul 1983
    2698012800     23    # 1 Jul 1985
    2776982400     24    # 1 Jan 1988
    2840140800     25    # 1 Jan 1990
    2871676800     26    # 1 Jan 1991
    2918937600     27    # 1 Jul 1992
    2950473600     28    # 1 Jul 1993
    2982009600     29    # 1 Jul 1994
    3029443200     30    # 1 Jan 1996
    3076704000     31    # 1 Jul 1997
    3124137600     32    # 1 Jan 1999
    3345062400     33    # 1 Jan 2006
    3439756800     34    # 1 Jan 2009
    3550089600     35    # 1 Jul 2012
    3644697600     36    # 1 Jul 2015
    3692217600     37    # 1 Jan 2017

    #h  e65754d4 8f39962b aa854a61 661ef546 d2af0bfa
    ```

    </div>

</div>

# Configuring linuxptp services as a boundary clock

You can configure the `linuxptp` services (`ptp4l`, `phc2sys`) as boundary clock by creating a `PtpConfig` custom resource (CR) object.

> [!NOTE]
> Use the following example `PtpConfig` CR as the basis to configure `linuxptp` services as the boundary clock for your particular hardware and environment. This example CR does not configure PTP fast events. To configure PTP fast events, set appropriate values for `ptp4lOpts`, `ptp4lConf`, and `ptpClockThreshold`. `ptpClockThreshold` is used only when events are enabled. See "Configuring the PTP fast event notifications publisher" for more information.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the following `PtpConfig` CR, and then save the YAML in the `boundary-clock-ptp-config.yaml` file.

    <div class="formalpara">

    <div class="title">

    Example PTP boundary clock configuration

    </div>

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: boundary-clock
      namespace: openshift-ptp
      annotations: {}
    spec:
      profile:
        - name: boundary-clock
          ptp4lOpts: "-2"
          phc2sysOpts: "-a -r -n 24"
          ptpSchedulingPolicy: SCHED_FIFO
          ptpSchedulingPriority: 10
          ptpSettings:
            logReduce: "true"
          ptp4lConf: |
            # The interface name is hardware-specific
            [$iface_slave]
            masterOnly 0
            [$iface_master_1]
            masterOnly 1
            [$iface_master_2]
            masterOnly 1
            [$iface_master_3]
            masterOnly 1
            [global]
            #
            # Default Data Set
            #
            twoStepFlag 1
            slaveOnly 0
            priority1 128
            priority2 128
            domainNumber 24
            #utc_offset 37
            clockClass 248
            clockAccuracy 0xFE
            offsetScaledLogVariance 0xFFFF
            free_running 0
            freq_est_interval 1
            dscp_event 0
            dscp_general 0
            dataset_comparison G.8275.x
            G.8275.defaultDS.localPriority 128
            #
            # Port Data Set
            #
            logAnnounceInterval -3
            logSyncInterval -4
            logMinDelayReqInterval -4
            logMinPdelayReqInterval -4
            announceReceiptTimeout 3
            syncReceiptTimeout 0
            delayAsymmetry 0
            fault_reset_interval -4
            neighborPropDelayThresh 20000000
            masterOnly 0
            G.8275.portDS.localPriority 128
            #
            # Run time options
            #
            assume_two_step 0
            logging_level 6
            path_trace_enabled 0
            follow_up_info 0
            hybrid_e2e 0
            inhibit_multicast_service 0
            net_sync_monitor 0
            tc_spanning_tree 0
            tx_timestamp_timeout 50
            unicast_listen 0
            unicast_master_table 0
            unicast_req_duration 3600
            use_syslog 1
            verbose 0
            summary_interval 0
            kernel_leap 1
            check_fup_sync 0
            clock_class_threshold 135
            #
            # Servo Options
            #
            pi_proportional_const 0.0
            pi_integral_const 0.0
            pi_proportional_scale 0.0
            pi_proportional_exponent -0.3
            pi_proportional_norm_max 0.7
            pi_integral_scale 0.0
            pi_integral_exponent 0.4
            pi_integral_norm_max 0.3
            step_threshold 2.0
            first_step_threshold 0.00002
            max_frequency 900000000
            clock_servo pi
            sanity_freq_limit 200000000
            ntpshm_segment 0
            #
            # Transport options
            #
            transportSpecific 0x0
            ptp_dst_mac 01:1B:19:00:00:00
            p2p_dst_mac 01:80:C2:00:00:0E
            udp_ttl 1
            udp6_scope 0x0E
            uds_address /var/run/ptp4l
            #
            # Default interface options
            #
            clock_type BC
            network_transport L2
            delay_mechanism E2E
            time_stamping hardware
            tsproc_mode filter
            delay_filter moving_median
            delay_filter_length 10
            egressLatency 0
            ingressLatency 0
            boundary_clock_jbod 0
            #
            # Clock description
            #
            productDescription ;;
            revisionData ;;
            manufacturerIdentity 00:00:00
            userDescription ;
            timeSource 0xA0
      recommend:
        - profile: boundary-clock
          priority: 4
          match:
            - nodeLabel: "node-role.kubernetes.io/$mcp"
    ```

    </div>

    | CR field | Description |
    |----|----|
    | `name` | The name of the `PtpConfig` CR. |
    | `profile` | Specify an array of one or more `profile` objects. |
    | `name` | Specify the name of a profile object which uniquely identifies a profile object. |
    | `ptp4lOpts` | Specify system config options for the `ptp4l` service. The options should not include the network interface name `-i <interface>` and service config file `-f /etc/ptp4l.conf` because the network interface name and the service config file are automatically appended. |
    | `ptp4lConf` | Specify the required configuration to start `ptp4l` as boundary clock. For example, `ens1f0` synchronizes from a grandmaster clock and `ens1f3` synchronizes connected devices. |
    | `<interface_1>` | The interface that receives the synchronization clock. |
    | `<interface_2>` | The interface that sends the synchronization clock. |
    | `tx_timestamp_timeout` | For Intel Columbiaville 800 Series NICs, set `tx_timestamp_timeout` to `50`. |
    | `boundary_clock_jbod` | For Intel Columbiaville 800 Series NICs, ensure `boundary_clock_jbod` is set to `0`. For Intel Fortville X710 Series NICs, ensure `boundary_clock_jbod` is set to `1`. |
    | `phc2sysOpts` | Specify system config options for the `phc2sys` service. If this field is empty, the PTP Operator does not start the `phc2sys` service. |
    | `ptpSchedulingPolicy` | Scheduling policy for ptp4l and phc2sys processes. Default value is `SCHED_OTHER`. Use `SCHED_FIFO` on systems that support FIFO scheduling. |
    | `ptpSchedulingPriority` | Integer value from 1-65 used to set FIFO priority for `ptp4l` and `phc2sys` processes when `ptpSchedulingPolicy` is set to `SCHED_FIFO`. The `ptpSchedulingPriority` field is not used when `ptpSchedulingPolicy` is set to `SCHED_OTHER`. |
    | `ptpClockThreshold` | Optional. If `ptpClockThreshold` is not present, default values are used for the `ptpClockThreshold` fields. `ptpClockThreshold` configures how long after the PTP master clock is disconnected before PTP events are triggered. `holdOverTimeout` is the time value in seconds before the PTP clock event state changes to `FREERUN` when the PTP master clock is disconnected. The `maxOffsetThreshold` and `minOffsetThreshold` settings configure offset values in nanoseconds that compare against the values for `CLOCK_REALTIME` (`phc2sys`) or master offset (`ptp4l`). When the `ptp4l` or `phc2sys` offset value is outside this range, the PTP clock state is set to `FREERUN`. When the offset value is within this range, the PTP clock state is set to `LOCKED`. |
    | `recommend` | Specify an array of one or more `recommend` objects that define rules on how the `profile` should be applied to nodes. |
    | `.recommend.profile` | Specify the `.recommend.profile` object name defined in the `profile` section. |
    | `.recommend.priority` | Specify the `priority` with an integer value between `0` and `99`. A larger number gets lower priority, so a priority of `99` is lower than a priority of `10`. If a node can be matched with multiple profiles according to rules defined in the `match` field, the profile with the higher priority is applied to that node. |
    | `.recommend.match` | Specify `.recommend.match` rules with `nodeLabel` or `nodeName` values. |
    | `.recommend.match.nodeLabel` | Set `nodeLabel` with the `key` of the `node.Labels` field from the node object by using the `oc get nodes --show-labels` command. For example, `node-role.kubernetes.io/worker`. |
    | `.recommend.match.nodeName` | Set `nodeName` with the value of the `node.Name` field from the node object by using the `oc get nodes` command. For example, `compute-1.example.com`. |

    PTP boundary clock CR configuration options

2.  Create the CR by running the following command:

    ``` terminal
    $ oc create -f boundary-clock-ptp-config.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                            READY   STATUS    RESTARTS   AGE   IP               NODE
        linuxptp-daemon-4xkbb           1/1     Running   0          43m   10.1.196.24      compute-0.example.com
        linuxptp-daemon-tdspf           1/1     Running   0          43m   10.1.196.25      compute-1.example.com
        ptp-operator-657bbb64c8-2f8sj   1/1     Running   0          43m   10.129.0.61      control-plane-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile. Run the following command:

        ``` terminal
        $ oc logs linuxptp-daemon-4xkbb -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        I1115 09:41:17.117596 4143292 daemon.go:107] in applyNodePTPProfile
        I1115 09:41:17.117604 4143292 daemon.go:109] updating NodePTPProfile to:
        I1115 09:41:17.117607 4143292 daemon.go:110] ------------------------------------
        I1115 09:41:17.117612 4143292 daemon.go:102] Profile Name: profile1
        I1115 09:41:17.117616 4143292 daemon.go:102] Interface:
        I1115 09:41:17.117620 4143292 daemon.go:102] Ptp4lOpts: -2
        I1115 09:41:17.117623 4143292 daemon.go:102] Phc2sysOpts: -a -r -n 24
        I1115 09:41:17.117626 4143292 daemon.go:116] ------------------------------------
        ```

        </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring FIFO priority scheduling for PTP hardware](configuring-ptp.md#cnf-configuring-fifo-priority-scheduling-for-ptp_configuring-ptp)

- [Configuring the PTP fast event notifications publisher](ptp-cloud-events-consumer-dev-reference-v2.md#cnf-configuring-the-ptp-fast-event-publisher-v2_ptp-consumer)

</div>

## Configuring linuxptp services as boundary clocks for dual-NIC hardware

You can configure the `linuxptp` services (`ptp4l`, `phc2sys`) as boundary clocks for dual-NIC hardware by creating a `PtpConfig` custom resource (CR) object for each NIC.

Dual NIC hardware allows you to connect each NIC to the same upstream leader clock with separate `ptp4l` instances for each NIC feeding the downstream clocks.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create two separate `PtpConfig` CRs, one for each NIC, using the reference CR in "Configuring linuxptp services as a boundary clock" as the basis for each CR. For example:

    1.  Create `boundary-clock-ptp-config-nic1.yaml`, specifying values for `phc2sysOpts`:

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: boundary-clock-ptp-config-nic1
          namespace: openshift-ptp
        spec:
          profile:
          - name: "profile1"
            ptp4lOpts: "-2 --summary_interval -4"
            ptp4lConf: |
              [ens5f1]
              masterOnly 1
              [ens5f0]
              masterOnly 0
            ...
            phc2sysOpts: "-a -r -m -n 24 -N 8 -R 16"
        ```

        where:

        `ptp4lConf`
        Specifies the required interfaces to start `ptp4l` as a boundary clock. For example, `ens5f0` synchronizes from a grandmaster clock and `ens5f1` synchronizes connected devices.

        `phc2sysOpts: "-a -r -m -n 24 -N 8 -R 16"`
        Sets the required `phc2sysOpts` values. `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics.

    2.  Create `boundary-clock-ptp-config-nic2.yaml`, removing the `phc2sysOpts` field altogether to disable the `phc2sys` service for the second NIC:

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: boundary-clock-ptp-config-nic2
          namespace: openshift-ptp
        spec:
          profile:
          - name: "profile2"
            ptp4lOpts: "-2 --summary_interval -4"
            ptp4lConf: |
              [ens7f1]
              masterOnly 1
              [ens7f0]
              masterOnly 0
        ...
        ```

        Specify the required interfaces to start `ptp4l` as a boundary clock on the second NIC.

        > [!NOTE]
        > You must completely remove the `phc2sysOpts` field from the second `PtpConfig` CR to disable the `phc2sys` service on the second NIC.

2.  Create the dual-NIC `PtpConfig` CRs by running the following commands:

    1.  Create the CR that configures PTP for the first NIC:

        ``` terminal
        $ oc create -f boundary-clock-ptp-config-nic1.yaml
        ```

    2.  Create the CR that configures PTP for the second NIC:

        ``` terminal
        $ oc create -f boundary-clock-ptp-config-nic2.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

- Check that the PTP Operator has applied the `PtpConfig` CRs for both NICs. Examine the logs for the `linuxptp` daemon corresponding to the node that has the dual-NIC hardware installed. For example, run the following command:

  ``` terminal
  $ oc logs linuxptp-daemon-cvgr6 -n openshift-ptp -c linuxptp-daemon-container
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  ptp4l[80828.335]: [ptp4l.1.config] master offset          5 s2 freq   -5727 path delay       519
  ptp4l[80828.343]: [ptp4l.0.config] master offset         -5 s2 freq  -10607 path delay       533
  phc2sys[80828.390]: [ptp4l.0.config] CLOCK_REALTIME phc offset         1 s2 freq  -87239 delay    539
  ```

  </div>

</div>

## Configuring linuxptp as a highly available system clock for dual-NIC Intel E810 PTP boundary clocks

You can configure the `linuxptp` services `ptp4l` and `phc2sys` as a highly available (HA) system clock for dual PTP boundary clocks (T-BC).

The highly available system clock uses multiple time sources from dual-NIC Intel E810 Salem channel hardware configured as two boundary clocks. Two boundary clocks instances participate in the HA setup, each with its own configuration profile. You connect each NIC to the same upstream leader clock with separate `ptp4l` instances for each NIC feeding the downstream clocks.

Create two `PtpConfig` custom resource (CR) objects that configure the NICs as T-BC and a third `PtpConfig` CR that configures high availability between the two NICs.

> [!IMPORTANT]
> You set `phc2SysOpts` options once in the `PtpConfig` CR that configures HA. Set the `phc2sysOpts` field to an empty string in the `PtpConfig` CRs that configure the two NICs. This prevents individual `phc2sys` processes from being set up for the two profiles.

The third `PtpConfig` CR configures a highly available system clock service. The CR sets the `ptp4lOpts` field to an empty string to prevent the `ptp4l` process from running. The CR adds profiles for the `ptp4l` configurations under the `spec.profile.ptpSettings.haProfiles` key and passes the kernel socket path of those profiles to the `phc2sys` service. When a `ptp4l` failure occurs, the `phc2sys` service switches to the backup `ptp4l` configuration. When the primary profile becomes active again, the `phc2sys` service reverts to the original state.

> [!IMPORTANT]
> Ensure that you set `spec.recommend.priority` to the same value for all three `PtpConfig` CRs that you use to configure HA.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

- Configure a cluster node with Intel E810 Salem channel dual-NIC.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create two separate `PtpConfig` CRs, one for each NIC, using the CRs in "Configuring linuxptp services as boundary clocks for dual-NIC hardware" as a reference for each CR.

    1.  Create the `ha-ptp-config-nic1.yaml` file, specifying an empty string for the `phc2sysOpts` field. For example:

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: ha-ptp-config-nic1
          namespace: openshift-ptp
        spec:
          profile:
          - name: "ha-ptp-config-profile1"
            ptp4lOpts: "-2 --summary_interval -4"
            ptp4lConf: |
              [ens5f1]
              masterOnly 1
              [ens5f0]
              masterOnly 0
            #...
            phc2sysOpts: ""
        ```

        where:

        `ptp4lConf`
        Specifies the required interfaces to start `ptp4l` as a boundary clock. For example, `ens5f0` synchronizes from a grandmaster clock and `ens5f1` synchronizes connected devices.

        `phc2sysOpts: ""`
        Sets `phc2sysOpts` with an empty string. These values are populated from the `spec.profile.ptpSettings.haProfiles` field of the `PtpConfig` CR that configures high availability.

    2.  Apply the `PtpConfig` CR for NIC 1 by running the following command:

        ``` terminal
        $ oc create -f ha-ptp-config-nic1.yaml
        ```

    3.  Create the `ha-ptp-config-nic2.yaml` file, specifying an empty string for the `phc2sysOpts` field. For example:

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: ha-ptp-config-nic2
          namespace: openshift-ptp
        spec:
          profile:
          - name: "ha-ptp-config-profile2"
            ptp4lOpts: "-2 --summary_interval -4"
            ptp4lConf: |
              [ens7f1]
              masterOnly 1
              [ens7f0]
              masterOnly 0
            #...
            phc2sysOpts: ""
        ```

    4.  Apply the `PtpConfig` CR for NIC 2 by running the following command:

        ``` terminal
        $ oc create -f ha-ptp-config-nic2.yaml
        ```

2.  Create the `PtpConfig` CR that configures the HA system clock. For example:

    1.  Create the `ptp-config-for-ha.yaml` file. Set `haProfiles` to match the `metadata.name` fields that are set in the `PtpConfig` CRs that configure the two NICs. For example: `haProfiles: ha-ptp-config-nic1,ha-ptp-config-nic2`

        ``` yaml
        apiVersion: ptp.openshift.io/v1
        kind: PtpConfig
        metadata:
          name: boundary-ha
          namespace: openshift-ptp
          annotations: {}
        spec:
          profile:
            - name: "boundary-ha"
              ptp4lOpts: ""
              phc2sysOpts: "-a -r -n 24"
              ptpSchedulingPolicy: SCHED_FIFO
              ptpSchedulingPriority: 10
              ptpSettings:
                logReduce: "true"
                haProfiles: "$profile1,$profile2"
          recommend:
            - profile: "boundary-ha"
              priority: 4
              match:
                - nodeLabel: "node-role.kubernetes.io/$mcp"
        ```

        Set the `ptp4lOpts` field to an empty string. If it is not empty, the `p4ptl` process starts with a critical error.

        > [!IMPORTANT]
        > Do not apply the high availability `PtpConfig` CR before the `PtpConfig` CRs that configure the individual NICs.

    2.  Apply the HA `PtpConfig` CR by running the following command:

        ``` terminal
        $ oc create -f ptp-config-for-ha.yaml
        ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify that the PTP Operator has applied the `PtpConfig` CRs correctly. Perform the following steps:

  1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

      ``` terminal
      $ oc get pods -n openshift-ptp -o wide
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      NAME                            READY   STATUS    RESTARTS   AGE   IP               NODE
      linuxptp-daemon-4xkrb           1/1     Running   0          43m   10.1.196.24      compute-0.example.com
      ptp-operator-657bbq64c8-2f8sj   1/1     Running   0          43m   10.129.0.61      control-plane-1.example.com
      ```

      </div>

      > [!NOTE]
      > There should be only one `linuxptp-daemon` pod.

  2.  Check that the profile is correct by running the following command. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile.

      ``` terminal
      $ oc logs linuxptp-daemon-4xkrb -n openshift-ptp -c linuxptp-daemon-container
      ```

      <div class="formalpara">

      <div class="title">

      Example output

      </div>

      ``` terminal
      I1115 09:41:17.117596 4143292 daemon.go:107] in applyNodePTPProfile
      I1115 09:41:17.117604 4143292 daemon.go:109] updating NodePTPProfile to:
      I1115 09:41:17.117607 4143292 daemon.go:110] ------------------------------------
      I1115 09:41:17.117612 4143292 daemon.go:102] Profile Name: ha-ptp-config-profile1
      I1115 09:41:17.117616 4143292 daemon.go:102] Interface:
      I1115 09:41:17.117620 4143292 daemon.go:102] Ptp4lOpts: -2
      I1115 09:41:17.117623 4143292 daemon.go:102] Phc2sysOpts: -a -r -n 24
      I1115 09:41:17.117626 4143292 daemon.go:116] ------------------------------------
      ```

      </div>

</div>

## Boundary clocks without holdover on Intel Granite Rapids-D hardware

Intel Granite Rapids-D (GNR-D) server platforms support Precision Time Protocol (PTP) boundary clock (BC) deployments without holdover for high-density Radio Access Network (RAN) sites that use onboard Network Acceleration Complex (NAC) ports and optional Carter Flat expansion network interface cards (NICs).

> [!NOTE]
> Configuring a BC without holdover support on GNR-D hardware is a Technology Preview (TP) feature in OpenShift Container Platform 4.20.16 and is Generally Available (GA) in OpenShift Container Platform 4.20.24 and later versions.

In a BC deployment, one time receiver (TR) port synchronizes to an upstream timing source while time transmitter (TT) ports distribute synchronized time to downstream devices. GNR-D platforms use platform-specific `PtpConfig` plugin configurations and internal timing paths.

Before you configure a BC profile on GNR-D hardware, verify that your qualified hardware layout, interface naming, and plugin configuration align with your deployment requirements.

GNR-D BC deployments use onboard NAC ports as the primary timing controller and can extend timing distribution by using optional Carter Flat expansion NICs.

GNR-D platforms route synchronization internally instead of using external timing cabling.

Your qualified hardware layout determines the available TR and TT port roles across NAC ports and optional Carter Flat expansion cards.

### Boundary clock without holdover behavior

GNR-D boundary clock deployments on Carter Flat hardware do not maintain time synchronization if the upstream timing source becomes unavailable. This deployment model operates without monitored holdover because Carter Flat hardware does not expose sufficient follower digital phase-locked loop (DPLL) accuracy information for holdover support.

To maintain synchronization, keep a continuous connection to a qualified upstream PTP source.

Red Hat tools can detect follower DPLL lock state, but they cannot monitor the detailed follower DPLL accuracy that holdover support requires.

When you configure a BC profile on GNR-D hardware that uses Carter Flat NICs, disable holdover.

## Configuring linuxptp services as a boundary clock without holdover on Intel Granite Rapids-D hardware

Use this procedure to configure a Precision Time Protocol (PTP) boundary clock (BC) profile without holdover on Intel Granite Rapids-D (GNR-D) hardware that uses onboard Network Acceleration Complex (NAC) ports and optional Carter Flat expansion network interface cards (NICs).

> [!NOTE]
> Configuring a BC without holdover support on GNR-D hardware is a Technology Preview (TP) feature in OpenShift Container Platform 4.20.16 and is Generally Available (GA) in OpenShift Container Platform 4.20.24 and later versions.

In this deployment, one time receiver (TR) port synchronizes to an upstream timing source and time transmitter (TT) ports distribute synchronized time downstream.

> [!IMPORTANT]
> GNR-D BC deployments that use Carter Flat NICs operate without monitored holdover. Disable holdover in your `PtpConfig` profile.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You are logged in as a user with `cluster-admin` privileges.

- You have installed the PTP Operator.

- You have verified your qualified GNR-D hardware layout, including NAC ports, Carter Flat ports, and TR/TT role assignments.

- You have verified interface naming and plugin device alignment for your hardware layout.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `PtpConfig` custom resource (CR) that matches your qualified GNR-D BC without holdover hardware layout:

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: gnrd-bc
      namespace: openshift-ptp
      annotations:
        ran.openshift.io/ztp-deploy-wave: "10"
    spec:
      profile:
        - name: 00-bc-tt
          ptp4lConf: |
            # All TimeTransmitter ports should be outlined here with 'masterOnly 1'
            #[eno8303]
            # ** Host management interface
            [eno8403]
            masterOnly 1
            #[eno8503]
            # ** TR port (see 01-bc-tr profile)
            [eno8603]
            masterOnly 1
            [eno8703]
            masterOnly 1
            [eno8803]
            masterOnly 1
            [eno8903]
            masterOnly 1
            [eno9003]
            masterOnly 1
            [enp108s0f0]
            masterOnly 1
            [enp108s0f1]
            masterOnly 1
            [enp108s0f2]
            masterOnly 1
            [enp108s0f3]
            masterOnly 1
            [enp108s0f4]
            masterOnly 1
            [enp108s0f5]
            masterOnly 1
            [enp108s0f6]
            masterOnly 1
            [enp108s0f7]
            masterOnly 1
            [enp110s0f0]
            masterOnly 1
            [enp110s0f1]
            masterOnly 1
            [enp110s0f2]
            masterOnly 1
            [enp110s0f3]
            masterOnly 1
            [enp110s0f4]
            masterOnly 1
            [enp110s0f5]
            masterOnly 1
            [enp110s0f6]
            masterOnly 1
            [enp110s0f7]
            masterOnly 1
            [global]
            #
            # Default Data Set
            #
            twoStepFlag 1
            slaveOnly 0
            priority1 128
            priority2 128
            domainNumber 24
            #utc_offset 37
            clockClass 248
            clockAccuracy 0xFE
            offsetScaledLogVariance 0xFFFF
            free_running 0
            freq_est_interval 1
            dscp_event 0
            dscp_general 0
            dataset_comparison G.8275.x
            G.8275.defaultDS.localPriority 128
            #
            # Port Data Set
            #
            logAnnounceInterval -3
            logSyncInterval -4
            logMinDelayReqInterval -4
            logMinPdelayReqInterval -4
            announceReceiptTimeout 3
            syncReceiptTimeout 0
            delayAsymmetry 0
            fault_reset_interval -4
            neighborPropDelayThresh 20000000
            masterOnly 0
            G.8275.portDS.localPriority 128
            #
            # Run time options
            #
            assume_two_step 0
            logging_level 6
            path_trace_enabled 0
            follow_up_info 0
            hybrid_e2e 0
            inhibit_multicast_service 0
            net_sync_monitor 0
            tc_spanning_tree 0
            tx_timestamp_timeout 50
            unicast_listen 0
            unicast_master_table 0
            unicast_req_duration 3600
            use_syslog 1
            verbose 0
            summary_interval 0
            kernel_leap 1
            check_fup_sync 0
            clock_class_threshold 135
            #
            # Servo Options
            #

            # NGEN TEST MODIFIED
            # New:
            # pi_proportional_const 0.60
            # pi_integral_const 0.0003
            # Old:
            # pi_proportional_const 0.0
            # pi_integral_const 0.0
            # END TEST MOD

            pi_proportional_const 0.60
            pi_integral_const 0.001
            pi_proportional_scale 0.0
            pi_proportional_exponent -0.3
            pi_proportional_norm_max 0.7
            pi_integral_scale 0.0
            pi_integral_exponent 0.4
            pi_integral_norm_max 0.3
            step_threshold 2.0
            # end T-BC experiment
            first_step_threshold 0.00002
            max_frequency 900000000
            clock_servo pi
            sanity_freq_limit 200000000
            ntpshm_segment 0
            #
            # Transport options
            #
            transportSpecific 0x0
            ptp_dst_mac 01:1B:19:00:00:00
            p2p_dst_mac 01:80:C2:00:00:0E
            udp_ttl 1
            udp6_scope 0x0E
            uds_address /var/run/ptp4l
            #
            # Default interface options
            #
            clock_type BC
            network_transport L2
            delay_mechanism E2E
            time_stamping hardware
            tsproc_mode filter
            delay_filter moving_median
            delay_filter_length 10
            egressLatency 0
            ingressLatency 0
            boundary_clock_jbod 1
            #
            # Clock description
            #
            productDescription ;;
            revisionData ;;
            manufacturerIdentity 00:00:00
            userDescription ;
            timeSource 0xA0
          ptp4lOpts: -2 --summary_interval -4
          ptpSchedulingPolicy: SCHED_FIFO
          ptpSchedulingPriority: 10
          ptpSettings:
            controllingProfile: 01-bc-tr
            logReduce: "true"
        - name: 01-bc-tr
          phc2sysOpts: -r -n 24 -N 8 -R 16 -u 0 -m -s $upstreamInterface
          ptp4lConf: |
            [$upstreamInterface]
            masterOnly 0
            [global]
            #
            # Default Data Set
            #
            twoStepFlag 1
            slaveOnly 0
            priority1 128
            priority2 128
            domainNumber 24
            #utc_offset 37
            clockClass 248
            clockAccuracy 0xFE
            offsetScaledLogVariance 0xFFFF
            free_running 0
            freq_est_interval 1
            dscp_event 0
            dscp_general 0
            dataset_comparison G.8275.x
            G.8275.defaultDS.localPriority 128
            #
            # Port Data Set
            #
            logAnnounceInterval -3
            logSyncInterval -4
            logMinDelayReqInterval -4
            logMinPdelayReqInterval -4
            announceReceiptTimeout 3
            syncReceiptTimeout 0
            delayAsymmetry 0
            fault_reset_interval -4
            neighborPropDelayThresh 20000000
            masterOnly 0
            G.8275.portDS.localPriority 128
            #
            # Run time options
            #
            assume_two_step 0
            logging_level 6
            path_trace_enabled 0
            follow_up_info 0
            hybrid_e2e 0
            inhibit_multicast_service 0
            net_sync_monitor 0
            tc_spanning_tree 0
            tx_timestamp_timeout 50
            unicast_listen 0
            unicast_master_table 0
            unicast_req_duration 3600
            use_syslog 1
            verbose 0
            summary_interval 0
            kernel_leap 1
            check_fup_sync 0
            clock_class_threshold 135
            #
            # Servo Options
            #

            # NGEN TEST MODIFIED
            # New:
            # pi_proportional_const 0.60
            # pi_integral_const 0.0003
            # Old:
            # pi_proportional_const 0.0
            # pi_integral_const 0.0
            # END TEST MOD

            pi_proportional_const 0.60
            pi_integral_const 0.001
            pi_proportional_scale 0.0
            pi_proportional_exponent -0.3
            pi_proportional_norm_max 0.7
            pi_integral_scale 0.0
            pi_integral_exponent 0.4
            pi_integral_norm_max 0.3
            step_threshold 2.0
            # end T-BC experiment
            first_step_threshold 0.00002
            max_frequency 900000000
            clock_servo pi
            sanity_freq_limit 200000000
            ntpshm_segment 0
            #
            # Transport options
            #
            transportSpecific 0x0
            ptp_dst_mac 01:1B:19:00:00:00
            p2p_dst_mac 01:80:C2:00:00:0E
            udp_ttl 1
            udp6_scope 0x0E
            uds_address /var/run/ptp4l
            #
            # Default interface options
            #
            clock_type OC
            network_transport L2
            delay_mechanism E2E
            time_stamping hardware
            tsproc_mode filter
            delay_filter moving_median
            delay_filter_length 10
            egressLatency 0
            ingressLatency 0
            boundary_clock_jbod 1
            #
            # Clock description
            #
            productDescription ;;
            revisionData ;;
            manufacturerIdentity 00:00:00
            userDescription ;
            timeSource 0xA0
          ptp4lOpts: -2 --summary_interval -4
          ptpSchedulingPolicy: SCHED_FIFO
          ptpSchedulingPriority: 10
          ptpSettings:
            clockType: T-BC
            inSyncConditionThreshold: "10"
            inSyncConditionTimes: "12"
            logReduce: "true"
            leadingInterface: eno8703
            upstreamPort: $upstreamInterface
          plugins:
            e825:
              devices:
                - eno8703
              settings:
                LocalMaxHoldoverOffSet: 500
                LocalHoldoverTimeout: 0
                MaxInSpecOffset: 100
            e830:
              devices:
                - enp108s0f0
                - enp110s0f0
          ts2phcConf: |
            [global]
            use_syslog  0
            verbose 1
            logging_level 7
            ts2phc.pulsewidth 500000000
            leapfile  /usr/share/zoneinfo/leap-seconds.list
            domainNumber 24
            uds_address /var/run/ptp4l.1.socket
            [eno8703]
            ts2phc.extts_correction 0
            ts2phc.master 0
            ts2phc.channel 0
            ts2phc.pin_index 1
            # This should be one section per Carter Flats (e830) card:
            [enp108s0f0]
            ts2phc.extts_polarity rising
            ts2phc.extts_correction 0
            ts2phc.master 0
            ts2phc.channel 0
            ts2phc.pin_index 1
            [enp110s0f0]
            ts2phc.extts_polarity rising
            ts2phc.extts_correction 0
            ts2phc.master 0
            ts2phc.channel 0
            ts2phc.pin_index 1
          ts2phcOpts: -s generic -a --ts2phc.rh_external_pps 1
      recommend:
        - match:
          - nodeLabel: node-role.kubernetes.io/$mcp
          priority: 4
          profile: 00-bc-tt
        - match:
          - nodeLabel: node-role.kubernetes.io/$mcp
          priority: 4
          profile: 01-bc-tr
    ```

    where:

    TR interface
    Specifies the interface that synchronizes to the upstream timing source. Replace this value with the qualified TR interface from your site bill of materials.

    TT interfaces
    Specify the interfaces that distribute synchronized time downstream. Replace these values with the qualified TT interfaces for your deployment.

    `plugins.e825.devices`
    Specifies the qualified NAC interfaces for your hardware layout.

    `plugins.e830.devices`
    Specifies the qualified Carter Flat interfaces for your hardware layout, if installed.

    `ptp4lConf`
    Defines BC timing behavior, including TR and TT interface roles.

    `ts2phcConf`
    Defines timing synchronization behavior for qualified hardware devices.

    `recommend`
    Specifies the machine config pool that selects the target DU nodes. Replace placeholder values with the machine config pool label for your deployment.

2.  Apply the `PtpConfig` CR:

    ``` terminal
    $ oc apply -f <name_of_the_ptpconfig_yaml_file>
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Verify that the `PtpConfig` profile is applied:

    ``` terminal
    $ oc get ptpconfig -n openshift-ptp
    ```

2.  Verify that the `linuxptp` daemon is running on the target node:

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

3.  Review `linuxptp` daemon logs for BC status:

    ``` terminal
    $ oc logs <linuxptp_daemon_pod> -n openshift-ptp -c linuxptp-daemon-container
    ```

4.  Verify the following:

    - The TR port synchronizes successfully to the upstream timing source.

    - TT ports distribute timing downstream.

    - The deployed BC profile operates without holdover.

</div>

# Configuring linuxptp services as an ordinary clock

You can configure `linuxptp` services (`ptp4l`, `phc2sys`) as ordinary clock by creating a `PtpConfig` custom resource (CR) object.

> [!NOTE]
> Use the following example `PtpConfig` CR as the basis to configure `linuxptp` services as an ordinary clock for your particular hardware and environment. This example CR does not configure PTP fast events. To configure PTP fast events, set appropriate values for `ptp4lOpts`, `ptp4lConf`, and `ptpClockThreshold`. `ptpClockThreshold` is required only when events are enabled. See "Configuring the PTP fast event notifications publisher" for more information.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the following `PtpConfig` CR, and then save the YAML in the `ordinary-clock-ptp-config.yaml` file.

    <div id="ptp-ordinary-clock" class="formalpara">

    <div class="title">

    Example PTP ordinary clock configuration

    </div>

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: ordinary-clock
      namespace: openshift-ptp
      annotations: {}
    spec:
      profile:
        - name: ordinary-clock
          # The interface name is hardware-specific
          interface: $interface
          ptp4lOpts: "-2 -s"
          phc2sysOpts: "-a -r -n 24"
          ptpSchedulingPolicy: SCHED_FIFO
          ptpSchedulingPriority: 10
          ptpSettings:
            logReduce: "true"
          ptp4lConf: |
            [global]
            #
            # Default Data Set
            #
            twoStepFlag 1
            slaveOnly 1
            priority1 128
            priority2 128
            domainNumber 24
            #utc_offset 37
            clockClass 255
            clockAccuracy 0xFE
            offsetScaledLogVariance 0xFFFF
            free_running 0
            freq_est_interval 1
            dscp_event 0
            dscp_general 0
            dataset_comparison G.8275.x
            G.8275.defaultDS.localPriority 128
            #
            # Port Data Set
            #
            logAnnounceInterval -3
            logSyncInterval -4
            logMinDelayReqInterval -4
            logMinPdelayReqInterval -4
            announceReceiptTimeout 3
            syncReceiptTimeout 0
            delayAsymmetry 0
            fault_reset_interval -4
            neighborPropDelayThresh 20000000
            masterOnly 0
            G.8275.portDS.localPriority 128
            #
            # Run time options
            #
            assume_two_step 0
            logging_level 6
            path_trace_enabled 0
            follow_up_info 0
            hybrid_e2e 0
            inhibit_multicast_service 0
            net_sync_monitor 0
            tc_spanning_tree 0
            tx_timestamp_timeout 50
            unicast_listen 0
            unicast_master_table 0
            unicast_req_duration 3600
            use_syslog 1
            verbose 0
            summary_interval 0
            kernel_leap 1
            check_fup_sync 0
            clock_class_threshold 7
            #
            # Servo Options
            #
            pi_proportional_const 0.0
            pi_integral_const 0.0
            pi_proportional_scale 0.0
            pi_proportional_exponent -0.3
            pi_proportional_norm_max 0.7
            pi_integral_scale 0.0
            pi_integral_exponent 0.4
            pi_integral_norm_max 0.3
            step_threshold 2.0
            first_step_threshold 0.00002
            max_frequency 900000000
            clock_servo pi
            sanity_freq_limit 200000000
            ntpshm_segment 0
            #
            # Transport options
            #
            transportSpecific 0x0
            ptp_dst_mac 01:1B:19:00:00:00
            p2p_dst_mac 01:80:C2:00:00:0E
            udp_ttl 1
            udp6_scope 0x0E
            uds_address /var/run/ptp4l
            #
            # Default interface options
            #
            clock_type OC
            network_transport L2
            delay_mechanism E2E
            time_stamping hardware
            tsproc_mode filter
            delay_filter moving_median
            delay_filter_length 10
            egressLatency 0
            ingressLatency 0
            boundary_clock_jbod 0
            #
            # Clock description
            #
            productDescription ;;
            revisionData ;;
            manufacturerIdentity 00:00:00
            userDescription ;
            timeSource 0xA0
      recommend:
        - profile: ordinary-clock
          priority: 4
          match:
            - nodeLabel: "node-role.kubernetes.io/$mcp"
    ```

    </div>

    | CR field | Description |
    |----|----|
    | `name` | The name of the `PtpConfig` CR. |
    | `profile` | Specify an array of one or more `profile` objects. Each profile must be uniquely named. |
    | `interface` | Specify the network interface to be used by the `ptp4l` service, for example `ens787f1`. |
    | `ptp4lOpts` | Specify system config options for the `ptp4l` service, for example `-2` to select the IEEE 802.3 network transport. The options should not include the network interface name `-i <interface>` and service config file `-f /etc/ptp4l.conf` because the network interface name and the service config file are automatically appended. Append `--summary_interval -4` to use PTP fast events with this interface. |
    | `phc2sysOpts` | Specify system config options for the `phc2sys` service. If this field is empty, the PTP Operator does not start the `phc2sys` service. For Intel Columbiaville 800 Series NICs, set `phc2sysOpts` options to `-a -r -m -n 24 -N 8 -R 16`. `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics. |
    | `ptp4lConf` | Specify a string that contains the configuration to replace the default `/etc/ptp4l.conf` file. To use the default configuration, leave the field empty. |
    | `tx_timestamp_timeout` | For Intel Columbiaville 800 Series NICs, set `tx_timestamp_timeout` to `50`. |
    | `boundary_clock_jbod` | For Intel Columbiaville 800 Series NICs, set `boundary_clock_jbod` to `0`. |
    | `ptpSchedulingPolicy` | Scheduling policy for `ptp4l` and `phc2sys` processes. Default value is `SCHED_OTHER`. Use `SCHED_FIFO` on systems that support FIFO scheduling. |
    | `ptpSchedulingPriority` | Integer value from 1-65 used to set FIFO priority for `ptp4l` and `phc2sys` processes when `ptpSchedulingPolicy` is set to `SCHED_FIFO`. The `ptpSchedulingPriority` field is not used when `ptpSchedulingPolicy` is set to `SCHED_OTHER`. |
    | `ptpClockThreshold` | Optional. If `ptpClockThreshold` is not present, default values are used for the `ptpClockThreshold` fields. `ptpClockThreshold` configures how long after the PTP master clock is disconnected before PTP events are triggered. `holdOverTimeout` is the time value in seconds before the PTP clock event state changes to `FREERUN` when the PTP master clock is disconnected. The `maxOffsetThreshold` and `minOffsetThreshold` settings configure offset values in nanoseconds that compare against the values for `CLOCK_REALTIME` (`phc2sys`) or master offset (`ptp4l`). When the `ptp4l` or `phc2sys` offset value is outside this range, the PTP clock state is set to `FREERUN`. When the offset value is within this range, the PTP clock state is set to `LOCKED`. |
    | `recommend` | Specify an array of one or more `recommend` objects that define rules on how the `profile` should be applied to nodes. |
    | `.recommend.profile` | Specify the `.recommend.profile` object name defined in the `profile` section. |
    | `.recommend.priority` | Set `.recommend.priority` to `0` for ordinary clock. |
    | `.recommend.match` | Specify `.recommend.match` rules with `nodeLabel` or `nodeName` values. |
    | `.recommend.match.nodeLabel` | Set `nodeLabel` with the `key` of the `node.Labels` field from the node object by using the `oc get nodes --show-labels` command. For example, `node-role.kubernetes.io/worker`. |
    | `.recommend.match.nodeName` | Set `nodeName` with the value of the `node.Name` field from the node object by using the `oc get nodes` command. For example, `compute-1.example.com`. |

    PTP ordinary clock CR configuration options

2.  Create the `PtpConfig` CR by running the following command:

    ``` terminal
    $ oc create -f ordinary-clock-ptp-config.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                            READY   STATUS    RESTARTS   AGE   IP               NODE
        linuxptp-daemon-4xkbb           1/1     Running   0          43m   10.1.196.24      compute-0.example.com
        linuxptp-daemon-tdspf           1/1     Running   0          43m   10.1.196.25      compute-1.example.com
        ptp-operator-657bbb64c8-2f8sj   1/1     Running   0          43m   10.129.0.61      control-plane-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile. Run the following command:

        ``` terminal
        $ oc logs linuxptp-daemon-4xkbb -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        I1115 09:41:17.117596 4143292 daemon.go:107] in applyNodePTPProfile
        I1115 09:41:17.117604 4143292 daemon.go:109] updating NodePTPProfile to:
        I1115 09:41:17.117607 4143292 daemon.go:110] ------------------------------------
        I1115 09:41:17.117612 4143292 daemon.go:102] Profile Name: profile1
        I1115 09:41:17.117616 4143292 daemon.go:102] Interface: ens787f1
        I1115 09:41:17.117620 4143292 daemon.go:102] Ptp4lOpts: -2 -s
        I1115 09:41:17.117623 4143292 daemon.go:102] Phc2sysOpts: -a -r -n 24
        I1115 09:41:17.117626 4143292 daemon.go:116] ------------------------------------
        ```

        </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring FIFO priority scheduling for PTP hardware](configuring-ptp.md#cnf-configuring-fifo-priority-scheduling-for-ptp_configuring-ptp)

- [Configuring the PTP fast event notifications publisher](ptp-cloud-events-consumer-dev-reference-v2.md#cnf-configuring-the-ptp-fast-event-publisher-v2_ptp-consumer)

</div>

## Intel Columbiaville E800 series NIC as PTP ordinary clock reference

The following table describes the changes that you must make to the reference PTP configuration to use Intel Columbiaville E800 series NICs as ordinary clocks. Make the changes in a `PtpConfig` custom resource (CR) that you apply to the cluster.

| PTP configuration      | Recommended setting         |
|------------------------|-----------------------------|
| `phc2sysOpts`          | `-a -r -m -n 24 -N 8 -R 16` |
| `tx_timestamp_timeout` | `50`                        |
| `boundary_clock_jbod`  | `0`                         |

Recommended PTP settings for Intel Columbiaville NIC

> [!NOTE]
> For `phc2sysOpts`, `-m` prints messages to `stdout`. The `linuxptp-daemon` `DaemonSet` parses the logs and generates Prometheus metrics.

## Configuring linuxptp services as an ordinary clock with dual-port NIC redundancy

You can configure `linuxptp` services (`ptp4l`, `phc2sys`) as an ordinary clock with dual-port NIC redundancy by creating a `PtpConfig` custom resource (CR) object.

In a dual-port NIC configuration for an ordinary clock, if one port fails, the standby port takes over, maintaining PTP timing synchronization.

> [!IMPORTANT]
> Configuring linuxptp services as an ordinary clock with dual-port NIC redundancy is a Technology Preview feature only. Technology Preview features are not supported with Red Hat production service level agreements (SLAs) and might not be functionally complete. Red Hat does not recommend using them in production. These features provide early access to upcoming product features, enabling customers to test functionality and provide feedback during the development process.
>
> For more information about the support scope of Red Hat Technology Preview features, see [Technology Preview Features Support Scope](https://access.redhat.com/support/offerings/techpreview/).

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

- Check the hardware requirements for using your dual-port NIC as an ordinary clock with added redundancy. For further information, see "Using dual-port NICs to improve redundancy for PTP ordinary clocks".

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create the following `PtpConfig` CR, and then save the YAML in the `oc-dual-port-ptp-config.yaml` file.

    <div class="formalpara">

    <div class="title">

    Example PTP ordinary clock dual-port configuration

    </div>

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: ordinary-clock-1
      namespace: openshift-ptp
    spec:
      profile:
      - name: oc-dual-port
        phc2sysOpts: -a -r -n 24 -N 8 -R 16 -u 0
        ptp4lConf: |-
          [ens3f2]
          masterOnly 0
          [ens3f3]
          masterOnly 0

          [global]
          #
          # Default Data Set
          #
          slaveOnly 1
    #...
    ```

    </div>

    where:

    `phc2sysOpts: -a -r -n 24 -N 8 -R 16 -u 0`
    Specifies the system config options for the `phc2sys` service.

    `ptp4lConf`
    Specifies the interface configuration for the `ptp4l` service. In this example, setting `masterOnly 0` for the `ens3f2` and `ens3f3` interfaces enables both ports on the `ens3` interface to run as leader or follower clocks. In combination with the `slaveOnly 1` specification, this configuration ensures one port operates as the active ordinary clock, and the other port operates as a standby ordinary clock in the `Listening` port state.

    `slaveOnly 1`
    Configures `ptp4l` to run as an ordinary clock only.

2.  Create the `PtpConfig` CR by running the following command:

    ``` terminal
    $ oc create -f oc-dual-port-ptp-config.yaml
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  Check that the `PtpConfig` profile is applied to the node.

    1.  Get the list of pods in the `openshift-ptp` namespace by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                            READY   STATUS    RESTARTS   AGE   IP               NODE
        linuxptp-daemon-4xkbb           1/1     Running   0          43m   10.1.196.24      compute-0.example.com
        linuxptp-daemon-tdspf           1/1     Running   0          43m   10.1.196.25      compute-1.example.com
        ptp-operator-657bbb64c8-2f8sj   1/1     Running   0          43m   10.129.0.61      control-plane-1.example.com
        ```

        </div>

    2.  Check that the profile is correct. Examine the logs of the `linuxptp` daemon that corresponds to the node you specified in the `PtpConfig` profile. Run the following command:

        ``` terminal
        $ oc logs linuxptp-daemon-4xkbb -n openshift-ptp -c linuxptp-daemon-container
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        I1115 09:41:17.117596 4143292 daemon.go:107] in applyNodePTPProfile
        I1115 09:41:17.117604 4143292 daemon.go:109] updating NodePTPProfile to:
        I1115 09:41:17.117607 4143292 daemon.go:110] ------------------------------------
        I1115 09:41:17.117612 4143292 daemon.go:102] Profile Name: oc-dual-port
        I1115 09:41:17.117616 4143292 daemon.go:102] Interface: ens787f1
        I1115 09:41:17.117620 4143292 daemon.go:102] Ptp4lOpts: -2 --summary_interval -4
        I1115 09:41:17.117623 4143292 daemon.go:102] Phc2sysOpts: -a -r -n 24 -N 8 -R 16 -u 0
        I1115 09:41:17.117626 4143292 daemon.go:116] ------------------------------------
        ```

        </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring linuxptp services as ordinary clock](configuring-ptp.md#configuring-linuxptp-services-as-ordinary-clock_configuring-ptp)

- [Using dual-port NICs to improve redundancy for PTP ordinary clocks](about-ptp.md#ptp-dual-ports-oc_about-ptp)

</div>

# Configuring FIFO priority scheduling for PTP hardware

In telco or other deployment types that require low latency performance, PTP daemon threads run in a constrained CPU footprint alongside the rest of the infrastructure components. By default, PTP threads run with the `SCHED_OTHER` policy. Under high load, these threads might not get the scheduling latency they require for error-free operation.

To mitigate against potential scheduling latency errors, you can configure the PTP Operator `linuxptp` services to allow threads to run with a `SCHED_FIFO` policy. If `SCHED_FIFO` is set for a `PtpConfig` CR, then `ptp4l` and `phc2sys` will run in the parent container under `chrt` with a priority set by the `ptpSchedulingPriority` field of the `PtpConfig` CR.

> [!NOTE]
> Setting `ptpSchedulingPolicy` is optional, and is only required if you are experiencing latency errors.

<div>

<div class="title">

Procedure

</div>

1.  Edit the `PtpConfig` CR profile:

    ``` terminal
    $ oc edit PtpConfig -n openshift-ptp
    ```

2.  Change the `ptpSchedulingPolicy` and `ptpSchedulingPriority` fields:

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: <ptp_config_name>
      namespace: openshift-ptp
    ...
    spec:
      profile:
      - name: "profile1"
    ...
        ptpSchedulingPolicy: SCHED_FIFO
        ptpSchedulingPriority: 10
    ```

    where:

    `ptpSchedulingPolicy: SCHED_FIFO`
    Sets the scheduling policy for `ptp4l` and `phc2sys` processes. Use `SCHED_FIFO` on systems that support FIFO scheduling.

    `ptpSchedulingPriority: 10`
    Sets the integer value 1-65 used to configure FIFO priority for `ptp4l` and `phc2sys` processes.

3.  Save and exit to apply the changes to the `PtpConfig` CR.

</div>

<div>

<div class="title">

Verification

</div>

1.  Get the name of the `linuxptp-daemon` pod and corresponding node where the `PtpConfig` CR has been applied:

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
    linuxptp-daemon-gmv2n           3/3     Running   0          1d17h   10.1.196.24   compute-0.example.com
    linuxptp-daemon-lgm55           3/3     Running   0          1d17h   10.1.196.25   compute-1.example.com
    ptp-operator-3r4dcvf7f4-zndk7   1/1     Running   0          1d7h    10.129.0.61   control-plane-1.example.com
    ```

    </div>

2.  Check that the `ptp4l` process is running with the updated `chrt` FIFO priority:

    ``` terminal
    $ oc -n openshift-ptp logs linuxptp-daemon-lgm55 -c linuxptp-daemon-container|grep chrt
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    I1216 19:24:57.091872 1600715 daemon.go:285] /bin/chrt -f 65 /usr/sbin/ptp4l -f /var/run/ptp4l.0.config -2  --summary_interval -4 -m
    ```

    </div>

</div>

# Configuring PTP log reduction

The `linuxptp-daemon` generates logs that you can use for debugging purposes. In telco or other deployment types that feature a limited storage capacity, these logs can add to the storage demand. Currently, the default logging rate is high, causing logs to rotate out in under 24 hours, which makes it difficult to track changes and identify problems.

You can achieve basic log reduction by configuring the `PtpConfig` custom resource (CR) to exclude log messages that report the master offset value. The master offset log message reports the difference between the clock of the current node and the master clock in nanoseconds. However, with this method, there is no summary status of filtered logs. The enhanced log reduction feature allows you to configure the logging rate of PTP logs. You can set a specific logging rate, which can help reduce the volume of logs generated by the `linuxptp-daemon` while still retaining essential information for troubleshooting. With the enhanced log reduction feature, you can also specify a threshold that still displays the offset logs if the offset is higher than that threshold.

## Configuring log filtering for PTP

Modify the `PtpConfig` custom resource (CR) to configure basic log filtering and exclude log messages that report the master offset value.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `PtpConfig` CR:

    ``` terminal
    $ oc edit PtpConfig -n openshift-ptp
    ```

2.  In `spec.profile`, add the `ptpSettings.logReduce` specification and set the value to `true`:

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: <ptp_config_name>
      namespace: openshift-ptp
    ...
    spec:
      profile:
      - name: "profile1"
    ...
        ptpSettings:
          logReduce: "true"
    ```

    > [!NOTE]
    > For debugging purposes, you can revert this specification to `False` to include the master offset messages.

3.  Save and exit to apply the changes to the `PtpConfig` CR.

</div>

<div>

<div class="title">

Verification

</div>

1.  Get the name of the `linuxptp-daemon` pod and corresponding node where the `PtpConfig` CR has been applied:

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
    linuxptp-daemon-gmv2n           3/3     Running   0          1d17h   10.1.196.24   compute-0.example.com
    linuxptp-daemon-lgm55           3/3     Running   0          1d17h   10.1.196.25   compute-1.example.com
    ptp-operator-3r4dcvf7f4-zndk7   1/1     Running   0          1d7h    10.129.0.61   control-plane-1.example.com
    ```

    </div>

2.  Verify that master offset messages are excluded from the logs by running the following command:

    ``` terminal
    $ oc -n openshift-ptp logs <linux_daemon_container> -c linuxptp-daemon-container | grep "master offset"
    ```

    - `<linux_daemon_container>` is the name of the `linuxptp-daemon` pod, for example `linuxptp-daemon-gmv2n`.

      When you configure the `logReduce` specification, this command does not report any instances of `master offset` in the logs of the `linuxptp` daemon.

</div>

## Configuring enhanced PTP log reduction

Basic log reduction effectively filters out frequent logs. However, if you want a periodic summary of the filtered logs, use the enhanced log reduction feature.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Edit the `PtpConfig` custom resource (CR):

    ``` terminal
    $ oc edit PtpConfig -n openshift-ptp
    ```

2.  Add the `ptpSettings.logReduce` specification in the `spec.profile` section, and set the value to `enhanced`:

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: <ptp_config_name>
      namespace: openshift-ptp
    ...
    spec:
      profile:
      - name: "profile1"
    ...
        ptpSettings:
          logReduce: "enhanced"
    ```

3.  Optional: Configure the interval for summary logs and a threshold in nanoseconds for the master offset logs. For example, to set the interval to 60 seconds and the threshold to 100 nanoseconds, add the `ptpSettings.logReduce` specification in the `spec.profile` section and set the value to `enhanced 60s 100`.

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: <ptp_config_name>
      namespace: openshift-ptp
    spec:
      profile:
      - name: "profile1"
        ptpSettings:
          logReduce: "enhanced 60s 100"
    ```

    - By default, the `linuxptp-daemon` is configured to generate summary logs every 30 seconds if no value is specified. In the example configuration, the daemon generates summary logs every 60 seconds and a threshold of 100 nanoseconds for the master offset logs is set. This means the daemon only produces summary logs at the specified interval. However, if your clock’s offset from the master exceeds plus or minus 100 nanoseconds, that specific log entry is recorded.

4.  Optional: To set the interval without a master offset threshold, configure the `logReduce` field to `enhanced 60s` in the YAML.

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: <ptp_config_name>
      namespace: openshift-ptp
    spec:
      profile:
      - name: "profile1"
        ptpSettings:
          logReduce: "enhanced 60s"
    ```

5.  Save and exit to apply the changes to the `PtpConfig` CR.

</div>

<div>

<div class="title">

Verification

</div>

1.  Get the name of the `linuxptp-daemon` pod and the corresponding node where the `PtpConfig` CR is applied by running the following command

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
    linuxptp-daemon-gmv2n           3/3     Running   0          1d17h   10.1.196.24   compute-0.example.com
    linuxptp-daemon-lgm55           3/3     Running   0          1d17h   10.1.196.25   compute-1.example.com
    ptp-operator-3r4dcvf7f4-zndk7   1/1     Running   0          1d7h    10.129.0.61   control-plane-1.example.com
    ```

    </div>

2.  Verify that master offset messages are excluded from the logs by running the following command:

    ``` terminal
    $ oc -n openshift-ptp logs <linux_daemon_container> -c linuxptp-daemon-container | grep "master offset"
    ```

    - `<linux_daemon_container>` is the name of the `linuxptp-daemon` pod, for example, `linuxptp-daemon-gmv2n`.

</div>

# Configuring GNSS failover to NTP for time synchronization continuity

Automatic failover from global navigation satellite system (GNSS) to Network Time Protocol (NTP) maintains time synchronization continuity when the primary signal is lost, ensuring system stability for telco operations.

Telco operators require time source redundancy to ensure time synchronization continuity and system stability.

OpenShift Container Platform provides automatic failover capabilities to maintain synchronization. The system utilizes GNSS (delivered by `phc2sys`) as the primary time source. To protect against primary signal loss, such as jamming or antenna failure, the system automatically transitions to the secondary time source, NTP delivered by `chronyd`. Upon signal recovery, the system automatically switches back to and resumes synchronization with `phc2sys`.

You can control the resilience of the time synchronization by setting the `ts2phc.holdover` parameter in seconds. This value dictates the maximum time the internal control algorithm can continue synchronizing the PHC after the main time of day (ToD) source such as a GNSS receiver is lost. The algorithm can only continue if it remains in a stable state (SERVO_LOCKED_STABLE). When the process exits this configured holdover period, it signifies an unrecoverable primary signal loss. The system then allows failover to a secondary source such as NTP.

## Creating a PTP Grandmaster configuration with GNSS failover

Configure a Precision Time Protocol (PTP) Telecom Grandmaster clock with automatic failover from global navigation satellite system (GNSS) to Network Time Protocol (NTP) when satellite signals are unavailable.

This procedure configures a T-GM (Telecom Grandmaster) clock that uses an Intel E810 Westport Channel NIC as the PTP grandmaster clock with GNSS to NTP failover capabilities.

<div>

<div class="title">

Prerequisites

</div>

- For T-GM clocks in production environments, install an Intel E810 Westport Channel NIC in the bare-metal cluster host.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify the PTP Operator installation by running the following command:

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    The output is similar to the following listing the PTP Operator pod and the `linuxptp-daemon` pods:

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE   IP              NODE                       NOMINATED NODE   READINESS GATES
    linuxptp-daemon-4xk9m           2/2     Running   0          15m   192.168.1.101   worker-0.cluster.local     <none>           <none>
    linuxptp-daemon-7bv2n           2/2     Running   0          15m   192.168.1.102   worker-1.cluster.local     <none>           <none>
    linuxptp-daemon-9cp4r           2/2     Running   0          15m   192.168.1.103   worker-2.cluster.local     <none>           <none>
    linuxptp-daemon-kw8h5           2/2     Running   0          15m   192.168.1.104   worker-3.cluster.local     <none>           <none>
    linuxptp-daemon-m3j7t           2/2     Running   0          15m   192.168.1.105   worker-4.cluster.local     <none>           <none>
    ptp-operator-75c77dbf86-xm9kl   1/1     Running   0          20m   10.129.0.45     master-1.cluster.local     <none>           <none>
    ```

    - `ptp-operator-*`: The PTP Operator pod (one instance in the cluster)

    - `linuxptp-daemon-*`: The linuxptp daemon pods. A daemon pod runs on each node that matches the PtpConfig profile. Each daemon pod should show `2/2` in the READY column, indicating both containers (`linuxptp-daemon-container` and `kube-rbac-proxy`) are running.

      > [!NOTE]
      > The number of `linuxptp-daemon` pods is determined by the node labels defined in the `PtpOperatorConfig` which controls the DaemonSet deployment. The PtpConfig profile matching, as shown in Step 4, only determines which specific PTP settings are applied on the running daemons. In this example, the operator configuration targets all 5 worker nodes. For single-node OpenShift clusters, you will see only one `linuxptp-daemon` pod, as the configuration targets only the control plane node which acts as the worker.

2.  Check which network interfaces support hardware timestamping by running the following command:

    ``` terminal
    $ oc get NodePtpDevice -n openshift-ptp -o yaml
    ```

    The output is similar to the following showing NodePtpDevice resources for nodes with PTP-capable network interfaces:

    ``` yaml
    apiVersion: v1
    items:
    - apiVersion: ptp.openshift.io/v1
      kind: NodePtpDevice
      metadata:
        name: worker-0.cluster.local
        namespace: openshift-ptp
      spec: {}
      status:
        devices:
        - name: ens7f0
          hwConfig:
            phcIndex: 0
        - name: ens7f1
          hwConfig:
            phcIndex: 1
    - apiVersion: ptp.openshift.io/v1
      kind: NodePtpDevice
      metadata:
        name: worker-1.cluster.local
        namespace: openshift-ptp
      spec: {}
      status:
        devices:
        - name: ens7f0
          hwConfig:
            phcIndex: 0
        - name: ens7f1
          hwConfig:
            phcIndex: 1
    kind: List
    metadata:
      resourceVersion: ""
    ```

    In this example output:

    - `ens7f0` and `ens7f1` are PTP-capable interfaces (Intel E810 NIC ports).

    - `phcIndex` indicates the PTP Hardware Clock number (maps to `/dev/ptp0`, `/dev/ptp1`, and so on).

      > [!NOTE]
      > The output shows one NodePtpDevice resource for each node with PTP-capable interfaces. In this example, five worker nodes have Intel E810 NICs. For single-node OpenShift clusters, you would see only one NodePtpDevice resource.

3.  The PTP profile uses node labels for matching. Check your machine config pool (MCP) to find the node labels by running the following command:

    ``` terminal
    $ oc get mcp
    ```

    The output is similar to the following:

    ``` terminal
    NAME     CONFIG                   UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
    master   rendered-master-a1b1**   True      False      False      3              3                   3                   0                    45d
    worker   rendered-worker-f6e5**   True      False      False      5              5                   5                   0                    45d
    ```

    > [!NOTE]
    > The CONFIG column shows a truncated hash of the rendered MachineConfig. In actual output, this will be a full 64-character hash such as `rendered-master-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`.

    - In this example, the `<MCP-name>` is `worker` for worker nodes and `master` for control plane nodes. Most T-GM deployments use worker nodes, so you would use `worker` as the `<MCP-name>`.

    - For single-node OpenShift clusters, the `<MCP-name>` is `master` (the worker MCP will show `MACHINECOUNT` of 0).

4.  Create a `PtpConfig` custom resource (CR) that configures the T-GM clock with GNSS to NTP failover. Save the following YAML configuration to a file named `ptp-config-gnss-ntp-failover.yaml`, replacing `<MCP-name>` with the name of your machine config pool from the previous step.

    ``` yaml
    # The grandmaster profile is provided for testing only
    # It is not installed on production clusters
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: grandmaster
      namespace: openshift-ptp
      annotations:
        ran.openshift.io/ztp-deploy-wave: "10"
    spec:
      profile:
      - name: "grandmaster"
        ptp4lOpts: "-2 --summary_interval -4"
        phc2sysOpts: -r -u 0 -m -N 8 -R 16 -s ens7f0 -n 24
        ptpSchedulingPolicy: SCHED_FIFO
        ptpSchedulingPriority: 10
        ptpSettings:
          logReduce: "true"

        # --- FAILOVER CONFIGURATION ---
        # Holdover time: 14400 seconds (4 hours) before switching to NTP
        ts2phcOpts: "--ts2phc.holdover 14400"

        # Configure Chronyd (Secondary Time Source)
        chronydOpts: "-d"
        chronydConf: |
          server time.nist.gov iburst
          makestep 1.0 -1
          pidfile /var/run/chronyd.pid

        plugins:
          # E810 Hardware-Specific Configuration
          e810:
            enableDefaultConfig: false
            settings:
              LocalHoldoverTimeout: 14400
              LocalMaxHoldoverOffSet: 1500
              MaxInSpecOffset: 1500
            pins:
              # Syntax guide:
              # - The 1st number in each pair must be one of:
              #    0 - Disabled
              #    1 - RX
              #    2 - TX
              # - The 2nd number in each pair must match the channel number
              ens7f0:
                SMA1: 0 1
                SMA2: 0 2
                U.FL1: 0 1
                U.FL2: 0 2
            ublxCmds:
              - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                  - "-P"
                  - "29.20"
                  - "-z"
                  - "CFG-HW-ANT_CFG_VOLTCTRL,1"
                reportOutput: false
              - args: #ubxtool -P 29.20 -e GPS
                  - "-P"
                  - "29.20"
                  - "-e"
                  - "GPS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d Galileo
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "Galileo"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d GLONASS
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "GLONASS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d BeiDou
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "BeiDou"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d SBAS
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "SBAS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                  - "-P"
                  - "29.20"
                  - "-t"
                  - "-w"
                  - "5"
                  - "-v"
                  - "1"
                  - "-e"
                  - "SURVEYIN,600,50000"
                reportOutput: true
              - args: #ubxtool -P 29.20 -p MON-HW
                  - "-P"
                  - "29.20"
                  - "-p"
                  - "MON-HW"
                reportOutput: true
              - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                  - "-P"
                  - "29.20"
                  - "-p"
                  - "CFG-MSG,1,38,248"
                reportOutput: true

          # NTP Failover Plugin
          ntpfailover:
            gnssFailover: true

        # --- GNSS (ts2phc) CONFIGURATION (Primary Source) ---
        ts2phcConf: |
          [nmea]
          ts2phc.master 1
          [global]
          use_syslog  0
          verbose 1
          logging_level 7
          ts2phc.pulsewidth 100000000
          ts2phc.nmea_serialport /dev/ttyGNSS_1700_0
          leapfile  /usr/share/zoneinfo/leap-seconds.list
          [ens7f0]
          ts2phc.extts_polarity rising
          ts2phc.extts_correction 0

        # --- PTP4L CONFIGURATION (Grandmaster Role) ---
        ptp4lConf: |
          [ens7f0]
          masterOnly 1
          [ens7f1]
          masterOnly 1
          [global]
          #
          # Default Data Set
          #
          twoStepFlag 1
          priority1 128
          priority2 128
          domainNumber 24
          #utc_offset 37
          clockClass 6
          clockAccuracy 0x27
          offsetScaledLogVariance 0xFFFF
          free_running 0
          freq_est_interval 1
          dscp_event 0
          dscp_general 0
          dataset_comparison G.8275.x
          G.8275.defaultDS.localPriority 128
          #
          # Port Data Set
          #
          logAnnounceInterval -3
          logSyncInterval -4
          logMinDelayReqInterval -4
          logMinPdelayReqInterval 0
          announceReceiptTimeout 3
          syncReceiptTimeout 0
          delayAsymmetry 0
          fault_reset_interval -4
          neighborPropDelayThresh 20000000
          masterOnly 0
          G.8275.portDS.localPriority 128
          #
          # Run time options
          #
          assume_two_step 0
          logging_level 6
          path_trace_enabled 0
          follow_up_info 0
          hybrid_e2e 0
          inhibit_multicast_service 0
          net_sync_monitor 0
          tc_spanning_tree 0
          tx_timestamp_timeout 50
          unicast_listen 0
          unicast_master_table 0
          unicast_req_duration 3600
          use_syslog 1
          verbose 0
          summary_interval -4
          kernel_leap 1
          check_fup_sync 0
          clock_class_threshold 7
          #
          # Servo Options
          #
          pi_proportional_const 0.0
          pi_integral_const 0.0
          pi_proportional_scale 0.0
          pi_proportional_exponent -0.3
          pi_proportional_norm_max 0.7
          pi_integral_scale 0.0
          pi_integral_exponent 0.4
          pi_integral_norm_max 0.3
          step_threshold 2.0
          first_step_threshold 0.00002
          clock_servo pi
          sanity_freq_limit  200000000
          ntpshm_segment 0
          #
          # Transport options
          #
          transportSpecific 0x0
          ptp_dst_mac 01:1B:19:00:00:00
          p2p_dst_mac 01:80:C2:00:00:0E
          udp_ttl 1
          udp6_scope 0x0E
          uds_address /var/run/ptp4l
          #
          # Default interface options
          #
          clock_type BC
          network_transport L2
          delay_mechanism E2E
          time_stamping hardware
          tsproc_mode filter
          delay_filter moving_median
          delay_filter_length 10
          egressLatency 0
          ingressLatency 0
          boundary_clock_jbod 0
          #
          # Clock description
          #
          productDescription ;;
          revisionData ;;
          manufacturerIdentity 00:00:00
          userDescription ;
          timeSource 0x20
        ptpClockThreshold:
          holdOverTimeout: 5
          maxOffsetThreshold: 100
          minOffsetThreshold: -100
      recommend:
      - profile: "grandmaster"
        priority: 4
        match:
        - nodeLabel: node-role.kubernetes.io/<MCP-name>
    ```

    > [!IMPORTANT]
    > Replace the example interface names (`ens7f0`, `ens7f1`) with your actual E810 NIC interface names found in step 2. Common E810 interface naming patterns include `ens7f0`, `ens8f0`, `eth0`, `enp2s0f0`, and so on. The exact name depends on your system firmware settings and Linux network device naming conventions. Also replace `/dev/ttyGNSS_1700_0` with your actual GNSS serial port device path. For single-node OpenShift clusters, replace `<MCP-name>` with `master` in the nodeLabel match. For multi-node clusters using worker nodes as T-GM, use `worker`.

    The configuration includes the following components:

    - **PTP4L options:**

      - `-2`: Use PTP version 2

      - `--summary_interval -4`: Log summary every 2^(-4) = 0.0625 seconds

    - **PHC2SYS options:**

      - `-r`: Synchronize system clock from PTP hardware clock

      - `-u 0`: Update rate multiplier

      - `-m`: Print messages to stdout

      - `-N 8`: Domain number for ptp4l

      - `-R 16`: Update rate

      - `-s ens7f0`: Source interface (replace with your E810 interface name)

      - `-n 24`: Domain number

    - **Failover configuration:**

      - `ts2phcOpts --ts2phc.holdover 14400`: 4-hour holdover before switching to NTP

      - `chronydConf`: NTP server configuration for failover replace `time.nist.gov` with your preferred NTP server

      - `ntpfailover plugin`: Enables automatic GNSS-to-NTP switching with `gnssFailover: true`

    - **E810 plugin configuration:**

      - `LocalHoldoverTimeout: 14400`: E810 hardware holdover timeout (4 hours)

      - `pins`: Configuration for 1PPS input on E810 physical pins (U.FL2, SMA1, SMA2, U.FL1)

      - `ublxCmds`: Commands to configure u-blox GNSS receiver (enable GPS, disable other constellations, set survey-in mode)

    - **GNSS (ts2phc) configuration:**

      - `ts2phc.nmea_serialport /dev/ttyGNSS_1700_0`: GNSS serial port device path (replace with your actual GNSS device)

      - `ts2phc.extts_polarity rising`: 1PPS signal on rising edge

      - `ts2phc.pulsewidth 100000000`: 1PPS pulse width in nanoseconds

    - **PTP4L configuration:**

      - `masterOnly 1`: Interface acts only as PTP master

      - `clockClass 6`: GPS-synchronized quality level

      - `domainNumber 24`: PTP domain

      - `clock_type BC`: Boundary Clock mode

      - `time_stamping hardware`: Use hardware timestamps from E810 NIC

5.  Apply the `PtpConfig` CR by running the following command:

    ``` terminal
    $ oc apply -f ptp-config-gnss-ntp-failover.yaml
    ```

    The output is similar to the following:

    ``` terminal
    ptpconfig.ptp.openshift.io/grandmaster created
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  The PTP daemon checks for profile updates every 30 seconds. Wait approximately 30 seconds, then verify by running the following command:

    ``` terminal
    $ oc get ptpconfig -n openshift-ptp
    ```

    The output is similar to the following:

    ``` terminal
    NAME           AGE
    grandmaster    2m
    ```

2.  Check the NodePtpDevice to see if the profile is applied by running the following command, replacing `<node_name>` with your node hostname:

    ``` terminal
    $ oc describe nodeptpdevice <node_name> -n openshift-ptp
    ```

    For example, on a multi-node cluster with worker nodes: `worker-0.cluster.local`

    For single-node OpenShift clusters, use the control plane node name, which you can find by running:

    ``` terminal
    $ oc get nodes
    ```

3.  Check if the profile is being loaded by monitoring the daemon logs:

    ``` terminal
    $ oc get pods -n openshift-ptp | grep linuxptp-daemon
    ```

    Then check the logs, replacing `<linuxptp-daemon-pod>` with the actual pod name from the previous command:

    ``` terminal
    $ oc logs -n openshift-ptp <linuxptp-daemon-pod> -c linuxptp-daemon-container --tail=100
    ```

    Success indicators in the logs are:

    - `load profiles` - Profile is being loaded

    - `in applyNodePTPProfiles` - Profile is being applied

    - No `ptp profile doesn’t exist for node` errors

4.  Check `chronyd` status to verify NTP is running as the secondary time source by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp <linuxptp-daemon-pod> -c linuxptp-daemon-container | grep chronyd
    ```

    The output is similar to the following:

    ``` terminal
    chronyd version 4.5 starting
    Added source ID#0000000001 (time.nist.gov)
    ```

5.  Check GNSS/gpsd by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp <linuxptp-daemon-pod> -c linuxptp-daemon-container | grep gpsd
    ```

    The output shows the following when GNSS is functioning correctly:

    - `gpsd` starting successfully

    - No `No such file or directory` errors exist

6.  Check `ts2phc` (GNSS synchronization) status by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp <linuxptp-daemon-pod> -c linuxptp-daemon-container | grep ts2phc
    ```

7.  Check `phc2sys` (system clock sync) status by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp <linuxptp-daemon-pod> -c linuxptp-daemon-container | grep phc2sys
    ```

    The output shows synchronization status messages for `phc2sys`.

    ``` terminal
    phc2sys[xxx]: CLOCK_REALTIME phc offset -17 s2 freq -13865 delay 2305
    ```

</div>

## Creating a PTP Grandmaster configuration with GNSS failover on Single Node OpenShift

This procedure configures a T-GM (Telecom Grandmaster) clock on single-node OpenShift that uses an Intel E810 Westport Channel NIC as the PTP grandmaster clock with GNSS to NTP failover capabilities.

<div>

<div class="title">

Prerequisites

</div>

- For T-GM clocks in production environments, install an Intel E810 Westport Channel NIC in the bare metal single-node OpenShift host.

- Install the OpenShift CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify the PTP Operator installation by running the following command:

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    The output is similar to the following listing the PTP Operator pod and the single `linuxptp-daemon` pod:

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE   IP              NODE                   NOMINATED NODE   READINESS GATES
    linuxptp-daemon-xz8km           2/2     Running   0          15m   192.168.1.50    mysno-sno.demo.lab     <none>           <none>
    ptp-operator-75c77dbf86-xm9kl   1/1     Running   0          20m   10.129.0.45     mysno-sno.demo.lab     <none>           <none>
    ```

    - `ptp-operator-*`: The PTP Operator pod (one instance in the cluster).

    - `linuxptp-daemon-*`: The linuxptp daemon pod. On single-node OpenShift, there is only one daemon pod running on the master node. The daemon pod should show `2/2` in the READY column, indicating both containers (`linuxptp-daemon-container` and `kube-rbac-proxy`) are running.

2.  Check which network interfaces support hardware timestamping by running the following command:

    ``` terminal
    $ oc get NodePtpDevice -n openshift-ptp -o yaml
    ```

    The output is similar to the following one, showing the NodePtpDevice resource for the single-node OpenShift node with PTP-capable network interfaces:

    ``` yaml
    apiVersion: v1
    items:
    - apiVersion: ptp.openshift.io/v1
      kind: NodePtpDevice
      metadata:
        name: mysno-sno.demo.lab
        namespace: openshift-ptp
      spec: {}
      status:
        devices:
        - name: ens7f0
          hwConfig:
            phcIndex: 0
        - name: ens7f1
          hwConfig:
            phcIndex: 1
    kind: List
    metadata:
      resourceVersion: ""
    ```

    In this example output:

    - `ens7f0` and `ens7f1` are PTP-capable interfaces (Intel E810 NIC ports).

    - `phcIndex` indicates the PTP Hardware Clock number (maps to `/dev/ptp0`, `/dev/ptp1`, etc.)

      > [!NOTE]
      > On single-node OpenShift clusters, you will see only one NodePtpDevice resource for the single master node.

3.  The PTP profile uses node labels for matching. Check your machine config pool (MCP) to verify the master MCP by running the following command:

    ``` terminal
    $ oc get mcp
    ```

    The output is similar to the following:

    ``` terminal
    NAME     CONFIG                  UPDATED   UPDATING   DEGRADED   MACHINECOUNT   READYMACHINECOUNT   UPDATEDMACHINECOUNT DEGRADEDMACHINECOUNT AGE
    master   rendered-master-a1b1*   True      False      False      1              1                   1                   0                    45d
    worker   rendered-worker-f6e5*   True      False      False      0              0                   0                   0                    45d
    ```

    > [!NOTE]
    > The CONFIG column shows a truncated hash of the rendered MachineConfig. In actual output, this will be a full 64-character hash like `rendered-master-a1b2c3d4e5f6a7b8c9d0e1f2a3b4c5d6`.

    On single-node OpenShift clusters, the master MCP shows `MACHINECOUNT` of 1 (the single node), and the worker MCP shows `MACHINECOUNT` of 0. The PTP profile must target the `master` node label.

4.  Create a `PtpConfig` custom resource (CR) that configures the T-GM clock with GNSS to NTP failover. Save the following YAML configuration to a file named `ptp-config-gnss-ntp-failover-sno.yaml`.

    ``` yaml
    # The grandmaster profile is provided for testing only
    # It is not installed on production clusters
    apiVersion: ptp.openshift.io/v1
    kind: PtpConfig
    metadata:
      name: grandmaster
      namespace: openshift-ptp
      annotations:
        ran.openshift.io/ztp-deploy-wave: "10"
    spec:
      profile:
      - name: "grandmaster"
        ptp4lOpts: "-2 --summary_interval -4"
        phc2sysOpts: -r -u 0 -m -N 8 -R 16 -s ens7f0 -n 24
        ptpSchedulingPolicy: SCHED_FIFO
        ptpSchedulingPriority: 10
        ptpSettings:
          logReduce: "true"

        # --- FAILOVER CONFIGURATION ---
        # Holdover time: 14400 seconds (4 hours) before switching to NTP
        ts2phcOpts: "--ts2phc.holdover 14400"

        # Configure Chronyd (Secondary Time Source)
        chronydOpts: "-d"
        chronydConf: |
          server time.nist.gov iburst
          makestep 1.0 -1
          pidfile /var/run/chronyd.pid

        plugins:
          # E810 Hardware-Specific Configuration
          e810:
            enableDefaultConfig: false
            settings:
              LocalHoldoverTimeout: 14400
              LocalMaxHoldoverOffSet: 1500
              MaxInSpecOffset: 1500
            pins:
              # Syntax guide:
              # - The 1st number in each pair must be one of:
              #    0 - Disabled
              #    1 - RX
              #    2 - TX
              # - The 2nd number in each pair must match the channel number
              ens7f0:
                SMA1: 0 1
                SMA2: 0 2
                U.FL1: 0 1
                U.FL2: 0 2
            ublxCmds:
              - args: #ubxtool -P 29.20 -z CFG-HW-ANT_CFG_VOLTCTRL,1
                  - "-P"
                  - "29.20"
                  - "-z"
                  - "CFG-HW-ANT_CFG_VOLTCTRL,1"
                reportOutput: false
              - args: #ubxtool -P 29.20 -e GPS
                  - "-P"
                  - "29.20"
                  - "-e"
                  - "GPS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d Galileo
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "Galileo"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d GLONASS
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "GLONASS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d BeiDou
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "BeiDou"
                reportOutput: false
              - args: #ubxtool -P 29.20 -d SBAS
                  - "-P"
                  - "29.20"
                  - "-d"
                  - "SBAS"
                reportOutput: false
              - args: #ubxtool -P 29.20 -t -w 5 -v 1 -e SURVEYIN,600,50000
                  - "-P"
                  - "29.20"
                  - "-t"
                  - "-w"
                  - "5"
                  - "-v"
                  - "1"
                  - "-e"
                  - "SURVEYIN,600,50000"
                reportOutput: true
              - args: #ubxtool -P 29.20 -p MON-HW
                  - "-P"
                  - "29.20"
                  - "-p"
                  - "MON-HW"
                reportOutput: true
              - args: #ubxtool -P 29.20 -p CFG-MSG,1,38,248
                  - "-P"
                  - "29.20"
                  - "-p"
                  - "CFG-MSG,1,38,248"
                reportOutput: true

          # NTP Failover Plugin
          ntpfailover:
            gnssFailover: true

        # --- GNSS (ts2phc) CONFIGURATION (Primary Source) ---
        ts2phcConf: |
          [nmea]
          ts2phc.master 1
          [global]
          use_syslog  0
          verbose 1
          logging_level 7
          ts2phc.pulsewidth 100000000
          ts2phc.nmea_serialport /dev/ttyGNSS_1700_0
          leapfile  /usr/share/zoneinfo/leap-seconds.list
          [ens7f0]
          ts2phc.extts_polarity rising
          ts2phc.extts_correction 0

        # --- PTP4L CONFIGURATION (Grandmaster Role) ---
        ptp4lConf: |
          [ens7f0]
          masterOnly 1
          [ens7f1]
          masterOnly 1
          [global]
          #
          # Default Data Set
          #
          twoStepFlag 1
          priority1 128
          priority2 128
          domainNumber 24
          #utc_offset 37
          clockClass 6
          clockAccuracy 0x27
          offsetScaledLogVariance 0xFFFF
          free_running 0
          freq_est_interval 1
          dscp_event 0
          dscp_general 0
          dataset_comparison G.8275.x
          G.8275.defaultDS.localPriority 128
          #
          # Port Data Set
          #
          logAnnounceInterval -3
          logSyncInterval -4
          logMinDelayReqInterval -4
          logMinPdelayReqInterval 0
          announceReceiptTimeout 3
          syncReceiptTimeout 0
          delayAsymmetry 0
          fault_reset_interval -4
          neighborPropDelayThresh 20000000
          masterOnly 0
          G.8275.portDS.localPriority 128
          #
          # Run time options
          #
          assume_two_step 0
          logging_level 6
          path_trace_enabled 0
          follow_up_info 0
          hybrid_e2e 0
          inhibit_multicast_service 0
          net_sync_monitor 0
          tc_spanning_tree 0
          tx_timestamp_timeout 50
          unicast_listen 0
          unicast_master_table 0
          unicast_req_duration 3600
          use_syslog 1
          verbose 0
          summary_interval -4
          kernel_leap 1
          check_fup_sync 0
          clock_class_threshold 7
          #
          # Servo Options
          #
          pi_proportional_const 0.0
          pi_integral_const 0.0
          pi_proportional_scale 0.0
          pi_proportional_exponent -0.3
          pi_proportional_norm_max 0.7
          pi_integral_scale 0.0
          pi_integral_exponent 0.4
          pi_integral_norm_max 0.3
          step_threshold 2.0
          first_step_threshold 0.00002
          clock_servo pi
          sanity_freq_limit  200000000
          ntpshm_segment 0
          #
          # Transport options
          #
          transportSpecific 0x0
          ptp_dst_mac 01:1B:19:00:00:00
          p2p_dst_mac 01:80:C2:00:00:0E
          udp_ttl 1
          udp6_scope 0x0E
          uds_address /var/run/ptp4l
          #
          # Default interface options
          #
          clock_type BC
          network_transport L2
          delay_mechanism E2E
          time_stamping hardware
          tsproc_mode filter
          delay_filter moving_median
          delay_filter_length 10
          egressLatency 0
          ingressLatency 0
          boundary_clock_jbod 0
          #
          # Clock description
          #
          productDescription ;;
          revisionData ;;
          manufacturerIdentity 00:00:00
          userDescription ;
          timeSource 0x20
        ptpClockThreshold:
          holdOverTimeout: 5
          maxOffsetThreshold: 100
          minOffsetThreshold: -100
      recommend:
      - profile: "grandmaster"
        priority: 4
        match:
        - nodeLabel: node-role.kubernetes.io/master
    ```

    > [!IMPORTANT]
    > Replace the example interface names (`ens7f0`, `ens7f1`) with your actual E810 NIC interface names found in step 2. Common E810 interface naming patterns include `ens7f0`, `ens8f0`, `eth0`, `enp2s0f0`, and so on. The exact name depends on your system BIOS settings and Linux network device naming conventions. Also, replace `/dev/ttyGNSS_1700_0` with your actual GNSS serial port device path. The `nodeLabel` is set to `node-role.kubernetes.io/master` to target the single-node OpenShift master node which serves all roles.

    The configuration includes the following components:

    - **PTP4L options**:

      - `-2`: Use PTP version 2

      - `--summary_interval -4`: Log summary every 2^(-4) = 0.0625 seconds

    - **PHC2SYS options:**

      - `-r`: Synchronize system clock from PTP hardware clock

      - `-u 0`: Update rate multiplier

      - `-m`: Print messages to stdout

      - `-N 8`: Domain number for ptp4l

      - `-R 16`: Update rate

      - `-s ens7f0`: Source interface (replace with your E810 interface name)

      - `-n 24`: Domain number

    - **Failover configuration:**

      - `ts2phcOpts --ts2phc.holdover 14400`: 4-hour holdover before switching to NTP

      - `chronydConf`: NTP server configuration for failover replace `time.nist.gov` with your preferred NTP server

      - `ntpfailover plugin`: Enables automatic GNSS-to-NTP switching with `gnssFailover: true`.

    - **E810 plugin configuration:**

      - `LocalHoldoverTimeout: 14400`: E810 hardware holdover timeout (4 hours)

      - `pins`: Configuration for 1PPS input on E810 physical pins (U.FL2, SMA1, SMA2, U.FL1)

      - `ublxCmds`: Commands to configure u-blox GNSS receiver (enable GPS, disable other constellations, set survey-in mode)

    - **GNSS (ts2phc) configuration:**

      - `ts2phc.nmea_serialport /dev/ttyGNSS_1700_0`: GNSS serial port device path (replace with your actual GNSS device)

      - `ts2phc.extts_polarity rising`: 1PPS signal on rising edge

      - `ts2phc.pulsewidth 100000000`: 1PPS pulse width in nanoseconds

    - **PTP4L configuration:**

      - `masterOnly 1`: Interface acts only as PTP master

      - `clockClass 6`: GPS-synchronized quality level

      - `domainNumber 24`: PTP domain

      - `clock_type BC`: Boundary Clock mode

      - `time_stamping hardware`: Use hardware timestamps from E810 NIC

5.  Apply the `PtpConfig` CR by running the following command:

    ``` terminal
    $ oc apply -f ptp-config-gnss-ntp-failover-sno.yaml
    ```

    The output is similar to the following:

    ``` terminal
    ptpconfig.ptp.openshift.io/grandmaster created
    ```

</div>

<div>

<div class="title">

Verification

</div>

1.  The PTP daemon checks for profile updates every 30 seconds. Wait approximately 30 seconds, then verify by running the following command:

    ``` terminal
    $ oc get ptpconfig -n openshift-ptp
    ```

    The output is similar to the following:

    ``` terminal
    NAME           AGE
    grandmaster    2m
    ```

2.  Check the NodePtpDevice to see if the profile is applied. First, get your single-node OpenShift node name:

    ``` terminal
    $ oc get nodes
    ```

    The output is similar to the following:

    ``` terminal
    NAME                 STATUS   ROLES                         AGE     VERSION
    mysno-sno.demo.lab   Ready    control-plane,master,worker   4h19m   v1.34.1
    ```

    Then describe the NodePtpDevice using your node name:

    ``` terminal
    $ oc describe nodeptpdevice mysno-sno.demo.lab -n openshift-ptp
    ```

3.  Check if the profile is being loaded by monitoring the daemon logs. First, get the daemon pod name:

    ``` terminal
    $ oc get pods -n openshift-ptp | grep linuxptp-daemon
    ```

    The output shows the single linuxptp-daemon pod:

    ``` terminal
    linuxptp-daemon-xz8km           2/2     Running   0          15m
    ```

    Then check the logs using the pod name:

    ``` terminal
    $ oc logs -n openshift-ptp linuxptp-daemon-xz8km -c linuxptp-daemon-container --tail=100
    ```

    Success indicators in the logs are:

    - `load profiles` - Profile is being loaded

    - `in applyNodePTPProfiles` - Profile is being applied

    - No `ptp profile doesn’t exist for node` errors

4.  Check `chronyd` status to verify NTP is running as the secondary time source by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp linuxptp-daemon-xz8km -c linuxptp-daemon-container | grep chronyd
    ```

    The output is similar to the following:

    ``` terminal
    chronyd version 4.5 starting
    Added source ID#0000000001 (time.nist.gov)
    ```

5.  Check GNSS/gpsd by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp linuxptp-daemon-xz8km -c linuxptp-daemon-container | grep gpsd
    ```

    The output shows the following when GNSS is functioning correctly:

    - `gpsd` starting successfully

    - No `No such file or directory` errors exist

6.  Check `ts2phc` (GNSS synchronization) status by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp linuxptp-daemon-xz8km -c linuxptp-daemon-container | grep ts2phc
    ```

7.  Check `phc2sys` (system clock sync) status by running the following command:

    ``` terminal
    $ oc logs -n openshift-ptp linuxptp-daemon-xz8km -c linuxptp-daemon-container | grep phc2sys
    ```

    The output shows synchronization status messages for `phc2sys`.

    ``` terminal
    phc2sys[xxx]: CLOCK_REALTIME phc offset -17 s2 freq -13865 delay 2305
    ```

</div>

# Troubleshooting common PTP Operator issues

Troubleshoot common problems with the PTP Operator by performing the following steps.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift Container Platform CLI (`oc`).

- Log in as a user with `cluster-admin` privileges.

- Install the PTP Operator on a bare-metal cluster with hosts that support PTP.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Check the Operator and operands are successfully deployed in the cluster for the configured nodes.

    ``` terminal
    $ oc get pods -n openshift-ptp -o wide
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
    linuxptp-daemon-lmvgn           3/3     Running   0          4d17h   10.1.196.24   compute-0.example.com
    linuxptp-daemon-qhfg7           3/3     Running   0          4d17h   10.1.196.25   compute-1.example.com
    ptp-operator-6b8dcbf7f4-zndk7   1/1     Running   0          5d7h    10.129.0.61   control-plane-1.example.com
    ```

    </div>

    > [!NOTE]
    > When the PTP fast event bus is enabled, the number of ready `linuxptp-daemon` pods is `3/3`. If the PTP fast event bus is not enabled, `2/2` is displayed.

2.  Check that supported hardware is found in the cluster.

    ``` terminal
    $ oc -n openshift-ptp get nodeptpdevices.ptp.openshift.io
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                                  AGE
    control-plane-0.example.com           10d
    control-plane-1.example.com           10d
    compute-0.example.com                 10d
    compute-1.example.com                 10d
    compute-2.example.com                 10d
    ```

    </div>

3.  Check the available PTP network interfaces for a node:

    ``` terminal
    $ oc -n openshift-ptp get nodeptpdevices.ptp.openshift.io <node_name> -o yaml
    ```

    where:

    \<node_name\>
    Specifies the node you want to query, for example, `compute-0.example.com`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` yaml
    apiVersion: ptp.openshift.io/v1
    kind: NodePtpDevice
    metadata:
      creationTimestamp: "2021-09-14T16:52:33Z"
      generation: 1
      name: compute-0.example.com
      namespace: openshift-ptp
      resourceVersion: "177400"
      uid: 30413db0-4d8d-46da-9bef-737bacd548fd
    spec: {}
    status:
      devices:
      - name: eno1
      - name: eno2
      - name: eno3
      - name: eno4
      - name: enp5s0f0
      - name: enp5s0f1
    ```

    </div>

4.  Check that the PTP interface is successfully synchronized to the primary clock by accessing the `linuxptp-daemon` pod for the corresponding node.

    1.  Get the name of the `linuxptp-daemon` pod and corresponding node you want to troubleshoot by running the following command:

        ``` terminal
        $ oc get pods -n openshift-ptp -o wide
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME                            READY   STATUS    RESTARTS   AGE     IP            NODE
        linuxptp-daemon-lmvgn           3/3     Running   0          4d17h   10.1.196.24   compute-0.example.com
        linuxptp-daemon-qhfg7           3/3     Running   0          4d17h   10.1.196.25   compute-1.example.com
        ptp-operator-6b8dcbf7f4-zndk7   1/1     Running   0          5d7h    10.129.0.61   control-plane-1.example.com
        ```

        </div>

    2.  Remote shell into the required `linuxptp-daemon` container:

        ``` terminal
        $ oc rsh -n openshift-ptp -c linuxptp-daemon-container <linux_daemon_container>
        ```

        where:

        \<linux_daemon_container\>
        is the container you want to diagnose, for example `linuxptp-daemon-lmvgn`.

    3.  In the remote shell connection to the `linuxptp-daemon` container, use the PTP Management Client (`pmc`) tool to diagnose the network interface. Run the following `pmc` command to check the sync status of the PTP device, for example `ptp4l`.

        ``` terminal
        # pmc -u -f /var/run/ptp4l.0.config -b 0 'GET PORT_DATA_SET'
        ```

        <div class="formalpara">

        <div class="title">

        Example output when the node is successfully synced to the primary clock

        </div>

        ``` terminal
        sending: GET PORT_DATA_SET
            40a6b7.fffe.166ef0-1 seq 0 RESPONSE MANAGEMENT PORT_DATA_SET
                portIdentity            40a6b7.fffe.166ef0-1
                portState               SLAVE
                logMinDelayReqInterval  -4
                peerMeanPathDelay       0
                logAnnounceInterval     -3
                announceReceiptTimeout  3
                logSyncInterval         -4
                delayMechanism          1
                logMinPdelayReqInterval -4
                versionNumber           2
        ```

        </div>

5.  For GNSS-sourced grandmaster clocks, verify that the in-tree NIC ice driver is correct by running the following command, for example:

    ``` terminal
    $ oc rsh -n openshift-ptp -c linuxptp-daemon-container linuxptp-daemon-74m2g ethtool -i ens7f0
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    driver: ice
    version: 5.14.0-356.bz2232515.el9.x86_64
    firmware-version: 4.20 0x8001778b 1.3346.0
    ```

    </div>

6.  For GNSS-sourced grandmaster clocks, verify that the `linuxptp-daemon` container is receiving signal from the GNSS antenna. If the container is not receiving the GNSS signal, the `/dev/gnss0` file is not populated. To verify, run the following command:

    ``` terminal
    $ oc rsh -n openshift-ptp -c linuxptp-daemon-container linuxptp-daemon-jnz6r cat /dev/gnss0
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    $GNRMC,125223.00,A,4233.24463,N,07126.64561,W,0.000,,300823,,,A,V*0A
    $GNVTG,,T,,M,0.000,N,0.000,K,A*3D
    $GNGGA,125223.00,4233.24463,N,07126.64561,W,1,12,99.99,98.6,M,-33.1,M,,*7E
    $GNGSA,A,3,25,17,19,11,12,06,05,04,09,20,,,99.99,99.99,99.99,1*37
    $GPGSV,3,1,10,04,12,039,41,05,31,222,46,06,50,064,48,09,28,064,42,1*62
    ```

    </div>

</div>

# Getting the DPLL firmware version for the CGU in an Intel 800 series NIC

You can get the digital phase-locked loop (DPLL) firmware version for the Clock Generation Unit (CGU) in an Intel 800 series NIC by opening a debug shell to the cluster node and querying the NIC hardware.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`).

- You have logged in as a user with `cluster-admin` privileges.

- You have installed an Intel 800 series NIC in the cluster host.

- You have installed the PTP Operator on a bare-metal cluster with hosts that support PTP.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Start a debug pod by running the following command:

    ``` terminal
    $ oc debug node/<node_name>
    ```

    where:

    \<node_name\>
    Is the node where you have installed the Intel 800 series NIC.

2.  Check the CGU firmware version in the NIC by using the `devlink` tool and the bus and device name where the NIC is installed. For example, run the following command:

    ``` terminal
    sh-4.4# devlink dev info <bus_name>/<device_name> | grep cgu
    ```

    where:

    \<bus_name\>
    Is the bus where the NIC is installed. For example, `pci`.

    \<device_name\>
    Is the NIC device name. For example, `0000:51:00.0`.

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    cgu.id 36
    fw.cgu 8032.16973825.6021
    ```

    </div>

    where:

    `cgu.id 36`
    CGU hardware revision number.

    `fw.cgu 8032.16973825.6021`
    DPLL firmware version running in the CGU, where the DPLL firmware version is `6201`, and the DPLL model is `8032`. The string `16973825` is a shorthand representation of the binary version of the DPLL firmware version (`1.3.0.1`).

    > [!NOTE]
    > The firmware version has a leading nibble and 3 octets for each part of the version number. The number `16973825` in binary is `0001 0000 0011 0000 0000 0000 0001`. Use the binary value to decode the firmware version. For example:
    >
    > | Binary part | Decimal value |
    > |-------------|---------------|
    > | `0001`      | 1             |
    > | `0000 0011` | 3             |
    > | `0000 0000` | 0             |
    > | `0000 0001` | 1             |
    >
    > DPLL firmware version

</div>

# Collecting PTP Operator data

You can use the `oc adm must-gather` command to collect information about your cluster, including features and objects associated with PTP Operator.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have installed the OpenShift CLI (`oc`).

- You have installed the PTP Operator.

</div>

<div>

<div class="title">

Procedure

</div>

- To collect PTP Operator data with `must-gather`, you must specify the PTP Operator `must-gather` image.

  ``` terminal
  $ oc adm must-gather --image=registry.redhat.io/openshift4/ptp-must-gather-rhel9:v4.17
  ```

</div>
