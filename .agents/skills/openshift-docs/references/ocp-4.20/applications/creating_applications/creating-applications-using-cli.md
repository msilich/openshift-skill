<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can create applications on your OpenShift Container Platform cluster from a Git repository, a container image, or a template using the `oc new-app` command. Customize names, labels, environment variables, target projects, and other deployment options with command flags.

# Creating an application from source code

You can create an application on your OpenShift Container Platform cluster from a local or remote Git repository using the `oc new-app` command. Use command flags to target a specific branch or subdirectory, authenticate to a private repository, or control the build strategy and builder image.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.

- You have access to a Git repository containing your application source code.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create an application from a Git repository in a local directory by running the following command:

    ``` terminal
    $ oc new-app /<path_to_source_code>
    ```

    > [!NOTE]
    > If you use a local Git repository, the repository must have a remote named `origin` that points to a URL that is accessible by the OpenShift Container Platform cluster. If there is no recognized remote, running the `new-app` command creates a binary build.

2.  Create an application from a public remote Git repository by running the following command:

    ``` terminal
    $ oc new-app https://github.com/sclorg/cakephp-ex
    ```

3.  Create an application from a private remote Git repository by running the following command:

    ``` terminal
    $ oc new-app https://github.com/<your_user>/<your_private_repo> --source-secret=yoursecret
    ```

    > [!NOTE]
    > If you use a private remote Git repository, use the `--source-secret` flag to specify a source clone secret for access to the repository.

4.  Use a subdirectory of your source repository by running the following command:

    ``` terminal
    $ oc new-app https://github.com/sclorg/s2i-ruby-container.git \
        --context-dir=2.0/test/puma-test-app
    ```

5.  Specify a Git branch by running the following command:

    ``` terminal
    $ oc new-app https://github.com/openshift/ruby-hello-world.git#beta4
    ```

6.  Override the automatically detected build strategy by running the following command:

    ``` terminal
    $ oc new-app /home/user/code/myapp --strategy=docker
    ```

    > [!NOTE]
    > The `oc` command requires that files containing build sources are available in a remote Git repository. For all source builds, you must use `git remote -v`.

7.  Specify the builder image and source repository:

    1.  Specify the builder image and source repository for a remote repository by running the following command:

        ``` terminal
        $ oc new-app myproject/my-ruby~https://github.com/openshift/ruby-hello-world.git
        ```

    2.  Specify the builder image and source repository for a local repository by running the following command:

        ``` terminal
        $ oc new-app openshift/ruby-20-centos7:latest~/home/user/code/my-ruby-app
        ```

</div>

# Build strategy and language detection for source applications

You can determine which build strategy and language builder the `oc new-app` command selects by reviewing files in the root or context directory of your Git repository. Use these detection rules to override the build strategy or specify a builder image when automatic detection does not apply.

## Build strategy detection

OpenShift Container Platform automatically determines which build strategy to use by detecting certain files:

- If a `Jenkinsfile` exists in the root or specified context directory of the source repository when creating a new application, OpenShift Container Platform generates a pipeline build strategy.

  > [!NOTE]
  > The `pipeline` build strategy is deprecated; consider using Red Hat OpenShift Pipelines instead.

- If a `Dockerfile` exists in the root or specified context directory of the source repository when creating a new application, OpenShift Container Platform generates a docker build strategy.

- If neither a `Jenkinsfile` nor a `Dockerfile` is detected, OpenShift Container Platform generates a source build strategy.

## Language detection

If you use the source build strategy, `new-app` detects the language builder from certain files in the root or context directory of the repository.

| Language | Files                              |
|----------|------------------------------------|
| `dotnet` | `project.json`, `*.csproj`         |
| `jee`    | `pom.xml`                          |
| `nodejs` | `app.json`, `package.json`         |
| `perl`   | `cpanfile`, `index.pl`             |
| `php`    | `composer.json`, `index.php`       |
| `python` | `requirements.txt`, `setup.py`     |
| `ruby`   | `Gemfile`, `Rakefile`, `config.ru` |
| `scala`  | `build.sbt`                        |
| `golang` | `Godeps`, `main.go`                |

Languages detected by `new-app`

After a language is detected, the `new-app` command searches the OpenShift Container Platform server for image stream tags with a matching `supports` annotation or image streams that match the language name. If a match is not found, the `new-app` command searches the Docker Hub registry for an image that matches the detected language based on name.

When you specify an image and repository with the `~` separator, build strategy detection and language detection are not carried out.

