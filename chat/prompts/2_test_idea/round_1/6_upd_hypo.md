# upd_hypo — test_idea

> Phase: `invention_loop` · round 1 · `upd_hypo`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `upd_hypo` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 00:17:21 UTC

````
<current_hypothesis>
The hypothesis as it stands. Revise it based on the evidence below.

kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed
  a smooth, prolonged fade — a gradually declining trajectory, measurable as the slope of the founder's month-by-month share
  of merges, commits, and code-review decisions over the project's life — rather than an abrupt cliff or a flat plateau that
  ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts
  post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count,
  popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive,
  while those whose founder maintained high involvement up to a sudden exit — or withdrew abruptly with no transition period
  — collapse.
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
</all_artifacts>

<new_artifacts_this_iteration>
These 3 artifacts were created THIS iteration.

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
</new_artifacts_this_iteration>

<current_paper>
The paper draft from this iteration — represents the current state of the research story.

# The Founder Fade Curve: Trajectory Shape Predicts OSS Project Survival

## Abstract

Open-source projects frequently depend on a single founder, yet little is known about how the *shape* of that founder's involvement over time affects whether the project survives their departure. We introduce the founder fade curve — a quantitative descriptor of the trajectory of a founder's monthly share of commits, merges, and reviews prior to leaving — and test whether its shape predicts post-departure survival better than static snapshot measures such as bus factor and contributor count. We evaluate a pilot cohort of 14 curated GitHub repositories with documented founder departures (7 survived, 7 collapsed). Trajectory shape descriptors alone fail to predict survival, while static features achieve strong performance; combined, they reach the highest accuracy. Synthetic validation confirms that our descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff patterns across 30 synthetic trajectories. A falsification control using non-founder trajectories yields no founder-specific effect. These results indicate that, at pilot scale, fade-curve shape does not yet add predictive value above static measures — a finding that calls for larger-scale validation using full trajectory data from GH Archive or equivalent sources.

## 1. Introduction

Open-source software underpins global critical infrastructure. Git, the Linux kernel, Python's standard library, and thousands of widely used packages are all maintained by communities that often trace back to one or two founding developers. When such a founder departs — whether through burnout, career change, or simple exhaustion — the project faces a fork in the road: it either survives, attracting new caretakers, or it collapses into inactivity. Roughly half of projects that lose their key developers do not survive [1].

The dominant framework for measuring this risk is the Truck Factor Developer Detachment (TFDD) model [1]. TFDD defines a project's truck factor as the minimal number of developers whose simultaneous departure would critically impair the project, and identifies the moment all truck-factor developers leave as the detachment event. Projects that subsequently attract at least one new truck-factor developer are classified as surviving; others are classified as collapsed. This framework has proven useful: across 1,932 popular GitHub projects, 57% have a truck factor of 1, 16% experience a TFDD, and only 41% of detached projects survive [1]. A later study of 36,464 projects found even higher detachment rates (89%) but lower survival (27%), and reported that departures occurring early in a project's life are less likely to be survived [2].

Yet static measures — how many key developers there are at the moment of departure — explain surprisingly little of the variation in survival outcomes. Projects that survive their TFDD often have *fewer* developers, commits, and files than those that collapse [1]. This paradox suggests that something beyond a snapshot of contributor count matters. Management literature on founder-CEO succession has noted that most founders remain partially involved for an extended period after stepping down, hinting at a gradient of involvement that binary departure labels miss [3].

We hypothesize that the *shape* of the founder's involvement trajectory over the project's entire pre-departure lifespan predicts survival better than any static snapshot. Specifically, we propose that a "scaffolding fade" — a gradual, sustained decline in the founder's share of commits, merges, and review decisions — signals that the contributor community has had time to internalize decision-making capability and will sustain the project after departure. By contrast, an abrupt cliff (high involvement maintained until sudden exit) or a flat plateau ending in a sharp drop predicts collapse. This hypothesis imports an established educational mechanism: scaffolding with fading, in which a more capable tutor gradually withdraws support as the learner internalizes the necessary skill [4]. Sudden removal of support before competence matures causes collapse; gradual withdrawal allows competence to consolidate.

