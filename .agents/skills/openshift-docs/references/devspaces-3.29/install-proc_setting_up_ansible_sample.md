> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/install-proc_setting_up_ansible_sample). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Enable the Ansible sample in a restricted environment

Enable the Ansible getting-started sample in a restricted OpenShift Dev Spaces environment by mirroring the required container images and allowing access to the Ansible Galaxy domains.

## Before you begin

- You have Microsoft Visual Studio Code - Open Source IDE as the configured editor.
- You have a 64-bit x86 system.

## Procedure

1.  Mirror the following images:

    ``` bash
    ghcr.io/ansible/ansible-devspaces@sha256:d7711d5205a89c0c2b71d0937d70916feabcda343b7522da6413aa762b506c65
    registry.access.redhat.com/ubi8/python-39@sha256:301fec66443f80c3cc507ccaf72319052db5a1dc56deb55c8f169011d4bbaacb
    ```

2.  Configure the cluster proxy to allow access to the following domains:

    ``` bash
    .ansible.com
    .ansible-galaxy-ng.s3.dualstack.us-east-1.amazonaws.com
    ```

    Note

    Support for the following IDE and CPU architectures is planned for a future release:

    - CPU architectures
      - IBM Power (ppc64le)
      - IBM Z (s390x)

## Results

- Verify that the mirrored images are accessible from the OpenShift cluster.

**Related tasks**  

- [Deploy using the CLI](install-proc_installing_dev_spaces_using_cli.md "Deploy OpenShift Dev Spaces from the command line using the dsc management tool so that you have full control over configuration options and can automate the installation.")
- [Deploy using the web console](install-proc_installing_dev_spaces_using_web_console.md "Deploy OpenShift Dev Spaces through the OpenShift web console using the standard OperatorHub workflow so that you can install without command-line access.")
- [Deploy in an air-gapped environment](install-proc_installing_dev_spaces_in_a_restricted_environment_on_openshift.md "Deploy OpenShift Dev Spaces on an OpenShift cluster with no internet access by mirroring the required container images and Operator catalogs to a private registry.")
