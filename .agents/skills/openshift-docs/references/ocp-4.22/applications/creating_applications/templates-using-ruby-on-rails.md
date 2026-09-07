<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can build and deploy a Ruby on Rails 4 application on OpenShift Container Platform by developing it locally.

Store the source in Git, then deploy the database, frontend, and route services. With this process, you can validate your application locally before deploying it to the cluster as a set of distinct services.

> [!WARNING]
> You must complete each part of this tutorial in order to before you deploy your application on OpenShift Container Platform. If a step fails, confirm that every preceding step completed successfully before you continue.

# Prerequisites

- You have basic Ruby on Rails knowledge.

- You have Ruby 2.0.0+, Rubygems, and Bundler installed locally.

- You have basic Git knowledge.

- You have a running instance of OpenShift Container Platform 4.

- The OpenShift CLI (`oc`) installed.

- You are logged into a running OpenShift Container Platform cluster.

# Setting up the database

You can install PostgreSQL on your local system for Ruby on Rails development. This gives your application a local database to connect to during development and testing before you deploy to OpenShift Container Platform.

<div>

<div class="title">

Procedure

</div>

1.  Install the database by running the following command:

    ``` terminal
    $ sudo yum install -y postgresql postgresql-server postgresql-devel
    ```

2.  Initialize the database by running the following command:

    ``` terminal
    $ sudo postgresql-setup initdb
    ```

    This command creates the `/var/lib/pgsql/data` directory, in which the data is stored.

3.  Start the database by running the following command:

    ``` terminal
    $ sudo systemctl start postgresql.service
    ```

4.  When the database is running, create your `rails` user by running the following command:

    ``` terminal
    $ sudo -u postgres createuser -s rails
    ```

    > [!NOTE]
    > The user that is created has no password.

</div>

# Writing your application

You can create a Ruby on Rails application that uses PostgreSQL. Install the Rails gem, configure the `database.yml` file, and initialize the development and test databases. These steps ensure that your application can interact with PostgreSQL in both development and test environments.

<div>

<div class="title">

Procedure

</div>

1.  Install the Rails gem by running the following command:

    ``` terminal
    $ gem install rails
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Successfully installed rails-4.3.0
    1 gem installed
    ```

    </div>

2.  Create a new application with PostgreSQL as your database by running the following command:

    ``` terminal
    $ rails new rails-app --database=postgresql
    ```

3.  Change into your new application directory by running the following command:

    ``` terminal
    $ cd rails-app
    ```

4.  If you already have an application, ensure that the PostgreSQL adapter gem (`pg`) is present in your `Gemfile`. If not, edit your `Gemfile` by adding the gem:

    ``` terminal
    gem 'pg'
    ```

5.  Generate a new `Gemfile.lock` with all your dependencies by running the following command:

    ``` terminal
    $ bundle install
    ```

6.  Update the `default` section in the `config/database.yml` file to use the `postgresql` adapter, as shown in the following example:

    ``` yaml
    default: &default
      adapter: postgresql
      encoding: unicode
      pool: 5
      host: localhost
      username: rails
      password: <password>
    ```

7.  Create the `development` and `test` databases for your application by running the following command:

    ``` terminal
    $ rake db:create
    ```

</div>

## Creating a welcome page

You can run the Rails generator to create a custom welcome page for your Rails application. A welcome page gives you content to display when you run the Rails server and open the application in your browser.

<div>

<div class="title">

Procedure

</div>

1.  Run the Rails generator by running the following command:

    ``` terminal
    $ rails generate controller welcome index
    ```

    The command creates all the necessary files.

2.  Edit line 2 in the `config/routes.rb` file as follows:

    ``` ruby
    root 'welcome#index'
    ```

3.  Run the Rails server to verify that the page is available by running the following command:

    ``` terminal
    $ rails server
    ```

    Verify that the page is available by visiting `http://localhost:3000` in your browser. If the page does not display, check the server logs for errors.

</div>

## Configuring application for OpenShift Container Platform

To configure your Rails application for OpenShift Container Platform, you must edit the `default` section in the `config/database.yml` file. This is required for OpenShift Container Platform to supply the correct database credentials at runtime so your application can connect to PostgreSQL on the cluster.

<div>

<div class="title">

Procedure

</div>

- Edit the `default` section in your `config/database.yml` with pre-defined variables as follows:

  <div class="formalpara">

  <div class="title">

  Sample `config/database` YAML file

  </div>

  ``` eruby
  <% user = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? "root" : ENV["POSTGRESQL_USER"] %>
  <% password = ENV.key?("POSTGRESQL_ADMIN_PASSWORD") ? ENV["POSTGRESQL_ADMIN_PASSWORD"] : ENV["POSTGRESQL_PASSWORD"] %>
  <% db_service = ENV.fetch("DATABASE_SERVICE_NAME","").upcase %>

  default: &default
    adapter: postgresql
    encoding: unicode
    # For details on connection pooling, see rails configuration guide
    # http://guides.rubyonrails.org/configuring.html#database-pooling
    pool: <%= ENV["POSTGRESQL_MAX_CONNECTIONS"] || 5 %>
    username: <%= user %>
    password: <%= password %>
    host: <%= ENV["#{db_service}_SERVICE_HOST"] %>
    port: <%= ENV["#{db_service}_SERVICE_PORT"] %>
    database: <%= ENV["POSTGRESQL_DATABASE"] %>
  ```

  </div>

</div>

## Storing your application in Git

You can commit your Rails application to Git and push the source to a remote repository. Remote storage keeps your source available for deployment on OpenShift Container Platform.

