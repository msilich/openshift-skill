<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Learn about authentication and authorization in OpenShift Container Platform, and how you can control access to your cluster.

# Glossary of common terms for OpenShift Container Platform authentication and authorization

This glossary defines common terms that are used in OpenShift Container Platform authentication and authorization.

authentication
An authentication determines access to an OpenShift Container Platform cluster and ensures only authenticated users access the OpenShift Container Platform cluster.

authorization
Authorization determines whether the identified user has permissions to perform the requested action.

bearer token
Bearer token is used to authenticate to API with the header `Authorization: Bearer <token>`.

<!-- -->

Cloud Credential Operator
The Cloud Credential Operator (CCO) manages cloud provider credentials as custom resource definitions (CRDs).

config map
A config map provides a way to inject configuration data into the pods. You can reference the data stored in a config map in a volume of type `ConfigMap`. Applications running in a pod can use this data.

containers
Lightweight and executable images that consist of software and all its dependencies. Because containers virtualize the operating system, you can run containers in a data center, public or private cloud, or your local host.

Custom Resource (CR)
A CR is an extension of the Kubernetes API.

group
A group is a set of users. A group is useful for granting permissions to multiple users one time.

HTPasswd
HTPasswd updates the files that store usernames and password for authentication of HTTP users.

Keystone
Keystone is an Red Hat OpenStack Platform (RHOSP) project that provides identity, token, catalog, and policy services.

Lightweight directory access protocol (LDAP)
LDAP is a protocol that queries user information.

manual mode
In manual mode, a user manages cloud credentials instead of the Cloud Credential Operator (CCO).

mint mode
In mint mode, the Cloud Credential Operator (CCO) uses the provided administrator-level cloud credential to create new credentials for components in the cluster with only the specific permissions that are required.

> [!NOTE]
> Mint mode is the default and the preferred setting for the CCO to use on the platforms for which it is supported.

namespace
A namespace isolates specific system resources that are visible to all processes. Inside a namespace, only processes that are members of that namespace can see those resources.

node
A node is a worker machine in the OpenShift Container Platform cluster. A node is either a virtual machine (VM) or a physical machine.

OAuth client
OAuth client is used to get a bearer token.

OAuth server
The OpenShift Container Platform control plane includes a built-in OAuth server that determines the user’s identity from the configured identity provider and creates an access token.

OpenID Connect
The OpenID Connect is a protocol to authenticate the users to use single sign-on (SSO) to access sites that use OpenID Providers.

passthrough mode
In passthrough mode, the Cloud Credential Operator (CCO) passes the provided cloud credential to the components that request cloud credentials.

pod
A pod is the smallest logical unit in Kubernetes. A pod consists of one or more containers to run in a worker node.

regular users
Users that are created automatically in the cluster upon first login or via the API.

request header
A request header is an HTTP header that is used to provide information about HTTP request context, so that the server can track the response of the request.

role-based access control (RBAC)
A key security control to ensure that cluster users and workloads have access to only the resources required to execute their roles.

service accounts
Service accounts are used by the cluster components or applications.

system users
Users that are created automatically when the cluster is installed.

users
Users is an entity that can make requests to API.

# About authentication in OpenShift Container Platform

