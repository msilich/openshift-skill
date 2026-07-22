<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can write and install plugins to build on the default `oc` commands, allowing you to perform new and more complex tasks with the OpenShift CLI (`oc`).

# Writing CLI plugins

You can write a plugin for the OpenShift CLI (`oc`) in any programming language or script that allows you to write command-line commands. Note that you cannot use a plugin to overwrite an existing `oc` command.

This procedure creates a simple Bash plugin that prints a message to the terminal when the `oc foo` command is issued.

<div>

<div class="title">

Procedure

</div>

1.  Create a file called `oc-foo`.

    When naming your plugin file, keep the following in mind:

    - The file must begin with `oc-` or `kubectl-` to be recognized as a plugin.

    - The file name determines the command that invokes the plugin. For example, a plugin with the file name `oc-foo-bar` can be invoked by a command of `oc foo bar`. You can also use underscores if you want the command to contain dashes. For example, a plugin with the file name `oc-foo_bar` can be invoked by a command of `oc foo-bar`.

2.  Add the following contents to the file.

    ``` bash
    #!/bin/bash

    # optional argument handling
    if [[ "$1" == "version" ]]
    then
        echo "1.0.0"
        exit 0
    fi

    # optional argument handling
    if [[ "$1" == "config" ]]
    then
        echo $KUBECONFIG
        exit 0
    fi

    echo "I am a plugin named kubectl-foo"
    ```

    After you install this plugin for the OpenShift CLI (`oc`), you can invoke it by using the `oc foo` command.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Sample plugin repository](https://github.com/kubernetes/sample-cli-plugin)

- [CLI runtime repository](https://github.com/kubernetes/cli-runtime/)

</div>

# Installing and using CLI plugins

After you write a custom plugin for the OpenShift CLI (`oc`), you must install the plugin before you can use it.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `oc` CLI tool installed.

- You must have a CLI plugin file that begins with `oc-` or `kubectl-`.

</div>

<div>

<div class="title">

Procedure

</div>

1.  If necessary, update the plugin file to be executable.

    ``` terminal
    $ chmod +x <plugin_file>
    ```

2.  Place the file anywhere in your `PATH`, such as `/usr/local/bin/`.

    ``` terminal
    $ sudo mv <plugin_file> /usr/local/bin/.
    ```

3.  Run `oc plugin list` to make sure that the plugin is listed.

    ``` terminal
    $ oc plugin list
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    The following compatible plugins are available:

    /usr/local/bin/<plugin_file>
    ```

    </div>

    If your plugin is not listed here, verify that the file begins with `oc-` or `kubectl-`, is executable, and is on your `PATH`.

4.  Invoke the new command or option introduced by the plugin.

    For example, if you built and installed the `kubectl-ns` plugin from the [Sample plugin repository](https://github.com/kubernetes/sample-cli-plugin), you can use the following command to view the current namespace:

    ``` terminal
    $ oc ns
    ```

    Note that the command to invoke the plugin depends on the plugin file name. For example, a plugin with the file name of `oc-foo-bar` is invoked by the `oc foo bar` command.

</div>
