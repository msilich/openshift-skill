<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The following sections provide instructions for basic build operations, including starting and canceling builds, editing `BuildConfigs`, deleting `BuildConfigs`, viewing build details, and accessing build logs.

# Starting a build

You can manually start a new build from an existing build configuration in your current project.

<div>

<div class="title">

Procedure

</div>

- To start a build manually, enter the following command:

  ``` terminal
  $ oc start-build <buildconfig_name>
  ```

</div>

## Re-running a build

You can manually re-run a build using the `--from-build` flag.

<div>

<div class="title">

Procedure

</div>

- To manually re-run a build, enter the following command:

  ``` terminal
  $ oc start-build --from-build=<build_name>
  ```

</div>

## Streaming build logs

You can specify the `--follow` flag to stream the build’s logs in `stdout`.

<div>

<div class="title">

Procedure

</div>

- To manually stream a build’s logs in `stdout`, enter the following command:

  ``` terminal
  $ oc start-build <buildconfig_name> --follow
  ```

</div>

## Setting environment variables when starting a build

You can specify the `--env` flag to set any desired environment variable for the build.

<div>

<div class="title">

Procedure

</div>

- To specify a desired environment variable, enter the following command:

  ``` terminal
  $ oc start-build <buildconfig_name> --env=<key>=<value>
  ```

</div>

## Starting a build with source

Rather than relying on a Git source pull or a Dockerfile for a build, you can also start a build by directly pushing your source, which could be the contents of a Git or SVN working directory, a set of pre-built binary artifacts you want to deploy, or a single file. This can be done by specifying one of the following options for the `start-build` command:

| Option | Description |
|----|----|
| `--from-dir=<directory>` | Specifies a directory that will be archived and used as a binary input for the build. |
| `--from-file=<file>` | Specifies a single file that will be the only file in the build source. The file is placed in the root of an empty directory with the same file name as the original file provided. |
| `--from-repo=<local_source_repo>` | Specifies a path to a local repository to use as the binary input for a build. Add the `--commit` option to control which branch, tag, or commit is used for the build. |

When passing any of these options directly to the build, the contents are streamed to the build and override the current build source settings.

> [!NOTE]
> Builds triggered from binary input will not preserve the source on the server, so rebuilds triggered by base image changes will use the source specified in the build configuration.

<div>

<div class="title">

Procedure

</div>

- To start a build from a source code repository and send the contents of a local Git repository as an archive from the tag `v2`, enter the following command:

  ``` terminal
  $ oc start-build hello-world --from-repo=../hello-world --commit=v2
  ```

</div>

# Canceling a build

You can cancel a build using the web console, or with the following CLI command.

<div>

<div class="title">

Procedure

</div>

- To manually cancel a build, enter the following command:

  ``` terminal
  $ oc cancel-build <build_name>
  ```

</div>

## Canceling multiple builds

You can cancel multiple builds with the following CLI command.

<div>

<div class="title">

Procedure

</div>

- To manually cancel multiple builds, enter the following command:

  ``` terminal
  $ oc cancel-build <build1_name> <build2_name> <build3_name>
  ```

</div>

## Canceling all builds

You can cancel all builds from the build configuration with the following CLI command.

<div>

<div class="title">

Procedure

</div>

- To cancel all builds, enter the following command:

  ``` terminal
  $ oc cancel-build bc/<buildconfig_name>
  ```

</div>

## Canceling all builds in a given state

You can cancel all builds in a given state, such as `new` or `pending`, while ignoring the builds in other states.

<div>

<div class="title">

Procedure

</div>

- To cancel all in a given state, enter the following command:

  ``` terminal
  $ oc cancel-build bc/<buildconfig_name>
  ```

</div>

# Editing a BuildConfig

To edit your build configurations, you use the **Edit BuildConfig** option in the **Builds** page.

You can use either of the following views to edit a `BuildConfig`:

- The **Form view** enables you to edit your `BuildConfig` using the standard form fields and checkboxes.

- The **YAML view** enables you to edit your `BuildConfig` with full control over the operations.

You can switch between the **Form view** and **YAML view** without losing any data. The data in the **Form view** is transferred to the **YAML view** and vice versa.

<div>

<div class="title">

Procedure

</div>

1.  On the **Builds** page, click the Options menu ![kebab](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABsAAAAjCAIAAADqn+bCAAAACXBIWXMAAA7EAAAOxAGVKw4bAAAA+0lEQVRIie2WMQqEMBBFJ47gUXRBLyBYqbUXULCx9CR2XsAb6AlUEM9kpckW7obdZhwWYWHXX/3i8TPJZEKEUgpOlXFu3JX4V4kmB2qaZhgGKSUiZlkWxzEBC84N9zxv27bdO47Tti0Bs3at4wBgXVca/lJnfN/XPggCGmadIwAsywIAiGhZFk1ydy2EYJKgGCqK4vZUVVU0zKpxnmftp2mi4S/1GhG1N82DMWNNYVmW4zgqpRAxTVMa5t4evlg11nXd9/1eY57nSZIQMKtG13WllLu3bbvrOgJmdUbHwfur8Xniqw6Hh5UYRdGDNowwDA+WvP4UV+JPJ94B1gKUWcTOCT0AAAAASUVORK5CYII=) to see the **Edit BuildConfig** option.

