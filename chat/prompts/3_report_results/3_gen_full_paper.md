# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 20:36:03 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: >-
  Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
abstract: >-
  Open-source software (OSS) projects that lose their founder face a high risk of collapse, yet existing risk metrics rely
  on static snapshots — contributor counts, bus factors, and project age — measured at the moment of departure. We propose
  that the **shape** of the founder's involvement trajectory across the project's entire lifespan is a stronger predictor
  of post-departure survival: projects whose founder's share of commits, merges, and code reviews declined smoothly over time
  ("scaffolding fade") are more likely to survive than those whose founder maintained high involvement until an abrupt exit.
  To test this hypothesis, we present a complete methodological framework for empirical validation including founder-specific
  trajectory extraction, rigorous statistical testing with effect sizes, falsification controls comparing founder vs. non-founder
  trajectories, and diversity considerations across project characteristics. We validate the framework's correctness using
  synthetically generated data that matches structural properties of real OSS projects, demonstrating pipeline readiness for
  empirical testing on real GitHub repositories. This work shifts OSS sustainability assessment from static headcount metrics
  to dynamic trajectory analysis, providing both a diagnostic tool for risk assessment and a prescriptive guideline for founder
  succession planning.
paper_text: "# Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation\n\
  \n## Abstract\n\nOpen-source software (OSS) projects that lose their founder face a high risk of collapse, yet existing\
  \ risk metrics rely on static snapshots — contributor counts, bus factors, and project age — measured at the moment of departure.\
  \ We propose that the **shape** of the founder's involvement trajectory across the project's entire lifespan is a stronger\
  \ predictor of post-departure survival: projects whose founder's share of commits, merges, and code reviews declined smoothly\
  \ over time (\"scaffolding fade\") are more likely to survive than those whose founder maintained high involvement until\
  \ an abrupt exit. To test this hypothesis, we present a complete methodological framework for empirical validation including\
  \ founder-specific trajectory extraction, rigorous statistical testing with effect sizes, falsification controls comparing\
  \ founder vs. non-founder trajectories, and diversity considerations across project characteristics. We validate the framework's\
  \ correctness using synthetically generated data that matches structural properties of real OSS projects, demonstrating\
  \ pipeline readiness for empirical testing on real GitHub repositories. This work shifts OSS sustainability assessment from\
  \ static headcount metrics to dynamic trajectory analysis, providing both a diagnostic tool for risk assessment and a prescriptive\
  \ guideline for founder succession planning.\n\n## Introduction\n\nOpen-source software underpins critical global infrastructure:\
  \ operating systems, web servers, programming language runtimes, and data-science libraries all depend on volunteer communities\
  \ coordinated around one or two principal developers. When these founders step away, the consequences can be severe. Empirical\
  \ studies estimate that 16% of OSS projects experience the detachment of all their \"truck-factor\" developers — the minimal\
  \ set whose simultaneous departure would impair the project — and only 41% of those projects survive the event by attracting\
  \ new core contributors [1]. The remaining majority collapse into inactivity, leaving downstream dependents without maintenance.\n\
  \nThe standard approach to measuring this risk is **static**: count the number of active contributors, compute the bus factor,\
  \ measure project age and popularity, and evaluate all of these at the moment of departure. This state-based framing has\
  \ two limitations. First, it treats the founder's departure as a binary event — present or absent — ignoring the empirically\
  \ observed reality that most founders remain partially involved for an extended period before fully disengaging [1]. Second,\
  \ it cannot distinguish between a project where the founder gradually transferred decision-making authority to the community\
  \ and one where the founder held all power until a sudden exit, even though these two scenarios should produce very different\
  \ survival outcomes.\n\nWe address this gap by importing an established mechanism from educational psychology: **scaffolding\
  \ with fading** [8, 9]. In the learning sciences, a tutor provides structured support that is gradually withdrawn (\"fading\"\
  ) as the learner internalizes the necessary skill; abrupt removal of support before competence matures causes collapse.\
  \ We hypothesize that the same mechanism operates in OSS: a founder who gradually reduces their share of commits, merges,\
  \ and code reviews signals that the contributor community is being scaffolded into caretaker capability. A founder who maintains\
  \ high involvement until a sudden exit leaves the community unprepared, and the project collapses.\n\nOur contribution is\
  \ a complete methodological framework for testing this hypothesis that directly addresses limitations in prior work:\n\n\
  - **Founder involvement trajectory as a quantitative predictor.** We operationalize the founder's monthly share of commits,\
  \ merges, and code reviews from project inception to departure as a time series, and derive shape descriptors (slope, fade\
  \ index, duration) that capture the \"scaffolding fade\" hypothesis.\n- **Founder-specificity with falsification controls.**\
  \ We implement trajectory-shuffling controls and compare founder trajectories against trajectories of randomly selected\
  \ non-founder contributors to establish that the mechanism is founder-specific rather than a general property of contributor\
  \ activity.\n- **Rigorous statistical evaluation.** We provide effect sizes, confidence intervals, and appropriate statistical\
  \ tests (Mann-Whitney U, logistic regression with cross-validation) to move beyond descriptive statistics.\n- **Empirical\
  \ validation pathway.** We outline a concrete plan for collecting real GitHub data with verified founder departures, addressing\
  \ sample size, diversity, and generalizability concerns from prior work.\n- **Cross-domain mechanism validation.** We connect\
  \ the educational psychology concept of scaffolding with fading to the founder-community dynamic in OSS, providing theoretical\
  \ grounding beyond descriptive correlations.\n\n[FIGURE:fig1]\n\nThe rest of this paper proceeds as follows. Section 2 reviews\
  \ related work on OSS survival, truck factor, and contributor disengagement. Section 3 describes our methodology for founder\
  \ identification, trajectory extraction, and survival labeling. Section 4 presents results from synthetic validation demonstrating\
  \ the framework's readiness for empirical testing. Section 5 discusses implications, limitations, and the path to empirical\
  \ validation. Section 6 concludes.\n\n## Related Work\n\n**Open-source abandonment and survival.** The foundational study\
  \ by Avelino et al. [1] defines truck-factor-developer detachment (TFDD) and finds that 41% of projects survive their last\
  \ observed TFDD by attracting new core contributors. Surviving projects tend to be younger at the time of TFDD, but no significant\
  \ differences emerge in developer count, commit volume, or file count at the detachment moment. This null result on static\
  \ features motivates our shift to dynamic trajectory analysis. Kamei et al. [2] apply survival analysis to developer turnover\
  \ in industrial open-source projects, finding that turnover patterns predict project longevity, but again using aggregate\
  \ counts rather than per-developer trajectories.\n\n**Truck factor and bus factor estimation.** The truck factor (equivalent\
  \ to the bus factor) measures the minimal number of developers whose departure would impair a project. Multiple algorithms\
  \ have been proposed for estimating it, ranging from commit-share thresholds to code-ownership graphs. All of these approaches\
  \ produce a single number at a single point in time. Longitudinal evaluation of bus factor has been explored, demonstrating\
  \ that temporal metrics reveal trends invisible to snapshots — a methodological precedent for our approach [4].\n\n**Contributor\
  \ disengagement.** Prior work has used difference-in-differences designs across large numbers of repositories to estimate\
  \ the impact of core contributor disengagement on pull-request throughput, finding that the impact varies with the disengaging\
  \ developer's static commit-share and tenure. This study measures post-departure throughput decline rather than binary survival,\
  \ and focuses on aggregate core contributors rather than the founder specifically. Our work complements it by targeting\
  \ the founder's unique role and by using the full pre-departure trajectory as a predictor.\n\n**Project lifecycle and death\
  \ spirals.** Kaushik and Chahal [6] identify a \"death spiral\" in inactive open-source projects: aggregate pull-request\
  \ workflow signals (friction, backlog growth, falling innovation, rising merge latency) deteriorate in a self-reinforcing\
  \ loop after decline begins. Their analysis models community-level dynamics after the decline has started and does not analyze\
  \ the founder. Our approach models the founder-specific trajectory before departure and predicts survival before the decline\
  \ becomes visible in aggregate metrics.\n\n**Project initiator effects.** Prior work has studied how project initiators\
  \ influence open-source success, finding that initiator characteristics matter for project growth. However, this work does\
  \ not model the initiator's involvement trajectory over time or its relationship to post-departure survival.\n\n**Scaffolding\
  \ theory.** The concept of scaffolding with fading originates in Vygotsky's zone of proximal development [7] and was operationalized\
  \ by Wood, Bruner, and Ross [8] as a measurable tutoring mechanism: the tutor's support is systematically reduced as the\
  \ learner's competence grows. The cross-domain transfer to open-source software — treating the founder's involvement as\
  \ scaffolding and predicting post-departure survival from the shape of the fade — has not been previously operationalized\
  \ in the software engineering literature.\n\n## Method\n\n### Dataset Collection Plan\n\nTo properly test the scaffolding-fade\
  \ hypothesis, we propose collecting an empirical dataset of real GitHub repositories with verified founder departures. Our\
  \ data collection procedure follows:\n\n1. **Founder identification:** We identify the founder as the user with the earliest\
  \ sustained commit activity on the repository, typically the repository creator. This approach is validated against CODEOWNERS\
  \ files and initial commit analysis where available.\n\n2. **Founder departure detection:** We define founder departure\
  \ as 12+ months of inactivity in commits, merges, and reviews, consistent with abandonment-threshold literature [1] and\
  \ allowing sufficient time to observe post-departure survival outcomes.\n\n3. **Survival labeling:** Following Avelino et\
  \ al. [1], we label a project as survived if it attracts new core contributors (defined as contributors achieving truck-factor\
  \ status) after the founder's departure window, or alternatively measures continuous activity via the ratio of post-departure\
  \ to pre-departure commit volume.\n\n4. **Diversity sampling:** We ensure representation across:\n   - Project sizes (small:\
  \ <10 contributors, medium: 10-50, large: >50)\n   - Ages (young: <2 years, medium: 2-5 years, old: >5 years)\n   - Domains\
  \ (libraries, frameworks, applications, devops tools)\n   - Governance models (BDFL, meritocratic, foundation-backed, corporate)\n\
  \   - Primary languages (Python, JavaScript, Go, Rust, Java, etc.)\n\n### Target Dataset Characteristics\n\nBased on power\
  \ analysis for detecting medium effect sizes (Cohen's d = 0.5) with 80% power and alpha = 0.05, we target a minimum of 100\
  \ projects with balanced survival outcomes (approximately 50 survived, 50 collapsed) to enable robust statistical analysis\
  \ and subgroup investigations.\n\n### Data Extraction\n\nFor each qualifying project, we extract:\n\n- **Founder involvement\
  \ trajectory:** Monthly time series from project inception to founder departure, measuring the founder's share of (a) commits\
  \ authored, (b) pull requests merged, and (c) code reviews participated in, using the GitHub REST API with pagination handling.\n\
  \n- **Static features at departure:** Bus factor (calculated as the minimum number of contributors contributing 50% of commits),\
  \ total contributor count, project age in months, GitHub star count, and file count.\n\n- **Survival labels:** Binary survival\
  \ label (survived/collapsed) based on sustained non-founder activity post-departure, and a continuous survival metric defined\
  \ as the ratio of post-departure total commits to the pre-departure baseline.\n\n### Trajectory Descriptors\n\nFrom each\
  \ founder involvement trajectory, we compute the following shape descriptors:\n\n1. **Slope:** The linear regression coefficient\
  \ of founder share over time (per month). A negative slope indicates declining involvement; a slope near zero indicates\
  \ a flat plateau.\n\n2. **Fade index:** The normalized total decline, computed as $(s_0 - s_T) / s_0$, where $s_0$ is the\
  \ founder's initial share and $s_T$ is the final share before departure. Values range from 0 (no decline) to 1 (complete\
  \ withdrawal).\n\n3. **Duration:** The number of months from project inception to founder departure, capturing the timescale\
  \ over which the fade occurs.\n\n4. **Time-to-onset:** The month index where decline begins (first month where share drops\
  \ below 90% of peak), capturing when the founder started reducing involvement.\n\n5. **Abrupt-cliff indicator:** Binary\
  \ indicator if any month shows a sharp drop (>25% decline from previous month), capturing sudden withdrawal.\n\n6. **Plateau-then-cliff\
  \ indicator:** Binary indicator if there was a stable period (CV < 0.1 for 3+ months) followed by a sharp drop, capturing\
  \ delayed abrupt withdrawal.\n\nWe compute these descriptors for each of the three activity channels (commits, merges, reviews),\
  \ yielding 18 trajectory features total (including initial and final share).\n\n### Baseline Features\n\nFor comparison,\
  \ we evaluate conventional static features computed at the moment of founder departure: bus factor, contributor count, project\
  \ age, star count, and file count. These represent the state-of-the-art in OSS risk assessment [1, 3].\n\n### Analysis Approach\n\
  \nOur analysis follows a rigorous statistical framework to address prior limitations:\n\n1. **Descriptive statistics:**\
  \ Means, standard deviations, and distributions grouped by survival outcome.\n\n2. **Statistical significance testing:**\
  \ \n   - Mann-Whitney U tests for comparing group distributions (non-parametric, suitable for non-normal distributions)\n\
  \   - Effect sizes reported as Cohen's d with 95% confidence intervals\n   - Bonferroni correction for multiple comparisons\
  \ where appropriate\n\n3. **Predictive modeling:**\n   - Logistic regression with stratified 5-fold cross-validation\n \
  \  - Performance metrics: AUC-ROC, F1-score, precision, recall, accuracy\n   - 95% confidence intervals via bootstrapping\
  \ (1000 iterations)\n   - Comparison of trajectory-only, static-only, and combined models\n\n4. **Falsification controls:**\n\
  \   - **Trajectory shuffling:** For each project, randomly permute the monthly founder-share time series to destroy temporal\
  \ order while preserving distribution\n   - **Founder-specificity control:** For each project, extract trajectory of a randomly\
  \ selected high-activity non-founder contributor (matched for activity level) and compute identical trajectory descriptors\n\
  \   - Permutation-based feature importance to quantify each feature's contribution to predictive power\n\n5. **Subgroup\
  \ analysis:** \n   - Test robustness across project characteristics (size, age, domain, governance)\n   - Interaction effects\
  \ between trajectory features and static context\n   - Survival analysis using Kaplan-Meier estimation and Cox proportional\
  \ hazards models\n\n6. **Power analysis:** Post-hoc power analysis to confirm adequate sample size for detected effects.\n\
  \nThis framework directly addresses the reviewer concerns by:\n- Replacing synthetic data with plans for empirical data\
  \ collection\n- Ensuring adequate sample size (100+ projects) for statistical power\n- Implementing comprehensive statistical\
  \ testing with effect sizes\n- Including founder-specificity falsification controls\n- Addressing generalizability through\
  \ diverse sampling\n- Differentiating from prior work by focusing on founder-specific trajectories rather than aggregate\
  \ metrics\n\n[FIGURE:fig2]\n\n## Results\n\nSince this paper presents a methodological framework for empirical validation\
  \ rather than final empirical results, we describe the expected outcomes and validation approach that will be used when\
  \ applying this framework to real data.\n\n### Expected Survival Outcomes\n\nBased on Avelino et al.'s [1] findings, we\
  \ expect approximately 40% of projects with founder TFDD to survive by attracting new core contributors. Surviving projects\
  \ should maintain post-departure activity levels comparable to pre-departure baselines (survival metric ≈ 1.0), while collapsed\
  \ projects should show significant activity reduction (survival metric < 0.3).\n\n[FIGURE:fig2]\n\n### Expected Founder\
  \ Involvement Trajectories\n\nWe hypothesize distinct trajectory patterns between survival outcomes:\n\n- **Surviving projects:**\
  \ Gradual, sustained decline in founder share over an extended period (\"scaffolding fade\"), characterized by:\n  - Moderate\
  \ negative slope (e.g., -0.01 to -0.03 per month)\n  - High fade index (0.5-0.8) indicating substantial but not complete\
  \ withdrawal\n  - Extended duration (12+ months) allowing time for capability transfer\n  - Low probability of abrupt-cliff\
  \ indicators\n  - Moderate time-to-onset (decline begins early in project lifecycle)\n\n- **Collapsed projects:** Either\
  \ prolonged high involvement followed by abrupt exit, or premature complete withdrawal:\n  - Either near-zero slope until\
  \ sudden drop (plateau-then-cliff pattern)\n  - Or steep negative slope throughout (abrupt decline pattern)\n  - Higher\
  \ probability of abrupt-cliff or plateau-then-cliff indicators\n  - Potentially shorter duration before departure\n\n[FIGURE:fig3]\n\
  \n### Expected Statistical Comparisons\n\nWe anticipate the following statistical patterns when applying our framework to\
  \ empirical data:\n\n1. **Trajectory features:** Significant differences between survival groups for:\n   - Slope: Surviving\
  \ projects showing less negative slopes (more gradual decline)\n   - Fade index: Surviving projects showing moderate values\
  \ (balanced withdrawal)\n   - Abrupt-cliff indicator: Higher prevalence in collapsed projects\n   - Time-to-onset: Earlier\
  \ onset in surviving projects\n   - Effect sizes: Cohen's d > 0.5 for key trajectory features\n\n2. **Static features:**\
  \ Continued relevance but reduced dominance compared to synthetic settings:\n   - Contributor count: Significant but smaller\
  \ effect size (d ≈ 0.8)\n   - Bus factor: Moderate predictive value\n   - Project age, star count: Weaker predictors when\
  \ controlling for other factors\n\n3. **Predictive performance:** \n   - Trajectory-only model: AUC significantly > 0.6\
  \ (target: 0.70-0.80)\n   - Static-only model: AUC significantly > 0.6 (target: 0.65-0.75)\n   - Combined model: AUC significantly\
  \ > either alone (target: 0.75-0.85)\n   - Statistical significance: p < 0.05 for AUC differences via DeLong's test\n\n\
  4. **Falsification control outcomes:**\n   - Trajectory-shuffled features: Performance at or below chance level (AUC ≈ 0.50)\n\
  \   - Non-founder trajectories: Significantly lower predictive power than founder trajectories\n   - Founder-specificity:\
  \ Significant difference in AUC between founder and matched non-founder trajectories (p < 0.05)\n\n### Expected Subgroup\
  \ Patterns\n\nWe anticipate the relationship to hold across project characteristics with some variation:\n\n- **By project\
  \ size:** Stronger trajectory effects in medium-sized projects (10-50 contributors) where founder influence is balanced\
  \ with community capacity\n- **By age:** Consistent effects across age groups, potentially stronger in established projects\
  \ (>2 years)\n- **By domain:** Observable effects across libraries, applications, and infrastructure projects\n- **By governance:**\
  \ Particularly relevant in BDFL and meritocratic models where founder influence is pronounced\n\n### Validation of Framework\
  \ Readiness\n\nTo demonstrate our framework's readiness for empirical testing, we have implemented and validated the complete\
  \ analytical pipeline on synthetic data that matches structural properties of real OSS projects. This validation confirms:\n\
  \n1. **Trajectory extraction:** Correct computation of all 18 descriptor types from time series data\n2. **Statistical tests:**\
  \ Proper calculation of Mann-Whitney U statistics, p-values, and effect sizes\n3. **Predictive modeling:** Stable cross-validation\
  \ performance with confidence intervals\n4. **Falsification controls:** Trajectory shuffling reduces performance below chance;\
  \ permutation importance identifies informative features\n5. **Subgroup analysis:** Proper handling of class imbalance cases\n\
  6. **Survival analysis:** Kaplan-Meier and Cox models produce hazard ratios and p-values\n\nThe synthetic validation (shown\
  \ in the appended results section) demonstrates that our framework correctly identifies when temporal features lack predictive\
  \ power (as designed in the synthetic data) and is prepared to detect genuine signals when present in empirical data.\n\n\
  [FIGURE:fig4]\n\n## Discussion\n\n### Implications for OSS Sustainability\n\nIf validated on empirical data, our findings\
  \ would have significant implications for open-source sustainability:\n\n1. **Risk assessment paradigm shift:** Moving from\
  \ static snapshot metrics (contributor count, bus factor) to dynamic trajectory analysis would provide earlier and more\
  \ accurate warnings of founder departure risks.\n\n2. **Founder succession planning:** The scaffolding-fade hypothesis provides\
  \ a quantitative guideline for founders: gradual reduction of involvement over 12+ months predicts better survival outcomes\
  \ than abrupt exit or prolonged high involvement.\n\n3. **Ecosystem intervention:** Funders and maintainer organizations\
  \ could evaluate founder trajectories when triaging at-risk projects, prioritizing those with healthy fade patterns for\
  \ support.\n\n4. **Contributor development:** Projects could use founder trajectory data to identify when community members\
  \ are ready for increased responsibility, enabling targeted mentorship and gradual authority transfer.\n\n### Addressing\
  \ Reviewer Concerns\n\nOur methodological framework directly addresses all major criticisms from prior work:\n\n1. **Empirical\
  \ data requirement:** We explicitly outline a plan for collecting real GitHub data with verified founder departures, moving\
  \ beyond synthetic validation.\n\n2. **Statistical rigor:** Our framework includes appropriate statistical tests (Mann-Whitney\
  \ U, Cohen's d with CIs), power analysis for sample size justification, and correction for multiple comparisons.\n\n3. **Founder-specificity:**\
  \ The falsification control comparing founder vs. non-founder trajectories is a core component of our framework, essential\
  \ for establishing that the mechanism is founder-specific rather than a general property of contributor activity.\n\n4.\
  \ **Generalizability:** Our diversity sampling plan ensures representation across project sizes, ages, domains, and governance\
  \ models, with explicit subgroup analysis to test robustness.\n\n5. **Novelty beyond prior longitudinal work:** While extending\
  \ the PRIME tool's longitudinal approach, we focus specifically on founder-specific trajectories rather than aggregate metrics,\
  \ and we connect the mechanism to the established educational psychology theory of scaffolding with fading.\n\n### Limitations\
  \ of Current Validation\n\nIt is important to note that our current validation uses synthetic data, which by design cannot\
  \ capture the social mechanisms underlying the scaffolding-fade hypothesis. The synthetic validation serves only to demonstrate\
  \ framework correctness, not to test the hypothesis itself. This limitation is explicitly acknowledged and forms the basis\
  \ for our clear path to empirical validation.\n\n### Comparison to Prior Work\n\nOur approach makes several distinct contributions\
  \ beyond existing literature:\n\n- **Vs. Avelino et al. [1]:** We model the dynamic trajectory of founder involvement over\
  \ the entire pre-departure lifespan rather than static snapshots at departure, and we focus specifically on the founder\
  \ rather than the anonymous set of key developers.\n\n- **Vs. PRIME tool [6]:** While both use longitudinal metrics, we\
  \ apply them specifically to founder involvement shares rather than aggregate project metrics, and we test a specific social\
  \ mechanism (scaffolding-fade) rather than general process monitoring.\n\n- **Vs. Kaushik and Chahal [10]:** We model founder-specific\
  \ behavior before departure to predict survival, whereas they analyze aggregate community dynamics after decline has begun\
  \ to understand project mortality.\n\n- **Vs. Chen et al. [7]:** We predict binary survival outcomes rather than continuous\
  \ throughput decline, and we focus on the founder's unique role rather than aggregate core contributors.\n\n- **Vs. Scaffolding\
  \ theory [12,13]:** We operationalize the educational psychology concept of scaffolding with fading in the OSS context,\
  \ providing a quantitative predictor of survival based on the shape of founder involvement decay.\n\n### Path Forward\n\n\
  The immediate next step is to apply this framework to an empirical dataset of real GitHub repositories. This involves:\n\
  \n1. **Data collection:** Implementing the GitHub API-based collector for founder trajectories and survival labels\n2. **Quality\
  \ assurance:** Validating founder identification and departure detection against known cases\n3. **Analysis execution:**\
  \ Running the complete statistical framework described above\n4. **Result interpretation:** Evaluating whether the scaffolding-fade\
  \ hypothesis holds on real data\n5. **Publication:** Reporting empirical findings with appropriate statistical rigor\n\n\
  If the hypothesis is validated empirically, this work would provide both a diagnostic tool for OSS risk assessment and a\
  \ prescriptive guideline for founder succession planning, potentially improving the sustainability of critical open-source\
  \ infrastructure.\n\n## Conclusion\n\nWe have presented a complete methodological framework for testing the hypothesis that\
  \ the shape of a founder's involvement trajectory across an open-source project's lifespan predicts post-departure survival.\
  \ Our framework directly addresses limitations in prior work by:\n\n1. **Planning for empirical validation:** Outlining\
  \ a concrete procedure for collecting real GitHub data with verified founder departures\n2. **Ensuring statistical rigor:**\
  \ Including appropriate statistical tests, effect sizes, confidence intervals, and power analysis\n3. **Establishing founder-specificity:**\
  \ Implementing falsification controls that compare founder trajectories against non-founder contributor trajectories\n4.\
  \ **Addressing generalizability:** Planning for diverse sampling across project characteristics with explicit subgroup analysis\n\
  5. **Differentiating from prior work:** Focusing on founder-specific trajectories rather than aggregate metrics, and grounding\
  \ the mechanism in established educational psychology theory\n\nWhile we validate the framework's correctness using synthetic\
  \ data, we explicitly acknowledge that synthetic data cannot capture the social mechanisms underlying the scaffolding-fade\
  \ hypothesis. The true test will come from applying this framework to empirical data from real GitHub repositories.\n\n\
  If validated on empirical data, the scaffolding-fade hypothesis would shift open-source risk assessment from static headcount\
  \ snapshots to dynamic trajectory analysis, suggesting that maintainers should consciously decay their involvement as a\
  \ survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk\
  \ projects. The framework provided here enables that critical test.\n\n[FIGURE:fig4]\n\n---\n\n\\bibliographystyle{plainnat}\n\
  \\bibliography{references}"
