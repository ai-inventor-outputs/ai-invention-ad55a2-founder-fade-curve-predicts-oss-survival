# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_plan`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (sdk_openhands_agent, openai/@cf/nvidia/nemotron-3-120b-a12b)

### [1] CONFIG · 2026-08-21 17:30:17 UTC

```
Model: openai/@cf/nvidia/nemotron-3-120b-a12b | Session: a60f9920-0b53-4e0c-99bc-012d9e3805fb | CWD: /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [2] SYSTEM PROMPT · 2026-08-21 17:30:19 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: DATASET

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect
</artifact_type_info>

<available_resources>
<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>
</available_resources>

<time_budget>

The dataset executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>
```

### [3] SYSTEM-USER prompt · 2026-08-21 17:30:19 UTC

````
<hypothesis>
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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter2_dir1
type: dataset
objective: >-
  Collect 50-100 real GitHub OSS projects with verified founder departures, extract monthly founder involvement trajectories,
  compute static features, and label survival outcomes using the Avelino et al. (2019) criterion.
approach: >-
  Step 1: Use web search to identify known lists of abandoned/revived OSS projects from academic papers (Avelino et al. 2019),
  GitHub archives, and community sources. Step 2: Supplement by querying the GitHub API for repositories with stars > 100
  where the earliest committer has 6+ months of inactivity. Step 3: For each candidate, clone the repository and parse git
  history to identify the founder (earliest sustained committer, typically repo creator). Step 4: Extract monthly aggregates
  of founder's share of commits, PR merges, and code reviews from inception through the inactivity window. Step 5: Label survival:
  if the project had sustained activity (commits from non-founder contributors) in the 12 months after the founder's inactivity
  window began, label as 'survived'; otherwise 'collapsed'. Also compute a continuous survival metric (post-departure commit
  volume normalized to pre-departure baseline). Step 6: Compute static snapshot features at departure (bus factor, contributor
  count, project age, star count, file count). Step 7: Ensure diversity across project types (libraries vs applications),
  governance models (BDFL vs meritocratic), and domains. Step 8: Validate schema and output full/mini/preview JSON variants.
  Use parallel cloning and parsing with multiprocessing to stay within the 6-hour time budget. Use the aii-parallel-computing
  skill for parallel repo cloning and the aii-use-hardware skill for memory management.
depends_on:
- id: art_f8OOJq5VnC0z
  label: methodology
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>


GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for a DATASET artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-21 17:30:19 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [5] RETRY (attempt 1) · 2026-08-21 17:32:27 UTC

```
Agent result indicates failure (attempt 1/6): structured_output is None
```

### [6] RETRY (attempt 2) · 2026-08-21 17:32:29 UTC

```
Agent retry... (attempt 2/6): structured_output is None
```

### [7] CONFIG · 2026-08-21 17:32:29 UTC

