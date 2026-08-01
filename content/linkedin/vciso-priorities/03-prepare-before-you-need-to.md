---
title: "Prepare Before You Need To"
date: 2026-08-11
platform: linkedin
status: draft
tags: [vciso, incident-response, sre, prestaging]
scheduled_time: "08:00"
series: vciso-priorities
series_order: 3
---

The primary failure mode in incidents is not lack of tools. It is lack of practiced capacity to use them.

Heather Adkins and the Google SRE team make this case in *Building Secure and Reliable Systems* (O'Reilly, 2020). *Site Reliability Engineering* (O'Reilly, 2016) is blunt about it: "you only know recovery works if you test it." NIST SP 800-61 Revision 2, the federal standard for incident response, structures the hierarchy: events become adverse events become incidents, each with defined escalation triggers. ISO 27002:2022 provides the five-control incident management cycle. These documents are not competing frameworks. They make the same argument from different starting points.

Prestaging means forensic agents deployed on endpoints before the breach. Backup hardware procured and configured before the primary fails. Fallback access paths established before the VPN goes down. Escalation procedures defined, tested, and updated before the 3 a.m. phone call. Procurement contracts negotiated before you need emergency shipping.

The security manager who prestages response capacity delivers something that compounds. During an incident, practiced teams execute. They do not stop to debate procedure. The difference between a two-hour containment and a two-week recovery is often whether the team had run the procedure before they needed it, not whether they had better tools.

In the first engagement, before recommending any new tool, verify that the client has prestaged response capacity. Do they have forensic agents deployed? Tested recovery procedures? Escalation paths that work when primary communication channels are down? If the answer to any of these is no, fixing that is higher-leverage than any product you could recommend.
