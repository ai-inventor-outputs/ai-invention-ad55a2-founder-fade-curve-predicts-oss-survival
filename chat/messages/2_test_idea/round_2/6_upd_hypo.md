# upd_hypo — test_idea

> Phase: `invention_loop` · round 2 · `upd_hypo`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent, openai/agnes-2.0-flash)

### [1] CONFIG · 2026-08-21 01:49:31 UTC

```
Model: openai/agnes-2.0-flash | Session: b7f3a578-5885-432f-8405-f73a51625355 | CWD: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo | Tools: 3 | Permission: acceptEdits
```

### [2] SYSTEM PROMPT · 2026-08-21 01:49:33 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis reviser (Step 3.6: UPD_HYPO in the invention loop)

You received the current hypothesis, all artifacts, and the paper draft.
Revise the hypothesis based on what the evidence supports.

Honest revision → focused research. Inflated confidence → wasted iteration.
</your_role>
</ai_inventor_context>

You are revising a research hypothesis based on empirical evidence gathered
during an iterative invention loop. Your role is internal reflection — honest
assessment of what the evidence supports.

SCOPE: Your ONLY output is the revised hypothesis text. You do NOT run code,
produce artifacts, fix bugs, or otherwise act on the evidence yourself — the
next iteration of the invention loop will spawn fresh artifacts based on your
revised hypothesis. Reflect on the evidence and rewrite the hypothesis;
nothing else.

PRINCIPLES:
- Ground every revision in specific artifacts and results
- Treat negative and null results as valuable contributions. If the original
  approach failed, the null result IS often the contribution — frame it as
  such (e.g. "X does not improve Y under conditions Z"). Only pivot to a
  different positive claim when the evidence actually supports one; never
  fabricate a positive narrative to mask a failed approach.
- Increase specificity as evidence accumulates
- Don't inflate confidence without strong evidence
- Preserve the core AII prompt unless evidence clearly contradicts it
- Revise hypothesis text only — never attempt to address feedback by running
  code, proposing fixes, or producing artifacts; the next loop iteration
  handles all artifact generation
