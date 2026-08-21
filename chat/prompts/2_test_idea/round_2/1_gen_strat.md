# gen_strat_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_strat`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_strat_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 17:25:48 UTC

````
<hypothesis>
Your strategy should advance this hypothesis.

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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for study design, proper baselines, and the evaluation/validity norms this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<iteration_status>
Current iteration: 2 of 2
Remaining (including this one): 1
</iteration_status>

<previous_strategies>
Strategies from the PREVIOUS iteration. You can CONTINUE these directions,
ADAPT based on what worked and what didn't in the artifacts produced, or PIVOT if results suggest a better path.

--- Strategy 1 ---
kind: strategy
id: gen_strat_1_idx1
title: Build and Test Founder Fade Curve Predictor
objective: >-
  Assemble a cohort of OSS projects with founder departures, extract founder involvement trajectories, compute fade-curve
  shape descriptors, and test whether they predict project survival better than static snapshot features.
rationale: >-
  This is iteration 1 of 2. The hypothesis requires three foundational pieces: (1) domain knowledge about how prior work defines
  founder departure and survival, (2) a curated dataset of projects with labeled founder trajectories and outcomes, and (3)
  initial experimental validation. Since the experiment depends on the dataset and no existing artifacts exist, iteration
  1 focuses on the two prerequisites: research and dataset. The research artifact runs in parallel to guide methodology choices
  (e.g., which inactivity threshold to use, how to identify founders, which GitHub API endpoints to use). The dataset artifact
  builds the cohort of projects with founder departures, extracts monthly involvement trajectories, and labels survival outcomes.
  Iteration 2 will then run the core experiment (fade-curve descriptors vs static features) and evaluation (ablations, robustness
  checks, falsification control) on top of this foundation.
artifact_directions:
- id: research_iter1_dir1
  type: research
  objective: >-
    Survey OSS sustainability literature and GitHub API capabilities to determine: (a) established methods for identifying
    project founders from repository history, (b) operational definitions of founder departure and project survival from Avelino
    et al. (2019) and subsequent work, (c) existing datasets or lists of abandoned/abandoned-then-revived OSS projects, (d)
    GitHub API endpoints and rate limits for extracting per-user commit, merge, and review histories at scale, (e) how prior
    work computes bus factor and truck factor, and (f) whether any prior work has attempted to model temporal trajectories
    of contributor involvement.
  approach: >-
    Use web search (general + scholarly modes) to find: (1) Avelino et al. 2019 paper and follow-up studies on TFDD and project
    survival, (2) GitHub API documentation for commits, pulls, and reviews endpoints, (3) existing lists or datasets of abandoned
    OSS projects (e.g., from GitHub archives, academic studies), (4) methods for founder identification in prior OSS research,
    (5) any work on temporal dynamics of contributor involvement. Synthesize findings into a structured report with specific
    recommendations for the dataset and experiment artifacts: which inactivity threshold to use (6mo vs 12mo), how to define
    survival (binary vs continuous), which GitHub endpoints to use, and potential confounds to control for.
  depends_on: []
- id: dataset_iter1_dir2
  type: dataset
  objective: >-
    Curate a cohort of 50-200 public GitHub OSS projects whose identified founder has departed, and for each project extract:
    (a) the founder's identity, (b) monthly time series of founder's share of commits, PR merges, and code reviews from inception
    to departure, (c) static snapshot features at departure (bus factor, contributor count, project age, star count, file
    count), (d) a survival label based on post-departure activity. Output standardized JSON with all features and labels.
  approach: >-
    Step 1: Identify candidate projects by searching for known lists of abandoned OSS projects from academic papers, GitHub
    archives, and community sources; supplement with a search for popular repositories (stars > 500) that show a founder with
    12+ months of inactivity. Step 2: For each candidate, clone the repository and parse git history to identify the founder
    (earliest sustained committer, typically the repo creator). Step 3: Extract monthly aggregates of: founder commits / total
    commits, founder merges / total merges, founder reviews / total reviews — from inception through the 12-month inactivity
    window. Step 4: Label survival: if the project had sustained activity (commits from non-founder contributors) in the 24
    months after the founder's inactivity window began, label as 'survived'; otherwise 'collapsed'. Also compute a continuous
    survival metric (post-departure commit volume normalized to pre-departure baseline). Step 5: Compute static snapshot features
    at the departure date. Step 6: Validate schema and output full/mini/preview JSON variants. Use parallel cloning and parsing
    to stay within the 6-hour time budget.
  depends_on: []
expected_outcome: >-
  By end of iteration 1: (1) A research report synthesizing prior work on OSS survival, founder identification methods, GitHub
  API capabilities, and recommended methodology; (2) A curated dataset of 50-200 OSS projects with founder departures, including
  monthly founder involvement trajectories, static snapshot features, and survival labels in standardized JSON. These two
  artifacts provide the foundation for iteration 2, which will run the core experiment: computing fade-curve shape descriptors,
  training predictive models, and testing whether founder fade curves outperform static features in predicting project survival.