```
Model: openai/nvidia/nemotron-3-super-120b-a12b | Session: 82496366-118f-4a75-8fe5-a2718c610134 | CWD: /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [8] SYSTEM PROMPT · 2026-08-21 17:32:31 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A plan generator (Step 3.2: GEN_PLAN in the invention loop)

You received the hypothesis, an artifact direction to elaborate, and dependency artifacts relevant to the plan.
Your job: elaborate this direction into a detailed, actionable plan for the executor agent.

Specific, actionable plan → valuable artifact. Vague plan → wasted execution.
</your_role>
</ai_inventor_context>

<artifact_type_info>
You are expanding an artifact direction of type: DATASET

DATASET
Collect, prepare, and merge datasets for experiments and analysis.
Runtime: Python 3.12, UV, isolated workspace.
Tools: Full shell/Python/filesystem access, the aii-web-tools skill (web search, page fetch, regex grep over full page/PDF text), and other skills.
Skills: aii-hf-datasets (HuggingFace Hub — ML datasets, many UCI/OpenML/Kaggle mirrors), aii-owid-datasets (Our World in Data — global statistics), aii-json (schema validation). Also any Python source (sklearn.datasets, openml, direct URLs, APIs) — must verify within 300MB limit.
Capabilities: Search, acquire, transform, combine, and standardize data from any available source.
Deps: REQUIRED none | OPTIONAL RESEARCH for guidance on what data to collect
</artifact_type_info>

<available_resources>
<skills>
Skills are self-contained capabilities with instructions, context, and tools.

- aii-web-tools: Free-first web search (general + scholarly modes), page/PDF fetch as markdown, regex grep over page/PDF text
- aii-semscholar-bib: Batch-fetch BibTeX from Semantic Scholar
- aii-openrouter-llms: Search and call 300+ LLMs via OpenRouter
- aii-hf-datasets: Search, preview, download HuggingFace datasets
- aii-owid-datasets: Search and load Our World in Data tables
- aii-lean: Compile/verify Lean 4 code, Mathlib search, tactic suggestions
- aii-concept-fig-gen: Generate/edit images via Gemini 3 Pro Image (Nano Banana Pro)
- aii-json: Validate JSON against schemas, generate mini/preview variants
- aii-paper-writing: Academic paper structure, bibliography, citations
- aii-paper-to-latex: Assemble LaTeX papers and compile to PDF
- aii-parallel-computing: GPU acceleration, CPU parallelism, async I/O
- aii-python: Python coding standards for experiment scripts
- aii-use-hardware: Detect CPU/RAM/GPU, memory-safe processing
- aii-long-running-tasks: Gradual scaling pattern for long-running tasks
- aii-colab: Google Colab runtime constraints for notebooks
- aii-file-size-limit: Check and split oversized output files
</skills>

<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>
</available_resources>

<time_budget>

The dataset executor has 6h total (including writing code, debugging, testing, and fixing errors).

</time_budget>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<plan_guidelines>
You are expanding an artifact direction from the strategy into a detailed plan.
The artifact direction specifies what to do at a high level (type, objective, approach, dependencies).
Your job is to make it concrete and actionable as a detailed plan.
Use web research to look up technical details, verify feasibility, and find reference materials
that will make your plan more concrete and actionable for the executor.

GOOD PLANS:
- Make each component SPECIFIC and actionable (not vague platitudes)
- Consider both success AND failure scenarios
- Build on the approach in the artifact direction
- Add concrete details the executor needs

BAD PLANS:
- Vague hand-waving ("do research on X")
- Ignoring the approach in the artifact direction
- Missing critical details the executor needs
</plan_guidelines>

<system_reminder>
Do not ask follow up questions and do not ask the user anything. Execute all steps independently.
You must follow the todo list provided in each prompt exactly as written.
No placeholders, stubs, or incomplete code — all code must be complete and functional.
</system_reminder>

<process_isolation>
CRITICAL: Multiple pipeline runs may execute simultaneously on this machine. `ps aux | grep method.py` matches ALL runs, not just yours.
- NEVER kill processes by name (`killall`, `pkill -f`, `ps aux | grep ... | xargs kill`). This kills OTHER runs' processes.
- NEVER monitor processes by name (`ps aux | grep method.py`). You will see other runs' processes and get confused.
- ALWAYS use PID-based process management:
  Run: `uv run method.py & PID=$!` or `timeout <seconds> uv run method.py & PID=$!`
  Check: `kill -0 $PID 2>/dev/null && echo "Running" || echo "Ended"`
  Stop: `kill $PID`
  Wait: `wait $PID; echo "Exit code: $?"`
  Monitor: `tail -f logs/run.log & TAIL_PID=$!` then `kill $TAIL_PID` when done
</process_isolation>
```

### [9] SYSTEM-USER prompt · 2026-08-21 17:32:31 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement followed a smooth, prolonged
  fade — a gradually declining trajectory measurable as the slope of the foun
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<hypothesis>
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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter2_dir1
type: dataset
objective: >-
  Collect 50-100 real GitHub OSS projects with verified founder departures, extract monthly founder involvement trajectories,
  compute static features, and label survival outcomes using the Avelino et al. (2019) criterion.
approach: >-
  Step 1: Use web search to identify known lists of abandoned/revived OSS projects from academic papers (Avelino et al. 2019),
  GitHub archives, and community sources. Step 2: Supplement by querying the GitHub API for repositories with stars > 100
  where the earliest committer has 6+ months of inactivity. Step 3: For each candidate, clone the repository and parse git
  history to identify the founder (earliest sustained committer, typically repo creator). Step 4: Extract monthly aggregates
  of founder's share of commits, PR merges, and code reviews from inception through the inactivity window. Step 5: Label survival:
  if the project had sustained activity (commits from non-founder contributors) in the 12 months after the founder's inactivity
  window began, label as 'survived'; otherwise 'collapsed'. Also compute a continuous survival metric (post-departure commit
  volume normalized to pre-departure baseline). Step 6: Compute static snapshot features at departure (bus factor, contributor
  count, project age, star count, file count). Step 7: Ensure diversity across project types (libraries vs applications),
  governance models (BDFL vs meritocratic), and domains. Step 8: Validate schema and output full/mini/preview JSON variants.
  Use parallel cloning and parsing with multiprocessing to stay within the 6-hour time budget. Use the aii-parallel-computing
  skill for parallel repo cloning and the aii-use-hardware skill for memory management.
depends_on:
- id: art_f8OOJq5VnC0z
  label: methodology
  relation_type:
  relation_rationale:
</artifact_direction>

<dependencies>
Completed artifacts this artifact can use during execution.

--- Dependency 1 ---
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
</dependencies>

<instructions>
YOUR ROLE: Write a detailed PLAN for the artifact. A separate executor agent runs the actual artifact later.

