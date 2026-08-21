# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:39:25 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [2] HUMAN-USER prompt · 2026-08-20 20:39:25 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: Python coding standards for experiment and evaluation scripts. Covers environment setup, logging, error handling, and code structure.
---

## Environment Setup

- Python 3.12+
- **NEVER use `pip` or `.venv/bin/pip`** — they are not installed. Use `uv` for ALL package operations:
  ```bash
  uv venv .venv --python=3.12
  source .venv/bin/activate  # or: .venv/bin/python script.py
  uv pip install pandas loguru  # NOT: pip install
  ```
- Create `.toml` file with dependencies, create uv `.venv` and activate it
- NO inline dependencies (no `# /// script` headers)

## Logging

Use `loguru` for all logging. Add a file sink alongside stdout.

```python
from loguru import logger
import sys

logger.remove()  # Remove default handler
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")
```

Rules:
- Log every major step (data loading, processing start/end, results)
- If applicable, log every LLM API call input and output
- Truncate long outputs in logs (add truncation logic for potentially large strings)
- Use `logger.error()` in except blocks (traceback auto-captured)

## Error Handling

- Wrap major operations in try/except blocks
- Use `@logger.catch(reraise=True)` decorator on main functions — without `reraise=True`, the script exits 0 even on uncaught exceptions, hiding failures from downstream consumers
- Use explicit exception types, not bare `except:`
- Never silently swallow exceptions — always log them

```python
@logger.catch(reraise=True)
def main():
    try:
        data = load_data(path)
    except FileNotFoundError:
        logger.error("Data file not found")
        raise
    except json.JSONDecodeError:
        logger.error("Invalid JSON in data file")
        raise
```

## Code Structure

- Use `pathlib.Path` for file operations: `Path("data/input.json").read_text()` not `open(...).read()`
- Use type hints for function signatures
- Use keyword arguments for functions with more than 4 parameters
- No hardcoded paths — derive from script location or accept as arguments

## Script Pattern

Standard pattern for experiment/evaluation scripts:

```python
#!/usr/bin/env python3
"""Brief description of what this script does."""

from loguru import logger
from pathlib import Path
import json
import sys

logger.remove()
logger.add(sys.stdout, level="INFO", format="{time:HH:mm:ss}|{level:<7}|{message}")
logger.add("logs/run.log", rotation="30 MB", level="DEBUG")

@logger.catch(reraise=True)
def main():
    # Load data
    data_path = Path("full_data_out.json")
    logger.info(f"Loading data from {data_path}")
    data = json.loads(data_path.read_text())
    logger.info(f"Loaded {len(data['examples'])} examples")

    # Process
    results = []
    for i, example in enumerate(data["examples"]):
        try:
            result = process(example)
            results.append(result)
        except Exception:
            logger.error(f"Failed on example {i}")
            continue

    # Save output
    output = {"examples": results}
    Path("method_out.json").write_text(json.dumps(output, indent=2))
    logger.info(f"Saved {len(results)} results")

if __name__ == "__main__":
    main()
```
````

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: Gradual scaling pattern for long-running autonomous tasks. Use when running experiments, evaluations, or any code that processes data at increasing scale with runtime checks.
---

## Core Principles

1. **Time budget first**: Read your time/runtime constraints before running anything. Set every Bash timeout to fit within the budget.
2. **Start small, scale up**: Run on minimal input first, fix errors, then increase scale.
3. **Extrapolate before scaling**: Use recorded runtimes to predict whether the next step fits in the budget. Don't guess — calculate.
4. **Background execution**: For anything that takes >1 min, run in background (`run_in_background=true`) and do useful work while waiting.
5. **Stop early if needed**: Quality results on less data beats a timeout or crash. It's always acceptable to stop at a smaller scale.

---

## Gradual Scaling Sequence

Run code at increasing data sizes, checking runtime at each step.

Substitute your actual file names:
- `{mini_file}` — mini JSON (3 examples) from dependency workspace
- `{full_file}` — full dataset from dependency workspace
- `{script}` — your processing script (e.g., `./method.py`, `./eval.py`)
- `{schema}` — JSON schema to validate output against

**STEP 1 — MINI DATA:** Run `{script}` on `{mini_file}`. Do NOT truncate logs. Fix all errors. Validate output against `{schema}`. Verify you are NOT using mock scripts, mock data, or mock APIs.

**STEP 2 — 10 EXAMPLES:** Modify `{script}` to load only the first 10 examples from `{full_file}`. Run and fix errors. Validate schema. Record the runtime.

**STEP 3 — 50 EXAMPLES:** Load first 50 examples from `{full_file}`. Run and fix errors. Record runtime. **EXTRAPOLATE**: Using runtimes from steps 2-3, estimate time per example. Calculate how many examples fit in your remaining time budget. If 50 already used most of the budget, stop here.

**STEP 4 — 100 EXAMPLES (if budget allows):** Load first 100 examples. Run and fix errors. Record runtime. Re-extrapolate with the new data point.

**STEP 5 — 200 EXAMPLES (if budget allows):** Load first 200 examples from `{full_file}`. Run and fix errors. Record runtime.

**STEP 6 — MAXIMIZE:** Using all recorded runtimes, extrapolate time-per-example (it may not be perfectly linear — account for overhead). Calculate the maximum number of examples that fits within your remaining time budget with a 10% safety margin. Load that many (or all if they fit). Run and validate.

## Final Testing Phase

After completing the scaling sequence, redo the entire sequence **one more time** up to your final example count:

mini → 10 → 50 → 100 → 200 → max

At each scale: look for issues, fix problems, validate output, ensure it completes within time limits.

---

## Background Execution

For any step that takes >1 min, run as a **background task**:

1. Launch with Bash `run_in_background=true`
2. While it runs, use the time productively:
   - Sanity-check previous outputs
   - Verify file integrity (correct field names, non-empty values)
   - Review code for edge cases at larger scale
   - Prepare the next step
3. Check back on the background task to get results
4. If it failed, fix errors and re-run

---

## Resource Limits

Set hard RAM and CPU time limits so code fails fast instead of crashing the system. Read limits from `<hardware>` and leave headroom for the OS (e.g., if 16GB total, cap at 14GB).