In this paper we present the first quantitative evaluation of the founder fade curve hypothesis. Our contributions are:

1. **A trajectory-shape descriptor pipeline** that extracts nine features from a founder's monthly involvement share time series, including slope, convexity, onset of decline, cliff indicator, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).
2. **A synthetic validation** demonstrating that the descriptor pipeline correctly classifies smooth fades, abrupt cliffs, and plateau-then-cliff patterns across 30 synthetic trajectories.
3. **A pilot empirical evaluation** on 14 curated GitHub repositories with documented founder departures (7 survived, 7 collapsed), comparing predictive performance of trajectory shape descriptors, static features, and their combination.
4. **A falsification control** using non-founder trajectories, testing whether the founder-specific mechanism hypothesis holds.

Our results show that static features achieve AUC = 0.857 via leave-one-out cross-validated logistic regression, while trajectory shape descriptors alone achieve AUC = 0.408 (below chance). Combined features reach AUC = 0.898 with Cox PH concordance = 0.92. The falsification control finds no founder-specific effect. We interpret these results as evidence that the fade curve hypothesis, while theoretically compelling, requires larger-scale validation with full trajectory data and proper survival labels before claims of predictive superiority can be supported.

[FIGURE:fig1]

## 2. Related Work

### 2.1 OSS Project Survival and Abandonment

The most influential framework for OSS survival analysis is the Truck Factor Developer Detachment (TFDD) model introduced by Avelino et al. [1]. They defined the truck factor as the minimum number of developers whose departure would critically impair project maintenance, operationalized using a greedy algorithm that adds developers in descending order of commit count until 50% of files are covered [1]. A TFDD event occurs when all truck-factor developers become inactive within a defined abandonment window. Through sensitivity analysis on 1,932 GitHub projects, they validated a 12-month inactivity threshold as optimal (precision 0.82, harmonic mean 0.66). Their key finding: 57% of projects have truck factor 1, 16% experience at least one TFDD, and only 41% of detached projects survive.

Nourry et al. [2] replicated and extended this work on 36,464 projects, finding much higher TFDD rates (89%) but lower survival (27%). They reported that projects losing core developers early in their life are less likely to survive, a finding that directly motivates our hypothesis about the importance of departure *timing* and *process*.

### 2.2 Founder Identification

Identifying the founder of an OSS project is non-trivial. Avelino et al. [5] introduced Degree of Authorship (DOA), measuring the ratio of created files to changed files at project inception. Developers with high DOA on ≥50% of files are identified as founders. This method was validated against developer surveys, achieving 84% agreement on main author identification [5]. GitHub's API provides a `repository.creator` field, but alias resolution remains imperfect: Avelino et al. [1] found a median 11% alias rate per project when mapping commit emails to GitHub accounts.

### 2.3 Trajectory and Temporal Analysis in OSS

Several recent works have analyzed temporal patterns in OSS projects, but none focus on the founder's involvement trajectory as a survival predictor. Kaushik and Chahal [6] identified a "death spiral" in inactive projects using PR workflow dynamics (friction, backlog growth, falling innovation, rising merge latency), but their analysis focuses on community-level aggregate signals *after* decline begins and does not model the founder. Chen et al. [7] used difference-in-differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput, finding that impact varies with static contributor profile (commit share, tenure) but not with dynamic trajectory. Karim et al. [8] built a hierarchical Transformer model over 24-month aggregate activity sequences to classify projects into lifecycle stages, with no mention of founders or succession. Noori et al. [9] applied NLP to GOVERNANCE.md files to document governance evolution across 637 repositories, modeling textual constitution artifacts rather than behavioral trajectories.

