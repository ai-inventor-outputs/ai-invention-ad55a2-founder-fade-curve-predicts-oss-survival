# review_paper — test_idea

> Phase: `invention_loop` · round 2 · `review_paper`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 01:44:25 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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
2. **A synthetic validation** demonstrating that the descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff patterns across 30 synthetic trajectories [ARTIFACT:art_501ZvV17S5Y5].
3. **A pilot empirical evaluation** on 14 curated GitHub repositories with documented founder departures (7 survived, 7 collapsed), comparing predictive performance of trajectory shape descriptors, static features, and their combination [ARTIFACT:art_501ZvV17S5Y5].
4. **Bootstrap confidence intervals and power analysis** showing that the pilot is underpowered and that a minimum of 100 projects is needed for 80% power to detect the observed effect size [ARTIFACT:art_eSx8EALUZo99].
5. **A falsification control** using non-founder trajectories, testing whether the founder-specific mechanism hypothesis holds [ARTIFACT:art_501ZvV17S5Y5].

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

Before evaluating on real projects, we validated the descriptor pipeline on 30 synthetic trajectories: 10 smooth fades (exponential decay with noise), 10 abrupt cliffs (constant until sharp drop), and 10 plateau-then-cliff (flat plateau followed by gradual decline). All 7 validation assertions passed [ARTIFACT:art_501ZvV17S5Y5]:

- Smooth fade trajectories have mean fade index > 0.5 (actual: 0.94)
- Smooth fade trajectories have mean cliff indicator < 2.5 (actual: 0.21)
- Smooth fade trajectories have mean decline duration > 0.4 (actual: 0.58)
- Abrupt cliff trajectories have mean fade index < 0.5 (actual: 0.11)
- Abrupt cliff trajectories have mean cliff indicator > 0.5 (actual: 1.17)
- Plateau-then-cliff trajectories have mean plateau indicator > 0.3 (actual: 0.93)
- Fade index separates smooth fades from abrupt cliffs (0.94 vs 0.11)

## 5. Results

### 5.1 Predictive Performance

Table 2 summarizes the predictive performance of the three model variants, with bootstrap confidence intervals from 10,000 resamples [ARTIFACT:art_eSx8EALUZo99].

**Table 2: Predictive performance (LOOCV) on 14-project pilot cohort with bootstrap confidence intervals.**

| Model | AUC | 95% CI | Accuracy | Key Features |
|-------|-----|--------|----------|--------------|
| Static-only | 0.857 | [0.556, 1.000] | 0.857 | contributor_count, total_commits, bus_factor |
| Shape-only | 0.408 | [0.100, 0.750] | 0.429 | All shape descriptors |
| Combined | 0.898 | [0.667, 1.000] | 0.786 | All features |

Static features alone achieve strong predictive performance (AUC = 0.857), with contributor count, total commits, and bus factor emerging as the most important features via permutation importance. Trajectory shape descriptors alone perform below chance (AUC = 0.408), suggesting that fade curve shape does not predict survival in this small cohort. The combined model achieves the highest AUC (0.898) but permutation importance reveals that static features dominate: contributor count (0.044), total commits (0.066), and bus factor (0.069) account for the majority of importance, while shape descriptors contribute minimally.

[FIGURE:fig2]

### 5.2 Statistical Significance and Power

DeLong tests comparing model pairs show that the static vs. shape difference is statistically significant (p = 0.043), confirming that static features outperform shape features. However, the static vs. combined difference is not significant (p = 0.797), indicating that adding shape features does not significantly improve prediction [ARTIFACT:art_eSx8EALUZo99].

The net reclassification improvement (NRI) for adding shape features to static features is −0.143 (p = 0.571), indicating that the combined model actually worsens classification relative to the static-only model. The calibration analysis shows a static Brier score of 0.129 versus 0.147 for the combined model, further suggesting that the shape features add noise rather than signal.