Python example using stdlib `resource` module:
```python
import resource
resource.setrlimit(resource.RLIMIT_AS, (14 * 1024**3, 14 * 1024**3))  # 14GB RAM
resource.setrlimit(resource.RLIMIT_CPU, (3600, 3600))  # 1 hour CPU time
```
Exceeding RAM raises `MemoryError`. Exceeding CPU time sends `SIGKILL`.

## Monitoring

At each step, record runtime AND check resource usage (`free -h` for RAM, `top -bn1 | head -5` for CPU). If memory usage is climbing toward the limit or CPU is pegged, stop and investigate before scaling further.
````

### [5] SKILL-INPUT — aii-json · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: JSON validation and formatting toolkit. Validate JSON files against schemas for experiment pipelines, and generate full/mini/preview versions of JSON datasets. Use for validating pipeline outputs, checking schema compliance, or creating size-optimized JSON variants.
---

## Contents

- Validating JSON (schema validation against experiment schemas)
- Formatting JSON (generate full/mini/preview versions)

**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:
```
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json"
export PY="$SKILL_DIR/../.ability_client_venv/bin/python"
```

---

## Validating JSON

Validate JSON files against predefined schemas for experiment-based hypothesis selection, data collection, solution generation, and evaluation.

### Quick Start

1. Read the schema spec you need to adhere to (e.g., `schemas/exp_eval_sol_out.json`)
2. Create your output file following that schema structure
3. Validate:

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /path/to/eval_out.json
```

### Script: aii_json_validate_schema.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_validate_schema.py --format exp_eval_sol_out --file /tmp/eval_out.json
```

**Parallel execution (multiple validations):**

IMPORTANT: When validating multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_validate_schema.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --format {1} --file {2}' ::: 'exp_sel_data_out' 'exp_gen_sol_out' 'exp_eval_sol_out' :::+ '/tmp/full_data_out.json' '/tmp/method_out.json' '/tmp/eval_out.json'
```

**Example output (success):**
```
Validating: aii_json_validate_schema.py
Format: exp_eval_sol_out

✓ Validation PASSED
```

**Example output (failure):**
```
Validating: aii_json_validate_schema.py
Format: exp_sel_data_out

✗ Validation FAILED

Errors:
  Path: datasets → 0 → examples → 0
  Error: 'output' is a required property
  Validator: required
```

**Parameters:**

`--format` (required)
- Format type to validate against
- Determines which schema to use

`--file` (required)
- Path to JSON file to validate
- Must be valid JSON
- **Always pass an absolute path.** Relative paths resolve from the
  ability server's CWD (typically ``/ai-inventor/aii_server``), not from
  your agent workspace, so ``data_out/x.json`` will silently look in the
  wrong directory and fail with "Could not load JSON file". The validate
  endpoint also accepts a ``workspace_dir`` arg if you need to keep a
  relative path — pass your workspace path there.

**Tips:**
- Fix errors in your JSON and rerun validation until it passes

### Schema Files

Schemas are stored in `.claude/skills/aii-json/schemas/`:

**Hypothesis Selection & Evaluation:**
- `sel_hypo_out.json` - Hypothesis Selection output (all hypotheses with selected flags)
- `feasibility_eval_all.json` - All hypotheses with feasibility scores
- `feasibility_eval_top.json` - Top 5 most feasible hypotheses
- `novelty_research_one.json` - Single hypothesis novelty research arguments with citations
- `novelty_eval_all.json` - All hypotheses with novelty scores
- `novelty_eval_top.json` - Single best selected hypothesis

**Experiment Pipeline:**
- `exp_sel_data_out.json` - Experiment Data Selection format
- `exp_gen_sol_out.json` - Experiment Solution Generation format
- `exp_eval_sol_out.json` - Experiment Solution Evaluation format

---

## Formatting JSON

Generate three size-optimized versions of a JSON file for efficient development and preview:
- **full**: Identical to original (all data)
- **mini**: First 3 items only (for quick testing)
- **preview**: Mini + all strings truncated to 200 chars (for quick inspection)

### Quick Start

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

### Script: aii_json_format_mini_preview.py

**Example input:**
```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_json_format_mini_preview.py --input method_out.json
```

**Parallel execution (multiple files):**

IMPORTANT: When formatting multiple files, use GNU parallel instead of separate Bash tool calls:
```bash
export SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-json" && \
export PY="$SKILL_DIR/../.ability_client_venv/bin/python" && \
export S="$SKILL_DIR/scripts/aii_json_format_mini_preview.py" && \
parallel -j 50 -k --group --will-cite '$PY $S --input {}' ::: 'full_data_out.json' 'method_out.json' 'eval_out.json'
```

**Example output:**
```
Generated 3 versions:
  Full (50 items): /path/to/full_method_out.json
  Mini (3 items): /path/to/mini_method_out.json
  Preview (3 items, truncated): /path/to/preview_method_out.json
```

**Parameters:**

`--input` (required)
- Path to input JSON file
- Must have a top-level array
- Example: `method_out.json`, `full_data_out.json`

`--output-dir` (optional)
- Output directory for generated files
- Default: same directory as input file
- Files are prefixed with `full_`, `mini_`, `preview_`

**Output Files:**

All three files use the same base name with different prefixes:
- `full_{basename}.json` - Complete dataset (identical to original)
- `mini_{basename}.json` - First 3 array items only
- `preview_{basename}.json` - First 3 items with strings truncated to 200 chars

**Tips:**
- Input JSON must have a top-level array structure
- String truncation is recursive (applies to nested objects and arrays)
- Use preview files for quick inspection without reading large datasets
- Use mini files for developing/testing code before running on full dataset

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: File size check procedure for splitting oversized output files. Use after generating JSON output files to check and split files exceeding the provided size limit.
---

## File Size Check

After generating output files, run `ls -lh` to check sizes. If ANY file exceeds the provided file size limit:

1. Create directory with same base name (e.g., `data_out/` for `full_data_out.json`)
2. Split into parts under the limit named: `full_data_out_1.json`, `full_data_out_2.json`, etc.
3. Place parts in directory (e.g., `data_out/full_data_out_1.json`, `data_out/full_data_out_2.json`)
4. Delete the original oversized file
5. Update the script to read from split files: `for f in sorted(glob.glob('data_out/full_data_out_*.json')): data.extend(json.load(open(f)))`
6. For each split part, generate its own mini/preview versions with the json skill's format script
```

