<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use templates to deploy preconfigured applications and create reusable object definitions on your OpenShift Container Platform cluster. Upload, instantiate, and author templates from the web console or CLI to speed up application creation.

# Understanding templates

You can use templates to describe reusable, parameterized object sets that OpenShift Container Platform processes into resources such as `Service` and `DeploymentConfig` objects. Templates help you deploy the same application structure consistently from the web console or CLI.

A template can be processed to create anything you have permission to create within a project. A template can also define a set of labels to apply to every object defined in the template.

# Uploading a template

To add a template to your OpenShift Container Platform project, upload a JSON or YAML template file with the CLI. Uploaded templates are saved to the project template library for reuse by users with access to that project.

<div>

<div class="title">

Procedure

</div>

- Upload a template using one of the following methods:

  - Upload a JSON or YAML template file to the template library of your current project by running the following command:

    ``` terminal
    $ oc create -f <filename>
    ```

  - Upload a template to a different project using the `-n` option with the name of the project by running the following command:

    ``` terminal
    $ oc create -f <filename> -n <project>
    ```

    The template is now available for selection using the web console or the CLI.

</div>

# Creating an application by using the web console

To create an application from a template on your OpenShift Container Platform cluster, use the web console **Developer Catalog**. Select a template or builder image and configure the generated objects before you deploy.

<div>

<div class="title">

Procedure

</div>

1.  Navigate to your project and click **+Add**.

2.  Click **All services** in the **Developer Catalog** tile.

3.  Click **Builder Images** under **Type** to see the available builder images.

    > [!NOTE]
    > Only image stream tags that have the `builder` tag listed in their annotations appear in this list, as demonstrated in the following example. Include `builder` in the `tags` annotation so the image stream tag appears in the web console as a builder.

    ``` yaml
    kind: "ImageStream"
    apiVersion: "image.openshift.io/v1"
    metadata:
      name: "ruby"
      creationTimestamp: null
    spec:
    # ...
      tags:
        - name: "2.6"
          annotations:
            description: "Build and run Ruby 2.6 applications"
            iconClass: "icon-ruby"
            tags: "builder,ruby"
            supports: "ruby:2.6,ruby"
            version: "2.6"
    # ...
    ```

4.  Modify the settings in the new application screen to configure the objects to support your application.

</div>

# Creating objects from templates by using the CLI

You can use the CLI to create objects from templates on your OpenShift Container Platform cluster by processing a template into a list of objects in your project. Use CLI commands to manage template labels, parameters, and generated object lists.

## Adding labels

To add labels when you process a template on your OpenShift Container Platform cluster, pass label selectors to the `oc process` command. The labels specified in the template are applied to every object that is generated from the template.

Labels are used to manage and organize generated objects, such as pods.

<div>

<div class="title">

Procedure

</div>

- Add labels in the template by running the following command:

  ``` terminal
  $ oc process -f <filename> -l name=otherLabel
  ```

</div>

## Listing parameters

You can list template parameters on your OpenShift Container Platform cluster to see which values you can override before processing a template. Use the `oc process --parameters` command with a template file or uploaded template name.

<div>

<div class="title">

Procedure

</div>

- List template parameters from a local template file by running the following command:

  ``` terminal
  $ oc process --parameters -f <filename>
  ```

