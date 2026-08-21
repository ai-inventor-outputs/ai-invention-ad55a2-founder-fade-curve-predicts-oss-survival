# Methodology Grounding for Founder Fade Research

## Summary

This research establishes the methodological foundation for studying founder involvement trajectories and OSS project survival. It synthesizes findings from the foundational Avelino et al. (2019) study on Truck Factor Developer Detachment (TFDD), its 2025 large-scale replication by Nourry et al., and practical GitHub data extraction protocols. Key findings: (1) TFDD occurs when ALL truck-factor developers abandon a project, with a 1-year inactivity threshold providing the best precision-improvement tradeoff; (2) Among 1,932 popular projects, 16% faced TFDD and 41% survived; among 36,464 projects of all sizes, 89.6% faced TFDD but only 27% survived — revealing that smaller projects are far more fragile; (3) Surviving projects tend to be younger at TFDD time, have more post-TFDD commits, and often attract a single new core developer (86% of survivals); (4) GitHub data extraction is feasible via REST/GraphQL APIs for commits, merges, and reviews, but GH Archive BigQuery lacks PullRequestReviewEvent data; (5) Founder identification should combine repository creation metadata with earliest sustained contribution patterns; (6) Recommended statistical models include Cox Proportional Hazards for time-to-survival analysis and logistic regression for binary survival outcomes, controlling for project age, star count, contributor diversity, and file count.

## Research Findings

## Methodology Grounding for Founder Fade Research: What Determines OSS Project Survival After Founder Departure?

### 1. DEFINING THE CORE PHENOMENON: Truck Factor Developer Detachment (TFDD)

The foundational concept for studying founder departure in open-source projects is **Truck Factor Developer Detachment (TFDD)**, introduced and operationalized by Avelino, Constantinou, Valente, and Serebrenik (2019) [1]. The **Truck Factor (TF)** is defined as the minimal number of developers whose departure would put a project in serious trouble [1, 2]. TF is computed using the **Degree of Authorship (DOA)** metric: for each file, a developer's expertise is measured by whether they created the file and how many changes they made relative to others. The TF set comprises the minimal group of developers who are main authors (highest DOA) of at least 50% of the project's files [1].

**TFDD occurs when ALL TF developers abandon the project simultaneously** [1]. A developer is considered to have abandoned a project if their last commit occurred at least one year before the most recent repository commit [1]. This one-year threshold was selected from a sensitivity analysis comparing five thresholds (3 months, 6 months, 1 year, 1.5 years, 2 years), where the 1-year threshold achieved the highest harmonic mean of precision (82%) and improvement (55%) over the 6-month threshold [1].

A project is classified as **surviving** if, after a TFDD event, it attracts at least one new TF developer who assumes maintenance — transitioning the project from an "Inactive" state back to "Active" [1].

### 2. EMPIRICAL LANDSCAPE: HOW COMMON IS ABANDONMENT AND SURVIVAL?

**Avelino et al. (2019) — Popular Projects** [1]: In a dataset of 1,932 popular GitHub projects (top-500 most-starred across 6 languages), 315 projects (16%) experienced at least one TFDD. Of these, 128 projects (41%) survived by attracting new core developers. Key patterns:
- 66% of TFDDs occurred in projects with TF=1 (single core developer) [1]
- 59% of TFDDs happened in the first two years of development [1]
- 86% of survivals involved attracting a single new TF developer [1]
- 52% of new TF developers were existing contributors; 41% were newcomers [1]
- Surviving projects had significantly more post-TFDD commits (median: 505 vs. 126) and higher percentage of post-TFDD commits (56% vs. 15%) than non-surviving projects [1]
- Counterintuitively, surviving projects had FEWER developers (32 vs. 47), FEWER commits (384 vs. 694), and FEWER files (54 vs. 108) at the time of TFDD [1]

**Nourry et al. (2025) — Large-Scale Replication** [3]: Replicating Avelino's methodology on 36,464 projects (minimum 20 stars, 10 contributors, 2 years of history), they found dramatically different rates:
- 89.65% of projects faced at least one TFDD (vs. 16% in Avelino) — the difference attributed to including smaller, less popular projects [3]
- Only 27% of abandoned projects survived (vs. 41%) — smaller projects are less likely to attract new core developers [3]
- 70% of TFDDs occurred within the first three years [3]
- Most projects rely on a single core developer [3]
- The only metric showing a clear difference between surviving and non-surviving projects was **project age at TFDD**: surviving projects were older (1,267 days vs. 830 days) [3]