### 2.4 Scaffolding Theory

The educational mechanism of scaffolding with fading originates in Vygotsky's zone of proximal development [10] and was formalized by Wood, Bruner, and Ross [4]. In this framework, a more capable tutor provides structured support that is gradually withdrawn (faded) as the learner internalizes the skill. Abrupt removal of support before competence matures causes performance collapse; gradual withdrawal allows competence to consolidate. Recent work has extended scaffolding theory to human-AI collaboration [11], but no prior work has operationalized the fading mechanism in the context of OSS project sustainability.

## 3. Method

### 3.1 Problem Formulation

Given an OSS project $P$ with founder $f$, let $S_f(t)$ denote the founder's share of project activity at month $t$, defined as:

$$S_f(t) = rac{c_f(t)}{c_{total}(t)}$$

where $c_f(t)$ is the number of commits authored by $f$ in month $t$ and $c_{total}(t)$ is the total number of commits in the project in month $t$. The **founder fade curve** is the time series $\{S_f(t)\}_{t=1}^{T}$ over the pre-departure window $[1, T]$, where $T$ is the month of founder departure (defined as the first month after which the founder has zero commits for 12 consecutive months).

Our hypothesis is that the *shape* of this trajectory predicts binary survival $y \in \{0, 1\}$, where $y = 1$ if the project survives (new truck-factor developers appear and sustain activity) and $y = 0$ otherwise.

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
9. **Plateau-then-cliff indicator** ($PTC$): A composite score (0–1) that detects trajectories with a stable plateau followed by a sharp drop. Computed as: 1.0 if pre-plateau slope $< 0.02$ and mean $> 0.5$ and post-onset slope $< -0.02$; 0.6 if slope $< 0.03$ and mean $> 0.4$ and post-onset slope $< -0.01$; 0.3 if post-onset slope $< -0.02$.

A composite **fade index** ($FI$) is constructed from the raw descriptors via min-max normalization and weighted combination:

$$FI = 0.3(1 - \text{norm}(|\beta_1|)) + 0.3 \cdot \text{norm}(d_{frac}) + 0.4(1 - \text{norm}(CI))$$

where higher $FI$ indicates a smoother, more gradual fade (bounded in $[0, 1]$).

### 3.3 Static Baseline Features

Following prior work [1, 2], we compute five static features at the departure snapshot:

- **Project age** (months from first commit to departure)
- **Contributor count** (unique commit authors)
- **Total commits** (cumulative)
- **File count** (files in HEAD tree)
- **Bus factor** (greedy: number of top contributors needed to cover 50% of files)

### 3.4 Survival Labeling

We adopt the Avelino et al. [1] TFDD framework with a 12-month inactivity threshold. A project survives if, after the founder's departure month, non-founder contributors maintain at least 50% of their pre-departure average commit rate for at least 3 months of post-departure data. The survival ratio is defined as:

$$r = \frac{\text{mean post-departure non-founder commits}}{\text{mean pre-departure non-founder commits}}$$

Projects with $r \geq 0.5$ and $\geq 3$ post-departure months are labeled survived ($y = 1$); otherwise collapsed ($y = 0$).

### 3.5 Falsification Control

To test the founder-specific mechanism hypothesis, we construct a control using the most active non-founder contributor in each project (before departure). We compute their fade curve descriptors and evaluate whether the founder fade curve predicts survival better than a randomly selected high-activity contributor's curve. If the mechanism is founder-specific, the founder's fade curve should outperform the non-founder's.

### 3.6 Predictive Modeling

We fit three logistic regression models using leave-one-out cross-validation (LOOCV):

1. **Static-only**: Predictors = {project_age, contributor_count, total_commits, file_count, bus_factor}
2. **Shape-only**: Predictors = {slope, $R^2_{linear}$, normalized_slope, quadratic_coef, onset_decline, decline_duration, cliff_indicator, plateau_then_cliff, fade_index}
3. **Combined**: Predictors = static features + shape descriptors

