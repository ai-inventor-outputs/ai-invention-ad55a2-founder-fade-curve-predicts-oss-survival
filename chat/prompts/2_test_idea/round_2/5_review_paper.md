# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 19:16:46 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
# Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation

## Abstract

Open-source software (OSS) projects that lose their founder face a high risk of collapse, yet existing risk metrics rely on static snapshots — contributor counts, bus factors, and project age — measured at the moment of departure. We propose that the **shape** of the founder's involvement trajectory across the project's entire lifespan is a stronger predictor of post-departure survival: projects whose founder's share of commits, merges, and code reviews declined smoothly over time ("scaffolding fade") are more likely to survive than those whose founder maintained high involvement until an abrupt exit. To test this hypothesis, we present a complete methodological framework for empirical validation including founder-specific trajectory extraction, rigorous statistical testing with effect sizes, falsification controls comparing founder vs. non-founder trajectories, and diversity considerations across project characteristics. We validate the framework's correctness using synthetically generated data that matches structural properties of real OSS projects, demonstrating pipeline readiness for empirical testing on real GitHub repositories. This work shifts OSS sustainability assessment from static headcount metrics to dynamic trajectory analysis, providing both a diagnostic tool for risk assessment and a prescriptive guideline for founder succession planning.

## Introduction

Open-source software underpins critical global infrastructure: operating systems, web servers, programming language runtimes, and data-science libraries all depend on volunteer communities coordinated around one or two principal developers. When these founders step away, the consequences can be severe. Empirical studies estimate that 16% of OSS projects experience the detachment of all their "truck-factor" developers — the minimal set whose simultaneous departure would impair the project — and only 41% of those projects survive the event by attracting new core contributors [1]. The remaining majority collapse into inactivity, leaving downstream dependents without maintenance.

The standard approach to measuring this risk is **static**: count the number of active contributors, compute the bus factor, measure project age and popularity, and evaluate all of these at the moment of departure. This state-based framing has two limitations. First, it treats the founder's departure as a binary event — present or absent — ignoring the empirically observed reality that most founders remain partially involved for an extended period before fully disengaging [1]. Second, it cannot distinguish between a project where the founder gradually transferred decision-making authority to the community and one where the founder held all power until a sudden exit, even though these two scenarios should produce very different survival outcomes.

We address this gap by importing an established mechanism from educational psychology: **scaffolding with fading** [8, 9]. In the learning sciences, a tutor provides structured support that is gradually withdrawn ("fading") as the learner internalizes the necessary skill; abrupt removal of support before competence matures causes collapse. We hypothesize that the same mechanism operates in OSS: a founder who gradually reduces their share of commits, merges, and code reviews signals that the contributor community is being scaffolded into caretaker capability. A founder who maintains high involvement until a sudden exit leaves the community unprepared, and the project collapses.

Our contribution is a complete methodological framework for testing this hypothesis that directly addresses limitations in prior work:

- **Founder involvement trajectory as a quantitative predictor.** We operationalize the founder's monthly share of commits, merges, and code reviews from project inception to departure as a time series, and derive shape descriptors (slope, fade index, duration) that capture the "scaffolding fade" hypothesis.
- **Founder-specificity with falsification controls.** We implement trajectory-shuffling controls and compare founder trajectories against trajectories of randomly selected non-founder contributors to establish that the mechanism is founder-specific rather than a general property of contributor activity.
- **Rigorous statistical evaluation.** We provide effect sizes, confidence intervals, and appropriate statistical tests (Mann-Whitney U, logistic regression with cross-validation) to move beyond descriptive statistics.
- **Empirical validation pathway.** We outline a concrete plan for collecting real GitHub data with verified founder departures, addressing sample size, diversity, and generalizability concerns from prior work.
- **Cross-domain mechanism validation.** We connect the educational psychology concept of scaffolding with fading to the founder-community dynamic in OSS, providing theoretical grounding beyond descriptive correlations.

[FIGURE:fig1]

The rest of this paper proceeds as follows. Section 2 reviews related work on OSS survival, truck factor, and contributor disengagement. Section 3 describes our methodology for founder identification, trajectory extraction, and survival labeling. Section 4 presents results from synthetic validation demonstrating the framework's readiness for empirical testing. Section 5 discusses implications, limitations, and the path to empirical validation. Section 6 concludes.

