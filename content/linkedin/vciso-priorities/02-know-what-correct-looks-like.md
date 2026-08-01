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

If the vCISO's master problem is that nobody knows what they are measuring, the operational answer is straightforward. Encode the intended state and compare against it continuously.

Twenty-eight independent sources converge on this. Google's SRE book. Adkins et al. in *Building Secure and Reliable Systems*. The mechanism: encode intended state as a set of packages with checksums, continuously monitor actual filesystem state, compare centrally, repair deviations automatically.

One mechanism catches random bit flips, accidental misconfigurations, buggy deployments, and malicious tampering. It unifies monitoring, compliance verification, incident detection, and recovery validation into a single operational principle.

The implications go beyond DevOps. If intended state is thoroughly encoded and continuously enforced, compliance becomes a side effect. If the intended state includes the controls required by ISO 27001 Annex A, and the system continuously enforces intended state, the system is continuously compliant by construction, not by periodic audit.

Incident response accelerates: the first responder's question, "what is normal?", is answered before the incident begins. Recovery becomes mechanical: restore to intended state.

This is the vCISO's operational north star. In every engagement, ask: have you encoded what correct looks like? If not, that is the first technical work. Not deploying tools. Not writing policies. Encoding intended state.

Because until you know what correct looks like, you cannot detect incorrect. And if you cannot detect incorrect, every other security investment is operating blind.
