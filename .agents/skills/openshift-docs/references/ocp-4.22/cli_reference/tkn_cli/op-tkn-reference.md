<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

This section lists the basic `tkn` CLI commands.

# Basic syntax

`tkn [command or options] [arguments…​]`

# Global options

`--help, -h`

# Utility commands

## tkn

Parent command for `tkn` CLI.

<div class="formalpara">

<div class="title">

Example: Display all options

</div>

``` terminal
$ tkn
```

</div>

## completion \[shell\]

Print shell completion code which must be evaluated to provide interactive completion. Supported shells are `bash` and `zsh`.

<div class="formalpara">

<div class="title">

Example: Completion code for `bash` shell

</div>

``` terminal
$ tkn completion bash
```

</div>

## version

Print version information of the `tkn` CLI.

<div class="formalpara">

<div class="title">

Example: Check the `tkn` version

</div>

``` terminal
$ tkn version
```

</div>

# Pipelines management commands

## pipeline

Manage pipelines.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn pipeline --help
```

</div>

## pipeline delete

Delete a pipeline.

<div class="formalpara">

<div class="title">

Example: Delete the `mypipeline` pipeline from a namespace

</div>

``` terminal
$ tkn pipeline delete mypipeline -n myspace
```

</div>

## pipeline describe

Describe a pipeline.

<div class="formalpara">

<div class="title">

Example: Describe the `mypipeline` pipeline

</div>

``` terminal
$ tkn pipeline describe mypipeline
```

</div>

## pipeline list

Display a list of pipelines.

<div class="formalpara">

<div class="title">

Example: Display a list of pipelines

</div>

``` terminal
$ tkn pipeline list
```

</div>

## pipeline logs

Display the logs for a specific pipeline.

<div class="formalpara">

<div class="title">

Example: Stream the live logs for the `mypipeline` pipeline

</div>

``` terminal
$ tkn pipeline logs -f mypipeline
```

</div>

## pipeline start

Start a pipeline.

<div class="formalpara">

<div class="title">

Example: Start the `mypipeline` pipeline

</div>

``` terminal
$ tkn pipeline start mypipeline
```

</div>

# Pipeline run commands

## pipelinerun

Manage pipeline runs.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn pipelinerun -h
```

</div>

## pipelinerun cancel

Cancel a pipeline run.

<div class="formalpara">

<div class="title">

Example: Cancel the `mypipelinerun` pipeline run from a namespace

</div>

``` terminal
$ tkn pipelinerun cancel mypipelinerun -n myspace
```

</div>

## pipelinerun delete

Delete a pipeline run.

<div class="formalpara">

<div class="title">

Example: Delete pipeline runs from a namespace

</div>

``` terminal
$ tkn pipelinerun delete mypipelinerun1 mypipelinerun2 -n myspace
```

</div>

<div class="formalpara">

<div class="title">

Example: Delete all pipeline runs from a namespace, except the five most recently executed pipeline runs

</div>

``` terminal
$ tkn pipelinerun delete -n myspace --keep 5
```

</div>

- Replace `5` with the number of most recently executed pipeline runs you want to retain.

<div class="formalpara">

<div class="title">

Example: Delete all pipelines

</div>

``` terminal
$ tkn pipelinerun delete --all
```

</div>

> [!NOTE]
> Starting with Red Hat OpenShift Pipelines 1.6, the `tkn pipelinerun delete --all` command does not delete any resources that are in the running state.

## pipelinerun describe

Describe a pipeline run.

<div class="formalpara">

<div class="title">

Example: Describe the `mypipelinerun` pipeline run in a namespace

</div>

``` terminal
$ tkn pipelinerun describe mypipelinerun -n myspace
```

</div>

## pipelinerun list

List pipeline runs.

<div class="formalpara">

<div class="title">

Example: Display a list of pipeline runs in a namespace

</div>

``` terminal
$ tkn pipelinerun list -n myspace
```

</div>

## pipelinerun logs

Display the logs of a pipeline run.

<div class="formalpara">

<div class="title">

Example: Display the logs of the `mypipelinerun` pipeline run with all tasks and steps in a namespace

</div>

``` terminal
$ tkn pipelinerun logs mypipelinerun -a -n myspace
```

