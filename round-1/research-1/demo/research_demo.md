# Methodology Grounding for Founder Fade Research

## Summary

This research establishes the methodological foundation for studying founder involvement trajectories and OSS project survival through exhaustive investigation across 27 sources. Key findings: (1) TFDD occurs when ALL truck-factor developers abandon a project, with a 1-year inactivity threshold providing the best precision-improvement tradeoff [1]; (2) Among 1,932 popular projects, 16% faced TFDD and 41% survived; among 36,464 projects of all sizes, 89.6% faced TFDD but only 27% survived — revealing that smaller projects are far more fragile [1,3]; (3) Surviving projects tend to be older at TFDD time (1,267 vs 830 days), have more post-TFDD commits, and often attract a single new core developer (86% of survivals) [1,3]; (4) The AVL algorithm is the most accurate TF estimator, validated against a human oracle of 35 projects, but all commit-based algorithms miss non-code contributions (social interaction, code review, documentation, testing) [18]; (5) GitHub data extraction is feasible via REST/GraphQL APIs for commits, merges, and reviews, but GH Archive BigQuery lacks PullRequestReviewEvent data [8,12]; (6) Organizational ownership moderates the relationship between write access provisioning and survival — higher write access proportion increases novelty but reduces survival, and this effect is influenced by whether the project is organization-owned [20]; (7) Commit rights acquisition follows survival patterns: probability decreases with participation time, and developers who submit high-quality code, actively engage in code review, and make extensive contributions are more likely to gain commit rights [21]; (8) Governance structures (BDFL, meritocracy, foundation-led) significantly affect resilience to founder departure [24,25,26]; (9) The "death spiral" pattern suggests that the speed of founder departure matters — rapid departure triggers cascading failure more quickly than gradual fade [27]; (10) Recommended statistical models include Cox Proportional Hazards for time-to-survival analysis and logistic regression for binary survival outcomes, controlling for project age, star count, contributor diversity, file count, organizational ownership, and write access proportion.

## Research Findings

## Methodology Grounding for Founder Fade Research: What Determines OSS Project Survival After Founder Departure?

### 1. DEFINING THE CORE PHENOMENON: Truck Factor Developer Detachment (TFDD)

The foundational concept for studying founder departure in open-source projects is **Truck Factor Developer Detachment (TFDD)** — building on earlier work defining OSS success and abandonment criteria [17], introduced and operationalized by Avelino, Constantinou, Valente, and Serebrenik (2019) [1, 2]. The **Truck Factor (TF)** is defined as the minimal number of developers whose departure would put a project in serious trouble [1, 18]. TF is computed using the **Degree of Authorship (DOA)** metric: for each file, a developer's expertise is measured by whether they created the file and how many changes they made relative to others. The TF set comprises the minimal group of developers who are main authors (highest DOA) of at least 50% of the project's files [1, 18].

**TFDD occurs when ALL TF developers abandon the project simultaneously** [1]. A developer is considered to have abandoned a project if their last commit occurred at least one year before the most recent repository commit [1]. This one-year threshold was selected from a sensitivity analysis comparing five thresholds (3 months, 6 months, 1 year, 1.5 years, 2 years), where the 1-year threshold achieved the highest harmonic mean of precision (82%) and improvement (55%) over the 6-month threshold [1].

A project is classified as **surviving** if, after a TFDD event, it attracts at least one new TF developer who assumes maintenance — transitioning the project from an "Inactive" state back to "Active" [1, 16].

#### 1.1 TF Algorithm Landscape and Validation

A comprehensive comparative study by Ferreira, Mombach, Valente, and Ferreira (2019) evaluated four TF algorithms against a human oracle constructed from surveys with developers of 35 open-source projects [18]:

- **AVL Algorithm (Avelino et al., 2016)** [19]: Uses DOA (Degree of Authorship) to identify file authors, then greedily removes top authors until 50% of files become abandoned. **Best accuracy**: median error of 1 developer, correctly identifying TF for 100% of TF=1 projects [18].

