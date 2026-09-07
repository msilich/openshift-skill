> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/secure-proc_configuring_advanced_authorization). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Restrict access to specific users and groups

Restrict OpenShift Dev Spaces access to specific users and groups so that you can control which users are allowed or denied access to the platform.

## Before you begin

- You have an active `oc` session with administrative permissions to the OpenShift cluster. See [Getting started with the CLI](https://docs.openshift.com/container-platform/4.22/cli_reference/openshift_cli/getting-started-cli.html).

## Procedure

1.  Edit the `CheCluster` Custom Resource to add the `advancedAuthorization` section:

    ``` bash
    $ oc patch checluster devspaces --type=merge -n openshift-devspaces \
      --patch '{
        "spec": {
          "networking": {
            "auth": {
              "advancedAuthorization": {
                "allowUsers": ["<allow_users>"],
                "allowGroups": ["<allow_groups>"],
                "denyUsers": ["<deny_users>"],
                "denyGroups": ["<deny_groups>"]
              }
            }
          }
        }
      }'
    ```

    where:

    allowUsers  
    List of users allowed to access Red Hat OpenShift Dev Spaces.

    allowGroups  
    List of groups of users allowed to access Red Hat OpenShift Dev Spaces (for OpenShift Container Platform only).

    denyUsers  
    List of users denied access to Red Hat OpenShift Dev Spaces.

    denyGroups  
    List of groups of users denied access to Red Hat OpenShift Dev Spaces (for OpenShift Container Platform only).

    If a user is on both `allow` and `deny` lists, access is denied. If `allowUsers` and `allowGroups` are empty, all users are allowed except the ones on the `deny` lists. If `denyUsers` and `denyGroups` are empty, only the users from `allow` lists are allowed. If both `allow` and `deny` lists are empty, all users are allowed.

2.  Wait for the rollout of the OpenShift Dev Spaces server components to complete.

## Results

- Log in to the OpenShift Dev Spaces dashboard as a user on the `allowUsers` list and verify access to the dashboard.

- Log in as a user on the `denyUsers` list and verify that OpenShift Dev Spaces displays the following message:

  ``` plaintext
  Advanced authorization is enabled. User might not be allowed. Please, contact the administrator.
  ```

**Related tasks**  

- [Grant additional permissions to users](secure-proc_configuring_cluster_roles_for_users.md "Grant your developers additional OpenShift permissions by adding cluster roles so they can access resources beyond the default workspace operations.")
- [Remove user data for GDPR compliance](secure-proc_removing_user_data_in_compliance_with_the_gdpr.md "Remove a user’s data from OpenShift Container Platform when a developer leaves your organization, to comply with the General Data Protection Regulation (GDPR). The process for other Kubernetes infrastructures might vary.")