**Contradiction and Resolution**: The disparity between Avelino's 16% and Nourry's 89.6% TFDD rate is explained by sample composition. Avelino studied only the top-500 most-starred projects per language — elite projects with large communities. Nourry included projects with as few as 20 stars, capturing the long tail of smaller projects where abandonment is the norm [3]. This suggests that **project popularity and community size are critical confounding variables**.

### 3. WHAT PREDICTS SURVIVAL? EMPIRICAL FINDINGS

The empirical literature identifies several factors associated with project survival after founder departure:

**Project characteristics** [1, 3]:
- **Age at TFDD**: Older projects survive better (Nourry et al.: 1,267 vs. 830 days) [3]
- **Post-TFDD activity**: Surviving projects show substantially more commits after TFDD [1]
- **Size paradox**: Avelino found surviving projects were smaller at TFDD time, while Nourry found minor differences in size — suggesting the relationship may be non-linear or context-dependent [1, 3]

**Human and social factors** [1]:
- New maintainers were often already aware of abandonment risks when they started contributing [1]
- Their own usage of the system was the primary motivation to take over [1]
- Human and social factors played a key role in the transition [1]
- Lack of time and difficulty obtaining push access were the main barriers [1]

**Developer turnover patterns** [4, 5]:
- Ferreira et al. found larger projects and organization-owned projects showed higher core developer turnover rates [4]
- Lin et al. found developers with higher codebase ownership are more likely to stay [5]
- Calefato et al. found 45% of core developers completely disengage for at least one year, with 35-55% returning [6]

**Value-related discussions** [7]: Jamieson, Yamashita, and Foong (2024) showed that value-related discussions in GitHub issues can predict contributor turnover, suggesting that social dynamics and value alignment matter beyond pure code metrics [7].

### 4. DATA EXTRACTION PIPELINE: TECHNICAL FEASIBILITY

**Three-Channel Involvement Trajectories**:

1. **Commits**: Feasible via both REST API (`GET /repos/{owner}/{repo}/commits`) and GraphQL API (`repository.commits` connection). REST API returns 30 commits per page with pagination; GraphQL allows flexible filtering by author and date range. Rate limits: 5,000 requests/hour (REST, authenticated) or 5,000 points/hour (GraphQL) [8, 9].

2. **Merges**: Identifiable via REST API (`GET /repos/{owner}/{repo}/pulls?state=closed`) — the `merged_by` field identifies who performed the merge. GraphQL offers `repository.pullRequests` with `mergedBy` field. The `PullRequestEvent` in GH Archive contains merge information [10, 11].

3. **Reviews**: REST API (`GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews`) returns review data per PR. GraphQL offers `pullRequest.reviews` connection. **Critical limitation**: GH Archive BigQuery does NOT collect `PullRequestReviewEvent` — only `PullRequestReviewCommentEvent` is available [12]. Reviews without comments are invisible in the archive. For comprehensive review data, the REST or GraphQL API must be used directly.

**Bulk Extraction Options**:

- **GH Archive BigQuery**: Contains hourly GitHub event dumps since 2011. Event types include: PushEvent, PullRequestEvent, PullRequestReviewCommentEvent, IssueCommentEvent, CreateEvent, DeleteEvent, ForkEvent, ReleaseEvent, WatchEvent, and others [13]. Free tier allows 1 TB of queries per month. Best for commit and PR merge analysis, but NOT for comprehensive review data.

- **GitHub REST API**: 5,000 requests/hour for authenticated users. Suitable for per-repository extraction but requires careful rate-limit management for large cohorts.

- **GitHub GraphQL API**: 5,000 points/hour with complex scoring based on node counts. More efficient for complex queries but requires query optimization [8].

**Recommendation**: Use GH Archive BigQuery for commit and merge history at scale, supplemented by targeted REST/GraphQL API calls for review data on the specific project cohort.

### 5. FOUNDER AND DEPARTURE IDENTIFICATION PROTOCOLS

**Founder Definition**:
- **Primary method**: Repository creator (GitHub API: `repository.owner` and `repository.createdAt`) [14]
- **Secondary method**: Earliest sustained contributor — the developer with the most commits in the first 6-12 months of project history [1]
- **Pitfalls**: Multiple early contributors in team projects; organizational repositories where the "creator" is a bot or organization account; forks where the original founder is not the fork creator