Model performance is evaluated using AUC-ROC and accuracy. We also fit a Cox proportional hazards model (via lifelines) to assess concordance. Feature importance is computed via permutation importance.

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

### 4.2 Implementation Details

Repository history was extracted via `git log` with month-level aggregation. PR merge data was approximated from merge commits when GitHub API access was unavailable. Trajectory descriptors were computed using the pipeline described in Section 3.2. Logistic regression was implemented via scikit-learn's `LogisticRegression` with LOOCV. The Cox PH model was fit using lifelines' `CoxPHFitter`. Permutation importance was computed using scikit-learn's `permutation_importance`.

### 4.3 Synthetic Validation

Before evaluating on real projects, we validated the descriptor pipeline on 30 synthetic trajectories: 10 smooth fades (exponential decay with noise), 10 abrupt cliffs (constant until sharp drop), and 10 plateau-then-cliff (flat plateau followed by gradual decline). All 7 validation assertions passed:

- Smooth fade trajectories have mean fade index > 0.5 (actual: 0.94)
- Smooth fade trajectories have mean cliff indicator < 2.5 (actual: 0.21)
- Smooth fade trajectories have mean decline duration > 0.4 (actual: 0.58)
- Abrupt cliff trajectories have mean fade index < 0.5 (actual: 0.11)
- Abrupt cliff trajectories have mean cliff indicator > 0.5 (actual: 1.17)
- Plateau-then-cliff trajectories have mean plateau indicator > 0.3 (actual: 0.93)
- Fade index separates smooth fades from abrupt cliffs (0.94 vs 0.11)

## 5. Results

### 5.1 Predictive Performance

Table 2 summarizes the predictive performance of the three model variants.

**Table 2: Predictive performance (LOOCV) on 14-project pilot cohort.**

| Model | AUC | Accuracy | Key Features |
|-------|-----|----------|--------------|
| Static-only | 0.857 | 0.857 | contributor_count, total_commits, bus_factor |
| Shape-only | 0.408 | 0.429 | All shape descriptors |
| Combined | 0.898 | 0.786 | All features |

Static features alone achieve strong predictive performance (AUC = 0.857), with contributor count, total commits, and bus factor emerging as the most important features via permutation importance. Trajectory shape descriptors alone perform below chance (AUC = 0.408), suggesting that fade curve shape does not predict survival in this small cohort. The combined model achieves the highest AUC (0.898) but permutation importance reveals that static features dominate: contributor count (0.044), total commits (0.066), and bus factor (0.069) account for the majority of importance, while shape descriptors contribute minimally.

### 5.2 Cox Proportional Hazards

The Cox PH model fit on combined features achieves a concordance index of 0.92, indicating strong discriminatory power for time-to-event prediction. However, with only 14 projects and binary survival labels (not time-to-event), this result should be interpreted cautiously.

### 5.3 Falsification Control

The falsification control comparing founder vs. non-founder fade curves yields identical AUC values (0.408 for both), with a delta of 0.0. This result fails to support the founder-specific mechanism hypothesis: the fade curve of a randomly selected high-activity non-founder predicts survival no better than the founder's curve.

### 5.4 Case Studies

Figure 1 illustrates representative fade curves for surviving and collapsed projects. Surviving projects (node, Homebrew, bootstrap) tend to show gradual decline in founder involvement over 12-24 months before departure. Collapsed projects (request, grunt, component) often exhibit plateau-then-cliff patterns, with the founder maintaining high involvement until sudden departure.

[FIGURE:fig1]

## 6. Discussion

### 6.1 Interpretation of Results

The primary finding of this pilot study is that trajectory shape descriptors, while theoretically motivated, do not add predictive value above static features in a small cohort of 14 projects. The static-only model achieves AUC = 0.857, and adding shape descriptors improves AUC to only 0.898 — a marginal gain that disappears when permutation importance is considered. The shape-only model performs at chance (AUC = 0.408), and the falsification control finds no founder-specific effect.

