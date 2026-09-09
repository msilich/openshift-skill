<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

With Red Hat Advanced Cluster Security for Kubernetes, you can add security notices that users see when they log in.

<a id="add-security-notices-overview_add-security-notices"></a>

# Security notices overview

You can configure security notices to display login messages, headers, and footers in the RHACS portal for policy reminders, disclaimers, and legal notifications.

You can also set up an organization-wide message or disclaimers on the top or bottom of the RHACS portal.

This message can serve as a reminder of corporate policies and tell employees of the appropriate policies. Alternatively, you might want to display these messages for legal reasons, for example, to warn users that you audit their actions.

<a id="add-a-custom-login-message_add-security-notices"></a>

# Adding a custom login message

You can configure a message to display when a user logs in to the portal. For example, you can display a message to warn malicious or uninformed users about the consequences of their actions.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `Administration` role with `read` permission to view the login message configuration options.

- You must have the `Administration` role with `write` permission to change, enable or disable the login message.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  On the **System Configuration** view header, click **Edit**.

3.  Enter your login message in the **Login configuration** section.

4.  To enable the login message, turn on the toggle in the **Login configuration** section.

5.  Click **Save**.

</div>

<a id="add-a-custom-header-and-footer_add-security-notices"></a>

# Adding a custom header and footer

You can configure the Red Hat Advanced Cluster Security for Kubernetes (RHACS) portal by entering custom text in the header and footer and configuring the text size and color.

<div>

<div class="title">

Prerequisites

</div>

- You must have the `Administration` role with `read` permission to view the custom header and footer configuration options.

- You must have the `Administration` role with `write` permission to change, enable or disable the custom header and footer.

</div>

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration** → **System Configuration**.

2.  On the **System Configuration** view header, click **Edit**.

3.  Under the **Header configuration** and **Footer configuration** sections, enter the header and footer text.

4.  Customize the header and footer **Text Color**, **Size**, and **Background Color**.

5.  To enable the header, turn on the toggle in the **Header Configuration** section.

6.  To enable the footer, turn on the toggle in the **Footer Configuration** section.

7.  Click **Save**.

</div>