2.  Click **Edit BuildConfig** to see the **Form view** option.

3.  In the **Git** section, enter the Git repository URL for the codebase you want to use to create an application. The URL is then validated.

    - Optional: Click **Show Advanced Git Options** to add details such as:

      - **Git Reference** to specify a branch, tag, or commit that contains code you want to use to build the application.

      - **Context Dir** to specify the subdirectory that contains code you want to use to build the application.

      - **Source Secret** to create a **Secret Name** with credentials for pulling your source code from a private repository.

4.  In the **Build from** section, select the option that you would like to build from. You can use the following options:

    - **Image Stream tag** references an image for a given image stream and tag. Enter the project, image stream, and tag of the location you would like to build from and push to.

    - **Image Stream image** references an image for a given image stream and image name. Enter the image stream image you would like to build from. Also enter the project, image stream, and tag to push to.

    - **Docker image**: The Docker image is referenced through a Docker image repository. You will also need to enter the project, image stream, and tag to refer to where you would like to push to.

5.  Optional: In the **Environment Variables** section, add the environment variables associated with the project by using the **Name** and **Value** fields. To add more environment variables, use **Add Value**, or **Add from ConfigMap** and **Secret** .

6.  Optional: To further customize your application, use the following advanced options:

    Trigger
    Triggers a new image build when the builder image changes. Add more triggers by clicking **Add Trigger** and selecting the **Type** and **Secret**.

    Secrets
    Adds secrets for your application. Add more secrets by clicking **Add secret** and selecting the **Secret** and **Mount point**.

    Policy
    Click **Run policy** to select the build run policy. The selected policy determines the order in which builds created from the build configuration must run.

    Hooks
    Select **Run build hooks after image is built** to run commands at the end of the build and verify the image. Add **Hook type**, **Command**, and **Arguments** to append to the command.

7.  Click **Save** to save the `BuildConfig`.

</div>

# Deleting a BuildConfig

You can delete a `BuildConfig` using the following command.

<div>

<div class="title">

Procedure

</div>

- To delete a `BuildConfig`, enter the following command:

  ``` terminal
  $ oc delete bc <BuildConfigName>
  ```

  This also deletes all builds that were instantiated from this `BuildConfig`.

- To delete a `BuildConfig` and keep the builds instatiated from the `BuildConfig`, specify the `--cascade=false` flag when you enter the following command:

  ``` terminal
  $ oc delete --cascade=false bc <BuildConfigName>
  ```

</div>

# Viewing build details

You can view build details with the web console or by using the `oc describe` CLI command.

This displays information including:

- The build source.

- The build strategy.

- The output destination.

- Digest of the image in the destination registry.

- How the build was created.

If the build uses the `Docker` or `Source` strategy, the `oc describe` output also includes information about the source revision used for the build, including the commit ID, author, committer, and message.

<div>

<div class="title">

Procedure

</div>

- To view build details, enter the following command:

  ``` terminal
  $ oc describe build <build_name>
  ```

</div>

# Accessing build logs

You can access build logs using the web console or the CLI.

<div>

<div class="title">

Procedure

</div>

- To stream the logs using the build directly, enter the following command:

  ``` terminal
  $ oc describe build <build_name>
  ```

</div>

## Accessing BuildConfig logs

You can access `BuildConfig` logs using the web console or the CLI.

<div>

<div class="title">

Procedure

</div>

- To stream the logs of the latest build for a `BuildConfig`, enter the following command:

  ``` terminal
  $ oc logs -f bc/<buildconfig_name>
  ```

</div>

## Accessing BuildConfig logs for a given version build

You can access logs for a given version build for a `BuildConfig` using the web console or the CLI.

<div>

<div class="title">

Procedure

</div>

- To stream the logs for a given version build for a `BuildConfig`, enter the following command:

  ``` terminal
  $ oc logs --version=<number> bc/<buildconfig_name>
  ```

</div>

## Enabling log verbosity

You can enable a more verbose output by passing the `BUILD_LOGLEVEL` environment variable as part of the `sourceStrategy` or `dockerStrategy` in a `BuildConfig`.

> [!NOTE]
> An administrator can set the default build verbosity for the entire OpenShift Container Platform instance by configuring `env/BUILD_LOGLEVEL`. This default can be overridden by specifying `BUILD_LOGLEVEL` in a given `BuildConfig`. You can specify a higher priority override on the command line for non-binary builds by passing `--build-loglevel` to `oc start-build`.

Available log levels for source builds are as follows:

|  |  |
|----|----|
| Level 0 | Produces output from containers running the `assemble` script and all encountered errors. This is the default. |
| Level 1 | Produces basic information about the executed process. |
| Level 2 | Produces very detailed information about the executed process. |
| Level 3 | Produces very detailed information about the executed process, and a listing of the archive contents. |
| Level 4 | Currently produces the same information as level 3. |
| Level 5 | Produces everything mentioned on previous levels and additionally provides docker push messages. |

<div>

<div class="title">

Procedure

</div>

- To enable more verbose output, pass the `BUILD_LOGLEVEL` environment variable as part of the `sourceStrategy` or `dockerStrategy` in a `BuildConfig`:

  ``` yaml
  sourceStrategy:
  ...
    env:
      - name: "BUILD_LOGLEVEL"
        value: "2"
  ```

  - Adjust this value to the desired log level.

</div>
