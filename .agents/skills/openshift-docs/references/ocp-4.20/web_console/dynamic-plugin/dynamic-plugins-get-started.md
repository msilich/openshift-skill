<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To get started using the dynamic plugin, you must set up your environment to write a new OpenShift Container Platform dynamic plugin. For an example of how to write a new plugin, see [Adding a tab to the pods page](dynamic-plugin-example.md#adding-tab-to-pods-page_dynamic-plugin-example).

# Dynamic plugin development

You can run the plugin using a local development environment. The OpenShift Container Platform web console runs in a container connected to the cluster you have logged into.

<div>

<div class="title">

Prerequisites

</div>

- You must have cloned the [`console-plugin-template`](https://github.com/openshift/console-plugin-template) repository, which contains a template for creating plugins.

  > [!IMPORTANT]
  > Red Hat does not support custom plugin code. Only [Cooperative community support](https://access.redhat.com/solutions/5893251) is available for your plugin.

- You must have an OpenShift Container Platform cluster running.

- You must have the OpenShift CLI (`oc`) installed.

- You must have [`yarn`](https://yarnpkg.com/) installed.

- You must have [Docker](https://www.docker.com/) v3.2.0 or later or [Podman](https://podman.io/) v3.2.0 or later installed and running.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Open two terminal windows.

2.  In one terminal window, run the following command to install the dependencies for your plugin using yarn.

    ``` terminal
    $ yarn install
    ```

3.  After installing, run the following command to start yarn.

    ``` terminal
    $ yarn run start
    ```

4.  In another terminal window, login to the OpenShift Container Platform web console through the CLI.

    ``` terminal
    $ oc login
    ```

5.  Run the OpenShift Container Platform web console in a container connected to the cluster you have logged in to by running the following command:

    ``` terminal
    $ yarn run start-console
    ```

    > [!NOTE]
    > The `yarn run start-console` command runs an `amd64` image and might fail when run with Apple Silicon and Podman. You can work around it with `qemu-user-static` by running the following commands:
    >
    > ``` terminal
    > $ podman machine ssh
    > ```
    >
    > ``` terminal
    > $ sudo -i
    > ```
    >
    > ``` terminal
    > $ rpm-ostree install qemu-user-static
    > ```
    >
    > ``` terminal
    > $ systemctl reboot
    > ```

</div>

<div>

<div class="title">

Verification

</div>

- Visit [localhost:9000](http://localhost:9000/example) to view the running plugin. Inspect the value of `window.SERVER_FLAGS.consolePlugins` to see the list of plugins which load at runtime.

</div>
