<!-- Format modified: converted from AsciiDoc to Markdown. See SOURCE.json for provenance. -->

You can view administration event information in a single interface with Red Hat Advanced Cluster Security for Kubernetes (RHACS). You can use this interface to help you understand and interpret important event details.

<a id="accessing-the-event-logs-in-different-domains_using-the-administration-events-page"></a>

# Accessing the event logs in different domains

By viewing the administration events page, you can access various event logs in different domains.

<div>

<div class="title">

Procedure

</div>

- In the RHACS platform, go to **Platform Configuration → Administration Events**.

</div>

<a id="administration-events-page-overview_using-the-administration-events-page"></a>

# Administration events page overview

The administration events page organizes information in the following groups:

- **Domain**: Categorizes events by the specific area or domain within RHACS in which the event occurred. This classification helps organize and understand the context of events.

  The following domains are included:

  - `Authentication`

  - `General`

  - `Image Scanning`

  - `Integrations`

- **Resource type**: Classifies events based on the resource or component type involved.

  The following resource types are included:

  - `API Token`

  - `Cluster`

  - `Image`

  - `Node`

  - `Notifier`

- **Level**: Indicates the severity or importance of an event.

  The following levels are included:

  - `Error`

  - `Warning`

  - `Success`

  - `Info`

  - `Unknown`

- **Event last occurred at**: Provides information about the timestamp and date when an event occurred. It helps track the timing of events, which is essential for diagnosing issues and understanding the sequence of actions or incidents.

- **Count**: Indicates the number of times a particular event occurred. This number is useful in assessing the frequency of an issue. An event that has occurred multiple times indicates a persistent issue that you need to fix.

Each event also gives you an indication of what you need to do to fix the error.

<a id="getting-information-about-the-events-in-a-particular-domain_using-the-administration-events-page"></a>

# Getting information about the events in a particular domain

By viewing the details of an administration event, you get more information about the events in that particular domain. This enables you to better understand the context and details of the events.

<div>

<div class="title">

Procedure

</div>

- In the **Administration Events** page, click the domain to view its details.

</div>

<a id="administration-event-details-overview_using-the-administration-events-page"></a>

# Administration event details overview

The administration event provides log information that describes the error or event.

The logs provide the following information:

- Context of the event

- Steps to take to fix the error

The administration event page organizes information in the following groups:

- **Resource type**: Classifies events based on the resource or component type involved.

  The following resource types are included:

  - `API Token`

  - `Cluster`

  - `Image`

  - `Node`

  - `Notifier`

- **Resource name**: Specifies the name of the resource or component to which the event refers. It identifies the specific instance within the domain where the event occurred.

- **Event type**: Specifies the source of the event. Central generates log events that correspond to administration events created from log statements.

- **Event ID**: A unique identifier composed of alphanumeric characters that is assigned to each event. Event IDs can be useful in identifying, tracking, and managing events over time.

- **Created at**: Indicates the timestamp and date when the event was originally created or recorded.

- **Last occurred at**: Specifies the timestamp and date when the event last occurred. This tracks the timing of the event, which can be critical for diagnosing and fixing recurring issues.

- **Count**: Indicates the number of times a particular event occurred. This number is useful in assessing the frequency of an issue. An event that has occurred multiple times indicates a persistent issue that you need to fix.

<a id="setting-the-expiration-of-the-administration-events_using-the-administration-events-page"></a>

# Setting the expiration of the administration events

By specifying the number of days, you can control when the administration events expire. This is important for managing your events and ensuring that you retain the information for the desired duration.

> [!NOTE]
> By default, administration events are retained for 4 days. The retention period for these events is determined by the time of the last occurrence and not by the time of creation. This means that an event expires and is deleted only if the time of the last occurrence exceeds the specified retention period.

<div>

<div class="title">

Procedure

</div>

1.  In the RHACS portal, go to **Platform Configuration → System Configuration**. You can configure the following setting for administration events:

    - **Administration events retention days**: The number of days to retain your administration events.

2.  To change this value, click **Edit**, make your changes, and then click **Save**.

</div>