summary: >-
  Two parallel artifacts build the foundation: research guides methodology choices, dataset curates projects and extracts
  founder involvement trajectories with survival labels. Iteration 2 will run the experiment on top of this data.
</previous_strategies>

<dependency_rules>
- depends_on is a list of objects {id, label} — each entry references an existing artifact and tags how it is being used
- "id" can ONLY reference IDs from <existing_artifacts> — never IDs you are proposing (all new artifacts run in parallel)
- "label" is a SHORT free-text type label (a word or two, NOT a sentence) describing what role the dep plays — e.g. "dataset", "validates", "extends", "supersedes". Required on every dep.
- Setting depends_on provides the dependency's out_dependency_files to your artifact at execution time
- If no suitable existing artifacts exist, use empty depends_on
- New artifact IDs are assigned by the system after submission — do not invent IDs for your proposed artifacts
</dependency_rules>

<available_artifact_types>
Artifact types you can plan. Use this to choose the right types for your strategy objectives.

<artifact_types>
RESEARCH
Web research to answer key questions — like a researcher making decisions.
Runtime: LLM Agent, no code execution.
Tools: the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text).
Capabilities: Find, synthesize, and compare information across sources; survey SOTA and best practices.
Deps: REQUIRED none | OPTIONAL other RESEARCH to build on prior findings

EXPERIMENT
Run code to test hypotheses, implement methods, and collect empirical results.
Runtime: Python 3.12, UV (any pip package), isolated workspace, gradual scaling (mini → full data).
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Implement and run any code-based experiment, compare method vs baselines.
Deps: REQUIRED at least one DATASET | OPTIONAL RESEARCH for methodology guidance

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect

EVALUATION
Evaluate experiment results with metrics, statistical analysis, and validity checks.
Runtime: Python 3.12, UV (any evaluation library), isolated workspace, gradual scaling matching experiment.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-json (schema validation), aii-openrouter-llms (call any LLM — GPT, Gemini, Llama, etc.), domain-specific as needed.
Capabilities: Compute any quantitative metrics and statistical tests, analyze validity and robustness.
Deps: REQUIRED at least one EXPERIMENT | OPTIONAL DATASET if reference data needed

PROOF
Formally prove mathematical statements in Lean 4 with automated iteration.
Runtime: LLM agent with Lean 4 compiler feedback loop.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-lean (proof verification, Mathlib search, tactics: ring, linarith, nlinarith, omega, simp, etc.)
Capabilities: Formally verify properties and inequalities, iterative proof development, lemma decomposition.
Deps: REQUIRED none | OPTIONAL RESEARCH for mathematical background
</artifact_types>
</available_artifact_types>

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

RESEARCH executor scope:
  Output: research_out.json with {answer, sources, follow_up_questions} + research_report.md
  DOES: Web research — search, read, synthesize information from papers/docs/APIs into a structured report
  DOES NOT: Run code, download files, execute scripts, compute anything — no shell/Python access
  Use for literature surveys, API documentation, technical specifications — pure information gathering

EXPERIMENT executor scope:
  Output: method_out.json with results (metrics, predictions, analysis) — the core computational work
  DOES: Implement and run methods/algorithms, compute metrics, compare approaches, produce quantitative results
  DOES NOT: Collect new datasets (depends on DATASET artifacts for input data), write formal proofs
  This is the right artifact for any code that processes data and produces results

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead

EVALUATION executor scope:
  Output: eval_out.json with evaluation results
  DOES: Any evaluation of experiment results — metrics, statistical tests, ablations, comparisons, visualizations, robustness checks, error analysis, etc.
  DOES NOT: Implement new methods (use EXPERIMENT), collect data (use DATASET)
  This is for analyzing experiment outputs from any angle

PROOF executor scope:
  Output: Lean 4 proof files (.lean) with verified theorems
  DOES: Write and verify Lean 4 formal proofs with Mathlib, iterative compilation
  DOES NOT: Run Python experiments, collect data, do empirical analysis
  Use only when formal mathematical guarantees are needed
</artifact_executor_scope>

<artifact_planning_rules>
RESEARCH: Plan early — findings guide dataset selection, experiment design, and methodology.
EXPERIMENT: Must depend on at least one DATASET. Define clear metrics and baselines before running. Consider trying multiple method variations rather than a single approach.
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
EVALUATION: Must depend on at least one EXPERIMENT. Focus on statistical rigor and validity checks.
PROOF: Use only when the hypothesis requires formal mathematical guarantees. Lean 4 + Mathlib.
</artifact_planning_rules>

<existing_artifacts>
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
out_dependency_files:
  file_list:
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
out_dependency_files:
  file_list:
  - data.py
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
  data_file_paths:
  - full_data_out.json
  - mini_data_out.json
  - preview_data_out.json
</existing_artifacts>

<current_paper>
The current paper draft — represents the research story so far.

