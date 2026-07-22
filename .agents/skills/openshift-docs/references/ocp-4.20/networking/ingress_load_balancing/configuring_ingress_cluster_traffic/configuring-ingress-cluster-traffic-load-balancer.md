<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform provides methods for communicating from outside the cluster with services running in the cluster. This method uses a load balancer.

Before starting the following procedures, the administrator must complete the following prerequisite tasks:

- Set up the external port to the cluster networking environment so that requests can reach the cluster.

- Have an OpenShift Container Platform cluster with at least one control plane node, at least one compute node, and a system outside the cluster that has network access to the cluster. This procedure assumes that the external system is on the same subnet as the cluster. The additional networking required for external systems on a different subnet is out-of-scope for this topic.

- Make sure there is at least one user with cluster admin role. To add this role to a user, run the following command:

  ``` terminal
  $ oc adm policy add-cluster-role-to-user cluster-admin username
  ```

# Using a load balancer to get traffic into the cluster

If you do not need a specific external IP address, you can configure a load balancer service to allow external access to an OpenShift Container Platform cluster.

A load balancer service allocates a unique IP. The load balancer has a single edge router IP, which can be a virtual IP (VIP), but is still a single machine for initial load balancing.

> [!NOTE]
> A pool gets configured at the infrastructure level and not the cluster administrator level.

# Creating a project and service

If the project and service that you want to expose does not exist, create the project and then create the service.

If the project and service already exists, skip to the procedure on exposing the service to create a route.

<div>

<div class="title">

Prerequisites

</div>

- Install the OpenShift CLI (`oc`) and log in as a cluster administrator.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Create a new project for your service by running the `oc new-project` command:

    ``` terminal
    $ oc new-project <project_name>
    ```

2.  Use the `oc new-app` command to create your service:

    ``` terminal
    $ oc new-app nodejs:12~https://github.com/sclorg/nodejs-ex.git
    ```

3.  To verify that the service was created, run the following command:

    ``` terminal
    $ oc get svc -n <project_name>
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME        TYPE        CLUSTER-IP       EXTERNAL-IP   PORT(S)    AGE
    nodejs-ex   ClusterIP   172.30.197.157   <none>        8080/TCP   70s
    ```

    </div>

    > [!NOTE]
    > By default, the new service does not have an external IP address.

</div>

# Exposing the service by creating a route

To enable external access to your application that runs on OpenShift Container Platform, you can expose the service as a route by using the `oc expose` command.

<div>

<div class="title">

Prerequisites

</div>

- You logged into OpenShift Container Platform.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to the project where the service you want to expose is located:

    ``` terminal
    $ oc project <project_name>
    ```

2.  Run the `oc expose service` command to expose the route:

    ``` terminal
    $ oc expose service nodejs-ex
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    route.route.openshift.io/nodejs-ex exposed
    ```

    </div>

3.  To verify that the service is exposed, you can use a tool, such as `curl` to check that the service is accessible from outside the cluster.

    1.  To find the hostname of the route, enter the following command:

        ``` terminal
        $ oc get route
        ```

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        NAME        HOST/PORT                        PATH   SERVICES    PORT       TERMINATION   WILDCARD
        nodejs-ex   nodejs-ex-myproject.example.com         nodejs-ex   8080-tcp                 None
        ```

        </div>

    2.  To check that the host responds to a GET request, enter the following command:

        <div class="formalpara">

        <div class="title">

        Example `curl` command

        </div>

        ``` terminal
        $ curl --head nodejs-ex-myproject.example.com
        ```

        </div>

        <div class="formalpara">

        <div class="title">

        Example output

        </div>

        ``` terminal
        HTTP/1.1 200 OK
        ...
        ```

        </div>

</div>

# Creating a load balancer service

To distribute incoming traffic efficiently and ensure high availability for your applications in OpenShift Container Platform, create a load balancer service.

<div>

<div class="title">

Prerequisites

</div>

- Make sure that the project and service you want to expose exist.

- Your cloud provider supports load balancers.

</div>

<div>

<div class="title">

Procedure

</div>

1.  Log in to OpenShift Container Platform.

2.  Load the project where the service you want to expose is located.

    <div class="formalpara">

    <div class="title">

    Example command

    </div>

    ``` terminal
    $ oc project project1
    ```

    </div>

3.  Open a text file on the control plane node and paste the following text into the file. Edit the file as needed.

    <div class="formalpara">

    <div class="title">

    Sample load balancer configuration file

    </div>

    ``` yaml
    apiVersion: v1
    kind: Service
    metadata:
      name: egress-2
    spec:
      ports:
      - name: db
        port: 3306
      loadBalancerIP:
      loadBalancerSourceRanges:
      - 10.0.0.0/8
      - 192.168.0.0/16
      type: LoadBalancer
      selector:
        name: mysql
    ```

    </div>

    where:

    `metadata.name`
    Specifies a descriptive name for the load balancer service.

    `ports.port`
    Specifies the same port that the service you want to expose is listening on.

    `loadBalancerSourceRanges`
    Specifies a list of specific IP addresses to restrict traffic through the load balancer. The parameter is ignored if the cloud provider does not support the feature.

    `type`
    Specifies `Loadbalancer` as the type.

    `selector.name`
    Specifies the name of the service.

    > [!NOTE]
    > To restrict the traffic through the load balancer to specific IP addresses, use the `spec.endpointPublishingStrategy.loadBalancer.allowedSourceRanges` Ingress Controller parameter. Do not set the `loadBalancerSourceRanges` parameter.

4.  Save and exit the file.

5.  Run the following command to create the service:

    ``` terminal
    $ oc create -f <file_name>
    ```

    For example:

    ``` terminal
    $ oc create -f mysql-lb.yaml
    ```

6.  Execute the following command to view the new service:

    ``` terminal
    $ oc get svc
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    NAME       TYPE           CLUSTER-IP      EXTERNAL-IP                             PORT(S)          AGE
    egress-2   LoadBalancer   172.30.22.226   ad42f5d8b303045-487804948.example.com   3306:30357/TCP   15m
    ```

    </div>

    The service has an external IP address automatically assigned if there is a cloud provider enabled.

7.  On the master, use a tool, such as `curl`, to make sure you can reach the service by using the public IP address:

    ``` terminal
    $ curl <public_ip>:<port>
    ```

    For example:

    ``` terminal
    $ curl 172.29.121.74:3306
    ```

    The examples in this section use a MySQL service, which requires a client application. If you get a string of characters with the `Got packets out of order` message, you are connecting with the service:

    If you have a MySQL client, log in with the standard CLI command:

    ``` terminal
    $ mysql -h 172.30.131.89 -u admin -p
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    Enter password:
    Welcome to the MariaDB monitor.  Commands end with ; or \g.

    MySQL [(none)]>
    ```

    </div>

</div>