**Departure Detection**:
- **Standard threshold**: 1 year of inactivity (last commit > 1 year before most recent repo commit) [1]
- **Alternative thresholds**: 3 months, 6 months (higher false positive rate), 1.5-2 years (higher false negative rate) [1]
- **Recommendation**: Use 1-year threshold as primary, with sensitivity analysis at 6-month and 1.5-year thresholds

**Control Variables** (confounding factors to include in models) [1, 3, 4]:
- Project age at time of TFDD
- Total star count
- Number of contributors
- Number of files and commits
- Programming language
- Organizational vs. individual ownership
- Contributor diversity (number of distinct contributors)
- Historical activity patterns (commit frequency before TFDD)

### 6. STATISTICAL ANALYSIS FRAMEWORK

**Recommended Models**:

1. **Cox Proportional Hazards**: For time-to-survival analysis — modeling the hazard of project death as a function of founder fade trajectory shape, controlling for covariates [15]

2. **Logistic Regression**: For binary survival outcome (survived vs. did not survive) with features derived from involvement trajectories [1]

3. **Mann-Whitney U Test**: For comparing distributions of metrics between surviving and non-surviving projects (as used in Avelino et al.) [1]

4. **Survival curves (Kaplan-Meier)**: For visualizing survival probability over time post-TFDD

**Feature Engineering from Trajectories**:
- Share of activity over time (monthly commits/merges/reviews as fraction of total)
- Fade curve shape (linear decline, step function, gradual taper)
- Time to last contribution
- Whether departure was abrupt (step) or gradual (fade)
- Presence of succession (new developer ramping up as founder ramps down)

### 7. LIMITATIONS AND OPEN QUESTIONS

- **TF algorithm limitations**: The DOA-based TF algorithm may not capture non-code contributions (documentation, issue triage, community management) that are critical to project survival [1]
- **Alias resolution**: The GitHub API email-to-user mapping misses developers with multiple accounts; median alias rate is 11% [1]
- **Review data gap**: GH Archive lacks PullRequestReviewEvent, limiting bulk analysis of code review patterns [12]
- **Survival definition**: Current definition (new TF developer arrives) may miss projects that survive through distributed maintenance without a single new core developer
- **Causal inference**: Observational studies cannot establish causality — projects that survive may have inherent characteristics that both enable survival and attract new developers

### 8. CONFIDENCE ASSESSMENT

**High confidence**: TFDD definition, 1-year threshold selection, basic survival statistics from Avelino et al. and Nourry et al., GitHub API capabilities for commits and merges.

**Medium confidence**: The relationship between project size and survival (contradictory findings between studies), the predictive power of fade curve shape (not yet empirically tested), the adequacy of commit-based metrics for capturing full involvement.

**Low confidence**: The generalizability of findings beyond GitHub to other platforms, the long-term survival of projects beyond the observation window of existing studies.

### FOLLOW-UP QUESTIONS

1. Can the **shape** of a founder's exit trajectory (abrupt departure vs. gradual fade vs. planned succession) predict survival better than static snapshots of project health at the time of departure?

2. How do **non-code contributions** (issue triage, documentation, community management, code review) factor into project survival when the founder departs — and can these be reliably measured from GitHub data?

3. What role does **organizational backing** (corporate sponsorship, foundation support, grant funding) play in mediating the relationship between founder departure and project survival, and how can this be operationalized as a control variable?


## Sources

