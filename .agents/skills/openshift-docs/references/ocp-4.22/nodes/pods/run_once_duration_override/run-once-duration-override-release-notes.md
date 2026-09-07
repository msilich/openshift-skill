<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

The Run Once Duration Override Operator sets a maximum active deadline on run-once pods, terminating pods that exceed the configured duration.

To apply the run-once duration override from the Run Once Duration Override Operator to run-once pods, you must enable it on each applicable namespace.

These release notes track the development of the Run Once Duration Override Operator for OpenShift Container Platform.

<div>

<div class="title">

Additional resources

</div>

- [About the Run Once Duration Override Operator](index.md#rodoo-about_run-once-duration-override-about)

</div>

# Run Once Duration Override Operator 1.4.1

Review the features, enhancements, and advisory for the release of Run Once Duration Override Operator 1.4.1.

Issued: 17 June 2026

The following advisory is available for the Run Once Duration Override Operator 1.4.1:

- [RHBA-2026:26526](https://access.redhat.com/errata/RHBA-2026:26526)

## New features and enhancements

- This release of the Run Once Duration Override Operator updates the Kubernetes version to 1.35.

## Bug fixes

- This release of the Run Once Duration Override Operator addresses several Common Vulnerabilities and Exposures (CVEs).

# Run Once Duration Override Operator 1.4.0

Review the features, enhancements, and advisory for the release of Run Once Duration Override Operator 1.4.0.

Issued: 12 February 2026

The following advisory is available for the Run Once Duration Override Operator 1.4.0:

- [RHBA-2026:2649](https://access.redhat.com/errata/RHBA-2026:2649)

## New features and enhancements

- This release of the Run Once Duration Override Operator updates the Kubernetes version to 1.34.

- Users should set `.spec.managementState: Managed` in Run Once Duration Override Operator 1.4.0 custom resources (CR). In a future release, the `spec.managementState` field in the Run Once Duration Override Operator CR will be required to be set to `Managed`.

## Bug fixes

- This release of the Run Once Duration Override Operator addresses several Common Vulnerabilities and Exposures (CVEs).