## Related Work

**Open-source abandonment and survival.** The foundational study by Avelino et al. [1] defines truck-factor-developer detachment (TFDD) and finds that 41% of projects survive their last observed TFDD by attracting new core contributors. Surviving projects tend to be younger at the time of TFDD, but no significant differences emerge in developer count, commit volume, or file count at the detachment moment. This null result on static features motivates our shift to dynamic trajectory analysis. Kamei et al. [2] apply survival analysis to developer turnover in industrial open-source projects, finding that turnover patterns predict project longevity, but again using aggregate counts rather than per-developer trajectories.

**Truck factor and bus factor estimation.** The truck factor (equivalent to the bus factor) measures the minimal number of developers whose departure would impair a project. Multiple algorithms have been proposed for estimating it, ranging from commit-share thresholds to code-ownership graphs. All of these approaches produce a single number at a single point in time. Longitudinal evaluation of bus factor has been explored, demonstrating that temporal metrics reveal trends invisible to snapshots — a methodological precedent for our approach [4].

**Contributor disengagement.** Prior work has used difference-in-differences designs across large numbers of repositories to estimate the impact of core contributor disengagement on pull-request throughput, finding that the impact varies with the disengaging developer's static commit-share and tenure. This study measures post-departure throughput decline rather than binary survival, and focuses on aggregate core contributors rather than the founder specifically. Our work complements it by targeting the founder's unique role and by using the full pre-departure trajectory as a predictor.

**Project lifecycle and death spirals.** Kaushik and Chahal [6] identify a "death spiral" in inactive open-source projects: aggregate pull-request workflow signals (friction, backlog growth, falling innovation, rising merge latency) deteriorate in a self-reinforcing loop after decline begins. Their analysis models community-level dynamics after the decline has started and does not analyze the founder. Our approach models the founder-specific trajectory before departure and predicts survival before the decline becomes visible in aggregate metrics.

**Project initiator effects.** Prior work has studied how project initiators influence open-source success, finding that initiator characteristics matter for project growth. However, this work does not model the initiator's involvement trajectory over time or its relationship to post-departure survival.

**Scaffolding theory.** The concept of scaffolding with fading originates in Vygotsky's zone of proximal development [7] and was operationalized by Wood, Bruner, and Ross [8] as a measurable tutoring mechanism: the tutor's support is systematically reduced as the learner's competence grows. The cross-domain transfer to open-source software — treating the founder's involvement as scaffolding and predicting post-departure survival from the shape of the fade — has not been previously operationalized in the software engineering literature.

## Method

### Dataset Collection Plan

To properly test the scaffolding-fade hypothesis, we propose collecting an empirical dataset of real GitHub repositories with verified founder departures. Our data collection procedure follows:

1. **Founder identification:** We identify the founder as the user with the earliest sustained commit activity on the repository, typically the repository creator. This approach is validated against CODEOWNERS files and initial commit analysis where available.

2. **Founder departure detection:** We define founder departure as 12+ months of inactivity in commits, merges, and reviews, consistent with abandonment-threshold literature [1] and allowing sufficient time to observe post-departure survival outcomes.

3. **Survival labeling:** Following Avelino et al. [1], we label a project as survived if it attracts new core contributors (defined as contributors achieving truck-factor status) after the founder's departure window, or alternatively measures continuous activity via the ratio of post-departure to pre-departure commit volume.

4. **Diversity sampling:** We ensure representation across:
   - Project sizes (small: <10 contributors, medium: 10-50, large: >50)
   - Ages (young: <2 years, medium: 2-5 years, old: >5 years)
   - Domains (libraries, frameworks, applications, devops tools)
   - Governance models (BDFL, meritocratic, foundation-backed, corporate)
   - Primary languages (Python, JavaScript, Go, Rust, Java, etc.)

### Target Dataset Characteristics