You are a PLANNER, not an executor. Your output is a plan that tells the executor what to do and how.
Do NOT execute the artifact itself — a separate agent handles that. Your job is to plan it so well that the executor can follow your plan step by step.

You CAN and SHOULD: search the web, read papers, and explore library docs to make your plan concrete.
You CANNOT run shell commands or scripts — code execution is disabled. Research via web tools only.

Do NOT do the executor's job: don't download datasets, don't implement code, don't run experiments, don't write proofs, don't compute evaluations.

<artifact_executor_scope>
IMPORTANT: Each artifact executor has a focused prompt that guides it to do ONE thing well. It will NOT perform tasks outside its scope — assigning the wrong work to the wrong artifact type wastes an iteration. Match the task to the right executor.

DATASET executor scope:
  Output: data_out.json with rows of {input, output, metadata_fold, ...} — raw data only, no derived computations
  DOES: Download/generate datasets, analyze candidates to pick the best ones, standardize to JSON schema (features, labels, folds, metadata), validate schema, split into full/mini/preview
  DOES NOT: Run experiments, train models, compute derived statistics (PID/MI/correlations/synergy matrices) as final output
  If you need to COMPUTE something from data (synergy matrices, MI scores, timing benchmarks), use an EXPERIMENT artifact instead
</artifact_executor_scope>

<artifact_planning_rules>
DATASET:
- Plan for REAL third-party datasets (HuggingFace, Kaggle, direct-download URLs) — downloadable within time and size constraints
- Describe dataset criteria (domain, size, format) — executors find exact sources, but you can suggest candidates or search directions
- ALWAYS prefer real datasets over synthetic. Synthetic is a LAST RESORT only when no suitable real data exists
</artifact_planning_rules>


GOOD PLANS: specific, actionable, consider failure scenarios, build on the suggested approach.
BAD PLANS: vague hand-waving, ignoring the suggested approach, missing critical executor details.
</instructions><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "description": "Plan for a DATASET artifact.",
  "properties": {
    "title": {
      "description": "Plan title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters).",
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Brief summary",
      "title": "Summary",
      "type": "string"
    },
    "runpod_compute_profile": {
      "anyOf": [
        {
          "type": "string"
        },
        {
          "type": "null"
        }
      ],
      "default": "cpu_light",
      "description": "Compute tier for execution \u2014 pick from the available profiles list (e.g., 'gpu', 'cpu_heavy', 'cpu_light'). Only used in RunPod mode.",
      "title": "Runpod Compute Profile"
    },
    "ideal_dataset_criteria": {
      "description": "What makes an ideal dataset for this purpose - size, format, content requirements",
      "title": "Ideal Dataset Criteria",
      "type": "string"
    },
    "dataset_search_plan": {
      "description": "Step-by-step plan for finding/creating this dataset - sources to check, fallback options",
      "title": "Dataset Search Plan",
      "type": "string"
    },
    "target_num_datasets": {
      "description": "How many individual datasets should be delivered. Count each dataset separately, not collections \u2014 a benchmark suite of N datasets counts as N. This controls how broadly the executor searches, so setting it too low will under-collect.",
      "title": "Target Num Datasets",
      "type": "integer"
    }
  },
  "required": [
    "title",
    "ideal_dataset_criteria",
    "dataset_search_plan",
    "target_num_datasets"
  ],
  "title": "DatasetPlan",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [10] HUMAN-USER prompt · 2026-08-21 17:32:31 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [11] THINKING · 2026-08-21 17:32:39 UTC

```
We need to produce a plan for the dataset artifact. We have hypothesis and artifact direction. We need to output a JSON with title, summary, runpod_compute_profile, ideal_dataset_criteria, dataset_search_plan, target_num_datasets.

We need to read the hypothesis and artifact direction to understand what dataset we need: 50-100 real GitHub OSS projects with verified founder departures, extract monthly founder involvement trajectories, compute static features, label survival outcomes.

Thus ideal dataset: JSON with each project having features: founder involvement trajectory (monthly shares of commits, merges, reviews), static features (bus factor, contributor count, project age, star count, file count), survival label (binary), maybe continuous survival metric.

We need to plan to collect from GitHub using API and cloning. Use web search to find known lists of abandoned/revived OSS projects. Then supplement via GitHub API query for repos with stars>100 where earliest committer has 6+ months inactivity. Then clone and parse git history.

We need to plan for parallel cloning, memory management, etc.

We need to output a plan, not execute.

Thus we need to write the plan in the JSON fields.

We should also consider using skills: aii-web-tools for search, aii-hf-datasets maybe not relevant, aii-parallel-computing, aii-use-hardware.

We need to produce the JSON file at the given path.

Let's first look at the directory to see if any existing files.

We'll use file_editor view to see current directory.
```

### [12] TOOL CALL — file_editor · 2026-08-21 17:32:39 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [13] TOOL RESULT — file_editor · 2026-08-21 17:32:39 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [14] THINKING · 2026-08-21 17:32:47 UTC

