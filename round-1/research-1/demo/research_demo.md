# Literature Survey: Founder Fade & OSS Survival

## Summary

This research synthesizes findings across four critical areas for evaluating the Founder Fade Curve hypothesis: (1) OSS project abandonment and survival measurement using the Truck Factor Developer Detachment (TFDD) framework from Avelino et al. (2019) and Nourry et al. (2024), (2) founder identification methods including Degree of Authorship (DOA) and GitHub API alias resolution, (3) large-scale GitHub data sources with GH Archive/BigQuery recommended as primary due to free access and comprehensive coverage, and (4) trajectory shape analysis techniques including Theil-Sen estimators, ruptures change-point detection, convexity analysis, and composite index construction. Key findings: 57% of OSS projects have truck factor of 1, 16% experience founder detachment, only 41% survive. The survey identifies significant research gaps for several 2025-2026 papers cited in the hypothesis, and recommends adopting the Avelino TFDD framework with 1-year inactivity threshold as the primary survival definition.

## Research Findings

## Executive Summary

This literature survey establishes the methodological foundation for investigating the Founder Fade Curve hypothesis. The key finding is that the Truck Factor Developer Detachment (TFDD) framework from Avelino et al. (2019) provides the most rigorous existing methodology for defining and detecting founder departure events in OSS projects, with Nourry et al. (2024) validating and extending these findings to 36,000+ projects.

## Area 1: OSS Project Survival Measurement

The dominant framework is the Truck Factor Developer Detachment (TFDD) model [1]. Avelino et al. (2019) defined TF as the minimal number of developers whose departure would critically impact project maintenance [1]. They identified TFDD as the event when ALL truck factor developers abandon the project [1]. Their threshold sensitivity analysis validated a 1-year inactivity period as optimal (precision 0.82, harmonic mean 0.66) [1]. In their dataset of 1,932 popular GitHub projects:
- 57% have truck factor = 1 (single core developer) [1]
- 16% experienced at least one TFDD [1]
- 66% of TFDDs occurred in projects with TF=1 [1]
- 59% of TFDDs happened within the first 2 years [1]
- Only 41% (128/315) of projects survived their TFDD [1]
- Surviving projects had fewer developers, commits, and files but were younger at TFDD time [1]

Nourry et al. (2024) replicated this on 36,464 projects and found much higher TFDD rates (89%) but lower survival (27%) [2]. They concluded that 'projects that lose their core developer(s) early seem less likely to survive this event than projects that lost their core developers later on during their life' [2]. This directly supports the Founder Fade Curve hypothesis core premise that departure timing matters.

## Area 2: Founder Identification and Key-Developer Attribution

Three complementary methods emerge:

1. **Degree of Authorship (DOA)** [1, 3]: Identifies founders as developers with highest DOA (created file + change ratio) on >=50% of files at project inception. Validated by developer surveys (84% agreement on main authors, 53% agreement on TF values) [3].

2. **GitHub API Alias Resolution** [1]: Maps email addresses in commit headers to GitHub accounts. Median 11% alias rate per project [1]. Does not handle developers with multiple accounts.

3. **Repository Creator + Earliest Sustained Activity** [2]: Primary method combining creation date metadata with commit history patterns.

## Area 3: Large-Scale GitHub Data Sources

### GH Archive / BigQuery (RECOMMENDED) [8, 9]
- **Coverage:** February 2011 - present, hourly updates [8]
- **Cost:** 1 TB free/month on BigQuery [9]
- **Access:** Public dataset `bigquery-public-data.github_archive` [9]
- **Feasibility:** HIGH - most accessible, well-documented, cost-effective

### GHTorrent [6, 7]
- **Status:** Last full download January 2018; not actively maintained [7]
- **Feasibility:** LOW - stale data, complex MongoDB access

### GitHub REST API [10]
- **Rate limits:** 60/hour unauthenticated, 5,000/hour authenticated [10]
- **Feasibility:** MEDIUM - good for targeted queries, rate-limited for bulk

### GitHub GraphQL API [11]
- **Rate limits:** 5,000 points/hour (user), 10,000 points/hour (enterprise) [11]
- **Feasibility:** MEDIUM - powerful but complex

## Area 4: Trajectory Shape Analysis Methods

### Trend Estimation: Theil-Sen Estimator [12]
- **Implementation:** `scipy.stats.theilslopes()` or `sklearn.linear_model.TheilSenRegressor()` [12]
- **Advantages:** Robust to outliers (50% breakdown point), works with small samples [12]

### Change-Point Detection: ruptures Library [13]
- **Algorithms:** Binary Segmentation, PELT, Wild Binary Segmentation [13]
- **Python:** `ruptures.pelt(cost, min_size=5, pen=10).predict(n_bkps=1)` [13]

### Convexity Analysis [14]
- **Method:** Quadratic fit y = ax^2 + bx + c; coefficient 'a' indicates convexity
- **Interpretation:** a > 0 = decelerating fade (convex), a < 0 = accelerating fade (concave)

### Half-Life / Decay Rate [14]
- **Model:** Exponential decay y(t) = y0 * e^(-lambda*t)
- **Half-life:** t_1/2 = ln(2)/lambda

