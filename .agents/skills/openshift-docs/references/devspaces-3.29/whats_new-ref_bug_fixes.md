> Source: [Red Hat OpenShift Dev Spaces 3.29](https://docs.redhat.com/en/documentation/red_hat_openshift_dev_spaces/3.29/whats_new-ref_bug_fixes). Copyright Red Hat.
> Adapted from HTML to Markdown for offline use; see [legal notice](LEGAL-NOTICE.md) and [CC BY-SA 3.0](LICENSE.md). Links adjusted; source-fragment gaps are recorded in SOURCE.json.

<span id="ariaid-title1"></span>

# Bug fixes

The following release notes detail the bug fixes for the Red Hat OpenShift Dev Spaces 3.29 general availability release.

## Backup and restore operations now work correctly after workspace renaming

Before this update, backup and restore operations could fail after renaming a workspace. With this update, backup and restore operations use the immutable Kubernetes resource name instead of the display name. As a result, workspaces can be reliably restored after renaming.

**Additional resources**

- [CRW-10477](https://redhat.atlassian.net/browse/CRW-10477)

## Workspace restore from backup now works with private container registries

Before this update, restoring a workspace from a backup stored in a private container registry failed with a CrashLoopBackOff error in the workspace-restore init container. With this update, the backup restore process correctly authenticates with private container registries. As a result, workspaces can be restored from backups stored in private repositories.

**Additional resources**

- [CRW-10591](https://redhat.atlassian.net/browse/CRW-10591)

## User provisioning no longer fails on high-load clusters

Before this update, user provisioning could fail on busy clusters because reading the user-profile secret during concurrent operations caused 404 errors and infinite namespace creation attempts. With this update, user profile management has been simplified to a username-only approach. As a result, user provisioning is reliable on high-load clusters.

**Additional resources**

- [CRW-10682](https://redhat.atlassian.net/browse/CRW-10682)

## GitConfig Save button is now correctly disabled when required fields are empty

Before this update, the Save button on the User Preferences GitConfig tab was enabled even when the name or email field was empty, allowing users to save invalid gitconfig data. With this update, the Save button is disabled when required fields are empty. As a result, only valid gitconfig data can be saved.

**Additional resources**

- [CRW-10719](https://redhat.atlassian.net/browse/CRW-10719)

## Backup entries for deleted workspaces now display correctly

Before this update, the Backups tab failed to display backup entries for deleted workspaces because it read the registry authentication secret from the wrong namespace. With this update, the secret is read from the workspace namespace. As a result, backup entries for deleted workspaces are now accessible.

**Additional resources**

- [CRW-11421](https://redhat.atlassian.net/browse/CRW-11421)

## Resolved accessibility issues on the User Dashboard

To improve compliance with WCAG accessibility standards, the following issues on the User Dashboard have been resolved:

- Removed focusable elements from the collapsed left side panel to prevent keyboard navigation traps
- Removed empty alert group list element that violated ARIA required children rules on the Workspace Creation page Logs tab
- Fixed Git Services table display in User Preferences at 400% browser zoom
- Improved color contrast for event helper text on Workspace Details and Start Workspace pages
- Added mechanism to halt workspace starting from the Workspace Creation page
- Improved visibility of Delete and Revoke buttons in User Preferences dark mode
- Added discernible text to registry modal links for screen reader compatibility
- Fixed interactive controls nested in sample cards on the Create Workspace page
- Fixed invalid ARIA attribute on workspace status indicator
- Fixed invalid list structure in the navigation panel
- Fixed incomplete error suggestion fields in User Preferences and Create Workspace pages
- Fixed interactive controls nested in the Add Container Registry modal

**Additional resources**

- [CRW-11422](https://redhat.atlassian.net/browse/CRW-11422)

## Traefik ForwardAuth middleware no longer warns about unlimited response body size

Before this update, the Traefik ForwardAuth middleware produced a warning about unlimited response body size that could lead to DoS attacks and memory exhaustion. With this update, maxResponseBodySize is now configured. As a result, the warning is eliminated and the security concern is resolved.

**Additional resources**

- [CRW-11428](https://redhat.atlassian.net/browse/CRW-11428)