```
We are in the directory is empty. We need to first read the dependency artifact (research) to understand the background.
 Let's look at the dependency artifact: art_f8OOJq5VnC0z (research) located at:
   /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1
 We'll view that file to get the research summary.
```

### [15] TOOL CALL — file_editor · 2026-08-21 17:32:47 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [16] TOOL RESULT — file_editor · 2026-08-21 17:32:47 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/\n/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json\n/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_report.md\n\n2 hidden files/directories in this directory are excluded. You can use 'ls -la /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1' to see them."}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [17] THINKING · 2026-08-21 17:32:51 UTC

```
We need to produce a plan for the dataset artifact. The artifact direction is about collecting 50-100 real GitHub OSS projects with verified founder departures, extracting monthly founder involvement trajectories, computing static features, and labeling survival outcomes.

We need to create a detailed plan that the executor can follow. The plan should include steps, tools, parallelization, error handling, and produce the expected output (data_out.json with rows of data). We must respect the scope: dataset executor outputs raw data only, no derived computations? Actually they compute derived statistics as features? The direction says compute static features and label survival outcomes. That's derived from raw git history. The dataset executor can compute features as part of data preparation. The artifact type is DATASET, which includes collecting, preparing, merging datasets. So we can include computation of features.

We need to output a JSON with fields: title, summary, runpod_compute_profile (optional), ideal_dataset_criteria, dataset_search_plan, target_num_datasets.

We need to fill these based on the artifact direction.

Let's first examine the research_out.json to see what was found in the literature survey.
```

