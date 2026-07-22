<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Because OpenShift Container Platform is a certified Kubernetes distribution, you can use the Kubernetes CLI (`kubectl`) that ships with OpenShift Container Platform to interact with your cluster. You can also gain extended functionality specific to OpenShift Container Platform by using the OpenShift CLI (`oc`) binary.

# The oc binary

The OpenShift CLI (`oc`) binary offers the same capabilities as the `kubectl` binary, but it extends to natively support additional OpenShift Container Platform features.

Full support for OpenShift Container Platform resources
Resources such as `DeploymentConfig`, `BuildConfig`, `Route`, `ImageStream`, and `ImageStreamTag` objects are specific to OpenShift Container Platform distributions, and build upon standard Kubernetes primitives.

Authentication
The `oc` binary offers a built-in `login` command for authentication and lets you work with projects, which map Kubernetes namespaces to authenticated users. Read "Understanding authentication" for more information.

Additional commands
The additional command `oc new-app`, for example, makes it easier to get new applications started using existing source code or pre-built images. Similarly, the additional command `oc new-project` makes it easier to start a project that you can switch to as your default.

> [!IMPORTANT]
> If you installed an earlier version of the `oc` binary, you cannot use it to complete all of the commands in OpenShift Container Platform 4.17 . If you want the latest features, you must download and install the latest version of the `oc` binary corresponding to your OpenShift Container Platform server version.

Non-security API changes will involve, at minimum, two minor releases (4.1 to 4.2 to 4.3, for example) to allow older `oc` binaries to update. Using new capabilities might require newer `oc` binaries. A 4.3 server might have additional capabilities that a 4.2 `oc` binary cannot use and a 4.3 `oc` binary might have additional capabilities that are unsupported by a 4.2 server.

