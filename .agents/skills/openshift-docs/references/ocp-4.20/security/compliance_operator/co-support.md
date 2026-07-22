<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

# Compliance Operator lifecycle

The Compliance Operator is a "Rolling Stream" Operator, meaning updates are available asynchronously of OpenShift Container Platform releases. For more information, see [OpenShift Operator Life Cycles](https://access.redhat.com/support/policy/updates/openshift_operators) on the Red Hat Customer Portal.

# Getting support

If you experience difficulty with a procedure described in this documentation, or with OpenShift Container Platform in general, visit the [Red Hat Customer Portal](http://access.redhat.com).

From the Customer Portal, you can:

- Search or browse through the Red Hat Knowledgebase of articles and solutions relating to Red Hat products.

- Submit a support case to Red Hat Support.

- Access other product documentation.

To identify issues with your cluster, you can use Red Hat Lightspeed in [OpenShift Cluster Manager](https://console.redhat.com/openshift). Red Hat Lightspeed provides details about issues and, if available, information on how to solve a problem.

If you have a suggestion for improving this documentation or have found an error, submit a [Jira issue](https://issues.redhat.com/secure/CreateIssueDetails!init.jspa?pid=12332330&summary=Documentation_issue&issuetype=1&components=12367614&priority=10200&versions=12385624) for the most relevant documentation component. Please provide specific details, such as the section name and OpenShift Container Platform version.

# Using the must-gather tool for the Compliance Operator

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

- [Product Compliance](https://access.redhat.com/compliance)