### [18] TOOL CALL — file_editor · 2026-08-21 17:32:51 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [19] TOOL RESULT — file_editor · 2026-08-21 17:32:51 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json:\n     1\t{\n     2\t  \"title\": \"Founder Fade Curve and OSS Survival Literature Survey\",\n     3\t  \"summary\": \"This research surveyed literature on founder identification, project survival metrics, GitHub API capabilities, and prior work on temporal trajectories of contributor involvement in open source software. Key findings include: Truck Factor (TF) as a measure of project dependency on key developers; 16% of projects experience TF developers detachment (TFDD); 41% of projects survive TFDD by attracting new core contributors; survival is associated with younger projects at TFDD time; GitHub API provides commits, pull requests, and review comments endpoints with pagination and rate limits; founder identification can be approached through initial commit analysis or CODEOWNERS files; longitudinal bus factor analysis reveals contributor turnover risks. Recommendations for hypothesis testing include: using 6-month inactivity threshold for founder departure, defining survival as continued commits after departure, utilizing GitHub commits API with author tracking, and controlling for project age and initial team size as confounds.\",\n     4\t  \"layman_summary\": \"This research investigated what happens to open-source projects when their founders leave, examining how to measure founder dependency, predict project survival, and identify relevant data sources from GitHub.\",\n     5\t  \"answer\": \"Research into founder fade curves and OSS survival reveals several key insights for hypothesis testing:\\n\\n1. **Founder Dependency Measurement**: The Truck Factor (TF) concept measures the minimal number of developers critical to project maintenance [1]. TF developers detachment (TFDD) occurs when these critical contributors leave [1]. Studies show 16% of projects experience at least one TFDD, with 66% occurring in projects where TF=1 (indicating single-founder dependency) [1].\\n\\n2. **Survival Patterns**: 41% of projects survive their last observed TFDD [1]. Survival typically occurs by attracting a single new TF developer (86% of cases), with newcomers contributing to recovery in 48% of surviving projects [1]. Notably, surviving projects are younger at the time of TFDD compared to non-surviving ones, though no significant differences exist in developer count, commits, or files at the detachment moment [1].\\n\\n3. **Temporal Dynamics**: 59% of TFDDs occur within the first two years of project development [1], suggesting early vulnerability periods. This aligns with the hypothesis of a \\\"founder fade curve\\\" where founder involvement decays over time.\\n\\n4. **GitHub API Capabilities**: For tracking contributor activity, the GitHub REST API provides:\\n   - Commits endpoint: Lists commits with filtering by author, date range, and file path [3]\\n   - Pull requests endpoint: Tracks collaborative contributions [4]\\n   - Pull request review comments endpoint: Captures code review interactions [5]\\n   All endpoints support pagination (max 100 items per page) and require authentication for rate-limited access [3,4,5].\\n\\n5. **Founder Identification Methods**: While no universal standard exists, approaches include:\\n   - Analyzing initial commits to identify early contributors [6]\\n   - Examining CODEOWNERS files when present [7]\\n   - Tracking contributors with merge privileges or review responsibilities\\n   - Note that team membership visibility is often private, limiting direct API access [7]\\n\\n6. **Longitudinal Risk Metrics**: The bus factor (equivalent to TF) can be tracked longitudinally to measure evolving project resilience [8]. Tools like PRIME demonstrate how to compute and visualize such metrics over time, revealing trends in contributor dependency [8].\\n\\n**Recommendations for Experiment Design**:\\n- **Inactivity Threshold**: Use 6 months of no commits from a founder to signal potential departure, balancing detection of true abandonment against temporary absences\\n- **Survival Definition**: Define project survival as continued commits (from any contributor) for at least 3 months post-founder-departure\\n- **Primary Data Source**: GitHub commits API to track author-specific activity over time\\n- **Key Confounds to Control**: Project age at founder departure, initial team size (TF), and external events like funding changes or major version releases\\n\\n**Contradicting Evidence**: While the Avelino study found no pre-TFDD differences between surviving/non-surviving projects [1], other research suggests factors like documentation quality, issue responsiveness, and community engagement may predict survival prospects [2]. This indicates founder departure alone may not be sufficient to predict outcomes.\\n\\n**Follow-up Questions**:\\n1. How does the decay pattern of founder commits (founder fade curve) vary across different types of OSS projects (e.g., libraries vs. applications)?\\n2. What early-warning signals in contributor behavior precede actual founder departure beyond simple commit frequency?\\n3. How do different governance models (BDFL, meritocratic, corporate-backed) influence the relationship between founder departure and project survival?\",\n     6\t  \"sources\": [\n     7\t    {\n     8\t      \"index\": 1,\n     9\t      \"url\": \"http://soft.vub.ac.be/benevol2019/papers/BENEVOL_2019_paper_3.pdf\",\n    10\t      \"title\": \"On the abandonment and survival of open source projects: An empirical investigation\",\n    11\t      \"summary\": \"Foundational study showing Truck Factor concept, TFDD frequency (16%), survival rate (41%), and characteristics of surviving projects (younger at TFDD time).\"\n    12\t    },\n    13\t    {\n    14\t      \"index\": 2,\n    15\t      \"url\": \"https://doi.org/10.1109/esem.2019.8870181\",\n    16\t      \"title\": \"On the abandonment and survival of open source projects: An empirical investigation\",\n    17\t      \"summary\": \"Duplicate source confirming the Avelino et al. 2019 findings on OSS project abandonment and survival dynamics.\"\n    18\t    },\n    19\t    {\n    20\t      \"index\": 3,\n    21\t      \"url\": \"https://docs.github.com/en/rest/commits/commits?apiVersion=2026-03-10\",\n    22\t      \"title\": \"REST API endpoints for commits\",\n    23\t      \"summary\": \"GitHub API documentation for commits endpoint showing parameters for filtering by author, date, and path, plus pagination and rate limit information.\"\n    24\t    },\n    25\t    {\n    26\t      \"index\": 4,\n    27\t      \"url\": \"https://docs.github.com/rest/pulls/pulls\",\n    28\t      \"title\": \"REST API endpoints for pull requests\",\n    29\t      \"summary\": \"GitHub API documentation for pull requests endpoint showing parameters for filtering by state, head, base, and sort options.\"\n    30\t    },\n    31\t    {\n    32\t      \"index\": 5,\n    33\t      \"url\": \"https://docs.github.com/en/rest/pulls/comments\",\n    34\t      \"title\": \"REST API endpoints for pull request review comments\",\n    35\t      \"summary\": \"GitHub API documentation for accessing review comments on pull requests, useful for understanding collaboration patterns.\"\n    36\t    },\n    37\t    {\n    38\t      \"index\": 6,\n    39\t      \"url\": \"https://stackoverflow.com/questions/23540639/how-to-know-who-is-the-maintainer-of-a-github-repository\",\n    40\t      \"title\": \"How to know who is the maintainer of a GitHub repository?\",\n    41\t      \"summary\": \"Stack Overflow discussion highlighting challenges in identifying maintainers, noting that team privileges aren't public and CODEOWNERS file can help when present.\"\n    42\t    },\n    43\t    {\n    44\t      \"index\": 7,\n    45\t      \"url\": \"https://github.com/blog/2392-introducing-code-owners\",\n    46\t      \"title\": \"Introducing Code Owners\",\n    47\t      \"summary\": \"GitHub blog post introducing CODEOWNERS file format for designating maintainers and reviewers for specific code paths.\"\n    48\t    },\n    49\t    {\n    50\t      \"index\": 8,\n    51\t      \"url\": \"https://wenxin-jiang.github.io/files/SynovicHyattSethiThotaShilpikaMillerJiangPinderskiLauferHaywardKlingensmithDavisThiruvathukal-LongitudinalMetrics-ASE22Demo.pdf\",\n    52\t      \"title\": \"Snapshot Metrics Are Not Enough: Analyzing Software Repositories with Longitudinal Metrics\",\n    53\t      \"summary\": \"Paper describing PRIME tool for longitudinal metrics including bus factor, demonstrating how to track contributor dependency metrics over time.\"\n    54\t    }\n    55\t  ],\n    56\t  \"follow_up_questions\": [\n    57\t    \"How does the decay pattern of founder commits (founder fade curve) vary across different types of OSS projects (e.g., libraries vs. applications)?\",\n    58\t    \"What early-warning signals in contributor behavior precede actual founder departure beyond simple commit frequency?\",\n    59\t    \"How do different governance models (BDFL, meritocratic, corporate-backed) influence the relationship between founder departure and project survival?\"\n    60\t  ],\n    61\t  \"out_expected_files\": {\n    62\t    \"output\": \"research_out.json\"\n    63\t  },\n    64\t  \"upload_ignore_regexes\": [\n    65\t    \"(^|/)cache/\",\n    66\t    \"(^|/)checkpoints/\",\n    67\t    \"(^|/)__pycache__/\",\n    68\t    \"(^|*)\\\\.pyc\",\n    69\t    \"(^|*)\\\\.pyo\",\n    70\t    \"(^|*)\\\\.pyd\",\n    71\t    \".DS_Store\"\n    72\t  ]\n    73\t}\n"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/gen_art/gen_art_research_1/research_out.json", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [20] THINKING · 2026-08-21 17:33:19 UTC

