<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can confirm the operational status of Red Hat Advanced Cluster Security for Kubernetes (RHACS) by deploying sample applications that contain known vulnerabilities. You can run these workloads to test the build and deploy-time assessment features and view the resulting policy violations in the RHACS portal.

<a id="verify-acs-installation_verify-installation-rhacs-ocp"></a>

# Verifying installation

After you complete the installation, run a few vulnerable applications and go to the RHACS portal to evaluate the results of security assessments and policy violations.

> [!NOTE]
> The sample applications listed in the following section contain critical vulnerabilities and they are specifically designed to verify the build and deploy-time assessment features of Red Hat Advanced Cluster Security for Kubernetes.

To verify installation:

1.  Find the address of the RHACS portal based on your exposure method:

    1.  For a route:

        ``` terminal
        $ oc get route central -n stackrox
        ```

    2.  For a load balancer:

        ``` terminal
        $ oc get service central-loadbalancer -n stackrox
        ```

    3.  For port forward:

        1.  Run the following command:

            ``` terminal
            $ oc port-forward svc/central 18443:443 -n stackrox
            ```

        2.  Go to `https://localhost:18443/`.

2.  Using the Red Hat OpenShift CLI, create a new project:

    ``` terminal
    $ oc new-project test
    ```

3.  Start some applications with critical vulnerabilities:

    ``` terminal
    $ oc run shell --labels=app=shellshock,team=test-team \
      --image=quay.io/stackrox-io/docs:example-vulnerables-cve-2014-6271 -n test
    $ oc run samba --labels=app=rce \
      --image=quay.io/stackrox-io/docs:example-vulnerables-cve-2017-7494 -n test
    ```

    Red Hat Advanced Cluster Security for Kubernetes automatically scans these deployments for security risks and policy violations as soon as they are submitted to the cluster. Go to the RHACS portal to view the violations. You can log in to the RHACS portal by using the default username **admin** and the generated password.