|  |  |  |
|----|----|----|
|  | **X.Y** (`oc` Client) | **X.Y+N** [^1] (`oc` Client) |
| **X.Y** (Server) | ![Red circle 1](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi0d3YBVmQAAAeFJREFUOMu91b9LG2Ecx/H3XWx+XCJEShexQsyQtkEu2EmHI1s7FncjTo27Q/+Dkq1ORhAXCehk8S8IBwZzU0QIVtAcpZuCQu6xpq13HUpSmtwl1zT24Kbnntd9+D58n6/kOI7DAz1jfVfv77k5OEBUq9zWatzWaiBJKJnMr3dujonFRQgEXLdLXslbFxc0lpYQlUrf/0cXFkjs7BCamelZk902XG1tUVfVgTCAqFSoqypX29uDk18Wi3xeXR2qxtMbGzzJ593x1vk5dVXFFmIoXI5GeXF8TCiZ7CqLbdPI5TzhsVfvSV07vLzeZyLkjttC0FheBtv+ExeG4VHjEJG3+zz7+I5YfHB6cXiIMIwu/OjI/etUnukPr6Fc5Mb0V5621cEtL/xTETOb5fTNLt991t7qxj2T06JVrfLjLw62J7l9dzeytm9bHVzJZEaGt63/g0dGiLetTofaQnA6P8/Xk5N/gsPpNM8NA1lRfieXo1ESpRJSMDg0LAWDJPf2kBWl91aMzM4yVSgMjU8VCoTT6f73+eXmJl/W1rAtyxcaiMd5ur7O41zO37D4ZpqYKys0y+W+8Hg2S6JU4tHkpP9J1OnPszOauk5T17F0HRyHmKYxrmnENI1wKuV9Bg85oH8CT8DJrJGjGicAAAAASUVORK5CYII=) | ![Red circle 3](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi4fGKNndgAAAoBJREFUOMu1lT9ME1Ecxz9toRw9CIgiDQLyZ2i1wWtwKQxNR0fCogsFNtgYGBgZ7aRMlIQQCOnARliEiaYJTdvFIySIJEAxakogCtKDVuydg1IEeqWp4ZK33Pu+z/u97/u938+gaZrGHX0leWczGY4WF1GiUU5lmVNZBoMBi9P5Z3R0cK+nB0ymnMsNepGnd3bY7e1FCYfz7i92ddEyN0dZa+uNOWOuBYdTU2xI0q1gACUcZkOSOJyevj3yA7+fT0NDRXncNDFB7eBgbnh6e5sNSUJVlKLgRlHk6doaZW1t12xRVXa93htgk9RH07v3PPt+xnPtDOnDCk0vbRhywFVFYbevD1T1KlyJxXJ6rAp2RJeV88gC3xZktGYPtTNvqanTuYPVVZRY7GoqKpFITrEWHWOreYzMcRqo4sFKgsceKyXVwL7OBpEIost1CU/qwCFNJlWH2Wal1P6KGrvAr+AMRx/1vU9GIjwsJHIAg+c19qV+SgE1vsCX0RnS+dLzLyvruZpK6Yo12c9efz97o34UoZvGYJBHkj78gpWFW5xOffV+lOPZWQ59wySWEiA4EV1VuvILVsm/P34sL1+TlVHxJkijM0EqnkAVnFR2W4FNFPm4cHh5zsjTnMubqN0vqHZZMZLiPL7E/tgwX6P6B71gZV+oqihsdnZytr7+X2VWcDh4EothtFguPTeKIi2BAAazuWiwwWymbX4eo8VysyqWt7fT4PMVDW/w+RAcjvz1/GByks8jI6jJZEFQU3U1jePj3Pd6C2sWP+Nx4gMDnASDecGVHg8tgQCl9fWFd6JsvmxtcRIKcRIKkQyFQNOocLupdLupcLsRbDb9O7jLBv0bSIsLiZTWWjcAAAAASUVORK5CYII=) |
| **X.Y+N** (Server) | ![Red circle 2](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi4QiBx65wAAAmhJREFUOMu11T9IG1EcwPFvoiYxF6nSWor4L8YSbZA77FIdQsZ2qrjUxaibTrUgdHU0U+ukgohFAmYyddGtGjBophOpiFVj/0BbtKCY00s1lw5tUqp3iaT44Kb33ud+7/d4v58pnU6nuaFRnHM2leJofh5lbY1TWeZUlsFkwi5Jv7/WVio6O6GoSHe7ySjy5N4e8e5ulGg05/+F9nacMzNYGxquzJn1NhxOTrIpinlhACUaZVMUOZyayh/5wfg4nwYGCspx7dgYlf39+nhyd5dNUURTlIJwsyDwYH0dq8t1KS2aRtzvvwpb3VS8mqP56xkP02eI8XfUPq3TxTVFId7TA5r2L67EYro5Lu4YoWawA4sqc7wok7rno3J2mjt1BnewsoISi13CV1d1F1+Eetnt8PHe2cbOEx+fw0dga0Kotxpf8h8riycMcDhGebvMBYC1CYdUDuoWylbSEE9cxhVDPDNu4RiZ5m6Tijo+zI/v5I08+0I1Vc0JCy8XcQ1KnId72XmxTK6akbGykdslyWCpldLnYRpHJFLhXj50vSGZ54wZKy9u6Znl/msfxeo3zm1d1IQXaFyYo/ZZXV48m5ZSXdyK5ZFECYCtHsfj+uyMKg9D6KMunrGyL1RTFLba2jjb2PivMmvzeGiOxTDb7X/TYhYEnMEgJoulYNhkseAKhTDb7VerYmlLC9WBQMF4dSCAzePJXc8PJib4MjSElkhcCy0qL6dmdJTbfv/1msXP/X32+/o4WVrKCZf5fDiDQUqqqq7fibJleHubk0iEk0iERCQC6TQOr5cyrxeH14vN7Ta+g5ts0L8Ax+z488wl6EkAAAAASUVORK5CYII=) | ![Red circle 1](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi0d3YBVmQAAAeFJREFUOMu91b9LG2Ecx/H3XWx+XCJEShexQsyQtkEu2EmHI1s7FncjTo27Q/+Dkq1ORhAXCehk8S8IBwZzU0QIVtAcpZuCQu6xpq13HUpSmtwl1zT24Kbnntd9+D58n6/kOI7DAz1jfVfv77k5OEBUq9zWatzWaiBJKJnMr3dujonFRQgEXLdLXslbFxc0lpYQlUrf/0cXFkjs7BCamelZk902XG1tUVfVgTCAqFSoqypX29uDk18Wi3xeXR2qxtMbGzzJ593x1vk5dVXFFmIoXI5GeXF8TCiZ7CqLbdPI5TzhsVfvSV07vLzeZyLkjttC0FheBtv+ExeG4VHjEJG3+zz7+I5YfHB6cXiIMIwu/OjI/etUnukPr6Fc5Mb0V5621cEtL/xTETOb5fTNLt991t7qxj2T06JVrfLjLw62J7l9dzeytm9bHVzJZEaGt63/g0dGiLetTofaQnA6P8/Xk5N/gsPpNM8NA1lRfieXo1ESpRJSMDg0LAWDJPf2kBWl91aMzM4yVSgMjU8VCoTT6f73+eXmJl/W1rAtyxcaiMd5ur7O41zO37D4ZpqYKys0y+W+8Hg2S6JU4tHkpP9J1OnPszOauk5T17F0HRyHmKYxrmnENI1wKuV9Bg85oH8CT8DJrJGjGicAAAAASUVORK5CYII=) |