**Power analysis**: Post-hoc power analysis estimates that the pilot (N = 14) has only 20.4% power to detect the observed effect size (AUC delta = 0.041). A minimum of 100 projects is needed for 80% power, with 150+ projects needed for 95% power [ARTIFACT:art_eSx8EALUZo99]. The power curve is shown in Table 3.

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

Feature importance bootstrap analysis confirms that all fade features (fade_index, cliff_indicator, slope) have median importance of 0.0 with narrow confidence intervals [ARTIFACT:art_eSx8EALUZo99]. The fade index shows a weak positive correlation with survival (r = 0.189), but this correlation is not statistically significant in the pilot cohort.

### 5.4 Falsification Control

The falsification control comparing founder vs. non-founder fade curves yields identical AUC values (0.408 for both), with a delta of 0.0. This result fails to support the founder-specific mechanism hypothesis: the fade curve of the most active non-founder predicts survival no better than the founder's curve. As discussed in Section 3.5, the control design may be suboptimal (most active non-founder vs. random matched contributor), but the result is directionally consistent with the null finding in the main analysis.

### 5.5 Sensitivity Analysis

Leave-one-out sensitivity analysis reveals that LOO AUCs are uniformly 1.0 (leaving out any single project yields perfect discrimination), indicating that the conclusions are fragile and driven by the small sample [ARTIFACT:art_eSx8EALUZo99]. This underscores the need for a larger cohort before drawing definitive conclusions.

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
</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

--- Item 1 ---
id: art_XZccH0dIj4ss
type: research
title: 'Literature Survey: Founder Fade & OSS Survival'
summary: >-
  This research synthesizes findings across four critical areas for evaluating the Founder Fade Curve hypothesis: (1) OSS
  project abandonment and survival measurement using the Truck Factor Developer Detachment (TFDD) framework from Avelino et
  al. (2019) and Nourry et al. (2024), (2) founder identification methods including Degree of Authorship (DOA) and GitHub
  API alias resolution, (3) large-scale GitHub data sources with GH Archive/BigQuery recommended as primary due to free access
  and comprehensive coverage, and (4) trajectory shape analysis techniques including Theil-Sen estimators, ruptures change-point
  detection, convexity analysis, and composite index construction. Key findings: 57% of OSS projects have truck factor of
  1, 16% experience founder detachment, only 41% survive. The survey identifies significant research gaps for several 2025-2026
  papers cited in the hypothesis, and recommends adopting the Avelino TFDD framework with 1-year inactivity threshold as the
  primary survival definition.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 2 ---
id: art_oy-M28PzQPWY
type: dataset
title: GitHub OSS Repos for Founder Fade Study
summary: >-
  This artifact provides a curated dataset of 14,428 public GitHub OSS repositories from the h1alexbel/github-repos collection
  (MIT license, collected via ghminer tool). Each record contains repo-level features: full repo name, branch, description,
  topics, creation date, last commit date, contributor count, PR count, commit count, issue count, fork count, star count,
  disk usage, license, and primary language. A proxy survival label (ACTIVE/INACTIVE) is computed based on contributor count
  and activity ratio, serving as a baseline for the Founder Fade hypothesis that the shape of founder involvement decline
  predicts project survival. The dataset spans multiple ecosystems (JavaScript, Python, Go, Rust, Ruby, etc.) and includes
  repositories of varying sizes and ages. Downstream experiments will use this as a candidate pool to identify repos with
  departed founders, then extract time-series founder involvement trajectories via GitHub API and git log parsing. The dataset
  is organized in exp_sel_data_out.json schema format with 5-fold stratified cross-validation splits.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
out_expected_files:
- data.py
- full_data_out.json
- preview_data_out.json
- mini_data_out.json