```

### [3] SYSTEM-USER prompt · 2026-08-21 01:49:33 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Founder Fade Curve May Complement Static Predictors of OSS Survival
hypothesis: >-
  An open-source project's post-departure survival may be enhanced by the shape of the founder's involvement trajectory, but
  this effect is likely secondary to static snapshot measures (contributor count, bus factor, project age) and requires larger-scale
  validation to confirm. Specifically, a smooth, prolonged founder fade — where the founder's share of commits, merges, and
  review decisions gradually declines over an extended pre-departure window — is hypothesized to be *complementary* to static
  features rather than superior to them. The core empirical claim is now more modest: (1) trajectory shape descriptors add
  some predictive value beyond static features in combination, rather than outperforming them alone; (2) the founder-specific
  mechanism (scaffolding fade unique to the founder's role) is not yet supported by pilot evidence and should be treated as
  an open question rather than a central prediction; (3) multi-dimensional involvement metrics (code review, architectural
  decisions, governance participation) are likely more predictive than commit share alone, and future work should incorporate
  these channels. The hypothesis is reformulated to be testable at scale with properly computed survival labels (not pre-assigned
  from public knowledge), and to acknowledge that static features already capture substantial predictive signal in small cohorts.
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
  Evolution: keeping trajectory frame but dropping superiority and founder-specificity claims per null pilot results
_confidence_delta: decreased
_key_changes:
- >-
  Dropped claim that fade curve 'outperforms' static measures; reframed as potentially complementary predictor
- >-
  Founder-specific mechanism claim downgraded from central prediction to open question (falsification control found no founder-specific
  effect)
- >-
  Added emphasis on multi-dimensional involvement metrics (reviews, governance, architectural decisions) beyond commit share
- >-
  Acknowledged that static features already achieve strong prediction (AUC=0.857) and trajectory effects may only emerge at
  larger scale
- >-
  Specified that survival labels must be computed from TFDD framework data, not pre-assigned from public knowledge (addressing
  circularity critique)
- >-
  Called for 100+ project cohort with bootstrap confidence intervals rather than 14-project pilot
relation_type: evolution
</current_hypothesis>

<all_artifacts>
Complete set of research artifacts across all iterations.

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
in_dependencies:
- id: art_oy-M28PzQPWY
  label: dataset
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
in_dependencies:
- id: art_XZccH0dIj4ss
  label: foundation
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
in_dependencies:
- id: art_501ZvV17S5Y5
  label: pilot results
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
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

id: art_H-TNs6qLkOWs
type: experiment
in_dependencies:
- id: art_oy-M28PzQPWY
  label: dataset
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

id: art_BCR-_cTiEwyd
type: research
in_dependencies:
- id: art_XZccH0dIj4ss
  label: foundation
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

id: art_eSx8EALUZo99
type: evaluation
in_dependencies:
- id: art_501ZvV17S5Y5
  label: pilot results
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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

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
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

- [MAJOR] (methodology) Survival labels still use pre-assigned 'expected_survival' values rather than computed TFDD labels. The code at line 756 explicitly sets survival_label = expected_survival, overriding computed labels. This creates circularity: the authors test whether features predict labels they assigned based on the same public knowledge used to select projects. Three projects (phantomjs, bower, grunt) showed discrepancies (computed=1, expected=0) but were forced to match expected labels.
  Action: Compute survival labels from data using the TFDD framework (12-month inactivity threshold, 50% activity retention). Use computed labels for all analyses. Report discrepancies between computed and expected labels as part of the analysis, not as overrides. This is essential for scientific validity and was flagged in the previous review but remains unaddressed.
- [MAJOR] (rigor) The sample size of 14 projects is far too small for the statistical claims made. LOOCV on 14 samples produces high variance in AUC estimates (95% CI: [0.556, 1.000] for static model). The shape-only model's AUC of 0.408 (below chance) suggests features may be systematically misleading, not just uninformative. The Cox PH concordance of 0.92 is unreliable with only 14 observations and 7 events. The paper acknowledges this but still presents results as if they are meaningful.
  Action: Either (a) expand to 100+ projects using GH Archive/BigQuery data for per-author per-month commit counts, or (b) reframe as a qualitative case study with detailed trajectory analysis rather than claiming predictive modeling. The power analysis shows N=100 is needed for 80% power - this should be the minimum for claims of predictive performance.
- [MAJOR] (novelty) A key related work is missing from the literature review. A 2025 paper titled 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' was found in Semantic Scholar and directly addresses founder transition patterns in OSS projects. This paper should be cited and discussed in Section 2 to properly position the work within the current literature.
  Action: Search for and cite the 2025 paper on founder transition patterns. Discuss how the founder fade curve hypothesis relates to and differs from findings in that work. This is essential for demonstrating thorough literature coverage and proper positioning of the contribution.
- [MAJOR] (methodology) The falsification control uses the 'most active non-founder' as comparison, but this contributor is likely a successor rather than a random high-activity contributor. The finding that founder and non-founder AUCs are identical (0.408) suggests trajectory features are not founder-specific, but the control design cannot distinguish this from features being generally uninformative. The limitation is acknowledged but the implementation remains unchanged.
  Action: Compare founder trajectories against multiple matched non-founders (same project, matched activity level and tenure) or use random contributors as control. Test whether the founder-specific effect holds when controlling for project-level factors (size, age, topic). A more rigorous control would compare founder fade curves against the average of multiple non-founder curves within the same project.
- [MAJOR] (evidence) The iter_2 scaled experiment (art_H-TNs6qLkOWs) that attempted 100+ projects is not reported in the paper. This experiment reconstructs synthetic trajectories from aggregate features and generates synthetic survival labels - a fundamentally different methodology from the real git log data approach claimed in the paper. The paper only reports the iter_1 results with N=14, despite having access to a larger-scale experiment.
  Action: Either (a) report the scaled experiment results alongside the pilot study, with clear distinction between real and synthetic data, or (b) explain why the scaled experiment was not included and what its limitations are. If the scaled experiment used synthetic labels, this should be clearly disclosed and not presented as real data analysis.
- [MINOR] (methodology) The fade index uses heuristic weights (0.3, 0.3, 0.4) that are not empirically validated. Different weight combinations may yield different results, and the composite index may not optimally capture the predictive signal. The limitation is acknowledged but no sensitivity analysis is provided.
  Action: Conduct sensitivity analysis showing how results change with different weight combinations. Consider learning weights from data rather than using arbitrary values. Report how the fade index performance varies across a grid of weight combinations.
- [MINOR] (scope) The paper focuses exclusively on commit share as the involvement metric, ignoring other dimensions of founder influence such as code review, architectural decisions, community mentorship, and governance. A founder may fade from commits while maintaining influence through other channels. The limitation is acknowledged but no multi-dimensional analysis is attempted.
  Action: Discuss this limitation more explicitly and propose a concrete multi-dimensional involvement metric for future work. Consider whether 'fade' should be measured as decline in any form of influence, not just commits. If GitHub API data is available, incorporate PR merge and review shares.
- [MINOR] (clarity) The case studies section (5.6) is underdeveloped. It mentions that surviving projects tend to show gradual decline and collapsed projects show plateau-then-cliff patterns, but provides no detailed trajectory analysis or quantitative support for these qualitative observations.
  Action: Expand Section 5.6 with detailed trajectory plots for 2-3 representative projects from each group (survived vs collapsed), showing the fade curves with annotations of key events (e.g., when new maintainers appeared, when commit rates changed). This would strengthen the qualitative argument and provide visual evidence for the hypothesis.
- [MINOR] (rigor) The sensitivity analysis shows that LOO AUCs are uniformly 1.0 (leaving out any single project yields perfect discrimination), indicating that the conclusions are fragile and driven by the small sample. This is reported but not adequately discussed in terms of its implications for the main findings.
  Action: Discuss the implications of the LOO sensitivity analysis more explicitly: if removing any single project yields perfect discrimination, the model is likely overfitting to the small sample. This should be highlighted as a key limitation that prevents drawing definitive conclusions from the pilot study.
</reviewer_feedback>



<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, crowded lanes, and the novelty bar — consult it while revising so the updated hypothesis stays genuinely novel and well-positioned.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<task>
IMPORTANT: Your ONLY output is the revised hypothesis text. Do NOT run code, produce artifacts,
fix bugs, or attempt to address the evidence yourself — the next iteration of the invention loop
will generate fresh artifacts based on your revised hypothesis. Reflect and rewrite; nothing else.

Do NOT generate a completely new hypothesis. Take the current hypothesis and REVISE it
to incorporate new evidence. Keep the core idea — refine, narrow, or strengthen it.

1. Does the evidence support the hypothesis? Narrow or broaden scope as needed.
2. Which claims now have strong evidence? Which are still unsupported?
3. Should the hypothesis become more specific based on what we've learned?
4. If reviewer feedback is provided, address the critiques directly.

STABILITY IS OK: If progress is good and evidence supports the current direction, keep the
hypothesis similar or identical. Only make substantive changes when evidence clearly calls for
them — e.g., contradictory results, fundamental reviewer critiques, or findings that refine scope.

You must also classify two kinds of edges in the research trace:

(A) The H↔H edge — how does this revised hypothesis relate to the previous one?
    Set `relation_type` (Moulines's structuralist typology) to one of:
    - "evolution": refining specialised claims, same conceptual frame
    - "embedding": previous hypothesis is now a special case of a broader frame
    - "replacement": rejecting the previous frame entirely (Kuhnian shift)
    Set `relation_rationale` to a brief justification (≤120 chars).

(B) The A↔A edges — for each artifact created THIS iteration, classify each of its
    `in_dependencies` (predecessor → dependent) using MultiCite's citation-function
    typology (Lauscher et al., NAACL 2022) — emit one entry in `artifact_relations`
    per (predecessor, dependent) pair. Predecessors are ALWAYS artifacts from EARLIER
    iterations — artifacts within one iteration run in parallel and cannot depend on
    each other, so never emit a relation between two same-iteration artifacts (it
    will be dropped):
    - "background": predecessor is treated as background context
    - "motivation": predecessor motivated this artifact's research
    - "uses": this artifact uses the predecessor's data, method, or output
    - "extends": this artifact extends the predecessor
    - "similarities": this artifact's results agree with the predecessor's
    - "differences": this artifact's results disagree with the predecessor's
    Each `relation_rationale` must be ≤120 characters.

Output the COMPLETE revised hypothesis (with the H↔H relation fields) AND the full
list of A↔A `artifact_relations` for this iteration's new artifacts.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactRelation": {
      "description": "One typed A\u2194A edge between a dependent artifact and one of its in_dependencies.\n\nMultiCite citation-function typology (Lauscher et al., NAACL 2022),\nreduced to 6 plain-English types.",
      "properties": {
        "from_id": {
          "description": "ID of the predecessor artifact (the one being depended on)",
          "title": "From Id",
          "type": "string"
        },
        "to_id": {
          "description": "ID of the dependent artifact (the new artifact this iteration)",
          "title": "To Id",
          "type": "string"
        },
        "relation_type": {
          "description": "MultiCite citation-function type for the predecessor\u2192dependent edge: 'background' \u2014 predecessor is treated as background context; 'motivation' \u2014 predecessor motivated this artifact's research; 'uses' \u2014 this artifact uses the predecessor's data, method, or output; 'extends' \u2014 this artifact extends the predecessor; 'similarities' \u2014 this artifact's results agree with the predecessor's; 'differences' \u2014 this artifact's results disagree with the predecessor's.",
          "enum": [
            "background",
            "motivation",
            "uses",
            "extends",
            "similarities",
            "differences"
          ],
          "title": "Relation Type",
          "type": "string"
        },
        "relation_rationale": {
          "description": "Brief rationale for this relation type (one short line, max 120 characters).",
          "maxLength": 120,
          "title": "Relation Rationale",
          "type": "string"
        }
      },
      "required": [
        "from_id",
        "to_id",
        "relation_type",
        "relation_rationale"
      ],
      "title": "ArtifactRelation",
      "type": "object"
    }
  },
  "description": "Revised hypothesis after reviewing iteration results.\n\nOutput matches the hypothesis dict structure so it can replace the\noriginal hypothesis in subsequent iterations.",
  "properties": {
    "title": {
      "description": "Revised hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); may be unchanged if still accurate.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "Revised hypothesis statement \u2014 what we now believe based on evidence",
      "title": "Hypothesis",
      "type": "string"
    },
    "relation_rationale": {
      "description": "Brief rationale for the H\u2194H revision type (one short line, max 120 characters).",
      "maxLength": 120,
      "title": "Relation Rationale",
      "type": "string"
    },
    "confidence_delta": {
      "description": "How confidence changed: 'increased', 'decreased', or 'unchanged'",
      "title": "Confidence Delta",
      "type": "string"
    },
    "key_changes": {
      "description": "Bullet list of specific changes made to the hypothesis",
      "items": {
        "type": "string"
      },
      "title": "Key Changes",
      "type": "array"
    },
    "relation_type": {
      "description": "Moulines's structuralist typology of this hypothesis revision: 'evolution' \u2014 refining specialised claims while keeping the same conceptual frame; 'embedding' \u2014 the previous hypothesis is now a special case of a broader frame; 'replacement' \u2014 rejecting the previous frame entirely (incommensurable, Kuhnian revolution).",
      "enum": [
        "evolution",
        "embedding",
        "replacement"
      ],
      "title": "Relation Type",
      "type": "string"
    },
    "artifact_relations": {
      "description": "Typed A\u2194A edges for this iteration's new artifacts. Emit one entry per (predecessor \u2192 dependent) edge for every in_dependency on each artifact produced this iteration.",
      "items": {
        "$ref": "#/$defs/ArtifactRelation"
      },
      "title": "Artifact Relations",
      "type": "array"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "relation_rationale",
    "confidence_delta",
    "key_changes",
    "relation_type"
  ],
  "title": "RevisedHypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-21 01:49:33 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [5] THINKING · 2026-08-21 01:51:09 UTC

```
Let me carefully analyze the evidence from the artifacts and reviewer feedback to revise the hypothesis.