</div>

# Task management commands

## task

Manage tasks.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn task -h
```

</div>

## task delete

Delete a task.

<div class="formalpara">

<div class="title">

Example: Delete `mytask1` and `mytask2` tasks from a namespace

</div>

``` terminal
$ tkn task delete mytask1 mytask2 -n myspace
```

</div>

## task describe

Describe a task.

<div class="formalpara">

<div class="title">

Example: Describe the `mytask` task in a namespace

</div>

``` terminal
$ tkn task describe mytask -n myspace
```

</div>

## task list

List tasks.

<div class="formalpara">

<div class="title">

Example: List all the tasks in a namespace

</div>

``` terminal
$ tkn task list -n myspace
```

</div>

## task logs

Display task logs.

<div class="formalpara">

<div class="title">

Example: Display logs for the `mytaskrun` task run of the `mytask` task

</div>

``` terminal
$ tkn task logs mytask mytaskrun -n myspace
```

</div>

## task start

Start a task.

<div class="formalpara">

<div class="title">

Example: Start the `mytask` task in a namespace

</div>

``` terminal
$ tkn task start mytask -s <ServiceAccountName> -n myspace
```

</div>

# Task run commands

## taskrun

Manage task runs.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn taskrun -h
```

</div>

## taskrun cancel

Cancel a task run.

<div class="formalpara">

<div class="title">

Example: Cancel the `mytaskrun` task run from a namespace

</div>

``` terminal
$ tkn taskrun cancel mytaskrun -n myspace
```

</div>

## taskrun delete

Delete a TaskRun.

<div class="formalpara">

<div class="title">

Example: Delete the `mytaskrun1` and `mytaskrun2` task runs from a namespace

</div>

``` terminal
$ tkn taskrun delete mytaskrun1 mytaskrun2 -n myspace
```

</div>

<div class="formalpara">

<div class="title">

Example: Delete all but the five most recently executed task runs from a namespace

</div>

``` terminal
$ tkn taskrun delete -n myspace --keep 5
```

</div>

- Replace `5` with the number of most recently executed task runs you want to retain.

## taskrun describe

Describe a task run.

<div class="formalpara">

<div class="title">

Example: Describe the `mytaskrun` task run in a namespace

</div>

``` terminal
$ tkn taskrun describe mytaskrun -n myspace
```

</div>

## taskrun list

List task runs.

<div class="formalpara">

<div class="title">

Example: List all the task runs in a namespace

</div>

``` terminal
$ tkn taskrun list -n myspace
```

</div>

## taskrun logs

Display task run logs.

<div class="formalpara">

<div class="title">

Example: Display live logs for the `mytaskrun` task run in a namespace

</div>

``` terminal
$ tkn taskrun logs -f mytaskrun -n myspace
```

</div>

# Condition management commands

## condition

Manage Conditions.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn condition --help
```

</div>

## condition delete

Delete a Condition.

<div class="formalpara">

<div class="title">

Example: Delete the `mycondition1` Condition from a namespace

</div>

``` terminal
$ tkn condition delete mycondition1 -n myspace
```

</div>

## condition describe

Describe a Condition.

<div class="formalpara">

<div class="title">

Example: Describe the `mycondition1` Condition in a namespace

</div>

``` terminal
$ tkn condition describe mycondition1 -n myspace
```

</div>

## condition list

List Conditions.

<div class="formalpara">

<div class="title">

Example: List Conditions in a namespace

</div>

``` terminal
$ tkn condition list -n myspace
```

</div>

# Pipeline Resource management commands

## resource

Manage Pipeline Resources.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn resource -h
```

</div>

## resource create

Create a Pipeline Resource.

<div class="formalpara">

<div class="title">

Example: Create a Pipeline Resource in a namespace

</div>

``` terminal
$ tkn resource create -n myspace
```

</div>

This is an interactive command that asks for input on the name of the Resource, type of the Resource, and the values based on the type of the Resource.

## resource delete

Delete a Pipeline Resource.

<div class="formalpara">

<div class="title">

Example: Delete the `myresource` Pipeline Resource from a namespace

</div>

``` terminal
$ tkn resource delete myresource -n myspace
```

</div>

## resource describe

