<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Sync LDAP groups with OpenShift Container Platform so you can manage user membership and permissions using groups stored in your LDAP directory.

As an administrator, you can use groups to manage users, change their permissions, and enhance collaboration. Your organization may have already created user groups and stored them in an LDAP server. OpenShift Container Platform can sync those LDAP records with internal OpenShift Container Platform records, enabling you to manage your groups in one place. OpenShift Container Platform currently supports group sync with LDAP servers using three common schemas for defining group membership: RFC 2307, Active Directory, and augmented Active Directory.

For more information on configuring LDAP, see "Configuring an LDAP identity provider".

> [!NOTE]
> You must have `cluster-admin` privileges to sync groups.

# About configuring LDAP sync

Review how LDAP group sync works and what the sync configuration file contains so you can configure group sync for your LDAP schema.

Before you can run LDAP sync, you need a sync configuration file. This file contains the following LDAP client configuration details:

- Configuration for connecting to your LDAP server.

- Sync configuration options that are dependent on the schema used in your LDAP server.

- An administrator-defined list of name mappings that maps OpenShift Container Platform group names to groups in your LDAP server.

The format of the configuration file depends upon the schema you are using:

- RFC 2307

- Active Directory

- augmented Active Directory.

## LDAP client configuration

The LDAP client configuration section of the configuration defines the connections to your LDAP server. The following example shows the LDAP client configuration fields:

``` yaml
url: ldap://10.0.0.0:389
bindDN: cn=admin,dc=example,dc=com
bindPassword: <password>
insecure: false
ca: my-ldap-ca-bundle.crt
```

- The `url` field shows the connection protocol, IP address of the LDAP server hosting your database, and the port to connect to, formatted as `scheme://host:port`.

- The `bindDN` field shows an optional distinguished name (DN) to use as the Bind DN. OpenShift Container Platform uses this if elevated privilege is required to retrieve entries for the sync operation.

- The `bindPassword` field shows an optional password to use to bind. OpenShift Container Platform uses this if elevated privilege is necessary to retrieve entries for the sync operation. This value may also be provided in an environment variable, external file, or encrypted file.

- The `insecure` field controls whether the LDAP connection uses TLS. When set to `false`, `ldaps://` URLs connect to the server using TLS, and `ldap://` URLs are upgraded to TLS. When set to `true`, no TLS connection is made to the server, and you cannot use `ldaps://` URL schemes.

- The `ca` field shows the certificate bundle to use for validating server certificates for the configured URL. If empty, OpenShift Container Platform uses system-trusted roots. This only applies if `insecure` is set to `false`.

## LDAP query definition

Sync configurations consist of LDAP query definitions for the entries that are required for synchronization. The specific definition of an LDAP query depends on the schema used to store membership information in the LDAP server. The following example shows the LDAP query definition fields:

``` yaml
baseDN: ou=users,dc=example,dc=com
scope: sub
derefAliases: never
timeout: 0
filter: (objectClass=person)
pageSize: 0
```

- The `baseDN` field contains the distinguished name (DN) of the branch of the directory where all searches start from. It is required that you specify the top of your directory tree, but you can also specify a subtree in the directory.

- The `scope` field shows the search scope. Valid values are `base`, `one`, and `sub`. If you omit this field, the default is `sub`. For descriptions of each value, see Table 1, *LDAP search scope options*.

- The `derefAliases` field shows the behavior of the search with respect to aliases in the LDAP tree. Valid values are `never`, `search`, `base`, or `always`. If this is left undefined, then the default is to `always` dereference aliases. Descriptions of the dereferencing behaviors are in Table 2, *LDAP dereferencing behaviors*.

- The `timeout` field shows the time limit allowed for the search by the client, in seconds. A value of `0` imposes no client-side limit.

- The `filter` field contains a valid LDAP search filter. If this is left undefined, then the default is `(objectClass=*)`.

- The `pageSize` field shows the maximum number of LDAP entries the server returns per page. If set to `0`, no page size limit applies. Set this field when a query returns more entries than the client or server allow by default.

| LDAP search scope | Description |
|----|----|
| `base` | Only consider the object specified by the base DN given for the query. |
| `one` | Consider all of the objects on the same level in the tree as the base DN for the query. |
| `sub` | Consider the entire subtree rooted at the base DN given for the query. |

| Dereferencing behavior | Description |
|----|----|
| `never` | Never dereference any aliases found in the LDAP tree. |
| `search` | Only dereference aliases found while searching. |
| `base` | Only dereference aliases while finding the base object. |
| `always` | Always dereference all aliases found in the LDAP tree. |

## User-defined name mapping

A user-defined name mapping explicitly maps the names of OpenShift Container Platform groups to unique identifiers that find groups on your LDAP server. The mapping uses normal YAML syntax. A user-defined mapping can contain an entry for every group in your LDAP server or only a subset of those groups. If there are groups on the LDAP server that do not have a user-defined name mapping, the default behavior during sync is to use the attribute specified as the name of the OpenShift Container Platform group.

The following example shows a user-defined name mapping:

``` yaml
groupUIDNameMapping:
  "cn=group1,ou=groups,dc=example,dc=com": firstgroup
  "cn=group2,ou=groups,dc=example,dc=com": secondgroup
  "cn=group3,ou=groups,dc=example,dc=com": thirdgroup
```