### [7] SKILL-INPUT — aii-use-hardware · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: Detect hardware and use it responsibly. Covers CPU/RAM/GPU detection, memory-safe data processing, and resource-aware computation.
---

**Step 1** — Run `bash scripts/get_hardware.sh` (relative to this skill's directory).

Read the `=== CGROUP ===` section carefully. If `Type: cgroup v1` or `cgroup v2`:
- You are in a **container with hard resource limits**. Exceeding them = OOM kill, no recovery.
- **Never** use `psutil.virtual_memory().total`, `free -h`, `/proc/meminfo`, `os.cpu_count()`, or `nproc` for resource limits — these report **host** values, not your container's allocation.
- **Always** read limits from the cgroup paths shown in the output, or use the Python helpers below.
- For **runtime memory monitoring**, read current usage from cgroup too:
  - v2: `/sys/fs/cgroup/memory.current`
  - v1: `/sys/fs/cgroup/memory/memory.usage_in_bytes`

**Step 2** — Use Step 1 results to pick package variants **before** installing.

Defaults often target the most powerful environment — PyPI's `torch` ships with CUDA libs even on CPU-only hosts. Wrong variant = wasted disk, slow setup, possible import-time failures.

If `=== GPU ===` shows `No GPU`, install torch's CPU build (skips ~4.5GB of CUDA libs):
```bash
uv pip install torch --extra-index-url https://download.pytorch.org/whl/cpu
```
Same idea for any library whose wheel selection depends on detected hardware (GPU/CPU-only builds, architecture-specific wheels).

After install, sanity-check imports right away (`python -c "import torch"`). Disk-pressure or interrupted installs leave half-built wheels (e.g. `libtorch_global_deps.so` missing) — catch these before the experiment runs.

**Step 3** — Set Python constants from the Step 1 results:
```python
import os, math, torch, psutil
from pathlib import Path

def _detect_cpus() -> int:
    """Detect actual CPU allocation (containers/pods/bare metal)."""
    try:  # cgroups v2 quota
        parts = Path("/sys/fs/cgroup/cpu.max").read_text().split()
        if parts[0] != "max":
            return math.ceil(int(parts[0]) / int(parts[1]))
    except (FileNotFoundError, ValueError): pass
    try:  # cgroups v1 quota
        q = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_quota_us").read_text())
        p = int(Path("/sys/fs/cgroup/cpu/cpu.cfs_period_us").read_text())
        if q > 0:
            return math.ceil(q / p)
    except (FileNotFoundError, ValueError): pass
    try:  # CPU affinity (cpuset — used by RunPod, Docker --cpuset-cpus)
        return len(os.sched_getaffinity(0))
    except (AttributeError, OSError): pass
    return os.cpu_count() or 1

def _container_ram_gb() -> float | None:
    """Read RAM limit from cgroup (containers/pods)."""
    for p in ["/sys/fs/cgroup/memory.max", "/sys/fs/cgroup/memory/memory.limit_in_bytes"]:
        try:
            v = Path(p).read_text().strip()
            if v != "max" and int(v) < 1_000_000_000_000:
                return int(v) / 1e9
        except (FileNotFoundError, ValueError): pass
    return None

NUM_CPUS = _detect_cpus()
HAS_GPU = torch.cuda.is_available()
VRAM_GB = torch.cuda.get_device_properties(0).total_mem / 1e9 if HAS_GPU else 0
DEVICE = torch.device("cuda" if HAS_GPU else "cpu")
TOTAL_RAM_GB = _container_ram_gb() or psutil.virtual_memory().total / 1e9
AVAILABLE_RAM_GB = min(psutil.virtual_memory().available / 1e9, TOTAL_RAM_GB)
```

## Step 4 — Set Memory Limits

OOM kills the entire container. **Every script MUST set RAM and VRAM limits at startup.**

Decide the budget based on what the script actually needs. Estimate data size × 2-5x for in-memory overhead, then add ~50% breathing room for temporaries. You may use up to 90% of available RAM/VRAM, but **scale gradually** — start small (e.g. 30-50%), verify it works, then increase toward the limit. Never exceed 90% to keep a buffer for the OS, system processes, and the agent runtime itself. Going over crashes the container/machine with no recovery.

```python
import resource, psutil

_avail = psutil.virtual_memory().available
RAM_BUDGET = ???  # YOU decide: estimate what this script needs (in bytes)
assert RAM_BUDGET < _avail, f"Budget {RAM_BUDGET/1e9:.1f}GB > available {_avail/1e9:.1f}GB"
resource.setrlimit(resource.RLIMIT_AS, (RAM_BUDGET * 3, RAM_BUDGET * 3))  # 3x: virtual > RSS; raises MemoryError on exceed

if HAS_GPU:
    _free, _total = torch.cuda.mem_get_info(0)
    VRAM_BUDGET = ???  # YOU decide: estimate GPU memory needs
    torch.cuda.set_per_process_memory_fraction(min(VRAM_BUDGET / _total, 0.95))  # raises OutOfMemoryError on exceed
```

## Memory-Safe Data Processing

- **One at a time**: load one large object → process → `del obj; gc.collect()` → next
- **Load only what you need**: select specific tables/columns/rows, not entire databases
- **Test small first**: run on a sample before scaling to full data to estimate memory/time
- **Free intermediates in loops**: don't accumulate large results — aggregate incrementally
- **Size before loading**: check file/dataset size before loading; if it's >30% of `RAM_BUDGET`, chunk it

## Common Mistakes (from real crashes)

- **Skipping this skill entirely** — loading data with no RAM detection, no limits, no budget. Container OOM-killed, all agents lost.
- **Using `psutil.virtual_memory().total` instead of `_container_ram_gb()`** — reports host RAM (e.g. 66 GB) when container limit is 28 GB. You MUST use the cgroup-aware functions above.
- **Loading all tables from a multi-table database at once** — one agent loaded 14 RelBench tables simultaneously, spiked past container limit.
- **Setting no memory limits** — without `resource.setrlimit` (RAM) and `set_per_process_memory_fraction` (VRAM), a runaway script OOM-kills the container instead of raising a catchable error.
- **Using `os.cpu_count()` directly** — returns host CPUs (e.g. 192) instead of container limit (e.g. 4) on RunPod/Docker. Always use `_detect_cpus()` above which checks cgroup quota → CPU affinity → `os.cpu_count()` in order.

## Hardware Use

- Keep these results in mind for ALL subsequent tasks — don't assume more than detected
- GPU if available and parallelizable, multiprocessing if multiple CPUs
- Push available resources to their full potential — don't leave hardware idle
````

### [8] SKILL-INPUT — aii-parallel-computing · 2026-08-20 20:39:44 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "CRITICAL PERFORMANCE SKILL. Maximize hardware utilization for compute-intensive tasks. Covers GPU acceleration, CPU parallelism, and async I/O. The difference between hours of failure and minutes of success. Use whenever writing ANY script that processes data, makes API calls, or does computation."
---

**ALWAYS parallelize. Sequential processing is unacceptable for any non-trivial workload.** A sequential script doing 1000 API calls takes hours and fails halfway. An async version finishes in minutes with proper error handling. ALWAYS ask: "Can this run in parallel?" — the answer is almost always yes.

Read aii-use-hardware skill first → get `NUM_CPUS`, `HAS_GPU`, `VRAM_GB`, `device`. Set `NUM_WORKERS` proportional to available CPU capacity — check `psutil.cpu_percent(interval=1)` and scale accordingly (e.g. 30% used → use ~70% of cores).

## Decision Tree (follow strictly)

- **I/O-bound** (API calls, downloads, web, file reads) → `asyncio` + `aiohttp` with `Semaphore(NUM_WORKERS * 4)`. NEVER do sequential HTTP requests in a loop.
- **CPU-bound, vectorizable** → GPU available: PyTorch on device / No GPU: NumPy vectorized ops. NEVER loop over array elements in Python.
- **CPU-bound, independent items** → `ProcessPoolExecutor(max_workers=NUM_WORKERS)`. NEVER process items one-by-one when they're independent.
- **Sequential** → only acceptable when items have data dependencies (each depends on the previous result).

## GPU Rules

- Use up to 90% of available VRAM — scale gradually (start small, increase after each successful run, keep 10% buffer)
- Move to device → compute → move back: `torch.tensor(data, device=device)` → `.cpu().numpy()`
- OOM fallback: catch `torch.cuda.OutOfMemoryError` → `empty_cache()` → halve batch size → retry on GPU. Keep reducing until it fits. Stay on GPU.
- Batch large data: chunk it, `del batch` between iterations to free VRAM

## Parallelism Rules

- **CPU-bound**: `ProcessPoolExecutor` + `as_completed`, pre-allocate result list indexed by submission order
- **I/O-bound**: `asyncio` + `aiohttp`, `Semaphore(NUM_WORKERS * 4)`, single shared `ClientSession`, `asyncio.gather(*tasks, return_exceptions=True)`
- Always add `tenacity` retries for transient failures, always set timeouts on HTTP requests
- **CRITICAL — `ProcessPoolExecutor` start method**: Default `fork` deadlocks with loguru (and any threading library). ALWAYS pass `mp_context=multiprocessing.get_context("spawn")` when constructing `ProcessPoolExecutor` in any script that uses loguru, threading, or async I/O. Example:
  ```python
  import multiprocessing as mp
  from concurrent.futures import ProcessPoolExecutor
  with ProcessPoolExecutor(max_workers=N, mp_context=mp.get_context("spawn")) as pool:
      ...
  ```
````

### [9] SYSTEM-USER prompt · 2026-08-20 21:09:33 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 1800s message timeout. Each individual operation must complete within 1800s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 1800s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_response]: 

Now let me also fix the `compute_survival_label` function which uses `pd.to_datetime` without `utc=True`:


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "    # Find departure index\n    dep_idx = None\n    for i, m in enumerate(all_months):\n        i
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_think]: Now let me re-run the fixed script. The main issues were:
1. `pd.to_datetime` without `utc=True` causing mixed timezone issues
2. `pd.DateOffset(months=3)` causing tz-aware/tz-naive comparison issues
3. The `compute_static_features` function had tz comparison issues

