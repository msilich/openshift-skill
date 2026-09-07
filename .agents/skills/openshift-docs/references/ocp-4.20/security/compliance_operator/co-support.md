<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can find support resources for the Compliance Operator, including lifecycle information, general support procedures, and troubleshooting tools.

# Compliance Operator lifecycle

The Compliance Operator is a "Rolling Stream" Operator, meaning updates are available asynchronously of OpenShift Container Platform releases. For more information, see "OpenShift Operator Life Cycles" on the Red Hat Customer Portal.

# Get support

Red Hat offers several support channels to help you troubleshoot issues and get the most from OpenShift Container Platform.

From the Red Hat Customer Portal, you can:

- Search or browse through the Red Hat Knowledgebase of articles and solutions about Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information about how to solve a problem.

To suggest improvements or report errors, give specific details such as the section name and OpenShift Container Platform version.

# Using the must-gather tool for the Compliance Operator

You can collect detailed Compliance Operator configuration and logs by using the must-gather tool to aid in troubleshooting issues and support case resolution.

Starting in Compliance Operator v1.6.0, you can collect data about the Compliance Operator resources by running the `must-gather` command with the Compliance Operator image.

> [!NOTE]
> Consider using the `must-gather` tool when opening support cases or filing bug reports, as it provides additional details about the Operator configuration and logs.

<div>

<div class="title">

Procedure

</div>

- Run the following command to collect data about the Compliance Operator:

  ``` terminal
  $ oc adm must-gather --image=$(oc get csv compliance-operator.v1.6.0 -o=jsonpath='{.spec.relatedImages[?(@.name=="must-gather")].image}')
  ```

</div>

# Additional resources

- [About the must-gather tool](../../support/gathering-cluster-data.md#about-must-gather_gathering-cluster-data)

- [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators)

- [Product Compliance](https://access.redhat.com/compliance)