--- Item 3 ---
id: art_501ZvV17S5Y5
type: experiment
title: Founder Fade Curve Predicts OSS Survival
summary: >-
  Pilot experiment implementing trajectory shape-descriptor pipeline to predict OSS project survival after founder departure.
  Analyzed 14 curated GitHub repos with documented founder departures (7 survived, 7 collapsed). Key results: (1) Synthetic
  validation passed all 7 assertions, confirming descriptors correctly identify fade/cliff patterns across 30 synthetic trajectories.
  (2) Static features (contributor_count, total_commits, bus_factor) achieved AUC=0.857 via LOOCV logistic regression. (3)
  Trajectory shape descriptors alone achieved AUC=0.408 (below chance). (4) Combined features achieved AUC=0.898 with CoxPH
  concordance=0.92. (5) Falsification control found no founder-specific effect (founder_AUC=non_founder_AUC=0.41). Conclusion:
  fade_index and trajectory shape descriptors do not significantly predict survival beyond static features in this pilot.
  The experiment used git log analysis with fallback for PR merge data, OLS slope computation, and leave-one-out cross-validation
  with permutation tests. Output contains 49 examples including synthetic trajectories, project analyses with predictions,
  and model comparison results.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 4 ---
id: art_H-TNs6qLkOWs
type: experiment
title: Founder Fade Curve Analysis on OSS Projects
summary: >-
  Scaled experiment analyzing founder fade curves across 100+ OSS projects from a 14K GitHub repository dataset. The study
  reconstructs founder involvement trajectories using aggregate repository features (commit counts, contributor ratios, activity
  patterns) when direct GitHub API access is unavailable. Key methodology includes: (1) Filtering candidates by language,
  age, contributor count, and star count; (2) Reconstructing synthetic fade trajectories from aggregate metrics including
  founder dominance, fade slope, convexity, cliff indicators, and fade index; (3) Computing survival labels based on fade
  characteristics (projects with steep decline and high founder dominance labeled as COLLAPSE); (4) Training logistic regression
  with LOOCV and bootstrap CIs; (5) Attempting Cox proportional hazards modeling; (6) Computing permutation feature importance;
  (7) Generating falsification controls for matched non-founder patterns. The experiment demonstrates the full pipeline for
  testing the founder fade hypothesis with graceful fallback when API-based data extraction is unavailable.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_experiment_1
out_expected_files:
- method.py
- full_method_out.json
- mini_method_out.json
- preview_method_out.json

--- Item 5 ---
id: art_BCR-_cTiEwyd
type: research
title: Citation Verification & Real OSS Survival Papers
summary: >-
  This research systematically verified all 15 references from the iter_1 literature survey plus 7 hypothesis-related works
  cited in the Founder Fade Curve hypothesis. Key findings: (1) Of 15 original references, 11 are fully verified (Avelino
  2019, Nourry 2024, Avelino 2016 truck factor, GHTorrent, GH Archive, BigQuery, GitHub APIs, SciPy, ruptures, Theil-Sen,
  Wikipedia), 2 could not be verified (MIT Press chapter on OSS success/abandonment at DOI 10.7551/mitpress/8413.003.0013,
  PeerJ preprint on truck factor at DOI 10.7287/peerj.preprints.1233v2), and 1 is partial (OSF scaffolding preprint DOI 10.35542/osf.io/5eutb_v1
  exists but content could not be verified). (2) Of 7 hypothesis-related works: Kaushik & Chahal (2026) 'Death Spiral' was
  VERIFIED and is real (JSS 2026, arXiv:2605.11844); Vygotsky (1978) and Wood/Bruner/Ross (1976) are verified classics; but
  Chen et al. (ICSE 2026) on core contributor disengagement, Karim et al. (2026) on deep temporal neural architectures, and
  Noori et al. (2025) on governance transition are FABRICATED. (3) Real replacements were identified: for Chen et al. -> 'Will
  You Come Back to Contribute?' (Empirical Software Engineering 2022); for Karim et al. -> 'Predicting long-time contributors'
  (Information and Software Technology 2021); for Noori et al. -> 'Governance in Practice' (2026). (4) Supplementary work
  found includes: Chengalur-Smith et al. (2010) on longitudinal OSS sustainability, Yehudi et al. (2023) showing context-free
  indicators fail, 'Being a Mentor in OSS' (2021) on scaffolding in practice, and 'Exploring Community Smells' (TSE 2019)
  on temporal community degradation. (5) Positioning analysis: The Founder Fade Curve hypothesis occupies a unique space between
  static TFDD frameworks (Avelino, Nourry) and aggregate temporal studies, by focusing specifically on the SHAPE of founder
  withdrawal trajectories rather than binary departure events.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1