Key findings from the evidence:
1. Pilot (N=14): Static features achieve AUC=0.857, shape descriptors alone achieve AUC=0.408 (below chance), combined AUC=0.898 but NRI is negative (-0.143)
2. Power analysis: N=100 needed for 80% power
3. Falsification control: founder-specific effect NOT supported (founder_AUC = non-founder_AUC = 0.41)
4. Scaled experiment (art_H-TNs6qLkOWs): Used synthetic trajectories from aggregate features with synthetic survival labels - fundamentally different methodology from real data


5. Critical issues emerged: survival labels were pre-assigned rather than computed using TFDD, the N=14 sample is insufficient, the falsification control design is flawed, and the related work on founder transition patterns is incomplete.

I'm noticing a key tension though — the scaled experiment used synthetic data generated from aggregate features with synthetic survival labels based on fade characteristics, which creates circularity since the labels are derived from the features themselves rather than from actual project outcomes.

Let me reconsider what this means for the hypothesis. The pilot found that static features alone predict survival much better than trajectory shape descriptors, and non-founder trajectories performed equally poorly. The real problem is that the N=14 sample is too small to draw firm conclusions, and the survival labels weren't properly computed. So I need to revise the hypothesis to reflect that static measures already capture substantial predictive signal at pilot scale, and the fade curve's contribution remains unconfirmed — but only with properly computed labels and a larger cohort.

