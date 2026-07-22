<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

When proving compliance for your OpenShift Container Platform cluster, you might need to provide the scan results for auditing purposes.

# Obtaining Compliance Operator raw results from a persistent volume

<div class="formalpara">

<div class="title">

Procedure

</div>

The Compliance Operator generates and stores the raw results in a persistent volume. These results are in Asset Reporting Format (ARF).

</div>

1.  Explore the `ComplianceSuite` object:

    ``` terminal
    $ oc get compliancesuites nist-moderate-modified \
    -o json -n openshift-compliance | jq '.status.scanStatuses[].resultsStorage'
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    {
         "name": "ocp4-moderate",
         "namespace": "openshift-compliance"
    }
    {
         "name": "nist-moderate-modified-master",
         "namespace": "openshift-compliance"
    }
    {
         "name": "nist-moderate-modified-worker",
         "namespace": "openshift-compliance"
    }
    ```

    </div>

    This shows the persistent volume claims where the raw results are accessible.

2.  Verify the raw data location by using the name and namespace of one of the results:

    ``` terminal
    $ oc get pvc -n openshift-compliance rhcos4-moderate-worker
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME                     STATUS   VOLUME                                     CAPACITY   ACCESS MODES   STORAGECLASS   AGE
    rhcos4-moderate-worker   Bound  pvc-548f6cfe-164b-42fe-ba13-a07cfbc77f3a   1Gi      RWO         gp2         92m
    ```

    </div>

3.  Fetch the raw results by spawning a pod that mounts the volume and copying the results:

    ``` terminal
    $ oc create -n openshift-compliance -f pod.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example pod.yaml

    </div>

    ``` yaml
    apiVersion: "v1"
    kind: Pod
    metadata:
      name: pv-extract
    spec:
      securityContext:
        runAsNonRoot: true
        seccompProfile:
          type: RuntimeDefault
      containers:
        - name: pv-extract-pod
          image: registry.access.redhat.com/ubi9/ubi
          command: ["sleep", "3000"]
          volumeMounts:
          - mountPath: "/workers-scan-results"
            name: workers-scan-vol
          securityContext:
            allowPrivilegeEscalation: false
            capabilities:
              drop: [ALL]
      volumes:
        - name: workers-scan-vol
          persistentVolumeClaim:
            claimName: rhcos4-moderate-worker
    ```

    </div>

4.  After the pod is running, download the results:

    ``` terminal
    $ oc cp pv-extract:/workers-scan-results -n openshift-compliance .
    ```

    > [!IMPORTANT]
    > Spawning a pod that mounts the persistent volume will keep the claim as `Bound`. If the volume’s storage class in use has permissions set to `ReadWriteOnce`, the volume is only mountable by one pod at a time. You must delete the pod upon completion, or it will not be possible for the Operator to schedule a pod and continue storing results in this location.

5.  After the extraction is complete, the pod can be deleted:

    ``` terminal
    $ oc delete pod pv-extract -n openshift-compliance
    ```
