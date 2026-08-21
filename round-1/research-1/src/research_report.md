# Founder Fade Curve and OSS Survival Literature Survey

## Summary

This research surveyed literature on founder identification, project survival metrics, GitHub API capabilities, and prior work on temporal trajectories of contributor involvement in open source software. Key findings include: Truck Factor (TF) as a measure of project dependency on key developers; 16% of projects experience TF developers detachment (TFDD); 41% of projects survive TFDD by attracting new core contributors; survival is associated with younger projects at TFDD time; GitHub API provides commits, pull requests, and review comments endpoints with pagination and rate limits; founder identification can be approached through initial commit analysis or CODEOWNERS files; longitudinal bus factor analysis reveals contributor turnover risks. Recommendations for hypothesis testing include: using 6-month inactivity threshold for founder departure, defining survival as continued commits after departure, utilizing GitHub commits API with author tracking, and controlling for project age and initial team size as confounds.

## Research Findings

Research into founder fade curves and OSS survival reveals several key insights for hypothesis testing:

1. **Founder Dependency Measurement**: The Truck Factor (TF) concept measures the minimal number of developers critical to project maintenance [1]. TF developers detachment (TFDD) occurs when these critical contributors leave [1]. Studies show 16% of projects experience at least one TFDD, with 66% occurring in projects where TF=1 (indicating single-founder dependency) [1].

2. **Survival Patterns**: 41% of projects survive their last observed TFDD [1]. Survival typically occurs by attracting a single new TF developer (86% of cases), with newcomers contributing to recovery in 48% of surviving projects [1]. Notably, surviving projects are younger at the time of TFDD compared to non-surviving ones, though no significant differences exist in developer count, commits, or files at the detachment moment [1].

3. **Temporal Dynamics**: 59% of TFDDs occur within the first two years of project development [1], suggesting early vulnerability periods. This aligns with the hypothesis of a "founder fade curve" where founder involvement decays over time.

4. **GitHub API Capabilities**: For tracking contributor activity, the GitHub REST API provides:
   - Commits endpoint: Lists commits with filtering by author, date range, and file path [3]
   - Pull requests endpoint: Tracks collaborative contributions [4]
   - Pull request review comments endpoint: Captures code review interactions [5]
   All endpoints support pagination (max 100 items per page) and require authentication for rate-limited access [3,4,5].

5. **Founder Identification Methods**: While no universal standard exists, approaches include:
   - Analyzing initial commits to identify early contributors [6]
   - Examining CODEOWNERS files when present [7]
   - Tracking contributors with merge privileges or review responsibilities
   - Note that team membership visibility is often private, limiting direct API access [7]

6. **Longitudinal Risk Metrics**: The bus factor (equivalent to TF) can be tracked longitudinally to measure evolving project resilience [8]. Tools like PRIME demonstrate how to compute and visualize such metrics over time, revealing trends in contributor dependency [8].

**Recommendations for Experiment Design**:
- **Inactivity Threshold**: Use 6 months of no commits from a founder to signal potential departure, balancing detection of true abandonment against temporary absences
- **Survival Definition**: Define project survival as continued commits (from any contributor) for at least 3 months post-founder-departure
- **Primary Data Source**: GitHub commits API to track author-specific activity over time
- **Key Confounds to Control**: Project age at founder departure, initial team size (TF), and external events like funding changes or major version releases

**Contradicting Evidence**: While the Avelino study found no pre-TFDD differences between surviving/non-surviving projects [1], other research suggests factors like documentation quality, issue responsiveness, and community engagement may predict survival prospects [2]. This indicates founder departure alone may not be sufficient to predict outcomes.

## Sources

[1] [On the abandonment and survival of open source projects: An empirical investigation](http://soft.vub.ac.be/benevol2019/papers/BENEVOL_2019_paper_3.pdf) — Foundational study showing Truck Factor concept, TFDD frequency (16%), survival rate (41%), and characteristics of surviving projects (younger at TFDD time).

[2] [On the abandonment and survival of open source projects: An empirical investigation](https://doi.org/10.1109/esem.2019.8870181) — Duplicate source confirming the Avelino et al. 2019 findings on OSS project abandonment and survival dynamics.

[3] [REST API endpoints for commits](https://docs.github.com/en/rest/commits/commits?apiVersion=2026-03-10) — GitHub API documentation for commits endpoint showing parameters for filtering by author, date, and path, plus pagination and rate limit information.

[4] [REST API endpoints for pull requests](https://docs.github.com/rest/pulls/pulls) — GitHub API documentation for pull requests endpoint showing parameters for filtering by state, head, base, and sort options.

[5] [REST API endpoints for pull request review comments](https://docs.github.com/en/rest/pulls/comments) — GitHub API documentation for accessing review comments on pull requests, useful for understanding collaboration patterns.

[6] [How to know who is the maintainer of a GitHub repository?](https://stackoverflow.com/questions/23540639/how-to-know-who-is-the-maintainer-of-a-github-repository) — Stack Overflow discussion highlighting challenges in identifying maintainers, noting that team privileges aren't public and CODEOWNERS file can help when present.

[7] [Introducing Code Owners](https://github.com/blog/2392-introducing-code-owners) — GitHub blog post introducing CODEOWNERS file format for designating maintainers and reviewers for specific code paths.

[8] [Snapshot Metrics Are Not Enough: Analyzing Software Repositories with Longitudinal Metrics](https://wenxin-jiang.github.io/files/SynovicHyattSethiThotaShilpikaMillerJiangPinderskiLauferHaywardKlingensmithDavisThiruvathukal-LongitudinalMetrics-ASE22Demo.pdf) — Paper describing PRIME tool for longitudinal metrics including bus factor, demonstrating how to track contributor dependency metrics over time.

## Follow-up Questions

- How does the decay pattern of founder commits (founder fade curve) vary across different types of OSS projects (e.g., libraries vs. applications)?
- What early-warning signals in contributor behavior precede actual founder departure beyond simple commit frequency?
- How do different governance models (BDFL, meritocratic, corporate-backed) influence the relationship between founder departure and project survival?

---
*Generated by AI Inventor Pipeline*