The core mechanism itself is still theoretically compelling even though the pilot didn't find evidence for it. The key changes needed are acknowledging that static features already dominate prediction, dropping the founder-specific claim since both founder and non-founder fade curves performed similarly, recognizing that the pilot was underpowered rather than conclusive, and addressing the methodological issues around label computation. I should also clarify that any scaled experiment using synthetic data shouldn't be presented as equivalent to real data analysis. So the core insight is that the fade curve hypothesis isn't falsified—it just needs a much larger, properly computed dataset to test whether trajectory shape adds predictive value beyond static features, particularly for early-departure scenarios where static measures might be weakest. I'm refining the hypothesis to emphasize this more modest, testable claim and note that previous findings were underpowered.
```

### [6] ASSISTANT · 2026-08-21 01:51:09 UTC

_(empty)_

### [7] TOOL CALL — file_editor · 2026-08-21 01:51:09 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"Founder Fade Curve as a Complementary Predictor of OSS Survival\",\n  \"hypothesis\": \"An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade \u2014 where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window \u2014 is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N \u2265 100); (2) the founder-specific mechanism claim is unsupported \u2014 pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N \u2265 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.\",\n  \"relation_rationale\": \"Narrowing: static dominance confirmed at pilot scale, founder-specificity rejected by falsification, and claim restricted to large-scale properly-powered studies\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Dropped founder-specific mechanism claim \u2014 falsification control found identical AUC (0.408) for founder and non-founder trajectories\",\n    \"Acknowledged static features dominate prediction (AUC=0.857) and capture the bulk of predictable variance at pilot scale\",\n    \"Added explicit constraint that any confirming evidence requires N \u2265 100 with properly computed TFDD labels, not pre-assigned labels\",\n    \"Restricted incremental value claim to AUC improvement < 0.05, reflecting the observed non-significant NRI (-0.143)\",\n    \"Added multi-dimensional involvement metrics (reviews, governance, architectural decisions) as required future measurement channels\",\n    \"Acknowledged that iter_2 scaled experiment used synthetic trajectories/labels and cannot serve as evidence for the hypothesis\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Scaled experiment used the 14K repo dataset as candidate pool for filtering and trajectory reconstruction\"\n    },\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Scaled experiment reconstructed synthetic trajectories from aggregates vs. pilot used real git log per-month data\"\n    },\n    {\n      \"from_id\": \"art_XZccH0dIj4ss\",\n      \"to_id\": \"art_BCR-_cTiEwyd\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Verified and replaced fabricated citations from the iter_1 literature survey with real papers\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Bootstrap CI and power analysis re-analyzed the pilot experiment results from iter_1\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Evaluation revealed pilot was underpowered (20.4% power) with fragile LOO sensitivity\"\n    }\n  ]\n}\n",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [8] TOOL CALL — finish · 2026-08-21 01:51:09 UTC

```
{
  "message": "Revised hypothesis saved to the required output path. Key revisions: (1) dropped founder-specific mechanism claim \u2014 falsification control found identical AUC for founder and non-founder curves; (2) acknowledged static features dominate (AUC=0.857) and capture bulk of predictable variance; (3) restricted confirming evidence to N\u2265100 with properly computed TFDD labels; (4) limited incremental value to AUC improvement <0.05; (5) added multi-dimensional involvement metrics; (6) acknowledged iter_2 scaled experiment used synthetic data."
}
```

### [9] TOOL RESULT — file_editor · 2026-08-21 01:51:09 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json", "prev_exist": false, "old_content": null, "new_content": "{\n  \"title\": \"Founder Fade Curve as a Complementary Predictor of OSS Survival\",\n  \"hypothesis\": \"An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade \u2014 where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window \u2014 is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N \u2265 100); (2) the founder-specific mechanism claim is unsupported \u2014 pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N \u2265 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.\",\n  \"relation_rationale\": \"Narrowing: static dominance confirmed at pilot scale, founder-specificity rejected by falsification, and claim restricted to large-scale properly-powered studies\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Dropped founder-specific mechanism claim \u2014 falsification control found identical AUC (0.408) for founder and non-founder trajectories\",\n    \"Acknowledged static features dominate prediction (AUC=0.857) and capture the bulk of predictable variance at pilot scale\",\n    \"Added explicit constraint that any confirming evidence requires N \u2265 100 with properly computed TFDD labels, not pre-assigned labels\",\n    \"Restricted incremental value claim to AUC improvement < 0.05, reflecting the observed non-significant NRI (-0.143)\",\n    \"Added multi-dimensional involvement metrics (reviews, governance, architectural decisions) as required future measurement channels\",\n    \"Acknowledged that iter_2 scaled experiment used synthetic trajectories/labels and cannot serve as evidence for the hypothesis\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Scaled experiment used the 14K repo dataset as candidate pool for filtering and trajectory reconstruction\"\n    },\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Scaled experiment reconstructed synthetic trajectories from aggregates vs. pilot used real git log per-month data\"\n    },\n    {\n      \"from_id\": \"art_XZccH0dIj4ss\",\n      \"to_id\": \"art_BCR-_cTiEwyd\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Verified and replaced fabricated citations from the iter_1 literature survey with real papers\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Bootstrap CI and power analysis re-analyzed the pilot experiment results from iter_1\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Evaluation revealed pilot was underpowered (20.4% power) with fragile LOO sensitivity\"\n    }\n  ]\n}\n", "kind": "FileEditorObservation"}
```

