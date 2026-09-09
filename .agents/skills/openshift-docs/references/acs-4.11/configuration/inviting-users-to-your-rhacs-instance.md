<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

Invite users to Red Hat Advanced Cluster Security for Kubernetes (RHACS) so that the right users have the appropriate access rights within your cluster. You can invite one or more users by assigning roles and defining the authentication provider.

<a id="configuring-access-control-and-sending-invitations_inviting-users-to-your-rhacs-instance"></a>

# Configuring access control and sending invitations

By configuring access control in the RHACS portal, you can invite users to your RHACS instance.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to the **Platform Configuration → Access Control → Auth providers** tab, and then click **Invite users**.

2.  In the **Invite users** dialog box, enter the following information:

    - **Emails to invite**: Enter one or more email addresses of the users you want to invite. Ensure that they are valid email addresses associated with the intended recipients.

    - **Provider**: From the drop-down list, select a provider you want to use for each invited user.

      <div class="important">

      <div class="title">

      </div>

      - If you have only one authentication provider available, it is selected by default.

      - If many authentication providers are available and at least one of them is `Red Hat SSO` or `Default Internal SSO`, that provider is selected by default.

      - If many authentication providers are available, but none of them is `Red Hat SSO` or `Default Internal SSO`, you are prompted to select one manually.

      - If you have not yet set up an authentication provider, a warning message is displayed and the form is disabled. Click the link, which takes you to the **Access Control** section to configure an authentication provider.

      </div>

    - **Role**: From the drop-down list, select the role to assign to each invited user.

3.  Click **Invite users**.

4.  On the confirmation dialog box, you receive a confirmation that the users have been created with the selected role.

5.  Copy the one or more email addresses and the message into an email that you create in your own email client, and send it to the users.

6.  Click **Done**.

</div>

<div>

<div class="title">

Verification

</div>

1.  In the RHACS portal, go to the **Platform Configuration → Access Control → Auth providers** tab.

2.  Select the authentication provider you used to invite users.

3.  Scroll down to the **Rules** section.

4.  Verify that the user emails and authentication provider roles have been added to the list.

</div>