out_expected_files:
- research_out.json

--- Item 6 ---
id: art_eSx8EALUZo99
type: evaluation
title: Bootstrap CI and Power Analysis for Founder Fade Curve Pilot
summary: >-
  Comprehensive statistical re-analysis of the founder fade curve pilot experiment (N=14 OSS projects, 7 survived/7 collapsed
  after founder departure). Performed 10,000-resample bootstrap AUC confidence intervals showing static features AUC=0.857
  (95% CI: [0.556, 1.000]), shape features AUC=0.408 (95% CI: [0.100, 0.750]), combined AUC=0.898 (95% CI: [0.667, 1.000]).
  LOOCV stability analysis reveals static model achieves 85.7% accuracy (12/14 correct) but with wide CIs indicating instability
  at N=14. Post-hoc power analysis estimates minimum N=100 projects needed for 80% power to detect the observed fade contribution
  (AUC delta=0.041). DeLong tests show static vs combined difference is non-significant (p=0.797), confirming null result
  for fade features. NRI is -0.143 (p=0.571), indicating adding fade features actually worsens classification. Calibration
  analysis shows static Brier score 0.129 vs combined 0.147. Feature importance bootstrap confirms all fade features (fade_index,
  cliff_indicator, slope) have median importance near zero. Sensitivity analysis shows LOO AUCs are uniformly 1.0 (leaving
  out any single project yields perfect discrimination), indicating fragile conclusions driven by small sample. Key conclusion:
  fade curve features do not significantly predict OSS survival beyond static repository features; future work requires N>=100
  projects for adequate power.
workspace_path: >-
  /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_evaluation_1
out_expected_files:
- eval.py
- full_eval_out.json
- mini_eval_out.json
- preview_eval_out.json
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<previous_review>
Your review from the previous iteration. Check which critiques have been addressed
in the revised paper. Do NOT re-raise critiques that have been adequately fixed.
Only re-raise if the fix is insufficient.

- [MAJOR] (novelty) References [6], [7], and [8] claim publication in 2026 at top venues (Journal of Systems and Software, ICSE 2026, ICSME 2026) but cannot be verified through scholarly search. Reference [7] (Chen et al. on core contributor disengagement) is particularly concerning as it is cited as key prior work but appears to not exist. Fabricated or unverifiable references constitute a serious academic integrity issue.
  Action: Verify all references exist before submission. For [6], [7], [8], either replace with verifiable prior work or remove citations. Search Semantic Scholar, Google Scholar, or venue proceedings to confirm these papers are real and accurately described.
- [MAJOR] (methodology) Survival labels are pre-assigned ('expected_survival') based on public knowledge rather than computed from the TFDD framework. The code explicitly sets survival_label = expected_survival and only logs discrepancies. This introduces circularity: the authors are testing whether features predict labels they themselves assigned based on the same public knowledge they used to select the projects.
  Action: Compute survival labels from data using the TFDD framework (12-month inactivity threshold, 50% activity retention). Use computed labels for all analyses. Report any discrepancies between computed and expected labels as part of the analysis. This is essential for scientific validity.
- [MAJOR] (rigor) The sample size of 14 projects is far too small for reliable statistical inference. LOOCV on 14 samples produces high variance in AUC estimates. The shape-only model's AUC of 0.408 (below chance) suggests the features may be systematically misleading, not just uninformative. The Cox PH concordance of 0.92 is also unreliable with only 14 observations and 7 events.
  Action: Expand to a larger cohort: at minimum 100 projects for preliminary findings, 500+ for robust statistical claims. Report confidence intervals via bootstrap. Acknowledge that the current results are directional only. Consider focusing on case studies with detailed trajectory analysis rather than claiming predictive modeling.
