<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

OpenShift Container Platform 4 contains new technologies and functionality that result in a cluster that is self-managing, flexible, and automated. OpenShift Container Platform 4 clusters are deployed and managed very differently from OpenShift Container Platform 3.

The most effective way to migrate from OpenShift Container Platform 3 to 4 is by using a CI/CD pipeline to automate deployments in an [application lifecycle management](https://www.redhat.com/en/topics/devops/what-is-application-lifecycle-management-alm) framework.

If you do not have a CI/CD pipeline or if you are migrating stateful applications, you can use the Migration Toolkit for Containers (MTC) to migrate your application workloads.

You can use Red Hat Advanced Cluster Management for Kubernetes to help you import and manage your OpenShift Container Platform 3 clusters easily, enforce policies, and redeploy your applications. Take advantage of the [free subscription](https://www.redhat.com/en/engage/free-access-redhat-e-202202170127) to use Red Hat Advanced Cluster Management to simplify your migration process.

To successfully transition to OpenShift Container Platform 4, review the following information:

[Differences between OpenShift Container Platform 3 and 4](planning-migration-3-4.md#planning-migration-3-4)
- Architecture

- Installation and upgrade

- Storage, network, logging, security, and monitoring considerations

[About the Migration Toolkit for Containers](about-mtc-3-4.md#about-mtc-3-4)
- Workflow

- File system and snapshot copy methods for persistent volumes (PVs)

- Direct volume migration

- Direct image migration

[Advanced migration options](advanced-migration-options-3-4.md#advanced-migration-options-3-4)
- Automating your migration with migration hooks

- Using the MTC API

- Excluding resources from a migration plan

- Configuring the `MigrationController` custom resource for large-scale migrations

- Enabling automatic PV resizing for direct volume migration

- Enabling cached Kubernetes clients for improved performance

For new features and enhancements, technical changes, and known issues, see the [MTC release notes](../migration_toolkit_for_containers/release_notes/mtc-release-notes.md#mtc-release-notes).