Let me restart the process.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "kill 8821 2>/dev/null; sleep 1; cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && source .venv/bin/activate && timeout 3600 uv run method.py > logs/run_stdout.log 2>&1 & PID=$! && echo \"PID: $PID\"",
  "is_input": f
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "[1] 9823\nPID: 9823"}], "is_error": false, "command": "kill 8821 2>/dev/null; sleep 1; cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && source .venv/bin/activate
  - [agent_think]: The user sent an empty command. This typically means they want me to check on the running process. Let me check the status of the background process and the logs.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "kill -0 9823 2>/dev/null && echo \"Running\" || echo \"Ended\"; tail -100 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_stdout.log",
  "is_input": false,
  "timeout": 10.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Running"}], "is_error": false, "command": "kill -0 9823 2>/dev/null && echo \"Running\" || echo \"Ended\"; tail -100 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/l
  - [agent_think]: The stdout log seems empty. Let me wait longer and check again.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 90 && tail -120 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_stdout.log",
  "is_input": false,
  "timeout": 120.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "21:00:27|INFO   |============================================================\n21:00:27|INFO   |FOUNDER FADE CURVE PREDICTS OSS SURVIVAL - PILOT EXPERIMENT\n21:00:27|INFO   |=========================================
  - [agent_think]: 


  - [agent_response]: 

Good progress! nodejs/node succeeded (106992 commits, survival=1 matching expected=1). It's processing Homebrew now. Let me wait more:


  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 120 && tail -150 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_stdout.log",
  "is_input": false,
  "timeout": 150.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "21:00:27|INFO   |============================================================\n21:00:27|INFO   |FOUNDER FADE CURVE PREDICTS OSS SURVIVAL - PILOT EXPERIMENT\n21:00:27|INFO   |=========================================
  - [agent_think]: Excellent! The pipeline is working well now:
