<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can use Red Hat Advanced Cluster Security for Kubernetes (RHACS) to ensure the integrity of the container images in your clusters by verifying image signatures against pre-configured keys.

<a id="verify-image-signatures-overview_verify-image-signatures"></a>

# Image signature verification overview

You can create policies to block unsigned images and images that do not have a verified signature. You can also enforce the policy by using the RHACS admission controller to stop unauthorized deployment creation.

<div class="note">

<div class="title">

</div>

- RHACS supports Cosign signature verification by using Cosign public keys, Cosign certificates, or both.

- For Cosign signature verification, RHACS supports communication with the transparency log.

- For Cosign signature verification, you can use keyless verification with RHACS. If you want to host the key infrastructure yourself, you can do this by using Red Hat Trusted Artifact Signer (RHTAS).

- You must configure signature integration with at least 1 Cosign verification method for signature verification.

- For all deployed and watched images:

  - RHACS fetches and verifies the signatures every 4 hours.

  - RHACS verifies the signatures whenever you change or update your signature integration verification data.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Overview (Sigstore documentation)](https://docs.sigstore.dev/cosign/signing/overview/)

- [Rekor (Sigstore documentation)](https://docs.sigstore.dev/logging/overview/)

</div>

<a id="securing-container-images-by-using-signature-integration_verify-image-signatures"></a>

# Securing container images by using signature integration

By creating a signature integration, you can ensure that a trusted source signs the container image.

When you create a signature integration, you can use the following verification methods:

- Cosign public keys

- Cosign certificates

You can also enhance signature verification by enabling transparency log validation. The transparency log records the signature in a public log and provides cryptographic proof of its inclusion. You can strengthen verification by adding traceability and increasing trust when you use public keys or certificates.

> [!IMPORTANT]
> You must configure at least one trusted signer. To configure a trusted signer, you must specify a Cosign public encryption key or a Cosign certificate chain. You can combine multiple image signers in a single signature integration.

<div>

<div class="title">

Prerequisites

</div>

- You have a Cosign public key encoded in Privacy Enhanced Mail (PEM) format.

  For more information about Cosign public keys, see the "Overview" topic in the Sigstore documentation.

- You have the certificate identity and issuer.

- Optional: You have a certificate and chain encoded in PEM format.

  For more information about Cosign certificates, see the "Verifying Signatures" topic in the Sigstore documentation.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Signature Integrations** section, and then click **Signature**.

3.  To create a new signature integration, click **New integration**.

4.  Enter a name for the integration.

5.  To add a new public key, complete the following steps:

    <div class="note">

    <div class="title">

    </div>

    - If you add a public key, you do not need to create a new certificate verification.

    - You can add one or more public keys.

    </div>

    1.  Expand **Cosign public Keys**, and then click **Add new public key**.

    2.  Enter a name for the key.

    3.  Enter a value for the key encoded in PEM format.

6.  To add a new certificate verification, complete the following steps:

    <div class="important">

    <div class="title">

    </div>

    - When you create a signature integration, you must add a new certificate verification if you want to use keyless verification for the image signature by using Red Hat Trusted Artifact Signer (RHTAS).

    - You can add one or more certificate verifications.

    </div>

    1.  Expand **Cosign certificates**, and then click **Add new certificate verification**.

    2.  Enter the certificate OIDC issuer that Cosign specifies. You must use regular expressions in RE2 syntax for matching.

        For more information, go to the GitHub repository at `google/re2`, open the `Wiki` section, and then select the `Syntax` page.

    3.  Enter the certificate identity that Cosign specifies. You must use regular expressions in RE2 syntax for matching.

        For more information, go to the GitHub repository at `google/re2`, open the `Wiki` section, and then select the `Syntax` page.

    4.  Enter the trusted certificate root encoded in PEM format to verify the certificates. If you do not specify the certificate root, the system uses the public Fulcio roots automatically for verification.

        For more information, see the "Fulcio" topic in the Sigstore documentation.

    5.  Enter the trusted signer intermediate certificate authority to verify the certificates. If you do not specify the certificate authority, the system uses the certificate chain automatically for verification.

    6.  Optional: Select the **Enable certificate transparency log validation** checkbox to validate the proof of inclusion into the certificate transparency log.

        Enter the public key that you want to use to validate the proof of inclusion into the certificate transparency log. If you do not specify the public key, the system uses the key of the public Sigstore instance automatically for validation.

7.  To configure the transparency log, complete the following steps:

    > [!NOTE]
    > When you create a signature integration, you can enable the validation of transparency logs in the following situations:
    >
    > - When the signatures contain short-lived certificates that Fulcio issues.
    >
    > - When you want to use keyless verification of the signatures.
    >
    > - To verify the signatures, when you use a public key.

    1.  Select the **Enable transparency log validation** checkbox to validate the inclusion of the signature in a transparency log.

        Enter the URL where the Rekor transparency log is available. If you do not specify the URL, the system uses the public Rekor instance of Sigstore automatically for validation.

        > [!NOTE]
        > You must specify the Rekor URL for online confirmation of the inclusion into the transparency log.

    2.  Optional: Select the **Validate in offline mode** checkbox to force the offline validation of the signature proof of inclusion into the transparency log.

        > [!NOTE]
        > You can force the offline validation of the signature proof of inclusion into the transparency log only if you have enabled the validation of the transparency log.

        Enter the public key to validate the signature proof of inclusion into the Rekor transparency log. If you do not specify the public key, the system uses the key of the public Sigstore instance automatically for validation.

8.  Click **Save**.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the RHACS portal, click **Platform Configuration** → **Integrations**.

2.  Scroll down to the **Signature Integrations** section, and then click **Signature**.

3.  Verify that the creation of the signature integration was successful.

4.  Optional: Choose the appropriate method to manage the signature integration that you have created:

    - To delete the signature integration, click the overflow menu ![kebab](../images/kebab.png) and then select **Delete Integration**.

    - To edit the signature integration, click the overflow menu ![kebab](../images/kebab.png) and then select **Edit Integration**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Overview (Sigstore documentation)](https://docs.sigstore.dev/cosign/signing/overview/)

- [Verifying Signatures (Sigstore documentation)](https://docs.sigstore.dev/cosign/verifying/verify/)

- [Fulcio (Sigstore documentation)](https://docs.sigstore.dev/certificate_authority/overview/)

</div>

<a id="verifying-image-signatures-to-ensure-image-integrity_verify-image-signatures"></a>

# Verifying image signatures to ensure image integrity

To verify image integrity, you must check that a trusted source signed the image. If you have enabled transparency log validation for your signature integration, you must also confirm that the scan includes a valid transparency log bundle.

For multi-architecture images, you must sign both the index and architecture-specific digests to avoid runtime resolution issues.

<div>

<div class="title">

Prerequisites

</div>

- You have created a signature integration.

  For more information about how to create a signature integration, see "Securing container Images by using signature integration".

</div>

<div>

<div class="title">

Procedure

</div>

- To scan an image signature by using the `roxctl` CLI, run the following command:

  ``` terminal
  $ roxctl image scan \
  --image=<registry>/<repository>/<image>@<digest> \
  --force-insecure-skip-tls-verify
  ```

  where:

  `<registry>`  
  Specifies the container image registry. For example, `quay.io`.

  `<repository>`  
  Specifies the repository of the container image. For example, `quay`.

  `<image>`  
  Specifies the name of the container image that you want to scan. For example, `busybox`.

  `<digest>`  
  Specifies the digest of the container image. For example, `sha256:92f3298bf80a1ba949140d77987f5de081f010337880cd771f7e7fc928f8c74d`.

  Verify that the output includes the signature. If you enabled transparency log validation for your signature integration, verify that the output includes the Rekor bundle with the proof of inclusion into the transparency log.

  If you enabled certificate verification for your signature integration, verify that the output includes the certificate verification data.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Securing container images by using signature integration](verify-image-signatures.md#securing-container-images-by-using-signature-integration_verify-image-signatures)

</div>

<a id="use-signature-verification_verify-image-signatures"></a>

# Using signature verification in a policy

When creating custom security policies, you can use the **Require image signature** policy criteria to verify image signatures.

<div>

<div class="title">

Prerequisites

</div>

- You must have already configured a signature integration with at least 1 Cosign public key.

</div>

<div>

<div class="title">

Procedure

</div>

1.  When creating or editing a policy, drag the **Require image signature** policy criteria in the policy field drop area for the **Policy criteria** section.

2.  Click **Select**.

3.  Select the trusted image signers from the list and click **Save**.

</div>

<div>

<div class="title">

Additional resources

</div>

- [Creating a security policy from the system policies view](manage_security_policies/custom-security-policies.md#create-policy-from-system-policies-view_custom-security-policies)

- [Understanding rules and policy criteria](manage_security_policies/security-policy-reference.md#policy-criteria_security-policy-reference)

</div>

<a id="enforcing-signature-verification_verify-image-signatures"></a>

# Enforcing signature verification

To prevent users from using unsigned images, you can enforce signature verification by using the RHACS admission controller. You must first enable the **Contact Image Scanners** feature in your cluster configuration settings. Then, while creating a security policy to enforce signature verification, you can use the **Inform and enforce** option.

<a id="additional-resources_verify-image-signatures"></a>

# Additional resources

- [Enabling admission controller enforcement](manage_security_policies/use-admission-controller-enforcement.md#enable-admission-controller-enforcement_use-admission-controller-enforcement)

- [Creating a security policy from the system policies view](manage_security_policies/custom-security-policies.md#create-policy-from-system-policies-view_custom-security-policies)
