<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Impersonation allows you to create a project as a different user.

# API impersonation

You can configure a request to the OpenShift Container Platform API to act as though it originated from another user. For more information, see [User impersonation](https://kubernetes.io/docs/reference/access-authn-authz/authentication/#user-impersonation) in the Kubernetes documentation.

# Impersonating a user when you create a project

You can impersonate a different user when you create a project request. Because `system:authenticated:oauth` is the only bootstrap group that can create project requests, you must impersonate that group.

<div>

<div class="title">

Procedure

</div>

- To create a project request on behalf of a different user:

  ``` terminal
  $ oc new-project <project> --as=<user> \
      --as-group=system:authenticated --as-group=system:authenticated:oauth
  ```

</div>