- List template parameters from an uploaded template by running the following command:

  ``` terminal
  $ oc process --parameters -n <project> <template_name>
  ```

  For example, to list parameters for the `rails-postgresql-example` quick start template in the default `openshift` project, run the following command:

  ``` terminal
  $ oc process --parameters -n openshift rails-postgresql-example
  ```

  <div class="formalpara">

  <div class="title">

  Example output

  </div>

  ``` terminal
  NAME                         DESCRIPTION                                                                                              GENERATOR           VALUE
  SOURCE_REPOSITORY_URL        The URL of the repository with your application source code                                                                  https://github.com/sclorg/rails-ex.git
  SOURCE_REPOSITORY_REF        Set this to a branch name, tag or other ref of your repository if you are not using the default branch
  CONTEXT_DIR                  Set this to the relative path to your project if it is not in the root of your repository
  APPLICATION_DOMAIN           The exposed hostname that will route to the Rails service                                                                    rails-postgresql-example.openshiftapps.com
  GITHUB_WEBHOOK_SECRET        A secret string used to configure the GitHub webhook                                                     expression          [a-zA-Z0-9]{40}
  SECRET_KEY_BASE              Your secret key for verifying the integrity of signed cookies                                            expression          [a-z0-9]{127}
  APPLICATION_USER             The application user that is used within the sample application to authorize access on pages                                 openshift
  APPLICATION_PASSWORD         The application password that is used within the sample application to authorize access on pages                             secret
  DATABASE_SERVICE_NAME        Database service name                                                                                                        postgresql
  POSTGRESQL_USER              database username                                                                                        expression          user[A-Z0-9]{3}
  POSTGRESQL_PASSWORD          database password                                                                                        expression          [a-zA-Z0-9]{8}
  POSTGRESQL_DATABASE          database name                                                                                                                root
  POSTGRESQL_MAX_CONNECTIONS   database max connections                                                                                                     10
  POSTGRESQL_SHARED_BUFFERS    database shared buffers                                                                                                      12MB
  ```

  </div>

  The output identifies several parameters that are generated with a regular expression-like generator when the template is processed.

</div>

## Generating a list of objects

To preview objects a template creates on your OpenShift Container Platform cluster, run `oc process` on the template without applying it. Review the generated object list and save it to a file before you create resources in your project.

<div>

<div class="title">

Procedure

</div>

- Process a file defining a template to return the list of objects to standard output by running the following command:

  ``` terminal
  $ oc process -f <filename>
  ```

- Process an uploaded template in the current project to return the list of objects to standard output by running the following command:

  ``` terminal
  $ oc process <template_name>
  ```

- Create objects from a template by processing the template and piping the output to `oc create` by running the following command:

  ``` terminal
  $ oc process -f <filename> | oc create -f -
  ```

- Create objects from an uploaded template in the current project by processing the template and piping the output to `oc create` by running the following command:

  ``` terminal
  $ oc process <template> | oc create -f -
  ```

- You can override any parameter values defined in the file by adding the `-p` option for each `<name>=<value>` pair you want to override. A parameter reference appears in any text field inside the template items.

  For example, in the following the `POSTGRESQL_USER` and `POSTGRESQL_DATABASE` parameters of a template are overridden to output a configuration with customized environment variables:

  - Create a list of objects from a template by running the following command:

    ``` terminal
    $ oc process -f my-rails-postgresql \
        -p POSTGRESQL_USER=bob \
        -p POSTGRESQL_DATABASE=mydatabase
    ```

  - Create the objects from the processed output by running the following command:

    ``` terminal
    $ oc process -f my-rails-postgresql \
        -p POSTGRESQL_USER=bob \
        -p POSTGRESQL_DATABASE=mydatabase \
        | oc create -f -
    ```

    > [!NOTE]
    > You can redirect the JSON output to a file, or apply it directly without uploading the template by piping it to the `oc create` command.

  - If you have a large number of parameters, you can store them in a file and then pass this file to `oc process` by running the following commands:

    ``` terminal
    $ cat postgres.env
    ```

    ``` terminal
    $ oc process -f my-rails-postgresql --param-file=postgres.env
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    POSTGRESQL_USER=bob
    POSTGRESQL_DATABASE=mydatabase
    ```

    </div>

  - You can also read parameter values from standard input by specifying "-" as the value of the `--param-file` option by running the following command:

    ``` terminal
    $ sed s/bob/alice/ postgres.env | oc process -f my-rails-postgresql --param-file=-
    ```

</div>

# Modifying uploaded templates

