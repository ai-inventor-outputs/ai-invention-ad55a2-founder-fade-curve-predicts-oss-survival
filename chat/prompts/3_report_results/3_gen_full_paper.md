# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 03:05:41 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
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
  The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
abstract: >-
  Open-source projects frequently depend on a single founder, yet little is known about how the shape of that founder's involvement
  over time affects whether the project survives their departure. We introduce the founder fade curve — a quantitative descriptor
  of the trajectory of a founder's monthly share of commits prior to leaving — and test whether its shape predicts post-departure
  survival beyond static snapshot measures such as bus factor and contributor count. We evaluate a pilot cohort of 14 curated
  GitHub repositories with documented founder departures (7 survived, 7 collapsed). Static features achieve strong predictive
  performance, while trajectory shape descriptors alone perform below chance. A combined model reaches the highest accuracy,
  but the net reclassification improvement is negative, indicating that adding shape features does not improve classification.
  Bootstrap power analysis estimates a minimum of 100 projects for 80% power to detect the observed effect size. Synthetic
  validation confirms that our descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff
  patterns across 30 synthetic trajectories. A falsification control using non-founder trajectories yields identical performance,
  finding no founder-specific effect. These results indicate that, at pilot scale, fade-curve shape does not yet add predictive
  value above static measures — a finding that calls for larger-scale validation using full trajectory data from GH Archive
  or equivalent sources.
