<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Viewing Argo CD logs helps you troubleshoot GitOps deployments and monitor application synchronization. Use the logging subsystem for Red Hat OpenShift to access and filter Argo CD controller and application logs through the Kibana dashboard. The logging subsystem for Red Hat OpenShift collects logs from all pods in the cluster, including Red Hat OpenShift GitOps components.

# Searching and filtering Argo CD logs

You can use the Kibana dashboard to view, search, and filter Argo CD logs to troubleshoot GitOps deployments and monitor application synchronization.

<div>

<div class="title">

Prerequisites

</div>

- The Red Hat OpenShift GitOps Operator is installed on your OpenShift Container Platform cluster.

- The logging subsystem for Red Hat OpenShift is installed and configured to collect logs on your OpenShift Container Platform cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the OpenShift Container Platform web console, go to the ![red hat applications menu icon](data:image/jpg;base64,/9j/4QCLRXhpZgAATU0AKgAAAAgABgEPAAIAAAAIAAAAVgESAAMAAAABAAEAAAEaAAUAAAABAAAAXgEbAAUAAAABAAAAZgEoAAMAAAABAAIAAAExAAIAAAAVAAAAbgAAAABCZUZ1bmt5AAAAASwAAAABAAABLAAAAAFCZUZ1bmt5IFBob3RvIEVkaXRvcgD/4AAQSkZJRgABAQEBLAEsAAD/2wBDAAEBAQEBAQEBAQEBAQEBAQIBAQEBAQIBAQECAgICAgICAgIDAwQDAwMDAwICAwQDAwQEBAQEAgMFBQQEBQQEBAT/2wBDAQEBAQEBAQIBAQIEAwIDBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAQEBAT/wAARCAAgACADAREAAhEBAxEB/8QAHwAAAQUBAQEBAQEAAAAAAAAAAAECAwQFBgcICQoL/8QAtRAAAgEDAwIEAwUFBAQAAAF9AQIDAAQRBRIhMUEGE1FhByJxFDKBkaEII0KxwRVS0fAkM2JyggkKFhcYGRolJicoKSo0NTY3ODk6Q0RFRkdISUpTVFVWV1hZWmNkZWZnaGlqc3R1dnd4eXqDhIWGh4iJipKTlJWWl5iZmqKjpKWmp6ipqrKztLW2t7i5usLDxMXGx8jJytLT1NXW19jZ2uHi4+Tl5ufo6erx8vP09fb3+Pn6/8QAHwEAAwEBAQEBAQEBAQAAAAAAAAECAwQFBgcICQoL/8QAtREAAgECBAQDBAcFBAQAAQJ3AAECAxEEBSExBhJBUQdhcRMiMoEIFEKRobHBCSMzUvAVYnLRChYkNOEl8RcYGRomJygpKjU2Nzg5OkNERUZHSElKU1RVVldYWVpjZGVmZ2hpanN0dXZ3eHl6goOEhYaHiImKkpOUlZaXmJmaoqOkpaanqKmqsrO0tba3uLm6wsPExcbHyMnK0tPU1dbX2Nna4uPk5ebn6Onq8vP09fb3+Pn6/9oADAMBAAIRAxEAPwD+KegAoAKACgAoA/uU+J37BH/BDLTPjd+xX4f8J/sXftm6d4P+IXiXxTF8TtE1b9nP9rG01Hxxptl4D1fUdPW1trjTxqN7cQalHpl0w8Mq4jhS4kucWo3UAL8MP2CP+CGWqfG79tPw/wCLP2Lv2zdR8IfD3xN4Wi+GOh6T+zn+1jd6j4H0298B6RqOoLdW1vp51GyuJ9Sk1O6UeJlQSQvbyW2bUhqAP4aqACgD/UT+OXhb/goEP2lv+Cc9vrX7V/7GWrazq3xB8by+GrvSf2NfFdjpy3kfws8TSXF/dWLfE6SXVbc2rXkSmzudLWGa+t5nE6AW1AB8DPC3/BQJv2lv+Ci9vov7V/7GWk6zpPxB8ES+JbvVv2NfFd/pzXknws8MyW9/a2A+J0culW4tVs4m+2XOqLNNY3EyCBCbagD/AC7KACgAoAKAD9KAP//Z) menu → **Observability** → **Logging** to view the Kibana dashboard.

2.  Create an index pattern.

    1.  To display all the indices, define the index pattern as `*`, and click **Next step**.

    2.  Select **@timestamp** for **Time Filter field name**.

    3.  Click **Create index pattern**.

3.  In the navigation panel of the Kibana dashboard, click the **Discover** tab.

4.  Create a filter to retrieve logs for Argo CD. The following steps create a filter that retrieves logs for all the pods in the `openshift-gitops` namespace:

    1.  Click **Add a filter +**.

    2.  Select the **kubernetes.namespace_name** field.

    3.  Select the **is** operator.

    4.  Select the **openshift-gitops** value.

    5.  Click **Save**.

5.  Optional: Add additional filters to narrow the search. For example, to retrieve logs for a particular pod, you can create another filter with `kubernetes.pod_name` as the field.

6.  View the filtered Argo CD logs in the Kibana dashboard.

</div>

# Additional resources

- [Installing the logging subsystem for Red Hat OpenShift using the web console](https://docs.redhat.com/en/documentation/openshift_container_platform/latest/html/logging/about-logging)