Describe a Pipeline Resource.

<div class="formalpara">

<div class="title">

Example: Describe the `myresource` Pipeline Resource

</div>

``` terminal
$ tkn resource describe myresource -n myspace
```

</div>

## resource list

List Pipeline Resources.

<div class="formalpara">

<div class="title">

Example: List all Pipeline Resources in a namespace

</div>

``` terminal
$ tkn resource list -n myspace
```

</div>

# ClusterTask management commands

> [!IMPORTANT]
> In Red Hat OpenShift Pipelines 1.10, ClusterTask functionality of the `tkn` command-line utility is deprecated and is planned to be removed in a future release.

## clustertask

Manage ClusterTasks.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn clustertask --help
```

</div>

## clustertask delete

Delete a ClusterTask resource in a cluster.

<div class="formalpara">

<div class="title">

Example: Delete `mytask1` and `mytask2` ClusterTasks

</div>

``` terminal
$ tkn clustertask delete mytask1 mytask2
```

</div>

## clustertask describe

Describe a ClusterTask.

<div class="formalpara">

<div class="title">

Example: Describe the `mytask` ClusterTask

</div>

``` terminal
$ tkn clustertask describe mytask1
```

</div>

## clustertask list

List ClusterTasks.

<div class="formalpara">

<div class="title">

Example: List ClusterTasks

</div>

``` terminal
$ tkn clustertask list
```

</div>

## clustertask start

Start ClusterTasks.

<div class="formalpara">

<div class="title">

Example: Start the `mytask` ClusterTask

</div>

``` terminal
$ tkn clustertask start mytask
```

</div>

# Trigger management commands

## eventlistener

Manage EventListeners.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn eventlistener -h
```

</div>

## eventlistener delete

Delete an EventListener.

<div class="formalpara">

<div class="title">

Example: Delete `mylistener1` and `mylistener2` EventListeners in a namespace

</div>

``` terminal
$ tkn eventlistener delete mylistener1 mylistener2 -n myspace
```

</div>

## eventlistener describe

Describe an EventListener.

<div class="formalpara">

<div class="title">

Example: Describe the `mylistener` EventListener in a namespace

</div>

``` terminal
$ tkn eventlistener describe mylistener -n myspace
```

</div>

## eventlistener list

List EventListeners.

<div class="formalpara">

<div class="title">

Example: List all the EventListeners in a namespace

</div>

``` terminal
$ tkn eventlistener list -n myspace
```

</div>

## eventlistener logs

Display logs of an EventListener.

<div class="formalpara">

<div class="title">

Example: Display the logs of the `mylistener` EventListener in a namespace

</div>

``` terminal
$ tkn eventlistener logs mylistener -n myspace
```

</div>

## triggerbinding

Manage TriggerBindings.

<div class="formalpara">

<div class="title">

Example: Display TriggerBindings help

</div>

``` terminal
$ tkn triggerbinding -h
```

</div>

## triggerbinding delete

Delete a TriggerBinding.

<div class="formalpara">

<div class="title">

Example: Delete `mybinding1` and `mybinding2` TriggerBindings in a namespace

</div>

``` terminal
$ tkn triggerbinding delete mybinding1 mybinding2 -n myspace
```

</div>

## triggerbinding describe

Describe a TriggerBinding.

<div class="formalpara">

<div class="title">

Example: Describe the `mybinding` TriggerBinding in a namespace

</div>

``` terminal
$ tkn triggerbinding describe mybinding -n myspace
```

</div>

## triggerbinding list

List TriggerBindings.

<div class="formalpara">

<div class="title">

Example: List all the TriggerBindings in a namespace

</div>

``` terminal
$ tkn triggerbinding list -n myspace
```

</div>

## triggertemplate

Manage TriggerTemplates.

<div class="formalpara">

<div class="title">

Example: Display TriggerTemplate help

</div>

``` terminal
$ tkn triggertemplate -h
```

</div>

## triggertemplate delete

Delete a TriggerTemplate.

<div class="formalpara">

<div class="title">

Example: Delete `mytemplate1` and `mytemplate2` TriggerTemplates in a namespace

</div>

``` terminal
$ tkn triggertemplate delete mytemplate1 mytemplate2 -n `myspace`
```