- nodejs/node: SUCCESS (106992 commits, survival=1, expected=1)
- Homebrew/brew: SUCCESS (52018 commits, survival=1, expected=1)
- twbs/bootstrap: SUCCESS (26211 commits, survival=1, expected=1)
- redis/redis: processing...

This is taking about 60-70 sec
  - [agent_response]: 

Excellent! 3/15 projects succeeded with correct labels. Let me wait for the full run to complete:


  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 300 && tail -200 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_stdout.log",
  "is_input": false,
  "timeout": 330.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "21:00:27|INFO   |============================================================\n21:00:27|INFO   |FOUNDER FADE CURVE PREDICTS OSS SURVIVAL - PILOT EXPERIMENT\n21:00:27|INFO   |=========================================

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>

What determines whether an open-source project survives its founder stepping away?
```

### [10] SYSTEM-USER prompt · 2026-08-20 22:25:58 UTC

```
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [11] HUMAN-USER prompt · 2026-08-20 22:25:58 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [12] SYSTEM-USER prompt · 2026-08-20 22:57:40 UTC

```
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 1800s message timeout. Each individual operation must complete within 1800s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 1800s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "444:    safe_args = [\"git\", \"-c\", \"safe.directory=*\"] + args\n477:            [\"git\", \"-C\", repo_path, \"config\", \"--local\", \"safe.directory\", repo_path],\n487:            [\"git\", \"-C\", repo_path,
  - [agent_response]: 

I need to replace all remaining `subprocess.run(["git", "-C", ...])` calls with `_git_cmd(["-C", ...])`.


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": [
    483,
    545
  ]
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py:\n   483\tdef parse_git_log(repo_path: str) -> pd.DataFrame:\n  
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "def parse_git_log(repo_path: str) -> pd.DataFrame:\n    \"\"\"Parse git log into DataFrame with c
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "def parse_git_merges(repo_path: str) -> pd.DataFrame:\n    \"\"\"Parse merge commits to get merge
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "view",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": [
    830,
    870
  ]
}
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Here's the result of running `cat -n` on /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py:\n   830\t\n   831\t    # File count (approximate from git ls-tr
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "    # File count (approximate from git ls-tree)\n    try:\n        result = subprocess.run(\n    
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && python -c \"import ast; ast.parse(open('method.py').read()); print('Syntax OK')\" 2>&1",
  "is_input": false,
  "timeout": 10.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Syntax OK"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && python -c \"import ast; ast.parse(open('method.py').read()); print(
  - [agent_think]: The user is asking me to continue working on the task. Let me check the current state and run the experiment again with the fixed git commands.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v5_stdout.log 2>&1 & echo \"PID=$!\"",
  "is_input": false,
  "timeout": 10.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "[1] 2416\nPID=2416"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v5_stdout.
  - [agent_think]: The experiment is running in the background. Let me wait for it to complete and check the results.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 300 && tail -80 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_v5_stdout.log 2>/dev/null | head -80",
  "is_input": false,
  "timeout": 330.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "22:53:30|WARNING|  compute_all_descriptors(unknown): Theil-Sen failed: theilslopes() got an unexpected keyword argument 'per'\n22:53:30|INFO   |  compute_all_descriptors(unknown): OLS fallback: slope=-0.035174, r2=0

CONTINUE FOLLOWING THESE INSTRUCTIONS:

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>

What determines whether an open-source project survives its founder stepping away?
```

### [13] SYSTEM-USER prompt · 2026-08-20 23:27:44 UTC

```
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_think]: The experiment ran successfully with good results. Now I need to:
1. Fix the `per` parameter issue in Theil-Sen (scipy version incompatibility) - use `per` → `percentile`
2. Re-run the experiment with the CoxPH fix
3. Validate the output JSON

Let me fix the Theil-Sen parameter name issue first, the
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "        else:\n            ts = theilslopes(y, x, per=95.0)",
  "new_str": "        else:\n      
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_think]: Let me run the experiment again with the fixed Theil-Sen call and CoxPH error handling.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v6_stdout.log 2>&1 & echo \"PID=$!\"",
  "is_input": false,
  "timeout": 10.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "[1] 9468\nPID=9468"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v6_stdout.
  - [agent_think]: Let me wait for the experiment to complete and check the results.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 300 && tail -30 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_v6_stdout.log 2>/dev/null | tail -30",
  "is_input": false,
  "timeout": 330.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "23:16:26|INFO   |  compute_all_descriptors(nodejs/node founder): OLS fallback: slope=-0.039398, r2=0.8770\n23:16:47|WARNING|  compute_all_descriptors(nodejs/node non-founder): Theil-Sen failed: theilslopes() got an 
  - [agent_think]: Theil-Sen still failing with both `per` and `percentile` parameter names. The scipy version installed doesn't support either. Let me check the scipy version and just use OLS directly since the fallback is working fine.

  - [agent_response]: 

The `theilslopes` API differs across scipy versions. Let me just use OLS directly since the fallback works perfectly.


  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py",
  "file_text": null,
  "old_str": "    # (a) LINEAR SLOPE via Theil-Sen\n    slope = 0.0\n    r2_linear = 0.0\n    try:\n        # C
  - [agent_tool_result] file_editor: Tool: file_editor
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "The file /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/method.py has been edited. Here's the result of running `cat -n` on a snippet of /ai-inventor/aii_data/run
  - [agent_think]: </thinking>

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v7_stdout.log 2>&1 & echo \"PID=$!\"",
  "is_input": false,
  "timeout": 10.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "[2] 11055\nPID=11055"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1 && timeout 3600 uv run python method.py > logs/run_v7_stdou
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 300 && tail -30 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_v7_stdout.log 2>/dev/null | tail -30",
  "is_input": false,
  "timeout": 330.0,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "23:23:08|INFO   |  twbs/bootstrap: already cloned at /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/clones/twbs_bootstrap\n/ai-inventor/aii_data/runs/run_dX5VwxrQ9qy
  - [agent_think]: Good, the OLS fallback is working now without warnings. Let me wait for the experiment to complete.

  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 300 && tail -40 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/logs/run_v7_stdout.log 2>/dev/null | tail -40",
  "is_input": false,
  "timeout": 330.0,
  "reset": false
}

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-python, aii-long-running-tasks, aii-json, aii-file-size-limit, aii-use-hardware, aii-parallel-computing.
TODO 2. Read preview files from dependencies to understand data structure. Use ALL datasets provided — do not skip or select a subset. Read domain handbook if applicable (see <available_domain_handbooks>). Test basic functionality with 'uv run'.
TODO 3. Fully implement our method AND baseline (comparison) as described in artifact plan in './method.py'. Use exp_gen_sol_out.json schema in aii-json skill for output format validation. Include everything specified in the artifact plan, but you may also implement additional relevant methods or analysis beyond what's listed. Be very attentive to meticulously and exhaustively fix any errors in your code.
</todos>
```