To update a template already stored in your OpenShift Container Platform project, edit the template object and replace the existing version. Updated templates remain available in the project template library for reuse.

<div>

<div class="title">

Procedure

</div>

- Modify a template that has already been uploaded by running the following command:

  ``` terminal
  $ oc edit template <template>
  ```

</div>

# Using instant app and quick start templates

To try a sample application from an instant-app template on your OpenShift Container Platform cluster, create the application from the template and optionally fork the source repository of the template. Customize the build configuration to test changes and rebuild the application.

OpenShift Container Platform provides several default instant app and quick start templates to help you get started quickly creating a new application for different languages. Templates are provided for Rails (Ruby), Django (Python), Node.js, CakePHP (PHP), and Dancer (Perl). Your cluster administrator must create these templates in the default, global `openshift` project so you have access to them.

By default, the templates build using a public source repository on GitHub that contains the necessary application code.

<div>

<div class="title">

Procedure

</div>

1.  List the available default instant app and quick start templates by running the following command:

    ``` terminal
    $ oc get templates -n openshift
    ```

2.  Modify the source to build your own version of the application:

    1.  Fork the repository referenced by the default `SOURCE_REPOSITORY_URL` parameter of the template.

    2.  Override the value of the `SOURCE_REPOSITORY_URL` parameter when creating from the template, specifying your fork instead of the default value.

        By doing this, the build configuration created by the template now points to your fork of the application code. You can then modify the code and rebuild the application as needed.

        > [!NOTE]
        > Some of the instant app and quick start templates define a database `DeploymentConfig` object. The configuration they define uses ephemeral storage for the database content. These templates should be used for demonstration purposes only as all database data is lost if the database pod restarts for any reason.

</div>

## Quick start templates

To browse sample instant app and quick start templates on your OpenShift Container Platform cluster, review the default templates in the `openshift` project. Use these templates to deploy example applications for common languages and frameworks.

A quick start template is a basic example of an application running on OpenShift Container Platform. Quick starts come in a variety of languages and frameworks, and are defined in a template, which is constructed from a set of `Service`, `BuildConfig`, and `DeploymentConfig` objects. This template references the necessary images and source repositories to build and deploy the application.

Your administrator must have already installed these templates in your OpenShift Container Platform cluster, in which case you can select it from the web console.

Quick starts refer to a source repository that contains the application source code. To customize the quick start, fork the repository and, when creating an application from the template, substitute the default source repository name with your forked repository. This results in builds that are performed using your source code instead of the provided example source. You can then update the code in your source repository and launch a new build to see the changes reflected in the deployed application.

### Web framework quick start templates

These quick start templates provide a basic application of the indicated framework and language:

- CakePHP: a PHP web framework that includes a MySQL database

- Dancer: a Perl web framework that includes a MySQL database

- Django: a Python web framework that includes a PostgreSQL database

- NodeJS: a NodeJS web application that includes a MongoDB database

- Rails: a Ruby web framework that includes a PostgreSQL database

# Writing templates

To define reusable application templates on your OpenShift Container Platform cluster, create a `Template` object that lists the resources to deploy and metadata that guides their creation.

Use the following sample YAML to review the structure before you author your own template.

``` yaml
apiVersion: template.openshift.io/v1
kind: Template
metadata:
  name: redis-template
  annotations:
    description: "Description"
    iconClass: "icon-redis"
    tags: "database,nosql"
objects:
- apiVersion: v1
  kind: Pod
  metadata:
    name: redis-master
  spec:
    containers:
    - env:
      - name: REDIS_PASSWORD
        value: ${REDIS_PASSWORD}
      image: dockerfile/redis
      name: master
      ports:
      - containerPort: 6379
        protocol: TCP
parameters:
- description: Password used for Redis authentication
  from: '[A-Z0-9]{8}'
  generate: expression
  name: REDIS_PASSWORD
labels:
  redis: master
```

## Writing the template description

