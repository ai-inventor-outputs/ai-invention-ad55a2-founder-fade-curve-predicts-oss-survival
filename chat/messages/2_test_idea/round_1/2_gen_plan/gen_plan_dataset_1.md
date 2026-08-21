# gen_plan_dataset_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_plan`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Do Not Predict Open-Source Project Survival
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_plan_dataset_1` (sdk_openhands_agent, gemini/gemini-3.5-flash)

### [1] CONFIG · 2026-08-21 15:13:01 UTC

```
Model: gemini/gemini-3.5-flash | Session: c0300542-f4f7-4522-b905-4e02c6959438 | CWD: /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [2] SYSTEM PROMPT · 2026-08-21 15:13:03 UTC

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
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

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

### [3] SYSTEM-USER prompt · 2026-08-21 15:13:03 UTC

````
<hypothesis>
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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Build a curated cohort of 40-80 public GitHub OSS projects where the identified founder has departed, with per-month founder
  involvement time series (share of commits, merges, reviews) from inception to departure, and a survival label (survived
  vs collapsed) based on the Avelino TFDD criterion.
approach: >-
  Step 1: Identify candidate projects by searching for popular OSS projects with a clear founder who became inactive (using
  GitHub search, GitHub Archive, or curated lists of abandoned/revived projects). Step 2: For each candidate, clone the repo
  and extract: (a) founder identity (earliest sustained contributor), (b) founder departure date (12-month inactivity window),
  (c) per-month founder share of commits, PR merges, and code reviews from inception to departure, (d) post-departure activity
  metrics for 24 months. Step 3: Label survival using the Avelino TFDD criterion (new truck-factor developer appears post-departure
  with sustained activity) or fallback continuous metric (normalized post-departure commit volume). Step 4: Output as JSON
  with rows containing: project_id, founder, departure_date, pre_departure_months, monthly_founder_share_commits, monthly_founder_share_merges,
  monthly_founder_share_reviews, survival_label, static_features (bus_factor, contributor_count, project_age, stars, file_count
  at departure). Use parallel cloning and extraction to stay within the 6-hour time budget.
depends_on: []
</artifact_direction>



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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-21 15:13:03 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [5] THINKING · 2026-08-21 15:13:11 UTC

```
**Dataset Artifact Plan: Initial Thoughts**

Okay, so the user wants a plan for building a DATASET artifact. The objective is clear: curate a set of 40-80 open-source GitHub projects where the founders have left. I need to track the founder's involvement time series – things like commits, merges, and reviews – from the project's beginning right up to the founder's departure. Crucially, I have to generate a "survival" label for each project using the Avelino TFDD criterion (I'll need to refresh my memory on the specifics of that, but it's a known metric).

Before I dive too deep into building the plan, I should see if there are any existing uploads or starting points. Let's see if there is any existing information in `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Just to get a feel for what’s been done already or if there are any useful templates.

Next, I will check what's already there in `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1` to find out what's already been generated. Hopefully I can reuse some existing work.
```

### [6] TOOL CALL — file_editor · 2026-08-21 15:13:11 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [7] TOOL RESULT — file_editor · 2026-08-21 15:13:11 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [8] THINKING · 2026-08-21 15:13:21 UTC

```
**Empty Directory Blues**

Okay, so the `gen_plan_dataset_1` directory, specifically located at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/` is completely barren. That's not ideal, I was expecting some data there. This iteration seems to be off to a rocky start. Let's see if the user has uploaded anything useful to the `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads` directory. Perhaps the data I need is there. Time to pivot and see what we've got. Hopefully there's something to work with.
```

### [9] TOOL CALL — file_editor · 2026-08-21 15:13:21 UTC

```
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [10] TOOL RESULT — file_editor · 2026-08-21 15:13:21 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads/"}], "is_error": false, "command": "view", "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads", "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [11] RETRY (attempt 1) · 2026-08-21 15:15:22 UTC

```
Agent result indicates failure (attempt 1/6): structured_output is None
```

### [12] RETRY (attempt 2) · 2026-08-21 15:15:23 UTC

```
Agent retry... (attempt 2/6): structured_output is None
```

### [13] CONFIG · 2026-08-21 15:15:23 UTC

```
Model: openai/google/gemma-4-31b-it:free | Session: 07efc15e-0092-4514-bcaa-ead14fb3f0fa | CWD: /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [14] SYSTEM PROMPT · 2026-08-21 15:15:25 UTC

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
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

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

### [15] SYSTEM-USER prompt · 2026-08-21 15:15:25 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed
  a smooth, prolonged fade — a gradually declining trajectory, measurable as the s
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [agent_think]: **Dataset Artifact Plan: Initial Thoughts**

Okay, so the user wants a plan for building a DATASET artifact. The objective is clear: curate a set of 40-80 open-source GitHub projects where the founders have left. I need to track the founder's involvement time series – things like commits, merges, an
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr
  - [agent_think]: **Empty Directory Blues**