### Scaffolding Theory Connection [15]
- **Foundation:** Vygotsky's ZPD, Wood/Bruner/Ross scaffolding [15]
- **Limitation:** No existing quantitative fading index in educational psychology for this domain [15]
- **Novelty:** Requires original operationalization for software engineering context

## Validity Threats Summary

| Threat | Likelihood | Impact | Mitigation |
|--------|-----------|--------|------------|
| Founder misidentification | Medium | High | Multi-signal approach; manual validation |
| Survival label ambiguity | High | High | Adopt TFDD framework with validated threshold |
| Bus-factor confound | Medium | Medium | Control for TF value; stratify analysis |
| Project age confound | High | Medium | Include age as covariate; >2yr minimum |
| Small departed-founder cohort | High | High | Use large datasets (36K+ projects) |
| Multi-founder projects | High | Medium | Founder cohort variable; joint analysis |

## Research Gaps

1. Chen et al. (ICSE 2026) - Paper not located; may use different title or venue
2. Karim et al. (2026) - No matching paper on temporal transformers for OSS found
3. Noori et al. (2025) - No matching paper on governance.md textual analysis found
4. Death spiral paper - DOI exists but full text inaccessible via free search

## Next Steps

1. Query GH Archive/BigQuery for top-5000 repositories by stars
2. Extract per-author per-month commit counts (2015-2025)
3. Identify founders using repository creation date + earliest commits
4. Compute monthly founder involvement share trajectories
5. Apply Theil-Sen, ruptures, quadratic fit for feature extraction
6. Construct composite fade index
7. Correlate fade descriptors with survival outcomes

## Sources

[1] [On the abandonment and survival of open source projects: An empirical investigation](https://arxiv.org/abs/1906.08058) — Foundational TFDD framework study with 1,932 GitHub projects; established 1-year inactivity threshold; found 41% survival rate after founder departure

[2] [Myth: The loss of core developers is a critical issue for OSS communities](https://arxiv.org/abs/2412.00313) — Large-scale replication with 36,464 projects; found 89% TFDD rate but only 27% survival; early departures less likely to survive

[3] [A Novel Approach for Estimating Truck Factors](https://arxiv.org/abs/1604.06766) — DOA-based algorithm for identifying truck factor developers; validated on 133 projects with developer surveys

[4] [Defining Open-Source Software Success and Abandonment](https://doi.org/10.7551/mitpress/8413.003.0013) — Comprehensive framework for OSS success/failure definitions; identifies perils of mining GitHub data

[5] [What is the Truck Factor of popular GitHub applications? A first assessment](https://doi.org/10.7287/peerj.preprints.1233v2) — Early TF assessment in popular projects; found TF typically <= 2

[6] [GHTorrent: Github's Data from a Firehose](https://gousios.org/pub/ghtorrent-githubs-data-from-a-firehose.pdf) — Original GHTorrent dataset paper; MongoDB schema with events, commits, pulls, reviews

[7] [GHTorrent Querying MongoDB Programmatically](https://github.com/ghtorrent/ghtorrent.org/blob/master/raw.md) — Current GHTorrent access documentation; SSH tunnel requirements; ~10TB dataset

[8] [GH Archive](https://www.gharchive.org/) — Public GitHub timeline archive with hourly updates; 15+ event types available

[9] [Use BigQuery to query GitHub data](https://codelabs.developers.google.com/codelabs/bigquery-github) — Google codelab for querying GH Archive on BigQuery; 1TB free monthly tier; public dataset access

[10] [Rate limits for the REST API](https://docs.github.com/en/rest/using-the-rest-api/rate-limits-for-the-rest-api) — GitHub REST API documentation; 5,000 requests/hour authenticated; 60/hour unauthenticated

[11] [Rate and query limits for the GraphQL API](https://docs.github.com/en/graphql/overview/rate-limits-and-query-limits-for-the-graphql-api) — GraphQL API rate limits; 5,000 points/hour user, 10,000 points/hour enterprise; complexity-based scoring

[12] [theilslopes - SciPy v1.18.0 Manual](https://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.theilslopes.html) — Theil-Sen estimator implementation in scipy; robust regression with 50% breakdown point

[13] [ruptures: change point detection in Python](https://github.com/deepcharles/ruptures) — Python library for offline change point detection; PELT, binary segmentation, wild binary segmentation algorithms

[14] [Theil-Sen estimator](https://en.wikipedia.org/wiki/Theil%E2%80%93Sen_estimator) — Wikipedia overview of Theil-Sen estimator; robust regression method based on median of pairwise slopes

[15] [Towards a Synergistic Fading Model: Adapting Scaffolding Theory for Human-AI Collaboration](https://doi.org/10.35542/osf.io/5eutb_v1) — Scaffolding theory application; connects to Vygotsky ZPD and temporary support withdrawal concepts

## Follow-up Questions

- How should the founder fade curve be operationally defined when multiple co-founders exist, and what happens to trajectory analysis when the founder is actually a small team?
- What statistical power is needed to detect meaningful differences in fade curves between surviving and non-surviving projects, given the expected effect sizes from Avelino et al. (Cliff delta d=0.64-0.79)?
- How does the 1-year inactivity threshold for founder departure compare to the death spiral onset thresholds in Kaushik and Chahal (2026), and can these frameworks be reconciled?

---
*Generated by AI Inventor Pipeline*