Use this to understand what's working, what's not, and what gaps remain.
Gaps and weak results signal what to try differently — not what to conclude.

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

</current_paper>

<reviewer_feedback>
Paper reviewer feedback from the previous iteration. Your strategy MUST address these critiques.
Prioritize major issues — these are the most impactful improvements to make.

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

<task>
Generate 1 research strategy for THIS iteration.

**ARTIFACT LIMIT: Each strategy may contain AT MOST 3 artifact directions.** Focus on the highest-impact artifacts. Quality over quantity.

Each strategy should:
1. Define a clear OBJECTIVE - what novel contribution we're building toward
2. Plan artifacts to execute NOW - specify type, objective, approach, and depends_on for each
3. Account for parallel execution - all strategies and all planned artifacts run simultaneously, their artifacts are combined into one shared pool

**BROADER IS NOT THE SAME AS DEEPER.** Adding models, datasets, or settings to
an experiment that already ran makes the table bigger; it does not make the
contribution stronger, and it is the default a strategy generator drifts into
when it has nothing sharper to propose. Spend an artifact on scale only when
the SPREAD itself is the finding (a scaling trend, a regime boundary, a
generalisation claim the paper actually makes). Otherwise spend it on
something that could change the conclusion: the mechanism behind an observed
effect, the condition under which it disappears, the confound that would
explain it away, or the baseline whose absence a reviewer would name first.


</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ArtifactDep": {
      "description": "A single dependency on an existing artifact, with a short type label.\n\n``id`` and ``label`` are LLM-generated at strategy time. ``label`` is free-text but\nshort \u2014 a word or two naming the type of dependency, not a sentence.\n\n``relation_type`` and ``relation_rationale`` are populated later, in upd_hypo,\nusing the MultiCite citation-function typology (Lauscher et al., NAACL 2022).\nThey are absent at strategy time and may stay absent for legacy runs.",
      "properties": {
        "id": {
          "description": "ID of an existing artifact this artifact depends on",
          "title": "Id",
          "type": "string"
        },
        "label": {
          "description": "Short free-text label naming the type of this dependency (a word or two, not a sentence)",
          "title": "Label",
          "type": "string"
        }
      },
      "required": [
        "id",
        "label"
      ],
      "title": "ArtifactDep",
      "type": "object"
    },
    "ArtifactDirection": {
      "description": "High-level direction for an artifact to execute this iteration.\n\nID is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).",
      "properties": {
        "type": {
          "description": "Type of artifact to create",
          "enum": [
            "experiment",
            "research",
            "proof",
            "evaluation",
            "dataset"
          ],
          "title": "Type",
          "type": "string"
        },
        "objective": {
          "description": "What we want to achieve with this artifact",
          "title": "Objective",
          "type": "string"
        },
        "approach": {
          "description": "High-level direction/method",
          "title": "Approach",
          "type": "string"
        },
        "depends_on": {
          "description": "Existing artifacts this depends on, each with a short type label",
          "items": {
            "$ref": "#/$defs/ArtifactDep"
          },
          "title": "Depends On",
          "type": "array"
        }
      },
      "required": [
        "type",
        "objective",
        "approach"
      ],
      "title": "ArtifactDirection",
      "type": "object"
    },
    "Strategy": {
      "description": "A research strategy.\n\nContent fields have LLMPrompt + LLMStructOut markers.\n``id`` is code-assigned (LLMPrompt only \u2014 visible in prompts, not LLM-generated).\n\nID format: gen_strat_idx{N}",
      "properties": {
        "title": {
          "description": "Strategy name in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
          "title": "Title",
          "type": "string"
        },
        "objective": {
          "description": "The novel contribution we're building toward",
          "title": "Objective",
          "type": "string"
        },
        "rationale": {
          "description": "Why this strategy is promising",
          "title": "Rationale",
          "type": "string"
        },
        "artifact_directions": {
          "description": "Artifacts to execute THIS iteration",
          "items": {
            "$ref": "#/$defs/ArtifactDirection"
          },
          "title": "Artifact Directions",
          "type": "array"
        },
        "expected_outcome": {
          "description": "What we'll have after this iteration's artifacts complete",
          "title": "Expected Outcome",
          "type": "string"
        },
        "summary": {
          "default": "",
          "description": "Brief summary of the strategy and its expected contribution",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "title",
        "objective",
        "rationale",
        "artifact_directions",
        "expected_outcome"
      ],
      "title": "Strategy",
      "type": "object"
    }
  },
  "description": "Top-level wrapper for LLM strategy generation output.",
  "properties": {
    "strategies": {
      "description": "List of generated strategies",
      "items": {
        "$ref": "#/$defs/Strategy"
      },
      "title": "Strategies",
      "type": "array"
    }
  },
  "required": [
    "strategies"
  ],
  "title": "Strategies",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_strat/gen_strat_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 17:25:48 UTC

```
What determines whether an open-source project survives its founder stepping away?
```