Okay, so the `gen_plan_dataset_1` directory, specifically located at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/` is completely barren. That's not ideal, I was expecting some data there. This iteration seems to be off to a rocky start. Le
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads/"}], "is_error":
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<hypothesis>
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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Build a curated cohort of 40-80 public GitHub OSS projects where the identified founder has departed, with per-month founder
  involvement time series (share of commits, merges, reviews) from inception to departure, and a survival label (survived
  vs collapsed) based on the Avelino TFDD criterion.
approach: >-
  Step 1: Identify candidate projects by searching for popular OSS projects with a clear founder who became inactive (using
  GitHub search, GitHub Archive, or curated lists of abandoned/revived projects). Step 2: For each candidate, clone the repo
  and extract: (a) founder identity (earliest sustained contributor), (b) founder departure date (12-month inactivity window),
  (c) per-month founder share of commits, PR merges, and code reviews from inception to departure, (d) post-departure activity
  metrics for 24 months. Step 3: Label survival using the Avelino TFDD criterion (new truck-factor developer appears post-departure
  with sustained activity) or fallback continuous metric (normalized post-departure commit volume). Step 4: Output as JSON
  with rows containing: project_id, founder, departure_date, pre_departure_months, monthly_founder_share_commits, monthly_founder_share_merges,
  monthly_founder_share_reviews, survival_label, static_features (bus_factor, contributor_count, project_age, stars, file_count
  at departure). Use parallel cloning and extraction to stay within the 6-hour time budget.
depends_on: []
</artifact_direction>



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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [16] HUMAN-USER prompt · 2026-08-21 15:15:25 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [17] RETRY (attempt 2) · 2026-08-21 15:17:34 UTC

```
Agent result indicates failure (attempt 2/6): structured_output is None
```

### [18] RETRY (attempt 3) · 2026-08-21 15:17:35 UTC

```
Agent retry... (attempt 3/6): structured_output is None
```

### [19] CONFIG · 2026-08-21 15:17:35 UTC

```
Model: openai/deepseek-ai/deepseek-v4-pro | Session: 191c2b53-ba8e-41cd-a0cd-a160d85a58f7 | CWD: /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [20] SYSTEM PROMPT · 2026-08-21 15:17:37 UTC

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
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

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

### [21] SYSTEM-USER prompt · 2026-08-21 15:17:37 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed
  a smooth, prolonged fade — a gradually declining trajectory, measurable as the s
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [agent_think]: **Dataset Artifact Plan: Initial Thoughts**

Okay, so the user wants a plan for building a DATASET artifact. The objective is clear: curate a set of 40-80 open-source GitHub projects where the founders have left. I need to track the founder's involvement time series – things like commits, merges, an
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr
  - [agent_think]: **Empty Directory Blues**

Okay, so the `gen_plan_dataset_1` directory, specifically located at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/` is completely barren. That's not ideal, I was expecting some data there. This iteration seems to be off to a rocky start. Le
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads/"}], "is_error":
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the f
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [PauseEvent]
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<hypothesis>
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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Build a curated cohort of 40-80 public GitHub OSS projects where the identified founder has departed, with per-month founder
  involvement time series (share of commits, merges, reviews) from inception to departure, and a survival label (survived
  vs collapsed) based on the Avelino TFDD criterion.
approach: >-
  Step 1: Identify candidate projects by searching for popular OSS projects with a clear founder who became inactive (using
  GitHub search, GitHub Archive, or curated lists of abandoned/revived projects). Step 2: For each candidate, clone the repo
  and extract: (a) founder identity (earliest sustained contributor), (b) founder departure date (12-month inactivity window),
  (c) per-month founder share of commits, PR merges, and code reviews from inception to departure, (d) post-departure activity
  metrics for 24 months. Step 3: Label survival using the Avelino TFDD criterion (new truck-factor developer appears post-departure
  with sustained activity) or fallback continuous metric (normalized post-departure commit volume). Step 4: Output as JSON
  with rows containing: project_id, founder, departure_date, pre_departure_months, monthly_founder_share_commits, monthly_founder_share_merges,
  monthly_founder_share_reviews, survival_label, static_features (bus_factor, contributor_count, project_age, stars, file_count
  at departure). Use parallel cloning and extraction to stay within the 6-hour time budget.
depends_on: []
</artifact_direction>



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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [22] HUMAN-USER prompt · 2026-08-21 15:17:37 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [23] RETRY (attempt 3) · 2026-08-21 15:17:37 UTC

```
Agent result indicates failure (attempt 3/6): structured_output is None
```

### [24] RETRY (attempt 4) · 2026-08-21 15:17:37 UTC

```
Agent retry... (attempt 4/6): structured_output is None
```

### [25] CONFIG · 2026-08-21 15:17:38 UTC

```
Model: openai/@cf/google/gemma-4-26b-a4b-it | Session: 4be9bfee-afc5-45ca-9b1a-88546a6070b7 | CWD: /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1 | Tools: 2 | Permission: acceptEdits
```

### [26] SYSTEM PROMPT · 2026-08-21 15:18:15 UTC

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
<software_constraints>
- Python only implementation
- Python standard library and all popular PyPI packages available (numpy, pandas, scikit-learn, scipy, matplotlib, requests, etc.)
- Local parallelism encouraged: multiprocessing, asyncio, threading — see aii-parallel-computing skill
- LLM API calls must go through OpenRouter only (no direct OpenAI, Anthropic, etc.)
- **SPEND BUDGET**: at most $10 USD of OpenRouter API calls for this artifact. Nothing outside your own code enforces this — the key you are given has no per-artifact cap — so it holds only if you track cumulative cost after every call and stop when you approach it. Budget the work up front: estimate the per-call cost and the number of calls BEFORE starting a sweep, not after it overruns. Exceeding it spends real money that the run cannot recover.
</software_constraints>

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

### [27] SYSTEM-USER prompt · 2026-08-21 15:18:15 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed
  a smooth, prolonged fade — a gradually declining trajectory, measurable as the s
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [agent_think]: **Dataset Artifact Plan: Initial Thoughts**

Okay, so the user wants a plan for building a DATASET artifact. The objective is clear: curate a set of 40-80 open-source GitHub projects where the founders have left. I need to track the founder's involvement time series – things like commits, merges, an
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr
  - [agent_think]: **Empty Directory Blues**

Okay, so the `gen_plan_dataset_1` directory, specifically located at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/` is completely barren. That's not ideal, I was expecting some data there. This iteration seems to be off to a rocky start. Le
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the files and directories up to 2 levels deep in /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads, excluding hidden items:\n/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads/"}], "is_error":
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the f
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [PauseEvent]
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <hypothesis>
kind: hypothesis
title: Founder Fade Curve Predicts OSS Survival
hypothesis: >-
  An open-source project survives its founder stepping away if and only if the f
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<hypothesis>
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
</hypothesis>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the methods, proper baselines, and evaluation this field demands.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_direction>
Make this direction concrete and actionable. Keep the same type and respect dependencies.

