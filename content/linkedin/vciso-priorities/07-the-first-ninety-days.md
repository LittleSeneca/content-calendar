---
title: "The First Ninety Days"
date: 2026-08-25
platform: linkedin
status: draft
tags: [vciso, strategy, playbook, onboarding]
scheduled_time: "08:00"
series: vciso-priorities
series_order: 7
---

The vCISO engagement clock starts ticking before the first invoice. Here is what the evidence says to do first.

Week one. Before recommending anything, establish what the client believes is true about their security posture and verify it against evidence. Ask for their risk register. If it is a spreadsheet of red, yellow, and green cells with no probabilities and no dollar ranges, the first finding is that they do not know their risk. Ask for their incident response plan. If it has not been tested in the last six months, the second finding is that they are not prepared to respond. Ask for their intended-state definition. If they cannot articulate what "correct" looks like for their critical systems, the third finding is that they cannot detect drift.

Three questions, one week, and you have the scope of the engagement.

Month one. Encode intended state for the highest-risk system. Pick one system, the one that if compromised would cause material harm. Encode its intended state: packages, versions, checksums, configurations, access policies. Set up continuous comparison. Automate repair of deviations. This accomplishes five things at once: it detects intrusions, prevents drift, verifies compliance, accelerates recovery, and demonstrates the methodology on a single system before scaling.

Month two. Prestage incident response. Deploy forensic agents. Test recovery procedures. Run a tabletop exercise. Verify escalation paths work when primary communication channels are down. A plan that has not been tested is not a plan. It is a wish.

Month three. Transition risk measurement from ordinal to quantitative. If the client has been using risk matrices, begin calibration training. Establish the decomposition framework for the highest-priority risks. Set an explicit, dated migration plan: calibrated estimation with Monte Carlo simulation within twelve months. The deadline matters. Without it, temporary ordinal assessment becomes permanent, and the illusion of communication returns.

The sequence matters more than the timeline. Close the communication gap first. Encode intended state second. Prestage response third. Transition measurement fourth. The sequence comes from the structure of the evidence, not from convention.