### [10] TOOL RESULT — finish · 2026-08-21 01:51:09 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Revised hypothesis saved to the required output path. Key revisions: (1) dropped founder-specific mechanism claim \u2014 falsification control found identical AUC for founder and non-founder curves; (2) acknowledged static features dominate (AUC=0.857) and capture bulk of predictable variance; (3) restricted confirming evidence to N\u2265100 with properly computed TFDD labels; (4) limited incremental value to AUC improvement <0.05; (5) added multi-dimensional involvement metrics; (6) acknowledged iter_2 scaled experiment used synthetic data."}], "is_error": false, "kind": "FinishObservation"}
```

### [11] HOOK — PostToolUse · 2026-08-21 01:51:09 UTC

```
<system-reminder>You have 113.4 minutes remaining to finish all your tasks.</system-reminder>
```

### [12] SYSTEM-USER prompt · 2026-08-21 01:51:10 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Narrowing: static dominance confirmed at pilot scale, founder-specificity rejected by falsification, and claim restricted to large-scale properly-powered studies' is too long (at most 120 characters, got 161)
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [13] THINKING · 2026-08-21 01:51:16 UTC

```
The validation failed because `relation_rationale` exceeds 120 characters. Let me fix that field to be shorter.
```

### [14] ASSISTANT · 2026-08-21 01:51:16 UTC

_(empty)_

### [15] TOOL CALL — file_editor · 2026-08-21 01:51:16 UTC

```
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": "  \"relation_rationale\": \"Narrowing: static dominance confirmed at pilot scale, founder-specificity rejected by falsification, and claim restricted to large-scale properly-powered studies\",",
  "new_str": "  \"relation_rationale\": \"Static dominance confirmed, founder-specificity rejected by falsification, claims restricted to N>=100 powered studies\",",
  "insert_line": null,
  "view_range": null
}
```

### [16] TOOL RESULT — file_editor · 2026-08-21 01:51:16 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Invalid `path` parameter: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json. The path /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json does not exist. Please provide a valid path."}], "is_error": true, "command": "str_replace", "path": null, "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [17] THINKING · 2026-08-21 01:51:20 UTC

```
Let me check the actual path. The working directory is /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo, so the file should be at that location. But the file_editor says it doesn't exist. Let me use the terminal to check and recreate the file.
```

### [18] ASSISTANT · 2026-08-21 01:51:20 UTC

_(empty)_

### [19] TOOL CALL — terminal · 2026-08-21 01:51:20 UTC

```
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/ 2>/dev/null || echo \"Directory not found\"",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [20] TOOL CALL — terminal · 2026-08-21 01:51:20 UTC

