> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/secure-proc_configuring_cluster_roles_for_users). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Grant additional permissions to users

Grant your developers additional OpenShift permissions by adding cluster roles so they can access resources beyond the default workspace operations.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Define the user roles name:

    ``` bash
    $ USER_ROLES=<name>
    ```

    where:

    name  
    Unique resource name.

2.  Determine the namespace where the OpenShift Dev Spaces Operator is deployed:

    ``` bash
    $ OPERATOR_NAMESPACE=$(oc get pods -l app.kubernetes.io/component=devspaces-operator -o jsonpath={".items[0].metadata.namespace"} --all-namespaces)
    ```

3.  Create needed roles:

    ``` bash
    $ oc apply -f - <<EOF
    kind: ClusterRole
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: ${USER_ROLES}
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
    rules:
      - verbs:
          - <verbs>
        apiGroups:
          - <apiGroups>
        resources:
          - <resources>
    EOF
    ```

    where:

    verbs  
    List all Verbs that apply to all ResourceKinds and AttributeRestrictions contained in this rule. You can use `*` to represent all verbs.

    apiGroups  
    Name the APIGroups that contain the resources.

    resources  
    List all resources that this rule applies to. You can use `*` to represent all verbs.

4.  Delegate the roles to the OpenShift Dev Spaces Operator:

    ``` bash
    $ oc apply -f - <<EOF
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: ${USER_ROLES}
      labels:
        app.kubernetes.io/part-of: che.eclipse.org
    subjects:
      - kind: ServiceAccount
        name: devspaces-operator
        namespace: ${OPERATOR_NAMESPACE}
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: ${USER_ROLES}
    EOF
    ```

5.  Configure the OpenShift Dev Spaces Operator to delegate the roles to the `che` service account:

    ``` bash
    $ oc patch checluster devspaces \
      --patch '{"spec": {"components": {"cheServer": {"clusterRoles": ["'${USER_ROLES}'"]}}}}' \
      --type=merge -n {prod-namespace}
    ```

6.  Configure the OpenShift Dev Spaces server to delegate the roles to a user:

    ``` bash
    $ oc patch checluster devspaces \
      --patch '{"spec": {"devEnvironments": {"user": {"clusterRoles": ["'${USER_ROLES}'"]}}}}' \
      --type=merge -n {prod-namespace}
    ```

7.  Wait for the rollout of the OpenShift Dev Spaces server components to complete.

8.  Ask the user to log out and log in to have the new roles applied.

## Results

- Verify that the ClusterRole exists:

  ``` bash
  $ oc get clusterrole ${USER_ROLES}
  ```

**Related tasks**  

- [Restrict access to specific users and groups](secure-proc_configuring_advanced_authorization.md "Restrict OpenShift Dev Spaces access to specific users and groups so that you can control which users are allowed or denied access to the platform.")
- [Remove user data for GDPR compliance](secure-proc_removing_user_data_in_compliance_with_the_gdpr.md "Remove a user’s data from OpenShift Container Platform when a developer leaves your organization, to comply with the General Data Protection Regulation (GDPR). The process for other Kubernetes infrastructures might vary.")
