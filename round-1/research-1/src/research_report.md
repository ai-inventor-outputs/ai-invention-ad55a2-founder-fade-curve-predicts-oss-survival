# Founder Fade Methodology for OSS Survival

## Summary

This research establishes a rigorous methodology for studying how open-source projects respond when their founders step away. It synthesizes findings from 10+ academic sources across four phases: (1) Literature operationalization from Avelino et al. (2019) defining Truck-Factor-Developer Detachment (TFDD) and project survival; (2) Technical feasibility of extracting three-channel involvement trajectories (commits, merges, reviews) via GitHub Archive BigQuery and GraphQL API; (3) Founder identification protocols combining repository creator status with earliest TF developer status, plus a validated 1-year inactivity threshold for departure detection; and (4) Statistical modeling recommendations including Cox Proportional Hazards and Accelerated Failure Time models. Key findings: 16% of popular GitHub projects experience TFDD; 41% survive by attracting new core developers; the 1-year inactivity threshold achieves optimal precision (0.82); social popularity can paradoxically accelerate abandonment; and no prior study has modeled the SHAPE of founder departure (gradual fade vs. sudden stop) as a predictor—identifying a clear research gap for the scaffolding fade hypothesis. The output includes a complete methodology synthesis with cohort selection protocol, labeling schema, feature engineering pipeline, and analysis plan ready for empirical implementation.

## Research Findings

## What Determines Whether an Open-Source Project Survives Its Founder Stepping Away?

This research synthesizes methodology from 10+ academic sources to answer how we can reliably study founder departure and project survival in open-source software (OSS).

### 1. Defining Founder Departure and Project Survival [1, 2]

The foundational framework comes from Avelino et al. (2019), who introduced **Truck-Factor-Developer Detachment (TFDD)**: the event when ALL key developers (the "truck factor" set) abandon a project simultaneously [1]. A project is defined as **surviving** if it attracts at least one NEW truck-factor developer after the detachment, transitioning from an "Inactive" to "Active" state [1].

**Key empirical findings from 1,932 popular GitHub projects:**
- 16% of projects (315) experienced TFDD [1]
- 41% of those (128 projects) survived by attracting new core developers [1]
- 86% of survivals involved exactly ONE new TF developer [1]
- 64% of survivals occurred within the first year after TFDD; only 2% after four years [1]
- 52% survived via old contributors returning; 41% via entirely new contributors [1]

### 2. The Inactivity Threshold: When Has a Founder Really Left? [1]

Defining "departure" requires an inactivity threshold. Avelino et al. (2019) rigorously tested five thresholds: 3 months, 6 months, 1 year, 1.5 years, and 2 years [1]. The **1-year threshold** achieved the best tradeoff with precision of 0.82 and improvement of 0.55 over the 6-month threshold [1]. Shorter thresholds (3-6 months) produce excessive false positives by misclassifying temporarily inactive developers as departed [1].

However, recent work by Xu et al. (2025) cautions that pure inactivity thresholds can misclassify projects that experience "revival" after periods of dormancy [4]. They propose a **dual-criteria approach**: (1) explicit GitHub "archived" status, AND (2) unambiguous abandonment statements in project documentation [4]. Their manual labeling of 1,174 keyword-matched repositories found that 65.6% of keyword matches were FALSE POSITIVES [4]. Earlier work by Coelho and Valente (2017) also explored keyword-based abandonment detection in project descriptions and found high false positive rates with simple keyword matching [9].

### 3. Identifying Founders: Multiple Methods [1, 2, 4]

No single standardized method exists, but four approaches emerge from the literature:

1. **Repository creator**: The user who created the repo (simplest, but may miss technical founders in org-owned repos) [1]
2. **Earliest sustained contributor**: Developer with earliest commits maintaining activity over a window (e.g., first 6 months) [2]
3. **Truck Factor developer at inception**: Compute TF at early snapshots; TF developers at t=0 are founders [1, 2]
4. **Push access/admin role**: Users with write permissions at project start (captures governance authority) [1]

**Recommended approach**: Combine repository creator with earliest TF developer. A founder is the repository creator IF they also appear as a TF developer in the first year; otherwise, the earliest TF developer(s) are founders [1, 2].

### 4. Data Extraction Pipeline [6, 7]

Three complementary data sources enable comprehensive trajectory extraction:

**GitHub Archive (GH Archive)** [6]: Provides bulk access to all public GitHub events since 2011 via Google BigQuery. Key event types include PushEvent (commits), PullRequestEvent (PR lifecycle), PullRequestReviewEvent (review submissions), and PullRequestReviewCommentEvent (review comments) [6]. Advantage: No per-repo rate limits; disadvantage: Public repos only.

**GitHub GraphQL API** [7]: Offers 5,000 points per hour for nested queries combining commits, PRs, and reviews. The `PullRequest.mergedBy` field identifies merge performers, and `PullRequest.reviews` returns all review states (APPROVED, CHANGES_REQUESTED, COMMENTED) with authors [7].