To help users find and understand your template in the web console, add description metadata such as display name, tags, and icon class. Use the annotations in this reference to document purpose, caveats, and support links.

The following is an example of template description metadata:

``` yaml
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: cakephp-mysql-example
  annotations:
    openshift.io/display-name: "CakePHP MySQL Example (Ephemeral)"
    description: >-
      An example CakePHP application with a MySQL database. For more information
      about using this template, including OpenShift considerations, see
      https://github.com/sclorg/cakephp-ex/blob/master/README.md.

      WARNING: Any data stored will be lost upon pod destruction. Only use this
      template for testing."
    openshift.io/long-description: >-
      This template defines resources needed to develop a CakePHP application,
      including a build configuration, application DeploymentConfig, and
      database DeploymentConfig.  The database is stored in
      non-persistent storage, so this configuration should be used for
      experimental purposes only.
    tags: "quickstart,php,cakephp"
    iconClass: icon-php
    openshift.io/provider-display-name: "Red Hat, Inc."
    openshift.io/documentation-url: "https://github.com/sclorg/cakephp-ex"
    openshift.io/support-url: "https://access.redhat.com"
message: "Your admin credentials are ${ADMIN_USERNAME}:${ADMIN_PASSWORD}"
```

where:

`metadata.name`
Specifies the unique name of the template.

`metadata.annotations.openshift.io/display-name`
Specifies a brief, user-friendly name, which can be employed by user interfaces.

`metadata.annotations.description`
Specifies a description of the template. Include enough detail that users understand what is being deployed and any caveats they must know before deploying. It should also provide links to additional information, such as a README file. You can include line breaks to create paragraphs.

`metadata.annotations.openshift.io/long-description`
Specifies an additional template description. This might be displayed by the service catalog.

`metadata.annotations.tags`
Specifies the tags to be associated with the template for searching and grouping. Add tags that group the template into one of the provided catalog categories. Refer to the `id` and `categoryAliases` in `CATALOG_CATEGORIES` in the console constants file. The categories can also be customized for the whole cluster.

`metadata.annotations.iconClass`
Specifies an icon to be displayed with your template in the web console.

The following is a list of available icons.

<div class="informalexample">

- `icon-3scale`

- `icon-aerogear`

- `icon-amq`

- `icon-angularjs`

- `icon-ansible`

- `icon-apache`

- `icon-beaker`

- `icon-camel`

- `icon-capedwarf`

- `icon-cassandra`

- `icon-catalog-icon`

- `icon-clojure`

- `icon-codeigniter`

- `icon-cordova`

- `icon-datagrid`

- `icon-datavirt`

- `icon-debian`

- `icon-decisionserver`

- `icon-django`

- `icon-dotnet`

- `icon-drupal`

- `icon-eap`

- `icon-elastic`

- `icon-erlang`

- `icon-fedora`

- `icon-freebsd`

- `icon-git`

- `icon-github`

- `icon-gitlab`

- `icon-glassfish`

- `icon-go-gopher`

- `icon-golang`

- `icon-grails`

- `icon-hadoop`

- `icon-haproxy`

- `icon-helm`

- `icon-infinispan`

- `icon-jboss`

- `icon-jenkins`

- `icon-jetty`

- `icon-joomla`

- `icon-jruby`

- `icon-js`

- `icon-knative`

- `icon-kubevirt`

- `icon-laravel`

- `icon-load-balancer`

- `icon-mariadb`

- `icon-mediawiki`

- `icon-memcached`

- `icon-mongodb`

- `icon-mssql`

- `icon-mysql-database`

- `icon-nginx`

- `icon-nodejs`

- `icon-openjdk`

- `icon-openliberty`

- `icon-openshift`

- `icon-openstack`

- `icon-other-linux`

- `icon-other-unknown`

- `icon-perl`

- `icon-phalcon`

- `icon-php`

- `icon-play`

- `iconpostgresql`

- `icon-processserver`

- `icon-python`