### [14] HUMAN-USER prompt · 2026-08-20 23:27:44 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [15] SYSTEM-USER prompt · 2026-08-20 23:33:13 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx3
type: experiment
title: Founder Fade Curve Predicts OSS Survival Pilot
summary: >-
  Implement the complete trajectory shape-descriptor pipeline (Theil-Sen slope, convexity, change-point detection, cliff indicator,
  composite fade index) on a self-sourced pilot cohort of 12-15 curated GitHub repos with documented founder departures. Run
  leave-one-out logistic regression comparing static vs trajectory-shape vs combined features for predicting post-departure
  survival, validate on synthetic trajectories, and run a falsification control using non-founder fade curves.
runpod_compute_profile: cpu_light
implementation_pseudocode: >-
  See gen_plan.py (in same directory) for the full executable generator script with complete pseudocode. Summary of 8 phases:
  PHASE 0 - Synthetic validation: generate 10 smooth-fade, 10 abrupt-cliff, 10 plateau-then-cliff synthetic trajectories using
  numpy (exp decay, step functions, plateau+ramp). Run compute_all_descriptors() on each. Assert smooth fades get fade_index>0.6
  and cliff_indicator<2.0; abrupt cliffs get fade_index<0.4 and cliff_indicator>3.0. PHASE 1 - Project curation and cloning:
  curate 12-15 GitHub repos with confirmed founder departures (6 survived: nodejs/node, Homebrew/brew, twbs/bootstrap, redis/redis,
  ipython/ipython, electron/electron; 6 collapsed: ariya/phantomjs, bower/bower, request/request, gruntjs/grunt, component/component,
  sindresorhus/ava; alternates: lodash/lodash, yarnpkg/yarn, pugjs/pug, gulpjs/gulp). Clone with git clone --filter=blob:none
  --no-checkout for speed. Parse git log: git -C dir log --all --format=%H|%an|%ae|%aI --date=iso-strict. Identify founder
  as user with earliest sustained commit (>=5 commits in first 3 months), cross-check with GET /repos API owner.login. Departure
  = first month after which founder has zero commits for 12 consecutive months. Compute monthly shares: founder_share = founder_count
  / total_count per month; handle gaps by carrying forward last value. PHASE 2 - GitHub API for PR merges and reviews: set
  GITHUB_TOKEN env var for 5000 req/hr rate limit. Use GraphQL query with pagination (pullRequests first:100, after cursor)
  to get mergedBy.login (merger) and reviews.author.login (reviewer) per PR. Compute monthly merge_share and review_share.
  Composite involvement = weighted 0.4*commit + 0.3*merge + 0.3*review. Fallback without API token: use git merge commit committer
  email (ce) as merger via git log --all --merges --format=%ae|%aI|%cN|%ce; reviews unavailable, drop component. PHASE 3 -
  Trajectory shape descriptors on pre-departure shares array: (a) Linear slope via scipy.stats.theilslopes(y, x) with R2 for
  smoothness; (b) Convexity via np.polyfit(x, y, 2) coefficient sign; (c) Time-to-onset-of-decline via ruptures Pelt(model=l2).fit(y).predict(pen=penalty),
  first breakpoint; (d) Abrupt-cliff indicator = max(abs(diff(y))) / (2*std(y)+epsilon), terminal cliff if cliff_month >=
  n-3; (e) Plateau-then-cliff indicator via Chow-style test: pre-breakpoint slope≈0 AND pre-mean>0.5 AND post-breakpoint slope<-0.02;
  (f) Composite fade_index = 0.3*norm(slope_smoothness_R2) + 0.3*norm(decline_duration_fraction) + 0.4*norm(1 - normalized_cliff_magnitude),
  min-max normalized across sample to [0,1]. PHASE 4 - Static baseline features at departure snapshot: project_age_months,
  contributor_count, total_commits, file_count (git ls-tree -r --name-only), stars (GitHub API stargazers_count, caveat: current
  not historical), bus_factor (greedily add devs by commit count until 50% file coverage reached). PHASE 5 - Survival labeling:
  binary label = 1 if post-departure non-founder monthly activity >= 0.3*pre-departure 12-month baseline, else 0; continuous
  metric = post_avg/pre_baseline ratio. Also check Avelino criterion: new key dev with >=10% of post-departure commits. PHASE
  6 - Predictive models: assemble X_static = [age, contributors, stars, files, bus_factor], X_shape = [slope, r2_linear, quadratic_coef,
  norm_slope, cliff_indicator, decline_duration_fraction, plateau_then_cliff, fade_index], X_combined = concatenation. StandardScaler
  normalize. LogisticRegression(penalty=l2, C=1.0, class_weight=balanced). LeaveOneOut CV with held-out proba predictions.
  roc_auc_score for AUC. permutation_test_score(n_permutations=500, scoring=roc_auc). lifelines CoxPHFitter as secondary model
  (concordance_index, hazard_ratios). Report coefficient signs and permutation feature importance. PHASE 7 - Falsification
  control: for each project find most active non-founder contributor, compute their monthly share trajectory + all descriptors,
  train same models, compare founder_AUC vs non_founder_AUC. If hypothesis correct: founder_AUC > non_founder_AUC (founder-specific
  mechanism). PHASE 8 - Output method_out.json: synthetic_validation (assertions, means per pattern), project_table (per-project
  descriptors, labels, features), model_comparison (static_only/shape_only/combined AUC+p-values+coefs, coxph concordance+ratios),
  falsification_control (AUCs, delta, founder_specific bool), feature_importance, notes (sample_size, data_sources, caveats).
