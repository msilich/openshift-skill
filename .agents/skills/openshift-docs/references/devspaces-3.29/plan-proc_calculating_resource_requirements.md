> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/plan-proc_calculating_resource_requirements). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Size your cluster for OpenShift Dev Spaces

Size your cluster by calculating the CPU and memory requirements for the OpenShift Dev Spaces Operator, Dev Workspace Controller, and user workspaces so that your cluster can handle the expected number of concurrent users.

## Before you begin

- You have a planned or existing OpenShift Dev Spaces deployment on OpenShift Container Platform 4.16 or later.
- You have the devfiles that define the development environments for your users.
- You have an estimate of the number of concurrent workspaces that your users will run.

## About this task

Note

The following link to an [example devfile](https://github.com/che-incubator/quarkus-api-example/blob/main/devfile.yaml) is a pointer to material from the upstream community. This material represents the very latest available content and the most recent best practices. These tips have not yet been vetted by Red Hat’s QE department, and they have not yet been proven by a wide user group. Please, use this information cautiously. It is best used for educational and 'developmental' purposes rather than 'production' purposes.

## Procedure

1.  Identify the workspace resource requirements from the devfile `components` section. The following example uses the [Quarkus API example devfile](https://github.com/che-incubator/quarkus-api-example/blob/main/devfile.yaml).
    - The `tools` component of the devfile defines the following requests and limits:

      ``` yaml
          memoryLimit: 6G
          memoryRequest: 512M
          cpuRequest: 1000m
          cpuLimit: 4000m
      ```

    - During workspace startup, an internal `che-gateway` container is implicitly provisioned with the following requests and limits:

      ``` yaml
          memoryLimit: 256M
          memoryRequest: 64M
          cpuRequest: 50m
          cpuLimit: 500m
      ```

    - Additional memory and CPU are added implicitly for the Visual Studio Code - Open Source ("Code - OSS") editor:

      ``` yaml
          memoryLimit: 1024M
          memoryRequest: 256M
          cpuRequest: 30m
          cpuLimit: 500m
      ```

    - Additional memory and CPU are added implicitly for a JetBrains IDE, for example IntelliJ IDEA Ultimate:

      ``` yaml
          memoryLimit: 6144M
          memoryRequest: 2048M
          cpuRequest: 1500m
          cpuLimit: 2000m
      ```
2.  Calculate the sums of the resources required for each workspace. If you intend to use multiple devfiles, repeat this calculation for every expected devfile. <span id="proc_calculating-resource-requirements_devspaces__entry__1"></span><span id="proc_calculating-resource-requirements_devspaces__entry__2"></span><span id="proc_calculating-resource-requirements_devspaces__entry__3"></span><span id="proc_calculating-resource-requirements_devspaces__entry__4"></span><span id="proc_calculating-resource-requirements_devspaces__entry__5"></span><span id="proc_calculating-resource-requirements_devspaces__entry__6"></span><span id="proc_calculating-resource-requirements_devspaces__entry__7"></span>
    <table>
    <caption>Table 1. Workspace requirements for the example devfile in the previous step</caption>
    <thead>
    <tr>
    <th>Purpose</th>
    <th>Pod</th>
    <th>Container name</th>
    <th>Memory limit</th>
    <th>Memory request</th>
    <th>CPU limit</th>
    <th>CPU request</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>Developer tools</p></td>
    <td><p><code>workspace</code></p></td>
    <td><p><code>tools</code></p></td>
    <td><p>6 GiB</p></td>
    <td><p>512 MiB</p></td>
    <td><p>4000 m</p></td>
    <td><p>1000 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces gateway</p></td>
    <td><p><code>workspace</code></p></td>
    <td><p><code>che-gateway</code></p></td>
    <td><p>256 MiB</p></td>
    <td><p>64 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>50 m</p></td>
    </tr>
    <tr>
    <td><p>Visual Studio Code</p></td>
    <td><p><code>workspace</code></p></td>
    <td><p><code>tools</code></p></td>
    <td><p>1024 MiB</p></td>
    <td><p>256 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>30 m</p></td>
    </tr>
    <tr>
    <td colspan="3"><p><strong>Total</strong></p></td>
    <td><p><strong>7.3 GiB</strong></p></td>
    <td><p><strong>832 MiB</strong></p></td>
    <td><p><strong>5000 m</strong></p></td>
    <td><p><strong>1080 m</strong></p></td>
    </tr>
    </tbody>
    </table>
3.  Multiply the resources calculated per workspace by the number of workspaces that you expect all of your users to run simultaneously.
4.  Calculate the sums of the requirements for the OpenShift Dev Spaces Operator, Operands, and Dev Workspace Controller. <span id="proc_calculating-resource-requirements_devspaces__entry__34"></span><span id="proc_calculating-resource-requirements_devspaces__entry__35"></span><span id="proc_calculating-resource-requirements_devspaces__entry__36"></span><span id="proc_calculating-resource-requirements_devspaces__entry__37"></span><span id="proc_calculating-resource-requirements_devspaces__entry__38"></span><span id="proc_calculating-resource-requirements_devspaces__entry__39"></span><span id="proc_calculating-resource-requirements_devspaces__entry__40"></span>
    <table>
    <caption>Table 2. Default requirements for the OpenShift Dev Spaces Operator, Operands, and Dev Workspace Controller</caption>
    <thead>
    <tr>
    <th>Purpose</th>
    <th>Pod name</th>
    <th>Container names</th>
    <th>Memory limit</th>
    <th>Memory request</th>
    <th>CPU limit</th>
    <th>CPU request</th>
    </tr>
    </thead>
    <tbody>
    <tr>
    <td><p>OpenShift Dev Spaces operator</p></td>
    <td><p><code>devspaces-operator</code></p></td>
    <td><p><code>devspaces-operator</code></p></td>
    <td><p>256 MiB</p></td>
    <td><p>64 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Server</p></td>
    <td><p><code>devspaces</code></p></td>
    <td><p><code>devspaces-server</code></p></td>
    <td><p>1 GiB</p></td>
    <td><p>512 MiB</p></td>
    <td><p>1000 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Dashboard</p></td>
    <td><p><code>devspaces-dashboard</code></p></td>
    <td><p><code>devspaces-dashboard</code></p></td>
    <td><p>256 MiB</p></td>
    <td><p>32 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Gateway</p></td>
    <td><p><code>devspaces-gateway</code></p></td>
    <td><p><code>traefik</code></p></td>
    <td><p>4 GiB</p></td>
    <td><p>128 MiB</p></td>
    <td><p>1000 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Gateway</p></td>
    <td><p><code>devspaces-gateway</code></p></td>
    <td><p><code>configbump</code></p></td>
    <td><p>256 MiB</p></td>
    <td><p>64 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>50 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Gateway</p></td>
    <td><p><code>devspaces-gateway</code></p></td>
    <td><p><code>oauth-proxy</code></p></td>
    <td><p>512 MiB</p></td>
    <td><p>64 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>OpenShift Dev Spaces Gateway</p></td>
    <td><p><code>devspaces-gateway</code></p></td>
    <td><p><code>kube-rbac-proxy</code></p></td>
    <td><p>512 MiB</p></td>
    <td><p>64 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>Plugin registry</p></td>
    <td><p><code>plugin-registry</code></p></td>
    <td><p><code>plugin-registry</code></p></td>
    <td><p>256 MiB</p></td>
    <td><p>32 MiB</p></td>
    <td><p>500 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>Dev Workspace Controller Manager</p></td>
    <td><p><code>devworkspace-controller-manager</code></p></td>
    <td><p><code>devworkspace-controller</code></p></td>
    <td><p>5 GiB</p></td>
    <td><p>100 MiB</p></td>
    <td><p>3000 m</p></td>
    <td><p>250 m</p></td>
    </tr>
    <tr>
    <td><p>Dev Workspace Controller Manager</p></td>
    <td><p><code>devworkspace-controller-manager</code></p></td>
    <td><p><code>kube-rbac-proxy</code></p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    </tr>
    <tr>
    <td><p>Dev Workspace Operator Catalog</p></td>
    <td><p><code>devworkspace-operator-catalog</code></p></td>
    <td><p><code>registry-server</code></p></td>
    <td><p>N/A</p></td>
    <td><p>50 MiB</p></td>
    <td><p>N/A</p></td>
    <td><p>10 m</p></td>
    </tr>
    <tr>
    <td><p>Dev Workspace Webhook Server</p></td>
    <td><p><code>devworkspace-webhook-server</code></p></td>
    <td><p><code>webhook-server</code></p></td>
    <td><p>300 MiB</p></td>
    <td><p>20 MiB</p></td>
    <td><p>200 m</p></td>
    <td><p>100 m</p></td>
    </tr>
    <tr>
    <td><p>Dev Workspace Webhook Server</p></td>
    <td><p><code>devworkspace-webhook-server</code></p></td>
    <td><p><code>kube-rbac-proxy</code></p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    <td><p>N/A</p></td>
    </tr>
    <tr>
    <td colspan="3"><p><strong>Total</strong></p></td>
    <td><p><strong>12.3 GiB</strong></p></td>
    <td><p><strong>1.1 GiB</strong></p></td>
    <td><p><strong>8.2</strong></p></td>
    <td><p><strong>1.1</strong></p></td>
    </tr>
    </tbody>
    </table>
5.  Add the workspace resources from step 3 and the operator resources from step 4 to determine total cluster resource requirements.

## Results

- Verify that the total resource requirements account for all OpenShift Dev Spaces Operator components, Dev Workspace Controller components, and the expected number of concurrent workspaces.

**Related information**  

- [What is a devfile](https://devfile.io/docs/2.2.0/what-is-a-devfile)
- [Benefits of devfile](https://devfile.io/docs/2.2.0/benefits-of-devfile)
- [Devfile customization overview](https://devfile.io/docs/2.2.0/overview)
