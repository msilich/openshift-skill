<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

To connect an Azure Active Directory (AD) to RHACS using Sign-On (SSO) configuration, you need to add specific claims (for example, `group` claim to tokens) and assign users, groups, or both to the enterprise application.

<a id="adding-group-claims-to-tokens-for-saml-applications-using-SSO-configuration_user-authentication"></a>

# Adding group claims to tokens for SAML applications using SSO configuration

Configure the application registration in Azure AD to include `group` claims in tokens. For instructions, see [Add group claims to tokens for SAML applications using SSO configuration](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-connect-fed-group-claims#add-group-claims-to-tokens-for-saml-applications-using-sso-configuration).

> [!IMPORTANT]
> Verify that you are using the latest version of Azure AD. For more information on how to upgrade Azure AD to the latest version, see [Azure AD Connect: Upgrade from a previous version to the latest](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/how-to-upgrade-previous-version).