To control access to an OpenShift Container Platform cluster, a cluster administrator can configure [user authentication](understanding-authentication.md#understanding-authentication) and ensure only approved users access the cluster.

To interact with an OpenShift Container Platform cluster, users must first authenticate to the OpenShift Container Platform API in some way. You can authenticate by providing an [OAuth access token or an X.509 client certificate](understanding-authentication.md#rbac-api-authentication_understanding-authentication) in your requests to the OpenShift Container Platform API.

> [!NOTE]
> If you do not present a valid access token or certificate, your request is unauthenticated and you receive an HTTP 401 error.

An administrator can configure authentication through the following tasks:

- Configuring an identity provider: You can define any [supported identity provider in OpenShift Container Platform](understanding-identity-provider.md#supported-identity-providers_understanding-identity-provider) and add it to your cluster.

- [Configuring the internal OAuth server](configuring-internal-oauth.md#configuring-internal-oauth): The OpenShift Container Platform control plane includes a built-in OAuth server that determines the user’s identity from the configured identity provider and creates an access token. You can configure the token duration and inactivity timeout, and customize the internal OAuth server URL.

  > [!NOTE]
  > Users can [view and manage OAuth tokens owned by them](managing-oauth-access-tokens.md#managing-oauth-access-tokens).

- Registering an OAuth client: OpenShift Container Platform includes several [default OAuth clients](configuring-oauth-clients.md#oauth-default-clients_configuring-oauth-clients). You can [register and configure additional OAuth clients](configuring-oauth-clients.md#oauth-register-additional-client_configuring-oauth-clients).

  > [!NOTE]
  > When users send a request for an OAuth token, they must specify either a default or custom OAuth client that receives and uses the token.

- Managing cloud provider credentials using the [Cloud Credentials Operator](managing_cloud_provider_credentials/about-cloud-credential-operator.md#about-cloud-credential-operator): Cluster components use cloud provider credentials to get permissions required to perform cluster-related tasks.

- Impersonating a system admin user: You can grant cluster administrator permissions to a user by [impersonating a system admin user](impersonating-system-admin.md#impersonating-system-admin).

# About authorization in OpenShift Container Platform

Authorization involves determining whether the identified user has permissions to perform the requested action.

Administrators can define permissions and assign them to users using the [RBAC objects, such as rules, roles, and bindings](using-rbac.md#authorization-overview_using-rbac). To understand how authorization works in OpenShift Container Platform, see [Evaluating authorization](using-rbac.md#evaluating-authorization_using-rbac).

You can also control access to an OpenShift Container Platform cluster through [projects and namespaces](using-rbac.md#rbac-projects-namespaces_using-rbac).

Along with controlling user access to a cluster, you can also control the actions a pod can perform and the resources it can access using [security context constraints (SCCs)](managing-security-context-constraints.md#managing-pod-security-policies).

You can manage authorization for OpenShift Container Platform through the following tasks:

- Viewing [local](using-rbac.md#viewing-local-roles_using-rbac) and [cluster](using-rbac.md#viewing-cluster-roles_using-rbac) roles and bindings.

- Creating a [local role](using-rbac.md#creating-local-role_using-rbac) and assigning it to a user or group.

- Creating a cluster role and assigning it to a user or group: OpenShift Container Platform includes a set of [default cluster roles](using-rbac.md#default-roles_using-rbac). You can create additional [cluster roles](using-rbac.md#creating-cluster-role_using-rbac) and [add them to a user or group](using-rbac.md#adding-roles_using-rbac).

- Creating a cluster-admin user: By default, your cluster has only one cluster administrator called `kubeadmin`. You can [create another cluster administrator](using-rbac.md#creating-cluster-admin_using-rbac). Before creating a cluster administrator, ensure that you have configured an identity provider.

  > [!NOTE]
  > After creating the cluster admin user, [delete the existing kubeadmin user](remove-kubeadmin.md#removing-kubeadmin_removing-kubeadmin) to improve cluster security.

- Creating service accounts: [Service accounts](understanding-and-creating-service-accounts.md#service-accounts-overview_understanding-service-accounts) provide a flexible way to control API access without sharing a regular user’s credentials. A user can [create and use a service account in applications](understanding-and-creating-service-accounts.md#service-accounts-managing_understanding-service-accounts) and also as [an OAuth client](using-service-accounts-as-oauth-client.md#using-service-accounts-as-oauth-client).

- [Scoping tokens](tokens-scoping.md#tokens-scoping): A scoped token is a token that identifies as a specific user who can perform only specific operations. You can create scoped tokens to delegate some of your permissions to another user or a service account.

- Syncing LDAP groups: You can manage user groups in one place by [syncing the groups stored in an LDAP server](ldap-syncing.md#ldap-syncing) with the OpenShift Container Platform user groups.
