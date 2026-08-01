---
title: "Know What Correct Looks Like"
date: 2026-08-07
platform: linkedin
status: draft
tags: [vciso, devops, compliance, intended-state]
scheduled_time: "08:00"
series: vciso-priorities
series_order: 2
---

Adkins et al., in *Building Secure and Reliable Systems*, describe a mechanism that sounds simple and is not. Encode intended state as a set of packages with checksums. Continuously monitor actual filesystem state. Compare centrally. Repair deviations automatically.

One mechanism catches random bit flips, accidental misconfigurations, buggy deployments, and malicious tampering. It is monitoring, compliance verification, incident detection, and recovery validation in a single operational principle.

If intended state includes the controls required by ISO 27001 Annex A, and the system continuously enforces intended state, the organization is continuously compliant by construction. No periodic audit required.

The first responder's question, "what is normal?", is answered before the incident begins. Recovery is mechanical: restore to intended state.

In every engagement, ask whether the client has encoded what correct looks like. If not, that is the first work. Not deploying tools. Not writing policies. Encoding intended state.