</div>

## triggertemplate describe

Describe a TriggerTemplate.

<div class="formalpara">

<div class="title">

Example: Describe the `mytemplate` TriggerTemplate in a namespace

</div>

``` terminal
$ tkn triggertemplate describe mytemplate -n `myspace`
```

</div>

## triggertemplate list

List TriggerTemplates.

<div class="formalpara">

<div class="title">

Example: List all the TriggerTemplates in a namespace

</div>

``` terminal
$ tkn triggertemplate list -n myspace
```

</div>

## clustertriggerbinding

Manage ClusterTriggerBindings.

<div class="formalpara">

<div class="title">

Example: Display ClusterTriggerBindings help

</div>

``` terminal
$ tkn clustertriggerbinding -h
```

</div>

## clustertriggerbinding delete

Delete a ClusterTriggerBinding.

<div class="formalpara">

<div class="title">

Example: Delete `myclusterbinding1` and `myclusterbinding2` ClusterTriggerBindings

</div>

``` terminal
$ tkn clustertriggerbinding delete myclusterbinding1 myclusterbinding2
```

</div>

## clustertriggerbinding describe

Describe a ClusterTriggerBinding.

<div class="formalpara">

<div class="title">

Example: Describe the `myclusterbinding` ClusterTriggerBinding

</div>

``` terminal
$ tkn clustertriggerbinding describe myclusterbinding
```

</div>

## clustertriggerbinding list

List ClusterTriggerBindings.

<div class="formalpara">

<div class="title">

Example: List all ClusterTriggerBindings

</div>

``` terminal
$ tkn clustertriggerbinding list
```

</div>

# Hub interaction commands

Interact with Tekton Hub for resources such as tasks and pipelines.

## hub

Interact with hub.

<div class="formalpara">

<div class="title">

Example: Display help

</div>

``` terminal
$ tkn hub -h
```

</div>

<div class="formalpara">

<div class="title">

Example: Interact with a hub API server

</div>

``` terminal
$ tkn hub --api-server https://api.hub.tekton.dev
```

</div>

> [!NOTE]
> For each example, to get the corresponding sub-commands and flags, run `tkn hub <command> --help`.

## hub downgrade

Downgrade an installed resource.

<div class="formalpara">

<div class="title">

Example: Downgrade the `mytask` task in the `mynamespace` namespace to its older version

</div>

``` terminal
$ tkn hub downgrade task mytask --to version -n mynamespace
```

</div>

## hub get

Get a resource manifest by its name, kind, catalog, and version.

<div class="formalpara">

<div class="title">

Example: Get the manifest for a specific version of the `myresource` pipeline or task from the `tekton` catalog

</div>

``` terminal
$ tkn hub get [pipeline | task] myresource --from tekton --version version
```

</div>

## hub info

Display information about a resource by its name, kind, catalog, and version.

<div class="formalpara">

<div class="title">

Example: Display information about a specific version of the `mytask` task from the `tekton` catalog

</div>

``` terminal
$ tkn hub info task mytask --from tekton --version version
```

</div>

## hub install

Install a resource from a catalog by its kind, name, and version.

<div class="formalpara">

<div class="title">

Example: Install a specific version of the `mytask` task from the `tekton` catalog in the `mynamespace` namespace

</div>

``` terminal
$ tkn hub install task mytask --from tekton --version version -n mynamespace
```

</div>

## hub reinstall

Reinstall a resource by its kind and name.

<div class="formalpara">

<div class="title">

Example: Reinstall a specific version of the `mytask` task from the `tekton` catalog in the `mynamespace` namespace

</div>

``` terminal
$ tkn hub reinstall task mytask --from tekton --version version -n mynamespace
```

</div>

## hub search

Search a resource by a combination of name, kind, and tags.

<div class="formalpara">

<div class="title">

Example: Search a resource with a tag `cli`

</div>

``` terminal
$ tkn hub search --tags cli
```

</div>

## hub upgrade

Upgrade an installed resource.

<div class="formalpara">

<div class="title">

Example: Upgrade the installed `mytask` task in the `mynamespace` namespace to a new version

</div>

``` terminal
$ tkn hub upgrade task mytask --to version -n mynamespace
```

</div>