<div>

<div class="title">

Prerequisites

</div>

- You have installed Git.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Verify that you are in your Rails application directory by running the following command:

    ``` terminal
    $ ls -1
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    app
    bin
    config
    config.ru
    db
    Gemfile
    Gemfile.lock
    lib
    log
    public
    Rakefile
    README.rdoc
    test
    tmp
    vendor
    ```

    </div>

2.  Initialize a Git repository in your Rails application directory by running the following command:

    ``` terminal
    $ git init
    ```

3.  Stage all application files by running the following command:

    ``` terminal
    $ git add .
    ```

4.  Commit the staged files by running the following command:

    ``` terminal
    $ git commit -m "initial commit"
    ```

5.  Create a GitHub repository for your application.

6.  Set the remote that points to your `git` repository by running the following command:

    ``` terminal
    $ git remote add origin git@github.com:<namespace/repository-name>.git
    ```

7.  Push your application to your remote Git repository by running the following command:

    ``` terminal
    $ git push
    ```

</div>

# Deploying your application to OpenShift Container Platform

You can create an OpenShift Container Platform project to deploy your Ruby on Rails application. This separates your database, frontend, and route into distinct services that OpenShift Container Platform can manage independently.

Deploying your application on OpenShift Container Platform takes three steps:

1.  Creating a database service from the PostgreSQL image on OpenShift Container Platform.

2.  Creating a frontend service from the Ruby 2.0 builder image on OpenShift Container Platform and your Ruby on Rails source code, connected to the database service.

3.  Creating a route for your application.

<div>

<div class="title">

Procedure

</div>

- Create a project for your Rails application by running the following command:

  ``` terminal
  $ oc new-project rails-app --description="My Rails application" --display-name="Rails Application"
  ```

</div>

## Creating the database service

You must create a database service for your Rails application. Be sure to set the environment variables for the database name, username, and password. These are required for the service to connect correctly to your Rails application.

You can change the values of these environment variables to any values you choose. The variables are as follows:

- `POSTGRESQL_DATABASE`

- `POSTGRESQL_USER`

- `POSTGRESQL_PASSWORD`

Setting these variables ensures that the following occurs:

- A database exists with the specified name.

- A user exists with the specified name.

- The user can access the specified database with the specified password.

<div>

<div class="title">

Procedure

</div>

1.  Create the database service by running the following command:

    ``` terminal
    $ oc new-app postgresql -e POSTGRESQL_DATABASE=db_name -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password
    ```

    > [!NOTE]
    > To also set a database administrator password, add `-e POSTGRESQL_ADMIN_PASSWORD=admin_pw` to the command.

2.  Monitor the pod status by running the following command:

    ``` terminal
    $ oc get pods --watch
    ```

</div>

## Creating the frontend service

You can create a frontend service with the `oc new-app` command. Specifying your source repository and database environment variables enables OpenShift Container Platform to build your application image and deploy it on the cluster.

<div>

<div class="title">

Procedure

</div>

1.  Create the frontend service and specify the database-related environment variables that were set up when creating the database service by running the following command:

    ``` terminal
    $ oc new-app path/to/source/code --name=rails-app -e POSTGRESQL_USER=username -e POSTGRESQL_PASSWORD=password -e POSTGRESQL_DATABASE=db_name -e DATABASE_SERVICE_NAME=postgresql
    ```

    With this command, OpenShift Container Platform fetches the source code, sets up the builder, builds your application image, and deploys the newly created image together with the specified environment variables. The application is named `rails-app`.

2.  Verify that the environment variables have been added by viewing the JSON document of the `rails-app` deployment config by running the following command:

    ``` terminal
    $ oc get dc rails-app -o json
    ```

    The output includes the following section:

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` json
    env": [
        {
            "name": "POSTGRESQL_USER",
            "value": "username"
        },
        {
            "name": "POSTGRESQL_PASSWORD",
            "value": "password"
        },
        {
            "name": "POSTGRESQL_DATABASE",
            "value": "db_name"
        },
        {
            "name": "DATABASE_SERVICE_NAME",
            "value": "postgresql"
        }

    ],
    ```

    </div>

3.  Check the build process by running the following command:

    ``` terminal
    $ oc logs -f build/rails-app-1
    ```

4.  After the build is complete, check the running pods in OpenShift Container Platform by running the following command:

    ``` terminal
    $ oc get pods
    ```

    The output includes a line starting with `myapp-<number>-<hash>`, which confirms that the application is running in OpenShift Container Platform.

5.  Before your application is functional, you must initialize the database by running the database migration script. There are two ways you can do this:

    - Manually from the running frontend container:

      - Open a remote shell to the frontend pod by running the following command:

        ``` terminal
        $ oc rsh <frontend_pod_id>
        ```

      - Run the migration from inside the container by running the following command:

        ``` terminal
        $ RAILS_ENV=production bundle exec rake db:migrate
        ```

        If you are running your Rails application in a `development` or `test` environment, you do not have to specify the `RAILS_ENV` environment variable.

    - You can also run the migration by adding pre-deployment lifecycle hooks to your template.

</div>

## Creating a route for your application

You can create a route for your application with the `oc expose service` command. The route makes the application accessible from outside the cluster.

<div>

<div class="title">

Procedure

</div>

- Make the frontend service accessible externally by running the following command:

  ``` terminal
  $ oc expose service rails-app --hostname=www.example.com
  ```

  > [!WARNING]
  > Ensure that the hostname you specify resolves to the IP address of the router.

</div>