```
{
  "command": "pwd",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [21] TOOL RESULT — terminal · 2026-08-21 01:51:22 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1\ndrwxr-xr-x 2 root root 1 Aug 21 01:51 .\ndrwxr-xr-x 3 root root 1 Aug 21 01:49 .."}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/ 2>/dev/null || echo \"Directory not found\"", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "051f147a1ea0", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/b7f3a5785885432f8405f73a51625355/observations", "kind": "TerminalObservation"}
```

### [22] TOOL RESULT — terminal · 2026-08-21 01:51:22 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo"}], "is_error": false, "command": "pwd", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "051f147a1ea0", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/b7f3a5785885432f8405f73a51625355/observations", "kind": "TerminalObservation"}
```

### [23] THINKING · 2026-08-21 01:52:50 UTC

```
The directory exists but the file was removed or not created. Let me create it again with the corrected relation_rationale.
```

### [24] ASSISTANT · 2026-08-21 01:52:50 UTC

_(empty)_

### [25] TOOL CALL — file_editor · 2026-08-21 01:52:50 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"Founder Fade Curve as a Complementary Predictor of OSS Survival\",\n  \"hypothesis\": \"An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade \u2014 where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window \u2014 is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N \u2265 100); (2) the founder-specific mechanism claim is unsupported \u2014 pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N \u2265 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.\",\n  \"relation_rationale\": \"Static dominance confirmed, founder-specificity rejected by falsification, claims restricted to N>=100 powered studies\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Dropped founder-specific mechanism claim \u2014 falsification control found identical AUC (0.408) for founder and non-founder trajectories\",\n    \"Acknowledged static features dominate prediction (AUC=0.857) and capture the bulk of predictable variance at pilot scale\",\n    \"Added explicit constraint that any confirming evidence requires N \u2265 100 with properly computed TFDD labels, not pre-assigned labels\",\n    \"Restricted incremental value claim to AUC improvement < 0.05, reflecting the observed non-significant NRI (-0.143)\",\n    \"Added multi-dimensional involvement metrics (reviews, governance, architectural decisions) as required future measurement channels\",\n    \"Acknowledged that iter_2 scaled experiment used synthetic trajectories/labels and cannot serve as evidence for the hypothesis\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Scaled experiment used the 14K repo dataset as candidate pool for filtering and trajectory reconstruction\"\n    },\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Scaled experiment reconstructed synthetic trajectories from aggregates vs. pilot used real git log per-month data\"\n    },\n    {\n      \"from_id\": \"art_XZccH0dIj4ss\",\n      \"to_id\": \"art_BCR-_cTiEwyd\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Verified and replaced fabricated citations from the iter_1 literature survey with real papers\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Bootstrap CI and power analysis re-analyzed the pilot experiment results from iter_1\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Evaluation revealed pilot was underpowered (20.4% power) with fragile LOO sensitivity\"\n    }\n  ]\n}\n",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [26] TOOL RESULT — file_editor · 2026-08-21 01:52:52 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json", "prev_exist": false, "old_content": null, "new_content": "{\n  \"title\": \"Founder Fade Curve as a Complementary Predictor of OSS Survival\",\n  \"hypothesis\": \"An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade \u2014 where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window \u2014 is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N \u2265 100); (2) the founder-specific mechanism claim is unsupported \u2014 pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N \u2265 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.\",\n  \"relation_rationale\": \"Static dominance confirmed, founder-specificity rejected by falsification, claims restricted to N>=100 powered studies\",\n  \"confidence_delta\": \"decreased\",\n  \"key_changes\": [\n    \"Dropped founder-specific mechanism claim \u2014 falsification control found identical AUC (0.408) for founder and non-founder trajectories\",\n    \"Acknowledged static features dominate prediction (AUC=0.857) and capture the bulk of predictable variance at pilot scale\",\n    \"Added explicit constraint that any confirming evidence requires N \u2265 100 with properly computed TFDD labels, not pre-assigned labels\",\n    \"Restricted incremental value claim to AUC improvement < 0.05, reflecting the observed non-significant NRI (-0.143)\",\n    \"Added multi-dimensional involvement metrics (reviews, governance, architectural decisions) as required future measurement channels\",\n    \"Acknowledged that iter_2 scaled experiment used synthetic trajectories/labels and cannot serve as evidence for the hypothesis\"\n  ],\n  \"relation_type\": \"evolution\",\n  \"artifact_relations\": [\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Scaled experiment used the 14K repo dataset as candidate pool for filtering and trajectory reconstruction\"\n    },\n    {\n      \"from_id\": \"art_oy-M28PzQPWY\",\n      \"to_id\": \"art_H-TNs6qLkOWs\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Scaled experiment reconstructed synthetic trajectories from aggregates vs. pilot used real git log per-month data\"\n    },\n    {\n      \"from_id\": \"art_XZccH0dIj4ss\",\n      \"to_id\": \"art_BCR-_cTiEwyd\",\n      \"relation_type\": \"extends\",\n      \"relation_rationale\": \"Verified and replaced fabricated citations from the iter_1 literature survey with real papers\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"uses\",\n      \"relation_rationale\": \"Bootstrap CI and power analysis re-analyzed the pilot experiment results from iter_1\"\n    },\n    {\n      \"from_id\": \"art_501ZvV17S5Y5\",\n      \"to_id\": \"art_eSx8EALUZo99\",\n      \"relation_type\": \"differences\",\n      \"relation_rationale\": \"Evaluation revealed pilot was underpowered (20.4% power) with fragile LOO sensitivity\"\n    }\n  ]\n}\n", "kind": "FileEditorObservation"}
```

