> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/get_started-con_your_first_week_as_administrator). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Your first week as a platform administrator

After installing OpenShift Dev Spaces, complete a short sequence of configuration tasks before inviting developers to the platform. Each task builds on the previous one and takes you from a fresh deployment to a production-ready environment.

Your post-installation tasks follow this order:

1.  **Verify the platform works end-to-end.** Confirm that the Operator is healthy, the dashboard loads, and a test workspace starts successfully.
2.  **Configure Git provider access.** Connect OpenShift Dev Spaces to your organization’s Git provider with OAuth so that developers can clone repositories and push code without manually configuring credentials.
3.  **Share the dashboard URL with developers.** After verification and Git configuration, share the OpenShift Dev Spaces dashboard URL with your team. Developers can start coding immediately by entering a Git repository URL on the **Create Workspace** page.
4.  **Tune the platform for your environment.** Adjust workspace resource limits, enable image caching for faster starts, and configure security policies based on your organization’s requirements.

The first three tasks are covered in this guide. The fourth task is covered across the Secure, Optimize, and Configure guides.

**Related information**  

- [Secure OpenShift Dev Spaces](https://access.redhat.com/documentation/en-us/red_hat_openshift_dev_spaces/3.29/html-single/secure/index#secure_overview_secure)
- [Speed up workspace starts with image caching](optimize-assembly_caching_images_for_faster_workspace_start.md)
- [Customize the central configuration](configure-assembly_configuring_the_checluster_custom_resource.md)
