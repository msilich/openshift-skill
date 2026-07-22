<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

While the Compliance Operator comes with ready-to-use profiles, they must be modified to fit the organizations’ needs and requirements. The process of modifying a profile is called *tailoring*.

The Compliance Operator provides the `TailoredProfile` object to help tailor profiles.

# Creating a new tailored profile

You can write a tailored profile from scratch by using the `TailoredProfile` object. Set an appropriate `title` and `description` and leave the `extends` field empty. Indicate to the Compliance Operator what type of scan this custom profile will generate:

- Node scan: Scans the Operating System.

- Platform scan: Scans the OpenShift Container Platform configuration.

<div>

<div class="title">

Procedure

</div>

- Set the following annotation on the `TailoredProfile` object:

</div>

<div class="formalpara">

<div class="title">

Example `new-profile.yaml`

</div>

``` yaml
apiVersion: compliance.openshift.io/v1alpha1
kind: TailoredProfile
metadata:
  name: new-profile
  annotations:
    compliance.openshift.io/product-type: Node
spec:
  extends: ocp4-cis-node
  description: My custom profile
  title: Custom profile
  enableRules:
    - name: ocp4-etcd-unique-ca
      rationale: We really need to enable this
  disableRules:
    - name: ocp4-file-groupowner-cni-conf
      rationale: This does not apply to the cluster
```

</div>

- Set `Node` or `Platform` accordingly.

- The `extends` field is optional.

- Use the `description` field to describe the function of the new `TailoredProfile` object.

- Give your `TailoredProfile` object a title with the `title` field.

  > [!NOTE]
  > Adding the `-node` suffix to the `name` field of the `TailoredProfile` object is similar to adding the `Node` product type annotation and generates an Operating System scan.

# Using tailored profiles to extend existing ProfileBundles

While the `TailoredProfile` CR enables the most common tailoring operations, the XCCDF standard allows even more flexibility in tailoring OpenSCAP profiles. In addition, if your organization has been using OpenScap previously, you may have an existing XCCDF tailoring file and can reuse it.

The `ComplianceSuite` object contains an optional `TailoringConfigMap` attribute that you can point to a custom tailoring file. The value of the `TailoringConfigMap` attribute is a name of a config map, which must contain a key called `tailoring.xml` and the value of this key is the tailoring contents.

<div>

<div class="title">

Procedure

</div>

1.  Browse the available rules for the Red Hat Enterprise Linux CoreOS (RHCOS) `ProfileBundle`:

    ``` terminal
    $ oc get rules.compliance -n openshift-compliance -l compliance.openshift.io/profile-bundle=rhcos4
    ```

2.  Browse the available variables in the same `ProfileBundle`:

    ``` terminal
    $ oc get variables.compliance -n openshift-compliance -l compliance.openshift.io/profile-bundle=rhcos4
    ```

3.  Create a tailored profile named `nist-moderate-modified`:

    1.  Choose which rules you want to add to the `nist-moderate-modified` tailored profile. This example extends the `rhcos4-moderate` profile by disabling two rules and changing one value. Use the `rationale` value to describe why these changes were made:

        <div class="formalpara">

        <div class="title">

        Example `new-profile-node.yaml`

        </div>

        ``` yaml
        apiVersion: compliance.openshift.io/v1alpha1
        kind: TailoredProfile
        metadata:
          name: nist-moderate-modified
        spec:
          extends: rhcos4-moderate
          description: NIST moderate profile
          title: My modified NIST moderate profile
          disableRules:
          - name: rhcos4-file-permissions-var-log-messages
            rationale: The file contains logs of error messages in the system
          - name: rhcos4-account-disable-post-pw-expiration
            rationale: No need to check this as it comes from the IdP
          setValues:
          - name: rhcos4-var-selinux-state
            rationale: Organizational requirements
            value: permissive
        ```

        </div>

        | Attribute | Description |
        |----|----|
        | `extends` | Name of the `Profile` object upon which this `TailoredProfile` is built. |
        | `title` | Human-readable title of the `TailoredProfile`. |
        | `disableRules` | A list of name and rationale pairs. Each name refers to a name of a rule object that is to be disabled. The rationale value is human-readable text describing why the rule is disabled. |
        | `manualRules` | A list of name and rationale pairs. When a manual rule is added, the check result status will always be `manual` and remediation will not be generated. This attribute is automatic and by default has no values when set as a manual rule. |
        | `enableRules` | A list of name and rationale pairs. Each name refers to a name of a rule object that is to be enabled. The rationale value is human-readable text describing why the rule is enabled. |
        | `description` | Human-readable text describing the `TailoredProfile`. |
        | `setValues` | A list of name, rationale, and value groupings. Each name refers to a name of the value set. The rationale is human-readable text describing the set. The value is the actual setting. |

        Attributes for spec variables

    2.  Add the `tailoredProfile.spec.manualRules` attribute:

        <div class="formalpara">

        <div class="title">

        Example `tailoredProfile.spec.manualRules.yaml`

        </div>

        ``` yaml
        apiVersion: compliance.openshift.io/v1alpha1
        kind: TailoredProfile
        metadata:
          name: ocp4-manual-scc-check
        spec:
          extends: ocp4-cis
          description: This profile extends ocp4-cis by forcing the SCC check to always return MANUAL
          title: OCP4 CIS profile with manual SCC check
          manualRules:
            - name: ocp4-scc-limit-container-allowed-capabilities
              rationale: We use third party software that installs its own SCC with extra privileges
        ```

        </div>

    3.  Create the `TailoredProfile` object:

        ``` terminal
        $ oc create -n openshift-compliance -f new-profile-node.yaml
        ```

        - The `TailoredProfile` object is created in the default `openshift-compliance` namespace.

          <div class="formalpara">

          <div class="title">

          Example output

          </div>

          ``` terminal
          tailoredprofile.compliance.openshift.io/nist-moderate-modified created
          ```

          </div>

4.  Define the `ScanSettingBinding` object to bind the new `nist-moderate-modified` tailored profile to the default `ScanSetting` object.

    <div class="formalpara">

    <div class="title">

    Example `new-scansettingbinding.yaml`

    </div>

    ``` yaml
    apiVersion: compliance.openshift.io/v1alpha1
    kind: ScanSettingBinding
    metadata:
      name: nist-moderate-modified
    profiles:
      - apiGroup: compliance.openshift.io/v1alpha1
        kind: Profile
        name: ocp4-moderate
      - apiGroup: compliance.openshift.io/v1alpha1
        kind: TailoredProfile
        name: nist-moderate-modified
    settingsRef:
      apiGroup: compliance.openshift.io/v1alpha1
      kind: ScanSetting
      name: default
    ```

    </div>

5.  Create the `ScanSettingBinding` object:

    ``` terminal
    $ oc create -n openshift-compliance -f new-scansettingbinding.yaml
    ```

    <div class="formalpara">

    <div class="title">

    Example output

    </div>

    ``` terminal
    scansettingbinding.compliance.openshift.io/nist-moderate-modified created
    ```

    </div>

</div>
