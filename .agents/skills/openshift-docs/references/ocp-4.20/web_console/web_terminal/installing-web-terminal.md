<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can install the web terminal by using the Web Terminal Operator listed in the OpenShift Container Platform software catalog. When you install the Web Terminal Operator, the custom resource definitions (CRDs) that are required for the command line configuration, such as the `DevWorkspace` CRD, are automatically installed. The web console creates the required resources when you open the web terminal.

# Prerequisites

- You are logged into the OpenShift Container Platform web console.

- You have cluster administrator permissions.

# Procedure

1.  In the **Administrator** perspective of the web console, navigate to **Ecosystem** → **Software Catalog**.

2.  Use the **Filter by keyword** box to search for the Web Terminal Operator in the catalog, and then click the **Web Terminal** tile.

3.  Read the brief description about the Operator on the **Web Terminal** page, and then click **Install**.

4.  On the **Install Operator** page, retain the default values for all fields.

    - The **fast** option in the **Update Channel** menu enables installation of the latest release of the Web Terminal Operator.

    - The **All namespaces on the cluster** option in the **Installation Mode** menu enables the Operator to watch and be available to all namespaces in the cluster.

    - The **openshift-operators** option in the **Installed Namespace** menu installs the Operator in the default `openshift-operators` namespace.

    - The **Automatic** option in the **Approval Strategy** menu ensures that the future upgrades to the Operator are handled automatically by the Operator Lifecycle Manager.

5.  Click **Install**.

6.  In the **Installed Operators** page, click the **View Operator** to verify that the Operator is listed on the **Installed Operators** page.

    > [!NOTE]
    > The Web Terminal Operator installs the DevWorkspace Operator as a dependency.

7.  After the Operator is installed, refresh your page to see the command-line terminal icon (![odc wto icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAbCAYAAABiFp9rAAAABHNCSVQICAgIfAhkiAAAAwVJREFUSIm9lstu5EQUhr9y+Va2Jz2dSYOQmC0wPADKSFzEJSIzIwGvgBDvgAQL3gMhHgExghWIPTPsIw3bCZBF0m23u90uu6pYJHRwuqcvgPLvyj7lz+eqIwaDgeMa5F0HBMDf1FD6Pr70kVICYK2lNS1t0/x3kOdJVKJQSUYYRkjp4XkeILDWYq1Ba82smjApS6y124Nipej1+qgkJQgDhPAQQizYWWtpsxtkN6aMhkOq6WRzUJpm3Ly1h1IJnrcccOm1RxCG+EGA7wfkozOKPF8PUknK7t4ApRKEt1mtCCEQQqCSFE9KrHWU46L7Q/88RHFMv3+LeAvIVWAUxfR394ii+NkglaQkWXaR8HPdv3fIm2+8joq7F1fBYqXo9XeBy5DPvxjHiizb6UAAxuMxDx7c4+7dfcIw3BwWK6I4mj+TaZp+CRdV1u/P++RvHR//jnOWjz78gKIY8+fJCcaYtSCAttHMZlXXI98/r5qrMsbw408/c3R0xKeffMzt2y9u5FUQBMQqmZ99OC9RKZe3lJSSd95+i1fv3OGrr7/h6dPjhfA653BucWQKIfA8D2vtetD+/mvcPzzk4fc/8MujR2RZxisvv4TvX9oX4zFPnvy2BOR1QdY5rFse995Oj2+/e8jjx79S1zXvH7zHwcG7RNFlos9Oh3z2+RdLbjvshadiMBg4IQS9/i7PPf/CyimwjZxzFPmIkz+Occ6dF4NzDtO2K4fitrLW0jTNPHfzrLZtQ6P1/wZqG90ZsHOQrmumk9WjflNZa6nrmvqihzogYwxlOWZWVUtLdVM552i0pshHncbuNMSsqshHQxqt/xXMOYcxhqLImU7Kzjuva2iZlAXD4Sl6S5hzjrZtyUdnjIanC3cXutQYM3d7Z+cmKkkW5t8yyHQ6YZznjIscaxd7cuk4sMZQFjmN1iRpShwrwihCXllOjGnRWlPPKiZlSTWdAsuj8MydwTnHrJpSzyqCICQIQ6SU8zlnrcNYQ6s1Wtdrw7x23XLOoXWN1vU605W6tgXyL7dibW7uBvzsAAAAAElFTkSuQmCC)) in the masthead of the console.

    > [!NOTE]
    > If you install the Web Terminal Operator manually by creating a `Subscription` resource, you must name the `Subscription` `web-terminal`. If you do not name it `web-terminal`, the terminal icon does not appear in the console masthead.
