<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Red Hat Advanced Cluster Security for Kubernetes has audit logging features that you can use to check all the changes made in Red Hat Advanced Cluster Security for Kubernetes. The audit log captures all the `PUT` and `POST` events, which are modifications to Red Hat Advanced Cluster Security for Kubernetes. Use this information to troubleshoot a problem or to keep a record of important events, such as changes to roles and permissions. With audit logging you get a complete picture of all normal and abnormal events that happened on Red Hat Advanced Cluster Security for Kubernetes.

> [!NOTE]
> Audit logging is not enabled by default. You must enable audit logging manually.

> [!WARNING]
> Currently there is no message delivery guarantee for audit log messages.

<a id="enable-audit-log_configure-audit-logging"></a>

# Enabling audit logging

When you enable audit logging, every time there is a modification, Red Hat Advanced Cluster Security for Kubernetes sends an HTTP POST message (in JSON format) to the configured system.

<div>

<div class="title">

Prerequisites

</div>

- Configure Splunk or another webhook receiver to handle Red Hat Advanced Cluster Security for Kubernetes log messages.

- You must have `write` permission enabled on the **Notifiers** resource for your role.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Notifier Integrations** section and select **Generic Webhook** or **Splunk**.

3.  Enter the required information and turn on the **Enable Audit Logging** toggle.

</div>

<a id="sample-audit-log-message_configure-audit-logging"></a>

# Sample audit log message

The log message has the following format:

``` json
{
  "headers": {
    "Accept-Encoding": [
      "gzip"
    ],
    "Content-Length": [
      "586"
    ],
    "Content-Type": [
      "application/json"
    ],
    "User-Agent": [
      "Go-http-client/1.1"
    ]
  },
  "data": {
    "audit": {
      "interaction": "CREATE",
      "method": "UI",
      "request": {
        "endpoint": "/v1/notifiers",
        "method": "POST",
        "source": {
          "requestAddr": "10.131.0.7:58276",
          "xForwardedFor": "8.8.8.8",
        },
        "sourceIp": "8.8.8.8",
        "payload": {
          "@type": "storage.Notifier",
          "enabled": true,
          "generic": {
            "auditLoggingEnabled": true,
            "endpoint": "http://samplewebhookserver.com:8080"
          },
          "id": "b53232ee-b13e-47e0-b077-1e383c84aa07",
          "name": "Webhook",
          "type": "generic",
          "uiEndpoint": "https://localhost:8000"
        }
      },
      "status": "REQUEST_SUCCEEDED",
      "time": "2019-05-28T16:07:05.500171300Z",
      "user": {
        "friendlyName": "John Doe",
        "role": {
          "globalAccess": "READ_WRITE_ACCESS",
          "name": "Admin"
        },
        "username": "john.doe@example.com"
      }
    }
  }
}
```

The source IP address of the request is displayed in the source parameters, which makes it easier for you to investigate audit log requests and identify their origin.

To find the source IP address of a request, RHACS uses the following parameters:

- `xForwardedFor`: The X-Forwarded-For header.

- `requestAddr`: The remote address header.

- `sourceIp`: The IP address of the HTTP request.

> [!IMPORTANT]
> How you find the source IP address depends on how you expose Central externally. You can consider the following options:
>
> - If you expose Central behind a load balancer, for example, if you are running Central on Google Kubernetes Engine (GKE) or Amazon Elastic Kubernetes Service (Amazon EKS) by using the Kubernetes External Load Balancer service type, see "Preserving the client source IP".
>
> - If you expose Central behind an Ingress Controller that forwards requests by using the "X-Forwarded-For header", you do not need to make any configuration changes.
>
> - If you expose Central with a TLS passthrough route, you cannot find the source IP address of the client. A cluster-internal IP address is displayed in the source parameters as the source IP address of the client.

<div>

<div class="title">

Additional resources

</div>

- [Preserving the client source IP](https://kubernetes.io/docs/tasks/access-application-cluster/create-external-load-balancer/#preserving-the-client-source-ip)

- [X-Forwarded-For header](https://datatracker.ietf.org/doc/html/rfc7239#section-5.2)

</div>
