<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To modify the default assemble and run script behavior in OpenShift Container Platform, you can customize source-to-image (S2I) builder images. You can adapt S2I builders to meet your specific application requirements when the default scripts are not suitable.

# Invoking scripts embedded in an image

To extend builder image behavior while preserving supported script logic and upgrade compatibility in OpenShift Container Platform, you can start embedded S2I image scripts by creating wrapper scripts. These wrapper scripts run custom logic and then call the default scripts from the image.

<div>

<div class="title">

Procedure

</div>

1.  Inspect the value of the `io.openshift.s2i.scripts-url` label to determine the location of the scripts inside of the builder image:

    ``` terminal
    $ podman inspect --format='{{ index .Config.Labels "io.openshift.s2i.scripts-url" }}' wildfly/wildfly-centos7
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    image:///usr/libexec/s2i
    ```

    </div>

2.  Create a script that includes an invocation of one of the standard scripts wrapped in other commands:

    <div class="formalpara">

    <div class="title">

    `.s2i/bin/assemble` script

    </div>

    ``` bash
    #!/bin/bash
    echo "Before assembling"

    /usr/libexec/s2i/assemble
    rc=$?

    if [ $rc -eq 0 ]; then
        echo "After successful assembling"
    else
        echo "After failed assembling"
    fi

    exit $rc
    ```

    </div>

    This example shows a custom assemble script that prints the message, runs the standard assemble script from the image, and prints another message depending on the exit code of the assemble script.

    > [!IMPORTANT]
    > When wrapping the run script, you must use `exec` for invoking it to ensure signals are handled properly. The use of `exec` also precludes the ability to run additional commands after invoking the default image run script.

    <div class="formalpara">

    <div class="title">

    `.s2i/bin/run` script

    </div>

    ``` bash
    #!/bin/bash
    echo "Before running application"
    exec /usr/libexec/s2i/run
    ```

    </div>

</div>
