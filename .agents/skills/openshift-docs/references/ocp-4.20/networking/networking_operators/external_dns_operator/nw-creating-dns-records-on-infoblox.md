<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To create DNS records on Infoblox, use the External DNS Operator. The Operator manages external name resolution for your cluster services.

# Creating DNS records on a public DNS zone on Infoblox

To create DNS records on Infoblox, use the External DNS Operator. The Operator manages external name resolution for your cluster services.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the OpenShift CLI (`oc`).

- You have access to the Infoblox UI.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a `secret` object with Infoblox credentials by running the following command:

    ``` terminal
    $ oc -n external-dns-operator create secret generic infoblox-credentials --from-literal=EXTERNAL_DNS_INFOBLOX_WAPI_USERNAME=<infoblox_username> --from-literal=EXTERNAL_DNS_INFOBLOX_WAPI_PASSWORD=<infoblox_password>
    ```

2.  Get a list of routes by running the following command:

    ``` terminal
    $ oc get routes --all-namespaces | grep console
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    openshift-console          console             console-openshift-console.apps.test.example.com                       console             https   reencrypt/Redirect     None
    openshift-console          downloads           downloads-openshift-console.apps.test.example.com                     downloads           http    edge/Redirect          None
    ```

    </div>

3.  Create a YAML file, for example, `external-dns-sample-infoblox.yaml`, that defines the `ExternalDNS` object:

    <div class="formalpara">

    <div class="title">

    Example `external-dns-sample-infoblox.yaml` file

    </div>

    ``` yaml
    apiVersion: externaldns.olm.openshift.io/v1beta1
    kind: ExternalDNS
    metadata:
      name: sample-infoblox
    spec:
      provider:
        type: Infoblox
        infoblox:
          credentials:
            name: infoblox-credentials
          gridHost: ${INFOBLOX_GRID_PUBLIC_IP}
          wapiPort: 443
          wapiVersion: "2.3.1"
      domains:
      - filterType: Include
        matchType: Exact
        name: test.example.com
      source:
        type: OpenShiftRoute
        openshiftRouteOptions:
          routerName: default
    ```

    </div>

    where:

    `metadata.name`
    Specifies the External DNS name.

    `provider.type`
    Specifies the provider type.

    `source.type`
    Specifies options for the source of DNS records.

    `routerName`
    If the source type is `OpenShiftRoute`, you can pass the OpenShift Ingress Controller name. External DNS selects the canonical hostname of that router as the target while creating a CNAME record.

4.  Create the `ExternalDNS` resource on Infoblox by running the following command:

    ``` terminal
    $ oc create -f external-dns-sample-infoblox.yaml
    ```

5.  From the Infoblox UI, check the DNS records created for `console` routes:

    1.  Click **Data Management** → **DNS** → **Zones**.

    2.  Select the zone name.

</div>
