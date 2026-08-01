---
title: "Risk Matrices Are Worse Than Random"
date: 2026-08-14
platform: linkedin
status: draft
tags: [vciso, risk-management, quantitative, grc]
scheduled_time: "08:00"
series: vciso-priorities
series_order: 4
---

The evidence against ordinal risk matrices is not ambiguous. Three independent research streams converge on the same finding: risk matrices should not be used for decisions of consequence.

The psychology of scales. Budescu's climate scientists and Heuer's intelligence analysts interpreted the same verbal labels across ranges spanning orders of magnitude. The mathematics. Cox's "risk matrix theorem" proved that risk matrices can be, under certain mathematically provable conditions, worse than random. The same input risk can map to different matrix cells, and different risks can map to the same cell, producing rank reversals. The empirical studies. Hubbard and Evans found that 76 percent of ordinal responses cluster on two values, reducing a 5x5 matrix to effectively 2x2.

Hubbard and Seiersen catalog this evidence in *How to Measure Anything in Cybersecurity Risk*. It is not a close call.

What replaces ordinal methods? Calibrated estimation. Untrained experts, including cybersecurity professionals, are systematically overconfident in their probability estimates. Calibration training produces measurable improvement. Experts go from 90 percent confidence intervals that capture the true value 40 percent of the time to intervals that capture it 80 to 90 percent of the time.

Decomposition is the second tool. Breaking an estimation problem into smaller, more estimable parts reduces error by factors of 10 to 100 for the most uncertain variables. Instead of asking "what is the probability of a material breach this year?", ask: what is the probability our web application has a SQL injection vulnerability? What is the probability an attacker discovers it? What is the probability exploitation succeeds? What is the probability success causes material financial damage?

The governance frameworks do not engage with this evidence. ISO 31010 states the risk matrix is "strongly applicable." NIST 800-30 uses likelihood and impact scales. The frameworks assume ordinal methods work because they have always assumed ordinal methods work. The evidence says that assumption is false.

The vCISO who uses risk matrices for decisions of consequence is practicing below the standard of care the evidence supports.