```
We need to output a plan for the dataset artifact. The direction: Collect 50-100 real GitHub OSS projects with verified founder departures, extract monthly founder involvement trajectories, compute static features, and label survival outcomes using the Avelino et al. (2019) criterion.

We need to produce a JSON with title, summary, runpod_compute_profile, ideal_dataset_criteria, dataset_search_plan, target_num_datasets.

We must follow the schema. The title should be short, 4-8 words. Summarize the plan.

We need to think about steps: search for known lists, supplement with GitHub API query, clone repos, parse git history, compute founder shares, label survival, compute static features, ensure diversity, output JSON.

We need to consider failure scenarios, parallelization, time budget.

We should also reference the dependency research artifact for guidance.

Let's craft the plan.

First, title: "Collect GitHub OSS Founder Departure Dataset"

Summary: "Plan to gather 50-100 OSS projects with verified founder departures, extract involvement trajectories, label survival, and compute static features for hypothesis testing."

Ideal dataset criteria: Should contain monthly time series of founder's share of commits, merges, reviews from project start to departure; static features at departure; binary survival label; continuous post-departure activity; metadata for diversity (domain, governance, stars). Size: 50-100 projects. Format: JSON array of objects each with project_id, founder_id, monthly_trajectories, static_features, survival_label, etc.

Dataset search plan: Step 1: Search web for known lists of abandoned/revived OSS projects from Avelino et al. 2019, GitHub archives, etc. Step 2: Use GitHub API to find repositories with stars >100 where earliest committer has 6+ months inactivity. Step 3: For each candidate, clone repo and parse git history to verify founder and extract trajectories. Step 4: Label survival using Avelino criterion. Step 5: Compute static features. Step 6: Ensure diversity across types, governance, domains. Step 7: Output JSON with full/mini/preview variants. Use parallel cloning and parsing to stay within 6h.

Target_num_datasets: 1 (since we are producing a single dataset containing multiple projects). But the schema says "target_num_datasets: How many individual datasets should be delivered. Count each dataset separately, not collections — a benchmark suite of N datasets counts as N." We are delivering one dataset (the collection). So target_num_datasets = 1.

We need to output JSON file at the specified path.

Let's first create the plan file. We'll use file_editor to create the JSON.

But we need to ensure the directory exists. It does.

We'll create the JSON with the required fields.

Let's do it.
```

