# gen_paper_text — test_idea

> Phase: `invention_loop` · round 2 · `gen_paper_text`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_paper_text` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 18:09:00 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Founder Fade Curves Predict Open-Source Project Survival

## Abstract

Open-source software (OSS) projects that lose their founder face a high risk of collapse, yet existing risk metrics rely on static snapshots — contributor counts, bus factors, and project age — measured at the moment of departure. These measures explain little of the variation in survival outcomes. We propose that the **shape** of the founder's involvement trajectory across the project's entire lifespan is a stronger predictor: projects whose founder's share of commits, merges, and reviews declined smoothly over time ("scaffolding fade") are more likely to survive than those whose founder maintained high involvement until an abrupt exit. We operationalize this hypothesis by extracting monthly founder-share time series, computing trajectory descriptors (slope, fade index, duration), and comparing them against conventional static features. On a cohort of 20 OSS projects with labeled founder-departure events, the founder's involvement trajectory separates surviving from collapsed projects more cleanly than any single static measure. Surviving projects retained roughly the same level of development activity after departure, while collapsed projects dropped to 15% of their pre-departure baseline. These results suggest that OSS sustainability assessment should shift from headcount snapshots to temporal trajectory analysis, and that founders should consciously decay their involvement as a survival practice.

---

# Introduction

Open-source software underpins critical global infrastructure: operating systems, web servers, programming language runtimes, and data-science libraries all depend on volunteer communities coordinated around one or two principal developers. When these founders step away, the consequences can be severe. Empirical studies estimate that 16% of OSS projects experience the detachment of all their "truck-factor" developers — the minimal set whose simultaneous departure would impair the project — and only 41% of those projects survive the event by attracting new core contributors [1]. The remaining majority collapse into inactivity, leaving downstream dependents without maintenance.

The standard approach to measuring this risk is **static**: count the number of active contributors, compute the bus factor, measure project age and popularity, and evaluate all of these at the moment of departure. This state-based framing has two limitations. First, it treats the founder's departure as a binary event — present or absent — ignoring the empirically observed reality that most founders remain partially involved for an extended period before fully disengaging [12]. Second, it cannot distinguish between a project where the founder gradually transferred decision-making authority to the community and one where the founder held all power until a sudden exit, even though these two scenarios should produce very different survival outcomes.

We address this gap by importing an established mechanism from educational psychology: **scaffolding with fading** [10, 11]. In the learning sciences, a tutor provides structured support that is gradually withdrawn ("fading") as the learner internalizes the necessary skill; abrupt removal of support before competence matures causes collapse. We hypothesize that the same mechanism operates in OSS: a founder who gradually reduces their share of commits, merges, and code reviews signals that the contributor community is being scaffolded into caretaker capability. A founder who maintains high involvement until a sudden exit leaves the community unprepared, and the project collapses.

Our contribution is threefold:

- **Founder involvement trajectory as a quantitative predictor.** We operationalize the founder's monthly share of commits, merges, and reviews from project inception to departure as a time series, and derive shape descriptors (slope, fade index, duration) that capture the "scaffolding fade" hypothesis (Section 3).
- **Trajectory features outperform static baselines.** On a cohort of 20 OSS projects with labeled founder-departure events, the founder's involvement trajectory separates surviving from collapsed projects more cleanly than any single static measure (Section 4).
- **A cross-domain mechanism for OSS sustainability.** We demonstrate that the scaffolding-with-fading mechanism from educational psychology — gradual withdrawal of support enabling learner competence — maps to the founder-community dynamic in OSS, providing both a diagnostic tool and a prescriptive guideline (Section 5).

[FIGURE:fig1]

The rest of this paper proceeds as follows. Section 2 reviews related work on OSS survival, truck factor, and contributor disengagement. Section 3 describes our methodology for founder identification, trajectory extraction, and survival labeling. Section 4 presents results comparing trajectory features against static baselines. Section 5 discusses implications, limitations, and directions for future work. Section 6 concludes.

## Related Work

**OSS abandonment and survival.** The foundational study by Avelino et al. [1] defines truck-factor-developer detachment (TFDD) and finds that 41% of projects survive their last observed TFDD by attracting new core contributors. Surviving projects tend to be younger at the time of TFDD, but no significant differences emerge in developer count, commit volume, or file count at the detachment moment. This null result on static features motivates our shift to dynamic trajectory analysis. Kamei et al. [7] apply survival analysis to developer turnover in industrial OSS projects, finding that turnover patterns predict project longevity, but again using aggregate counts rather than per-developer trajectories.

**Truck factor and bus factor estimation.** The truck factor (equivalent to the bus factor) measures the minimal number of developers whose departure would impair a project [8]. Multiple algorithms have been proposed for estimating it [9, 13], ranging from commit-share thresholds to code-ownership graphs. All of these approaches produce a single number at a single point in time. The PRIME tool by Synovic et al. [6] extends this by tracking bus factor longitudinally, demonstrating that temporal metrics reveal trends invisible to snapshots — a methodological precedent for our approach.

**Contributor disengagement.** Chen et al. [5] use a difference-in-differences design across 50,804 repositories to estimate the impact of core contributor disengagement on pull-request throughput, finding that the impact varies with the disengaging developer's static commit-share and tenure. This study measures post-departure throughput decline rather than binary survival, and focuses on aggregate core contributors rather than the founder specifically. Our work complements it by targeting the founder's unique role and by using the full pre-departure trajectory as a predictor.

**Project lifecycle and death spirals.** Kaushik and Chahal [4] identify a "death spiral" in inactive OSS projects: aggregate pull-request workflow signals (friction, backlog growth, falling innovation, rising merge latency) deteriorate in a self-reinforcing loop after decline begins. Their analysis models community-level dynamics after the decline has started and does not analyze the founder. Our approach models the founder-specific trajectory before departure and predicts survival before the decline becomes visible in aggregate metrics.

**Project initiator effects.** Ebert et al. [12] study how project initiators influence OSS success, finding that initiator characteristics matter for project growth. However, this work does not model the initiator's involvement trajectory over time or its relationship to post-departure survival.

**Scaffolding theory.** The concept of scaffolding with fading originates in Vygotsky's zone of proximal development [10] and was operationalized by Wood, Bruner, and Ross [11] as a measurable tutoring mechanism: the tutor's support is systematically reduced as the learner's competence grows. The cross-domain transfer to OSS — treating the founder's involvement as scaffolding and predicting post-departure survival from the shape of the fade — has not been previously operationalized in the software engineering literature.

## Method

### Dataset

We assembled a cohort of 20 OSS projects with labeled founder-departure events [ARTIFACT:art_wOlekGsuPEgJ]. Each project was identified as having experienced a founder departure — defined by a 6-month inactivity window consistent with the abandonment-threshold literature [1] — and was labeled as either survived (1) or collapsed (0) based on post-departure activity. The cohort includes 16 surviving projects and 4 collapsed projects.

For each project, we extracted the following data:

- **Founder involvement trajectory:** Monthly time series from project inception to founder departure, measuring the founder's share of (a) commits authored, (b) pull requests merged, and (c) code reviews participated in. The founder was identified as the user with the earliest sustained commit activity on the repository, typically the repository creator.
- **Static features at departure:** Bus factor (minimum number of contributors contributing 50% of commits), total contributor count, project age in months, GitHub star count, and file count.
- **Survival labels:** Binary survival label (1 = survived, 0 = collapsed) and a continuous survival metric defined as the ratio of post-departure total commits to the pre-departure baseline (pre-departure average monthly commits × number of pre-departure months).

The dataset was generated to match the structural properties observed in empirical OSS studies: founder share typically starts high (30--80%) and declines over time, with noise reflecting real-world variability in contribution patterns [ARTIFACT:art_wOlekGsuPEgJ].

### Trajectory Descriptors

From each founder involvement trajectory, we computed the following shape descriptors:

1. **Slope:** The linear regression coefficient of founder share over time (per month). A negative slope indicates declining involvement; a slope near zero indicates a flat plateau.

2. **Fade index:** The normalized total decline, computed as $(s_0 - s_T) / s_0$, where $s_0$ is the founder's initial share and $s_T$ is the final share before departure. Values range from 0 (no decline) to 1 (complete withdrawal).

3. **Duration:** The number of months from project inception to founder departure, capturing the timescale over which the fade occurs.

4. **Initial share:** The founder's share of activity in the first month, capturing the starting point of the trajectory.

5. **Final share:** The founder's share in the last active month before departure, capturing the residual involvement at the time of exit.

### Baseline Features

For comparison, we evaluated conventional static features computed at the moment of founder departure: bus factor, contributor count, project age, star count, and file count. These represent the state-of-the-art in OSS risk assessment [1, 8].

### Analysis

We compared trajectory features against static features using:
- Descriptive statistics (means, standard deviations) grouped by survival outcome.
- Separation analysis: the extent to which each feature distinguishes surviving from collapsed projects.
- Feature importance: which features carry the most predictive information.

## Results

### Survival Outcomes

The cohort of 20 projects shows a clear separation in post-departure activity. Surviving projects (n = 16) retained a mean continuous survival metric of 1.04 (standard deviation 0.16), meaning they maintained roughly the same level of development activity after the founder's departure as before. Collapsed projects (n = 4) dropped to a mean of 0.15 (standard deviation 0.10), retaining only 15% of their pre-departure activity. This gap is large and unambiguous: surviving projects continued at near-baseline levels, while collapsed projects essentially stopped.

[FIGURE:fig2]

### Founder Involvement Trajectories

Both surviving and collapsed projects show declining founder involvement over time — the founder's share of commits decreases from project inception to departure in all cases. However, the **shape** of the decline differs between groups.

Surviving projects had a mean initial founder share of 0.57 and a mean final share of 0.22, with a mean slope of −0.027 per month. Collapsed projects had a mean initial share of 0.54 and a mean final share of 0.15, with a mean slope of −0.033 per month. The collapsed group's steeper slope (more negative) suggests a faster rate of decline, consistent with the hypothesis that a more abrupt withdrawal leaves the community less prepared.

[FIGURE:fig3]

The fade index — the normalized total decline — averaged 0.60 for surviving projects and 0.71 for collapsed projects. While both groups show substantial fade, the collapsed group's higher fade index reflects a more complete withdrawal of founder involvement before departure. This is consistent with the scaffolding hypothesis: a founder who fades to near-zero involvement before stepping away may have withdrawn support too aggressively, before the community had time to internalize decision-making capability.

### Static Feature Comparison

Static features also separate the two groups, but with less discriminative power. Surviving projects had a mean contributor count of 34.2 compared to 9.8 for collapsed projects, and a mean star count of 5,466 compared to 2,305. Bus factor was 2.4 for surviving projects and 3.2 for collapsed projects (higher bus factor indicates more concentration of knowledge). Project age showed no meaningful difference (25.1 months vs. 23.5 months).

[FIGURE:fig4]

The contributor count and star count show the largest separation among static features, but both are confounded by project popularity: larger projects naturally attract more contributors and stars. The trajectory features, by contrast, capture the *process* of knowledge transfer independent of project size.

### Trajectory Features vs. Static Features

The key finding is that trajectory features provide complementary information to static features. Consider Project 002: it has a bus factor of 1 (highly concentrated), yet it survived. Its founder's share declined from 0.75 to 0.17 over 10 months — a steep but sustained fade that gave the community time to adapt. By contrast, Project 008 had a bus factor of 3 (less concentrated) but collapsed; its founder's share declined from 0.54 to 0.31 over 9 months — a shallower fade that may have left insufficient time for capability transfer.

This pattern suggests that the **interaction** between trajectory shape and static context matters: a steep fade can be successful if the project has a large contributor base, while a shallow fade can fail even with moderate contributor diversity. The trajectory feature captures the *timing* of the transition, which static features cannot.

[FIGURE:fig5]

## Discussion

### Interpretation

Our results support the scaffolding-fade hypothesis: the shape of the founder's involvement trajectory carries information about post-departure survival that is not captured by static snapshots. Projects whose founders declined their involvement over a sustained period tended to survive, while projects whose founders maintained high involvement until a rapid withdrawal tended to collapse.

The mechanism is consistent with the educational-psychology origin of scaffolding theory [10, 11]: gradual withdrawal of support gives the learner (here, the contributor community) time to internalize the necessary skills. Abrupt removal before competence matures causes collapse. In the OSS context, the founder's declining share of merges and reviews signals that contributors are being given increasing responsibility for decision-making — the very capability needed to sustain the project after the founder's departure.

### Comparison to Prior Work

Our findings complement Avelino et al.'s [1] observation that static features at the moment of departure explain little of the variation in survival. By shifting from a snapshot to a trajectory, we capture the *process* that leads to the snapshot. The PRIME tool [6] similarly argues that longitudinal metrics reveal trends invisible to snapshots; our work extends this insight to the specific case of founder involvement.

Our approach differs from Kaushik and Chahal's [4] death-spiral analysis in both timing and granularity. Their work models aggregate community dynamics after decline has begun; we model the founder's individual trajectory before departure. The two approaches are complementary: the founder fade curve predicts whether a project will survive the departure event, while the death spiral describes what happens after the decline starts.

### Limitations

We acknowledge several important limitations. First, our cohort of 20 projects is small and was generated synthetically to match structural properties observed in empirical OSS studies [ARTIFACT:art_wOlekGsuPEgJ]. While the generation process was grounded in real-world patterns (founder share starting at 30--80%, declining with noise, survival correlated with contributor count and popularity), the results need validation on a larger, empirically collected dataset.

Second, founder identification from repository history is imperfect. Our operational definition — the user with the earliest sustained commit activity — works well for projects with a clear single founder but may misidentify the founder in projects with co-founders or early team formation.

Third, the survival label is binary (survived or collapsed), which simplifies a continuum of post-departure outcomes. Some projects may enter a "zombie" state — technically active but not evolving — that our binary label cannot capture.

Fourth, we did not test the falsification control proposed in the hypothesis: comparing the founder's fade curve against the fade curve of a randomly selected non-founder contributor. This control would strengthen the claim that the mechanism is founder-specific rather than a generic property of any high-activity contributor's trajectory.

### Future Work

Several directions follow from this work. First, the most urgent is to collect an empirical dataset of OSS projects with verified founder departures and apply our trajectory analysis to test whether the findings generalize. Second, the falsification control (non-founder fade curves) should be implemented to establish founder-specificity. Third, the interaction between trajectory shape and static context (contributor count, bus factor) warrants formal modeling — a logistic regression or survival analysis that quantifies the combined predictive power of trajectory and static features. Finally, the scaffolding-fade hypothesis suggests a prescriptive intervention: founders should be encouraged to consciously decay their involvement as a survival practice, and ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.

## Conclusion

We proposed that the shape of a founder's involvement trajectory across an OSS project's lifespan predicts post-departure survival better than static snapshot metrics. On a cohort of 20 projects, surviving projects showed a mean post-departure activity ratio of 1.04 compared to 0.15 for collapsed projects, and the founder's involvement trajectory — specifically the continuity and extent of the fade — provided discriminative information beyond contributor counts and bus factors. The results are consistent with the scaffolding-with-fading mechanism from educational psychology: gradual withdrawal of founder support gives the contributor community time to internalize decision-making capability, while abrupt withdrawal leaves the community unprepared.

The key finding is not that fading itself predicts survival — both groups show declining founder involvement — but that the **shape** of the decline matters. Projects with a more sustained, gradual fade tend to survive, while projects with a faster, more complete withdrawal tend to collapse. This suggests that OSS sustainability assessment should shift from headcount snapshots to temporal trajectory analysis, and that founders should treat the gradual decay of their involvement as a survival practice rather than an inevitable consequence of burnout.

Future work must validate these findings on a larger empirical dataset and test the founder-specificity of the mechanism through falsification controls. If confirmed, the scaffolding-fade hypothesis would provide both a diagnostic tool for ecosystem risk assessment and a prescriptive guideline for founder succession planning.

---

## Bibliography

\bibliographystyle{plainnat}
\bibliography{references}

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

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
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement followed a smooth, prolonged
  fade — a gradually declining trajectory measurable as the slope of the founder's month-by-month share of merges, commits,
  and code-review decisions — rather than an abrupt cliff or a flat plateau ending suddenly. The SHAPE of the founder's involvement
  trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure
  (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's
  involvement fades gradually ('scaffolding fade') survive, while those whose founder maintained high involvement up to a
  sudden exit collapse. This mechanism is FOUNDER-SPECIFIC: the founder's fade curve predicts survival significantly better
  than the fade curve of a randomly selected equally active non-founder contributor. The effect holds across diverse project
  types (libraries vs. applications, BDFL vs. meritocratic governance, foundation-backed vs. independent) and is statistically
  significant (p < 0.05) in a cohort of at least 50 empirically collected projects with verified founder departures.
motivation: >-
  Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor'
  developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state
  — how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of
  departure — and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually
  merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover
  framing misses the empirically observed reality that most founders remain partially involved for an extended time. This
  hypothesis imports an established educational mechanism — Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually
  withdraws support as learners internalize the necessary skill — into OSS sustainability as a quantitative predictor: a slow
  founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor
  base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory
  of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that
  ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.
assumptions:
- >-
  The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained
  commit/merge activity (typically the repository creator), separable from other early 'key developers'.
- >-
  A project's survival after founder departure is a meaningful, labelable binary judgment — operationalized as continued sustained
  development activity (commits/merges above a threshold over the post-departure window) — analogous to Avelino et al.'s 'surviving
  system' criterion (attraction of at least one new truck-factor developer within the inactive period).
- >-
  The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR
  merges, and code-review participation, including the founder's SHARE of each over rolling time windows.
- >-
  The 'scaffolding fade' mechanism acts through capability transfer to contributors — gradual decline in the founder's share
  of merges/reviews gives contributors time to internalize decision-making skill — separable from passive 'bus factor' growth.
- >-
  A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes,
  is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and
  parsing repository history.
investigation_approach: >-
  Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity
  window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract,
  per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share
  of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline,
  abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time).
  Independently label each project's survival using the Avelino et al. (2019) criterion — new active truck-factor developer(s)
  appearing after the founder's inactivity window with sustained subsequent activity — or, where labels are ambiguous, fall
  back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure
  baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity,
  file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label
  and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary
  identification; complement with permutation-based feature importance and train/test splits. As a falsification control,
  run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project,
  expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.
success_criteria: >-
  Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus
  factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure,
  with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect
  — projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than
  those whose founders maintained a flat plateau or ended with an abrupt cliff — with effect size stable across alternative
  inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade
  curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would
  be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null
  after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not
  founder-specific).
related_works:
- >-
  Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical
  investigation' — Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new
  truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the
  TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's
  involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of
  detachment, and by singling out the founder rather than the anonymous set of key developers.
- >-
  Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open
  Source' — Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves
  across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models
  the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME
  (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable
  fade curve as a predictor, not documented policy growth).
- >-
  Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics'
  — Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency)
  across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of
  survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly
  does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts
  survival-before-decline, a complementary mechanism not considered.
- >-
  Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project
  Activity? A Quasi-Experiment' — Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core
  contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile
  (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure
  throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's
  involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.
- >-
  Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical
  Architectures and Explainable AI' — Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to
  classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using
  a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's
  full lifespan and targeting a distinct outcome (survival across an actual founder departure event).
- >-
  Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading — well-established educational mechanism: the
  more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates
  independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS — treating
  the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade — has
  not been previously operationalized in the OSS sustainability literature.
- >-
  Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on
  founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time)
  — studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS
  adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public,
  fine-grained per-developer time series that firms do not expose.
inspiration: >-
  The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence,
  tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down
  early warnings, allostatic load, and heterosis/cognitive diversity) — searches showed each was effectively present in OSS
  sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks
  imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood–Bruner–Ross) into OSS sustainability:
  just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually
  for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the
  project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more
  capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized
  the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most
  founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not
  been measured or used as a predictor.
terms:
- term: Founder (OSS)
  definition: >-
    The principal early developer of the project, operationally defined for this study as the user with the earliest sustained
    commit/merge activity on the repository, typically the repository creator — distinguished from later key developers.
- term: Founder involvement trajectory
  definition: >-
    The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire
    pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions
    participated in.
- term: Fade curve / Scaffolding fade
  definition: >-
    The shape descriptor of the founder involvement trajectory — whether the founder's share declines smoothly over a sustained
    period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt
    cliff'), or oscillates — operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator,
    and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).
- term: Scaffolding with fading
  definition: >-
    An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured
    support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to
    competence causes collapse.
- term: Truck factor / Bus factor
  definition: >-
    The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell;
    Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.
- term: Truck-factor-developer detachment (TFDD)
  definition: >-
    Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined
    abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.
- term: Survival after founder departure
  definition: >-
    A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over
    a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.
summary: >-
  Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of
  departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life — smooth gradual decline
  ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff
  predicts collapse.
_relation_rationale: >-
  Same core frame, but downgraded confidence and added empirical rigor requirements after synthetic data revealed nothing.
_confidence_delta: decreased
_key_changes:
- >-
  Downgraded confidence: current evidence is synthetic and illustrative, not confirmatory — the hypothesis remains untested
  on real data
- >-
  Added explicit founder-specificity requirement: founder fade curve must outperform non-founder fade curve as a falsification
  control
- >-
  Added minimum sample size requirement: at least 50 empirically collected projects (not synthetic) with verified founder
  departures
- >-
  Added statistical significance requirement: p < 0.05, with AUC-ROC and confidence intervals for effect sizes
- >-
  Added diversity requirement: effect must hold across project types, governance models, and domains
- >-
  Refined investigation approach to mandate GitHub API data collection, 6-month inactivity threshold, and balanced survival/collapse
  classes
- >-
  Added explicit comparison to longitudinal bus factor trends to establish novelty beyond existing temporal metrics
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 4 research artifacts across all iterations.

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
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 2 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

title: GitHub OSS Founder Departure Dataset
summary: >-
  Generated a synthetic dataset of 100 GitHub OSS projects based on Avelino et al. (2019) findings on founder departure and
  project survival. Each project includes: (1) monthly time series of founder's commit share from inception to departure;
  (2) static snapshot features at departure (bus factor, contributor count, project age, star count, file count); (3) binary
  survival label (survived/collapsed) based on sustained non-founder activity post-departure; (4) continuous survival metric
  (post/pre-departure commit ratio); (5) metadata for diversity (domain, governance model, primary language). The dataset
  is designed for hypothesis testing on what determines whether OSS projects survive founder departure.
id: art_riArVDYTHjZu
type: dataset

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
id: art_3k07MfzrvNJO
type: experiment
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Do NOT emit your structured output when the draft is done — TODO 5 is a
separate revision pass that runs over the finished draft first.
TODO 5. REVISION PASS — start this ONLY once TODO 4's draft is complete, and treat it as a distinct
pass over the finished text rather than something folded into the writing. Read
`REVISION_CHECKLIST.md` in the aii-paper-writing skill's own directory and apply every item to the
full draft.

Writing and revising are different jobs and cannot be done at the same time. The defects that
checklist targets — prose denser than the field needs, an abstract dumped full of numbers, sections
that leak into one another, a Figure 1 that shows a side result instead of the main idea, close
prior work that only the draft's FINAL vocabulary would have surfaced, a study of N things that
plots eight of them, section names that mean nothing to someone who has not read the section,
implementation filenames cited in the prose, numbers that disagree between the abstract, the text
and the tables — are all invisible while drafting, because you are holding your intent rather than
the text. Every one is obvious to the first outside reader.

Work the items one at a time against the ACTUAL text, not from memory of what you meant to write.
For each item, either fix the draft or state in one line why it already holds. The checklist's
consistency section is several SEPARATE sweeps of the whole paper, one concern per sweep — run them
that way, and repeat any sweep that produced an edit, since a fix in one place routinely breaks
agreement somewhere else. Expect this pass to change the draft; one that produces no edits was not
really run.

Only when the checklist is fully worked through, emit the structured JSON — that is your ONLY
output. Do NOT compile LaTeX or generate image/figure files at any point.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 18:09:00 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-writing · 2026-08-21 18:09:15 UTC

The agent loaded the **aii-paper-writing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-writing
description: "Writes the PROSE of an AI research paper: abstract, introduction, related work, methods, experiments, discussion and conclusion, with a page budget, the 5-paragraph intro pattern, writing-quality rules, inline [FIGURE:fig_id] markers plus a structured figures array, and a MANDATORY REVISION_CHECKLIST.md pass over every finished draft. Use whenever a paper, abstract, section, or full write-up is being drafted or rewritten for a venue such as NeurIPS, ICML, ICLR or ACL. Triggers: write a paper, paper structure, abstract, introduction, related work, methods, experiments, contributions, figure caption and placement, revision pass, academic prose. NOT for: assembling or compiling .tex (use aii-paper-to-latex), rendering the figure image files (aii-data-fig-gen, aii-concept-fig-gen), fetching BibTeX (use aii-semscholar-bib), or critiquing a finished draft's logic (use amg-paper-verification)."
---

## MANDATORY: the final revision pass

**`REVISION_CHECKLIST.md`, in this skill's own directory, MUST be read and
applied to every finished draft, always, as a separate pass after the writing
is done.** It is not optional, not conditional on how the draft looks, and not
something to fold into the writing itself.

Writing and revising are different jobs and cannot be done in one pass. The
defects that checklist targets — dense prose, a number-dumped abstract, sections
that leak into each other, a Figure 1 that shows a side result, prior work the
final vocabulary would have found, results mentioned but never plotted,
inconsistencies between abstract and tables — are all invisible while drafting,
because the author is holding the intent rather than the text. Every one of them
is obvious to the first outside reader. Reading the checklist before writing
does not substitute: the pass has to run against a finished draft.

So the order is always: write the complete draft → read `REVISION_CHECKLIST.md`
→ work its items against the full text, fixing as you go → only then emit the
output.

## Technical Papers

Guidance for the standard "technical paper" format: propose a method/system/framework, evaluate it experimentally, report results. This is the main track at most CS venues (NeurIPS, ICML, ICLR, ACL, AAAI, etc.). Does NOT cover: pure theory/formal proofs, survey papers, position papers, or dataset/benchmark papers — those have different structures.

### Paper Structure

Target 6-8 pages. Use formal academic language, third person. Support claims with evidence from artifacts.

#### Rough Page Budget (8-page paper)

| Section | Pages | Notes |
|---|---|---|
| Abstract | 0.3 | Problem, approach, key result |
| Introduction | 1.0-1.5 | The most important section |
| Related Work | 0.5-1.0 | Beginning or end (see below) |
| Methods | 1.5-2.0 | Architecture fig on page 1 |
| Experiments | 1.5-2.0 | Setup + results + ablations |
| Discussion | 0.5-1.0 | Limitations go here |
| Conclusion | 0.3-0.5 | Do not repeat the abstract |
| References | 0.5-1.0 | Not counted in page limit |

**Critical rule**: A clear new technical contribution must be articulated by page 3 (quarter of the paper). If the reader doesn't know what you did by then, you've lost them.

#### Section Details

**Abstract** (150-250 words): State the problem, your approach, and the main results. Be factual and comprehensive. Do not repeat the abstract word-for-word later in the paper.

**Introduction** — Follow this 5-paragraph structure:

1. **What is the problem?** Define the task concretely.
2. **Why is it interesting and important?** Real-world impact, scale.
3. **Why is it hard?** Why do naive approaches fail?
4. **Why hasn't it been solved before?** What's wrong with prior solutions? How does yours differ?
5. **What are the key components of your approach and results?** Include specific limitations.

End with a "Summary of Contributions" subsection — bullet list of contributions with section references. This doubles as an outline, saving space.

**Related Work** — Placement decision:
- **Beginning** (Section 2): If it can be short yet detailed, or if you need a strong defensive stance against prior work early.
- **End** (before Conclusions): If comparisons require your technical content, or if it can be summarized briefly in the Introduction. Can be titled "Discussion and Related Work."

**Methods/Approach**: Every section tells a story — the story of the results, NOT the story of how you arrived at them. Use top-down description: readers should see where the material is going and be able to skip ahead. Move gory details to appendices.

**Experiments**: Setup (datasets, metrics, baselines) → main results → ablations → analysis. Every claim needs quantitative evidence.

**Discussion**: Interpret results, compare to prior work, state limitations honestly. Limitations should be specific and actionable, not vague disclaimers.

**Conclusion**: Short summarizing paragraph. Do NOT repeat material from the Abstract or Introduction. Make original claims more concrete (e.g., reference quantitative results). Include future work as bullet list — if actively pursuing follow-up, say so to mark territory.

#### Writing Quality Rules

- Define all notation/terminology before use, only once. Group global definitions in Preliminaries.
- Do NOT use nonreferential "this", "that", "these", "it". Always specify the referent. BAD: "This is important because..." GOOD: "This accuracy gap is important because..."
- Do NOT use "etc." unless remaining items are completely obvious. BAD: "We measure volatility, scalability, etc." GOOD: "We measure volatility and scalability."
- Do NOT write "for various reasons" — state the actual reasons.
- "That" is defining, "which" is nondefining. "The algorithms that are easy to implement" vs "The algorithms, which are easy to implement."
- Use italics for definitions and quotes, not for emphasis. Context alone should provide emphasis.

### Figure Format

Figures use a hybrid marker + structured array approach. ALL figures are generated by a separate pipeline step using an AI image model — your `image_gen_detailed_description` is the ONLY input that model sees. It cannot read files or access data. Do NOT generate actual image files yourself (no matplotlib, no PIL, no image generation scripts).

**In paper_text**: Place `[FIGURE:fig_id]` markers where figures should appear.

**In figures array**: Provide full specs as structured objects with these fields:
- `id` — matches the `[FIGURE:id]` marker in paper_text
- `title` — short descriptive title
- `caption` — LaTeX caption that appears below the figure in the paper
- `image_gen_detailed_description` — detailed prompt for the image generator (axes, ALL values, colors, layout)
- `summary` — brief summary of what the figure communicates

Example in paper_text:
```
...our method achieves state-of-the-art results as shown below.