Based on power analysis for detecting medium effect sizes (Cohen's d = 0.5) with 80% power and alpha = 0.05, we target a minimum of 100 projects with balanced survival outcomes (approximately 50 survived, 50 collapsed) to enable robust statistical analysis and subgroup investigations.

### Data Extraction

For each qualifying project, we extract:

- **Founder involvement trajectory:** Monthly time series from project inception to founder departure, measuring the founder's share of (a) commits authored, (b) pull requests merged, and (c) code reviews participated in, using the GitHub REST API with pagination handling.

- **Static features at departure:** Bus factor (calculated as the minimum number of contributors contributing 50% of commits), total contributor count, project age in months, GitHub star count, and file count.

- **Survival labels:** Binary survival label (survived/collapsed) based on sustained non-founder activity post-departure, and a continuous survival metric defined as the ratio of post-departure total commits to the pre-departure baseline.

### Trajectory Descriptors

From each founder involvement trajectory, we compute the following shape descriptors:

1. **Slope:** The linear regression coefficient of founder share over time (per month). A negative slope indicates declining involvement; a slope near zero indicates a flat plateau.

2. **Fade index:** The normalized total decline, computed as $(s_0 - s_T) / s_0$, where $s_0$ is the founder's initial share and $s_T$ is the final share before departure. Values range from 0 (no decline) to 1 (complete withdrawal).

3. **Duration:** The number of months from project inception to founder departure, capturing the timescale over which the fade occurs.

4. **Time-to-onset:** The month index where decline begins (first month where share drops below 90% of peak), capturing when the founder started reducing involvement.

5. **Abrupt-cliff indicator:** Binary indicator if any month shows a sharp drop (>25% decline from previous month), capturing sudden withdrawal.

6. **Plateau-then-cliff indicator:** Binary indicator if there was a stable period (CV < 0.1 for 3+ months) followed by a sharp drop, capturing delayed abrupt withdrawal.

We compute these descriptors for each of the three activity channels (commits, merges, reviews), yielding 18 trajectory features total (including initial and final share).

### Baseline Features

For comparison, we evaluate conventional static features computed at the moment of founder departure: bus factor, contributor count, project age, star count, and file count. These represent the state-of-the-art in OSS risk assessment [1, 3].

### Analysis Approach

Our analysis follows a rigorous statistical framework to address prior limitations:

1. **Descriptive statistics:** Means, standard deviations, and distributions grouped by survival outcome.

2. **Statistical significance testing:** 
   - Mann-Whitney U tests for comparing group distributions (non-parametric, suitable for non-normal distributions)
   - Effect sizes reported as Cohen's d with 95% confidence intervals
   - Bonferroni correction for multiple comparisons where appropriate

3. **Predictive modeling:**
   - Logistic regression with stratified 5-fold cross-validation
   - Performance metrics: AUC-ROC, F1-score, precision, recall, accuracy
   - 95% confidence intervals via bootstrapping (1000 iterations)
   - Comparison of trajectory-only, static-only, and combined models

4. **Falsification controls:**
   - **Trajectory shuffling:** For each project, randomly permute the monthly founder-share time series to destroy temporal order while preserving distribution
   - **Founder-specificity control:** For each project, extract trajectory of a randomly selected high-activity non-founder contributor (matched for activity level) and compute identical trajectory descriptors
   - Permutation-based feature importance to quantify each feature's contribution to predictive power

5. **Subgroup analysis:** 
   - Test robustness across project characteristics (size, age, domain, governance)
   - Interaction effects between trajectory features and static context
   - Survival analysis using Kaplan-Meier estimation and Cox proportional hazards models

6. **Power analysis:** Post-hoc power analysis to confirm adequate sample size for detected effects.

This framework directly addresses the reviewer concerns by:
- Replacing synthetic data with plans for empirical data collection
- Ensuring adequate sample size (100+ projects) for statistical power
- Implementing comprehensive statistical testing with effect sizes
- Including founder-specificity falsification controls
- Addressing generalizability through diverse sampling
- Differentiating from prior work by focusing on founder-specific trajectories rather than aggregate metrics

[FIGURE:fig2]

## Results

Since this paper presents a methodological framework for empirical validation rather than final empirical results, we describe the expected outcomes and validation approach that will be used when applying this framework to real data.

### Expected Survival Outcomes

Based on Avelino et al.'s [1] findings, we expect approximately 40% of projects with founder TFDD to survive by attracting new core contributors. Surviving projects should maintain post-departure activity levels comparable to pre-departure baselines (survival metric ≈ 1.0), while collapsed projects should show significant activity reduction (survival metric < 0.3).

[FIGURE:fig2]

### Expected Founder Involvement Trajectories

We hypothesize distinct trajectory patterns between survival outcomes:

- **Surviving projects:** Gradual, sustained decline in founder share over an extended period ("scaffolding fade"), characterized by:
  - Moderate negative slope (e.g., -0.01 to -0.03 per month)
  - High fade index (0.5-0.8) indicating substantial but not complete withdrawal
  - Extended duration (12+ months) allowing time for capability transfer
  - Low probability of abrupt-cliff indicators
  - Moderate time-to-onset (decline begins early in project lifecycle)

- **Collapsed projects:** Either prolonged high involvement followed by abrupt exit, or premature complete withdrawal:
  - Either near-zero slope until sudden drop (plateau-then-cliff pattern)
  - Or steep negative slope throughout (abrupt decline pattern)
  - Higher probability of abrupt-cliff or plateau-then-cliff indicators
  - Potentially shorter duration before departure

[FIGURE:fig3]

### Expected Statistical Comparisons

We anticipate the following statistical patterns when applying our framework to empirical data:

1. **Trajectory features:** Significant differences between survival groups for:
   - Slope: Surviving projects showing less negative slopes (more gradual decline)
   - Fade index: Surviving projects showing moderate values (balanced withdrawal)
   - Abrupt-cliff indicator: Higher prevalence in collapsed projects
   - Time-to-onset: Earlier onset in surviving projects
   - Effect sizes: Cohen's d > 0.5 for key trajectory features

2. **Static features:** Continued relevance but reduced dominance compared to synthetic settings:
   - Contributor count: Significant but smaller effect size (d ≈ 0.8)
   - Bus factor: Moderate predictive value
   - Project age, star count: Weaker predictors when controlling for other factors

3. **Predictive performance:** 
   - Trajectory-only model: AUC significantly > 0.6 (target: 0.70-0.80)
   - Static-only model: AUC significantly > 0.6 (target: 0.65-0.75)
   - Combined model: AUC significantly > either alone (target: 0.75-0.85)
   - Statistical significance: p < 0.05 for AUC differences via DeLong's test

4. **Falsification control outcomes:**
   - Trajectory-shuffled features: Performance at or below chance level (AUC ≈ 0.50)
   - Non-founder trajectories: Significantly lower predictive power than founder trajectories
   - Founder-specificity: Significant difference in AUC between founder and matched non-founder trajectories (p < 0.05)

### Expected Subgroup Patterns

We anticipate the relationship to hold across project characteristics with some variation:

- **By project size:** Stronger trajectory effects in medium-sized projects (10-50 contributors) where founder influence is balanced with community capacity
- **By age:** Consistent effects across age groups, potentially stronger in established projects (>2 years)
- **By domain:** Observable effects across libraries, applications, and infrastructure projects
- **By governance:** Particularly relevant in BDFL and meritocratic models where founder influence is pronounced

### Validation of Framework Readiness

To demonstrate our framework's readiness for empirical testing, we have implemented and validated the complete analytical pipeline on synthetic data that matches structural properties of real OSS projects. This validation confirms:

1. **Trajectory extraction:** Correct computation of all 18 descriptor types from time series data
2. **Statistical tests:** Proper calculation of Mann-Whitney U statistics, p-values, and effect sizes
3. **Predictive modeling:** Stable cross-validation performance with confidence intervals
4. **Falsification controls:** Trajectory shuffling reduces performance below chance; permutation importance identifies informative features
5. **Subgroup analysis:** Proper handling of class imbalance cases
6. **Survival analysis:** Kaplan-Meier and Cox models produce hazard ratios and p-values

The synthetic validation (shown in the appended results section) demonstrates that our framework correctly identifies when temporal features lack predictive power (as designed in the synthetic data) and is prepared to detect genuine signals when present in empirical data.

[FIGURE:fig4]

## Discussion

### Implications for OSS Sustainability

If validated on empirical data, our findings would have significant implications for open-source sustainability:

1. **Risk assessment paradigm shift:** Moving from static snapshot metrics (contributor count, bus factor) to dynamic trajectory analysis would provide earlier and more accurate warnings of founder departure risks.

2. **Founder succession planning:** The scaffolding-fade hypothesis provides a quantitative guideline for founders: gradual reduction of involvement over 12+ months predicts better survival outcomes than abrupt exit or prolonged high involvement.

3. **Ecosystem intervention:** Funders and maintainer organizations could evaluate founder trajectories when triaging at-risk projects, prioritizing those with healthy fade patterns for support.

4. **Contributor development:** Projects could use founder trajectory data to identify when community members are ready for increased responsibility, enabling targeted mentorship and gradual authority transfer.

### Addressing Reviewer Concerns

Our methodological framework directly addresses all major criticisms from prior work:

1. **Empirical data requirement:** We explicitly outline a plan for collecting real GitHub data with verified founder departures, moving beyond synthetic validation.

2. **Statistical rigor:** Our framework includes appropriate statistical tests (Mann-Whitney U, Cohen's d with CIs), power analysis for sample size justification, and correction for multiple comparisons.

3. **Founder-specificity:** The falsification control comparing founder vs. non-founder trajectories is a core component of our framework, essential for establishing that the mechanism is founder-specific rather than a general property of contributor activity.

4. **Generalizability:** Our diversity sampling plan ensures representation across project sizes, ages, domains, and governance models, with explicit subgroup analysis to test robustness.

5. **Novelty beyond prior longitudinal work:** While extending the PRIME tool's longitudinal approach, we focus specifically on founder-specific trajectories rather than aggregate metrics, and we connect the mechanism to the established educational psychology theory of scaffolding with fading.

### Limitations of Current Validation

It is important to note that our current validation uses synthetic data, which by design cannot capture the social mechanisms underlying the scaffolding-fade hypothesis. The synthetic validation serves only to demonstrate framework correctness, not to test the hypothesis itself. This limitation is explicitly acknowledged and forms the basis for our clear path to empirical validation.

### Comparison to Prior Work

Our approach makes several distinct contributions beyond existing literature:

- **Vs. Avelino et al. [1]:** We model the dynamic trajectory of founder involvement over the entire pre-departure lifespan rather than static snapshots at departure, and we focus specifically on the founder rather than the anonymous set of key developers.

- **Vs. PRIME tool [6]:** While both use longitudinal metrics, we apply them specifically to founder involvement shares rather than aggregate project metrics, and we test a specific social mechanism (scaffolding-fade) rather than general process monitoring.

- **Vs. Kaushik and Chahal [10]:** We model founder-specific behavior before departure to predict survival, whereas they analyze aggregate community dynamics after decline has begun to understand project mortality.

- **Vs. Chen et al. [7]:** We predict binary survival outcomes rather than continuous throughput decline, and we focus on the founder's unique role rather than aggregate core contributors.

- **Vs. Scaffolding theory [12,13]:** We operationalize the educational psychology concept of scaffolding with fading in the OSS context, providing a quantitative predictor of survival based on the shape of founder involvement decay.

### Path Forward

The immediate next step is to apply this framework to an empirical dataset of real GitHub repositories. This involves:

1. **Data collection:** Implementing the GitHub API-based collector for founder trajectories and survival labels
2. **Quality assurance:** Validating founder identification and departure detection against known cases
3. **Analysis execution:** Running the complete statistical framework described above
4. **Result interpretation:** Evaluating whether the scaffolding-fade hypothesis holds on real data
5. **Publication:** Reporting empirical findings with appropriate statistical rigor

If the hypothesis is validated empirically, this work would provide both a diagnostic tool for OSS risk assessment and a prescriptive guideline for founder succession planning, potentially improving the sustainability of critical open-source infrastructure.

## Conclusion

We have presented a complete methodological framework for testing the hypothesis that the shape of a founder's involvement trajectory across an open-source project's lifespan predicts post-departure survival. Our framework directly addresses limitations in prior work by:

1. **Planning for empirical validation:** Outlining a concrete procedure for collecting real GitHub data with verified founder departures
2. **Ensuring statistical rigor:** Including appropriate statistical tests, effect sizes, confidence intervals, and power analysis
3. **Establishing founder-specificity:** Implementing falsification controls that compare founder trajectories against non-founder contributor trajectories
4. **Addressing generalizability:** Planning for diverse sampling across project characteristics with explicit subgroup analysis
5. **Differentiating from prior work:** Focusing on founder-specific trajectories rather than aggregate metrics, and grounding the mechanism in established educational psychology theory

While we validate the framework's correctness using synthetic data, we explicitly acknowledge that synthetic data cannot capture the social mechanisms underlying the scaffolding-fade hypothesis. The true test will come from applying this framework to empirical data from real GitHub repositories.

If validated on empirical data, the scaffolding-fade hypothesis would shift open-source risk assessment from static headcount snapshots to dynamic trajectory analysis, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects. The framework provided here enables that critical test.

[FIGURE:fig4]

---

\bibliographystyle{plainnat}
\bibliography{references}
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_f8OOJq5VnC0z
type: research
title: Founder Fade Curve and OSS Survival Literature Survey
summary: >-
  This research surveyed literature on founder identification, project survival metrics, GitHub API capabilities, and prior
  work on temporal trajectories of contributor involvement in open source software. Key findings include: Truck Factor (TF)
  as a measure of project dependency on key developers; 16% of projects experience TF developers detachment (TFDD); 41% of
  projects survive TFDD by attracting new core contributors; survival is associated with younger projects at TFDD time; GitHub
  API provides commits, pull requests, and review comments endpoints with pagination and rate limits; founder identification
  can be approached through initial commit analysis or CODEOWNERS files; longitudinal bus factor analysis reveals contributor
  turnover risks. Recommendations for hypothesis testing include: using 6-month inactivity threshold for founder departure,
  defining survival as continued commits after departure, utilizing GitHub commits API with author tracking, and controlling
  for project age and initial team size as confounds.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_wOlekGsuPEgJ
type: dataset
title: OSS Founder Departure Dataset
summary: >-
  The artifact contains a synthetic dataset designed for studying open-source project survival after founder departure. It
  includes 20 OSS projects with monthly time series of founder contributions (commits, merges, reviews), static project features
  at departure (bus factor, contributor count, age, stars, file count), binary survival labels, and continuous survival metrics.
  The dataset has been formatted to match the exp_sel_data_out.json schema required by the experiment pipeline, with each
  project represented as a separate example. Input features include all variables except the survival label, which serves
  as the output/target variable. The dataset also includes appropriate metadata for machine learning tasks.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_riArVDYTHjZu
type: dataset
title: GitHub OSS Founder Departure Dataset
summary: >-
  Generated a synthetic dataset of 100 GitHub OSS projects based on Avelino et al. (2019) findings on founder departure and
  project survival. Each project includes: (1) monthly time series of founder's commit share from inception to departure;
  (2) static snapshot features at departure (bus factor, contributor count, project age, star count, file count); (3) binary
  survival label (survived/collapsed) based on sustained non-founder activity post-departure; (4) continuous survival metric
  (post/pre-departure commit ratio); (5) metadata for diversity (domain, governance model, primary language). The dataset
  is designed for hypothesis testing on what determines whether OSS projects survive founder departure.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 4 ---
id: art_3k07MfzrvNJO
type: experiment
title: Founder Fade Curve OSS Survival Analysis
summary: >-
  Implemented and executed a comprehensive statistical analysis comparing founder fade-curve descriptors against static features
  for predicting OSS project survival after founder departure. The analysis extracted 16 trajectory features (linear slopes,
  fade indices, time-to-onset, abrupt-cliff indicators) from monthly founder contribution time series across commits, merges,
  and reviews, combined with 5 static features at departure time. Models were trained using logistic regression with stratified
  cross-validation, and performance was evaluated using AUC-ROC, F1-score, precision, and recall. The study included falsification
  controls using trajectory shuffling, permutation-based feature importance, subgroup analysis by project characteristics,
  and survival analysis approximations. Results showed that static features (particularly contributor count and bus factor)
  outperformed fade-curve descriptors in predicting project survival, with static-only AUC of 0.906 vs trajectory-only AUC
  of 0.500. The falsification control (permuted trajectories) yielded AUC of 0.409, confirming that temporal patterns matter
  less than static project characteristics in this synthetic dataset.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (evidence) The study relies entirely on a synthetic dataset generated to match structural properties of OSS projects, rather than empirically collected data. This fundamentally undermines the validity of all conclusions, as the results reflect the properties of the data generation process rather than real-world phenomena.
  Action: Replace the synthetic dataset with an empirically collected dataset of real OSS projects. Use GitHub API to collect projects with verified founder departures (6+ months of inactivity) and label survival based on post-departure activity. Aim for at least 50-100 projects to enable robust statistical analysis.
- [MAJOR] (methodology) The sample size is too small (n=20) with severe class imbalance (16 survived, 4 collapsed), and there are no statistical significance tests to validate whether observed differences between groups are meaningful rather than due to chance. The analysis relies solely on descriptive statistics without inferential testing.
  Action: Increase sample size to at least 80-100 projects with better balance between survival outcomes. Add appropriate statistical tests: t-tests or Mann-Whitney U tests for comparing group means, AUC-ROC analysis to quantify predictive performance, and confidence intervals for effect sizes.
- [MAJOR] (rigor) The paper acknowledges in its limitations that a falsification control was not implemented (comparing founder fade curves to non-founder contributor trajectories), but this control is essential for establishing that the observed effect is founder-specific rather than a general property of high-activity contributors' trajectories.
  Action: Implement the falsification control: for each project, extract the trajectory of a randomly selected high-activity non-founder contributor and compute the same trajectory descriptors. Test whether founder trajectories predict survival significantly better than non-founder trajectories.
- [MINOR] (scope) While the paper identifies important limitations, the generalizability claims are premature given the synthetic nature of the data. The findings may not transfer to real OSS ecosystems with diverse governance models, contribution patterns, and project types.
  Action: In the empirical validation phase, ensure diversity in the dataset: include projects of different sizes, ages, domains (libraries vs applications), and governance models (BDFL, meritocratic, foundation-backed). Analyze whether the relationship holds across these subgroups.
- [MINOR] (novelty) While the scaffolding-with-fading analogy is creative, the core methodology of analyzing temporal trajectories of contributor involvement has precedent in the cited PRIME tool and other longitudinal studies. The novelty would be stronger if demonstrated with empirical data showing insights beyond what existing temporal metrics provide.
  Action: Clearly differentiate the contribution from prior longitudinal work by showing: 1) founder-specific insights beyond aggregate metrics, 2) practical implications for founder succession planning, and 3) validation that trajectory features add predictive value beyond what longitudinal bus factor or contributor count trends provide.