### [21] TOOL CALL — file_editor · 2026-08-21 17:33:19 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"Collect GitHub OSS Founder Departure Dataset\",\n  \"summary\": \"Plan to gather 50-100 OSS projects with verified founder departures, extract founder involvement trajectories, label survival outcomes, and compute static features for hypothesis testing.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"ideal_dataset_criteria\": \"Dataset should contain: (1) monthly time series of founder's share of commits, PR merges, and code-review decisions from project inception to founder departure; (2) static snapshot features at departure (bus factor, contributor count, project age, star count, file count); (3) binary survival label based on Avelino et al. (2019) criterion (sustained activity from non-founder contributors in 12 months post-departure); (4) continuous survival metric (post-departure commit volume normalized to pre-departure baseline); (5) metadata for diversity assessment (project domain, governance model, primary language). Ideal size: 50-100 projects with balanced survival/collapse outcomes. Format: JSON array of objects, each representing one project with the above fields.\",\n  \"dataset_search_plan\": \"Step 1: Use web search (scholarly mode) to locate known lists of abandoned/revived OSS projects from Avelino et al. (2019) and related works; extract project names/URLs. Step 2: Supplement via GitHub API search for repositories with stars > 100 where the earliest committer (identified via initial commit analysis) has >=6 months of no commits; collect candidate URLs. Step 3: For each candidate, clone the repository (using parallel processes) and parse git history to verify founder identity (earliest sustained committer) and extract monthly aggregates of founder's share of commits, merges, and reviews from inception through the inactivity window. Step 4: Label survival: if the project had sustained activity (commits from non-founder contributors above a minimal threshold) in the 12 months after the founder's inactivity window began, label as 'survived'; otherwise 'collapsed'. Also compute continuous survival metric (post-departure commit volume normalized to pre-departure baseline). Step 5: Compute static snapshot features at departure: bus factor (via clique-finding or approximation), contributor count, project age, star count, file count. Step 6: Ensure diversity across project types (libraries vs. applications), governance models (BDFL vs. meritocratic), and domains (web, systems, data, etc.) by stratifying selection. Step 7: Validate schema and output full JSON dataset, then generate mini (first 10 rows) and preview (first 2 rows) variants. Use parallel cloning and parsing (via aii-parallel-computing) to stay within the 6-hour time budget; monitor memory usage with aii-use-hardware to avoid OOM.\",\n  \"target_num_datasets\": 1\n}",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [22] TOOL RESULT — file_editor · 2026-08-21 17:33:21 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json", "prev_exist": false, "old_content": null, "new_content": "{\n  \"title\": \"Collect GitHub OSS Founder Departure Dataset\",\n  \"summary\": \"Plan to gather 50-100 OSS projects with verified founder departures, extract founder involvement trajectories, label survival outcomes, and compute static features for hypothesis testing.\",\n  \"runpod_compute_profile\": \"cpu_light\",\n  \"ideal_dataset_criteria\": \"Dataset should contain: (1) monthly time series of founder's share of commits, PR merges, and code-review decisions from project inception to founder departure; (2) static snapshot features at departure (bus factor, contributor count, project age, star count, file count); (3) binary survival label based on Avelino et al. (2019) criterion (sustained activity from non-founder contributors in 12 months post-departure); (4) continuous survival metric (post-departure commit volume normalized to pre-departure baseline); (5) metadata for diversity assessment (project domain, governance model, primary language). Ideal size: 50-100 projects with balanced survival/collapse outcomes. Format: JSON array of objects, each representing one project with the above fields.\",\n  \"dataset_search_plan\": \"Step 1: Use web search (scholarly mode) to locate known lists of abandoned/revived OSS projects from Avelino et al. (2019) and related works; extract project names/URLs. Step 2: Supplement via GitHub API search for repositories with stars > 100 where the earliest committer (identified via initial commit analysis) has >=6 months of no commits; collect candidate URLs. Step 3: For each candidate, clone the repository (using parallel processes) and parse git history to verify founder identity (earliest sustained committer) and extract monthly aggregates of founder's share of commits, merges, and reviews from inception through the inactivity window. Step 4: Label survival: if the project had sustained activity (commits from non-founder contributors above a minimal threshold) in the 12 months after the founder's inactivity window began, label as 'survived'; otherwise 'collapsed'. Also compute continuous survival metric (post-departure commit volume normalized to pre-departure baseline). Step 5: Compute static snapshot features at departure: bus factor (via clique-finding or approximation), contributor count, project age, star count, file count. Step 6: Ensure diversity across project types (libraries vs. applications), governance models (BDFL vs. meritocratic), and domains (web, systems, data, etc.) by stratifying selection. Step 7: Validate schema and output full JSON dataset, then generate mini (first 10 rows) and preview (first 2 rows) variants. Use parallel cloning and parsing (via aii-parallel-computing) to stay within the 6-hour time budget; monitor memory usage with aii-use-hardware to avoid OOM.\",\n  \"target_num_datasets\": 1\n}", "kind": "FileEditorObservation"}
```

### [23] THINKING · 2026-08-21 17:33:21 UTC

```
We are in the plan generation step. We have created the plan JSON file. Now we should verify that the file exists and contains the correct JSON structure.
 Let's do a quick check and then mark the task as complete.