## About the RFC 2307 configuration file

Review the RFC 2307 LDAP sync configuration file so you can define user and group queries and the attributes used in OpenShift Container Platform group records.

The RFC 2307 schema requires you to provide an LDAP query definition for both user and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships:

> [!NOTE]
> If using user-defined name mappings, your configuration file differs.

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
insecure: false
bindDN: cn=admin,dc=example,dc=com
bindPassword:
  file: "/etc/secrets/bindPassword"
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
```

where:

`url`
Specifies the IP address and host of the LDAP server where the record of the group is stored.

`insecure`
Specifies whether the LDAP connection uses TLS. When set to `false`, `ldaps://` URLs connect to the server using TLS, and `ldap://` URLs are upgraded to TLS. When set to `true`, no TLS connection is made to the server, and you cannot use `ldaps://` URL schemes.

`rfc2307.groupUIDAttribute`
Specifies the attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for `groupUIDAttribute`. For fine-grained filtering, use an allowlist file, a denylist file, or both.

`rfc2307.groupNameAttributes`
Specifies the attribute to use as the name of the group.

`rfc2307.groupMembershipAttributes`
Specifies the attribute on the group that stores the membership information.

`rfc2307.userUIDAttribute`
Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both.

`rfc2307.userNameAttributes`
Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record.

## About the Active Directory configuration file

Review the Active Directory LDAP sync configuration file so you can define user queries and the attributes used in OpenShift Container Platform group records.

The Active Directory schema requires you to provide an LDAP query definition for user entries, as well as the attributes to represent them with in the internal OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, but define the name of the group by the name of the group on the LDAP server. The following configuration file creates these relationships:

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
activeDirectory:
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ]
    groupMembershipAttributes: [ memberOf ]
```

where:

`activeDirectory.userNameAttributes`
Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record.

`activeDirectory.groupMembershiptAttributes`
Specifies the attribute on the user that stores the membership information.

## About the augmented Active Directory configuration file

Review the augmented Active Directory LDAP sync configuration file so you can define user and group queries and the attributes used in OpenShift Container Platform group records.

The augmented Active Directory schema requires you to provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships.

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ]
    groupMembershipAttributes: [ memberOf ]
```

where:

`augmentedActiveDirectory.groupUIDAttribute`
Specifies the attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both.

`augmentedActiveDirectory.groupNameAttributes`
Specifies the attribute to use as the name of the group.

`augmentedActiveDirectory.userNameAttributes`
Specifies the attribute to use as the name of the user in the OpenShift Container Platform group record.

`augmentedActiveDirectory.groupMembershipAttributes`
Specifies the attribute on the user that stores the membership information.

# Running LDAP sync

Review LDAP sync types before running group sync between your LDAP server and OpenShift Container Platform. Each type defines sync direction and scope so you select the command that matches your directory layout.

After you have created a sync configuration file, you can begin to sync. OpenShift Container Platform allows administrators to perform several different sync types with the same server.

## Syncing the LDAP server with OpenShift Container Platform

Sync all groups from your LDAP server with OpenShift Container Platform so you can mirror your complete LDAP group membership in the cluster.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync all groups from the LDAP server with OpenShift Container Platform by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=config.yaml --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

## Syncing OpenShift Container Platform groups with the LDAP server

Sync existing OpenShift Container Platform groups with your LDAP server so you can update membership for groups that already exist in the cluster.

You can sync all groups already in OpenShift Container Platform that correspond to groups in the LDAP server specified in the configuration file.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync OpenShift Container Platform groups with the LDAP server by running the following command:

  ``` terminal
  $ oc adm groups sync --type=openshift --sync-config=config.yaml --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

## Syncing subgroups from the LDAP server with OpenShift Container Platform

Sync a subset of LDAP groups with OpenShift Container Platform so you can control which groups are synchronized using allowlist files, denylist files, or both.

> [!NOTE]
> You can use any combination of denylist files, allowlist files, or allowlist literals. Allowlist and denylist files must contain one unique group identifier per line, and you can include allowlist literals directly in the command itself. These guidelines apply to groups found on LDAP servers as well as groups already present in OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- To sync groups using an allowlist file, run the following command:

  ``` terminal
  $ oc adm groups sync --whitelist=<allowlist_file> \
                     --sync-config=config.yaml      \
                     --confirm
  ```

- To sync groups using a denylist file, run the following command:

  ``` terminal
  $ oc adm groups sync --blacklist=<denylist_file> \
                     --sync-config=config.yaml      \
                     --confirm
  ```

- To sync a single group by the unique identifier of the group, run the following command:

  ``` terminal
  $ oc adm groups sync <group_unique_identifier>    \
                     --sync-config=config.yaml      \
                     --confirm
  ```

- To sync a single group with both an allowlist and a denylist, run the following command:

  ``` terminal
  $ oc adm groups sync <group_unique_identifier>  \
                     --whitelist=<allowlist_file> \
                     --blacklist=<denylist_file> \
                     --sync-config=config.yaml    \
                     --confirm
  ```

- To sync existing OpenShift Container Platform groups using an allowlist file, run the following command:

  ``` terminal
  $ oc adm groups sync --type=openshift           \
                     --whitelist=<allowlist_file> \
                     --sync-config=config.yaml    \
                     --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

# Running a group pruning job

