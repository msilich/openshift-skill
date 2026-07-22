<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can launch an embedded command-line terminal instance in the web console. This terminal instance is preinstalled with common CLI tools for interacting with the cluster, such as `oc`, `kubectl`,`odo`, `kn`, `tkn`, `helm`, and `subctl`. It also has the context of the project you are working on and automatically logs you in using your credentials.

# Accessing the web terminal

After the Web Terminal Operator is installed, you can access the web terminal. After the web terminal is initialized, you can use the preinstalled CLI tools like `oc`, `kubectl`, `odo`, `kn`, `tkn`, `helm`, and `subctl` in the web terminal. You can re-run commands by selecting them from the list of commands you have run in the terminal. These commands persist across multiple terminal sessions. The web terminal remains open until you close it or until you close the browser window or tab.

<div>

<div class="title">

Prerequisites

</div>

- You have access to an OpenShift Container Platform cluster and are logged into the web console.

- The Web Terminal Operator is installed on your cluster.

</div>

<div>

<div class="title">

Procedure

</div>

1.  To launch the web terminal, click the command-line terminal icon (![odc wto icon](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAABoAAAAbCAYAAABiFp9rAAAABHNCSVQICAgIfAhkiAAAAwVJREFUSIm9lstu5EQUhr9y+Va2Jz2dSYOQmC0wPADKSFzEJSIzIwGvgBDvgAQL3gMhHgExghWIPTPsIw3bCZBF0m23u90uu6pYJHRwuqcvgPLvyj7lz+eqIwaDgeMa5F0HBMDf1FD6Pr70kVICYK2lNS1t0/x3kOdJVKJQSUYYRkjp4XkeILDWYq1Ba82smjApS6y124Nipej1+qgkJQgDhPAQQizYWWtpsxtkN6aMhkOq6WRzUJpm3Ly1h1IJnrcccOm1RxCG+EGA7wfkozOKPF8PUknK7t4ApRKEt1mtCCEQQqCSFE9KrHWU46L7Q/88RHFMv3+LeAvIVWAUxfR394ii+NkglaQkWXaR8HPdv3fIm2+8joq7F1fBYqXo9XeBy5DPvxjHiizb6UAAxuMxDx7c4+7dfcIw3BwWK6I4mj+TaZp+CRdV1u/P++RvHR//jnOWjz78gKIY8+fJCcaYtSCAttHMZlXXI98/r5qrMsbw408/c3R0xKeffMzt2y9u5FUQBMQqmZ99OC9RKZe3lJSSd95+i1fv3OGrr7/h6dPjhfA653BucWQKIfA8D2vtetD+/mvcPzzk4fc/8MujR2RZxisvv4TvX9oX4zFPnvy2BOR1QdY5rFse995Oj2+/e8jjx79S1zXvH7zHwcG7RNFlos9Oh3z2+RdLbjvshadiMBg4IQS9/i7PPf/CyimwjZxzFPmIkz+Occ6dF4NzDtO2K4fitrLW0jTNPHfzrLZtQ6P1/wZqG90ZsHOQrmumk9WjflNZa6nrmvqihzogYwxlOWZWVUtLdVM552i0pshHncbuNMSsqshHQxqt/xXMOYcxhqLImU7Kzjuva2iZlAXD4Sl6S5hzjrZtyUdnjIanC3cXutQYM3d7Z+cmKkkW5t8yyHQ6YZznjIscaxd7cuk4sMZQFjmN1iRpShwrwihCXllOjGnRWlPPKiZlSTWdAsuj8MydwTnHrJpSzyqCICQIQ6SU8zlnrcNYQ6s1Wtdrw7x23XLOoXWN1vU605W6tgXyL7dibW7uBvzsAAAAAElFTkSuQmCC)) in the masthead of the console. A web terminal instance is displayed in the **Command line terminal** pane. This instance is automatically logged in with your credentials.

2.  If a project has not been selected in the current session, select the project where the `DevWorkspace` CR must be created from the **Project** drop-down list. By default, the current project is selected.

    <div class="note">

    <div class="title">

    </div>

    - One `DevWorkspace` CR defines the web terminal of one user. This CR contains details about the user’s web terminal status and container image components.

    - The `DevWorkspace` CR is created only if it does not already exist.

    - The `openshift-terminal` project is the default project used for cluster administrators. They do not have the option to choose another project. The Web Terminal Operator installs the DevWorkspace Operator as a dependency.

    </div>

3.  Optional: Set the web terminal timeout for the current session:

    1.  Click Timeout.

    2.  In the field that appears, enter the timeout value.

    3.  From the drop-down list, select a timeout interval of **Seconds**, **Minutes**, **Hours**, or **Milliseconds**.

4.  Optional: Select a custom image for the web terminal to use.

    1.  Click Image.

    2.  In the field that appears, enter the URL of the image that you want to use.

5.  Click **Start** to initialize the web terminal using the selected project.

6.  Click **+** to open multiple tabs within the web terminal in the console.

</div>
