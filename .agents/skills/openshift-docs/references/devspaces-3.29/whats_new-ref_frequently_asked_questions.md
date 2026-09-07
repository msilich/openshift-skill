> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_frequently_asked_questions). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Frequently asked questions

The following are common questions about Red Hat OpenShift Dev Spaces.

Is it possible to deploy applications from OpenShift Dev Spaces to an OpenShift cluster?  
The OpenShift user token is automatically injected into workspace containers, which makes it possible to run `oc` commands against the OpenShift cluster.

For best performance, what is the recommended storage to use for Persistent Volumes used with OpenShift Dev Spaces?  
Use block storage.

Is it possible to deploy more than one OpenShift Dev Spaces instance on the same cluster?  
Only one OpenShift Dev Spaces instance can be deployed per cluster.

Is it possible to install OpenShift Dev Spaces offline (that is, disconnected from the internet)?  
See [Installing Red Hat OpenShift Dev Spaces in restricted environments on OpenShift](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/installation_guide/index#installing-devspaces-in-a-restricted-environment_devspaces).

Is it possible to use non-default certificates with OpenShift Dev Spaces?  
You can use self-signed or public certificates. See [Importing untrusted TLS certificates](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/configure_infra/index#importing-untrusted-tls-certificates_devspaces).

Is it possible to run multiple workspaces simultaneously?  
See [Enabling users to run multiple workspaces simultaneously](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/configure_workspaces/index#enabling-users-to-run-multiple-workspaces-simultaneously_devspaces).

Is it possible to configure OpenShift Dev Spaces to use open-vsx.org?  
Yes, but this is not the default configuration. While you can connect to the public **Open VSX Registry**, consider these factors:

- Service limits: API usage is organized into defined tiers. The Eclipse Foundation implements these limits to protect infrastructure from high-frequency automated traffic and to provide consistent service quality for all users. For more information, see [Rate Limits and Usage Tiers](https://github.com/EclipseFdn/open-vsx.org/wiki/rate-limiting) and the [open-vsx.org wiki](https://github.com/EclipseFdn/open-vsx.org/wiki).

- Security and stability: The public registry does not have an official service-level agreement (SLA) and poses potential security risks from unvetted extensions.

  For a secure, stable, and high-performance environment, use a self-hosted registry with a curated set of extensions that meet your organization’s requirements.
