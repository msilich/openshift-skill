> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/extend-proc_creating_a_telemetry_server). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Create a telemetry server

Create a server that receives telemetry events from the OpenShift Dev Spaces telemetry plugin and writes them to standard output. For production, consider integrating with a third-party telemetry system such as Segment or Woopra.

## Before you begin

- You have a running instance of Red Hat OpenShift Dev Spaces.

## Procedure

1.  Create a `main.go` file for a Go application that starts a server on port `8080` and writes events to standard output:

    ``` plaintext
    package main

    import (
    	"io/ioutil"
    	"net/http"

    	"go.uber.org/zap"
    )

    var logger *zap.SugaredLogger

    func event(w http.ResponseWriter, req *http.Request) {
    	switch req.Method {
    	case "GET":
    		logger.Info("GET /event")
    	case "POST":
    		logger.Info("POST /event")
    	}
    	body, err := req.GetBody()
    	if err != nil {
    		logger.With("err", err).Info("error getting body")
    		return
    	}
    	responseBody, err := ioutil.ReadAll(body)
    	if err != nil {
    		logger.With("error", err).Info("error reading response body")
    		return
    	}
    	logger.With("body", string(responseBody)).Info("got event")
    }

    func activity(w http.ResponseWriter, req *http.Request) {
    	switch req.Method {
    	case "GET":
    		logger.Info("GET /activity, doing nothing")
    	case "POST":
    		logger.Info("POST /activity")
    		body, err := req.GetBody()
    		if err != nil {
    			logger.With("error", err).Info("error getting body")
    			return
    		}
    		responseBody, err := ioutil.ReadAll(body)
    		if err != nil {
    			logger.With("error", err).Info("error reading response body")
    			return
    		}
    		logger.With("body", string(responseBody)).Info("got activity")
    	}
    }

    func main() {

    	log, _ := zap.NewProduction()
    	logger = log.Sugar()

    	http.HandleFunc("/event", event)
    	http.HandleFunc("/activity", activity)
    	logger.Info("Added Handlers")

    	logger.Info("Starting to serve")
    	http.ListenAndServe(":8080", nil)
    }
    ```

    The code for the example telemetry server is available in the `telemetry-server-example` repository.

2.  Create a container image based on this code and expose it as a deployment in OpenShift in the `openshift-devspaces` project. Clone the repository and build the container:

    ``` bash
    $ git clone https://github.com/che-incubator/telemetry-server-example
    $ cd telemetry-server-example
    $ podman build -t registry/organization/telemetry-server-example:latest .
    $ podman push registry/organization/telemetry-server-example:latest
    ```

3.  Deploy the telemetry server to OpenShift.

    Both `manifest_with_ingress.yaml` and `manifest_with_route` contain definitions for a Deployment and Service. The former also defines a Kubernetes Ingress, while the latter defines an OpenShift Route.

    In the manifest file, replace the `image` and `host` fields to match the image you pushed, and the public hostname of your OpenShift cluster. Then run:

    ``` bash
    $ oc apply -f manifest_with_[ingress|route].yaml -n openshift-devspaces
    ```

## Results

- Verify that the telemetry server pod is running:

  ``` bash
  oc get pods -n openshift-devspaces -l app=telemetry-server-example
  ```

**Related concepts**  

- [How telemetry plugins work](extend-con_telemetry_plugin_overview.md "A telemetry plugin for OpenShift Dev Spaces collects workspace usage data and sends it to your analytics backend. The plugin extends the AbstractAnalyticsManager class with methods for event handling, activity tracking, and shutdown.")

**Related information**  

- [telemetry-server-example](https://github.com/che-incubator/telemetry-server-example)
- [How server logging works](observe-con_configuring_server_logging.md)
- [What DevWorkspace Operator metrics reveal](observe-con_monitoring_devworkspace_operator.md)