id: dataset_iter1_dir2
type: dataset
objective: >-
  Build a curated cohort of 40-80 public GitHub OSS projects where the identified founder has departed, with per-month founder
  involvement time series (share of commits, merges, reviews) from inception to departure, and a survival label (survived
  vs collapsed) based on the Avelino TFDD criterion.
approach: >-
  Step 1: Identify candidate projects by searching for popular OSS projects with a clear founder who became inactive (using
  GitHub search, GitHub Archive, or curated lists of abandoned/revived projects). Step 2: For each candidate, clone the repo
  and extract: (a) founder identity (earliest sustained contributor), (b) founder departure date (12-month inactivity window),
  (c) per-month founder share of commits, PR merges, and code reviews from inception to departure, (d) post-departure activity
  metrics for 24 months. Step 3: Label survival using the Avelino TFDD criterion (new truck-factor developer appears post-departure
  with sustained activity) or fallback continuous metric (normalized post-departure commit volume). Step 4: Output as JSON
  with rows containing: project_id, founder, departure_date, pre_departure_months, monthly_founder_share_commits, monthly_founder_share_merges,
  monthly_founder_share_reviews, survival_label, static_features (bus_factor, contributor_count, project_age, stars, file_count
  at departure). Use parallel cloning and extraction to stay within the 6-hour time budget.
depends_on: []
</artifact_direction>



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
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [28] HUMAN-USER prompt · 2026-08-21 15:18:15 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [29] THINKING · 2026-08-21 15:19:10 UTC

````
The objective is to create a plan for a DATASET artifact.
The hypothesis is that an OSS project survives its founder's departure if their involvement follows a "smooth, prolonged fade" (scaffolding) rather than an abrupt cliff or a plateau-then-cliff.

The dataset needs to be a curated cohort of 40-80 public GitHub OSS projects where:
1. The founder has departed (defined by 12 months of inactivity).
2. Per-month founder involvement time series (commits, merges, reviews) is available from inception to departure.
3. Survival labels (survived vs. collapsed) are available based on the Avelino TFDD criterion (new active truck-factor developer appears post-departure).
4. Static features (bus factor, contributor count, project age, stars, file count at departure) are available.

Format: JSON with specific fields (`project_id`, `founder`, `departure_date`, `pre_departure_months`, `monthly_founder_share_commits`, `monthly_founder_share_merges`, `monthly_founder_share_reviews`, `survival_label`, `static_features`).

1.  **Identify Candidates**:
    *   Use GitHub search/APIs to find repositories.
    *   Search for "abandoned oss", "archived repositories", or use datasets like GH Archive.
    *   Look for projects that were once popular (high stars) but saw a sudden drop in activity.
    *   Alternatively, look for "revived" projects (projects that were inactive then had a surge of new contributors/activity).
    *   Search for lists of "dead open source projects".

2.  **Filtering & Identification (The "Founder" and "Departure" part)**:
    *   For a candidate, identify the creator/founder (earliest sustained contributor).
    *   Calculate the founder's activity profile.
    *   Identify a "departure event" (12 months of founder inactivity).
    *   Check if the project "collapsed" (no activity/new contributors) or "survived" (new truck-factor developer emerges) in the 24 months following the departure.

3.  **Data Extraction (The "Time Series" part)**:
    *   Clone the repo.
    *   Parse git history (commits, authors).
    *   Parse Pull Requests (merges, authors, reviewers) - this might require the GitHub API as git history doesn't always store the "reviewer" role explicitly in the log, though it's in the PR metadata.
    *   Compute monthly shares of total activity for the founder.

4.  **Standardization**:
    *   Consolidate everything into the requested JSON format.

