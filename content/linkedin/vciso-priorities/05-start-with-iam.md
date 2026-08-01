---
title: "Start With IAM"
date: 2026-08-18
platform: linkedin
status: draft
tags: [vciso, cloud, iam, aws, architecture]
scheduled_time: "08:00"
series: vciso-priorities
series_order: 5
---

Dylan Shields, in *AWS Security*, states the point directly. IAM misconfiguration is the root cause of most AWS security incidents. Every AWS service interaction flows through IAM. IAM is not one control among many. It is the control plane for all controls.

The mechanism that scales IAM is attribute-based access control with tags. ABAC enables dynamic, self-maintaining policies that scale with infrastructure without requiring policy updates for every resource change. The tagged-resources pattern, grant access based on resource tags, and tagged-principals pattern, match caller and resource tags, operationalize least privilege at scale.

What I see in practice is often the reverse. Organizations spend money on ZTNA tooling, device posture, and microsegmentation rules. And then they leave their IAM environments overprivileged, under-controlled, and untagged.

AWS Config fills the gap CloudTrail leaves. CloudTrail tells you what API calls were made. Config tells you whether those calls changed the intended state of your resources. Same operational pattern as intended-state comparison, applied to cloud resources instead of servers.

Before any other cloud security control, verify IAM is correctly configured. Verify the shared responsibility boundary is understood. Verify access policies scale with infrastructure growth.