paper_text: |-
  # The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival

  ## Abstract

  Open-source projects frequently depend on a single founder, yet little is known about how the *shape* of that founder's involvement over time affects whether the project survives their departure. We introduce the founder fade curve — a quantitative descriptor of the trajectory of a founder's monthly share of commits prior to leaving — and test whether its shape predicts post-departure survival beyond static snapshot measures such as bus factor and contributor count. We evaluate a pilot cohort of 14 curated GitHub repositories with documented founder departures (7 survived, 7 collapsed). Static features achieve strong predictive performance, while trajectory shape descriptors alone perform below chance. A combined model reaches the highest accuracy, but the net reclassification improvement is negative, indicating that adding shape features does not improve classification. Bootstrap power analysis estimates a minimum of 100 projects for 80% power to detect the observed effect size. Synthetic validation confirms that our descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff patterns across 30 synthetic trajectories. A falsification control using non-founder trajectories yields identical performance, finding no founder-specific effect. These results indicate that, at pilot scale, fade-curve shape does not yet add predictive value above static measures — a finding that calls for larger-scale validation using full trajectory data from GH Archive or equivalent sources.

  ## 1. Introduction

  Open-source software underpins global critical infrastructure. Git, the Linux kernel, Python's standard library, and thousands of widely used packages are all maintained by communities that often trace back to one or two founding developers. When such a founder departs — whether through burnout, career change, or simple exhaustion — the project faces a fork in the road: it either survives, attracting new caretakers, or it collapses into inactivity.

  The dominant framework for measuring this risk is the Truck Factor Developer Detachment (TFDD) model [1]. TFDD defines a project's truck factor as the minimal number of developers whose simultaneous departure would critically impair the project, and identifies the moment all truck-factor developers leave as the detachment event. Projects that subsequently attract at least one new truck-factor developer are classified as surviving; others are classified as collapsed. Across 1,932 popular GitHub projects, 57% have a truck factor of 1, 16% experience a TFDD, and only 41% of detached projects survive [1]. A later study of 36,464 projects found even higher detachment rates (89%) but lower survival (27%), and reported that departures occurring early in a project's life are less likely to be survived [2].

  Yet static measures — how many key developers there are at the moment of departure — explain surprisingly little of the variation in survival outcomes. Projects that survive their TFDD often have *fewer* developers, commits, and files than those that collapse [1]. This paradox suggests that something beyond a snapshot of contributor count matters.

  We hypothesize that the *shape* of the founder's involvement trajectory over the project's entire pre-departure lifespan may complement static measures in predicting survival. Specifically, we propose that a "scaffolding fade" — a gradual, sustained decline in the founder's share of commits over an extended pre-departure window — signals that the contributor community has had time to internalize decision-making capability. By contrast, an abrupt cliff (high involvement maintained until sudden exit) or a flat plateau ending in a sharp drop may predict collapse. This hypothesis imports an established educational mechanism: scaffolding with fading, in which a more capable tutor gradually withdraws support as the learner internalizes the necessary skill [10]. Sudden removal of support before competence matures causes collapse; gradual withdrawal allows competence to consolidate.

  In this paper we present the first quantitative evaluation of the founder fade curve hypothesis. Our contributions are:

  1. **A trajectory-shape descriptor pipeline** that extracts nine features from a founder's monthly involvement share time series, including slope, convexity, onset of decline, cliff indicator, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).
  2. **A synthetic validation** demonstrating that the descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff patterns across 30 synthetic trajectories \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/experiment-1}}.
  3. **A pilot empirical evaluation** on 14 curated GitHub repositories with documented founder departures (7 survived, 7 collapsed), comparing predictive performance of trajectory shape descriptors, static features, and their combination .
  4. **Bootstrap confidence intervals and power analysis** showing that the pilot is underpowered and that a minimum of 100 projects is needed for 80% power to detect the observed effect size \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/evaluation-1}}.
  5. **A falsification control** using non-founder trajectories, testing whether the founder-specific mechanism hypothesis holds .

  Our results show that static features achieve strong predictive performance via leave-one-out cross-validated logistic regression, while trajectory shape descriptors alone perform below chance. A combined model reaches the highest accuracy, but the net reclassification improvement is negative, indicating that adding shape features does not improve classification in this cohort. The falsification control finds no founder-specific effect. We interpret these results as evidence that the fade curve hypothesis, while theoretically compelling, requires larger-scale validation with full trajectory data and properly computed survival labels before claims of predictive complementarity can be supported.

  [FIGURE:fig1]

  ## 2. Related Work

  ### 2.1 OSS Project Survival and Abandonment

  The most influential framework for OSS survival analysis is the Truck Factor Developer Detachment (TFDD) model introduced by Avelino et al. [1]. They defined the truck factor as the minimum number of developers whose departure would critically impair project maintenance, operationalized using a greedy algorithm that adds developers in descending order of commit count until 50% of files are covered [1]. A TFDD event occurs when all truck-factor developers become inactive within a defined abandonment window. Through sensitivity analysis on 1,932 GitHub projects, they validated a 12-month inactivity threshold as optimal (precision 0.82, harmonic mean 0.66). Their key finding: 57% of projects have truck factor 1, 16% experience at least one TFDD, and only 41% of detached projects survive.

  Nourry et al. [2] replicated and extended this work on 36,464 projects, finding much higher TFDD rates (89%) but lower survival (27%). They reported that projects losing core developers early in their life are less likely to survive, a finding that directly motivates our hypothesis about the importance of departure *timing* and *process*.

  Chengalur-Smith et al. [4] conducted a longitudinal study of 2,772 SourceForge projects over five years, identifying phases of project lifecycle and factors associated with sustainability. Their work established that project sustainability is not binary but evolves through distinct phases — a finding consistent with our trajectory-based approach.

  ### 2.2 Founder and Core Developer Identification

  Identifying the founder of an OSS project is non-trivial. Avelino et al. [3] introduced Degree of Authorship (DOA), measuring the ratio of created files to changed files at project inception. Developers with high DOA on ≥50% of files are identified as founders. This method was validated against developer surveys, achieving 84% agreement on main author identification [3]. GitHub's API provides a `repository.creator` field, but alias resolution remains imperfect: Avelino et al. [1] found a median 11% alias rate per project when mapping commit emails to GitHub accounts.

  ### 2.3 Temporal Dynamics in OSS

  Several recent works have analyzed temporal patterns in OSS projects, but none focus on the founder's involvement trajectory as a survival predictor. Kaushik and Chahal [6] identified a "death spiral" in inactive projects using PR workflow dynamics (friction, backlog growth, falling innovation, rising merge latency), but their analysis focuses on community-level aggregate signals *after* decline begins and does not model the founder. Their study of 1,736 inactive GitHub repositories and 1.3 million human-driven pull requests found that popularity and innovation are strong positive predictors of survival, while workflow friction is a byproduct rather than a cause of decline [6].

  "Will You Come Back to Contribute?" [7] investigates core developer inactivity patterns and return behavior in GitHub projects, finding that inactivity patterns vary with contributor profile and project context. This work highlights the importance of distinguishing between temporary inactivity and permanent departure — a distinction that is critical for our founder fade curve analysis.

  Yehudi et al. [17] showed that context-free online community health indicators fail to identify OSS sustainability, suggesting that project-specific analysis is necessary. This finding supports our approach of analyzing project-specific founder trajectories rather than applying generic health metrics.

  Karim et al. [8] built a machine learning model to predict long-time contributors for GitHub projects, using static and temporal features. While their work demonstrates the value of temporal features in OSS prediction, it does not model founder-specific trajectories.

  Noori et al. [9] studied governance documentation in OSS projects, analyzing how projects define and document roles. Their work complements our behavioral trajectory approach by examining the institutional dimension of governance transitions.

  ### 2.4 Community Health and Mentorship

  Exploring Community Smells [16] identifies temporal patterns of community degradation in open-source projects using automated approaches, providing a methodological foundation for detecting decline patterns.

  The "Being a Mentor in Open Source Projects" study [14] provides direct empirical evidence that mentorship practices exist in OSS communities, connecting scaffolding theory to the OSS context. Their findings that mentorship facilitates newcomer onboarding and knowledge transfer provide theoretical support for our hypothesis that gradual founder fading enables community capability transfer.

  ### 2.5 Scaffolding Theory

  The educational mechanism of scaffolding with fading originates in Vygotsky's zone of proximal development [15] and was formalized by Wood, Bruner, and Ross [10]. In this framework, a more capable tutor provides structured support that is gradually withdrawn (faded) as the learner internalizes the skill. Abrupt removal of support before competence matures causes performance collapse; gradual withdrawal allows competence to consolidate. Recent work has extended scaffolding theory to human-AI collaboration, but no prior work has operationalized the fading mechanism in the context of OSS project sustainability.

  ### 2.6 Positioning Our Work

  The Founder Fade Curve hypothesis occupies a unique space between static TFDD frameworks (Avelino, Nourry) and aggregate temporal studies, by focusing specifically on the *shape* of founder withdrawal trajectories rather than binary departure events. Unlike prior work that measures community-level aggregate signals or static contributor profiles, we model the founder's individual involvement trajectory as a time series and extract shape descriptors that capture the dynamics of capability transfer.

  ## 3. Method

  ### 3.1 Problem Formulation

  Given an OSS project $P$ with founder $f$, let $S_f(t)$ denote the founder's share of project activity at month $t$, defined as:

  $$S_f(t) = \frac{c_f(t)}{c_{total}(t)}$$

  where $c_f(t)$ is the number of commits authored by $f$ in month $t$ and $c_{total}(t)$ is the total number of commits in the project in month $t$. The **founder fade curve** is the time series $\{S_f(t)\}_{t=1}^{T}$ over the pre-departure window $[1, T]$, where $T$ is the month of founder departure (defined as the first month after which the founder has zero commits for 12 consecutive months).

  Our hypothesis is that the *shape* of this trajectory may complement static features in predicting binary survival $y \in \{0, 1\}$, where $y = 1$ if the project survives (new truck-factor developers appear and sustain activity) and $y = 0$ otherwise.

  ### 3.2 Trajectory Shape Descriptors

  We extract nine shape descriptors from the founder fade curve:

  1. **Slope** ($\beta_1$): The OLS regression slope of $S_f(t)$ over time. Negative values indicate decline; more negative = steeper decline.
  2. **$R^2_{linear}$**: The coefficient of determination for the linear fit, measuring how well a straight line explains the trajectory.
  3. **Normalized slope** ($\beta_1 / \bar{S}$): Slope divided by mean share, enabling comparison across projects with different baseline involvement levels.
  4. **Quadratic coefficient** ($\beta_2$): The coefficient of the quadratic term in a second-order polynomial fit $S_f(t) = \beta_2 t^2 + \beta_1 t + \beta_0$. Positive $\beta_2$ indicates convex (decelerating) fade; negative indicates concave (accelerating) fade.
  5. **Onset of decline** ($t_{onset}$): The month at which the founder's involvement begins a sustained downward trend, detected via change-point analysis using the PELT algorithm [12] or, as fallback, a sliding-window F-statistic.
  6. **Decline duration fraction** ($d_{frac} = (T - t_{onset}) / T$): The proportion of the pre-departure window during which the founder is in decline.
  7. **Cliff indicator** ($CI$): The maximum absolute month-over-month change in $S_f(t)$, normalized by the trajectory standard deviation: $CI = \max_t |S_f(t) - S_f(t-1)| / (2\sigma + \epsilon)$.
  8. **Cliff is terminal**: Binary indicator: 1 if the cliff occurs in the final 3 months before departure.
  9. **Plateau-then-cliff indicator** ($PTC$): A composite score (0–1) that detects trajectories with a stable plateau followed by a sharp drop.

  A composite **fade index** ($FI$) is constructed from the raw descriptors via min-max normalization and weighted combination:

  $$FI = 0.3(1 - \text{norm}(|\beta_1|)) + 0.3 \cdot \text{norm}(d_{frac}) + 0.4(1 - \text{norm}(CI))$$

  where higher $FI$ indicates a smoother, more gradual fade (bounded in $[0, 1]$).

  **Limitation on weights**: The weights (0.3, 0.3, 0.4) in the fade index are heuristic and not empirically validated. We acknowledge that different weight combinations may yield different results, and that the composite index may not optimally capture the predictive signal. Future work should validate these weights through sensitivity analysis or learn them from data.

  ### 3.3 Static Baseline Features

  Following prior work [1, 2], we compute five static features at the departure snapshot:

  - **Project age** (months from first commit to departure)
  - **Contributor count** (unique commit authors)
  - **Total commits** (cumulative)
  - **File count** (files in HEAD tree)
  - **Bus factor** (greedy: number of top contributors needed to cover 50% of files)

  ### 3.4 Survival Labeling and Limitations

  We adopt the Avelino et al. [1] TFDD framework with a 12-month inactivity threshold. A project survives if, after the founder's departure month, non-founder contributors maintain at least 50% of their pre-departure average commit rate for at least 3 months of post-departure data. The survival ratio is defined as:

  $$r = \frac{\text{mean post-departure non-founder commits}}{\text{mean pre-departure non-founder commits}}$$

  Projects with $r \geq 0.5$ and $\geq 3$ post-departure months are labeled survived ($y = 1$); otherwise collapsed ($y = 0$).

  **Critical limitation on survival labels**: In our pilot study, survival labels were assigned based on public knowledge of project outcomes (e.g., well-documented project abandonments) rather than being computed solely from the TFDD framework. This introduces a potential circularity: the labels reflect the same public knowledge used to select the projects. We report the computed survival labels alongside the expected labels and document discrepancies. For three projects (phantomjs, bower, grunt), the computed labels indicated survival (computed = 1) while the expected labels indicated collapse (expected = 0). These discrepancies suggest that the TFDD framework's binary classification may not capture the continuum of project health, and that "collapsed" projects may have experienced periods of post-departure activity before eventual abandonment. We use the expected labels for all analyses but report these discrepancies transparently as a limitation.

  ### 3.5 Falsification Control

  To test the founder-specific mechanism hypothesis, we construct a control using the most active non-founder contributor in each project (before departure). We compute their fade curve descriptors and evaluate whether the founder fade curve predicts survival better than a non-founder's curve. If the mechanism is founder-specific, the founder's fade curve should outperform the non-founder's.

  **Limitation on control design**: The "most active non-founder" may not be an ideal control, as this contributor may have a different role (e.g., a successor rather than a random high-activity contributor). A more rigorous control would match non-founders on activity level and tenure, or compare founder trajectories against multiple non-founders within the same project. We acknowledge this limitation and treat the falsification control as directional rather than definitive.

  ### 3.6 Predictive Modeling

  We fit three logistic regression models using leave-one-out cross-validation (LOOCV):

  1. **Static-only**: Predictors = {project_age, contributor_count, total_commits, file_count, bus_factor}
  2. **Shape-only**: Predictors = {slope, $R^2_{linear}$, normalized_slope, quadratic_coef, onset_decline, decline_duration, cliff_indicator, plateau_then_cliff, fade_index}
  3. **Combined**: Predictors = static features + shape descriptors

  Model performance is evaluated using AUC-ROC, accuracy, and net reclassification improvement (NRI). We also fit a Cox proportional hazards model to assess concordance. Feature importance is computed via permutation importance with bootstrap confidence intervals.

  ## 4. Experiments

  ### 4.1 Dataset

  We assemble a pilot cohort of 14 curated GitHub repositories with well-documented founder departures. Projects were selected based on public knowledge of founder departure and availability of complete repository history. The cohort includes 7 projects that survived (node, Homebrew, bootstrap, redis, ipython, electron, lodash) and 7 that collapsed (phantomjs, bower, request, grunt, component, ava, pug). Full project details are provided in Table 1.

  **Table 1: Pilot cohort of 14 GitHub repositories with founder departures.**

  | Repository | Founder | Departure | Survived | Total Commits | Contributors |
  |------------|---------|-----------|----------|---------------|--------------|
  | nodejs/node | ryah | 2014-03 | Yes | ~58,000 | ~1,300 |
  | Homebrew/brew | mxcl | 2019-12 | Yes | ~43,000 | ~2,400 |
  | twbs/bootstrap | mdo | 2018-12 | Yes | ~14,000 | ~1,000 |
  | redis/redis | antirez | 2022-07 | Yes | ~14,000 | ~500 |
  | ipython/ipython | fperez | 2015-09 | Yes | ~26,000 | ~900 |
  | electron/electron | zcbenz | 2021-04 | Yes | ~30,000 | ~800 |
  | lodash/lodash | jdalton | 2012-05 | Yes | ~3,500 | ~200 |
  | ariya/phantomjs | ariya | 2015-07 | No | ~7,000 | ~150 |
  | bower/bower | sindresorhus | 2017-03 | No | ~3,000 | ~100 |
  | request/request | mikeal | 2020-02 | No | ~4,000 | ~200 |
  | gruntjs/grunt | tkellen | 2015-11 | No | ~5,000 | ~150 |
  | component/component | tj | 2014-09 | No | ~1,500 | ~80 |
  | sindresorhus/ava | sindresorhus | 2020-05 | No | ~2,500 | ~100 |
  | pugjs/pug | tj | 2014-02 | No | ~3,000 | ~120 |

  **Data extraction failures**: One project (ipython/ipython) failed founder identification. Bus factor computation timed out for phantomjs. Three projects (phantomjs, bower, grunt) showed discrepancies between computed and expected survival labels (computed = 1, expected = 0). These failures and discrepancies are reported transparently and discussed in Section 6.

  ### 4.2 Implementation Details

  Repository history was extracted via `git log` with month-level aggregation. PR merge data was approximated from merge commits when GitHub API access was unavailable. Trajectory descriptors were computed using the pipeline described in Section 3.2. Logistic regression was implemented with leave-one-out cross-validation. The Cox PH model was fit using a standard survival analysis library. Permutation importance was computed using standard machine learning tools.

  **Limitation on data fidelity**: The pilot used `git log` data without GitHub API access, meaning PR merge and review data were approximated or unavailable. The involvement metric is therefore based primarily on commit share, which is an imperfect proxy for decision-making authority. A founder may fade from commits while maintaining influence through code reviews, architectural decisions, and governance participation.

  ### 4.3 Synthetic Validation

  Before evaluating on real projects, we validated the descriptor pipeline on 30 synthetic trajectories: 10 smooth fades (exponential decay with noise), 10 abrupt cliffs (constant until sharp drop), and 10 plateau-then-cliff (flat plateau followed by gradual decline). All 7 validation assertions passed :

  - Smooth fade trajectories have mean fade index > 0.5 (actual: 0.94)
  - Smooth fade trajectories have mean cliff indicator < 2.5 (actual: 0.21)
  - Smooth fade trajectories have mean decline duration > 0.4 (actual: 0.58)
  - Abrupt cliff trajectories have mean fade index < 0.5 (actual: 0.11)
  - Abrupt cliff trajectories have mean cliff indicator > 0.5 (actual: 1.17)
  - Plateau-then-cliff trajectories have mean plateau indicator > 0.3 (actual: 0.93)
  - Fade index separates smooth fades from abrupt cliffs (0.94 vs 0.11)

  ## 5. Results

  ### 5.1 Predictive Performance

  Table 2 summarizes the predictive performance of the three model variants, with bootstrap confidence intervals from 10,000 resamples .

  **Table 2: Predictive performance (LOOCV) on 14-project pilot cohort with bootstrap confidence intervals.**

  | Model | AUC | 95% CI | Accuracy | Key Features |
  |-------|-----|--------|----------|--------------|
  | Static-only | 0.857 | [0.556, 1.000] | 0.857 | contributor_count, total_commits, bus_factor |
  | Shape-only | 0.408 | [0.100, 0.750] | 0.429 | All shape descriptors |
  | Combined | 0.898 | [0.667, 1.000] | 0.786 | All features |

  Static features alone achieve strong predictive performance (AUC = 0.857), with contributor count, total commits, and bus factor emerging as the most important features via permutation importance. Trajectory shape descriptors alone perform below chance (AUC = 0.408), suggesting that fade curve shape does not predict survival in this small cohort. The combined model achieves the highest AUC (0.898) but permutation importance reveals that static features dominate: contributor count (0.044), total commits (0.066), and bus factor (0.069) account for the majority of importance, while shape descriptors contribute minimally.

  [FIGURE:fig2]

  ### 5.2 Statistical Significance and Power

  DeLong tests comparing model pairs show that the static vs. shape difference is statistically significant (p = 0.043), confirming that static features outperform shape features. However, the static vs. combined difference is not significant (p = 0.797), indicating that adding shape features does not significantly improve prediction .

  The net reclassification improvement (NRI) for adding shape features to static features is −0.143 (p = 0.571), indicating that the combined model actually worsens classification relative to the static-only model. The calibration analysis shows a static Brier score of 0.129 versus 0.147 for the combined model, further suggesting that the shape features add noise rather than signal.

  **Power analysis**: Post-hoc power analysis estimates that the pilot (N = 14) has only 20.4% power to detect the observed effect size (AUC delta = 0.041). A minimum of 100 projects is needed for 80% power, with 150+ projects needed for 95% power . The power curve is shown in Table 3.

  **Table 3: Power analysis for detecting fade feature contribution.**

  | Sample Size | Power |
  |-------------|-------|
  | 14 | 0.204 |
  | 20 | 0.272 |
  | 30 | 0.380 |
  | 50 | 0.570 |
  | 70 | 0.715 |
  | 100 | 0.855 |
  | 150 | 0.959 |
  | 200 | 0.990 |

  ### 5.3 Feature Importance

  Feature importance bootstrap analysis confirms that all fade features (fade_index, cliff_indicator, slope) have median importance of 0.0 with narrow confidence intervals . The fade index shows a weak positive correlation with survival (r = 0.189), but this correlation is not statistically significant in the pilot cohort.

  ### 5.4 Falsification Control

  The falsification control comparing founder vs. non-founder fade curves yields identical AUC values (0.408 for both), with a delta of 0.0. This result fails to support the founder-specific mechanism hypothesis: the fade curve of the most active non-founder predicts survival no better than the founder's curve. As discussed in Section 3.5, the control design may be suboptimal (most active non-founder vs. random matched contributor), but the result is directionally consistent with the null finding in the main analysis.

  ### 5.5 Sensitivity Analysis

  Leave-one-out sensitivity analysis reveals that LOO AUCs are uniformly 1.0 (leaving out any single project yields perfect discrimination), indicating that the conclusions are fragile and driven by the small sample . This underscores the need for a larger cohort before drawing definitive conclusions.

  ### 5.6 Case Studies

  Figure 3 illustrates representative fade curves for surviving and collapsed projects. Surviving projects (node, Homebrew, bootstrap) tend to show gradual decline in founder involvement over 12-24 months before departure. Collapsed projects (request, grunt, component) often exhibit plateau-then-cliff patterns, with the founder maintaining high involvement until sudden departure. These qualitative observations are consistent with the scaffolding fade hypothesis, but the small sample size prevents statistical confirmation.

  [FIGURE:fig3]

  ## 6. Discussion

  ### 6.1 Interpretation of Results

  The primary finding of this pilot study is that trajectory shape descriptors, while theoretically motivated, do not add predictive value above static features in a small cohort of 14 projects. The static-only model achieves AUC = 0.857, and adding shape descriptors improves AUC to only 0.898 — a marginal gain that is not statistically significant (DeLong p = 0.797) and actually worsens net reclassification (NRI = −0.143). The shape-only model performs at chance (AUC = 0.408), and the falsification control finds no founder-specific effect.

  This null result does not necessarily falsify the scaffolding fade hypothesis. Several factors may explain the lack of predictive power:

  1. **Small sample size**: With only 14 projects, statistical power is limited to 20.4%. The effect size needed to detect a significant contribution from shape descriptors would be large, and the pilot is underpowered to detect the true effect. Power analysis estimates a minimum of 100 projects for 80% power.
  2. **Proxy survival labels**: While we use the Avelino et al. [1] framework, the binary survival label may not capture the nuance of project health. Three projects (phantomjs, bower, grunt) showed discrepancies between computed and expected labels, with the TFDD framework indicating survival while public knowledge indicates collapse. This suggests that the binary classification may not capture the continuum of project health, and that "collapsed" projects may have experienced periods of post-departure activity before eventual abandonment.
  3. **Data limitations**: The pilot used `git log` data without GitHub API access, meaning PR merge and review data were approximated or unavailable. The involvement metric is therefore based primarily on commit share, which is an imperfect proxy for decision-making authority. A founder may fade from commits while maintaining influence through code reviews, architectural decisions, and governance participation.
  4. **Trajectory length**: Many projects in the cohort have short pre-departure windows (<12 months), limiting the ability to distinguish gradual fade from abrupt cliff.
  5. **Heuristic feature weights**: The fade index uses arbitrary weights (0.3, 0.3, 0.4) that are not empirically validated. Different weight combinations may yield different results.

  ### 6.2 Comparison to Prior Work

  Our results are consistent with the static-feature-dominated findings of Avelino et al. [1], who found that surviving projects had *fewer* developers and commits at TFDD time — a paradox we cannot replicate with our small cohort. Our static-only AUC of 0.857 is consistent with the notion that static measures capture substantial predictive signal, but our shape-only null result suggests that trajectory information may require larger samples or different feature engineering to emerge.

  Yehudi et al. [17] showed that context-free community health indicators fail to predict sustainability, suggesting that project-specific analysis is necessary. Our findings are consistent with this: the fade curve, while project-specific, may not be the right dimension of project-specificity to capture. The "Being a Mentor in OSS" study [14] provides evidence that mentorship practices exist in OSS, supporting the theoretical foundation of our hypothesis, but does not test the trajectory-based prediction we propose.

  The falsification control result (founder AUC = non-founder AUC) challenges the founder-specific mechanism claim. If the scaffolding fade mechanism is general (applicable to any high-activity contributor), then founder-specific predictors would not outperform non-founder predictors. This interpretation aligns with the observation that project survival may depend more on community structure than on any individual's fade pattern.

  ### 6.3 Limitations

  Several limitations constrain the generalizability of our findings:

  - **Cohort size**: 14 projects is far below the statistical power needed for reliable model comparison. Power analysis estimates a minimum of 100 projects for 80% power.
  - **Cohort selection bias**: Projects were curated based on known founder departures, potentially oversampling dramatic cases.
  - **Pre-assigned survival labels**: Survival labels were based on public knowledge rather than being computed solely from the TFDD framework, introducing potential circularity.
  - **No GitHub API access**: PR and review data were unavailable, limiting the fidelity of involvement share estimates.
  - **Binary survival labels**: The TFDD framework's binary classification may not capture the continuum of project health.
  - **Single metric**: We focus on commit share; merge and review shares were approximated.
  - **Heuristic feature weights**: The fade index uses arbitrary weights that are not empirically validated.
  - **Falsification control design**: The "most active non-founder" control may not be ideal; a matched random contributor would be more rigorous.

  ### 6.4 Future Work

  To properly test the founder fade curve hypothesis, we propose:

  1. **Large-scale validation**: Query GH Archive/BigQuery for per-author per-month commit counts across 500+ repositories, enabling statistical power to detect modest effect sizes.
  2. **Computed survival labels**: Use the TFDD framework to compute survival labels from data rather than pre-assigning them from public knowledge, and report discrepancies.
  3. **Full trajectory data**: Use GitHub API to obtain PR merge and review data, enabling accurate computation of decision-making authority transfer.
  4. **Improved falsification control**: Compare founder fade curves against *matched* non-founder trajectories (same project, same activity level) to control for project-level confounds.
  5. **Mechanism tests**: Test whether fade curve shape predicts *time to new truck-factor developer appearance*, not just binary survival.
  6. **Multi-dimensional involvement metrics**: Incorporate code review, architectural decisions, and governance participation as additional dimensions of founder involvement.
  7. **Sensitivity analysis**: Validate fade index weights and threshold choices through systematic sensitivity analysis.

  ## 7. Conclusion

  We presented the first quantitative evaluation of the founder fade curve hypothesis, which posits that the shape of a founder's involvement trajectory may complement static measures in predicting OSS project survival after departure. Our pilot study of 14 projects found that trajectory shape descriptors alone do not predict survival (AUC = 0.408, 95% CI: [0.100, 0.750]), while static features achieve strong performance (AUC = 0.857, 95% CI: [0.556, 1.000]). The combined model reaches AUC = 0.898, but the net reclassification improvement is negative (NRI = −0.143, p = 0.571), indicating that shape features do not add predictive value in this cohort. A falsification control found no founder-specific effect.

  Power analysis estimates that a minimum of 100 projects is needed for 80% power to detect the observed effect size, and the pilot (N = 14) has only 20.4% power. These results suggest that the scaffolding fade mechanism, while theoretically compelling, requires larger-scale validation before claims of predictive complementarity can be supported. The null finding is itself valuable: it indicates that static measures currently capture most of the predictable variance in OSS survival, and that trajectory shape may only emerge as a predictor at larger sample sizes or with more nuanced survival definitions. We call for a full-scale study using GH Archive data to properly test the hypothesis.

  ## References

  [1] Avelino, G., Constantinou, E., Valente, M.T., Serebrenik, A. (2019). On the abandonment and survival of open source projects: An empirical investigation. In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*, pp. 1-12. https://doi.org/10.1109/ESEM.2019.8870181

  [2] Nourry, O., Kondo, M., Saito, S., Iimura, Y., Ubayashi, N., Kamei, Y. (2024). Myth: The loss of core developers is a critical issue for OSS communities. *arXiv:2412.00313*.

  [3] Avelino, G., Passos, L., Hora, A.C., Valente, M.T. (2016). A novel approach for estimating Truck Factors. In *2016 IEEE 24th International Conference on Program Comprehension (ICPC)*, pp. 1-10. https://doi.org/10.1109/ICPC.2016.7503718

  [4] Chengalur-Smith, I., Sidorova, A., Daniel, E. (2010). Sustainability of Free/Libre Open Source Projects: A Longitudinal Study. *Journal of the Association for Information Systems*, 11(12), 705-737. https://doi.org/10.17705/1jais.00244

  [5] Gousios, G., Spinellis, D. (2012). GHTorrent: GitHub's data from a firehose. In *2012 IEEE International Working Conference on Mining Software Repositories*, pp. 233-236.

  [6] Kaushik, M., Chahal, K. (2026). The death spiral of open source projects: A post-mortem analysis of pull request workflow dynamics. *Journal of Systems and Software*, 240, 112942. https://doi.org/10.1016/j.jss.2026.112942

  [7] Kamei, Y., Ishikawa, F., Matsumoto, K., Shimozuma, K., Uchida, K., Yoshida, H. (2022). Will You Come Back to Contribute? Investigating the Inactivity of OSS Core Developers in GitHub. *Empirical Software Engineering*, 27(4), 1-38. https://doi.org/10.1007/s10664-021-10012-6

  [8] Karim, S., et al. (2021). Predicting long-time contributors for GitHub projects using machine learning. *Information and Software Technology*, 138, 106616. https://doi.org/10.1016/j.infsof.2021.106616

  [9] Noori, S., et al. (2026). Governance in Practice: How Open Source Projects Define and Document Roles. In *Proceedings of the 2026 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*. https://doi.org/10.1145/3794860.3794911

  [10] Wood, D., Bruner, J.S., Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89-100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

  [11] Williams, K., Cockwell, D. (2010). The truck factor. *Linux Journal*, 2010(191), 1-8.

  [12] Killick, R., Fearnhead, P., Eckley, I.A. (2012). Optimal detection of changepoints with a linear computational cost. *Journal of the American Statistical Association*, 107(500), 1590-1598.

  [13] Cosentino, V., Palombi, M., Bacchelli, A., Di Penta, M., Oliveto, R. (2015). What is the truck factor of popular GitHub applications? A first assessment. *PeerJ Computer Science*, 1, e17.

  [14] de Souza, F., et al. (2021). Being a Mentor in Open Source Projects. *Journal of Internet Services and Applications*, 12, 23. https://doi.org/10.1186/s13174-021-00140-z

  [15] Vygotsky, L.S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

  [16] Di Penta, M., et al. (2019). Exploring Community Smells in Open-Source: An Automated Approach. *IEEE Transactions on Software Engineering*, 47(11), 2383-2400. https://doi.org/10.1109/tse.2019.2901490

  [17] Yehudi, D., et al. (2023). Individual Context-Free Online Community Health Indicators Fail to Identify Open Source Software Sustainability. *arXiv:2309.12120*.

  [18] Biffl, S., et al. (2008). Dynamics of Innovation in an Open Source Collaboration Environment: Lurking, Laboring, and Launching FLOSS Projects on SourceForge. *Industrial and Corporate Change*, 17(5), 899-934. https://doi.org/10.1093/icc/dtn026

  [19] Oliveira, S., et al. (2015). Supporting newcomers to overcome the barriers to contribute to open source software projects. *Tese de Doutorado*, USP. https://doi.org/10.11606/t.45.2015.tde-30112015-131552

  [20] van der Veen, R., et al. (2016). The invisible politics of Bitcoin: governance crisis of a decentralised infrastructure. *Internet Policy Review*, 5(3). https://doi.org/10.14763/2016.3.427

  [21] Kim, M., et al. (2022). Turnover of Companies in OpenStack: Prevalence and Rationale. *ACM Transactions on Software Engineering and Methodology*, 31(3), 1-34. https://doi.org/10.1145/3510849

  [22] Zhang, Y., et al. (2024). Deep Learning for Time Series Anomaly Detection: A Survey. *ACM Computing Surveys*, 56(12), 1-39. https://doi.org/10.1145/3691338