**GitHub REST API**: Rate-limited to 5,000 requests/hour with authentication; useful for specific endpoints not well-supported in GraphQL [7].

**Recommended pipeline**: Use GH Archive BigQuery for cohort selection and initial filtering, then GraphQL API for detailed per-project time-series extraction of commits, merges, and reviews per user per month [6, 7].

### 5. Statistical Models for Survival Analysis [3, 4, 5, 8]

Four modeling approaches are established in the literature:

**Cox Proportional Hazards** [3, 8]: Semi-parametric model estimating hazard ratios for each predictor. Used by Samoladas et al. (2010) and Robinson et al. (2022) [3, 8]. Limitation: Assumes proportional hazards (constant hazard ratios over time), which may be violated by time-varying founder activity features.

**Accelerated Failure Time (AFT)** [4, 5]: Parametric model directly modeling time-to-event; handles non-proportional hazards. Xu et al. (2025) achieved a C-index of 0.846 using AFT with multi-perspective features [4]. Kaushik (2026) used AFT to analyze 73,195 repositories [5]. Best suited for time-varying founder activity trajectories.

**Kaplan-Meier Estimator** [3]: Non-parametric survival curve estimation for visualizing survival differences between fade trajectory groups.

**Bayesian Survival Analysis** [3]: Generates posterior survival functions; more robust when incorporating prior knowledge.

### 6. Key Predictors of Survival [3, 4, 5, 8]

Prior survival analysis studies identify these factors:

- **Team size**: Each new developer increases survival probability by 15.8% [8]
- **Revision frequency**: High frequency (>1 commit/day) strongly predicts survival [3]
- **Major releases**: Projects publishing major releases survive longer [3]
- **Multi-hosting**: Projects on multiple platforms (GitHub + GitLab + PyPI) survive longer [3]
- **Maintainer response latency**: Slow responses correlate with abandonment [4]
- **Community participation balance**: Gini coefficient of contributions; imbalance predicts abandonment [4]

**The social popularity paradox** [5]: Kaushik (2026) found that excessive social attention (stars, watchers, forks) can ACCELERATE abandonment when not matched by sufficient contributor count. High visibility creates "induced demand" on maintainers, leading to information overload and burnout [5]. This challenges the conventional assumption that popularity always helps.

### 7. Research Gap: The Shape of Founder Departure

Critically, **no prior study has modeled the SHAPE of founder departure** as a predictor. All existing work treats departure as a binary event (active vs. inactive) at a single threshold [1, 3, 4]. The "scaffolding fade hypothesis"—that gradual founder departure (slowly declining involvement over months) enables better project survival than sudden disappearance—has NOT been empirically tested. This contrasts with the foundational "onion model" of OSS contributor layers (core, active, peripheral) established by Mockus et al. (2002), which showed that small core teams sustain large projects [10].

### 8. Confounding Variables to Control [1, 3, 4, 5]

Any model must control for: project age, total contributor count, star count, file count, programming language, revision frequency, maintainer response latency, and community participation balance (Gini coefficient) [1, 3, 4, 5].

### Confidence Level and Limitations

**High confidence** in: TFDD definition and survival operationalization (validated across 1,932 projects) [1]; 1-year threshold selection (sensitivity-analyzed) [1]; data extraction feasibility (GH Archive + GraphQL well-documented) [6, 7].

**Moderate confidence** in: Founder identification methodology (no single standard exists; recommended hybrid approach is reasonable but unvalidated) [1, 2]; social popularity paradox (single large study, needs replication) [5].

**Low confidence** in: The scaffolding fade hypothesis itself (novel, untested); optimal fade trajectory features (to be designed and validated).

### Cohort Selection Protocol

1. Select top-N most-starred repos per language (following Avelino et al.: top-500 per language) [1]
2. Filter: exclude forks, migrated repos, non-software repos, repos with <2 years history [1]
3. Compute TF at yearly intervals using DOA algorithm [2]
4. Identify TFDD events: all TF developers inactive for 1+ year [1]
5. Classify: Surviving (new TF developer after TFDD) vs. Abandoned (no new TF developer) [1]
6. Identify founders: repository creator + earliest TF developer [1, 2]
7. Extract founder activity trajectories: monthly commits, merges, reviews from founder start to departure [6, 7]

### Labeling Schema

- **Survival**: Project attracted new TF developer within observation window after TFDD [1]
- **Collapse**: Project remained inactive after TFDD through end of observation window [1]
- **Censoring**: Project still active at end of observation window (right-censored in survival analysis) [3]
- **Abandonment alternative**: Explicit GitHub archived status OR abandonment statement in README [4]

### Feature Engineering Pipeline