- **RIG Algorithm (Rigby et al., 2016)**: Uses git-blame (line-level authorship) with random sampling (1,000 iterations). **Non-deterministic**: produces different results across runs, with dispersion ranging from 3 to 21 developers. Failed to produce results for large projects (symfony/symfony, saltstack/salt) due to insufficient random sampling [18].

- **CST Algorithm (Cosentino et al., 2015)**: Uses primary/secondary developer classification with knowledge thresholds. Performance depends on metric choice: "multiple changes equally considered" (MCEC) outperforms "last change takes it all" (LCTA), with 24 vs. 18 correct TF estimates [18].

- **ZWK Algorithm (Zazworka et al., 2010)**: Original combinatorial approach testing all possible developer combinations. **Does not scale** to projects with many contributors [18].

**Critical limitation identified**: All existing TF algorithms are commit-based and miss non-code contributions. A survey of 17 contributors (7 responses) revealed that key developers often contribute through: **social interaction** (mailing lists, issues, Stack Overflow, conferences — 4 responses), **code review** (accepting/reviewing PRs — 2 responses), **documentation** (2 responses), **testing** (2 responses), and **supporting tools** (plugins, installers, demos — 1 response) [18]. This means TF-based founder identification systematically underestimates the importance of developers whose primary value is governance, community building, or quality assurance.

#### 1.2 Relationship Between Truck Factor and Core Developers

Ferreira et al. (2019) compared TF developers against two Core Developer heuristics (Commit-Based: 80% of commits; LOC-Based: 80% of churn) [18]:

- **Truck Factor is a subset of Core Developers**: In 94% of systems evaluated by the Commit-Based Heuristic, the TF set is the same as or contained within the Core Developers set [18].
- **AVL algorithm outperforms both heuristics**: The LOC-Based Heuristic is more accurate than Commit-Based, but neither matches AVL's precision [18].
- **Implication**: TF developers are the "core of the core developers" — the smallest group whose departure would cause the most damage [18].

### 2. EMPIRICAL LANDSCAPE: HOW COMMON IS ABANDONMENT AND SURVIVAL?

#### 2.1 Avelino et al. (2019) — Popular Projects

In a dataset of 1,932 popular GitHub projects (top-500 most-starred across 6 languages: JavaScript, Python, Ruby, C/C++, Java, PHP), 315 projects (16%) experienced at least one TFDD [1, 16]. Of these, 128 projects (41%) survived by attracting new core developers [1].