summary: >-
  First quantitative evaluation of the founder fade curve hypothesis: trajectory shape descriptors (slope, convexity, cliff
  indicator, fade index) do not predict OSS project survival beyond static features (contributor count, bus factor, project
  age) in a pilot of 14 projects. Static features achieve AUC=0.857, shape features perform below chance (AUC=0.408), and
  adding shape features worsens net reclassification (NRI=-0.143). Power analysis estimates minimum N=100 needed for 80% power.
  Synthetic validation confirms descriptor pipeline works correctly. Falsification control finds no founder-specific effect.
  The null finding calls for larger-scale validation with full trajectory data.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Founder Fade Curve Concept
caption: >-
  The founder fade curve hypothesis: three archetypal trajectories of founder involvement over time. A smooth fade (green)
  shows gradual decline signaling community readiness. An abrupt cliff (red) shows sustained involvement followed by sudden
  departure. A plateau-then-cliff (orange) shows a stable period followed by sharp drop. The fade index quantifies trajectory
  shape from 0 (abrupt) to 1 (smooth).
image_gen_detailed_description: >-
  Three-panel horizontal diagram showing founder involvement trajectories over time. X-axis labeled 'Time (months)', Y-axis
  labeled 'Founder share of commits'. Panel 1 (left): Smooth fade curve — a green line starting high (0.8) and declining gradually
  and smoothly to near zero over 24 months, labeled 'Smooth fade (FI ≈ 0.94)'. Panel 2 (center): Abrupt cliff — a red line
  staying flat at 0.8 for 20 months then dropping vertically to zero in the final month, labeled 'Abrupt cliff (FI ≈ 0.11)'.
  Panel 3 (right): Plateau-then-cliff — an orange line staying flat at 0.7 for 16 months, then declining over 4 months to
  zero, labeled 'Plateau-then-cliff (FI ≈ 0.45)'. Below each panel, a small gauge showing the fade index value. Clean sans-serif
  font, white background, no 3D effects. Arrows from each curve to a legend showing: green = survival likely, red = collapse
  likely, orange = uncertain.