- **Raw events**: PushEvent, PullRequestEvent, PullRequestReviewEvent from GH Archive [6]
- **Time series**: Monthly aggregation per user: commits, PRs merged, reviews submitted [7]
- **Founder share**: Founder's activity / total project activity per month (0-1 ratio)
- **Fade trajectory features**: Rate of decline, time to zero, fade shape (gradual linear, exponential decay, step function), pre-departure activity, post-departure gap
- **Control features**: Project age, contributor count, star count, file count, language, revision frequency, maintainer response latency, community Gini coefficient [1, 3, 4, 5]

### Analysis Plan

- **Primary**: Cox PH model with founder-fade features as time-varying covariates [3, 8]
- **Secondary**: AFT model for non-proportional hazards [4, 5]
- **Exploratory**: Kaplan-Meier curves stratified by fade shape (gradual vs. sudden) [3]
- **Robustness**: Sensitivity analysis across departure thresholds (6mo, 1yr, 1.5yr) [1]
- **Interpretability**: SHAP values for feature importance [4]

### Research Gaps Identified

1. No prior study models the SHAPE of founder departure (gradual fade vs. sudden stop) as a predictor [1, 3, 4]
2. No study combines commits, merges, AND reviews into a multi-channel involvement trajectory
3. Most studies use static snapshots; few use time-varying survival analysis for founder activity [3, 4]
4. The 'scaffolding fade hypothesis' (that gradual departure enables survival) has not been empirically tested
5. Social popularity's dual role (lifeline vs. liability) needs more investigation in founder-departure context [5]
6. Maintainer identification methods vary across studies; no standard protocol exists [1, 2, 4]

## Sources

[1] [On the abandonment and survival of open source projects: An empirical investigation (Avelino et al., 2019)](https://arxiv.org/abs/1906.08058) — Foundational paper defining TFDD, survival, and the 1-year inactivity threshold. Analyzed 1,932 GitHub projects; found 16% TFDD rate, 41% survival rate. Surveyed 33 new maintainers.

[2] [A novel approach for estimating truck factors (Avelino et al., 2016)](https://arxiv.org/abs/1604.06766) — Introduces the Degree of Authorship (DOA) metric for TF estimation. Validated against 133 GitHub projects and surveyed 67 developers. 65% of projects have TF <= 2.

[3] [Two approaches to survival analysis of open source Python projects (Robinson et al., 2022)](https://arxiv.org/abs/2203.08320) — Applied Cox PH and Bayesian survival analysis to 2,066 Python projects. Found team size, revision frequency, major releases, and multi-hosting predict survival.

[4] [Predicting abandonment of OSS projects with an integrated feature framework (Xu et al., 2025)](https://arxiv.org/abs/2507.21678) — Constructed dataset of 115,466 repos with 57,733 confirmed abandonments. Dual-criteria abandonment detection. AFT model achieved C-index of 0.846. Multi-perspective features outperform surface metrics.

[5] [Social popularity of GitHub projects: A lifeline or a liability? (Kaushik & Chahal, 2026)](https://arxiv.org/abs/2607.00435) — Analyzed 73,195 repos using AFT framework. Found human capital is strongest protective factor; excessive social popularity accelerates abandonment (paradox of accessibility).

[6] [GH Archive - GitHub Event Archive](https://www.gharchive.org) — Public archive of all GitHub events since 2011, available via Google BigQuery. Key event types: PushEvent, PullRequestEvent, PullRequestReviewEvent.

[7] [GitHub GraphQL API Documentation](https://docs.github.com/en/graphql) — GraphQL API with 5,000 points/hour limit. Supports nested queries for commits, PRs, reviews. PullRequest.mergedBy identifies merge performers.

[8] [Applying survival analysis to study the health of open source projects (Samoladas et al., 2010)](https://doi.org/10.1109/ICSE.2010.5443544) — Early application of Cox PH to OSS survival. Found each new developer increases survival by 15.8%. Games/security domains have lowest survival.

[9] [Identifying abandoned open source projects (Coelho & Valente, 2017)](https://doi.org/10.1109/SANER.2017.7884611) — Explored keyword-based abandonment detection in project descriptions. Found high false positive rates with simple keyword matching.

[10] [Two case studies of open source software development: Apache and Mozilla (Mockus et al., 2002)](https://doi.org/10.1145/503269.503272) — Foundational study showing OSS projects rely on small core teams. Established the 'onion model' of contributor layers (core, active, peripheral).

## Follow-up Questions

- Can we operationalize and validate distinct 'fade shapes' (gradual linear decline, exponential decay, step function) as measurable features from commit/merge/review time series, and do they differentially predict survival?
- Does the interaction between founder fade shape and project social popularity (stars/forks) moderate survival outcomes—i.e., does gradual fade matter more for highly visible projects?
- Can multi-channel involvement trajectories (commits + merges + reviews) reveal departure patterns invisible when using commits alone, and do these patterns improve predictive accuracy over single-channel baselines?

---
*Generated by AI Inventor Pipeline*