fallback_plan: >-
  FALLBACK PLAN activated if primary approach encounters problems: (1) GITHUB API RATE LIMITING or PR DATA UNAVAILABLE: If
  no GITHUB_TOKEN available, use git merge commits as fallback for merge data via git log --all --merges --format=%ae|%aI|%cN|%ce
  (committer email of a merge commit = person who merged it). Reviews are UNAVAILABLE without API, drop that component. Composite
  = weighted 0.4*commit + 0.3*merge, note limitation in method_out.json. (2) FOUNDER IDENTIFICATION AMBIGUITY: If multiple
  candidates, use repo creator from GitHub API GET /repos owner.login cross-referenced with earliest sustained committer.
  If founder never fully departed, lower inactivity threshold from 12 to 6 months, or define departure as 80% reduction from
  peak monthly activity. Report all adaptations. (3) SURVIVAL LABELING AMBIGUITY: Switch to continuous metric (post-departure/pre-departure
  activity ratio) as primary outcome, use linear regression with LOOCV R-squared. Test multiple thresholds (0.1, 0.3, 0.5)
  for robustness checks. (4) SMALL SAMPLE or MODEL CONVERGENCE: Increase regularization (C=0.1) or use RidgeClassifier. Use
  leave-two-out or 5-fold stratified CV if LOO is degenerate. Report bootstrap CIs (1000 resamples) as alternative to permutation
  test. With 12-15 projects, report AUC and effect DIRECTION only, do NOT over-claim statistical significance. This pilot
  provides directional evidence for iteration 2 scale-up. (5) CANNOT CLONE LARGE REPOS: Use --filter=blob:none --no-checkout
  (already planned). Use GitHub REST /commits endpoint with pagination (5000/hr with token) as alternative to cloning. Truncate
  analysis to last 5 years before departure for extremely large repos. (6) ruptures LIBRARY NOT AVAILABLE: Use scipy.signal.find_peaks
  on negative first derivative, or implement sliding-window F-statistic (for each candidate split, compute F comparing pre/post
  segment means, pick max F split). (7) lifelines NOT AVAILABLE: Drop CoxPH entirely, rely on logistic + linear regression
  only. (8) INSUFFICIENT PROJECTS IDENTIFIED: Lower bar to 8 projects (4 survived, 4 collapsed). Use aii-web-tools skill to
  search for more documented founder departures. Scan for archived GitHub repositories with known founder history.
testing_plan: >-
  TESTING PLAN - validate pipeline in 8 staged gates from fastest to slowest: STAGE 1 - Synthetic Validation (no external
  deps, run FIRST): Generate 10 smooth-fade (exp decay lambda=0.08), 10 abrupt-cliff (step at month 18), 10 plateau-then-cliff
  (plateau to month 16 then ramp) synthetic trajectories. Run compute_all_descriptors() on each. ASSERTIONS - Smooth fade:
  mean fade_index>0.6, cliff_indicator<2.0, decline_duration_fraction>0.5. Abrupt cliff: mean fade_index<0.4, cliff_indicator>3.0,
  cliff_is_terminal=True. Plateau-then-cliff: plateau_then_cliff>0.5, pre_breakpoint_slope≈0. If assertions fail, debug and
  tune ruptures penalty / cliff threshold / fade_index weights BEFORE touching real data. PASS: all 3 patterns clearly separated
  by fade_index. STAGE 2 - Single-Project Git Extraction: Clone ONE small archived repo (e.g., ariya/phantomjs or component/component)
  with blobless clone. Parse git log, compute monthly founder shares. Identify founder via earliest-sustained-commit method.
  Detect departure (12-month zero-commit gap). Visually plot shares over time for plausibility. PASS: pipeline runs end-to-end
  on one repo, produces plausible values. STAGE 3 - Single-Project GitHub API: Fetch PR data for pilot repo via GraphQL (or
  REST fallback). Verify PR count matches expectation, mergedBy fields populated. Aggregate monthly merge shares, compare
  with commit shares. PASS: API call succeeds, data non-empty, monthly shares plausible. STAGE 4 - Survival Labeling Check:
  Determine survival label for pilot repo. Cross-check against expected label from curated project list. If mismatch, debug
  labeling function and adjust thresholds. PASS: label matches expectation for pilot repo. STAGE 5 - Full Cohort Extraction
  (scale up): Once stages 1-4 pass, run full pipeline on ALL 12-15 projects. Monitor clone times (should be <5 min each with
  blobless clone), log API rate limits (remaining requests), extraction completion. After each project, log descriptors computed,
  label determined, any warnings. PASS: all projects extracted successfully or documented failures with reasons. STAGE 6 -
  Model Fitting and Validation: Assemble feature matrices, check for missing values (impute or drop). Check class balance
  - if e.g. 11 survived / 1 collapsed, adjust project selection to balance (aim 6/6 or 7/5). Fit logistic regression with
  LOOCV, report AUC and coefficient signs. Run permutation test (n_permutations=500). Compare shape_only AUC vs static_only
  AUC. PASS: models run without error, produce numeric output. DIRECTIONAL CHECK: does fade_index have positive coefficient
  with survival (if hypothesis supported) or null/negative (if not)? STAGE 7 - Falsification Control: Run most-active-non-founder
  analysis for each project. Compare AUCs: founder_AUC vs non_founder_AUC. PASS: control runs without error, comparison is
  reportable. STAGE 8 - Final Validation: Run CoxPH if lifelines available, check concordance index. Verify method_out.json
  is complete with all sub-results. Review all numbers for plausibility, check for NaN/Inf in descriptors. PASS: method_out.json
  is complete and correct. GRADUAL SCALING: Each stage gates the next. Fix problems at each stage before proceeding. TIME
  BUDGET: Stages 1-4 should complete in <30 min. Stage 5 (full cohort cloning) may take 1-2 hours. Stages 6-8 in <30 min.
  Total estimated 2-3 hours, leaving buffer for debugging within the 6h limit.