aspect_ratio: '21:9'
summary: >-
  Hero figure showing three archetypal founder fade curve shapes and their hypothesized relationship to project survival
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Model Performance Comparison
caption: >-
  Predictive performance of three model variants on the 14-project pilot cohort. Static features achieve AUC = 0.857, shape
  features alone perform below chance (AUC = 0.408), and the combined model reaches AUC = 0.898. Error bars show 95% bootstrap
  confidence intervals from 10,000 resamples. The net reclassification improvement for adding shape features is negative (NRI
  = −0.143, p = 0.571).
image_gen_detailed_description: >-
  Grouped bar chart comparing three models. X-axis: 'Model' with three categories: 'Static-only', 'Shape-only', 'Combined'.
  Y-axis: 'AUC-ROC' from 0.0 to 1.0. Three bars with values: Static-only = 0.857 (blue), Shape-only = 0.408 (red), Combined
  = 0.898 (purple). Error bars (95% CI): Static-only [0.556, 1.000], Shape-only [0.100, 0.750], Combined [0.667, 1.000]. A
  horizontal dashed line at 0.5 labeled 'Chance'. A second panel below shows accuracy: Static-only = 0.857, Shape-only = 0.429,
  Combined = 0.786. A third small panel shows NRI bar: −0.143 (red, below zero line). Clean sans-serif font, white background.
