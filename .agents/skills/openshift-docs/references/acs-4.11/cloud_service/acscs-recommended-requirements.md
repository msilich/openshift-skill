<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The recommended resource guidelines result from internal Red Hat testing processes that created the following objects across a given number of namespaces:

- 10 deployments, with 3 pod replicas in a sleep state, mounting 4 secrets, 4 config maps

- 10 services, each one pointing to the TCP/8080 and TCP/8443 ports of one of the previous deployments

- 1 route pointing to the first of the previous services

- 10 secrets containing 2048 random string characters

- 10 config maps containing 2048 random string characters

An analysis of results identified the number of deployments as a primary factor for increased usage of resources. Therefore, the number of deployments was used as the primary factor for the estimation of required resources.

<div>

<div class="title">

Additional resources

</div>

- [Default resource requirements](acscs-default-requirements.md#acs-cloud-requirements_acscs-default-requirements)

</div>

<a id="recommended-requirements-secured-cluster-services_acscs-recommended-requirements"></a>

# Secured cluster services

Secured cluster services contain the following components:

- Sensor

- Admission controller

- Collector

  > [!NOTE]
  > Information about the resource requirements for the Collector component is included in the Default resource requirements section.

<a id="recommended-requirements-secured-cluster-services-sensor_acscs-recommended-requirements"></a>

## Sensor

Sensor monitors your Kubernetes and OpenShift Container Platform clusters. These services currently deploy in a single deployment, which handles interactions with the Kubernetes API and coordinates with Collector.

<a id="recommended-requirements-sensor-requirements_acscs-recommended-requirements"></a>

## Memory and CPU requirements

The following table lists the minimum memory and CPU values required to run Sensor on a secured cluster.

| Deployments | CPU     | Memory |
|-------------|---------|--------|
| \< 25,000   | 2 cores | 10 GiB |
| \< 50,000   | 2 cores | 20 GiB |

<a id="recommended-requirements-secured-cluster-services-admission-controller_acscs-recommended-requirements"></a>

## Admission controller

The admission controller prevents users from creating workloads that violate policies that you configure.

<a id="recommended-requirements-admission-controller-requirements_acscs-recommended-requirements"></a>

## Memory and CPU requirements

The following table lists the minimum memory and CPU values required to run the admission controller on a secured cluster.

| Deployments | CPU       | Memory  |
|-------------|-----------|---------|
| \< 25,000   | 0.5 cores | 300 MiB |
| \< 50,000   | 0.5 cores | 600 MiB |
