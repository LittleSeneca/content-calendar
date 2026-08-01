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

In any cloud environment, start with IAM. Not network segmentation. Not WAF rules. Not EDR. IAM.

Dylan Shields makes this explicit in *AWS Security*. IAM misconfiguration is the root cause of most AWS security incidents. Every AWS service interaction flows through IAM. IAM is not one control among many. It is the control plane for all controls. If IAM is wrong, everything built on it is wrong.

The mechanism that scales IAM is attribute-based access control with tags. ABAC enables dynamic, self-maintaining policies that scale with infrastructure without requiring policy updates for every resource change. The tagged-resources pattern, grant access based on resource tags, and tagged-principals pattern, match caller and resource tags, operationalize least privilege at scale.

This converges with the infrastructure-as-code principle. Just as infrastructure should be defined in version-controlled code, access policy should be defined in version-controlled, testable policy documents that scale through attribute matching rather than resource enumeration. Policy-as-code, enforced at the CI/CD pipeline, with manual review reserved for changes to shared infrastructure that automated policies cannot evaluate.

What I see in practice is often the reverse. Organizations spend money on ZTNA tooling, device posture, and microsegmentation rules. And then they leave their IAM environments overprivileged, under-controlled, and untagged.

AWS Config fills the gap CloudTrail leaves. CloudTrail tells you what API calls were made. Config tells you whether those calls changed the intended state of your resources. It is the same operational pattern as intended-state comparison, applied to cloud resources instead of servers.

For the vCISO, the finding is straightforward. Before any other cloud security control, verify IAM is correctly configured. Verify the shared responsibility boundary is understood. Verify access policies scale with infrastructure growth. IAM is the keystone. Start there.