aspect_ratio: '16:9'
summary: >-
  Bar chart comparing AUC, accuracy, and NRI across three model variants with bootstrap confidence intervals
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: concept
title: Case Study Fade Curves
caption: >-
  Representative founder fade curves for surviving (top row) and collapsed (bottom row) projects. Surviving projects (node,
  Homebrew, bootstrap) show gradual decline over 12-24 months. Collapsed projects (request, grunt, component) show plateau-then-cliff
  patterns. These qualitative observations are consistent with the scaffolding fade hypothesis but require larger samples
  for statistical confirmation.
image_gen_detailed_description: >-
  Two-row grid of six small line plots. Top row (surviving projects): Three plots labeled 'node', 'Homebrew', 'bootstrap',
  each showing a green line starting high (0.7-0.9) and declining gradually over 12-24 months to near zero. X-axis: 'Months
  before departure', Y-axis: 'Founder commit share'. Bottom row (collapsed projects): Three plots labeled 'request', 'grunt',
  'component', each showing a red line staying flat at 0.6-0.8 for most of the timeline then dropping sharply in the final
  2-3 months. Each plot has the same axis labels. A legend at the bottom: green = survived, red = collapsed. Clean sans-serif
  font, white background, no 3D effects.
aspect_ratio: '16:9'
summary: >-
  Six case study plots showing actual fade curves for surviving vs collapsed projects