This null result does not necessarily falsify the scaffolding fade hypothesis. Several factors may explain the lack of predictive power:

1. **Small sample size**: With only 14 projects, statistical power is limited. The effect size needed to detect a significant contribution from shape descriptors would be large, and the pilot may be underpowered to detect the true effect.
2. **Proxy survival labels**: While we use the Avelino et al. [1] framework, the binary survival label may not capture the nuance of project health. Some "survived" projects may be marginally active, while some "collapsed" projects may have been resurrected.
3. **Data limitations**: The pilot used git log data without GitHub API access, meaning PR merge and review data were approximated or unavailable. The composite involvement metric (40% commits, 30% merges, 30% reviews fallback to commits) may not accurately capture decision-making authority transfer.
4. **Trajectory length**: Many projects in the cohort have short pre-departure windows (<12 months), limiting the ability to distinguish gradual fade from abrupt cliff.

### 6.2 Comparison to Prior Work

Our results contrast with the static-feature-dominated findings of Avelino et al. [1], who found that surviving projects had *fewer* developers and commits at TFDD time — a paradox we cannot replicate with our small cohort. Our static-only AUC of 0.857 is consistent with the notion that static measures capture substantial predictive signal, but our shape-only null result suggests that trajectory information may require larger samples or different feature engineering to emerge.

The falsification control result (founder AUC = non-founder AUC) challenges the founder-specific mechanism claim. If the scaffolding fade mechanism is general (applicable to any high-activity contributor), then founder-specific predictors would not outperform non-founder predictors. This interpretation aligns with the observation that project survival may depend more on community structure than on any individual's fade pattern.

### 6.3 Limitations

Several limitations constrain the generalizability of our findings:

- **Cohort size**: 14 projects is far below the statistical power needed for reliable model comparison.
- **Cohort selection bias**: Projects were curated based on known founder departures, potentially oversampling dramatic cases.
- **No GitHub API access**: PR and review data were unavailable, limiting the fidelity of involvement share estimates.
- **Binary survival labels**: The TFDD framework's binary classification may not capture the continuum of project health.
- **Single metric**: We focus on commit share; merge and review shares were approximated.

### 6.4 Future Work

To properly test the founder fade curve hypothesis, we propose:

1. **Large-scale validation**: Query GH Archive/BigQuery for per-author per-month commit counts across 5,000+ repositories, enabling statistical power to detect modest effect sizes.
2. **Improved survival labels**: Use the continuous survival ratio (post/pre departure activity) rather than binary labels, and incorporate multi-year follow-up.
3. **Full trajectory data**: Use GitHub API to obtain PR merge and review data, enabling accurate computation of decision-making authority transfer.
4. **Founder-specific tests**: Compare founder fade curves against *matched* non-founder trajectories (same project, same activity level) to control for project-level confounds.
5. **Mechanism tests**: Test whether fade curve shape predicts *time to new truck-factor developer appearance*, not just binary survival.

## 7. Conclusion

We presented the first quantitative evaluation of the founder fade curve hypothesis, which posits that the shape of a founder's involvement trajectory predicts OSS project survival after departure. Our pilot study of 14 projects found that trajectory shape descriptors alone do not predict survival (AUC = 0.408), while static features achieve strong performance (AUC = 0.857). The combined model reaches AUC = 0.898, but shape descriptors contribute minimally to predictive importance. A falsification control found no founder-specific effect.

These results suggest that the scaffolding fade mechanism, while theoretically compelling, requires larger-scale validation before claims of predictive superiority can be supported. The null finding is itself valuable: it indicates that static measures currently capture most of the predictable variance in OSS survival, and that trajectory shape may only emerge as a predictor at larger sample sizes or with more nuanced survival definitions. We call for a full-scale study using GH Archive data to properly test the hypothesis.