### [27] THINKING · 2026-08-21 01:53:06 UTC

```
The file was created successfully. Let me verify it was written correctly by checking its contents.
```

### [28] ASSISTANT · 2026-08-21 01:53:06 UTC

_(empty)_

### [29] TOOL CALL — file_editor · 2026-08-21 01:53:06 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [30] TOOL RESULT — file_editor · 2026-08-21 01:53:06 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json:\n     1\t{\n     2\t  \"title\": \"Founder Fade Curve as a Complementary Predictor of OSS Survival\",\n     3\t  \"hypothesis\": \"An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade \u2014 where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window \u2014 is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N \u2265 100); (2) the founder-specific mechanism claim is unsupported \u2014 pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N \u2265 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.\",\n     4\t  \"relation_rationale\": \"Static dominance confirmed, founder-specificity rejected by falsification, claims restricted to N>=100 powered studies\",\n     5\t  \"confidence_delta\": \"decreased\",\n     6\t  \"key_changes\": [\n     7\t    \"Dropped founder-specific mechanism claim \u2014 falsification control found identical AUC (0.408) for founder and non-founder trajectories\",\n     8\t    \"Acknowledged static features dominate prediction (AUC=0.857) and capture the bulk of predictable variance at pilot scale\",\n     9\t    \"Added explicit constraint that any confirming evidence requires N \u2265 100 with properly computed TFDD labels, not pre-assigned labels\",\n    10\t    \"Restricted incremental value claim to AUC improvement < 0.05, reflecting the observed non-significant NRI (-0.143)\",\n    11\t    \"Added multi-dimensional involvement metrics (reviews, governance, architectural decisions) as required future measurement channels\",\n    12\t    \"Acknowledged that iter_2 scaled experiment used synthetic trajectories/labels and cannot serve as evidence for the hypothesis\"\n    13\t  ],\n    14\t  \"relation_type\": \"evolution\",\n    15\t  \"artifact_relations\": [\n    16\t    {\n    17\t      \"from_id\": \"art_oy-M28PzQPWY\",\n    18\t      \"to_id\": \"art_H-TNs6qLkOWs\",\n    19\t      \"relation_type\": \"uses\",\n    20\t      \"relation_rationale\": \"Scaled experiment used the 14K repo dataset as candidate pool for filtering and trajectory reconstruction\"\n    21\t    },\n    22\t    {\n    23\t      \"from_id\": \"art_oy-M28PzQPWY\",\n    24\t      \"to_id\": \"art_H-TNs6qLkOWs\",\n    25\t      \"relation_type\": \"differences\",\n    26\t      \"relation_rationale\": \"Scaled experiment reconstructed synthetic trajectories from aggregates vs. pilot used real git log per-month data\"\n    27\t    },\n    28\t    {\n    29\t      \"from_id\": \"art_XZccH0dIj4ss\",\n    30\t      \"to_id\": \"art_BCR-_cTiEwyd\",\n    31\t      \"relation_type\": \"extends\",\n    32\t      \"relation_rationale\": \"Verified and replaced fabricated citations from the iter_1 literature survey with real papers\"\n    33\t    },\n    34\t    {\n    35\t      \"from_id\": \"art_501ZvV17S5Y5\",\n    36\t      \"to_id\": \"art_eSx8EALUZo99\",\n    37\t      \"relation_type\": \"uses\",\n    38\t      \"relation_rationale\": \"Bootstrap CI and power analysis re-analyzed the pilot experiment results from iter_1\"\n    39\t    },\n    40\t    {\n    41\t      \"from_id\": \"art_501ZvV17S5Y5\",\n    42\t      \"to_id\": \"art_eSx8EALUZo99\",\n    43\t      \"relation_type\": \"differences\",\n    44\t      \"relation_rationale\": \"Evaluation revealed pilot was underpowered (20.4% power) with fragile LOO sensitivity\"\n    45\t    }\n    46\t  ]\n    47\t}\n    48\t\n"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [31] THINKING · 2026-08-21 01:53:41 UTC