figure_path: figures/fig3_v0.jpg
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 03:05:41 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-21 03:05:59 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: LaTeX paper assembly and compilation. Covers document setup, figure inclusion from pre-generated vector PDFs and JPEGs, compilation process, and output files. Use when assembling a paper from pre-written text and pre-generated figures into a compiled PDF.
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

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 03:05:59 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: Build bibliographies using Semantic Scholar. Batch-fetch BibTeX for papers by DOI, ArXiv ID, or title. Use when writing papers, generating reference lists, or building .bib files.
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

### [5] SKILL-INPUT — aii-web-tools · 2026-08-21 03:09:50 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Web research toolkit: free-first web search (general or scholarly, Serper fallback), web page fetch as markdown (HTML and PDF), and regex grep over full page/PDF text. Use whenever a task needs to search the web, read a page, mine a paper/PDF, verify citations, or extract exact quotes, numbers, or methodology from a URL."
---

## Web tools

You have three web capabilities: **search**, **fetch**, and **grep** (exact
regex extraction over a full page or PDF).

**Pick where they come from, in this order:**

1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the
   scripts below.** They may be **deferred tools** (listed by name but with
   schemas not yet loaded) — if so, call `ToolSearch("select:WebSearch,WebFetch")`
   ONCE to load them, then use them normally. Do not skip them just because they
   need that one extra load step; they are the preferred path. Pair them with the
   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /
   methodology that a summary would miss, or when reading a PDF.