- `icon-quarkus`

- `icon-rabbitmq`

- `icon-rails`

- `icon-redhat`

- `icon-redis`

- `icon-rh-integration`

- `icon-rh-spring-boot`

- `icon-rh-tomcat`

- `icon-ruby`

- `icon-scala`

- `icon-serverlessfx`

- `icon-shadowman`

- `icon-spring-boot`

- `icon-spring`

- `icon-sso`

- `icon-stackoverflow`

- `icon-suse`

- `icon-symfony`

- `icon-tomcat`

- `icon-ubuntu`

- `icon-vertx`

- `icon-wildfly`

- `icon-windows`

- `icon-wordpress`

- `icon-xamarin`

- `icon-zend`

</div>

`metadata.annotations.openshift.io/provider-display-name`
Specifies the name of the person or organization providing the template.

`metadata.annotations.openshift.io/documentation-url`
Specifies a URL referencing further documentation for the template.

`metadata.annotations.openshift.io/support-url`
Specifies a URL where support can be obtained for the template.

`message`
Specifies an instructional message that is displayed when this template is instantiated. This field should inform the user how to use the newly created resources. Parameter substitution is performed on the message before being displayed so that generated credentials and other parameters can be included in the output. Include links to any next-steps documentation that users should follow.

## Writing template labels

To label every object created from a template, add a `labels` section to the template definition. Use parameterized labels so users can identify and manage resources created from your template.

The following is an example of template object labels:

``` yaml
kind: "Template"
apiVersion: "v1"
...
labels:
  template: "cakephp-mysql-example"
  app: "${NAME}"
```

where:

`labels.template`
Specifies a label that is applied to all objects created from this template.

`labels.app`
Specifies a parameterized label that is also applied to all objects created from this template. Parameter expansion is carried out on both label keys and values.

## Writing template parameters

To customize a template when you process it, define parameters with default or generated values and reference them in template fields. Use string or JSON substitution syntax to pass user-specific values into created objects.

Parameters allow a value to be supplied by you or generated when you process the template. Then, that value is substituted wherever the parameter is referenced. References can be defined in any field in the objects list field. This is useful for generating random passwords or allowing you to supply a hostname or other user-specific value that is required to customize the template. Parameters can be referenced in two ways:

- As a string value by placing values in the form `${PARAMETER_NAME}` in any string field in the template.

- As a JSON or YAML value by placing values in the form `${{PARAMETER_NAME}}` in place of any field in the template.

When using the `${PARAMETER_NAME}` syntax, multiple parameter references can be combined in a single field and the reference can be embedded within fixed data, such as `"http://${PARAMETER_1}${PARAMETER_2}"`. Both parameter values are substituted and the resulting value is a quoted string.

When using the `${{PARAMETER_NAME}}` syntax, only a single parameter reference is allowed and leading and trailing characters are not permitted. The resulting value is unquoted unless, after substitution is performed, the result is not a valid JSON object. If the result is not a valid JSON value, the resulting value is quoted and treated as a standard string.

A single parameter can be referenced multiple times within a template and it can be referenced using both substitution syntaxes within a single template.

A default value can be provided, which is used if you do not supply a different value:

The following is an example of setting an explicit value as the default value:

``` yaml
parameters:
  - name: USERNAME
    description: "The user name for Joe"
    value: joe
```

Parameter values can also be generated based on rules specified in the parameter definition:

``` yaml
parameters:
  - name: PASSWORD
    description: "The random user password"
    generate: expression
    from: "[a-zA-Z0-9]{12}"
```

In the previous example, processing generates a random password 12 characters long consisting of all upper and lowercase alphabet letters and numbers.

The syntax available is not a full regular expression syntax. However, you can use `\w`, `\d`, `\a`, and `\A` modifiers:

- `[\w]{10}` produces 10 alphabet characters, numbers, and underscores. This follows the PCRE standard and is equal to `[a-zA-Z0-9_]{10}`.