- [MAJOR] (methodology) The falsification control uses the 'most active non-founder' as a comparison, but this is not an appropriate control. Non-founders have different roles, less historical influence, and may be successors rather than random high-activity contributors. The finding that founder and non-founder AUCs are identical (0.408) suggests the trajectory features are not founder-specific, but the control design cannot distinguish this from the features being generally uninformative.
  Action: Use a random contributor matched on activity level as the control, or compare founder trajectories against multiple non-founders. Test whether the founder-specific effect holds when controlling for project-level factors (size, age, topic). The falsification should test whether founder fade curves are more predictive than non-founder fade curves from THE SAME projects, not just any high-activity contributor.
- [MAJOR] (evidence) Data extraction logs reveal multiple issues: ipython/ipython failed (could not identify founder), bus factor computation timed out for phantomjs, survival labels were overridden for phantomjs (computed=1, expected=0), bower (computed=1, expected=0), and grunt (computed=1, expected=0). These discrepancies suggest the curated labels may not align with computed metrics.
  Action: Report all data extraction failures and label discrepancies transparently. Investigate why computed survival labels differ from expected labels for multiple projects. Either use computed labels consistently or justify why expected labels are more appropriate. Document the proportion of projects with successful data extraction.
- [MINOR] (methodology) The composite involvement metric (40% commits + 30% merges + 30% reviews) is arbitrary. With no GitHub API access, reviews fall back to commits, making the composite effectively 70% commits + 30% merges. The weights are not justified and may not reflect actual decision-making authority transfer.
  Action: Justify weight choices with domain expertise or empirical validation. Report sensitivity analysis showing how results change with different weight combinations. Acknowledge that commits are an imperfect proxy for influence and decision-making authority.
- [MINOR] (rigor) The fade index uses min-max normalization across the small sample (n=14), which is unstable. The threshold values for cliff indicator (0.5), plateau detection (slope < 0.02), and decline duration are arbitrary and not validated against ground truth trajectory classifications.
  Action: Report how sensitive results are to threshold choices. Validate trajectory classifications against manual annotation of a subset of projects. Consider using the synthetic validation to establish reasonable thresholds rather than ad-hoc values.
- [MINOR] (clarity) The paper claims to be the 'first quantitative evaluation' of the founder fade curve hypothesis, but does not adequately discuss related work on contributor turnover, succession planning, or trajectory analysis in OSS. Kaushik & Chahal [6] on 'death spiral' and Chen et al. [7] on 'core contributor disengagement' are mentioned but their relationship to the current work is unclear.
  Action: Add a dedicated subsection on prior trajectory analysis in OSS. Clarify how the founder fade curve differs from existing measures of contributor turnover. Position the work more precisely within the OSS sustainability literature.
- [MINOR] (scope) The paper focuses exclusively on commit share as the involvement metric, ignoring other dimensions of founder influence such as code review, architectural decisions, community mentorship, and governance. A founder may fade from commits while maintaining influence through other channels.
  Action: Discuss this limitation explicitly. Propose future work to incorporate multi-dimensional involvement metrics (reviews, issues, governance decisions). Consider whether 'fade' should be measured as decline in any form of influence, not just commits.
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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/review_paper/review_paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 01:44:25 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-research-tools · 2026-08-21 01:44:37 UTC

The agent loaded the **aii-web-research-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-research-tools
description: "Comprehensive web research toolkit — use whenever a task needs MORE than a handful of WebSearch/WebFetch calls (multi-source literature reviews, deep verification across many pages, paper/PDF mining, cross-referencing claims, building bibliographies). Not for single quick lookups — use raw WebSearch/WebFetch for those. Adds aii_web_tools__fetch_grep for exact regex extraction over HTML or PDFs (arXiv, journals) with context windows, beyond what WebFetch's lossy summary returns. Trigger: any extensive/comprehensive/deep research task, literature review, multi-source investigation, verify many citations, arxiv, paper, PDF, exact quote, methodology, table value, regex."
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