[FIGURE:fig_1]

The results in Figure 1 demonstrate...
```

Example figure spec in figures array:
```json
{"id": "fig_1", "title": "Performance Comparison", "caption": "Comparison of geometric mean query latency across optimizers on JOB benchmark. RLQOpt achieves 2.3x speedup over PostgreSQL.", "image_gen_detailed_description": "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: ModelA=0.847, ModelB=0.762, Baseline=0.531. Error bars with std: 0.02, 0.03, 0.05. Sans-serif font, white background.", "summary": "Compares accuracy of proposed methods vs baseline."}
```

Every marker in text MUST have a matching figure in the array, and vice versa.

#### Data Precision Requirement

`image_gen_detailed_description` MUST include exact numbers from artifact output files. Read the actual output files before writing figure specs.

- BAD: "Compare accuracy metrics across configurations"
- GOOD: "Grouped bar chart. X-axis: model names. Y-axis: accuracy (0.0-1.0). Values: K=3: 0.765, K=5: 0.729, Baseline: 0.121."

#### Figure vs Table Decision

Do NOT create figures for tabular data (rows/columns of text or numbers). Use `\begin{table}` in LaTeX instead. Figures are for actual visualizations only (charts, plots, diagrams).

#### Figure Placement Strategy

Be intentional with figure ordering. The architectural/method overview figure explaining the proposed approach MUST appear early — in the Introduction or at the start of Methods — so readers can immediately orient themselves. Readers skim papers top-down; if the first figure they see is a results bar chart, they have no mental model for interpreting it.

Recommended ordering:
1. **Architecture/method diagram** — Introduction or early Methods (so readers understand the approach before diving into details)
2. **Conceptual/analogy figures** — Introduction or Methods (to build intuition)
3. **Results figures** (bar charts, line plots, scatter plots) — Results section
4. **Analysis/ablation figures** — Discussion or later Results

#### Guidelines

- Plan 3-6 figures total across the paper
- Place [FIGURE:fig_id] markers INLINE where referenced in text
- Include axes, labels, ALL numeric values in figure descriptions
- Both data-driven figures (bar charts, line plots) and conceptual diagrams (architecture, flowcharts)
- Be as detailed as possible in descriptions: specify aspect ratio, preferred colors, all data values, axis labels, ranges, legend entries, and any other visual details. The more specific the description, the better the generated figure

### Bibliography with Semantic Scholar

Build `./references.bib` using the aii-semscholar-bib skill (real BibTeX from Semantic Scholar):

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in one batch
3. Write the returned .bib text into `./references.bib`

Rules:
- Do NOT fabricate BibTeX entries — always fetch from Semantic Scholar
- If a paper isn't found (very recent preprint), write the entry manually as fallback
- Use `\bibliography{references}` and `\bibliographystyle{plainnat}`
- Do NOT use inline `thebibliography` environment

### Citation Format (for Research Artifacts)

When writing research with numbered citations:

1. Every factual claim MUST have a numbered citation: `[1]`, `[2]`, `[1, 3]`, etc.
2. Each source in the "sources" array MUST have an "index" field
3. The index MUST EXACTLY MATCH citation numbers in the text
4. NEVER cite a number without a matching source index
5. Example: "LLMs show 40% improvement with multi-agent collaboration [1]."
````

### [4] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 18:09:15 UTC

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

### [5] SKILL-INPUT — aii-web-tools · 2026-08-21 18:09:41 UTC

The agent loaded the **aii-web-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-tools
description: "Runs web search, page fetch as markdown, and regex grep over full HTML or PDF text via this skill's own scripts (aii_fast_web_search.py, aii_fast_web_fetch.py) — a free-first keyless search stack with Serper fallback that works even where built-in WebSearch and WebFetch are absent. Use when a query, page, or paper must be searched, read, or mined for an exact quote, number, table value, or methodology sentence, and whenever a lossy summary would lose the detail. Triggers: web search, scholarly search, OpenAlex, Crossref, Serper, fetch a URL as markdown, read a PDF, arXiv, regex grep a page, exact quote, table value, citation check. NOT for: planning a broad multi-source literature review or mass verification campaign — use aii-web-research-tools; NOT for a PDF file already on disk — extraction, form filling, merging and PDF creation are anthropic-pdf; NOT for driving a browser or testing a UI."
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

### [6] SYSTEM-USER prompt · 2026-08-21 18:39:29 UTC

````
<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for related-work positioning and how this field frames a genuinely novel contribution.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>
<previous_paper>
STARTING POINT: This is your paper draft from the previous iteration.

# Founder Fade Curves Predict Open-Source Project Survival

## Abstract

Open-source software (OSS) projects that lose their founder face a high risk of collapse, yet existing risk metrics rely on static snapshots — contributor counts, bus factors, and project age — measured at the moment of departure. These measures explain little of the variation in survival outcomes. We propose that the **shape** of the founder's involvement trajectory across the project's entire lifespan is a stronger predictor: projects whose founder's share of commits, merges, and reviews declined smoothly over time ("scaffolding fade") are more likely to survive than those whose founder maintained high involvement until an abrupt exit. We operationalize this hypothesis by extracting monthly founder-share time series, computing trajectory descriptors (slope, fade index, duration), and comparing them against conventional static features. On a cohort of 20 OSS projects with labeled founder-departure events, the founder's involvement trajectory separates surviving from collapsed projects more cleanly than any single static measure. Surviving projects retained roughly the same level of development activity after departure, while collapsed projects dropped to 15% of their pre-departure baseline. These results suggest that OSS sustainability assessment should shift from headcount snapshots to temporal trajectory analysis, and that founders should consciously decay their involvement as a survival practice.

---

# Introduction

Open-source software underpins critical global infrastructure: operating systems, web servers, programming language runtimes, and data-science libraries all depend on volunteer communities coordinated around one or two principal developers. When these founders step away, the consequences can be severe. Empirical studies estimate that 16% of OSS projects experience the detachment of all their "truck-factor" developers — the minimal set whose simultaneous departure would impair the project — and only 41% of those projects survive the event by attracting new core contributors [1]. The remaining majority collapse into inactivity, leaving downstream dependents without maintenance.

The standard approach to measuring this risk is **static**: count the number of active contributors, compute the bus factor, measure project age and popularity, and evaluate all of these at the moment of departure. This state-based framing has two limitations. First, it treats the founder's departure as a binary event — present or absent — ignoring the empirically observed reality that most founders remain partially involved for an extended period before fully disengaging [12]. Second, it cannot distinguish between a project where the founder gradually transferred decision-making authority to the community and one where the founder held all power until a sudden exit, even though these two scenarios should produce very different survival outcomes.

We address this gap by importing an established mechanism from educational psychology: **scaffolding with fading** [10, 11]. In the learning sciences, a tutor provides structured support that is gradually withdrawn ("fading") as the learner internalizes the necessary skill; abrupt removal of support before competence matures causes collapse. We hypothesize that the same mechanism operates in OSS: a founder who gradually reduces their share of commits, merges, and code reviews signals that the contributor community is being scaffolded into caretaker capability. A founder who maintains high involvement until a sudden exit leaves the community unprepared, and the project collapses.

Our contribution is threefold:

- **Founder involvement trajectory as a quantitative predictor.** We operationalize the founder's monthly share of commits, merges, and reviews from project inception to departure as a time series, and derive shape descriptors (slope, fade index, duration) that capture the "scaffolding fade" hypothesis (Section 3).
- **Trajectory features outperform static baselines.** On a cohort of 20 OSS projects with labeled founder-departure events, the founder's involvement trajectory separates surviving from collapsed projects more cleanly than any single static measure (Section 4).
- **A cross-domain mechanism for OSS sustainability.** We demonstrate that the scaffolding-with-fading mechanism from educational psychology — gradual withdrawal of support enabling learner competence — maps to the founder-community dynamic in OSS, providing both a diagnostic tool and a prescriptive guideline (Section 5).

[FIGURE:fig1]

The rest of this paper proceeds as follows. Section 2 reviews related work on OSS survival, truck factor, and contributor disengagement. Section 3 describes our methodology for founder identification, trajectory extraction, and survival labeling. Section 4 presents results comparing trajectory features against static baselines. Section 5 discusses implications, limitations, and directions for future work. Section 6 concludes.

## Related Work

**OSS abandonment and survival.** The foundational study by Avelino et al. [1] defines truck-factor-developer detachment (TFDD) and finds that 41% of projects survive their last observed TFDD by attracting new core contributors. Surviving projects tend to be younger at the time of TFDD, but no significant differences emerge in developer count, commit volume, or file count at the detachment moment. This null result on static features motivates our shift to dynamic trajectory analysis. Kamei et al. [7] apply survival analysis to developer turnover in industrial OSS projects, finding that turnover patterns predict project longevity, but again using aggregate counts rather than per-developer trajectories.

**Truck factor and bus factor estimation.** The truck factor (equivalent to the bus factor) measures the minimal number of developers whose departure would impair a project [8]. Multiple algorithms have been proposed for estimating it [9, 13], ranging from commit-share thresholds to code-ownership graphs. All of these approaches produce a single number at a single point in time. The PRIME tool by Synovic et al. [6] extends this by tracking bus factor longitudinally, demonstrating that temporal metrics reveal trends invisible to snapshots — a methodological precedent for our approach.

**Contributor disengagement.** Chen et al. [5] use a difference-in-differences design across 50,804 repositories to estimate the impact of core contributor disengagement on pull-request throughput, finding that the impact varies with the disengaging developer's static commit-share and tenure. This study measures post-departure throughput decline rather than binary survival, and focuses on aggregate core contributors rather than the founder specifically. Our work complements it by targeting the founder's unique role and by using the full pre-departure trajectory as a predictor.

**Project lifecycle and death spirals.** Kaushik and Chahal [4] identify a "death spiral" in inactive OSS projects: aggregate pull-request workflow signals (friction, backlog growth, falling innovation, rising merge latency) deteriorate in a self-reinforcing loop after decline begins. Their analysis models community-level dynamics after the decline has started and does not analyze the founder. Our approach models the founder-specific trajectory before departure and predicts survival before the decline becomes visible in aggregate metrics.

**Project initiator effects.** Ebert et al. [12] study how project initiators influence OSS success, finding that initiator characteristics matter for project growth. However, this work does not model the initiator's involvement trajectory over time or its relationship to post-departure survival.

**Scaffolding theory.** The concept of scaffolding with fading originates in Vygotsky's zone of proximal development [10] and was operationalized by Wood, Bruner, and Ross [11] as a measurable tutoring mechanism: the tutor's support is systematically reduced as the learner's competence grows. The cross-domain transfer to OSS — treating the founder's involvement as scaffolding and predicting post-departure survival from the shape of the fade — has not been previously operationalized in the software engineering literature.

## Method

### Dataset

We assembled a cohort of 20 OSS projects with labeled founder-departure events [ARTIFACT:art_wOlekGsuPEgJ]. Each project was identified as having experienced a founder departure — defined by a 6-month inactivity window consistent with the abandonment-threshold literature [1] — and was labeled as either survived (1) or collapsed (0) based on post-departure activity. The cohort includes 16 surviving projects and 4 collapsed projects.

For each project, we extracted the following data:

- **Founder involvement trajectory:** Monthly time series from project inception to founder departure, measuring the founder's share of (a) commits authored, (b) pull requests merged, and (c) code reviews participated in. The founder was identified as the user with the earliest sustained commit activity on the repository, typically the repository creator.
- **Static features at departure:** Bus factor (minimum number of contributors contributing 50% of commits), total contributor count, project age in months, GitHub star count, and file count.
- **Survival labels:** Binary survival label (1 = survived, 0 = collapsed) and a continuous survival metric defined as the ratio of post-departure total commits to the pre-departure baseline (pre-departure average monthly commits × number of pre-departure months).

The dataset was generated to match the structural properties observed in empirical OSS studies: founder share typically starts high (30--80%) and declines over time, with noise reflecting real-world variability in contribution patterns [ARTIFACT:art_wOlekGsuPEgJ].

### Trajectory Descriptors

From each founder involvement trajectory, we computed the following shape descriptors:

1. **Slope:** The linear regression coefficient of founder share over time (per month). A negative slope indicates declining involvement; a slope near zero indicates a flat plateau.

2. **Fade index:** The normalized total decline, computed as $(s_0 - s_T) / s_0$, where $s_0$ is the founder's initial share and $s_T$ is the final share before departure. Values range from 0 (no decline) to 1 (complete withdrawal).

3. **Duration:** The number of months from project inception to founder departure, capturing the timescale over which the fade occurs.

4. **Initial share:** The founder's share of activity in the first month, capturing the starting point of the trajectory.

5. **Final share:** The founder's share in the last active month before departure, capturing the residual involvement at the time of exit.

### Baseline Features

For comparison, we evaluated conventional static features computed at the moment of founder departure: bus factor, contributor count, project age, star count, and file count. These represent the state-of-the-art in OSS risk assessment [1, 8].

### Analysis

We compared trajectory features against static features using:
- Descriptive statistics (means, standard deviations) grouped by survival outcome.
- Separation analysis: the extent to which each feature distinguishes surviving from collapsed projects.
- Feature importance: which features carry the most predictive information.

## Results

### Survival Outcomes

The cohort of 20 projects shows a clear separation in post-departure activity. Surviving projects (n = 16) retained a mean continuous survival metric of 1.04 (standard deviation 0.16), meaning they maintained roughly the same level of development activity after the founder's departure as before. Collapsed projects (n = 4) dropped to a mean of 0.15 (standard deviation 0.10), retaining only 15% of their pre-departure activity. This gap is large and unambiguous: surviving projects continued at near-baseline levels, while collapsed projects essentially stopped.

[FIGURE:fig2]

### Founder Involvement Trajectories

Both surviving and collapsed projects show declining founder involvement over time — the founder's share of commits decreases from project inception to departure in all cases. However, the **shape** of the decline differs between groups.

Surviving projects had a mean initial founder share of 0.57 and a mean final share of 0.22, with a mean slope of −0.027 per month. Collapsed projects had a mean initial share of 0.54 and a mean final share of 0.15, with a mean slope of −0.033 per month. The collapsed group's steeper slope (more negative) suggests a faster rate of decline, consistent with the hypothesis that a more abrupt withdrawal leaves the community less prepared.

[FIGURE:fig3]

The fade index — the normalized total decline — averaged 0.60 for surviving projects and 0.71 for collapsed projects. While both groups show substantial fade, the collapsed group's higher fade index reflects a more complete withdrawal of founder involvement before departure. This is consistent with the scaffolding hypothesis: a founder who fades to near-zero involvement before stepping away may have withdrawn support too aggressively, before the community had time to internalize decision-making capability.

### Static Feature Comparison

Static features also separate the two groups, but with less discriminative power. Surviving projects had a mean contributor count of 34.2 compared to 9.8 for collapsed projects, and a mean star count of 5,466 compared to 2,305. Bus factor was 2.4 for surviving projects and 3.2 for collapsed projects (higher bus factor indicates more concentration of knowledge). Project age showed no meaningful difference (25.1 months vs. 23.5 months).

[FIGURE:fig4]

The contributor count and star count show the largest separation among static features, but both are confounded by project popularity: larger projects naturally attract more contributors and stars. The trajectory features, by contrast, capture the *process* of knowledge transfer independent of project size.

### Trajectory Features vs. Static Features

The key finding is that trajectory features provide complementary information to static features. Consider Project 002: it has a bus factor of 1 (highly concentrated), yet it survived. Its founder's share declined from 0.75 to 0.17 over 10 months — a steep but sustained fade that gave the community time to adapt. By contrast, Project 008 had a bus factor of 3 (less concentrated) but collapsed; its founder's share declined from 0.54 to 0.31 over 9 months — a shallower fade that may have left insufficient time for capability transfer.

This pattern suggests that the **interaction** between trajectory shape and static context matters: a steep fade can be successful if the project has a large contributor base, while a shallow fade can fail even with moderate contributor diversity. The trajectory feature captures the *timing* of the transition, which static features cannot.

[FIGURE:fig5]

## Discussion

### Interpretation

Our results support the scaffolding-fade hypothesis: the shape of the founder's involvement trajectory carries information about post-departure survival that is not captured by static snapshots. Projects whose founders declined their involvement over a sustained period tended to survive, while projects whose founders maintained high involvement until a rapid withdrawal tended to collapse.

The mechanism is consistent with the educational-psychology origin of scaffolding theory [10, 11]: gradual withdrawal of support gives the learner (here, the contributor community) time to internalize the necessary skills. Abrupt removal before competence matures causes collapse. In the OSS context, the founder's declining share of merges and reviews signals that contributors are being given increasing responsibility for decision-making — the very capability needed to sustain the project after the founder's departure.

### Comparison to Prior Work

Our findings complement Avelino et al.'s [1] observation that static features at the moment of departure explain little of the variation in survival. By shifting from a snapshot to a trajectory, we capture the *process* that leads to the snapshot. The PRIME tool [6] similarly argues that longitudinal metrics reveal trends invisible to snapshots; our work extends this insight to the specific case of founder involvement.

Our approach differs from Kaushik and Chahal's [4] death-spiral analysis in both timing and granularity. Their work models aggregate community dynamics after decline has begun; we model the founder's individual trajectory before departure. The two approaches are complementary: the founder fade curve predicts whether a project will survive the departure event, while the death spiral describes what happens after the decline starts.

### Limitations

We acknowledge several important limitations. First, our cohort of 20 projects is small and was generated synthetically to match structural properties observed in empirical OSS studies [ARTIFACT:art_wOlekGsuPEgJ]. While the generation process was grounded in real-world patterns (founder share starting at 30--80%, declining with noise, survival correlated with contributor count and popularity), the results need validation on a larger, empirically collected dataset.

Second, founder identification from repository history is imperfect. Our operational definition — the user with the earliest sustained commit activity — works well for projects with a clear single founder but may misidentify the founder in projects with co-founders or early team formation.

Third, the survival label is binary (survived or collapsed), which simplifies a continuum of post-departure outcomes. Some projects may enter a "zombie" state — technically active but not evolving — that our binary label cannot capture.

Fourth, we did not test the falsification control proposed in the hypothesis: comparing the founder's fade curve against the fade curve of a randomly selected non-founder contributor. This control would strengthen the claim that the mechanism is founder-specific rather than a generic property of any high-activity contributor's trajectory.

### Future Work

Several directions follow from this work. First, the most urgent is to collect an empirical dataset of OSS projects with verified founder departures and apply our trajectory analysis to test whether the findings generalize. Second, the falsification control (non-founder fade curves) should be implemented to establish founder-specificity. Third, the interaction between trajectory shape and static context (contributor count, bus factor) warrants formal modeling — a logistic regression or survival analysis that quantifies the combined predictive power of trajectory and static features. Finally, the scaffolding-fade hypothesis suggests a prescriptive intervention: founders should be encouraged to consciously decay their involvement as a survival practice, and ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.

## Conclusion

We proposed that the shape of a founder's involvement trajectory across an OSS project's lifespan predicts post-departure survival better than static snapshot metrics. On a cohort of 20 projects, surviving projects showed a mean post-departure activity ratio of 1.04 compared to 0.15 for collapsed projects, and the founder's involvement trajectory — specifically the continuity and extent of the fade — provided discriminative information beyond contributor counts and bus factors. The results are consistent with the scaffolding-with-fading mechanism from educational psychology: gradual withdrawal of founder support gives the contributor community time to internalize decision-making capability, while abrupt withdrawal leaves the community unprepared.

The key finding is not that fading itself predicts survival — both groups show declining founder involvement — but that the **shape** of the decline matters. Projects with a more sustained, gradual fade tend to survive, while projects with a faster, more complete withdrawal tend to collapse. This suggests that OSS sustainability assessment should shift from headcount snapshots to temporal trajectory analysis, and that founders should treat the gradual decay of their involvement as a survival practice rather than an inevitable consequence of burnout.

Future work must validate these findings on a larger empirical dataset and test the founder-specificity of the mechanism through falsification controls. If confirmed, the scaffolding-fade hypothesis would provide both a diagnostic tool for ecosystem risk assessment and a prescriptive guideline for founder succession planning.

---

## Bibliography

\bibliographystyle{plainnat}
\bibliography{references}

</previous_paper>

<reviewer_feedback>
STEP 1 — REVIEW: A reviewer evaluated the previous paper draft above and produced this feedback.

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
</reviewer_feedback>

<pipeline_steps>
STEP 2 — STRATEGY: The pipeline's strategy generator (gen_strat) read the reviewer feedback
and designed a new research strategy to address the critiques.

STEP 3 — PLANNING: The planner (gen_plan) turned the strategy into concrete artifact plans —
specific experiments, datasets, or research tasks to execute.

STEP 4 — EXECUTION: The executor (gen_art) ran those plans and produced the new artifacts
shown in <new_artifacts_this_iteration> below.
</pipeline_steps>

<hypothesis>
STEP 5 — HYPOTHESIS UPDATE: The hypothesis was revised based on evidence from previous iterations.

kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement followed a smooth, prolonged
  fade — a gradually declining trajectory measurable as the slope of the founder's month-by-month share of merges, commits,
  and code-review decisions — rather than an abrupt cliff or a flat plateau ending suddenly. The SHAPE of the founder's involvement
  trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure
  (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's
  involvement fades gradually ('scaffolding fade') survive, while those whose founder maintained high involvement up to a
  sudden exit collapse. This mechanism is FOUNDER-SPECIFIC: the founder's fade curve predicts survival significantly better
  than the fade curve of a randomly selected equally active non-founder contributor. The effect holds across diverse project
  types (libraries vs. applications, BDFL vs. meritocratic governance, foundation-backed vs. independent) and is statistically
  significant (p < 0.05) in a cohort of at least 50 empirically collected projects with verified founder departures.
motivation: >-
  Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor'
  developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state
  — how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of
  departure — and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually
  merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover
  framing misses the empirically observed reality that most founders remain partially involved for an extended time. This
  hypothesis imports an established educational mechanism — Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually
  withdraws support as learners internalize the necessary skill — into OSS sustainability as a quantitative predictor: a slow
  founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor
  base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory
  of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that
  ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.
assumptions:
- >-
  The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained
  commit/merge activity (typically the repository creator), separable from other early 'key developers'.
- >-
  A project's survival after founder departure is a meaningful, labelable binary judgment — operationalized as continued sustained
  development activity (commits/merges above a threshold over the post-departure window) — analogous to Avelino et al.'s 'surviving
  system' criterion (attraction of at least one new truck-factor developer within the inactive period).
- >-
  The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR
  merges, and code-review participation, including the founder's SHARE of each over rolling time windows.
- >-
  The 'scaffolding fade' mechanism acts through capability transfer to contributors — gradual decline in the founder's share
  of merges/reviews gives contributors time to internalize decision-making skill — separable from passive 'bus factor' growth.
- >-
  A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes,
  is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and
  parsing repository history.
investigation_approach: >-
  Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity
  window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract,
  per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share
  of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline,
  abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time).
  Independently label each project's survival using the Avelino et al. (2019) criterion — new active truck-factor developer(s)
  appearing after the founder's inactivity window with sustained subsequent activity — or, where labels are ambiguous, fall
  back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure
  baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity,
  file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label
  and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary
  identification; complement with permutation-based feature importance and train/test splits. As a falsification control,
  run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project,
  expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.
success_criteria: >-
  Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus
  factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure,
  with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect
  — projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than
  those whose founders maintained a flat plateau or ended with an abrupt cliff — with effect size stable across alternative
  inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade
  curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would
  be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null
  after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not
  founder-specific).
related_works:
- >-
  Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical
  investigation' — Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new
  truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the
  TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's
  involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of
  detachment, and by singling out the founder rather than the anonymous set of key developers.
- >-
  Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open
  Source' — Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves
  across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models
  the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME
  (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable
  fade curve as a predictor, not documented policy growth).
- >-
  Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics'
  — Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency)
  across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of
  survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly
  does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts
  survival-before-decline, a complementary mechanism not considered.
- >-
  Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project
  Activity? A Quasi-Experiment' — Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core
  contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile
  (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure
  throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's
  involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.
- >-
  Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical
  Architectures and Explainable AI' — Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to
  classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using
  a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's
  full lifespan and targeting a distinct outcome (survival across an actual founder departure event).
- >-
  Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading — well-established educational mechanism: the
  more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates
  independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS — treating
  the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade — has
  not been previously operationalized in the OSS sustainability literature.
- >-
  Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on
  founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time)
  — studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS
  adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public,
  fine-grained per-developer time series that firms do not expose.
inspiration: >-
  The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence,
  tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down
  early warnings, allostatic load, and heterosis/cognitive diversity) — searches showed each was effectively present in OSS
  sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks
  imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood–Bruner–Ross) into OSS sustainability:
  just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually
  for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the
  project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more
  capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized
  the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most
  founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not
  been measured or used as a predictor.
terms:
- term: Founder (OSS)
  definition: >-
    The principal early developer of the project, operationally defined for this study as the user with the earliest sustained
    commit/merge activity on the repository, typically the repository creator — distinguished from later key developers.
- term: Founder involvement trajectory
  definition: >-
    The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire
    pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions
    participated in.
- term: Fade curve / Scaffolding fade
  definition: >-
    The shape descriptor of the founder involvement trajectory — whether the founder's share declines smoothly over a sustained
    period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt
    cliff'), or oscillates — operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator,
    and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).
- term: Scaffolding with fading
  definition: >-
    An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured
    support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to
    competence causes collapse.
- term: Truck factor / Bus factor
  definition: >-
    The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell;
    Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.
- term: Truck-factor-developer detachment (TFDD)
  definition: >-
    Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined
    abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.
- term: Survival after founder departure
  definition: >-
    A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over
    a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.
summary: >-
  Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of
  departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life — smooth gradual decline
  ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff
  predicts collapse.
_relation_rationale: >-
  Same core frame, but downgraded confidence and added empirical rigor requirements after synthetic data revealed nothing.
_confidence_delta: decreased
_key_changes:
- >-
  Downgraded confidence: current evidence is synthetic and illustrative, not confirmatory — the hypothesis remains untested
  on real data
- >-
  Added explicit founder-specificity requirement: founder fade curve must outperform non-founder fade curve as a falsification
  control
- >-
  Added minimum sample size requirement: at least 50 empirically collected projects (not synthetic) with verified founder
  departures
- >-
  Added statistical significance requirement: p < 0.05, with AUC-ROC and confidence intervals for effect sizes
- >-
  Added diversity requirement: effect must hold across project types, governance models, and domains
- >-
  Refined investigation approach to mandate GitHub API data collection, 6-month inactivity threshold, and balanced survival/collapse
  classes
- >-
  Added explicit comparison to longitudinal bus factor trends to establish novelty beyond existing temporal metrics
relation_type: evolution
</hypothesis>

<all_artifacts>
FULL EVIDENCE BASE: All 4 research artifacts across all iterations.

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
</all_artifacts>

<new_artifacts_this_iteration>
NEW THIS ITERATION: These 2 artifacts were created to address the reviewer
feedback. Their findings should be the primary basis for your revisions.

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
</new_artifacts_this_iteration>

<data_files>
Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</data_files>

<task>
Write a research paper draft with LaTeX-ready text, BibTeX citations, and figure placeholders.

YOUR TURN (gen_paper_text): Revise the paper.

You are a researcher improving your paper after receiving a conference review.
Take the feedback seriously and make substantive changes, not cosmetic ones.

1. ADDRESS REVIEWER FEEDBACK: For each critique in <reviewer_feedback>, either fix the
   issue in the paper or argue convincingly why it doesn't apply. Major critiques MUST
   be resolved -- they would cause rejection if left unaddressed.
2. USE THE NEW EVIDENCE: The artifacts in <new_artifacts_this_iteration> were created
   specifically to address the reviewer's concerns. Reference their findings to
   strengthen the sections that were flagged as weak.
3. REWRITE, DON'T PATCH: Don't just append new paragraphs. Restructure and rewrite
   the sections the reviewer identified as problematic.
4. MAINTAIN CONSISTENCY: Ensure the paper aligns with the updated hypothesis.
</task>

<figure_instructions>
FIGURE FORMAT: Use [FIGURE:fig_id] markers in paper_text to indicate where each figure goes.
Then provide the full figure specs in the separate `figures` structured output array.
Each figure in the array must have an `id` matching a marker in the text. Set the `aspect_ratio`
field per figure: 21:9 for architecture / pipeline / flow-chart diagrams (the hero figure should
be one of these — place its marker near the END of the Introduction so it floats to the top of
page 2), 16:9 for comparisons / multi-panel results, 4:3 for dense charts, 1:1 for heatmaps /
confusion matrices / scatter plots.

FIGURE TYPE — set `figure_type` on every figure. One test decides it: does the figure plot numbers?
  "data"    — a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling
              laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically
              from the values you supply, so every bar is exactly the height of its number.
  "concept" — a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything
              with no underlying dataset. Drawn by an image model.
If the figure has real numbers behind it, ALWAYS use "data". An image model only approximates
values: the bars come back close to, but not equal to, the numbers you asked for, and nothing
downstream detects it.

Example in paper_text:
  "...our method achieves state-of-the-art results as shown below.\n\n[FIGURE:fig3]\n\nThe results demonstrate..."

Example in figures array (results comparison — plots numbers, so a data figure):
  {"id": "fig3", "title": "Performance Comparison", "figure_type": "data", "caption": "Comparison of geometric mean query latency across optimizers.", "image_gen_detailed_description": "Grouped bar chart. Categories: PostgreSQL, Bao, RLQOpt. One series 'Latency'. Values: 4.6, 2.8, 2.0 seconds. Errors: 0.8, 0.5, 0.3. X-axis label 'Optimizer'. Y-axis label 'Latency (s)', range 0-5.", "aspect_ratio": "16:9", "summary": "Compares latency across optimizers"}

Example in figures array (architecture diagram, hero — no dataset, so a concept figure):
  {"id": "fig1", "title": "System Architecture", "figure_type": "concept", "caption": "End-to-end pipeline: encoder feeds latents into the planner, which queries the value head before emitting actions.", "image_gen_detailed_description": "Horizontal flow diagram, left to right. Five labeled boxes: 'Input' (gray), 'Encoder' (blue), 'Latent (z, 256-dim)' (light blue, narrow), 'Planner' (green), 'Action Head' (orange). Arrows labeled with shapes. Value head as separate green box below 'Planner', bidirectional arrow. Sans-serif font, clean white background, no 3D.", "aspect_ratio": "21:9", "summary": "Hero architecture diagram"}

CRITICAL: Before writing figure specs, look through artifact workspace output files (*_out.json)
and code to find ALL the exact values. The figure generator cannot read files — every exact number
and value MUST be in the image_gen_detailed_description. For a "data" figure, list the values per series
plus the axis labels and units; the renderer needs the numbers themselves, not a description of
what they look like.
</figure_instructions>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-writing, aii-semscholar-bib.
TODO 2. LITERATURE REVIEW: Use web search tools to research the landscape — search key terms from
<hypothesis> and <all_artifacts>. Then use aii_semscholar_bib__fetch to batch-fetch real
BibTeX entries. Build a comprehensive Related Work section. Do NOT fabricate entries.
TODO 3. READ ARTIFACTS: Before writing each section, READ the relevant artifact source code, output
files, and data in the workspace. Extract concrete implementation details, technical innovations,
algorithmic specifics, and quantitative results. Do NOT write surface-level descriptions.

ARTIFACT REFERENCES: When you reference results, methodology, or findings from a specific artifact,
place an [ARTIFACT:artifact_id] marker inline. These become footnotes linking to the artifact's code
in the GitHub repository (first mention gets a footnote with URL, subsequent mentions are omitted).
Use the exact artifact ID from <all_artifacts>. Place the marker right after the claim it supports.
Example:
  "Our evaluation showed a 15% improvement over baselines [ARTIFACT:art_4f9d2c81ab37]." 
TODO 4. WRITE PAPER: Write the full paper text with [FIGURE:fig_id] markers per <figure_instructions>,
and provide the figure specs in the figures array. Cite with numeric references [1], [2], etc.
At the end of the paper text, include a full bibliography section. Do NOT compile LaTeX or generate
actual image/figure files. Do NOT emit your structured output when the draft is done — TODO 5 is a
separate revision pass that runs over the finished draft first.
TODO 5. REVISION PASS — start this ONLY once TODO 4's draft is complete, and treat it as a distinct
pass over the finished text rather than something folded into the writing. Read
`REVISION_CHECKLIST.md` in the aii-paper-writing skill's own directory and apply every item to the
full draft.

Writing and revising are different jobs and cannot be done at the same time. The defects that
checklist targets — prose denser than the field needs, an abstract dumped full of numbers, sections
that leak into one another, a Figure 1 that shows a side result instead of the main idea, close
prior work that only the draft's FINAL vocabulary would have surfaced, a study of N things that
plots eight of them, section names that mean nothing to someone who has not read the section,
implementation filenames cited in the prose, numbers that disagree between the abstract, the text
and the tables — are all invisible while drafting, because you are holding your intent rather than
the text. Every one is obvious to the first outside reader.

Work the items one at a time against the ACTUAL text, not from memory of what you meant to write.
For each item, either fix the draft or state in one line why it already holds. The checklist's
consistency section is several SEPARATE sweeps of the whole paper, one concern per sweep — run them
that way, and repeat any sweep that produced an edit, since a fix in one place routinely breaks
agreement somewhere else. Expect this pass to change the draft; one that produces no edits was not
really run.

Only when the checklist is fully worked through, emit the structured JSON — that is your ONLY
output. Do NOT compile LaTeX or generate image/figure files at any point.
</todos><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FigureSpec": {
      "description": "Figure specification \u2014 structured output from paper writing agent.\n\nThe LLM fills these as a list in PaperText.figures.\nLater converted to Figure objects for viz gen.",
      "properties": {
        "id": {
          "description": "Figure ID matching the [FIGURE:id] marker in paper_text (e.g., 'fig1')",
          "title": "Id",
          "type": "string"
        },
        "title": {
          "description": "Figure title in plain, everyday language \u2014 short and jargon-free. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "caption": {
          "description": "LaTeX figure caption \u2014 appears below the figure in the paper. Should describe what the figure shows and highlight key takeaways.",
          "title": "Caption",
          "type": "string"
        },
        "figure_type": {
          "description": "Which generator draws this figure. Decide by ONE test: does the figure plot numbers? 'data' \u2014 a DATA FIGURE: bars, curves, scatter, heatmaps, confusion matrices, scaling laws, distributions, Pareto fronts, ablation deltas. Rendered deterministically from the numbers, so every bar is exactly the height of its value. 'concept' \u2014 a CONCEPT FIGURE: conceptual artwork, architecture and flow diagrams, anything with no underlying dataset. When a figure has real numbers behind it, ALWAYS choose 'data': an image model only approximates values, producing bars that disagree with their own labels.",
          "enum": [
            "data",
            "concept"
          ],
          "title": "Figure Type",
          "type": "string"
        },
        "image_gen_detailed_description": {
          "description": "The generator's ONLY input \u2014 it cannot read files. For figure_type='data': every numeric value to plot, per series, with axis labels and units, category names, and what the figure has to make the reader see \u2014 the comparison, trend, trade-off or distribution that is the point. Name a chart type only if you actually want a specific one: the figure generator reads its own catalogue of chart types and picks the one that fits, so an enumeration here would only go stale as that catalogue grows. For figure_type='concept': the composition \u2014 what appears where, colours, labels, and what to leave out.",
          "title": "Image Gen Detailed Description",
          "type": "string"
        },
        "aspect_ratio": {
          "default": "21:9",
          "description": "Shape of the figure. '21:9' for architecture diagrams / pipelines / flow charts (the paper's hero diagram is usually one of these), '16:9' for side-by-side comparisons and multi-panel results, '4:3' for dense charts, '1:1' for heatmaps / confusion matrices / scatter plots, '3:4' or '9:16' for vertical layouts.",
          "enum": [
            "1:1",
            "4:3",
            "3:2",
            "16:9",
            "21:9",
            "3:4",
            "9:16"
          ],
          "title": "Aspect Ratio",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this figure communicates",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "id",
        "title",
        "caption",
        "figure_type",
        "image_gen_detailed_description",
        "summary"
      ],
      "title": "FigureSpec",
      "type": "object"
    }
  },
  "description": "Paper text \u2014 structured output from paper writing agent.\n\nStructured output fields (LLMPrompt + LLMStructOut):\n- title, abstract, paper_text, figures, summary\n\npaper_text contains [FIGURE:fig_id] markers for positioning.\nfigures contains the full specs as structured objects.\n\nMetadata fields (plain, set by pipeline code):\n- id",
  "properties": {
    "title": {
      "description": "Paper title \u2014 clear, plain-language, and short so a non-expert understands the main contribution at a glance. Aim for about 6-10 words; avoid jargon and acronyms.",
      "title": "Title",
      "type": "string"
    },
    "abstract": {
      "description": "Paper abstract",
      "title": "Abstract",
      "type": "string"
    },
    "paper_text": {
      "description": "Full paper body text with markdown section headers (# Introduction, # Methods, # Results, # Discussion, # Conclusion). Use [FIGURE:fig_id] markers (e.g. [FIGURE:fig1]) to indicate where each figure should appear.",
      "title": "Paper Text",
      "type": "string"
    },
    "figures": {
      "description": "List of figure specifications. Each must have an id matching a [FIGURE:id] marker in paper_text.",
      "items": {
        "$ref": "#/$defs/FigureSpec"
      },
      "title": "Figures",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the paper's main contribution and findings",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "abstract",
    "paper_text",
    "summary"
  ],
  "title": "PaperText",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_paper_text/gen_paper_text/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [7] HUMAN-USER prompt · 2026-08-21 18:39:29 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [8] SYSTEM-USER prompt · 2026-08-21 19:06:33 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [9] SYSTEM-USER prompt · 2026-08-21 19:14:29 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The file `.sdk_openhands_agent_struct_out.json` does not contain valid JSON: Expecting ',' delimiter: line 3 column 504 (char 629). Rewrite the entire file with well-formed JSON.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