</previous_review>

<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 19:16:46 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-research-tools · 2026-08-21 19:17:18 UTC

The agent loaded the **aii-web-research-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-research-tools
description: "Runs multi-source web research campaigns — literature reviews, deep cross-verification of many claims or citations, paper and PDF mining — by escalating WebSearch for discovery, WebFetch for the gist, then aii_web_tools__fetch_grep for exact regex extraction with context windows over HTML or PDFs. Use whenever a task needs far more than a handful of lookups: comprehensive or deep research, surveying a field, cross-referencing sources against each other, or checking many references at once. Triggers: literature review, comprehensive or extensive or deep research, survey the field, multi-source investigation, verify many citations, arXiv paper mining. NOT for: a single quick lookup, which raw WebSearch and WebFetch already handle; NOT for the script-level search, fetch, and grep tooling or running without built-in web tools — use aii-web-tools; NOT for fetching BibTeX into references.bib (use aii-semscholar-bib) or judging whether a draft's claims hold up (use amg-paper-verification)."
---

## Available Web Tools

Three levels of web tools:

1. **WebSearch** — broad discovery. Returns titles, URLs, snippets. Cheapest. Use first to scan the landscape.
2. **WebFetch** — read a specific page. LLM summarizes it. HTML only. May miss specific details.
3. **aii_web_tools__fetch_grep** — exact text extraction from HTML or PDF. Regex matching with context windows.
   Use for precise details, methodology, or when WebFetch missed something.
   Key params: pattern (required), max_matches (default 20), context_chars (default 200 per side).

**Workflow:** WebSearch → WebFetch for gist → aii_web_tools__fetch_grep for exact details or PDFs.

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-research-tools"
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````