Compatibility matrix

![Red circle 1](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi0d3YBVmQAAAeFJREFUOMu91b9LG2Ecx/H3XWx+XCJEShexQsyQtkEu2EmHI1s7FncjTo27Q/+Dkq1ORhAXCehk8S8IBwZzU0QIVtAcpZuCQu6xpq13HUpSmtwl1zT24Kbnntd9+D58n6/kOI7DAz1jfVfv77k5OEBUq9zWatzWaiBJKJnMr3dujonFRQgEXLdLXslbFxc0lpYQlUrf/0cXFkjs7BCamelZk902XG1tUVfVgTCAqFSoqypX29uDk18Wi3xeXR2qxtMbGzzJ593x1vk5dVXFFmIoXI5GeXF8TCiZ7CqLbdPI5TzhsVfvSV07vLzeZyLkjttC0FheBtv+ExeG4VHjEJG3+zz7+I5YfHB6cXiIMIwu/OjI/etUnukPr6Fc5Mb0V5621cEtL/xTETOb5fTNLt991t7qxj2T06JVrfLjLw62J7l9dzeytm9bHVzJZEaGt63/g0dGiLetTofaQnA6P8/Xk5N/gsPpNM8NA1lRfieXo1ESpRJSMDg0LAWDJPf2kBWl91aMzM4yVSgMjU8VCoTT6f73+eXmJl/W1rAtyxcaiMd5ur7O41zO37D4ZpqYKys0y+W+8Hg2S6JU4tHkpP9J1OnPszOauk5T17F0HRyHmKYxrmnENI1wKuV9Bg85oH8CT8DJrJGjGicAAAAASUVORK5CYII=) Fully compatible.

![Red circle 2](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi4QiBx65wAAAmhJREFUOMu11T9IG1EcwPFvoiYxF6nSWor4L8YSbZA77FIdQsZ2qrjUxaibTrUgdHU0U+ukgohFAmYyddGtGjBophOpiFVj/0BbtKCY00s1lw5tUqp3iaT44Kb33ud+7/d4v58pnU6nuaFRnHM2leJofh5lbY1TWeZUlsFkwi5Jv7/WVio6O6GoSHe7ySjy5N4e8e5ulGg05/+F9nacMzNYGxquzJn1NhxOTrIpinlhACUaZVMUOZyayh/5wfg4nwYGCspx7dgYlf39+nhyd5dNUURTlIJwsyDwYH0dq8t1KS2aRtzvvwpb3VS8mqP56xkP02eI8XfUPq3TxTVFId7TA5r2L67EYro5Lu4YoWawA4sqc7wok7rno3J2mjt1BnewsoISi13CV1d1F1+Eetnt8PHe2cbOEx+fw0dga0Kotxpf8h8riycMcDhGebvMBYC1CYdUDuoWylbSEE9cxhVDPDNu4RiZ5m6Tijo+zI/v5I08+0I1Vc0JCy8XcQ1KnId72XmxTK6akbGykdslyWCpldLnYRpHJFLhXj50vSGZ54wZKy9u6Znl/msfxeo3zm1d1IQXaFyYo/ZZXV48m5ZSXdyK5ZFECYCtHsfj+uyMKg9D6KMunrGyL1RTFLba2jjb2PivMmvzeGiOxTDb7X/TYhYEnMEgJoulYNhkseAKhTDb7VerYmlLC9WBQMF4dSCAzePJXc8PJib4MjSElkhcCy0qL6dmdJTbfv/1msXP/X32+/o4WVrKCZf5fDiDQUqqqq7fibJleHubk0iEk0iERCQC6TQOr5cyrxeH14vN7Ta+g5ts0L8Ax+z488wl6EkAAAAASUVORK5CYII=) `oc` client might not be able to access server features.

