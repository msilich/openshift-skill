<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes (RHACS) integrates with a variety of continuous integration (CI) products. Before you deploy images, you can use RHACS to apply build-time and deploy-time security rules to your images.

After images are built and pushed to a registry, RHACS integrates into CI pipelines. Pushing the image first allows developers to continue testing their artifacts while dealing with any policy violations alongside any other CI test failures, linter violations, or other problems.

If possible, configure the version control system to block pull or merge requests from being merged if the build stage, which includes RHACS checks, fails.

The integration with your CI product functions by contacting your RHACS installation to check whether the image complies with build-time policies you have configured. If there are policy violations, a detailed message is displayed on the console log, including the policy description, rationale, and remediation instructions.

Each policy includes an optional enforcement setting. If you mark a policy for build-time enforcement, failure of that policy causes the client to exit with a nonzero error code.

To integrate Red Hat Advanced Cluster Security for Kubernetes with your CI system, follow these steps:

1.  [Configure build policies](integrate-with-ci-systems.md#configure-build-policies).

2.  [Configure a registry integration](integrate-with-ci-systems.md#configure-registry-integration).

3.  [Configure access](integrate-with-ci-systems.md#configure-access) to your RHACS instance.

4.  [Integrate with your CI pipeline](integrate-with-ci-systems.md#integrate-with-your-ci-pipeline).

<a id="configure-build-policies"></a>

# Configuring build policies

You can check RHACS policies during builds.

<div>

<div class="title">

Procedure

</div>

1.  Configure policies that apply to the build stage of the container lifecycle.

2.  Integrate with the registry that images are pushed to during the build.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating and modifying security policies](../operating/manage_security_policies/custom-security-policies.md)

- [Integrating with image registries](integrate-with-image-registries.md)

</div>

<a id="integrate-ci-check-existing-build-phase-policies_integrate-with-ci-systems"></a>

## Checking existing build-time policies

Use the RHACS portal to check any existing build-time policies that you have configured in Red Hat Advanced Cluster Security for Kubernetes.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Policy Management**.

2.  Use global search to search for `Lifecycle Stage:Build`.

</div>

<a id="policy-enforcement-deploy_integrate-with-ci-systems"></a>

### Deploy stage enforcement

Red Hat Advanced Cluster Security for Kubernetes supports two forms of security policy enforcement for deploy-time policies: hard enforcement through the admission controller and soft enforcement by RHACS Sensor. The admission controller blocks creation or updating of deployments that violate policy. If the admission controller is disabled or unavailable, Sensor can perform enforcement by scaling down replicas for deployments that violate policy to 0.

> [!WARNING]
> Policy enforcement can impact running applications or development processes. Before you enable enforcement options, inform all stakeholders and plan how to respond to the automated enforcement actions.

<div>

<div class="title">

Additional resources

</div>

- [Using admission controller enforcement](../operating/manage_security_policies/use-admission-controller-enforcement.md)

</div>

<a id="configure-registry-integration"></a>

# Configuring registry integration

To scan images, you must provide Red Hat Advanced Cluster Security for Kubernetes with access to the image registry you are using in your build pipeline.

<a id="check-for-existing-registry-integration_integrate-with-ci-systems"></a>

## Checking for existing registry integration

You can use the RHACS portal to check if you have already integrated with a registry.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Under the **Image Integration** section, look for highlighted **Registry** tiles. The tiles also list the number of items already configured for that tile.

</div>

If none of the Registry tiles are highlighted, you must first integrate with an image registry.

<a id="_additional_resources"></a>

## Additional resources

- [Integrating with image registries](integrate-with-image-registries.md)

<a id="configure-access"></a>

# Configuring access

RHACS provides the `roxctl` command-line interface (CLI) to make it easy to integrate RHACS policies into your build pipeline. The `roxctl` CLI prints detailed information about problems and how to fix them so that developers can maintain high standards in the early phases of the container lifecycle.

To securely authenticate to the Red Hat Advanced Cluster Security for Kubernetes API server, you must create an API token.

<a id="cli-authentication_integrate-with-ci-systems"></a>

## Exporting and saving the API token

Export the generated API token as an environment variable or save it to a file for use with roxctl commands.

<div>

<div class="title">

Procedure

</div>

1.  After you have generated the authentication token, export it as the `ROX_API_TOKEN` variable by entering the following command:

    ``` terminal
    $ export ROX_API_TOKEN=<api_token>
    ```

2.  (Optional): You can also save the token in a file and use it with the `--token-file` option by entering the following command:

    ``` terminal
    $ roxctl central debug dump --token-file <token_file>
    ```

    Note the following guidelines:

    - You cannot use both the `-password` (`-p`) and the `--token-file` options simultaneously.

    - If you have already set the `ROX_API_TOKEN` variable, and specify the `--token-file` option, the `roxctl` CLI uses the specified token file for authentication.

    - If you have already set the `ROX_API_TOKEN` variable, and specify the `--password` option, the `roxctl` CLI uses the specified password for authentication.

</div>

<a id="install-roxctl-cli-binary"></a>

## Installing the roxctl CLI by downloading the binary

You can install the `roxctl` CLI to interact with Red Hat Advanced Cluster Security for Kubernetes from a command-line interface. You can install `roxctl` on Linux, Windows, or macOS.

<a id="installing-cli-on-linux_integrate-with-ci-systems"></a>

### Installing the roxctl CLI on Linux

You can install the `roxctl` CLI binary on Linux by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Linux is available for `amd64`, `arm64`, `ppc64le`, and `s390x` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Linux/roxctl${arch}"
    ```

3.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

4.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-macos_integrate-with-ci-systems"></a>

### Installing the roxctl CLI on macOS

You can install the `roxctl` CLI binary on macOS by using the following procedure.

> [!NOTE]
> `roxctl` CLI for macOS is available for `amd64` and `arm64` architectures.

<div>

<div class="title">

Procedure

</div>

1.  Find the `roxctl` architecture for the target operating system:

    ``` terminal
    $ arch="$(uname -m | sed "s/x86_64//")"; arch="${arch:+-$arch}"
    ```

2.  Download the `roxctl` CLI:

    ``` terminal
    $ curl -L -f -o roxctl "https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Darwin/roxctl${arch}"
    ```

3.  Remove all extended attributes from the binary:

    ``` terminal
    $ xattr -c roxctl
    ```

4.  Make the `roxctl` binary executable:

    ``` terminal
    $ chmod +x roxctl
    ```

5.  Place the `roxctl` binary in a directory that is on your `PATH`:

    To check your `PATH`, run the following command:

    ``` terminal
    $ echo $PATH
    ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="installing-cli-on-windows_integrate-with-ci-systems"></a>

### Installing the roxctl CLI on Windows

You can install the `roxctl` CLI binary on Windows by using the following procedure.

> [!NOTE]
> `roxctl` CLI for Windows is available for the `amd64` architecture.

<div>

<div class="title">

Procedure

</div>

- Download the `roxctl` CLI:

  ``` terminal
  $ curl -f -O https://mirror.openshift.com/pub/rhacs/assets/4.11.3/bin/Windows/roxctl.exe
  ```

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed:

  ``` terminal
  $ roxctl version
  ```

</div>

<a id="run-roxctl-from-container_integrate-with-ci-systems"></a>

## Running the roxctl CLI from a container

The `roxctl` client is the default entry point in the RHACS `roxctl` image. To run the `roxctl` client in a container image:

<div>

<div class="title">

Prerequisites

</div>

- You must first generate an authentication token from the RHACS portal.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the `registry.redhat.io` registry.

    ``` terminal
    $ docker login registry.redhat.io
    ```

2.  Pull the latest container image for the `roxctl` CLI.

    ``` terminal
    $ docker pull registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3
    ```

    After you install the CLI, you can run it by using the following command:

    ``` terminal
    $ docker run -e ROX_API_TOKEN=$ROX_API_TOKEN \
      -it registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3 \
      -e $ROX_CENTRAL_ADDRESS <command>
    ```

</div>

<div class="informalexample">

In Red Hat Advanced Cluster Security Cloud Service (RHACS Cloud Service), when using `roxctl` commands that require the Central address, use the **Central instance address** as displayed in the **Instance Details** section of the Red Hat Hybrid Cloud Console. For example, use `acs-ABCD12345.acs.rhcloud.com` instead of `acs-data-ABCD12345.acs.rhcloud.com`.

</div>

<div>

<div class="title">

Verification

</div>

- Verify the `roxctl` version you have installed.

  ``` terminal
  $ docker run -it registry.redhat.io/advanced-cluster-security/rhacs-roxctl-rhel9:4.11.3 version
  ```

</div>

<a id="integrate-with-your-ci-pipeline"></a>

# Integrating with your CI pipeline

After you have finished these procedures, the next step is to integrate with your CI pipeline.

Each CI system might require a slightly different configuration.

<a id="using-jenkins"></a>

## Using Jenkins

Use the [StackRox Container Image Scanner](https://plugins.jenkins.io/stackrox-container-image-scanner) Jenkins plugin for integrating with Jenkins. You can use this plugin in both Jenkins freestyle projects and pipelines.

<a id="integrate-circle-ci_integrate-with-ci-systems"></a>

## Using CircleCI

You can integrate Red Hat Advanced Cluster Security for Kubernetes with CircleCI.

<div>

<div class="title">

Prerequisites

</div>

- You have a token with `read` and `write` permissions for the `Image` resource.

- You have a username and password for your Docker Hub account.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to CircleCI and open an existing project or create a new project.

2.  Click **Project Settings**.

3.  Click **Environment variables**.

4.  Click **Add variable** and create the following three environment variables:

    - **Name**: **STACKROX_CENTRAL_HOST** - The DNS name or IP address of Central.

    - **Name**: **ROX_API_TOKEN** - The API token to access Red Hat Advanced Cluster Security for Kubernetes.

    - **Name**: **DOCKERHUB_PASSWORD** - The password for your Docker Hub account.

    - **Name**: **DOCKERHUB_USER** - The username for your Docker Hub account.

5.  Create a directory called `.circleci` in the root directory of your local code repository for your selected project, if you do not already have a CircleCI configuration file.

6.  Create a `config.yml` configuration file with the following lines in the `.circleci` directory:

    ``` yaml
    version: 2
    jobs:
      check-policy-compliance:
        docker:
          - image: 'circleci/node:latest'
            auth:
              username: $DOCKERHUB_USER
              password: $DOCKERHUB_PASSWORD
        steps:
          - checkout
          - run:
              name: Install roxctl
              command: |
                  curl -H "Authorization: Bearer $ROX_API_TOKEN" https://$STACKROX_CENTRAL_HOST:443/api/cli/download/roxctl-linux -o roxctl && chmod +x ./roxctl
          - run:
              name: Scan images for policy deviations and vulnerabilities
              command: |
                  ./roxctl image check --endpoint "$STACKROX_CENTRAL_HOST:443" --image "<your_registry/repo/image_name>"
          - run:
              name: Scan deployment files for policy deviations
              command: |
                  ./roxctl image check --endpoint "$STACKROX_CENTRAL_HOST:443" --image "<your_deployment_file>"
                  # Important note: This step assumes the YAML file you'd like to test is located in the project.
    workflows:
      version: 2
      build_and_test:
        jobs:
          - check-policy-compliance
    ```

    where:

    `<your_registry/repo/image_name>`  
    Specifies your registry and image path.

    `<your_deployment_file>`  
    Specifies the path to your deployment file.

    > [!NOTE]
    > If you already have a `config.yml` file for CircleCI in your repository, add a new jobs section with the specified details in your existing configuration file.

7.  After you commit the configuration file to your repository, go to the **Jobs** queue in your CircleCI dashboard to verify the build policy enforcement.

</div>