> [!NOTE]
> Language detection requires the Git client to be locally installed so that your repository can be cloned and inspected. If Git is not available, you can avoid the language detection step by specifying the builder image to use with your repository with the `<image>~<repository>` syntax.
>
> The `-i <image> <repository>` invocation requires that `new-app` attempt to clone `repository` to determine what type of artifact it is, so the command fails if Git is not available.
>
> The `-i <image> --code <repository>` invocation requires that `new-app` clone `repository` to learn whether `image` is a builder for the source or a separate deployment, such as a database image.

# Creating an application from an image

You can use the `oc new-app` command to create an application from a container image in Docker Hub, a private registry, or an image stream on your cluster. Use this procedure when you know the container image name or image stream you want to deploy.

Use the command that matches where your container image is stored.

> [!NOTE]
> If you specify an image from your local Docker repository, you must ensure that the same image is available to the OpenShift Container Platform cluster nodes.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.

- You know the container image name or image stream you want to deploy.

</div>

<div>

<div class="title">

Procedure

</div>

- Create an application from the Docker Hub MySQL image by running the following command:

  ``` terminal
  $ oc new-app mysql
  ```

- Create an application from an image in a private registry by specifying the full image path in the following command:

  ``` terminal
  $ oc new-app myregistry:5000/example/myimage
  ```

- Create an application from an existing image stream and optional image stream tag by running the following command:

  ``` terminal
  $ oc new-app my-stream:v1
  ```

</div>

<div>

<div class="title">

Additional resources

</div>

