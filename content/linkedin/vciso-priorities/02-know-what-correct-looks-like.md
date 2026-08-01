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

Heather Adkins, Betsy Beyer, Paul Blankinship, and the Google SRE team, in *Building Secure and Reliable Systems* (O'Reilly, 2020), describe a mechanism that is simple to state and hard to implement. Encode intended state as a set of packages with checksums. Continuously monitor actual filesystem state. Compare centrally. Repair deviations automatically.

One mechanism catches random bit flips, accidental misconfigurations, buggy deployments, and malicious tampering. It is monitoring, compliance verification, incident detection, and recovery validation in a single operational principle. Google's SRE book, *Site Reliability Engineering* (O'Reilly, 2016), reinforces the same idea from the operations side.

Here is the value for a security manager. If intended state includes the controls required by ISO 27001 Annex A, and the system continuously enforces intended state, the organization is continuously compliant by construction. No scrambling before the audit. No late nights rebuilding evidence. The auditor asks for proof that a control is in place. You point at a running system that cannot be out of compliance because deviation triggers automatic repair.

The first responder's question during an incident, "what is normal?", is answered before the incident begins. Recovery is mechanical: restore to intended state. You are not guessing whether the system is clean.

For a vCISO, this is the first technical work in any engagement. Not deploying tools. Not writing policies. Encoding what correct looks like. The client who has never had a security leader will have never done this. Delivering it in month one gives them something they can see working.