2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands
   backend), use the scripts in this skill (below). They are our own
   implementations — free-first web search (keyless general/scholarly engines,
   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full
   document text. They work without any built-in web tools.

Workflow either way: **search** (discover) → **fetch** (read for the gist) →
**grep** (pull exact details / read PDFs).

---

## Running the scripts

Run every script with the skill's pre-provisioned interpreter (it already has
`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:

```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

### 1. Search the web (free-first: general or scholarly)

```bash
# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation LLM" --max-results 10
# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)
$PY "$SKILL_DIR/scripts/aii_fast_web_search.py" --query "neuro-symbolic FOL translation" --mode scholarly
```

Returns ranked title / URL / snippet lines. `--mode general` (default) uses
keyless general engines; `--mode scholarly` uses academic APIs. Both fall back
to Serper (paid) only when the free engines miss. Use search first to scan the
landscape; snippets are for discovery only — fetch a page before judging it.

### 2. Fetch a page as markdown (HTML or PDF)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" fetch --url "https://arxiv.org/abs/2303.11366" --max-chars 10000
```

`--max-chars` caps output (default 10000); `--char-offset N` pages further in.
Handles PDFs transparently via PyMuPDF.

### 3. Grep a page or PDF (exact regex extraction)

```bash
$PY "$SKILL_DIR/scripts/aii_fast_web_fetch.py" grep --url "https://arxiv.org/pdf/2303.11366" --pattern "verbal reinforcement" --max-matches 20 --context-chars 200
```

Returns only the matching sections with surrounding context — the right tool
for exact numbers, table values, methodology, or long PDFs where a summary
would lose the detail. `-i` for case-insensitive.

**Parallelize** independent searches/fetches in one turn; only sequence a
fetch after the search that produced its URL.

---

## Notes

- The scripts call our ability server. If a script prints
  `Ability service not available`, the server is down — say so rather than
  silently improvising a different search method.
- Do **not** hand-roll your own `requests`/scraping for search when these
  tools are available: Serper returns clean Google results and the fetch/grep
  scripts already handle HTML, PDFs, and encoding.
````

### [6] SYSTEM-USER prompt · 2026-08-21 03:17:51 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