Run a group pruning job to remove LDAP-synced groups from OpenShift Container Platform when they no longer exist on your LDAP server so you can keep cluster group records aligned with your directory.

<div>

<div class="title">

Procedure

</div>

- Prune groups using a sync configuration file by running the following command:

  ``` terminal
  $ oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
  ```

- Prune groups using an allowlist file by running the following command:

  ``` terminal
  $ oc adm prune groups --whitelist=/path/to/whitelist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
  ```

- Prune groups using a denylist file by running the following command:

  ``` terminal
  $ oc adm prune groups --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
  ```

</div>

# Automatically syncing LDAP groups

Configure a cron job to automatically sync LDAP groups with OpenShift Container Platform so you can keep group membership up to date without running manual sync commands.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You configured an LDAP identity provider (IDP).

- You created an LDAP secret named `ldap-secret` and a config map named `ca-config-map`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a project where the cron job runs by running the following command:

    ``` terminal
    $ oc new-project ldap-sync
    ```

    This procedure uses a project called `ldap-sync`.

2.  Locate the secret and config map that you created when configuring the LDAP identity provider and copy them to this new project.

    The secret and config map exist in the `openshift-config` project and must be copied to the new `ldap-sync` project.

3.  Define a service account:

    ``` yaml
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      name: ldap-group-syncer
      namespace: ldap-sync
    ```

4.  Create the service account by running the following command:

    ``` terminal
    $ oc create -f ldap-sync-service-account.yaml
    ```

5.  Define a cluster role:

    ``` yaml
    apiVersion: rbac.authorization.k8s.io/v1
    kind: ClusterRole
    metadata:
      name: ldap-group-syncer
    rules:
      - apiGroups:
          - user.openshift.io
        resources:
          - groups
        verbs:
          - get
          - list
          - create
          - update
    ```

6.  Create the cluster role by running the following command:

    ``` terminal
    $ oc create -f ldap-sync-cluster-role.yaml
    ```

7.  Define a cluster role binding to bind the cluster role to the service account:

    ``` yaml
    kind: ClusterRoleBinding
    apiVersion: rbac.authorization.k8s.io/v1
    metadata:
      name: ldap-group-syncer
    subjects:
      - kind: ServiceAccount
        name: ldap-group-syncer
        namespace: ldap-sync
    roleRef:
      apiGroup: rbac.authorization.k8s.io
      kind: ClusterRole
      name: ldap-group-syncer
    ```

    where:

    `subjects.name`
    Specifies the service account created earlier in this procedure.

    `roleRef.name`
    Specifies the cluster role created earlier in this procedure.

8.  Create the cluster role binding by running the following command:

    ``` terminal
    $ oc create -f ldap-sync-cluster-role-binding.yaml
    ```

