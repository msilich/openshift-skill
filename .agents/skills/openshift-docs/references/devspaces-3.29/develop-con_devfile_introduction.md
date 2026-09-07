> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/develop-con_devfile_introduction). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Devfile in OpenShift Dev Spaces

Devfiles are `yaml` files used for development environment customization. Share devfiles across workspaces to ensure consistent build, run, and deploy behavior across your team.

Note

Red Hat OpenShift Dev Spaces is expected to work with most of the popular images defined in the `components` section of devfile. For production purposes, it is recommended to use one of the Universal Base Images (UBI) as a base image for defining the Cloud Development Environment. For a list of available base images, see Additional resources.

Warning

Some images can not be used as-is for defining Cloud Development Environment. Visual Studio Code - Open Source ("Code - OSS") can not be started in containers that are missing `openssl` and `libbrotli`. Install missing libraries explicitly on the Dockerfile level, for example `RUN yum install compat-openssl11 libbrotli`.

<span id="devfile-introduction_devspaces___devfile_and_universal_developer_image"></span>

## [Devfile and Universal Developer Image](develop-con_devfile_introduction.md#devfile-introduction_devspaces___devfile_and_universal_developer_image)

You do not need a devfile to start a workspace. If you do not include a devfile in your project repository, Red Hat OpenShift Dev Spaces automatically loads a default devfile with a Universal Developer Image (UDI).

<span id="devfile-introduction_devspaces___devfile_registry"></span>

## [Devfile Registry](develop-con_devfile_introduction.md#devfile-introduction_devspaces___devfile_registry)

The Devfile Registry contains ready-to-use community-supported devfiles for different languages and technologies. Devfiles included in the registry should be treated as samples rather than templates. To browse the registry, see Additional resources.

**Related information**  

- [What is a devfile](https://devfile.io/docs/2.3.0/what-is-a-devfile)
- [Benefits of devfile](https://devfile.io/docs/2.3.0/benefits-of-devfile)
- [Devfile customization overview](https://devfile.io/docs/2.3.0/overview)
- [Devfile.io](https://devfile.io/)
- [Universal Base Images](https://catalog.redhat.com/software/containers/search?gs&q=ubi)
- [Devfile Registry](https://registry.devfile.io/viewer)
- [Customizing Cloud Development Environments](https://che.eclipseprojects.io/2024/02/05/@mario.loriedo-cde-customization.html)