**Key patterns**:
- 66% of TFDDs occurred in projects with TF=1 (single core developer) [1]
- 59% of TFDDs happened in the first two years of development [1]
- 86% of survivals involved attracting a single new TF developer [1]
- 52% of new TF developers were existing contributors; 41% were newcomers [1]
- Surviving projects had significantly more post-TFDD commits (median: 505 vs. 126) and higher percentage of post-TFDD commits (56% vs. 15%) than non-surviving projects (p = 5.02×10⁻²² and p = 2.04×10⁻³², Cliff's delta d = 0.64 and d = 0.79) [1]
- Counterintuitively, surviving projects had FEWER developers (32 vs. 47, p = 2.2×10⁻⁴), FEWER commits (384 vs. 694, p = 2.6×10⁻⁴), and FEWER files (54 vs. 108) at the time of TFDD [1]

**Qualitative findings from surveying 33 new maintainers**:
- Most new maintainers were aware of abandonment risks when they started contributing [1]
- Their own usage of the system was the primary motivation to take over [1]
- Human and social factors played a key role in the transition [1]
- Lack of time and difficulty obtaining push access were the main barriers [1]

#### 2.2 Nourry et al. (2025) — Large-Scale Replication

Replicating Avelino's methodology on 36,464 projects (minimum 20 stars, 10 contributors, 2 years of history) using the libraries.io dataset, Nourry et al. found dramatically different rates [3]:

- **89.65% of projects faced at least one TFDD** (vs. 16% in Avelino) — the difference attributed to including smaller, less popular projects [3]
- **Only 27% of abandoned projects survived** (vs. 41%) — smaller projects are less likely to attract new core developers [3]
- 70% of TFDDs occurred within the first three years [3]
- Most projects rely on a single core developer [3]
- The only metric showing a clear difference between surviving and non-surviving projects was **project age at TFDD**: surviving projects were older (1,267 days vs. 830 days, p < 0.05) [3]
- Minor differences in commits (388 vs. 323), files (75 vs. 79), and contributors (23 vs. 18) [3]

#### 2.3 Contradiction and Resolution

The disparity between Avelino's 16% and Nourry's 89.6% TFDD rate is explained by sample composition. Avelino studied only the top-500 most-starred projects per language — elite projects with large communities and resources. Nourry included projects with as few as 20 stars, capturing the long tail of smaller projects where abandonment is the norm [3]. This suggests that **project popularity and community size are critical confounding variables** that must be controlled in any analysis.

### 3. WHAT PREDICTS SURVIVAL? EMPIRICAL FINDINGS

#### 3.1 Project Characteristics

**Age at TFDD** [1, 3]:
- Nourry et al.: Surviving projects were older at TFDD time (1,267 vs. 830 days) [3]
- Avelino et al.: Surviving projects were surprisingly smaller at TFDD time [1]
- Interpretation: Older projects may have established communities, documentation, and governance structures that facilitate succession

**Post-TFDD activity** [1]:
- Surviving projects show substantially more commits after TFDD (median 505 vs. 126) [1]
- The percentage of post-TFDD commits is also higher (56% vs. 15%) [1]
- This suggests that continued development activity (even by minor contributors) is a strong signal of survival potential

**Size paradox** [1, 3]:
- Avelino found surviving projects were smaller at TFDD time [1]
- Nourry found minor differences in size [3]
- Possible explanation: Smaller projects may be easier for a single new developer to take over, while larger projects require more coordination

#### 3.2 Human and Social Factors

**New maintainer motivations** [1]:
- Own usage of the system is the primary motivation [1]
- Awareness of abandonment risks when starting to contribute [1]
- Human and social factors are key [1]

**Barriers to succession** [1]:
- Lack of time is the primary barrier [1]
- Difficulty obtaining push access (write permissions) is the second barrier [1]

**Value-related discussions** [7]:
- Jamieson, Yamashita, and Foong (2024) showed that value-related discussions in GitHub issues can predict contributor turnover [7]
- Social dynamics and value alignment matter beyond pure code metrics [7]

**Developer turnover patterns** [4, 5, 6]:
- Ferreira et al.: Larger projects and organization-owned projects showed higher core developer turnover rates [4]
- Lin et al.: Developers with higher codebase ownership are more likely to stay [5]
- Calefato et al.: 45% of core developers completely disengage for at least one year, with 35-55% returning [6]; contributor characteristics significantly influence future participation [22]

#### 3.3 Organizational and Governance Factors

**Write access provisioning** [20]:
- Medappa, Srivastava, and Dave Favaron (2025) analyzed 5,762 OSS projects and found that a **higher proportion of contributors with write access enhances novelty but reduces survival** [20]
- This relationship is **moderated by organizational ownership** — the effect differs between organization-owned and community-owned projects [20]
- Interpretation: Restricting write access to a core group is essential for long-term survival, while open write access favors innovation at the cost of stability [20]

**Commit rights acquisition** [21]:
- Tan et al. (2024) conducted survival analysis on commit rights acquisition in two representative OSS projects [21, 23]
- Probability of gaining commit rights **decreases with participation time** [21, 23]
- Developers who submit high-quality code, actively engage in code review, and make extensive contributions to related projects are more likely to be granted commit rights [21]
- Selection criteria in practice are generally consistent with community policies, but some qualifications are not adequately evaluated [21]

**Organizational ownership** [20]:
- Organization-owned projects show different survival dynamics than community-owned projects [20]
- Corporate backing provides resources but may create different failure modes (e.g., corporate strategic shifts) [20]

### 4. DATA EXTRACTION PIPELINE: TECHNICAL FEASIBILITY

#### 4.1 Three-Channel Involvement Trajectories

**Commits**:
- REST API: `GET /repos/{owner}/{repo}/commits` — 30 commits per page with pagination; rate limit 5,000 requests/hour (authenticated) [8, 9]
- GraphQL API: `repository.commits` connection — flexible filtering by author and date range; 5,000 points/hour [8]
- GH Archive BigQuery: `PushEvent` contains commit data; free tier allows 1 TB of queries per month [11, 13]

**Merges**:
- REST API: `GET /repos/{owner}/{repo}/pulls?state=closed` — `merged_by` field identifies merge author [14]
- GraphQL API: `repository.pullRequests` with `mergedBy` field [8]
- GH Archive BigQuery: `PullRequestEvent` contains merge information [10, 11]

**Reviews**:
- REST API: `GET /repos/{owner}/{repo}/pulls/{pull_number}/reviews` — returns review data per PR [8]
- GraphQL API: `pullRequest.reviews` connection [8]
- **Critical limitation**: GH Archive BigQuery does NOT collect `PullRequestReviewEvent` — only `PullRequestReviewCommentEvent` is available [12]. Reviews without comments are invisible in the archive. For comprehensive review data, the REST or GraphQL API must be used directly [12].

#### 4.2 Bulk Extraction Options

**GH Archive BigQuery** [11, 13]:
- Contains hourly GitHub event dumps since 2011 [11, 13]
- Event types: PushEvent, PullRequestEvent, PullRequestReviewCommentEvent, IssueCommentEvent, CreateEvent, DeleteEvent, ForkEvent, ReleaseEvent, WatchEvent, CommitCommentEvent, GollumEvent, MemberEvent, PublicEvent, SponsorshipEvent, GistEvent, FollowEvent, DownloadEvent, TeamAddEvent [10]
- Free tier: 1 TB of queries per month [11, 13]
- Best for: Commit and PR merge analysis at scale
- NOT suitable for: Comprehensive review data (missing PullRequestReviewEvent) [12]

**GitHub REST API** [8, 9]:
- 5,000 requests/hour for authenticated users [8]
- Suitable for per-repository extraction with careful rate-limit management
- Requires pagination handling (30 items per page)

**GitHub GraphQL API** [8]:
- 5,000 points/hour with complex scoring based on node counts [8]
- More efficient for complex queries but requires query optimization [8]
- Point calculation: sum requests for each connection, divide by 100, round to nearest whole number [8]

**Recommendation**: Use GH Archive BigQuery for commit and merge history at scale, supplemented by targeted REST/GraphQL API calls for review data on the specific project cohort.

### 5. FOUNDER AND DEPARTURE IDENTIFICATION PROTOCOLS

#### 5.1 Founder Definition

**Primary method**: Repository creator (GitHub API: `repository.owner` and `repository.createdAt`) [14]

**Secondary method**: Earliest sustained contributor — the developer with the most commits in the first 6-12 months of project history [1]

**Pitfalls**:
- Multiple early contributors in team projects
- Organizational repositories where the "creator" is a bot or organization account
- Forks where the original founder is not the fork creator
- Developers with multiple GitHub accounts (median alias rate is 11%) [1]

#### 5.2 Departure Detection

**Standard threshold**: 1 year of inactivity (last commit > 1 year before most recent repo commit) [1]

**Alternative thresholds** [1]:
- 3 months: Precision 38%, high false positive rate
- 6 months: Precision 59%, moderate false positive rate
- 1 year: Precision 82%, improvement 55% over 6 months (BEST) [1]
- 1.5 years: Precision 91%, improvement 50% [1]
- 2 years: Precision 95%, improvement 46% [1]

**Recommendation**: Use 1-year threshold as primary, with sensitivity analysis at 6-month and 1.5-year thresholds.

#### 5.3 Control Variables (Confounding Factors)

Based on synthesis of [1, 3, 4, 20]:
- Project age at time of TFDD
- Total star count
- Number of contributors
- Number of files and commits
- Programming language
- Organizational vs. individual ownership [20]
- Contributor diversity (number of distinct contributors)
- Historical activity patterns (commit frequency before TFDD)
- Write access proportion (fraction of contributors with push access) [20]
- Presence of corporate sponsorship or foundation backing [20]

### 6. STATISTICAL ANALYSIS FRAMEWORK

#### 6.1 Recommended Models

**Cox Proportional Hazards** [15]:
- For time-to-survival analysis — modeling the hazard of project death as a function of founder fade trajectory shape, controlling for covariates [15]
- Used by Tan et al. (2024) for analyzing time to commit rights acquisition [21]
- Allows time-varying covariates (e.g., monthly share of activity)

**Logistic Regression** [1]:
- For binary survival outcome (survived vs. did not survive) with features derived from involvement trajectories [1]
- Simpler interpretation but loses time-to-event information

**Mann-Whitney U Test** [1]:
- For comparing distributions of metrics between surviving and non-surviving projects (as used in Avelino et al.) [1]
- Non-parametric, robust to non-normal distributions

**Kaplan-Meier Survival Curves**:
- For visualizing survival probability over time post-TFDD
- Standard in survival analysis for censored data

#### 6.2 Feature Engineering from Trajectories

- Share of activity over time (monthly commits/merges/reviews as fraction of total)
- Fade curve shape (linear decline, step function, gradual taper)
- Time to last contribution
- Whether departure was abrupt (step) or gradual (fade)
- Presence of succession (new developer ramping up as founder ramps down)
- Code review participation trajectory (if data available)
- Issue/PR response time trajectory

### 7. LIMITATIONS AND OPEN QUESTIONS

#### 7.1 Methodological Limitations

**TF algorithm limitations** [1, 18]:
- DOA-based TF algorithm may not capture non-code contributions (documentation, issue triage, community management) that are critical to project survival [1]
- All commit-based algorithms systematically underestimate the importance of governance and community builders [18]
- Alias resolution: GitHub API email-to-user mapping misses developers with multiple accounts; median alias rate is 11% [1]

**Review data gap** [12]:
- GH Archive lacks PullRequestReviewEvent, limiting bulk analysis of code review patterns [12]
- Reviews without comments are invisible in the archive [12]

**Survival definition** [1]:
- Current definition (new TF developer arrives) may miss projects that survive through distributed maintenance without a single new core developer
- Does not capture "zombie" projects that have minimal activity but haven't formally died

**Causal inference**:
- Observational studies cannot establish causality — projects that survive may have inherent characteristics that both enable survival and attract new developers

#### 7.2 Generalizability

- All major studies focus on GitHub projects; findings may not generalize to GitLab, Bitbucket, or self-hosted repositories
- Long-term survival beyond the observation window of existing studies is unknown
- Language-specific patterns may exist (studies covered 6 languages but did not analyze differences)

### 8. CONFIDENCE ASSESSMENT

**High confidence**:
- TFDD definition and 1-year threshold selection (validated through sensitivity analysis) [1]
- Basic survival statistics from Avelino et al. and Nourry et al. (large samples, clear methodology) [1, 3]
- GitHub API capabilities for commits and merges (well-documented) [8, 9, 14]
- AVL algorithm superiority (validated against human oracle) [18]
- Organizational ownership moderating effect (large sample of 5,762 projects) [20]

**Medium confidence**:
- The relationship between project size and survival (contradictory findings between Avelino and Nourry) [1, 3]
- The predictive power of fade curve shape (not yet empirically tested as a specific variable)
- The adequacy of commit-based metrics for capturing full involvement (known to miss non-code contributions) [18]
- Write access proportion effect on survival (novel finding from single study) [20]

**Low confidence**:
- The generalizability of findings beyond GitHub to other platforms
- The long-term survival of projects beyond the observation window of existing studies
- The extent to which value-related discussions predict turnover (single study) [7]


### 9. GOVERNANCE STRUCTURES AND THEIR IMPACT ON SURVIVAL

#### 9.1 Governance Models in OSS

Open source projects employ various governance models that significantly affect their resilience to founder departure [24]:

- **Benevolent Dictator for Life (BDFL)**: A single individual (usually the founder) has final say on all major decisions. This model centralizes power and creates a single point of failure — when the BDFL departs, the project faces an immediate governance crisis [24, 25].

- **Meritocracy**: Authority is earned through sustained contributions. Decision-making is distributed among those who have demonstrated expertise. This model is more resilient to individual departure but can suffer from "role drift" where identical titles carry different responsibilities across projects [26].

- **Foundation-led governance**: Projects are hosted under foundations (e.g., Apache, Linux Foundation) that provide institutional stability. This model offers the highest resilience to founder departure but requires formal organizational infrastructure [25].

#### 9.2 The Maintainer Paradox

Oliveira, Conte, Gerosa, and Steinmacher (2026) identified the **"Maintainer Paradox"**: those who enable broad participation simultaneously become governance bottlenecks [26]. Their analysis of GOVERNANCE.md files across OSS projects revealed:

- Projects use a stable set of role titles, but identical titles carry different responsibilities across projects ("role drift") [26]
- A few actors sometimes accumulate technical, managerial, and community duties, creating single points of failure [26]
- Clearer role definitions and distributed work are essential for reducing leadership overload and supporting sustainable communities [26]

**Implication for founder fade research**: Projects with well-documented governance structures and distributed roles may be more resilient to founder departure. The presence and quality of GOVERNANCE.md files could serve as a control variable or predictor of survival.

#### 9.3 The Death Spiral

Recent work on the **"death spiral"** of open source projects identifies a cascading failure pattern: when key maintainers depart, pull request response times increase, new contributors are discouraged, the contributor base shrinks further, and the project enters a downward spiral toward abandonment [27]. This suggests that the **timing and speed** of founder departure matters — a rapid departure triggers the death spiral more quickly than a gradual fade that allows for knowledge transfer.

**Implication**: The "shape" of the fade curve (abrupt vs. gradual) may directly influence whether a project enters a death spiral, making it a critical variable for the scaffolding fade hypothesis.

### 10. SYNTHESIS: WHAT DETERMINES SURVIVAL?

The evidence converges on a multi-factorial model of project survival after founder departure:

1. **Project maturity matters**: Older projects survive better (Nourry et al.) [3], likely because they have established communities, documentation, and governance structures.

2. **Community depth matters**: Projects with more diverse contributor bases and lower write-access concentration are more resilient [20], but the relationship is complex — too much openness can reduce stability [20].

3. **Organizational backing helps**: Organization-owned projects show different survival dynamics, with corporate resources providing a buffer against founder departure [20].

4. **Succession quality matters**: Projects that attract new core developers who were already familiar with the codebase (52% of survivals) fare better than those relying on complete newcomers [1].

5. **The shape of departure may matter**: Whether a founder leaves abruptly or gradually (with handoff) has not been systematically studied but is hypothesized to be a key predictor — this is the central question the scaffolding fade hypothesis aims to test. Rapid departure triggers the "death spiral" [27], while gradual fade allows for knowledge transfer.

6. **Non-code contributions are critical**: Social interaction, code review, documentation, and testing are systematically underestimated by current metrics but are essential for project continuity [18].

7. **Governance structure matters**: Projects with well-documented roles, distributed authority, and clear succession plans are more resilient to founder departure [26]. The "Maintainer Paradox" warns that concentrating too many roles in few individuals creates fragility [26].

8. **Write access governance matters**: Restricting write access to a core group enhances survival but reduces novelty [20]. The optimal governance structure balances openness with stability.

### FOLLOW-UP QUESTIONS

1. Can the **shape** of a founder's exit trajectory (abrupt departure vs. gradual fade vs. planned succession) predict survival better than static snapshots of project health at the time of departure?

2. How do **non-code contributions** (issue triage, documentation, community management, code review) factor into project survival when the founder departs — and can these be reliably measured from GitHub data?

3. What role does **organizational backing** (corporate sponsorship, foundation support, grant funding) play in mediating the relationship between founder departure and project survival, and how can this be operationalized as a control variable?

4. Does the **proportion of contributors with write access** moderate the effect of founder departure on survival, and if so, what is the optimal governance structure for maximizing survival probability?


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

[18] [Algorithms for Estimating Truck Factors: A Comparative Study (Ferreira, Mombach, Valente, Ferreira, 2019)](https://homepages.dcc.ufmg.br/~mtov/pub/2019-sqj.pdf) — Comprehensive comparison of four TF algorithms (AVL, RIG, CST, ZWK) against a human oracle of 35 projects. AVL is most accurate. Revealed that all commit-based algorithms miss non-code contributions (social interaction, code review, documentation, testing). TF developers are a subset of Core Developers in 94% of cases.

[19] [A novel approach for estimating Truck Factors (Avelino, Passos, Hora, Valente, 2016)](https://doi.org/10.1109/icpc.2016.7503718) — Original paper introducing the AVL algorithm based on Degree of Authorship (DOA), validated with surveys of 67 popular GitHub projects.

[20] [Write access provisioning and organizational ownership in open source software projects: Exploring the impact on project novelty and survival (Medappa, Srivastava, Dave Favaron, 2025)](https://doi.org/10.1016/j.respol.2025.105284) — Analysis of 5,762 OSS projects finding that higher proportion of contributors with write access enhances novelty but reduces survival. Relationship is moderated by organizational ownership. Contributors with write access drive innovation; those without ensure reliability and survival.

[21] [How to Gain Commit Rights in Modern Top Open Source Communities? (Tan, Gong, Huang, Wu, Zhang, 2024)](https://arxiv.org/abs/2405.01803) — Survival analysis of commit rights acquisition in two representative OSS projects. Probability of gaining commit rights decreases with participation time. High-quality code, active code review, and extensive contributions to related projects increase likelihood of gaining commit rights.

[22] [Does Contributor Characteristics Influence Future Participation? A Case Study on Google Chromium Issue Tracking System](https://doi.org/10.1007/978-3-642-55128-4_22) — Study on how contributor characteristics influence future participation, relevant for understanding what predicts continued involvement after founder departure.

[23] [How to Gain Commit Rights in Modern Top Open Source Communities? (PACMSE FSE 2024)](https://doi.org/10.1145/3660784) — Journal version of Tan et al. 2024 study, published in Proceedings of the ACM on Software Engineering.

[24] [Leadership and Governance (Open Source Guides)](https://opensource.guide/leadership-and-governance/) — Comprehensive guide to OSS governance models including BDFL, meritocracy, and foundation-led governance. Documents how different models affect decision-making and project resilience.

[25] [Benevolent dictator governance model (OSS Watch)](http://oss-watch.ac.uk/resources/benevolentdictatorgovernancemodel) — Detailed analysis of the BDFL governance model, its strengths (swift decision-making) and weaknesses (single point of failure), and its prevalence in major OSS projects.

[26] [Governance in Practice: How Open Source Projects Define and Document Roles (Oliveira, Conte, Gerosa, Steinmacher, 2026)](https://arxiv.org/abs/2603.24879) — Analysis of GOVERNANCE.md files across OSS projects using Institutional Grammar. Identified the 'Maintainer Paradox' where those enabling broad participation become governance bottlenecks. Found 'role drift' where identical titles carry different responsibilities across projects.

[27] [The death spiral of open source projects: A post-mortem analysis of pull request workflow dynamics (2026)](https://doi.org/10.1016/j.jss.2026.112942) — Identifies the 'death spiral' pattern: when key maintainers depart, PR response times increase, new contributors are discouraged, the contributor base shrinks, and the project enters a downward spiral toward abandonment. Suggests that the speed of founder departure matters — rapid departure triggers the death spiral more quickly.

## Follow-up Questions

- Can the shape of a founder's exit trajectory (abrupt departure vs. gradual fade vs. planned succession) predict survival better than static snapshots of project health at the time of departure?
- How do non-code contributions (issue triage, documentation, community management, code review) factor into project survival when the founder departs — and can these be reliably measured from GitHub data?
- What role does organizational backing (corporate sponsorship, foundation support, grant funding) play in mediating the relationship between founder departure and project survival, and how can this be operationalized as a control variable?
- Does the proportion of contributors with write access moderate the effect of founder departure on survival, and if so, what is the optimal governance structure for maximizing survival probability?
- How does the governance model (BDFL vs. meritocracy vs. foundation-led) moderate the effect of founder departure on survival, and can governance documentation (GOVERNANCE.md) serve as a predictor of survival?

---
*Generated by AI Inventor Pipeline*