## References

[1] Avelino, G., Constantinou, E., Valente, M.T., Serebrenik, A. (2019). On the abandonment and survival of open source projects: An empirical investigation. In *2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*, pp. 1-12. https://doi.org/10.1109/ESEM.2019.8870181

[2] Nourry, O., Kondo, M., Saito, S., Iimura, Y., Ubayashi, N., Kamei, Y. (2024). Myth: The loss of core developers is a critical issue for OSS communities. *arXiv:2412.00313*. https://doi.org/10.48550/arXiv.2412.00313

[3] Honjo, K., Kato, T. (2022). Founder-CEO succession and firm survival. *Journal of Corporate Finance*, 75, 102234.

[4] Wood, D., Bruner, J.S., Ross, G. (1976). The role of tutoring in problem solving. *Journal of Child Psychology and Psychiatry*, 17(2), 89-100. https://doi.org/10.1111/j.1469-7610.1976.tb00381.x

[5] Avelino, G., Passos, L., Hora, A.C., Valente, M.T. (2016). A novel approach for estimating Truck Factors. In *2016 IEEE 24th International Conference on Program Comprehension (ICPC)*, pp. 1-10. https://doi.org/10.1109/ICPC.2016.7503718

[6] Kaushik, M., Chahal, K. (2026). The death spiral of open source projects: A post-mortem analysis of pull request workflow dynamics. *Journal of Systems and Software*, 240, 112942. https://doi.org/10.1016/j.jss.2026.112942

[7] Chen, X., Stol, K.J., Santos, L., German, D.M., Trinkenreich, B. (2026). How does core contributor disengagement impact open source project activity? A quasi-experiment. In *Proceedings of the 2026 IEEE/ACM 48th International Conference on Software Engineering (ICSE)*.

[8] Karim, A., Lu, L., Kasaadha, R., Goggins, S. (2026). Predicting open source software sustainability with deep temporal neural hierarchical architectures and explainable AI. In *Proceedings of the 2026 IEEE International Conference on Software Maintenance and Evolution (ICSME)*.

[9] Noori, S., Chakraborti, S., Zhang, L., Frey, C. (2025). Patterns in the transition from founder-leadership to community governance of open source. In *Proceedings of the 2025 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM)*.

[10] Vygotsky, L.S. (1978). *Mind in society: The development of higher psychological processes*. Harvard University Press.

[11] Zhang, Y., et al. (2024). Towards a synergistic fading model: Adapting scaffolding theory for human-AI collaboration. *OSF Preprints*. https://doi.org/10.35542/osf.io/5eutb_v1

[12] Killick, R., Fearnhead, P., Eckley, I.A. (2012). Optimal detection of changepoints with a linear computational cost. *Journal of the American Statistical Association*, 107(500), 1590-1598.

[13] Williams, K., Cockwell, D. (2010). The truck factor. *Linux Journal*, 2010(191), 1-8.

[14] Cosentino, V., Palombi, M., Bacchelli, A., Di Penta, M., Oliveto, R. (2015). What is the truck factor of popular GitHub applications? A first assessment. *PeerJ Computer Science*, 1, e17. https://doi.org/10.7287/peerj.preprints.1233v2

[15] Gousios, G., Zaidman, A., Pinzger, M., van Deursen, A. (2014). GHTorrent: GitHub's data from a firehose. In *2014 IEEE International Working Conference on Mining Software Repositories*, pp. 1-4.
</current_paper>

<reviewer_feedback>
Feedback from the paper reviewer this iteration.

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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/upd_hypo/upd_hypo/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 00:17:21 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SYSTEM-USER prompt · 2026-08-21 00:18:07 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 1 problem — fix ALL of them at once:
  - at `relation_rationale`: 'Refining claims based on null pilot results; keeping trajectory-concept frame but dropping founder-specificity and superiority claims' is too long (at most 120 characters, got 133)
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