![Red circle 3](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABcAAAAWCAYAAAArdgcFAAAABmJLR0QA/wD/AP+gvaeTAAAACXBIWXMAAAsTAAALEwEAmpwYAAAAB3RJTUUH4QcFDi4fGKNndgAAAoBJREFUOMu1lT9ME1Ecxz9toRw9CIgiDQLyZ2i1wWtwKQxNR0fCogsFNtgYGBgZ7aRMlIQQCOnARliEiaYJTdvFIySIJEAxakogCtKDVuydg1IEeqWp4ZK33Pu+z/u97/u938+gaZrGHX0leWczGY4WF1GiUU5lmVNZBoMBi9P5Z3R0cK+nB0ymnMsNepGnd3bY7e1FCYfz7i92ddEyN0dZa+uNOWOuBYdTU2xI0q1gACUcZkOSOJyevj3yA7+fT0NDRXncNDFB7eBgbnh6e5sNSUJVlKLgRlHk6doaZW1t12xRVXa93htgk9RH07v3PPt+xnPtDOnDCk0vbRhywFVFYbevD1T1KlyJxXJ6rAp2RJeV88gC3xZktGYPtTNvqanTuYPVVZRY7GoqKpFITrEWHWOreYzMcRqo4sFKgsceKyXVwL7OBpEIost1CU/qwCFNJlWH2Wal1P6KGrvAr+AMRx/1vU9GIjwsJHIAg+c19qV+SgE1vsCX0RnS+dLzLyvruZpK6Yo12c9efz97o34UoZvGYJBHkj78gpWFW5xOffV+lOPZWQ59wySWEiA4EV1VuvILVsm/P34sL1+TlVHxJkijM0EqnkAVnFR2W4FNFPm4cHh5zsjTnMubqN0vqHZZMZLiPL7E/tgwX6P6B71gZV+oqihsdnZytr7+X2VWcDh4EothtFguPTeKIi2BAAazuWiwwWymbX4eo8VysyqWt7fT4PMVDW/w+RAcjvz1/GByks8jI6jJZEFQU3U1jePj3Pd6C2sWP+Nx4gMDnASDecGVHg8tgQCl9fWFd6JsvmxtcRIKcRIKkQyFQNOocLupdLupcLsRbDb9O7jLBv0bSIsLiZTWWjcAAAAASUVORK5CYII=) `oc` client might provide options and features that might not be compatible with the accessed server.

<div>

<div class="title">

Additional resources

</div>

- [Understanding authentication](../../authentication/understanding-authentication.md#understanding-authentication)

</div>

# The kubectl binary

The Kubernetes CLI (`kubectl`) binary is provided as a means to support existing workflows and scripts for new OpenShift Container Platform users coming from a standard Kubernetes environment, or for those who prefer to use the `kubectl` CLI. Existing users of `kubectl` can continue to use the binary to interact with Kubernetes primitives, with no changes required to the OpenShift Container Platform cluster.

You can install the supported `kubectl` binary by following the steps to install the OpenShift CLI. The `kubectl` binary is included in the archive if you download the binary, or is installed when you install the CLI by using an RPM.

<div>

<div class="title">

Additional resources

</div>

- [kubectl (Kubernetes documentation)](https://kubernetes.io/docs/reference/kubectl/overview/)

- [Getting started with the OpenShift CLI](getting-started-cli.md#cli-getting-started)

</div>

[^1]: Where **N** is a number greater than or equal to 1.