summary: >-
  This paper presents a methodological framework for testing the hypothesis that the shape of a founder's involvement trajectory
  predicts open-source project survival after founder departure. It addresses key limitations in prior work by planning for
  empirical validation with proper statistical rigor, founder-specificity controls, and diversity considerations. The framework
  is validated on synthetic data to demonstrate readiness for empirical testing on real GitHub repositories.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig2
figure_type: data
title: Expected Post-Departure Activity Levels
caption: >-
  Expected difference in post-departure activity levels between surviving and collapsed open-source projects. Surviving projects
  maintain activity near pre-departure baselines, while collapsed projects show severe activity reduction.
image_gen_detailed_description: >-
  Vertical bar chart. X-axis categories: 'Surviving Projects', 'Collapsed Projects'. Y-axis label: 'Post-Departure Activity
  Level (% of Pre-Departure Baseline)', range 0-120. Bar values: Surviving Projects = 100%, Collapsed Projects = 25%. Error
  bars: Surviving Projects ±10% (showing 90-110% range), Collapsed Projects ±5% (showing 20-30% range). Bar colors: Surviving
  Projects = green (#4CAF50), Collapsed Projects = red (#F44336). Y-axis grid lines at 25, 50, 75, 100. X-axis labels centered
  under each bar. Chart title positioned above plot area.
aspect_ratio: '21:9'
summary: >-
  Shows expected activity levels: surviving projects maintain ~100%, collapsed drop to ~25%
figure_path: figures/fig2_v0.pdf

--- Item 2 ---
id: fig3
figure_type: data
title: Expected Founder Involvement Trajectories
caption: >-
  Expected founder involvement trajectories for surviving versus collapsed projects. Surviving projects show gradual decline
  over time, while collapsed projects maintain high involvement until abrupt exit.
image_gen_detailed_description: >-
  Line chart with two trajectories. X-axis: 'Time (Months from Project Inception)', range 0-30. Y-axis: 'Founder Involvement
  Share (%)', range 0-100. Trajectory 1 - Surviving Projects: Starts at (0, 70), declines linearly to (24, 30), continues
  to (30, 25). Trajectory 2 - Collapsed Projects: Flat at 70% from months 0-20, then sharp drop to (22, 15) and (30, 5). Line
  styles: Surviving Projects = solid blue line (width 3px), Collapsed Projects = dashed red line (width 3px). Data points
  marked with circles (blue for surviving, red for collapsed). Legend positioned at top-right: 'Surviving Projects' (blue
  solid line), 'Collapsed Projects' (red dashed line). Grid lines: light gray every 10 units on both axes. Chart area has
  white background with thin black border.
aspect_ratio: '21:9'
summary: >-
  Surviving projects show gradual decline, collapsed projects show abrupt drop after prolonged high involvement
figure_path: figures/fig3_v0.pdf

--- Item 3 ---
id: fig4
figure_type: concept
title: Methodological Framework for Empirical Validation
caption: >-
  Complete analytical pipeline for testing the scaffolding-fade hypothesis, including trajectory extraction, statistical testing,
  falsification controls, and subgroup analysis.
image_gen_detailed_description: >-
  Horizontal flowchart diagram showing five main stages with arrows connecting them. Stage 1: 'Data Collection' (GitHub API
  → Founder identification → Trajectory extraction [18 features] → Static features [5 items]) represented as a cylinder/input
  symbol. Stage 2: 'Analysis Pipeline' with three parallel processes: Statistical Tests (Mann-Whitney U, Cohen's d, confidence
  intervals), Predictive Modeling (Logistic regression, AUC-ROC, F1-score with 5-fold CV), and Falsification Controls (Trajectory
  shuffling, Founder vs Non-founder comparison). Stage 3: 'Subgroup Analysis' (by size, age, domain, governance). Stage 4:
  'Survival Analysis' (Kaplan-Meier, Cox proportional hazards). Stage 5: 'Results Interpretation' (Evidence for/against hypothesis,
  Effect sizes, Practical implications). Arrows flow left to right connecting all stages. Each stage represented as a rounded
  rectangle with light blue background and dark blue border. Text labels inside each rectangle in 10pt sans-serif. Arrows
  are solid lines with arrowheads. Overall width 800px, height 400px. Clean white background.
aspect_ratio: '21:9'
summary: >-
  Shows the complete analytical pipeline from data collection to results interpretation
figure_path: figures/fig4_v0.jpg
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 20:36:03 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-21 20:36:45 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: "Assembles and compiles a LaTeX paper into paper.pdf: documentclass and package preamble, figure floats that includegraphics pre-generated vector .pdf and .jpg files, float-placement and width rules, and the required pdflatex, bibtex, pdflatex, pdflatex run sequence. Use whenever pre-written text and pre-generated figures must become a compiled PDF, and whenever a build misbehaves — citations printing as question marks, figures drifting to the end or above the title, shrunken axis labels, undefined references. Triggers: latex, tex, pdflatex, bibtex, natbib, includegraphics, figure float, htbp, compile or build the paper, paper.tex, paper.pdf. NOT for: writing the paper's text or deciding its structure (use aii-paper-writing), creating the figure images (aii-data-fig-gen, aii-concept-fig-gen), or fetching bibliography entries (use aii-semscholar-bib); NOT for reshaping a PDF that already exists — merging, splitting, form filling, table extraction (use anthropic-pdf)."
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. This document class is ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt either way) and gains nothing, while restricting the float
  to a page top
- ALWAYS constrain with `width` and `keepaspectratio`. Add `height` only as a
  LAST RESORT against a very tall figure overrunning the page, and keep it
  generous — `0.85\textheight`. A tight height cap binds on ordinary figures
  and LaTeX then shrinks the TEXT with them: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt.
  The figure generator measures legibility at the figure's OWN size, so it
  cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 20:36:45 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and writes the result into references.bib, with a mandatory web-search fallback for anything not found. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX first. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [5] SKILL-INPUT — aii-web-research-tools · 2026-08-21 20:37:22 UTC

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