[1] [On the abandonment and survival of open source projects: An empirical investigation (Avelino, Constantinou, Valente, Serebrenik, 2019)](https://pure.tue.nl/ws/files/128584841/ESEM2019.pdf) — Foundational study defining TFDD, establishing 1-year abandonment threshold, analyzing 1,932 popular GitHub projects. Found 16% TFDD rate, 41% survival rate. Identified that surviving projects have more post-TFDD commits but fewer developers/files at TFDD time. Surveyed 33 new maintainers about motivations and barriers.

[2] [On the abandonment and survival of open source projects: An empirical investigation (arXiv preprint)](https://arxiv.org/abs/1906.08058) — ArXiv preprint version of the same study, providing accessible full text and replication package reference.

[3] [Abandonment and Resilience: Understanding Core Developer Turnover in Open-Source Software (Nourry et al., 2025)](https://www.jstage.jst.go.jp/article/transinf/E108.D/11/E108.D_2025EDL8005/_pdf/-char/en) — Large-scale replication on 36,464 projects finding 89.6% TFDD rate and 27% survival rate. Revealed that smaller projects are far more fragile. Found project age at TFDD is the key differentiator between surviving and non-surviving projects.

[4] [Will you come back to contribute? Investigating the inactivity of OSS core developers in GitHub (Calefato et al., 2021)](https://doi.org/10.1007/s10664-021-10012-6) — Found that 45% of core developers completely disengage for at least one year, with 35-55% returning. Validated abandonment detection methods with real developers.

[5] [Predicting open source contributor turnover from value-related discussions: An analysis of GitHub issues (Jamieson, Yamashita, Foong, 2024)](https://doi.org/10.1145/3597503.3623340) — Showed that value-related discussions in GitHub issues can predict contributor turnover, suggesting social dynamics matter beyond code metrics.

[6] [Exploring factors affecting developer abandonment of open source software projects (Avelino, Constantinou, 2022)](https://doi.org/10.1002/smr.2484) — Follow-up study investigating specific factors affecting developer abandonment, extending the 2019 work with deeper analysis of motivational and contextual factors.

[7] [Rate limits and query limits for the GraphQL API (GitHub Documentation)](https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api) — Documents GraphQL API rate limits (5,000 points/hour for users), point calculation methodology, and query optimization strategies essential for bulk data extraction.

[8] [Rate limits for the REST API (GitHub Documentation)](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) — Documents REST API rate limits (5,000 requests/hour authenticated) and strategies for managing rate limits during bulk data extraction.

[9] [REST API endpoints for repository statistics (GitHub Documentation)](https://docs.github.com/en/rest/metrics/statistics) — Documents available REST API endpoints for fetching repository activity data including commits, pull requests, and contribution statistics.

[10] [Event types available on GHArchive](https://gist.github.com/jennynz/d8715f4db8eb562cf34efeac8785b8f1) — Comprehensive list of event types available in GH Archive BigQuery dataset, including PushEvent, PullRequestEvent, PullRequestReviewCommentEvent, and others.

[11] [GH Archive — GitHub event archive on BigQuery](https://github.com/igrigorik/gharchive.org) — GH Archive project providing hourly GitHub event dumps since 2011, accessible via Google BigQuery for bulk analysis of GitHub activity patterns.

[12] [PullRequestReviewEvent is not collected (GH Archive Issue #197)](https://github.com/igrigorik/gharchive.org/issues/197) — Documents the critical limitation that PullRequestReviewEvent is not collected in GH Archive — only PullRequestReviewCommentEvent is available, making reviews without comments invisible.

[13] [Google BigQuery + GH Archive (README)](https://github.com/igrigorik/gharchive.org/blob/master/bigquery/README.md) — Documents GH Archive availability on Google BigQuery with automatic hourly updates, enabling SQL queries over the entire GitHub event history.

[14] [REST API endpoints for pull requests (GitHub Documentation)](https://docs.github.com/en/rest/pulls/pulls) — Documents REST API endpoints for listing, viewing, and filtering pull requests, including the merged_by field for identifying merge authors.

[15] [The Cox Proportional Hazards Model (Survival Analysis)](https://doi.org/10.1093/acprof:oso/9780195337518.003.0004) — Standard reference for Cox Proportional Hazards model, the recommended statistical method for time-to-event analysis of project survival post-TFDD.

[16] [On the abandonment and survival of open source projects: Replication package (Avelino et al., 2019)](https://zenodo.org/records/2546008) — Replication package containing data and scripts used in the Avelino et al. 2019 study, enabling reproduction and extension of their analysis.

[17] [Defining Open-Source Software Success and Abandonment (Internet Success, 2012)](https://doi.org/10.7551/mitpress/8413.003.0013) — Early work defining OSS success and abandonment criteria, providing historical context for how the field has evolved in defining project survival.

## Follow-up Questions

- Can the shape of a founder's exit trajectory (abrupt departure vs. gradual fade vs. planned succession) predict survival better than static snapshots of project health at the time of departure?
- How do non-code contributions (issue triage, documentation, community management, code review) factor into project survival when the founder departs — and can these be reliably measured from GitHub data?
- What role does organizational backing (corporate sponsorship, foundation support, grant funding) play in mediating the relationship between founder departure and project survival, and how can this be operationalized as a control variable?

---
*Generated by AI Inventor Pipeline*
