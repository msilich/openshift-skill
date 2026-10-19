<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn how to add custom trusted certificate authorities to Red Hat Advanced Cluster Security for Kubernetes.

<a id="add-trusted-ca-overview_add-trusted-ca"></a>

# Overview of adding trusted CAs

If you are using an enterprise certificate authority (CA) on your network, or self-signed certificates, you must add the CA’s root certificate to Red Hat Advanced Cluster Security for Kubernetes as a trusted root CA.

Adding trusted root CAs allows:

- Central and Scanner to trust remote servers when you integrate with other tools.

- Sensor to trust custom certificates you use for Central.

You can add additional CAs during the installation or on an existing deployment.

> [!NOTE]
> You must first configure your trusted CAs in the cluster where you have deployed Central and then propagate the changes to Scanner and Sensor.

<a id="configure-additional-cas_add-trusted-ca"></a>

# Configuring additional CAs

You can add custom certificate authorities (CAs) to Red Hat Advanced Cluster Security for Kubernetes by using the `ca-setup.sh` script to configure single or multiple CA certificates.

<div>

<div class="title">

Procedure

</div>

1.  Download the `ca-setup.sh` script.

    <div class="note">

    <div class="title">

    </div>

    - If you are doing a new installation, you can find the `ca-setup.sh` script in the `scripts` directory at `central-bundle/central/scripts/ca-setup.sh`.

    - You must run the `ca-setup.sh` script in the same terminal from which you logged into your OpenShift Container Platform cluster.

    </div>

2.  Make the `ca-setup.sh` script executable:

    ``` terminal
    $ chmod +x ca-setup.sh
    ```

3.  Add the certificates by using one of the following options:

    1.  To add a single certificate, use the `-f` option to specify the certificate file:

        ``` terminal
        $ ./ca-setup.sh -f <certificate>
        ```

        <div class="note">

        <div class="title">

        </div>

        - You must use a PEM-encoded certificate file. The file can have any extension.

        - To update a certificate that you added before, use the `-u` option along with the `-f` option.

        </div>

    2.  To add many certificates at once, move all the certificates into a directory, and then use the `-d` option to specify that directory:

        ``` terminal
        $ ./ca-setup.sh -d <directory_name>
        ```

        <div class="note">

        <div class="title">

        </div>

        - You must use PEM-encoded certificate files with a `.crt` or `.pem` extension.

        - Each file must contain only a single certificate.

        - To update certificates that you added before, use the `-u` option along with the `-d` option.

        </div>

</div>

<div>

<div class="title">

Additional resources

</div>

- [ca-setup.sh script](https://raw.githubusercontent.com/openshift/openshift-docs/rhacs-docs-main/files/ca-setup.sh)

</div>

<a id="propagating-changes-overview_add-trusted-ca"></a>

# Propagating changes to services

After you configure trusted CAs, you must make Red Hat Advanced Cluster Security for Kubernetes services trust them.

- If you have configured trusted CAs after the installation, you must restart Central.

- Additionally, if you are also adding certificates for integrating with image registries, you must restart both Central and Scanner.

<a id="restart-central_add-trusted-ca"></a>

## Restarting the Central container

You can restart the Central container by deleting the Central pod.

> [!NOTE]
> If you use Kubernetes, enter `kubectl` instead of `oc`.

<div>

<div class="title">

Procedure

</div>

- To delete the Central pod, run the following command:

  ``` terminal
  $ oc -n stackrox delete pod -lapp=central
  ```

</div>

<a id="restart-scanner_add-trusted-ca"></a>

## Restarting the Scanner container

You can restart the Scanner container by deleting the pod.

<div>

<div class="title">

Procedure

</div>

- Run the following command to delete the Scanner pod:

  - On OpenShift Container Platform:

    ``` terminal
    $ oc delete pod -n stackrox -l app=scanner
    ```

  - On Kubernetes:

    ``` terminal
    $ kubectl delete pod -n stackrox -l app=scanner
    ```

</div>

<a id="post-configuration-notes_add-trusted-ca"></a>

## Post-configuration notes for Sensor deployments

New Sensor deployment bundles automatically include the trusted CAs that you added, but an existing Sensor or a Sensor that you deploy by using the `sensor.sh` script requires additional action.

> [!IMPORTANT]
> After you have added trusted CAs and configured Central, any new Sensor deployment bundles that you create include the CAs.
>
> - If an existing Sensor reports problems while connecting to Central, you must generate a Sensor deployment YAML file and update existing clusters.
>
> - If you are deploying a new Sensor using the `sensor.sh` script, run the following command before you run the `sensor.sh` script:
>
>   ``` terminal
>   $ ./ca-setup-sensor.sh -d ./additional-cas/
>   ```
>
> - If you are deploying a new Sensor using Helm, you do not have to run any additional scripts.
