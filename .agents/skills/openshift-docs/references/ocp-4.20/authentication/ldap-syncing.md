<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

As an administrator, you can use groups to manage users, change their permissions, and enhance collaboration. Your organization may have already created user groups and stored them in an LDAP server. OpenShift Container Platform can sync those LDAP records with internal OpenShift Container Platform records, enabling you to manage your groups in one place. OpenShift Container Platform currently supports group sync with LDAP servers using three common schemas for defining group membership: RFC 2307, Active Directory, and augmented Active Directory.

For more information on configuring LDAP, see [Configuring an LDAP identity provider](identity_providers/configuring-ldap-identity-provider.md#configuring-ldap-identity-provider).

> [!NOTE]
> You must have `cluster-admin` privileges to sync groups.

# About configuring LDAP sync

Before you can run LDAP sync, you need a sync configuration file. This file contains the following LDAP client configuration details:

- Configuration for connecting to your LDAP server.

- Sync configuration options that are dependent on the schema used in your LDAP server.

- An administrator-defined list of name mappings that maps OpenShift Container Platform group names to groups in your LDAP server.

The format of the configuration file depends upon the schema you are using: RFC 2307, Active Directory, or augmented Active Directory.

LDAP client configuration
The LDAP client configuration section of the configuration defines the connections to your LDAP server.

The LDAP client configuration section of the configuration defines the connections to your LDAP server.

<div class="formalpara">

<div class="title">

LDAP client configuration

</div>

``` yaml
url: ldap://10.0.0.0:389
bindDN: cn=admin,dc=example,dc=com
bindPassword: <password>
insecure: false
ca: my-ldap-ca-bundle.crt
```

</div>

- The connection protocol, IP address of the LDAP server hosting your database, and the port to connect to, formatted as `scheme://host:port`.

- Optional distinguished name (DN) to use as the Bind DN. OpenShift Container Platform uses this if elevated privilege is required to retrieve entries for the sync operation.

- Optional password to use to bind. OpenShift Container Platform uses this if elevated privilege is necessary to retrieve entries for the sync operation. This value may also be provided in an environment variable, external file, or encrypted file.

- When `false`, secure LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.

- The certificate bundle to use for validating server certificates for the configured URL. If empty, OpenShift Container Platform uses system-trusted roots. This only applies if `insecure` is set to `false`.

LDAP query definition
Sync configurations consist of LDAP query definitions for the entries that are required for synchronization. The specific definition of an LDAP query depends on the schema used to store membership information in the LDAP server.

<div class="formalpara">

<div class="title">

LDAP query definition

</div>

``` yaml
baseDN: ou=users,dc=example,dc=com
scope: sub
derefAliases: never
timeout: 0
filter: (objectClass=person)
pageSize: 0
```

</div>

- The distinguished name (DN) of the branch of the directory where all searches will start from. It is required that you specify the top of your directory tree, but you can also specify a subtree in the directory.

- The scope of the search. Valid values are `base`, `one`, or `sub`. If this is left undefined, then a scope of `sub` is assumed. Descriptions of the scope options can be found in the table below.

- The behavior of the search with respect to aliases in the LDAP tree. Valid values are `never`, `search`, `base`, or `always`. If this is left undefined, then the default is to `always` dereference aliases. Descriptions of the dereferencing behaviors can be found in the table below.

- The time limit allowed for the search by the client, in seconds. A value of `0` imposes no client-side limit.

- A valid LDAP search filter. If this is left undefined, then the default is `(objectClass=*)`.

- The optional maximum size of response pages from the server, measured in LDAP entries. If set to `0`, no size restrictions will be made on pages of responses. Setting paging sizes is necessary when queries return more entries than the client or server allow by default.

| LDAP search scope | Description |
|----|----|
| `base` | Only consider the object specified by the base DN given for the query. |
| `one` | Consider all of the objects on the same level in the tree as the base DN for the query. |
| `sub` | Consider the entire subtree rooted at the base DN given for the query. |

LDAP search scope options {#ldap-search}

| Dereferencing behavior | Description |
|----|----|
| `never` | Never dereference any aliases found in the LDAP tree. |
| `search` | Only dereference aliases found while searching. |
| `base` | Only dereference aliases while finding the base object. |
| `always` | Always dereference all aliases found in the LDAP tree. |

LDAP dereferencing behaviors {#deref-aliases}

User-defined name mapping
A user-defined name mapping explicitly maps the names of OpenShift Container Platform groups to unique identifiers that find groups on your LDAP server. The mapping uses normal YAML syntax. A user-defined mapping can contain an entry for every group in your LDAP server or only a subset of those groups. If there are groups on the LDAP server that do not have a user-defined name mapping, the default behavior during sync is to use the attribute specified as the OpenShift Container Platform group’s name.

<div class="formalpara">

<div class="title">

User-defined name mapping

</div>

``` yaml
groupUIDNameMapping:
  "cn=group1,ou=groups,dc=example,dc=com": firstgroup
  "cn=group2,ou=groups,dc=example,dc=com": secondgroup
  "cn=group3,ou=groups,dc=example,dc=com": thirdgroup
```

</div>

## About the RFC 2307 configuration file

The RFC 2307 schema requires you to provide an LDAP query definition for both user and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user- or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships:

> [!NOTE]
> If using user-defined name mappings, your configuration file will differ.

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses RFC 2307 schema: `rfc2307_config.yaml`

</div>

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

</div>

- The IP address and host of the LDAP server where this group’s record is stored.

- When `false`, secure LDAP (`ldaps://`) URLs connect using TLS, and insecure LDAP (`ldap://`) URLs are upgraded to TLS. When `true`, no TLS connection is made to the server and you cannot use `ldaps://` URL schemes.

- The attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for `groupUIDAttribute`. For fine-grained filtering, use the whitelist / blacklist method.

- The attribute to use as the name of the group.

- The attribute on the group that stores the membership information.

- The attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.

- The attribute to use as the name of the user in the OpenShift Container Platform group record.

## About the Active Directory configuration file

The Active Directory schema requires you to provide an LDAP query definition for user entries, as well as the attributes to represent them with in the internal OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user- or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, but define the name of the group by the name of the group on the LDAP server. The following configuration file creates these relationships:

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses Active Directory schema: `active_directory_config.yaml`

</div>

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

</div>

- The attribute to use as the name of the user in the OpenShift Container Platform group record.

- The attribute on the user that stores the membership information.

## About the augmented Active Directory configuration file

The augmented Active Directory schema requires you to provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user- or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships.

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses augmented Active Directory schema: `augmented_active_directory_config.yaml`

</div>

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

</div>

- The attribute that uniquely identifies a group on the LDAP server. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.

- The attribute to use as the name of the group.

- The attribute to use as the name of the user in the OpenShift Container Platform group record.

- The attribute on the user that stores the membership information.

# Running LDAP sync

Once you have created a sync configuration file, you can begin to sync. OpenShift Container Platform allows administrators to perform a number of different sync types with the same server.

## Syncing the LDAP server with OpenShift Container Platform

You can sync all groups from the LDAP server with OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- Create a sync configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- To sync all groups from the LDAP server with OpenShift Container Platform:

  ``` terminal
  $ oc adm groups sync --sync-config=config.yaml --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

## Syncing OpenShift Container Platform groups with the LDAP server

You can sync all groups already in OpenShift Container Platform that correspond to groups in the LDAP server specified in the configuration file.

<div>

<div class="title">

Prerequisites

</div>

- Create a sync configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- To sync OpenShift Container Platform groups with the LDAP server:

  ``` terminal
  $ oc adm groups sync --type=openshift --sync-config=config.yaml --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

## Syncing subgroups from the LDAP server with OpenShift Container Platform

You can sync a subset of LDAP groups with OpenShift Container Platform using whitelist files, blacklist files, or both.

> [!NOTE]
> You can use any combination of blacklist files, whitelist files, or whitelist literals. Whitelist and blacklist files must contain one unique group identifier per line, and you can include whitelist literals directly in the command itself. These guidelines apply to groups found on LDAP servers as well as groups already present in OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- Create a sync configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- To sync a subset of LDAP groups with OpenShift Container Platform, use any the following commands:

  ``` terminal
  $ oc adm groups sync --whitelist=<whitelist_file> \
                     --sync-config=config.yaml      \
                     --confirm
  ```

  ``` terminal
  $ oc adm groups sync --blacklist=<blacklist_file> \
                     --sync-config=config.yaml      \
                     --confirm
  ```

  ``` terminal
  $ oc adm groups sync <group_unique_identifier>    \
                     --sync-config=config.yaml      \
                     --confirm
  ```

  ``` terminal
  $ oc adm groups sync <group_unique_identifier>  \
                     --whitelist=<whitelist_file> \
                     --blacklist=<blacklist_file> \
                     --sync-config=config.yaml    \
                     --confirm
  ```

  ``` terminal
  $ oc adm groups sync --type=openshift           \
                     --whitelist=<whitelist_file> \
                     --sync-config=config.yaml    \
                     --confirm
  ```

  > [!NOTE]
  > By default, all group synchronization operations are dry-run, so you must set the `--confirm` flag on the `oc adm groups sync` command to make changes to OpenShift Container Platform group records.

</div>

# Running a group pruning job

An administrator can also choose to remove groups from OpenShift Container Platform records if the records on the LDAP server that created them are no longer present. The prune job will accept the same sync configuration file and whitelists or blacklists as used for the sync job.

For example:

``` terminal
$ oc adm prune groups --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

``` terminal
$ oc adm prune groups --whitelist=/path/to/whitelist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

``` terminal
$ oc adm prune groups --blacklist=/path/to/blacklist.txt --sync-config=/path/to/ldap-sync-config.yaml --confirm
```

# Automatically syncing LDAP groups

You can automatically sync LDAP groups on a periodic basis by configuring a cron job.

<div>

<div class="title">

Prerequisites

</div>

- You have access to the cluster as a user with the `cluster-admin` role.

- You have configured an LDAP identity provider (IDP).

  This procedure assumes that you created an LDAP secret named `ldap-secret` and a config map named `ca-config-map`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a project where the cron job will run:

    ``` terminal
    $ oc new-project ldap-sync
    ```

    - This procedure uses a project called `ldap-sync`.

2.  Locate the secret and config map that you created when configuring the LDAP identity provider and copy them to this new project.

    The secret and config map exist in the `openshift-config` project and must be copied to the new `ldap-sync` project.

3.  Define a service account:

    <div class="formalpara">

    <div class="title">

    Example `ldap-sync-service-account.yaml`

    </div>

    ``` yaml
    kind: ServiceAccount
    apiVersion: v1
    metadata:
      name: ldap-group-syncer
      namespace: ldap-sync
    ```

    </div>

4.  Create the service account:

    ``` terminal
    $ oc create -f ldap-sync-service-account.yaml
    ```

5.  Define a cluster role:

    <div class="formalpara">

    <div class="title">

    Example `ldap-sync-cluster-role.yaml`

    </div>

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

    </div>

6.  Create the cluster role:

    ``` terminal
    $ oc create -f ldap-sync-cluster-role.yaml
    ```

7.  Define a cluster role binding to bind the cluster role to the service account:

    <div class="formalpara">

    <div class="title">

    Example `ldap-sync-cluster-role-binding.yaml`

    </div>

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

    </div>

    - Reference to the service account created earlier in this procedure.

    - Reference to the cluster role created earlier in this procedure.

8.  Create the cluster role binding:

    ``` terminal
    $ oc create -f ldap-sync-cluster-role-binding.yaml
    ```

9.  Define a config map that specifies the sync configuration file:

    <div class="formalpara">

    <div class="title">

    Example `ldap-sync-config-map.yaml`

    </div>

    ``` yaml
    kind: ConfigMap
    apiVersion: v1
    metadata:
      name: ldap-group-syncer
      namespace: ldap-sync
    data:
      sync.yaml: |
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

    </div>

    - Define the sync configuration file.

    - Specify the URL.

    - Specify the `bindDN`.

    - This example uses the RFC2307 schema; adjust values as necessary. You can also use a different schema.

    - Specify the `baseDN` for `groupsQuery`.

    - Specify the `baseDN` for `usersQuery`.

10. Create the config map:

    ``` terminal
    $ oc create -f ldap-sync-config-map.yaml
    ```

11. Define a cron job:

    <div class="formalpara">

    <div class="title">

    Example `ldap-sync-cron-job.yaml`

    </div>

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

    </div>

    - Configure the settings for the cron job. See "Creating cron jobs" for more information on cron job settings.

    - The schedule for the job specified in [cron format](https://en.wikipedia.org/wiki/Cron). This example cron job runs every 30 minutes. Adjust the frequency as necessary, making sure to take into account how long the sync takes to run.

    - How long, in seconds, to keep finished jobs. This should match the period of the job schedule in order to clean old failed jobs and prevent unnecessary alerts. For more information, see [TTL-after-finished Controller](https://kubernetes.io/docs/concepts/workloads/controllers/ttlafterfinished) in the Kubernetes documentation.

    - The LDAP sync command for the cron job to run. Passes in the sync configuration file that was defined in the config map.

    - This secret was created when the LDAP IDP was configured.

    - This config map was created when the LDAP IDP was configured.

12. Create the cron job:

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

This section contains examples for the RFC 2307, Active Directory, and augmented Active Directory schemas.

> [!NOTE]
> These examples assume that all users are direct members of their respective groups. Specifically, no groups have other groups as members. See the Nested Membership Sync Example for information on how to sync nested groups.

## Syncing groups using the RFC 2307 schema

For the RFC 2307 schema, the following examples synchronize a group named `admins` that has two members: `Jane` and `Jim`. The examples explain:

- How the group and users are added to the LDAP server.

- What the resulting group record in OpenShift Container Platform will be after synchronization.

> [!NOTE]
> These examples assume that all users are direct members of their respective groups. Specifically, no groups have other groups as members. See the Nested Membership Sync Example for information on how to sync nested groups.

In the RFC 2307 schema, both users (Jane and Jim) and groups exist on the LDAP server as first-class entries, and group membership is stored in attributes on the group. The following snippet of `ldif` defines the users and group for this schema:

<div class="formalpara">

<div class="title">

LDAP entries that use RFC 2307 schema: `rfc2307.ldif`

</div>

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

</div>

- The group is a first-class entry in the LDAP server.

- Members of a group are listed with an identifying reference as attributes on the group.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `rfc2307_config.yaml` file:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `rfc2307_config.yaml` file

  </div>

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

  </div>

  - The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.

  - The unique identifier for the group on the LDAP server.

  - The IP address and host of the LDAP server where this group’s record is stored.

  - The name of the group as specified by the sync file.

  - The users that are members of the group, named as specified by the sync file.

</div>

## Syncing groups using the RFC2307 schema with user-defined name mappings

When syncing groups with user-defined name mappings, the configuration file changes to contain these mappings as shown below.

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses RFC 2307 schema with user-defined name mappings: `rfc2307_config_user_defined.yaml`

</div>

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

</div>

- The user-defined name mapping.

- The unique identifier attribute that is used for the keys in the user-defined name mapping. You cannot specify `groupsQuery` filters when using DN for groupUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.

- The attribute to name OpenShift Container Platform groups with if their unique identifier is not in the user-defined name mapping.

- The attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `rfc2307_config_user_defined.yaml` file:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config_user_defined.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `rfc2307_config_user_defined.yaml` file

  </div>

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

  </div>

  - The name of the group as specified by the user-defined name mapping.

</div>

## Syncing groups using RFC 2307 with user-defined error tolerances

By default, if the groups being synced contain members whose entries are outside of the scope defined in the member query, the group sync fails with an error:

    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with dn="<user-dn>" would search outside of the base dn specified (dn="<base-dn>")".

This often indicates a misconfigured `baseDN` in the `usersQuery` field. However, in cases where the `baseDN` intentionally does not contain some of the members of the group, setting `tolerateMemberOutOfScopeErrors: true` allows the group sync to continue. Out of scope members will be ignored.

Similarly, when the group sync process fails to locate a member for a group, it fails outright with errors:

    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" refers to a non-existent entry".
    Error determining LDAP group membership for "<group>": membership lookup for user "<user>" in group "<group>" failed because of "search for entry with base dn="<user-dn>" and filter "<filter>" did not return any results".

This often indicates a misconfigured `usersQuery` field. However, in cases where the group contains member entries that are known to be missing, setting `tolerateMemberNotFoundErrors: true` allows the group sync to continue. Problematic members will be ignored.

> [!WARNING]
> Enabling error tolerances for the LDAP group sync causes the sync process to ignore problematic member entries. If the LDAP group sync is not configured correctly, this could result in synced OpenShift Container Platform groups missing members.

<div class="formalpara">

<div class="title">

LDAP entries that use RFC 2307 schema with problematic group membership: `rfc2307_problematic_users.ldif`

</div>

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

</div>

- A member that does not exist on the LDAP server.

- A member that may exist, but is not under the `baseDN` in the user query for the sync job.

To tolerate the errors in the above example, the following additions to your sync configuration file must be made:

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses RFC 2307 schema tolerating errors: `rfc2307_config_tolerating.yaml`

</div>

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

</div>

- The attribute that uniquely identifies a user on the LDAP server. You cannot specify `usersQuery` filters when using DN for userUIDAttribute. For fine-grained filtering, use the whitelist / blacklist method.

- When `true`, the sync job tolerates groups for which some members were not found, and members whose LDAP entries are not found are ignored. The default behavior for the sync job is to fail if a member of a group is not found.

- When `true`, the sync job tolerates groups for which some members are outside the user scope given in the `usersQuery` base DN, and members outside the member query scope are ignored. The default behavior for the sync job is to fail if a member of a group is out of scope.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `rfc2307_config_tolerating.yaml` file:

  ``` terminal
  $ oc adm groups sync --sync-config=rfc2307_config_tolerating.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `rfc2307_config.yaml` file

  </div>

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

  </div>

  - The users that are members of the group, as specified by the sync file. Members for which lookup encountered tolerated errors are absent.

</div>

## Syncing groups using the Active Directory schema

In the Active Directory schema, both users (Jane and Jim) exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema:

<div class="formalpara">

<div class="title">

LDAP entries that use Active Directory schema: `active_directory.ldif`

</div>

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

</div>

- The user’s group memberships are listed as attributes on the user, and the group does not exist as an entry on the server. The `memberOf` attribute does not have to be a literal attribute on the user; in some LDAP servers, it is created during search and returned to the client, but not committed to the database.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `active_directory_config.yaml` file:

  ``` terminal
  $ oc adm groups sync --sync-config=active_directory_config.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `active_directory_config.yaml` file

  </div>

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

  </div>

  - The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.

  - The unique identifier for the group on the LDAP server.

  - The IP address and host of the LDAP server where this group’s record is stored.

  - The name of the group as listed in the LDAP server.

  - The users that are members of the group, named as specified by the sync file.

</div>

## Syncing groups using the augmented Active Directory schema

In the augmented Active Directory schema, both users (Jane and Jim) and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user. The following snippet of `ldif` defines the users and group for this schema:

<div class="formalpara">

<div class="title">

LDAP entries that use augmented Active Directory schema: `augmented_active_directory.ldif`

</div>

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

</div>

- The user’s group memberships are listed as attributes on the user.

- The group is a first-class entry on the LDAP server.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `augmented_active_directory_config.yaml` file:

  ``` terminal
  $ oc adm groups sync --sync-config=augmented_active_directory_config.yaml --confirm
  ```

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `augmented_active_directory_config.yaml` file

  </div>

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

  </div>

  - The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.

  - The unique identifier for the group on the LDAP server.

  - The IP address and host of the LDAP server where this group’s record is stored.

  - The name of the group as specified by the sync file.

  - The users that are members of the group, named as specified by the sync file.

</div>

### LDAP nested membership sync example

Groups in OpenShift Container Platform do not nest. The LDAP server must flatten group membership before the data can be consumed. Microsoft’s Active Directory Server supports this feature via the `LDAP_MATCHING_RULE_IN_CHAIN` rule, which has the OID `1.2.840.113556.1.4.1941`. Furthermore, only explicitly whitelisted groups can be synced when using this matching rule.

This section has an example for the augmented Active Directory schema, which synchronizes a group named `admins` that has one user `Jane` and one group `otheradmins` as members. The `otheradmins` group has one user member: `Jim`. This example explains:

- How the group and users are added to the LDAP server.

- What the LDAP sync configuration file looks like.

- What the resulting group record in OpenShift Container Platform will be after synchronization.

In the augmented Active Directory schema, both users (`Jane` and `Jim`) and groups exist in the LDAP server as first-class entries, and group membership is stored in attributes on the user or the group. The following snippet of `ldif` defines the users and groups for this schema:

<div class="formalpara">

<div class="title">

LDAP entries that use augmented Active Directory schema with nested members: `augmented_active_directory_nested.ldif`

</div>

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

</div>

- The user’s and group’s memberships are listed as attributes on the object.

- The groups are first-class entries on the LDAP server.

- The `otheradmins` group is a member of the `admins` group.

When syncing nested groups with Active Directory, you must provide an LDAP query definition for both user entries and group entries, as well as the attributes with which to represent them in the internal OpenShift Container Platform group records. Furthermore, certain changes are required in this configuration:

- The `oc adm groups sync` command must explicitly whitelist groups.

- The user’s `groupMembershipAttributes` must include `"memberOf:1.2.840.113556.1.4.1941:"` to comply with the `LDAP_MATCHING_RULE_IN_CHAIN` rule.

- The `groupUIDAttribute` must be set to `dn`.

- The `groupsQuery`:

  - Must not set `filter`.

  - Must set a valid `derefAliases`.

  - Should not set `baseDN` as that value is ignored.

  - Should not set `scope` as that value is ignored.

For clarity, the group you create in OpenShift Container Platform should use attributes other than the distinguished name whenever possible for user- or administrator-facing fields. For example, identify the users of an OpenShift Container Platform group by their e-mail, and use the name of the group as the common name. The following configuration file creates these relationships:

<div class="formalpara">

<div class="title">

LDAP sync configuration that uses augmented Active Directory schema with nested members: `augmented_active_directory_config_nested.yaml`

</div>

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

</div>

- `groupsQuery` filters cannot be specified. The `groupsQuery` base DN and scope values are ignored. `groupsQuery` must set a valid `derefAliases`.

- The attribute that uniquely identifies a group on the LDAP server. It must be set to `dn`.

- The attribute to use as the name of the group.

- The attribute to use as the name of the user in the OpenShift Container Platform group record.

  > [!NOTE]
  > `mail` or `sAMAccountName` are preferred choices in most installations.

- The attribute on the user that stores the membership information. Note the use of `LDAP_MATCHING_RULE_IN_CHAIN`.

<div>

<div class="title">

Prerequisites

</div>

- Create the configuration file.

- You have access to the cluster as a user with the `cluster-admin` role.

</div>

<div>

<div class="title">

Procedure

</div>

- Run the sync with the `augmented_active_directory_config_nested.yaml` file:

  ``` terminal
  $ oc adm groups sync \
      'cn=admins,ou=groups,dc=example,dc=com' \
      --sync-config=augmented_active_directory_config_nested.yaml \
      --confirm
  ```

  > [!NOTE]
  > You must explicitly whitelist the `cn=admins,ou=groups,dc=example,dc=com` group.

  OpenShift Container Platform creates the following group record as a result of the above sync operation:

  <div class="formalpara">

  <div class="title">

  OpenShift Container Platform group created by using the `augmented_active_directory_config_nested.yaml` file

  </div>

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

  </div>

  - The last time this OpenShift Container Platform group was synchronized with the LDAP server, in ISO 6801 format.

  - The unique identifier for the group on the LDAP server.

  - The IP address and host of the LDAP server where this group’s record is stored.

  - The name of the group as specified by the sync file.

  - The users that are members of the group, named as specified by the sync file. Note that members of nested groups are included since the group membership was flattened by the Microsoft Active Directory Server.

</div>

# LDAP sync configuration specification

The object specification for the configuration file is below. Note that the different schema objects have different fields. For example, v1.ActiveDirectoryConfig has no `groupsQuery` field whereas v1.RFC2307Config and v1.AugmentedActiveDirectoryConfig both do.

> [!IMPORTANT]
> There is no support for binary attributes. All attribute data coming from the LDAP server must be in the format of a UTF-8 encoded string. For example, never use a binary attribute, such as `objectGUID`, as an ID attribute. You must use string attributes, such as `sAMAccountName` or `userPrincipalName`, instead.

## v1.LDAPSyncConfig

`LDAPSyncConfig` holds the necessary configuration options to define an LDAP group sync.

| Name | Description | Schema |
|----|----|----|
| `kind` | String value representing the REST resource this object represents. Servers may infer this from the endpoint the client submits requests to. Cannot be updated. In CamelCase. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#types-kinds> | string |
| `apiVersion` | Defines the versioned schema of this representation of an object. Servers should convert recognized schemas to the latest internal value, and may reject unrecognized values. More info: <https://github.com/kubernetes/community/blob/master/contributors/devel/sig-architecture/api-conventions.md#resources> | string |
| `url` | Host is the scheme, host and port of the LDAP server to connect to: `scheme://host:port` | string |
| `bindDN` | Optional DN to bind to the LDAP server with. | string |
| `bindPassword` | Optional password to bind with during the search phase. | v1.StringSource |
| `insecure` | If `true`, indicates the connection should not use TLS. If `false`, `ldaps://` URLs connect using TLS, and `ldap://` URLs are upgraded to a TLS connection using StartTLS as specified in <https://tools.ietf.org/html/rfc2830>. If you set `insecure` to `true`, you cannot use `ldaps://` URL schemes. | boolean |
| `ca` | Optional trusted certificate authority bundle to use when making requests to the server. If empty, the default system roots are used. | string |
| `groupUIDNameMapping` | Optional direct mapping of LDAP group UIDs to OpenShift Container Platform group names. | object |
| `rfc2307` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to RFC2307: first-class group and user entries, with group membership determined by a multi-valued attribute on the group entry listing its members. | v1.RFC2307Config |
| `activeDirectory` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory: first-class user entries, with group membership determined by a multi-valued attribute on members listing groups they are a member of. | v1.ActiveDirectoryConfig |
| `augmentedActiveDirectory` | Holds the configuration for extracting data from an LDAP server set up in a fashion similar to that used in Active Directory as described above, with one addition: first-class group entries exist and are used to hold metadata but not group membership. | v1.AugmentedActiveDirectoryConfig |

## v1.StringSource

`StringSource` allows specifying a string inline, or externally via environment variable or file. When it contains only a string value, it marshals to a simple JSON string.

| Name | Description | Schema |
|----|----|----|
| `value` | Specifies the cleartext value, or an encrypted value if `keyFile` is specified. | string |
| `env` | Specifies an environment variable containing the cleartext value, or an encrypted value if the `keyFile` is specified. | string |
| `file` | References a file containing the cleartext value, or an encrypted value if a `keyFile` is specified. | string |
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
| `pageSize` | Maximum preferred page size, measured in LDAP entries. A page size of `0` means no paging will be done. | integer |

## v1.RFC2307Config

`RFC2307Config` holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the RFC2307 schema.

| Name | Description | Schema |
|----|----|----|
| `groupsQuery` | Holds the template for an LDAP query that returns group entries. | v1.LDAPQuery |
| `groupUIDAttribute` | Defines which attribute on an LDAP group entry will be interpreted as its unique identifier. (`ldapGroupUID`) | string |
| `groupNameAttributes` | Defines which attributes on an LDAP group entry will be interpreted as its name to use for an OpenShift Container Platform group. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP group entry will be interpreted as its members. The values contained in those attributes must be queryable by your `UserUIDAttribute`. | string array |
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userUIDAttribute` | Defines which attribute on an LDAP user entry will be interpreted as its unique identifier. It must correspond to values that will be found from the `GroupMembershipAttributes`. | string |
| `userNameAttributes` | Defines which attributes on an LDAP user entry will be used, in order, as its OpenShift Container Platform user name. The first attribute with a non-empty value is used. This should match your `PreferredUsername` setting for your `LDAPPasswordIdentityProvider`. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `tolerateMemberNotFoundErrors` | Determines the behavior of the LDAP sync job when missing user entries are encountered. If `true`, an LDAP query for users that does not find any will be tolerated and an only and error will be logged. If `false`, the LDAP sync job will fail if a query for users does not find any. The default value is `false`. Misconfigured LDAP sync jobs with this flag set to `true` can cause group membership to be removed, so it is recommended to use this flag with caution. | boolean |
| `tolerateMemberOutOfScopeErrors` | Determines the behavior of the LDAP sync job when out-of-scope user entries are encountered. If `true`, an LDAP query for a user that falls outside of the base DN given for the all user query will be tolerated and only an error will be logged. If `false`, the LDAP sync job will fail if a user query would search outside of the base DN specified by the all user query. Misconfigured LDAP sync jobs with this flag set to `true` can result in groups missing users, so it is recommended to use this flag with caution. | boolean |

## v1.ActiveDirectoryConfig

`ActiveDirectoryConfig` holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the Active Directory schema.

| Name | Description | Schema |
|----|----|----|
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userNameAttributes` | Defines which attributes on an LDAP user entry will be interpreted as its OpenShift Container Platform user name. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP user entry will be interpreted as the groups it is a member of. | string array |

## v1.AugmentedActiveDirectoryConfig

`AugmentedActiveDirectoryConfig` holds the necessary configuration options to define how an LDAP group sync interacts with an LDAP server using the augmented Active Directory schema.

| Name | Description | Schema |
|----|----|----|
| `usersQuery` | Holds the template for an LDAP query that returns user entries. | v1.LDAPQuery |
| `userNameAttributes` | Defines which attributes on an LDAP user entry will be interpreted as its OpenShift Container Platform user name. The attribute to use as the name of the user in the OpenShift Container Platform group record. `mail` or `sAMAccountName` are preferred choices in most installations. | string array |
| `groupMembershipAttributes` | Defines which attributes on an LDAP user entry will be interpreted as the groups it is a member of. | string array |
| `groupsQuery` | Holds the template for an LDAP query that returns group entries. | v1.LDAPQuery |
| `groupUIDAttribute` | Defines which attribute on an LDAP group entry will be interpreted as its unique identifier. (`ldapGroupUID`) | string |
| `groupNameAttributes` | Defines which attributes on an LDAP group entry will be interpreted as its name to use for an OpenShift Container Platform group. | string array |