9.  Define a config map that specifies the sync configuration file:

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: ldap-group-syncer
      namespace: ldap-sync
    data:
      sync.yaml:
        kind: LDAPSyncConfig
        apiVersion: v1
        url: ldaps://10.0.0.0:636
        insecure: false
        bindDN: cn=admin,dc=example,dc=com
        bindPassword:
          file: "/etc/secrets/bindPassword"
        ca: /etc/ldap-ca/ca.crt
        rfc2307:
          groupsQuery:
            baseDN: "ou=groups,dc=example,dc=com"
            scope: sub
            filter: "(objectClass=groupOfMembers)"
            derefAliases: never
            pageSize: 0
          groupUIDAttribute: dn
          groupNameAttributes: [ cn ]
          groupMembershipAttributes: [ member ]
          usersQuery:
            baseDN: "ou=users,dc=example,dc=com"
            scope: sub
            derefAliases: never
            pageSize: 0
          userUIDAttribute: dn
          userNameAttributes: [ uid ]
          tolerateMemberNotFoundErrors: false
          tolerateMemberOutOfScopeErrors: false
    ```

    where:

    `data.sync.yaml`
    Specifies the sync configuration file.

    `data.sync.yaml.url`
    Specifies the URL.

    `data.sync.yaml.bindDN`
    Specifies the `bindDN`.

    `data.sync.yaml.rfc2307`
    Specifies the RFC 2307 schema. Adjust the values as necessary. You can also use a different schema.

    `data.sync.yaml.rfc2307.groupsQuery.baseDN`
    Specifies the `baseDN` for `groupsQuery`.

    `data.sync.yaml.rfc2307.usersQuery.baseDN`
    Specifies the `baseDN` for `usersQuery`.

10. Create the config map by running the following command:

    ``` terminal
    $ oc create -f ldap-sync-config-map.yaml
    ```

11. Define a cron job:

    ``` yaml
    kind: CronJob
    apiVersion: batch/v1
    metadata:
      name: ldap-group-syncer
      namespace: ldap-sync
    spec:
      schedule: "*/30 * * * *"
      concurrencyPolicy: Forbid
      jobTemplate:
        spec:
          backoffLimit: 0
          ttlSecondsAfterFinished: 1800
          template:
            spec:
              containers:
                - name: ldap-group-sync
                  image: "registry.redhat.io/openshift4/ose-cli:latest"
                  command:
                    - "/bin/bash"
                    - "-c"
                    - "oc adm groups sync --sync-config=/etc/config/sync.yaml --confirm"
                  volumeMounts:
                    - mountPath: "/etc/config"
                      name: "ldap-sync-volume"
                    - mountPath: "/etc/secrets"
                      name: "ldap-bind-password"
                    - mountPath: "/etc/ldap-ca"
                      name: "ldap-ca"
              volumes:
                - name: "ldap-sync-volume"
                  configMap:
                    name: "ldap-group-syncer"
                - name: "ldap-bind-password"
                  secret:
                    secretName: "ldap-secret"
                - name: "ldap-ca"
                  configMap:
                    name: "ca-config-map"
              restartPolicy: "Never"
              terminationGracePeriodSeconds: 30
              activeDeadlineSeconds: 500
              dnsPolicy: "ClusterFirst"
              serviceAccountName: "ldap-group-syncer"
    ```

    where:

    `spec`
    Specifies the configuration settings for the cron job. See "Creating cron jobs" for more information on cron job settings.

    `spec.schedule`
    Specifies the schedule for the job specified in [cron format](https://en.wikipedia.org/wiki/Cron). This example cron job runs every 30 minutes. Adjust the frequency as necessary, making sure to take into account how long the sync takes to run.

    `spec.jobTemplate.spec.ttlSecondsAfterFinished`
    Specifies how long, in seconds, to keep finished jobs. This should match the period of the job schedule in order to clean old failed jobs and prevent unnecessary alerts. For more information, see [Automatic Cleanup for Finished Jobs (Kubernetes documentation)](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished).

    `spec.jobTemplate.spec.template.spec.containers.command`
    Specifies the LDAP sync command for the cron job to run. Passes in the sync configuration file that was defined in the config map.

    `spec.jobTemplate.spec.template.spec.volumes.secret.secretName`
    Specifies the name of the secret that you created when the LDAP IDP was configured.

    `spec.jobTemplate.spec.template.spec.volumes.configMap.name`
    Specifies the name of the config map that you created when the LDAP IDP was configured.

12. Create the cron job by running the following command:

    ``` terminal
    $ oc create -f ldap-sync-cron-job.yaml
    ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Configuring an LDAP identity provider](identity_providers/configuring-ldap-identity-provider.md#configuring-ldap-identity-provider)

- [Creating cron jobs](../nodes/jobs/nodes-nodes-jobs.md#nodes-nodes-jobs-creating-cron_nodes-nodes-jobs)

</div>

# LDAP group sync examples

Review LDAP group sync examples so you can configure synchronization for RFC 2307, Active Directory, or augmented Active Directory schemas.

> [!NOTE]
> These examples cover only direct group membership. Each user is a direct member of a group, and groups do not contain other groups as members. For information, see "LDAP nested membership sync".

## Syncing groups using the RFC 2307 schema

Sync LDAP groups by using the RFC 2307 schema so you can mirror direct group membership from your LDAP server in OpenShift Container Platform.

For the RFC 2307 schema, the following examples synchronize a group named `admins` that has two members: `Jane` and `Jim`. The examples explain:

- How the group and users are added to the LDAP server.

- What the resulting group record in OpenShift Container Platform is after synchronization.

> [!NOTE]
> These examples assume that all users are direct members of their respective groups. Specifically, no groups have other groups as members. For information on how to sync nested groups, see "LDAP nested membership sync".

In the RFC 2307 schema, users and groups exist on the LDAP server as first-class entries, and group membership is stored in attributes on the group. The following snippet of `ldif` defines the users and group for this schema:

``` ldif
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
```

where:

`dn: cn=admins,ou=groups,dc=example,dc=com`
Specifies that this group is a first-class entry in the LDAP server.

`member: cn=Jane,ou=users,dc=example,dc=com`
Specifies that the members of a group are listed with an identifying reference as attributes on the group.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync with the `rfc2307_config.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config.yaml --confirm
  ```

  After you run the sync command, the following group record is created in OpenShift Container Platform:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: admins
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `metadata.annotations.openshift.io/ldap.sync-time`
  Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format.

  `metadata.annotations.openshift.io/ldap.uid`
  Specifies the unique identifier for the group on the LDAP server.

  `metadata.annotations.openshift.io/ldap.url`
  Specifies the IP address and host of the LDAP server where the record of the group is stored.

  `metadata.name`
  Specifies the name of the group as specified by the sync file.

  `users`
  Specifies the users that are members of the group, named as specified by the sync file.

</div>

## Syncing groups by using the RFC 2307 schema with user-defined name mappings

Sync LDAP groups using the RFC 2307 schema with user-defined name mappings so you can map LDAP group identifiers to OpenShift Container Platform group names.

When you sync groups with user-defined name mappings, include the mappings in the configuration file, as shown in the following `rfc2307_config_user_defined.yaml` example:

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
groupUIDNameMapping:
  "cn=admins,ou=groups,dc=example,dc=com": Administrators
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        pageSize: 0
    userUIDAttribute: dn
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: false
    tolerateMemberOutOfScopeErrors: false
```

where:

`groupUIDNameMapping`
Specifies the user-defined name mapping.

`rfc2307.groupUIDAttribute`
Specifies the unique identifier attribute that is used for the keys in the user-defined name mapping. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both.

`rfc2307.groupNameAttributes`
Specifies the attribute to name OpenShift Container Platform groups with if their unique identifier is not in the user-defined name mapping.

`rfc2307.userUIDAttribute`
Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for the `userUIDAttribute` parameter. For fine-grained filtering, use an allowlist file, a denylist file, or both.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config_user_defined.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync groups using the `rfc2307_config_user_defined.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config_user_defined.yaml --confirm
  ```

  After you run the sync command, the following group record is created in OpenShift Container Platform:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: Administrators
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `metadata.name`
  Specifies the name of the group as specified by the user-defined name mapping.

</div>

## Syncing groups by using RFC 2307 with user-defined error tolerances

Sync LDAP groups using the RFC 2307 schema with error tolerances so you can complete group synchronization when some members are missing or out of scope.

By default, if the groups being synced contain members whose entries are outside of the scope defined in the member query, the group sync fails with an error:

    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with dn="<user-dn>" would search outside of the base dn specified (dn="<base-dn>")".

This often indicates a misconfigured `baseDN` in the `usersQuery` field. However, in cases where the `baseDN` intentionally does not contain some of the members of the group, setting `tolerateMemberOutOfScopeErrors: true` allows the group sync to continue. Out of scope members are ignored.

Similarly, when the group sync process fails to locate a member for a group, it fails with errors:

    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" refers to a non-existent entry".
    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" and filter "<filter>" did not return any results".

This often indicates a misconfigured `usersQuery` field. However, in cases where the group contains member entries that are known to be missing, setting `tolerateMemberNotFoundErrors: true` allows the group sync to continue. Missing members are ignored.

> [!WARNING]
> Enabling error tolerances for the LDAP group sync causes the sync process to ignore member entries that cause errors. If the LDAP group sync is not configured correctly, this could result in synced OpenShift Container Platform groups missing members.

The following example shows LDAP entries that use RFC 2307 schema with invalid group membership: `rfc2307_problematic_users.ldif`

``` ldif
  dn: ou=users,dc=example,dc=com
  objectClass: organizationalUnit
  ou: users
  dn: cn=Jane,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jane
  sn: Smith
  displayName: Jane Smith
  mail: jane.smith@example.com
  dn: cn=Jim,ou=users,dc=example,dc=com
  objectClass: person
  objectClass: organizationalPerson
  objectClass: inetOrgPerson
  cn: Jim
  sn: Adams
  displayName: Jim Adams
  mail: jim.adams@example.com
  dn: ou=groups,dc=example,dc=com
  objectClass: organizationalUnit
  ou: groups
  dn: cn=admins,ou=groups,dc=example,dc=com
  objectClass: groupOfNames
  cn: admins
  owner: cn=admin,dc=example,dc=com
  description: System Administrators
  member: cn=Jane,ou=users,dc=example,dc=com
  member: cn=Jim,ou=users,dc=example,dc=com
  member: cn=INVALID,ou=users,dc=example,dc=com
  member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com
```

where:

`member: cn=INVALID,ou=users,dc=example,dc=com`
Specifies a member that does not exist on the LDAP server.

`member: cn=Jim,ou=OUTOFSCOPE,dc=example,dc=com`
Specifies a member that may exist, but is not under the `baseDN` in the user query for the sync job.

To tolerate the errors in the above example, the following additions to your sync configuration file must be made:

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
rfc2307:
    groupsQuery:
        baseDN: "ou=groups,dc=example,dc=com"
        scope: sub
        derefAliases: never
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    groupMembershipAttributes: [ member ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
    userUIDAttribute: dn
    userNameAttributes: [ mail ]
    tolerateMemberNotFoundErrors: true
    tolerateMemberOutOfScopeErrors: true
```

where:

`rfc2307.userUIDAttribute`
Specifies the attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use an allowlist file, a denylist file, or both.

`rfc2307.tolerateMemberNotFoundErrors`
Specifies whether the sync job tolerates groups for which some members were not found. When set to `true`, members whose LDAP entries are not found are ignored. The default behavior for the sync job is to fail if a member of a group is not found.

`rfc2307.tolerateMemberOutOfScopeErrors`
Specifies whether the sync job tolerates groups for which some members are outside the user scope given in the `usersQuery` `baseDN`. When set to `true`, members outside the member query scope are ignored. The default behavior for the sync job is to fail if a member of a group is out of scope.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `rfc2307_config_tolerating.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync with the `rfc2307_config_tolerating.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config_tolerating.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the previous sync operation:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: admins
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `users`
  Specifies the users that are members of the group, as specified by the sync file. Members for which lookup encountered tolerated errors are absent.

</div>

## Syncing groups using the Active Directory schema

You can sync LDAP groups for your OpenShift Container Platform cluster using the Active Directory schema by running `oc adm groups sync` with an LDAP sync configuration file. In this schema, group membership is stored in attributes on user entries, such as `memberOf`.

In the Active Directory schema, users exist on the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema:

``` ldif
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: admins

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: admins
```

where:

`memberOf`
Specifies that the group memberships of the user are listed as attributes on the user, and the group does not exist as an entry on the server. The `memberOf` attribute does not have to be a literal attribute on the user; in some LDAP servers, the attribute is created during search and returned to the client, but not committed to the database.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `active_directory_config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync with the `active_directory_config.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=active_directory_config.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the previous sync operation:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: admins
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: admins
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `metadata.annotations.openshift.io/ldap.sync-time`
  Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format.

  `metadata.annotations.openshift.io/ldap.uid`
  Specifies the unique identifier for the group on the LDAP server.

  `metadata.annotations.openshift.io/ldap.url`
  Specifies the IP address and host of the LDAP server where the record of the group is stored.

  `metadata.name`
  Specifies the name of the group as listed in the LDAP server.

  `users`
  Specifies the users that are members of the group, named as specified by the sync file.

</div>

## Syncing groups using the augmented Active Directory schema

You can sync LDAP groups for your OpenShift Container Platform cluster using the augmented Active Directory schema by running `oc adm groups sync` with an LDAP sync configuration file.

In this schema, users and groups are first-class LDAP entries, and group membership is stored in attributes on user entries, such as `memberOf`.

In the augmented Active Directory schema, both users and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema:

``` ldif
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com
objectClass: groupOfNames
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
```

where:

`memberOf`
Specifies that the group memberships of the user are listed as attributes on the user.

`dn: cn=admins,ou=groups,dc=example,dc=com`
Specifies that the group is a first-class entry on the LDAP server.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `augmented_active_directory_config.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync with the `augmented_active_directory_config.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync --sync-config=augmented_active_directory_config.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the previous sync operation:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: admins
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `metadata.annotations.openshift.io/ldap.sync-time`
  Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format.

  `metadata.annotations.openshift.io/ldap.uid`
  Specifies the unique identifier for the group on the LDAP server.

  `metadata.annotations.openshift.io/ldap.url`
  Specifies the IP address and host of the LDAP server where the record of the group is stored.

  `metadata.name`
  Specifies the name of the group as specified by the sync file.

  `users`
  Specifies the users that are members of the group, named as specified by the sync file.

</div>

## LDAP nested membership sync

Understand how nested LDAP group membership is flattened during sync so you can configure allowlisted sync jobs that include members of nested Active Directory groups.

Groups in OpenShift Container Platform do not nest. The LDAP server must flatten group membership before the data can be consumed. The Microsoft Active Directory Server supports this feature via the `LDAP_MATCHING_RULE_IN_CHAIN` rule, which has the OID `1.2.840.113556.1.4.1941`. Furthermore, only explicitly allowlisted groups can be synced when using this matching rule.

The following example synchronizes a group named `admins` that has one user member, `Jane`, and one nested group member, `otheradmins`, which contains `Jim`.

This example explains:

- How the group and users are added to the LDAP server.

- What the LDAP sync configuration file looks like.

- What the resulting group record in OpenShift Container Platform is after synchronization.

### Example LDAP entries

In the augmented Active Directory schema, both users and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user or the group. The following `ldif` snippet defines the users and groups for this schema:

``` ldif
dn: ou=users,dc=example,dc=com
objectClass: organizationalUnit
ou: users

dn: cn=Jane,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jane
sn: Smith
displayName: Jane Smith
mail: jane.smith@example.com
memberOf: cn=admins,ou=groups,dc=example,dc=com

dn: cn=Jim,ou=users,dc=example,dc=com
objectClass: person
objectClass: organizationalPerson
objectClass: inetOrgPerson
objectClass: testPerson
cn: Jim
sn: Adams
displayName: Jim Adams
mail: jim.adams@example.com
memberOf: cn=otheradmins,ou=groups,dc=example,dc=com

dn: ou=groups,dc=example,dc=com
objectClass: organizationalUnit
ou: groups

dn: cn=admins,ou=groups,dc=example,dc=com
objectClass: group
cn: admins
owner: cn=admin,dc=example,dc=com
description: System Administrators
member: cn=Jane,ou=users,dc=example,dc=com
member: cn=otheradmins,ou=groups,dc=example,dc=com

dn: cn=otheradmins,ou=groups,dc=example,dc=com
objectClass: group
cn: otheradmins
owner: cn=admin,dc=example,dc=com
description: Other System Administrators
memberOf: cn=admins,ou=groups,dc=example,dc=com
member: cn=Jim,ou=users,dc=example,dc=com
```

where:

`memberOf`
Specifies that the memberships of the user and group are listed as attributes on the object.

`dn: cn=admins,ou=groups,dc=example,dc=com`
Specifies that groups are first-class entries on the LDAP server.

`member: cn=otheradmins,ou=groups,dc=example,dc=com`
Specifies that the `otheradmins` group is a member of the `admins` group.

### Configuration requirements

When syncing nested groups with Active Directory, you must provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records. Furthermore, certain changes are required in this configuration:

- The `oc adm groups sync` command requires you to explicitly allowlist groups.

- The `groupMembershipAttributes` field must include `"memberOf:1.2.840.113556.1.4.1941:"` to comply with the `LDAP_MATCHING_RULE_IN_CHAIN` rule.

- The `groupUIDAttribute` must be set to `dn`.

- The `groupsQuery`:

  - Must not set `filter`.

  - Must set a valid `derefAliases`.

  - Should not set `baseDN` as that value is ignored.

  - Should not set `scope` as that value is ignored.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user-facing or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name.

### Example sync configuration

The following configuration file creates these relationships. Save it as `augmented_active_directory_config_nested.yaml`:

``` yaml
kind: LDAPSyncConfig
apiVersion: v1
url: ldap://LDAP_SERVICE_IP:389
augmentedActiveDirectory:
    groupsQuery:
        derefAliases: never
        pageSize: 0
    groupUIDAttribute: dn
    groupNameAttributes: [ cn ]
    usersQuery:
        baseDN: "ou=users,dc=example,dc=com"
        scope: sub
        derefAliases: never
        filter: (objectclass=person)
        pageSize: 0
    userNameAttributes: [ mail ]
    groupMembershipAttributes: [ "memberOf:1.2.840.113556.1.4.1941:" ]
```

where:

`augmentedActiveDirectory.groupsQuery`
Specifies that the `groupsQuery` filters cannot be specified. The `groupsQuery` base DN and scope values are ignored. `groupsQuery` must set a valid `derefAliases`.

`augmentedActiveDirectory.groupUIDAttribute`
Specifies the attribute that uniquely identifies a group on the LDAP server. It must be set to `dn`.

`augmentedActiveDirectory.groupNameAttributes`
Specifies the attribute to use as the name of the group.

`augmentedActiveDirectory.userNameAttributes`
Specifies the attribute to use as the username of the user in the OpenShift Container Platform group record.

`augmentedActiveDirectory.groupMembershipAttributes`
Specifies the attribute on the user that stores the membership information. Note the use of `LDAP_MATCHING_RULE_IN_CHAIN`.

> [!NOTE]
> `mail` or `sAMAccountName` are preferred choices in most installations.

## LDAP nested membership sync example

Run the nested group LDAP sync example with an allowlisted group so you can verify that members of nested Active Directory groups appear in the resulting OpenShift Container Platform group.

<div>

<div class="title">

Prerequisites

</div>

- An LDAP sync configuration file exists. This procedure uses an example file named `augmented_active_directory_config_nested.yaml`.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Sync with the `augmented_active_directory_config_nested.yaml` file by running the following command:

  ``` terminal
  $ oc adm groups sync \
      'cn=admins,ou=groups,dc=example,dc=com' \
      --sync-config=augmented_active_directory_config_nested.yaml \
      --confirm
  ```

  > [!NOTE]
  > You must explicitly allowlist the `cn=admins,ou=groups,dc=example,dc=com` group.

  OpenShift Container Platform creates the following group record as a result of the previous sync operation:

  ``` yaml
  apiVersion: user.openshift.io/v1
  kind: Group
  metadata:
    annotations:
      openshift.io/ldap.sync-time: 2015-10-13T10:08:38-0400
      openshift.io/ldap.uid: cn=admins,ou=groups,dc=example,dc=com
      openshift.io/ldap.url: LDAP_SERVER_IP:389
    creationTimestamp:
    name: admins
  users:
  - jane.smith@example.com
  - jim.adams@example.com
  ```

  where:

  `metadata.annotations.openshift.io/ldap.sync-time`
  Specifies the last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 8601 format.

  `metadata.annotations.openshift.io/ldap.uid`
  Specifies the unique identifier for the group on the LDAP server.

  `metadata.annotations.openshift.io/ldap.url`
  Specifies the IP address and host of the LDAP server where the record of the group is stored.

  `metadata.name`
  Specifies the name of the group as specified by the sync file.

  `users`
  Specifies the users that are members of the group, named as specified by the sync file.

  > [!NOTE]
  > Members of nested groups are included because the group membership is flattened by the Microsoft Active Directory Server.

</div>

# LDAP sync configuration specification

Review the LDAP group sync configuration specification so you can identify required fields and schema-specific options for your sync configuration file.

The following sections describe the object specification for the configuration file. Note that the different schema types define different fields. For example, the `v1.ActiveDirectoryConfig` schema type has no `groupsQuery` field, but the `v1.RFC2307Config` and `v1.AugmentedActiveDirectoryConfig` schema types include a `groupsQuery` field.

> [!IMPORTANT]
> There is no support for binary attributes. All attribute data coming from the LDAP server must be in the UTF-8 encoded string format. For example, never use a binary attribute, such as `objectGUID`, as an ID attribute. You must use string attributes, such as `sAMAccountName` or `userPrincipalName`, instead.

## v1.LDAPSyncConfig

`LDAPSyncConfig` holds the necessary configuration options to define an LDAP group sync.

| Name | Description | Schema |
|----|----|----|
| `kind` | A camel case string value that represents the REST resource this object represents. Servers may infer this value from the endpoint that receives client requests. Clients cannot update this value. | string |
| `apiVersion` | Defines the versioned schema for this object representation. Servers should convert recognized schemas to the latest internal value and may reject unrecognized values. | string |
| `url` | Specifies the scheme, host, and port of the LDAP server to connect to, in the form `scheme://host:port`. | string |
| `bindDN` | Optional DN to bind to the LDAP server with. | string |
| `bindPassword` | Optional password to bind with during the search phase. | v1.StringSource |
| `insecure` | If `true`, indicates the connection should not use TLS. If `false`, `ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to a TLS connection using `StartTLS` as specified in <https://tools.ietf.org/html/rfc2830>. If you set `insecure` to `true`, you cannot use `ldaps://` URL schemes. | boolean |
| `ca` | Optional trusted certificate authority bundle to use when making requests to the server. If empty, the default system roots are used. | string |
| `groupUIDNameMapping` | Optional direct mapping of LDAP group UIDs to OpenShift Container Platform group names. | object |
| `rfc2307` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to RFC 2307: first-class group and user entries, with group membership determined by a multi-valued attribute on the group entry that lists the members of the group. | v1.RFC2307Config |
| `activeDirectory` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory: first-class user entries, with group membership determined by a multi-valued attribute on member entries that lists the groups to which each member belongs. | v1.ActiveDirectoryConfig |
| `augmentedActiveDirectory` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory as described above, with one addition: first-class group entries exist and are used to hold metadata but not group membership. | v1.AugmentedActiveDirectoryConfig |

## v1.StringSource

`StringSource` allows specifying a string inline, or externally via environment variable or file. When it contains only a string value, it marshals to a simple JSON string.

| Name | Description | Schema |
|----|----|----|
| `value` | Specifies the plain text value, or an encrypted value if `keyFile` is specified. | string |
| `env` | Specifies an environment variable containing the plain text value, or an encrypted value if the `keyFile` is specified. | string |
| `file` | References a file containing the plain text value, or an encrypted value if a `keyFile` is specified. | string |
| `keyFile` | References a file containing the key to use to decrypt the value. | string |

## v1.LDAPQuery

`LDAPQuery` holds the options necessary to build an LDAP query.

| Name | Description | Schema |
|----|----|----|
| `baseDN` | DN of the branch of the directory where all searches should start from. | string |
| `scope` | The optional scope of the search. Can be `base`: only the base object, `one`: all objects on the base level, `sub`: the entire subtree. Defaults to `sub` if not set. | string |
| `derefAliases` | The optional behavior of the search with regards to aliases. Can be `never`: never dereference aliases, `search`: only dereference in searching, `base`: only dereference in finding the base object, `always`: always dereference. Defaults to `always` if not set. | string |
| `timeout` | Holds the limit of time in seconds that any request to the server can remain outstanding before the wait for a response is given up. If this is `0`, no client-side limit is imposed. | integer |
| `filter` | A valid LDAP search filter that retrieves all relevant entries from the LDAP server with the base DN. | string |
| `pageSize` | Maximum preferred page size, measured in LDAP entries. A page size of `0` means no paging is done. | integer |

## v1.RFC2307Config

`RFC2307Config` holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the RFC 2307 schema.

| Name | Description | Schema |
|----|----|----|
| `groupsQuery` | Holds the template for an LDAP query that returns group entries. | v1.LDAPQuery |
| `groupUIDAttribute` | Defines which attribute on an LDAP group entry is interpreted as the unique identifier of the group. The default value is `ldapGroupUID`. | string |
| `groupNameAttributes` | Defines which attributes on an LDAP group entry are interpreted as the name of the group to use for an OpenShift Container Platform group. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP group entry are interpreted as the members of the group. The values contained in those attributes must be queryable by your `userUIDAttribute` field. | string array |
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userUIDAttribute` | Defines which attribute on an LDAP user entry is interpreted as the unique identifier of the user. It must correspond to values that are found from the `groupMembershipAttributes` field. | string |
| `userNameAttributes` | Defines which attributes on an LDAP user entry are used, in order, as the OpenShift Container Platform user name of the user. The first attribute with a non-empty value is used. This should match your `PreferredUsername` setting for your `LDAPPasswordIdentityProvider`. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `tolerateMemberNotFoundErrors` | Determines the behavior of the LDAP sync job when missing user entries are encountered. If `true`, an LDAP query for users that does not find any is tolerated and only an error is logged. If `false`, the LDAP sync job fails if a query for users does not find any. The default value is `false`. Misconfigured LDAP sync jobs with this flag set to `true` can cause group membership to be removed, so it is recommended to use this flag with caution. | boolean |
| `tolerateMemberOutOfScopeErrors` | Determines the behavior of the LDAP sync job when out-of-scope user entries are encountered. If `true`, an LDAP query for a user that falls outside of the base DN given for the all user query is tolerated and only an error is logged. If `false`, the LDAP sync job fails if a user query searches outside of the base DN specified by the all user query. Misconfigured LDAP sync jobs with this flag set to `true` can result in groups missing users, so it is recommended to use this flag with caution. | boolean |

## v1.ActiveDirectoryConfig

`ActiveDirectoryConfig` holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the Active Directory schema.

| Name | Description | Schema |
|----|----|----|
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userNameAttributes` | Defines which attributes on an LDAP user entry are interpreted as the OpenShift Container Platform user name of the user. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP user entry are interpreted as the LDAP groups that include the user as a member. | string array |

## v1.AugmentedActiveDirectoryConfig

The `AugmentedActiveDirectoryConfig` field holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the augmented Active Directory schema.

| Name | Description | Schema |
|----|----|----|
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userNameAttributes` | Defines which attributes on an LDAP user entry are interpreted as the OpenShift Container Platform user name of the user. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP user entry are interpreted as the LDAP groups that include the user as a member. | string array |
| `groupsQuery` | Holds the template for an LDAP query that returns group entries. | v1.LDAPQuery |
| `groupUIDAttribute` | Defines which attribute on an LDAP group entry is interpreted as the unique identifier of the group. The default value is `ldapGroupUID`. | string |
| `groupNameAttributes` | Defines which attributes on an LDAP group entry are interpreted as the name of the group to use for an OpenShift Container Platform group. | string array |

<div>

<div class="title">

Additional resources

</div>

- [LDAP nested membership sync](#ldap-syncing-nesting-about_ldap-syncing-groups)

- [Configuring an LDAP identity provider](identity_providers/configuring-ldap-identity-provider.md#configuring-ldap-identity-provider)

</div>