- [Docker Hub registry (Docker)](https://registry.hub.docker.com)

</div>

# Creating an application from a template

You can use the `oc new-app` command to create an application from a template stored in your project or from a template file on your local system. Use this procedure when you have a template JSON or YAML file, or a template in the template library of your current project.

<div>

<div class="title">

Prerequisites

</div>

- You have installed the OpenShift CLI (`oc`) and logged in to your cluster.

- You have a template JSON or YAML file, or a template stored in the template library of your current project.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Upload an application template to the template library of your current project by running the following command:

    ``` terminal
    $ oc create -f examples/sample-app/application-template-stibuild.json
    ```

2.  Create a new application from a stored template by running the following command:

    ``` terminal
    $ oc new-app ruby-helloworld-sample
    ```

3.  Create a new application from a template file on your local file system without storing it in OpenShift Container Platform by running the following command:

    ``` terminal
    $ oc new-app -f examples/sample-app/application-template-stibuild.json
    ```

4.  Set template parameter values when creating an application by running the following command:

    ``` terminal
    $ oc new-app ruby-helloworld-sample \
        -p ADMIN_USERNAME=admin -p ADMIN_PASSWORD=mypassword
    ```

5.  Store template parameters in a file by creating a file such as `helloworld.params` with the following content:

    ``` terminal
    ADMIN_USERNAME=admin
    ADMIN_PASSWORD=mypassword
    ```

    You can store your parameters in a file, then use that file with `--param-file` when instantiating a template. If you want to read the parameters from standard input, use `--param-file=-`.

6.  Create a new application from a template by using a parameter file by running the following command:

    ``` terminal
    $ oc new-app ruby-helloworld-sample --param-file=helloworld.params
    ```

    > [!NOTE]
    > To read parameters from standard input, use `--param-file=-`.

</div>

# Customization options for application creation

You can customize how the `oc new-app` command creates applications by setting names, labels, environment variables, target projects, and other options. Use these flags to control the objects the command generates before you deploy.

| Object | Description |
|----|----|
| `BuildConfig` | A `BuildConfig` object is created for each source repository that is specified in the command line. The `BuildConfig` object specifies the strategy to use, the source location, and the build output location. |
| `ImageStreams` | For the `BuildConfig` object, two image streams are usually created. One represents the input image. With source builds, this is the builder image. With `Docker` builds, this is the **FROM** image. The second one represents the output image. If a container image was specified as input to `new-app`, then an image stream is created for that image as well. |
| `DeploymentConfig` | A `DeploymentConfig` object is created either to deploy the output of a build, or a specified image. The `new-app` command creates `emptyDir` volumes for all Docker volumes that are specified in containers included in the resulting `DeploymentConfig` object. |
| `Service` | The `new-app` command attempts to detect exposed ports in input images. It uses the lowest numeric exposed port to generate a service that exposes that port. To expose a different port, after `new-app` has completed, use the `oc expose` command to generate additional services. |
| Other | Other objects can be generated when creating applications from templates, according to the template. |

`new-app` output objects

## Specifying environment variables

When generating applications from a template, source, or an image, you can use the `-e|--env` argument to pass environment variables to the application container at run time.

``` terminal
$ oc new-app openshift/postgresql-92-centos7 \
    -e POSTGRESQL_USER=user \
    -e POSTGRESQL_DATABASE=db \
    -e POSTGRESQL_PASSWORD=password
```

The variables can also be read from file using the `--env-file` argument. The following is an example file called `postgresql.env`:

``` terminal
POSTGRESQL_USER=user
POSTGRESQL_DATABASE=db
POSTGRESQL_PASSWORD=password
```

Read the variables from the file:

``` terminal
$ oc new-app openshift/postgresql-92-centos7 --env-file=postgresql.env
```

Additionally, environment variables can be given on standard input by using the `--env-file=-` argument:

``` terminal
$ cat postgresql.env | oc new-app openshift/postgresql-92-centos7 --env-file=-
```

> [!NOTE]
> Any `BuildConfig` objects created as part of `new-app` processing are not updated with environment variables passed with the `-e|--env` or `--env-file` argument.

## Specifying build environment variables

When generating applications from a template, source, or an image, you can use the `--build-env` argument to pass environment variables to the build container at run time:

``` terminal
$ oc new-app openshift/ruby-23-centos7 \
    --build-env HTTP_PROXY=http://myproxy.net:1337/ \
    --build-env GEM_HOME=~/.gem
```

The variables can also be read from a file using the `--build-env-file` argument. The following is an example file called `ruby.env`:

``` terminal
HTTP_PROXY=http://myproxy.net:1337/
GEM_HOME=~/.gem
```

Read the variables from the file:

``` terminal
$ oc new-app openshift/ruby-23-centos7 --build-env-file=ruby.env
```

Additionally, environment variables can be given on standard input by using `--build-env-file=-`:

``` terminal
$ cat ruby.env | oc new-app openshift/ruby-23-centos7 --build-env-file=-
```

## Specifying labels

When generating applications from source, images, or templates, you can use the `-l|--label` argument to add labels to the created objects. Labels make it easy to collectively select, configure, and delete objects associated with the application.

``` terminal
$ oc new-app https://github.com/openshift/ruby-hello-world -l name=hello-world
```

## Viewing the output without creation

You can preview objects without creating them by using `-o` or `--output` with a `yaml` or `json` value. Redirect the output to a file, edit the file, then create the objects with `oc create`.

<div class="formalpara">

<div class="title">

Writing `new-app` output to a file

</div>

``` terminal
$ oc new-app https://github.com/openshift/ruby-hello-world \
    -o yaml > myapp.yaml
```

</div>

<div class="formalpara">

<div class="title">

Creating objects from an edited file

</div>

``` terminal
$ oc create -f myapp.yaml
```

</div>

## Creating objects with different names

Objects created by `new-app` are normally named after the source repository, or the image used to generate them. You can set the name of the objects produced by adding a `--name` flag to the command:

``` terminal
$ oc new-app https://github.com/openshift/ruby-hello-world --name=myapp
```

## Creating objects in a different project

Normally, `new-app` creates objects in the current project. However, you can create objects in a different project by using the `-n|--namespace` argument:

``` terminal
$ oc new-app https://github.com/openshift/ruby-hello-world -n myproject
```

## Creating multiple objects

You can create multiple applications by specifying multiple parameters to `new-app`. Labels specified in the command line apply to all objects created by the single command. Environment variables apply to all components created from source or images.

To create an application from a source repository and a Docker Hub image:

``` terminal
$ oc new-app https://github.com/openshift/ruby-hello-world mysql
```

> [!NOTE]
> If a source code repository and a builder image are specified as separate arguments, `new-app` uses the builder image as the builder for the source code repository. If this is not the intent, specify the required builder image for the source using the `~` separator.

## Grouping images and source in a single pod

You can deploy multiple images together in a single pod. To specify which images to group together, use the `+` separator. The `--group` command-line argument can also be used to specify the images that should be grouped together. To group the image built from a source repository with other images, specify the builder image for the source in the group:

``` terminal
$ oc new-app ruby+mysql
```

To deploy an image built from source and an external image together:

``` terminal
$ oc new-app \
    ruby~https://github.com/openshift/ruby-hello-world \
    mysql \
    --group=ruby+mysql
```

## Searching for images, templates, and other inputs

To search for images, templates, and other inputs for the `oc new-app` command, add the `--search` and `--list` flags. For example, to find all of the images or templates that include PHP:

``` terminal
$ oc new-app --search php
```

## Setting the import mode

To set the import mode when using `oc new-app`, add the `--import-mode` flag. This flag can be appended with `Legacy` or `PreserveOriginal`, which provides users the option to create image streams using a single sub-manifest, or all manifests, respectively.

``` terminal
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest --import-mode=Legacy --name=test
```

``` terminal
$ oc new-app --image=registry.redhat.io/ubi8/httpd-24:latest --import-mode=PreserveOriginal --name=test
```