```
The file has been created successfully with the corrected `relation_rationale` length. Let me verify the JSON is valid and the rationale is under 120 characters.
```

### [32] ASSISTANT · 2026-08-21 01:53:42 UTC

_(empty)_

### [33] TOOL CALL — finish · 2026-08-21 01:53:42 UTC

```
{
  "message": "Revised hypothesis saved successfully. Fixed the `relation_rationale` length issue (was 161 chars, now 118 chars). The revised hypothesis reflects the pilot findings: static features dominate prediction, founder-specificity was rejected by falsification, and future work requires N\u2265100 with computed TFDD labels. The iter_2 scaled experiment was acknowledged as using synthetic data and cannot serve as evidence."
}
```

### [34] TOOL CALL — think · 2026-08-21 01:53:42 UTC

```
{
  "thought": "The revised hypothesis addresses all key findings from the iteration:\n1. Dropped founder-specific claim (falsification found identical AUC for founder/non-founder)\n2. Acknowledged static dominance (AUC=0.857)\n3. Added N\u2265100 requirement with computed labels\n4. Limited incremental value to AUC <0.05\n5. Added multi-dimensional metrics requirement\n6. Acknowledged iter_2 synthetic data limitation\nThe relation_rationale was shortened to meet the 120-character limit. All artifact relations were properly classified."
}
```

### [35] TOOL RESULT — finish · 2026-08-21 01:53:42 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Revised hypothesis saved successfully. Fixed the `relation_rationale` length issue (was 161 chars, now 118 chars). The revised hypothesis reflects the pilot findings: static features dominate prediction, founder-specificity was rejected by falsification, and future work requires N\u2265100 with computed TFDD labels. The iter_2 scaled experiment was acknowledged as using synthetic data and cannot serve as evidence."}], "is_error": false, "kind": "FinishObservation"}
```

### [36] HOOK — PostToolUse · 2026-08-21 01:53:42 UTC

```
<system-reminder>You have 110.8 minutes remaining to finish all your tasks.</system-reminder>
```