- `[\d]{10}` produces 10 numbers. This is equal to `[0-9]{10}`.

- `[\a]{10}` produces 10 alphabetical characters. This is equal to `[a-zA-Z]{10}`.

- `[\A]{10}` produces 10 punctuation or symbol characters. This is equal to `` [~!@#$%\^&*()\-_+={}\[\]\\|<,>.?/"';:`]{10} ``.

> [!NOTE]
> Depending on whether the template is written in YAML or JSON, you might need to escape the backslash with a second backslash. This also depends on the type of string in which the modifier is embedded. The following examples are equivalent:
>
> <div class="formalpara">
>
> <div class="title">
>
> Example YAML template with a modifier
>
> </div>
>
> ``` yaml
>   parameters:
>   - name: singlequoted_example
>     generate: expression
>     from: '[\A]{10}'
>   - name: doublequoted_example
>     generate: expression
>     from: "[\\A]{10}"
> ```
>
> </div>
>
> <div class="formalpara">
>
> <div class="title">
>
> Example JSON template with a modifier
>
> </div>
>
> ``` json
> {
>     "parameters": [
>        {
>         "name": "json_example",
>         "generate": "expression",
>         "from": "[\\A]{10}"
>        }
>     ]
> }
> ```
>
> </div>

Here is an example of a full template with parameter definitions and references:

``` yaml
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: my-template
objects:
  - kind: BuildConfig
    apiVersion: build.openshift.io/v1
    metadata:
      name: cakephp-mysql-example
      annotations:
        description: Defines how to build the application
    spec:
      source:
        type: Git
        git:
          uri: "${SOURCE_REPOSITORY_URL}"
          ref: "${SOURCE_REPOSITORY_REF}"
        contextDir: "${CONTEXT_DIR}"
  - kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: frontend
    spec:
      replicas: "${{REPLICA_COUNT}}"
parameters:
  - name: SOURCE_REPOSITORY_URL
    displayName: Source Repository URL
    description: The URL of the repository with your application source code
    value: https://github.com/sclorg/cakephp-ex.git
    required: true
  - name: GITHUB_WEBHOOK_SECRET
    description: A secret string used to configure the GitHub webhook
    generate: expression
    from: "[a-zA-Z0-9]{40}"
  - name: REPLICA_COUNT
    description: Number of replicas to run
    value: "2"
    required: true
message: "... The GitHub webhook secret is ${GITHUB_WEBHOOK_SECRET} ..."
```

where:

`spec.git.uri`
Specifies the value to be replaced with the value of the `SOURCE_REPOSITORY_URL` parameter when you process the template.

`spec.replicas`
Specifies the value to be replaced with the unquoted value of the `REPLICA_COUNT` parameter when you process the template.

`parameters.name`
Specifies the name of the parameter. This value is used to reference the parameter within the template.

`parameters.displayName`
Specifies the user-friendly name for the parameter. This is displayed to users.

`parameters.description`
Specifies a description of the parameter. Provide more detailed information for the purpose of the parameter, including any constraints on the expected value. Descriptions should use complete sentences to follow the console text standards. Do not make this a duplicate of the display name.

`parameters.value`
Specifies a default value for the parameter which is used if you do not override the value when you process the template. Avoid using default values for things like passwords, instead use generated parameters in combination with secrets.

`parameters.required`
Specifies that this parameter is required, meaning you cannot override it with an empty value. If the parameter does not provide a default or generated value, you must supply a value.

`parameters.generate`
Specifies that the parameter value is generated.

`parameters.from`
Specifies the input to the generator. In this case, the generator produces a 40 character alphanumeric value including upper and lowercase characters.

`message`
Specifies that parameters can be included in the template message. This field informs you about generated values.

## Writing the template object list

To specify what a template creates when processed, define an `objects` list with the API resources to deploy. Parameter values are substituted into each object definition before creation.

The following is an example of an object list:

``` yaml
kind: "Template"
apiVersion: "v1"
metadata:
  name: my-template
objects:
  - kind: "Service"
    apiVersion: "v1"
    metadata:
      name: "cakephp-mysql-example"
      annotations:
        description: "Exposes and load balances the application pods"
    spec:
      ports:
        - name: "web"
          port: 8080
          targetPort: 8080
      selector:
        name: "cakephp-mysql-example"
```

where:

`objects.kind`
Specifies the definition of a service, which is created by this template.

> [!NOTE]
> If an object definition metadata includes a fixed `namespace` field value, the field is stripped out of the definition during template instantiation. If the `namespace` field contains a parameter reference, normal parameter substitution is performed, and the object is created in the resulting namespace. This requires that the user has permission to create objects in that namespace.

## Marking a template as bindable

To prevent end users from binding to services provisioned from your template, add the `template.openshift.io/bindable: "false"` annotation to the template object. By default, the Template Service Broker advertises each template service as bindable in the service catalog.

<div>

<div class="title">

Procedure

</div>

- Prevent end users from binding against services provisioned from a given template by adding the annotation `template.openshift.io/bindable: "false"` to the template.

</div>

## Exposing template object fields

To return connection details when users bind to your template service, add `template.openshift.io/expose-` or `template.openshift.io/base64-expose-` annotations to `ConfigMap`, `Secret`, `Service`, or `Route` objects. Binding clients then receive the needed credentials and endpoints directly.

Each annotation key, with the prefix removed, is passed through to become a key in a `bind` response.

Each annotation value is a Kubernetes JSONPath expression, which is resolved at bind time to indicate the object field whose value should be returned in the `bind` response.

> [!NOTE]
> Unless escaped with a backslash, the JSONPath implementation of Kubernetes interprets characters such as `.`, `@`, and others as metacharacters, regardless of their position in the expression. Therefore, for example, to refer to a `ConfigMap` data named `my.key`, the required JSONPath expression is `{.data['my\.key']}`. Depending on how the JSONPath expression is then written in YAML, an additional backslash might be required, for example `"{.data['my\\.key']}"`.

The following is an example of fields of different objects being exposed:

``` yaml
kind: Template
apiVersion: template.openshift.io/v1
metadata:
  name: my-template
objects:
- kind: ConfigMap
  apiVersion: v1
  metadata:
    name: my-template-config
    annotations:
      template.openshift.io/expose-username: "{.data['my\\.username']}"
  data:
    my.username: foo
- kind: Secret
  apiVersion: v1
  metadata:
    name: my-template-config-secret
    annotations:
      template.openshift.io/base64-expose-password: "{.data['password']}"
  stringData:
    password: <password>
- kind: Service
  apiVersion: v1
  metadata:
    name: my-template-service
    annotations:
      template.openshift.io/expose-service_ip_port: "{.spec.clusterIP}:{.spec.ports[?(.name==\"web\")].port}"
  spec:
    ports:
    - name: "web"
      port: 8080
- kind: Route
  apiVersion: route.openshift.io/v1
  metadata:
    name: my-template-route
    annotations:
      template.openshift.io/expose-uri: "http://{.spec.host}{.spec.path}"
  spec:
    path: mypath
```

> [!NOTE]
> `Bind` response key-value pairs can be used in other parts of the system as environment variables. Therefore, each annotation key, with the prefix removed, should be a valid environment variable name. Valid names begin with a character `A-Z`, `a-z`, or `_`, followed by zero or more characters `A-Z`, `a-z`, `0-9`, or `_`.

An example response to a `bind` operation given the previous partial template:

``` json
{
  "credentials": {
    "username": "foo",
    "password": "YmFy",
    "service_ip_port": "172.30.12.34:8080",
    "uri": "http://route-test.router.default.svc.cluster.local/mypath"
  }
}
```

<div>

<div class="title">

Procedure

</div>

- Use the `template.openshift.io/expose-` annotation to return the field value as a string. This approach does not handle arbitrary binary data.

- If you want to return binary data, use the `template.openshift.io/base64-expose-` annotation instead to Base64 encode the data before it is returned.

</div>

## Waiting for template readiness

To delay creating resources from a template until key resources are ready, add the `template.alpha.openshift.io/wait-for-ready: "true"` annotation to supported object kinds. The service catalog, Template Service Broker, and `TemplateInstance` API wait for annotated objects to report ready.

Before starting the procedure, read the following considerations:

- Set memory, CPU, and storage default sizes to ensure your application is given enough resources to run smoothly.

- Avoid referencing the `latest` tag from images if that tag is used across major versions. This can cause running applications to break when new images are pushed to that tag.

- A good template builds and deploys cleanly without requiring modifications after the template is deployed.

<div>

<div class="title">

Procedure

</div>

- To use the template feature, mark one or more objects of kind `Build`, `BuildConfig`, `Deployment`, `DeploymentConfig`, `Job`, or `StatefulSet` in a template with the following annotation:

  ``` text
  "template.alpha.openshift.io/wait-for-ready": "true"
  ```

  Creating resources from the template is not complete until all objects marked with the annotation report ready. Similarly, if any of the annotated objects report failed, or if the template fails to become ready within a fixed timeout of one hour, creating resources from the template fails.

  When you create resources from a template, readiness and failure of each object kind are defined as follows:

  | Kind | Readiness | Failure |
  |----|----|----|
  | `Build` | Object reports phase complete. | Object reports phase canceled, error, or failed. |
  | `BuildConfig` | Latest associated build object reports phase complete. | Latest associated build object reports phase canceled, error, or failed. |
  | `Deployment` | Object reports new replica set and deployment available. This honors readiness probes defined on the object. | Object reports progressing condition as false. |
  | `DeploymentConfig` | Object reports new replication controller and deployment available. This honors readiness probes defined on the object. | Object reports progressing condition as false. |
  | `Job` | Object reports completion. | Object reports that one or more failures have occurred. |
  | `StatefulSet` | Object reports all replicas ready. This honors readiness probes defined on the object. | Not applicable. |

  The following is an example template extract, which uses the `wait-for-ready` annotation. Further examples can be found in the OpenShift Container Platform quick start templates.

  ``` yaml
  kind: Template
  apiVersion: template.openshift.io/v1
  metadata:
    name: my-template
  objects:
  - kind: BuildConfig
    apiVersion: build.openshift.io/v1
    metadata:
      name: ...
      annotations:
        # wait-for-ready used on BuildConfig ensures that creating resources from the template
        # fails immediately if the build fails
        template.alpha.openshift.io/wait-for-ready: "true"
    spec:
      ...
  - kind: DeploymentConfig
    apiVersion: apps.openshift.io/v1
    metadata:
      name: ...
      annotations:
        template.alpha.openshift.io/wait-for-ready: "true"
    spec:
      ...
  - kind: Service
    apiVersion: v1
    metadata:
      name: ...
    spec:
      ...
  ```

</div>

## Creating a template from existing objects

To create a template from existing objects in your project, export those objects and add parameters and other template customizations. Reusing deployed resources helps you capture a working configuration that others can deploy consistently from the template.

<div>

<div class="title">

Procedure

</div>

- Export objects in a project by running the following command:

  ``` terminal
  $ oc get -o yaml all > <yaml_filename>
  ```

  You can also substitute a particular resource type or multiple resources instead of `all`. Run `oc get -h` for more examples.

  The object types included in `oc get -o yaml all` are:

  - `BuildConfig`

  - `Build`

  - `DeploymentConfig`

  - `ImageStream`

  - `Pod`

  - `ReplicationController`

  - `Route`

  - `Service`

    > [!NOTE]
    > Using the `all` alias is not recommended because the contents might vary across different clusters and versions. Instead, specify all required resources.

</div>