*   `title`: 4-8 words. "OSS Founder Departure & Survival Dataset" or "Founder Fade Curve OSS Dataset".
*   `summary`: A brief summary of what the dataset contains.
*   `runpod_compute_profile`: Since this involves cloning many repos and parsing histories, `cpu_heavy` is appropriate.
*   `ideal_dataset_criteria`: 40-80 projects, JSON format, includes time-series (monthly shares) and survival labels.
*   `dataset_search_plan`:
    *   Step 1: Search for candidate repositories (GitHub search, GH Archive, lists of abandoned/revived projects).
    *   Step 2: Implement a filtering script to identify "founder departure" (12m inactivity) and "survival" (Avelino criterion).
    *   Step 3: Extraction loop (cloning, parsing git/PR history for founder's share of commits, merges, reviews).
    *   Step 4: Feature extraction (static features at departure).
    *   Step 5: Validation and JSON assembly.
*   `target_num_datasets`: This is a single dataset (a collection of projects), so `1`? Or should I count the projects? The instructions say "Count each dataset separately, not collections". But the output is a single `data_out.json`. Usually, for a curated cohort, the target is the number of *instances* if it were a benchmark, but here it's one dataset. I'll set it to 1. Wait, if I set it to 1, the executor might just find one dataset. But this is a *curated* dataset that needs to be *built*. The instructions for DATASET say "Collect, prepare, and merge datasets...". So the executor is building a custom dataset. I'll treat the "dataset" as the resulting JSON file.

Let's refine the `dataset_search_plan`.
1.  **Discovery Phase**: Use GitHub search queries (e.g., `stars:>500 archived:true`, or searching for keywords like "abandoned" in READMEs/issues) and GH Archive to find projects that underwent significant activity shifts.
2.  **Screening Phase**:
    *   Define "Founder" as the first user with significant, sustained activity.
    *   Locate "Departure" (the first 12-month window where the founder had no commits/merges/reviews).
    *   Determine "Survival" status based on the 24 months following departure (check for new top contributors/TF-developers).
3.  **Extraction Phase**:
    *   For candidates passing the screen, perform intensive repo crawling.
    *   Calculate the monthly share of activity (commits, PR merges, code reviews) for the founder from repo inception to departure.
    *   Calculate static snapshots at departure: star count, contributor count, total files, etc.
4.  **Consolidation Phase**:
    *   Format all project data into a single `data_out.json`.
    *   Validate against the target schema.

*   `title`: "OSS Founder Departure Survival Dataset"
*   `summary`: "A curated dataset of 40-80 GitHub projects tracking founder involvement trajectories (commits, merges, reviews) and project survival labels."
*   `ideal_dataset_criteria`: "A single JSON file containing 40-80 rows. Each row represents a GitHub project and includes: (1) founder identity and departure date, (2) a time-series of the founder's monthly share of commits, merges, and reviews from inception to departure, (3) survival labels (based on the Avelino TFDD criterion), and (4) static project metrics at the time of departure (stars, contributor count, etc.)."
*   `dataset_search_plan`: "1. **Candidate Discovery**: Search GitHub for abandoned/archived repositories with high stars and use GH Archive data to identify projects that experienced a sudden drop in activity. 2. **Founder & Departure Screening**: For each candidate, identify the founder (earliest sustained contributor) and find their departure point (a 12-month period of inactivity). 3. **Survival Labeling**: Label projects as 'survived' or 'collapsed' based on whether new truck-factor developers emerged in the 24 months following the founder's departure. 4. **Temporal Data Extraction**: For survivors and collapsed projects, clone the repository and use git/GitHub API to extract the monthly share of commits, merges, and code reviews performed by the founder from project start to departure. 5. **Feature Extraction**: Capture static metadata (stars, files, contributor count) at the moment of departure. 6. **Final Assembly**: Merge all data into a standardized JSON format."
*   `target_num_datasets`: 1 (The final curated collection).

Let's double check the `target_num_datasets` instruction: "How many individual datasets should be delivered. Count each dataset separately, not collections — a benchmark suite of N datasets counts as N."
Since this is a single curation task resulting in one JSON file, 1 is correct.

Wait, the executor is an agent. If I say 1, it might think it only needs to find one project. But the *objective* is 40-80. The `target_num_datasets` usually refers to how many *files* or *different sources*. In this case, we are *creating* a dataset. I will specify the requirement for 40-80 projects in the `ideal_dataset_criteria`.

Actually, looking at the `ideal_dataset_criteria` and `dataset_search_plan` is where the detail goes.

One concern: "Code reviews" are hard to get from git history. They usually require the GitHub API (Pull Request review events). The plan should mention using the GitHub API to get PR review data.

Final check of the schema and requirements.
- `title`: "OSS Founder Departure Survival Dataset" (5 words) - Good.
- `summary`: "Curated cohort of 40-80 GitHub projects tracking founder involvement trajectories and survival status." - Good.
- `runpod_compute_profile`: `cpu_heavy` - Good (cloning and parsing git history is intensive).
- `ideal_dataset_criteria`: "A single JSON file containing 40-80 curated project records. Each record must include: temporal founder activity (monthly shares of commits, PR merges, and code reviews from inception to departure), a binary survival label (Avelino TFDD criterion), and static project features (stars, file count, contributor count, project age) captured at the time of departure." - Good.
- `dataset_search_plan`: "1. **Discovery**: Use GitHub search and GH Archive to identify high-star repositories that transitioned to inactivity or were archived. 2. **Founder/Departure Screening**: For each project, identify the founder (earliest significant contributor) and detect their 'departure' (a 12-month inactivity window). 3. **Survival Labeling**: Classify projects as 'survived' or 'collapsed' by checking for new active truck-factor developers in the 24 months post-departure. 4. **Intensive Extraction**: For qualified projects, clone repositories and use the GitHub API to extract monthly shares of commits, merges, and reviews for the founder throughout the pre-departure period. 5. **Metadata Collection**: Record static project features at the moment of founder departure. 6. **Consolidation**: Compile into a single JSON file." - Good.
- `target_num_datasets`: 1.

Wait, is there any risk of exceeding the 300MB limit? 40-80 projects' metadata in JSON is tiny. The *cloned repositories* might be large, but the executor only needs to output the JSON. The plan should emphasize that only the *extracted metadata* is saved to the JSON.

One more detail: "The executor has 6h total". 40-80 projects is a lot for 6h if it clones everything. The plan should suggest "parallel cloning and extraction" (as mentioned in the artifact direction).

Let's refine the `dataset_search_plan` one last time to be very specific about the "per-month" requirement.

`dataset_search_plan`: "1. **Candidate Discovery**: Search GitHub and GH Archive for high-star repositories that were either archived or showed a significant drop in activity. 2. **Founder & Departure Detection**: For candidates, identify the founder (the earliest user with sustained activity) and find their departure (a 12-month period of total inactivity). 3. **Survival Labeling**: Apply the Avelino TFDD criterion—checking for the arrival of new truck-factor developers in the 24 months following the departure—to label the project as 'survived' or 'collapsed'. 4. **Time-Series Extraction**: For the selected 40-80 projects, clone the repos and use the GitHub API to extract the founder's monthly share of total commits, PR merges, and code reviews from the project's inception until departure. 5. **Feature Capture**: Capture static snapshots (stars, contributor count, project age, file count) at the moment of departure. 6. **Finalization**: Aggregate all extracted data into a single, validated JSON file."

This looks solid.

One detail: `monthly_founder_share_reviews`. Reviews are PR-based. The executor will need the GitHub API. I'll make sure the plan mentions the API.

The `target_num_datasets` should be 1 because we are delivering one JSON file containing the whole cohort.

Final Plan Structure:
- Title: OSS Founder Departure Survival Dataset
- Summary: A dataset of 40-80 GitHub projects tracking the temporal trajectories of founder involvement and subsequent project survival.
- Runpod: cpu_heavy
- Ideal Criteria: JSON with 40-80 rows. Each row: project_id, founder, departure_date, monthly_founder_share_commits, monthly_founder_share_merges, monthly_founder_share_reviews (from inception to departure), survival_label, and static features at departure (stars, contributors, age, files).
- Search Plan: (the 6 steps above)
- Target Num: 1

Wait, the `ideal_dataset_criteria` field description in schema says "What makes an ideal dataset for this purpose - size, format, content requirements".
The `dataset_search_plan` field description says "Step-by-step plan for finding/creating this dataset - sources to check, fallback options".

I'll make sure these are clearly delineated.

One edge case: If the executor can't find 40 projects, it should deliver what it found. The plan should mention this.

```json
{
  "title": "OSS Founder Departure Survival Dataset",
  "summary": "A curated dataset of 40-80 GitHub projects tracking founder involvement trajectories and project survival labels.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "A single JSON file (`data_out.json`) containing 40-80 project records. Each record must include: (1) founder identity and departure date, (2) a monthly time-series of the founder's share of commits, PR merges, and code reviews from project inception to departure, (3) a binary survival label based on the Avelino TFDD criterion (appearance of new truck-factor developers post-departure), and (4) static project features (stars, contributor count, project age, file count) at the moment of departure.",
  "dataset_search_plan": "1. **Candidate Discovery**: Search GitHub/GH Archive for high-star repositories that were archived or experienced significant activity drops. 2. **Founder/Departure Identification**: For each candidate, identify the founder (earliest sustained contributor) and detect their departure (a 12-month inactivity window). 3. **Survival Labeling**: Label projects as 'survived' or 'collapsed' by verifying if new active truck-factor developers emerged in the 24 months following the departure. 4. **Temporal Data Extraction**: For the final cohort, clone repositories and use the GitHub API to extract the founder's monthly share of total commits, PR merges, and code reviews from inception to departure. 5. **Static Feature Collection**: Extract metadata (stars, file count, etc.) at the time of departure. 6. **Consolidation**: Compile into a validated JSON file. If 40-80 projects cannot be reached, provide the maximum possible cohort discovered.",
  "target_num_datasets": 1
}
```

This looks complete.
````

### [30] ASSISTANT · 2026-08-21 15:19:10 UTC

````
```json
{
  "title": "OSS Founder Departure Survival Dataset",
  "summary": "A curated dataset of 40-80 GitHub projects tracking founder involvement trajectories and project survival labels.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "A single JSON file (`data_out.json`) containing 40-80 project records. Each record must include: (1) founder identity and departure date, (2) a monthly time-series of the founder's share of commits, PR merges, and code reviews from project inception to departure, (3) a binary survival label based on the Avelino TFDD criterion (appearance of new truck-factor developers in the 24 months post-departure), and (4) static project features (stars, contributor count, project age, file count) captured at the moment of departure.",
  "dataset_search_plan": "1. **Candidate Discovery**: Search GitHub and GH Archive for high-star repositories that were either archived or showed a significant, sudden drop in activity (indicating potential abandonment). 2. **Founder & Departure Identification**: For each candidate, identify the 'founder' (the user with the earliest sustained commit/merge activity) and detect a 'departure event' (the first 12-month window of total founder inactivity). 3. **Survival Labeling**: Label each project as 'survived' or 'collapsed' by checking for the arrival of new active truck-factor developers in the 24 months following the founder's departure. 4. **Intensive Data Extraction**: For the selected cohort, clone the repositories and use the GitHub API to extract the founder's monthly share of total project activity (commits, PR merges, and code reviews) from the project's inception until the departure date. 5. **Static Feature Capture**: Extract metadata (stars, contributor count, file count, etc.) as a snapshot at the time of departure. 6. **Consolidation**: Aggregate all findings into a single, standardized JSON file. If the 40-80 target cannot be reached, deliver the largest possible curated cohort found.",
  "target_num_datasets": 1
}
```
````

### [31] HOOK — PostToolUse · 2026-08-21 15:19:11 UTC

```
<system-reminder>You have 53.4 minutes remaining to finish all your tasks.</system-reminder>
```

### [32] HUMAN-USER prompt · 2026-08-21 15:19:12 UTC

```
be more exhaustive
```

### [33] THINKING · 2026-08-21 15:19:41 UTC

```
*   User wants a "more exhaustive" plan for the DATASET artifact.
    *   The current plan is good but could be more detailed regarding the specific metrics, the identification of the "founder", the precise implementation of the "Avelino TFDD criterion", and the technical workflow (parallelism, error handling) needed to stay within the 6-hour execution window.
    *   The goal is to provide the *executor* with a high-fidelity roadmap that minimizes ambiguity.

    *   Goal: 40-80 GitHub OSS projects with founder departure.
    *   Metrics: Monthly share of commits, merges, reviews (pre-departure).
    *   Label: Survival (Avelino TFDD criterion).
    *   Static Features: Stars, age, bus factor, files (at departure).
    *   Constraints: 6h runtime, 300MB limit (for files/downloads), parallel processing recommended.

    *   *Phase 1: Candidate Identification (Broad)*
        *   Need diverse projects (some huge, some niche).
        *   Search for: "archived" repos, "unmaintained" repos, "abandoned" repos.
        *   Use GitHub search queries or BigQuery (GH Archive) if possible via `web-tools` logic/research.
        *   Actually, the executor will use Python/Shell. I should suggest searching for projects with a high star count but low recent activity.

    *   *Phase 2: Refining the Cohort (Narrowing)*
        *   Identify the "Founder": Not just the creator (who might be a bot or organizational account), but the user with the highest density of early commits/merges.
        *   Identify "Departure": A 12-month period of zero activity by this founder.
        *   Verify "Survival": Check 24 months *after* that window for *new* core contributors (the TFDD criterion).

    *   *Phase 3: Extraction (Deep Data)*
        *   Need per-month time series.
        *   Metrics to extract (for the founder):
            *   `share_commits`: $\frac{\text{founder\_commits}_{month}}{\text{total\_commits}_{month}}$
            *   `share_merges`: $\frac{\text{founder\_merges}_{month}}{\text{total\_merges}_{month}}$
            *   `share_reviews`: $\frac{\text{founder\_reviews}_{month}}{\text{total\_reviews}_{month}}$
        *   This is compute-intensive. Parallelization is key.

    *   *Phase 4: Metadata/Static Features*
        *   Snapshot at $T_{departure}$.
        *   `stars`, `forks`, `contributor_count`, `file_count`, `repo_age`.

    *   *Phase 5: Formatting*
        *   JSON structure.
        *   Handle edge cases (founder never left, project died before founder left, etc.).

    *   `ideal_dataset_criteria`: Define the JSON schema explicitly.
    *   `dataset_search_plan`: Break down into:
        1.  Discovery (Repo identification).
        2.  Founder/Departure/Survival filtering (The "Triage" phase).
        3.  Data Extraction (The "Cloning/Parsing" phase).
        4.  Verification & Standardization.

    *   Make sure to mention "Bus Factor" calculation specifically.
    *   Clarify "Avelino TFDD" - it's about *new* high-impact contributors.
    *   Emphasize the "Fade Curve" granularity (monthly).

    *   *Self-Correction during drafting*: The executor is a DATASET agent. It's better to give it a "Triage" logic so it doesn't waste time cloning 1000 repos. First, search for candidates via API/Web, then perform lightweight checks (metadata only), then only clone the 40-80 selected projects.

    *   *Search Plan Structure*:
        1.  Search Stage (Metadata/Search).
        2.  Filtering Stage (Statistical triage - finding the departure/survival).
        3.  Deep Extraction Stage (The hard work: Git history/API calls).
        4.  Output Stage.

    *   *Refined Search Plan details*:
        *   Source 1: GitHub API / Search (queries for archived repos, specific keywords).
        *   Source 2: Curated lists of dead/revived projects (if found via web search).
        *   Filtering logic: (1) Founder detected $\rightarrow$ (2) Departure detected $\rightarrow$ (3) Survival status determined $\rightarrow$ (4) Candidate selected for deep extraction.

    *   *Refined Ideal Criteria details*:
        *   Mention the specific JSON keys: `project_id`, `founder_id`, `departure_date`, `survival_label`, `pre_departure_series` (list of dicts), `static_features_at_departure`.
```

### [34] ASSISTANT · 2026-08-21 15:19:41 UTC

````
```json
{
  "title": "OSS Founder Fade & Survival Dataset",
  "summary": "A curated time-series dataset of 40-80 OSS projects tracking founder involvement decay and post-departure survival.",
  "runpod_compute_profile": "cpu_heavy",
  "ideal_dataset_criteria": "A standardized `data_out.json` containing 40-80 distinct project records. Each record must follow this schema: \n- `project_id` (string: e.g., 'owner/repo')\n- `founder_id` (string: GitHub username)\n- `departure_date` (ISO date: start of 12-month inactivity window)\n- `survival_label` (boolean: true if survived according to Avelino TFDD criterion, false otherwise)\n- `pre_departure_metrics` (list of objects: one per month from inception to departure, containing `month_index`, `founder_commit_share`, `founder_merge_share`, `founder_review_share`, `total_monthly_commits`, `total_monthly_merges`)\n- `post_departure_metrics` (list of objects: one per month for 24 months post-departure, containing `month_index`, `total_monthly_commits`, `total_monthly_merges`, `new_truck_factor_developer_count`)\n- `static_features_at_departure` (object: `stars`, `forks`, `contributor_count`, `file_count`, `repo_age_days`, `bus_factor_at_departure`).\nAll metrics must be calculated as relative shares (0.0 to 1.0) where applicable.",
  "dataset_search_plan": "The executor should follow a multi-stage triage pipeline to maximize efficiency within the 6h limit:\n\n1. **Stage 1: Candidate Discovery (Metadata-only)**\n   - Perform broad searches using GitHub Search/API/Web tools for repositories that are: (a) 'archived', (b) marked as 'unmaintained' in READMEs, or (c) have high star counts (>500) but zero commits in the last 24 months.\n   - Target a broad list of 300-500 candidate URLs to allow for high attrition in later stages.\n\n2. **Stage 2: Triage & Filtering (Lightweight API/Metadata Analysis)**\n   - For each candidate, identify the 'Founder': The user with the highest density of commits/merges in the first 20% of the project's lifecycle.\n   - Detect 'Departure': Identify a continuous 12-month window where the identified founder has zero commits or merges.\n   - Detect 'Survival' (Avelino TFDD Criterion): Check the 24 months following the founder's departure. A project 'survives' if at least one *new* developer (not previously in the top 5 contributors) achieves a significant commit/merge threshold (e.g., >5% of total project volume) during that window.\n   - Filter the list down to the top 60-80 projects that show a clear distinction between 'collapsed' and 'survived' to ensure a balanced dataset.\n\n3. **Stage 3: Deep Data Extraction (Heavy Computation/Git Parsing)**\n   - For the selected 60-80 projects, perform local cloning (using `git clone --bare` to save space) or intensive GitHub API usage.\n   - **Time-Series Extraction**: Iterate through the project history month-by-month from inception to departure. Calculate the founder's share of: (1) total commits, (2) PR merges, and (3) code review actions (if available via API).\n   - **Static Snapshot**: Capture the project's stars, forks, and contributor count exactly at the moment the founder's 12-month inactivity window begins.\n   - **Parallelization**: Use `multiprocessing` or `asyncio` to parallelize the cloning and Git-log parsing of the 60-80 repositories.\n\n4. **Stage 4: Final Validation & JSON Assembly**\n   - Verify all time-series data is continuous (no missing months).\n   - Ensure `survival_label` is logically consistent with the `post_departure_metrics`.\n   - Export the final result to `data_out.json` and validate against the target schema.",
  "target_num_datasets": 1
}
```
````

### [35] SYSTEM-USER prompt · 2026-08-21 15:19:42 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [36] THINKING · 2026-08-21 15:20:16 UTC

````
The user is requesting that I produce the `.sdk_openhands_agent_struct_out.json` file again, following the specific schema provided in the prompt. My previous attempt failed because the file did not exist (it was likely not actually written to the file system, or I just haven't called the `file_editor` to create it).

Looking at the error message: "The output file `.sdk_openhands_agent_struct_out.json` does not exist yet."

I need to use the `file_editor` with the `create` command to save my JSON plan to the specified path.

The schema for the JSON is:
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

My content from the previous response was:
`title`: "OSS Founder Fade & Survival Dataset"
`summary`: "A curated time-series dataset of 40-80 OSS projects tracking founder involvement decay and post-departure survival."
`runpod_compute_profile`: "cpu_heavy"
`ideal_dataset_criteria`: "A standardized `data_out.json` containing 40-80 distinct project records. Each record must follow this schema: \n- `project_id` (string: e.g., 'owner/repo')\n- `founder_id` (string: GitHub username)\n- `departure_date` (ISO date: start of 12-month inactivity window)\n- `survival_label` (boolean: true if survived according to Avelino TFDD criterion, false otherwise)\n- `pre_departure_metrics` (list of objects: one per month from inception to departure, containing `month_index`, `founder_commit_share`, `founder_merge_share`, `founder_review_share`, `total_monthly_commits`, `total_monthly_merges`)\n- `post_departure_metrics` (list of objects: one per month for 24 months post-departure, containing `month_index`, `total_monthly_commits`, `total_monthly_merges`, `new_truck_factor_developer_count`)\n- `static_features_at_departure` (object: `stars`, `forks`, `contributor_count`, `file_count`, `repo_age_days`, `bus_factor_at_departure`).\nAll metrics must be calculated as relative shares (0.0 to 1.0) where applicable."
`dataset_search_plan`: "The executor should follow a multi-stage triage pipeline to maximize efficiency within the 6h limit:\n\n1. **Stage 1: Candidate Discovery (Metadata-only)**\n   - Perform broad searches using GitHub Search/API/Web tools for repositories that are: (a) 'archived', (b) marked as 'unmaintained' in READMEs, or (c) have high star counts (>500) but zero commits in the last 24 months.\n   - Target a broad list of 300-500 candidate URLs to allow for high attrition in later stages.\n\n2. **Stage 2: Triage & Filtering (Lightweight API/Metadata Analysis)**\n   - For each candidate, identify the 'Founder': The user with the highest density of commits/merges in the first 20% of the project's lifecycle.\n   - Detect 'Departure': Identify a continuous 12-month window where the identified founder has zero commits or merges.\n   - Detect 'Survival' (Avelino TFDD Criterion): Check the 24 months following the founder's departure. A project 'survives' if at least one *new* developer (not previously in the top 5 contributors) achieves a significant commit/merge threshold (e.g., >5% of total project volume) during that window.\n   - Filter the list down to the top 60-80 projects that show a clear distinction between 'collapsed' and 'survived' to ensure a balanced dataset.\n\n3. **Stage 3: Deep Data Extraction (Heavy Computation/Git Parsing)**\n   - For the selected 60-80 projects, perform local cloning (using `git clone --bare` to save space) or intensive GitHub API usage.\n   - **Time-Series Extraction**: Iterate through the project history month-by-month from inception to departure. Calculate the founder's share of: (1) total commits, (2) PR merges, and (3) code review actions (if available via API).\n   - **Static Snapshot**: Capture the project's stars, forks, and contributor count exactly at the moment the founder's 12-month inactivity window begins.\n   - **Parallelization**: Use `multiprocessing` or `asyncio` to parallelize the cloning and Git-log parsing of the 60-80 repositories.\n\n4. **Stage 4: Final Validation & JSON Assembly**\n   - Verify all time-series data is continuous (no missing months).\n   - Ensure `survival_label` is logically consistent with the `post_departure_metrics`.\n   - Export the final result to `data_out.json` and validate against the target schema."
`target_num_datasets`: 1

I will now use `file_editor` to create the file.
````

### [37] TOOL CALL — file_editor · 2026-08-21 15:20:16 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json",
  "file_text": "{\n  \"title\": \"OSS Founder Fade & Survival Dataset\",\n  \"summary\": \"A curated time-series dataset of 40-80 OSS projects tracking founder involvement decay and post-departure survival.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"A standardized `data_out.json` containing 40-80 distinct project records. Each record must follow this schema: \\n- `project_id` (string: e.g., 'owner/repo')\\n- `founder_id` (string: GitHub username)\\n- `departure_date` (ISO date: start of 12-month inactivity window)\\n- `survival_label` (boolean: true if survived according to Avelino TFDD criterion, false otherwise)\\n- `pre_departure_metrics` (list of objects: one per month from inception to departure, containing `month_index`, `founder_commit_share`, `founder_merge_share`, `founder_review_share`, `total_monthly_commits`, `total_monthly_merges`)\\n- `post_departure_metrics` (list of objects: one per month for 24 months post-departure, containing `month_index`, `total_monthly_commits`, `total_monthly_merges`, `new_truck_factor_developer_count`)\\n- `static_features_at_departure` (object: `stars`, `forks`, `contributor_count`, `file_count`, `repo_age_days`, `bus_factor_at_departure`).\\nAll metrics must be calculated as relative shares (0.0 to 1.0) where applicable.\",\n  \"dataset_search_plan\": \"The executor should follow a multi-stage triage pipeline to maximize efficiency within the 6h limit:\\n\\n1. **Stage 1: Candidate Discovery (Metadata-only)**\\n   - Perform broad searches using GitHub Search/API/Web tools for repositories that are: (a) 'archived', (b) marked as 'unmaintained' in READMEs, or (c) have high star counts (>500) but zero commits in the last 24 months.\\n   - Target a broad list of 300-500 candidate URLs to allow for high attrition in later stages.\\n\\n2. **Stage 2: Triage & Filtering (Lightweight API/Metadata Analysis)**\\n   - For each candidate, identify the 'Founder': The user with the highest density of commits/merges in the first 20% of the project's lifecycle.\\n   - Detect 'Departure': Identify a continuous 12-month window where the identified founder has zero commits or merges.\\n   - Detect 'Survival' (Avelino TFDD Criterion): Check the 24 months following the founder's departure. A project 'survives' if at least one *new* developer (not previously in the top 5 contributors) achieves a significant commit/merge threshold (e.g., >5% of total project volume) during that window.\\n   - Filter the list down to the top 60-80 projects that show a clear distinction between 'collapsed' and 'survived' to ensure a balanced dataset.\\n\\n3. **Stage 3: Deep Data Extraction (Heavy Computation/Git Parsing)**\\n   - For the selected 60-80 projects, perform local cloning (using `git clone --bare` to save space) or intensive GitHub API usage.\\n   - **Time-Series Extraction**: Iterate through the project history month-by-month from inception to departure. Calculate the founder's share of: (1) total commits, (2) PR merges, and (3) code review actions (if available via API).\\n   - **Static Snapshot**: Capture the project's stars, forks, and contributor count exactly at the moment the founder's 12-month inactivity window begins.\\n   - **Parallelization**: Use `multiprocessing` or `asyncio` to parallelize the cloning and Git-log parsing of the 60-80 repositories.\\n\\n4. **Stage 4: Final Validation & JSON Assembly**\\n   - Verify all time-series data is continuous (no missing months).\\n   - Ensure `survival_label` is logically consistent with the `post_departure_metrics`.\\n   - Export the final result to `data_out.json` and validate against the target schema.\",\n  \"target_num_datasets\": 1\n}",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [38] TOOL RESULT — file_editor · 2026-08-21 15:20:16 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_plan/gen_plan_dataset_1/.sdk_openhands_agent_struct_out.json", "prev_exist": false, "old_content": null, "new_content": "{\n  \"title\": \"OSS Founder Fade & Survival Dataset\",\n  \"summary\": \"A curated time-series dataset of 40-80 OSS projects tracking founder involvement decay and post-departure survival.\",\n  \"runpod_compute_profile\": \"cpu_heavy\",\n  \"ideal_dataset_criteria\": \"A standardized `data_out.json` containing 40-80 distinct project records. Each record must follow this schema: \\n- `project_id` (string: e.g., 'owner/repo')\\n- `founder_id` (string: GitHub username)\\n- `departure_date` (ISO date: start of 12-month inactivity window)\\n- `survival_label` (boolean: true if survived according to Avelino TFDD criterion, false otherwise)\\n- `pre_departure_metrics` (list of objects: one per month from inception to departure, containing `month_index`, `founder_commit_share`, `founder_merge_share`, `founder_review_share`, `total_monthly_commits`, `total_monthly_merges`)\\n- `post_departure_metrics` (list of objects: one per month for 24 months post-departure, containing `month_index`, `total_monthly_commits`, `total_monthly_merges`, `new_truck_factor_developer_count`)\\n- `static_features_at_departure` (object: `stars`, `forks`, `contributor_count`, `file_count`, `repo_age_days`, `bus_factor_at_departure`).\\nAll metrics must be calculated as relative shares (0.0 to 1.0) where applicable.\",\n  \"dataset_search_plan\": \"The executor should follow a multi-stage triage pipeline to maximize efficiency within the 6h limit:\\n\\n1. **Stage 1: Candidate Discovery (Metadata-only)**\\n   - Perform broad searches using GitHub Search/API/Web tools for repositories that are: (a) 'archived', (b) marked as 'unmaintained' in READMEs, or (c) have high star counts (>500) but zero commits in the last 24 months.\\n   - Target a broad list of 300-500 candidate URLs to allow for high attrition in later stages.\\n\\n2. **Stage 2: Triage & Filtering (Lightweight API/Metadata Analysis)**\\n   - For each candidate, identify the 'Founder': The user with the highest density of commits/merges in the first 20% of the project's lifecycle.\\n   - Detect 'Departure': Identify a continuous 12-month window where the identified founder has zero commits or merges.\\n   - Detect 'Survival' (Avelino TFDD Criterion): Check the 24 months following the founder's departure. A project 'survives' if at least one *new* developer (not previously in the top 5 contributors) achieves a significant commit/merge threshold (e.g., >5% of total project volume) during that window.\\n   - Filter the list down to the top 60-80 projects that show a clear distinction between 'collapsed' and 'survived' to ensure a balanced dataset.\\n\\n3. **Stage 3: Deep Data Extraction (Heavy Computation/Git Parsing)**\\n   - For the selected 60-80 projects, perform local cloning (using `git clone --bare` to save space) or intensive GitHub API usage.\\n   - **Time-Series Extraction**: Iterate through the project history month-by-month from inception to departure. Calculate the founder's share of: (1) total commits, (2) PR merges, and (3) code review actions (if available via API).\\n   - **Static Snapshot**: Capture the project's stars, forks, and contributor count exactly at the moment the founder's 12-month inactivity window begins.\\n   - **Parallelization**: Use `multiprocessing` or `asyncio` to parallelize the cloning and Git-log parsing of the 60-80 repositories.\\n\\n4. **Stage 4: Final Validation & JSON Assembly**\\n   - Verify all time-series data is continuous (no missing months).\\n   - Ensure `survival_label` is logically consistent with the `post_departure_metrics`.\\n   - Export the final result to `data_out.json` and validate against the target schema.\",\n  \"target_num_datasets\": 1\n}", "kind": "FileEditorObservation"}
```

### [39] TOOL CALL — finish · 2026-08-21 15:20:18 UTC

```
{
  "message": "The detailed dataset plan for the 'OSS Founder Fade & Survival' hypothesis has been generated and saved to `.sdk_openhands_agent_struct_out.json`. The plan outlines a multi-stage triage pipeline (Discovery, Triage, Deep Extraction, and Validation) to curate a 40-80 project cohort with time-series metrics of founder involvement and survival labels, designed to fit within a 6-hour execution window."
}
```

### [40] TOOL RESULT — finish · 2026-08-21 15:20:18 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "The detailed dataset plan for the 'OSS Founder Fade & Survival' hypothesis has been generated and saved to `.sdk_openhands_agent_struct_out.json`. The plan outlines a multi-stage triage pipeline (Discovery, Triage, Deep Extraction, and Validation) to curate a 40-80 project cohort with time-series metrics of founder involvement and survival labels, designed to fit within a 6-hour execution window."}], "is_error": false, "kind": "FinishObservation"}
```

### [41] HOOK — PostToolUse · 2026-08-21 15:20:18 UTC

```
<system-reminder>You have 52.3 minutes remaining to finish all your tasks.</system-reminder>
```