</artifact_plan>



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

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for framework choices, implementation patterns, agent orchestration.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

IMPORTANT: Your final response should be at most 300 characters long.

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Use aii-json skill's format script with `--input method_out.json` to generate full, mini, and preview versions. If not in your workspace (see <workspace> above), copy them there. Run 'ls -lh' to verify these three files exist (DO NOT read them).
TODO 2. Apply aii-file-size-limit skill's file size check procedure (100MB limit) to method_out.json and full_method_out.json.
TODO 3. Ensure a `pyproject.toml` exists in your workspace with ALL dependencies pinned to the exact versions installed in your .venv (run `.venv/bin/pip freeze` to get them). This is required for reproducibility. The [project] section must include name, version, requires-python, and a dependencies list with pinned versions (e.g. `numpy==2.0.2`, not `numpy>=2.0`).
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ExperimentExpectedFiles": {
      "description": "All expected output files from experiment artifact.",
      "properties": {
        "script": {
          "description": "Path to method.py script. Example: 'method.py'",
          "title": "Script",
          "type": "string"
        },
        "full_output": {
          "description": "Full method output JSON file. Example: 'full_method_out.json'",
          "title": "Full Output",
          "type": "string"
        },
        "mini_output": {
          "description": "Mini method output JSON file. Example: 'mini_method_out.json'",
          "title": "Mini Output",
          "type": "string"
        },
        "preview_output": {
          "description": "Preview method output JSON file. Example: 'preview_method_out.json'",
          "title": "Preview Output",
          "type": "string"
        }
      },
      "required": [
        "script",
        "full_output",
        "mini_output",
        "preview_output"
      ],
      "title": "ExperimentExpectedFiles",
      "type": "object"
    }
  },
  "description": "Experiment artifact \u2014 structured output + file metadata.\n\nImplements research methodology with baseline comparison.\nProduces method.py and method_out.json files.",
  "properties": {
    "title": {
      "default": "",
      "description": "Artifact title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); describe the content, not a status.",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "layman_summary": {
      "default": "",
      "description": "One-sentence plain-language summary of what this artifact does, accessible to non-experts. Used only in the per-artifact README, not in downstream prompts.",
      "maxLength": 250,
      "minLength": 80,
      "title": "Layman Summary",
      "type": "string"
    },
    "summary": {
      "default": "",
      "description": "Summary for downstream artifacts: what this artifact provides",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/ExperimentExpectedFiles",
      "description": "All output files you created. Must include method.py script plus full/mini/preview method output JSON files."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files"
  ],
  "title": "ExperimentArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [16] SYSTEM-USER prompt · 2026-08-20 23:34:38 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 1/10).
</verification_failed>

<file_errors>
MISSING OR UNREADABLE FILES:
  - Missing file: full_method_out.json

Fix: Create the missing files directly in your workspace (see <workspace> above for the exact path).
     Required files: method.py, method_out.json, full_method_out.json, mini_method_out.json, preview_method_out.json
     Use 'ls' to check what files exist.
</file_errors>

<schema_errors>
JSON SCHEMA / CODE VALIDATION ERRORS:
  - mini_method_out.json: Missing required 'datasets' key
  - preview_method_out.json: Missing required 'datasets' key

Fix: Your JSON files must follow the datasets-grouped exp_gen_sol_out.json schema:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "predict_<method_name>": "string - prediction per method"
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields.
     Read exp_gen_sol_out.json schema in aii-json skill.
     Then update method.py and regenerate the output files.

     If Python syntax errors: fix the syntax in method.py
</schema_errors>

<task>
FIX THESE ISSUES:
1. Create all missing files by running method.py
2. Fix schema/syntax errors in method.py
3. Re-run method.py to regenerate output files
4. Validate with aii-json skill: validate method_out.json against exp_gen_sol_out schema

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [17] SYSTEM-USER prompt · 2026-08-20 23:39:02 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 2/10).
</verification_failed>

<schema_errors>
JSON SCHEMA / CODE VALIDATION ERRORS:
  - full_method_out.json: Missing required 'datasets' key
  - mini_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)
  - preview_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)

Fix: Your JSON files must follow the datasets-grouped exp_gen_sol_out.json schema:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "predict_<method_name>": "string - prediction per method"
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields.
     Read exp_gen_sol_out.json schema in aii-json skill.
     Then update method.py and regenerate the output files.

     If Python syntax errors: fix the syntax in method.py
</schema_errors>

<task>
FIX THESE ISSUES:
2. Fix schema/syntax errors in method.py
3. Re-run method.py to regenerate output files
4. Validate with aii-json skill: validate method_out.json against exp_gen_sol_out schema

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```

### [18] SYSTEM-USER prompt · 2026-08-20 23:59:47 UTC

```
<verification_failed>
Your experiment output failed verification (attempt 3/10).
</verification_failed>

<schema_errors>
JSON SCHEMA / CODE VALIDATION ERRORS:
  - full_method_out.json: Missing required 'datasets' key
  - mini_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)
  - preview_method_out.json: No predict_* fields found in any of the sampled examples (at least one required)

Fix: Your JSON files must follow the datasets-grouped exp_gen_sol_out.json schema:
     {
       "datasets": [
         {
           "dataset": "dataset_name",
           "examples": [
             {
               "input": "string (required)",
               "output": "string (required)",
               "metadata_fold": 2,
               "predict_<method_name>": "string - prediction per method"
             }
           ]
         }
       ]
     }

     NO 'split', 'dataset', or 'context' per-example. Dataset name at group level.
     Metadata via flat metadata_<name> fields.
     Read exp_gen_sol_out.json schema in aii-json skill.
     Then update method.py and regenerate the output files.

     If Python syntax errors: fix the syntax in method.py
</schema_errors>

<task>
FIX THESE ISSUES:
2. Fix schema/syntax errors in method.py
3. Re-run method.py to regenerate output files
4. Validate with aii-json skill: validate method_out.json against exp_gen_sol_out schema

After making changes, verify:
- 'ls -la' shows all required files
- 'uv run method.py' completes successfully
- JSON files are valid (use aii-json skill validation)
- full_method_out.json has at least 50 examples
</task>
```