```

### [24] TOOL CALL — file_editor · 2026-08-21 17:33:21 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [25] TOOL RESULT — file_editor · 2026-08-21 17:33:23 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json:\n     1\t{\n     2\t  \"title\": \"Collect GitHub OSS Founder Departure Dataset\",\n     3\t  \"summary\": \"Plan to gather 50-100 OSS projects with verified founder departures, extract founder involvement trajectories, label survival outcomes, and compute static features for hypothesis testing.\",\n     4\t  \"runpod_compute_profile\": \"cpu_light\",\n     5\t  \"ideal_dataset_criteria\": \"Dataset should contain: (1) monthly time series of founder's share of commits, PR merges, and code-review decisions from project inception to founder departure; (2) static snapshot features at departure (bus factor, contributor count, project age, star count, file count); (3) binary survival label based on Avelino et al. (2019) criterion (sustained activity from non-founder contributors in 12 months post-departure); (4) continuous survival metric (post-departure commit volume normalized to pre-departure baseline); (5) metadata for diversity assessment (project domain, governance model, primary language). Ideal size: 50-100 projects with balanced survival/collapse outcomes. Format: JSON array of objects, each representing one project with the above fields.\",\n     6\t  \"dataset_search_plan\": \"Step 1: Use web search (scholarly mode) to locate known lists of abandoned/revived OSS projects from Avelino et al. (2019) and related works; extract project names/URLs. Step 2: Supplement via GitHub API search for repositories with stars > 100 where the earliest committer (identified via initial commit analysis) has >=6 months of no commits; collect candidate URLs. Step 3: For each candidate, clone the repository (using parallel processes) and parse git history to verify founder identity (earliest sustained committer) and extract monthly aggregates of founder's share of commits, merges, and reviews from inception through the inactivity window. Step 4: Label survival: if the project had sustained activity (commits from non-founder contributors above a minimal threshold) in the 12 months after the founder's inactivity window began, label as 'survived'; otherwise 'collapsed'. Also compute continuous survival metric (post-departure commit volume normalized to pre-departure baseline). Step 5: Compute static snapshot features at departure: bus factor (via clique-finding or approximation), contributor count, project age, star count, file count. Step 6: Ensure diversity across project types (libraries vs. applications), governance models (BDFL vs. meritocratic), and domains (web, systems, data, etc.) by stratifying selection. Step 7: Validate schema and output full JSON dataset, then generate mini (first 10 rows) and preview (first 2 rows) variants. Use parallel cloning and parsing (via aii-parallel-computing) to stay within the 6-hour time budget; monitor memory usage with aii-use-hardware to avoid OOM.\",\n     7\t  \"target_num_datasets\": 1\n     8\t}\n"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [26] THINKING · 2026-08-21 17:33:27 UTC

```
I have successfully created the dataset plan JSON file. The plan is comprehensive and follows the artifact direction provided. It includes:

1. Title: "Collect GitHub OSS Founder Departure Dataset"
2. Summary: Clear description of what the dataset will contain
3. Runpod compute profile: cpu_light (appropriate for this task)
4. Ideal dataset criteria: Detailed specifications of what the dataset should contain
5. Dataset search plan: Step-by-step approach matching the artifact direction
6. Target num datasets: 1 (as we're creating one comprehensive dataset)

The plan addresses all requirements from the artifact direction:
- Uses web search to find known lists of abandoned/revived OSS projects
- Supplements with GitHub API search
- Clones repositories and parses git history
- Extracts monthly founder involvement trajectories
- Labels survival using Avelino et al. (2019) criterion
- Computes static snapshot features
- Ensures diversity across project types, governance models, and domains
- Uses parallel processing for efficiency
- Outputs JSON with full/mini/preview variants

The plan is specific, actionable, and considers failure scenarios (like using approximation for bus factor computation, monitoring memory usage). It builds directly on the suggested approach in the artifact direction.

Now I should mark the task as complete.
```

### [27] TOOL CALL — finish · 2026-08-21 17:33:27 UTC

```
{
  "message": "I have created a detailed plan for collecting the GitHub OSS founder departure dataset as specified in the artifact direction. The plan outlines a step-by-step approach to gather 50-100 real OSS projects with verified founder departures, extract monthly founder involvement trajectories, compute static features, and label survival outcomes using the Avelino et al. (2019) criterion.\n\nThe plan includes:\n- Clear ideal dataset criteria specifying the required data fields\n- A comprehensive search plan combining web scholarly search for known project lists with GitHub API supplementation\n- Detailed execution steps for cloning, parsing, feature extraction, and labeling\n- Strategies for ensuring diversity and handling computational constraints\n- Output format specifications for full/mini/preview JSON variants\n\nThe plan is saved to: /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json"
}
```

### [28] TOOL RESULT — finish · 2026-08-21 17:33:27 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "I have created a detailed plan for collecting the GitHub OSS founder departure dataset as specified in the artifact direction. The plan outlines a step-by-step approach to gather 50-100 real OSS projects with verified founder departures, extract monthly founder involvement trajectories, compute static features, and label survival outcomes using the Avelino et al. (2019) criterion.\n\nThe plan includes:\n- Clear ideal dataset criteria specifying the required data fields\n- A comprehensive search plan combining web scholarly search for known project lists with GitHub API supplementation\n- Detailed execution steps for cloning, parsing, feature extraction, and labeling\n- Strategies for ensuring diversity and handling computational constraints\n- Output format specifications for full/mini/preview JSON variants\n\nThe plan is saved to: /ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_2/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "kind": "FinishObservation"}
```

### [29] HOOK — PostToolUse · 2026-08-21 17:33:27 UTC

```
<system-reminder>You have 54.0 minutes remaining to finish all your tasks.</system-reminder>
```
