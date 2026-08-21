# gen_art_experiment_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Do Not Predict Open-Source Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_experiment_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 18:36:40 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Founder Fade Curves Predict OSS Survival
summary: >-
  Test whether founder involvement fade curve descriptors provide complementary predictive value beyond static features in
  predicting OSS project survival after founder departure, using the ESEM2019 dataset.
runpod_compute_profile: cpu_light
implementation_pseudocode: |-
  ## EXPERIMENT PLAN: Founder Fade Curve Descriptors for OSS Survival Prediction

  ### OVERVIEW
  This experiment tests whether the SHAPE of a founder's involvement trajectory (fade curve) provides complementary predictive value beyond static project metrics in predicting whether an open-source project survives after the founder departs. We use the ESEM2019 dataset (Avelino et al., 315 GitHub projects) with pre-computed monthly founder involvement shares and survival labels.

  ### DATA SOURCE
  - Primary: full_data_out.json from dataset artifact (art_zNvSqNQvIA2R) at:
    /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json
  - Raw ESEM2019 CSVs available at:
    /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/esem2019/data/
    (tfprojects_commits_new.csv, leavers.csv, tfdevelopers.csv, projectinfo.csv, measures.csv)

  ### STEP 0: Environment Setup
  ```
  uv venv .venv --python=3.12
  source .venv/bin/activate
  uv pip install pandas numpy scikit-learn scipy loguru matplotlib seaborn lifelines
  ```

  ### STEP 1: Data Loading and Project Reconstruction
  1. Load full_data_out.json
  2. Group examples by project_id to reconstruct per-project time series
  3. For each project, extract:
     - Pre-departure monthly time series: founder_commit_share, founder_merge_share, founder_review_share
     - Static features at departure: stars, forks, contributor_count, file_count, bus_factor, repo_age_days
     - Survival label (binary: survived vs collapsed)
  4. Compute combined founder share per month: mean(commit_share, merge_share, review_share)
  5. Attempt to enrich with raw ESEM2019 commit data:
     - Load tfprojects_commits_new.csv to get per-developer commit counts per month
     - If founder-level granularity exists, replace synthetic shares with real ratios
     - If not, proceed with synthetic shares but document limitation
  6. Filter to projects with >= 6 months of pre-departure data (need sufficient trajectory for curve fitting)
  7. Verify label balance (expect ~50/50 survived/collapsed)

  ### STEP 2: Fade Curve Descriptor Computation
  For each project's pre-departure time series (t=0 to t=T, where T = months to departure):

  Let y[t] = combined founder share at month t.

  **Descriptor 1: Linear Slope (S_slope)**
  - Fit y[t] = a + b*t via OLS
  - S_slope = b (negative = declining, positive = increasing)
  - Normalized by dividing by initial share: S_slope_norm = b / y[0]

  **Descriptor 2: Convexity (S_convex)**
  - Fit quadratic: y[t] = a + b*t + c*t^2
  - S_convex = c (positive = convex/accelerating decline, negative = concave/decelerating)
  - Normalized: S_convex_norm = c / y[0]

  **Descriptor 3: Decline Onset Time (S_decline_start)**
  - Compute first derivative: dy/dt = gradient(y)
  - Find first index where dy/dt < -threshold (threshold = 0.01 share/month)
  - S_decline_start = index / T (normalized to [0,1], where 0 = immediate decline, 1 = never declined)

  **Descriptor 4: Cliff Score (S_cliff)**
  - Compare final 2-month average to prior 6-month average
  - S_cliff = (avg[y[T-6:T-2]] - avg[y[T-2:T]]) / avg[y[T-6:T-2]]
  - Clipped to [0, 1]. High = abrupt cliff, low = smooth ending

  **Descriptor 5: Plateau-then-Cliff Indicator (S_plateau)**
  - If decline_start > 0.5 (decline started in second half) AND variance of pre-decline period < 0.5 * total variance:
    S_plateau = 1 (plateau-then-cliff pattern)
  - Else S_plateau = 0

  **Descriptor 6: Composite Fade Index (S_fade_idx)**
  - S_fade_idx = 1.0 - S_cliff + (0.3 if S_slope < 0 else 0) - (0.2 if S_plateau else 0)
  - Clipped to [0, 1]
  - Interpretation: 1.0 = perfect smooth fade, 0.0 = abrupt cliff

  ### STEP 3: Feature Engineering
  **Static Features (at departure):**
  - bus_factor_at_departure
  - contributor_count_at_departure
  - stars_at_departure (log-transformed)
  - file_count_at_departure (log-transformed)
  - repo_age_days_at_departure (converted to years)
  - commits_before_departure (log-transformed)
  - commits_after_departure (log-transformed)

  **Fade Features:**
  - S_slope_norm, S_convex_norm, S_decline_start, S_cliff, S_plateau, S_fade_idx

  **Interaction Features (for combined model):**
  - S_fade_idx * contributor_count (does fade matter more with more contributors?)
  - S_cliff * bus_factor (does cliff matter more with low bus factor?)

  ### STEP 4: Model Training and Evaluation

  **Model A: Static-Only Baseline**
  - Logistic Regression (L2 penalty, C=1.0, class_weight='balanced')
  - Features: static features only
  - Cross-validation: Stratified 5-fold (use metadata_fold from dataset)

  **Model B: Fade-Only**
  - Logistic Regression (same hyperparameters)
  - Features: fade descriptors only
  - Cross-validation: Stratified 5-fold

  **Model C: Combined**
  - Logistic Regression (same hyperparameters)
  - Features: static + fade + interaction features
  - Cross-validation: Stratified 5-fold

  **Model D: Regularization Comparison**
  - Ridge Regression for continuous target (post-departure activity)
  - Random Forest (n_estimators=100, max_depth=5) for binary classification
  - Compare with logistic regression to check for non-linear effects

  **Metrics:**
  - Primary: AUC-ROC (mean and std across folds)
  - Secondary: Log-loss, Accuracy, F1-score
  - Continuous: R-squared (for post-departure activity prediction)
  - Statistical: McNemar's test comparing Model A vs Model C predictions

  ### STEP 5: Feature Importance Analysis
  1. **Permutation Feature Importance** (n_repeats=30, random_state=42)
     - Run on Model C (combined) with 5-fold CV
     - Report mean importance and std for each feature
     - Compare fade feature importance vs static feature importance

  2. **Coefficient Analysis**
     - Extract logistic regression coefficients
     - Report standardized coefficients (coefficient * feature_std)
     - Check directionality: does higher fade_idx correlate with survival?

  3. **Univariate Analysis**
     - For each fade descriptor: compute point-biserial correlation with survival
     - Report p-values
     - Create boxplots (survived vs collapsed) for each descriptor

  ### STEP 6: Directionality Analysis
  1. **Fade Index vs Survival**
     - Compute mean fade_idx for survived vs collapsed projects
     - Two-sample t-test (or Mann-Whitney U if non-normal)
     - Report effect size (Cohen's d)

  2. **Cliff Score vs Survival**
     - Same analysis for cliff_score
     - Expect: collapsed projects have higher cliff scores

  3. **Slope vs Survival**
     - Expect: survived projects have more negative slopes (gradual decline)

  4. **Visualize**
     - Kernel density plots of fade_idx for survived vs collapsed
     - Scatter plot: fade_idx vs post-departure activity
     - Heatmap: correlation matrix of all features with survival

  ### STEP 7: Falsification Control (Founder-Specificity Test)
  **Purpose:** Verify that the fade curve's predictive power is founder-specific, not just a property of any high-activity contributor.

  1. For each project, identify the second-most-active contributor (not the founder)
  2. Generate synthetic "non-founder" involvement trajectories:
     - Use the same time series length as the founder
     - Randomize the shape: shuffle the founder's monthly shares, or generate random trajectories with the same mean and variance
  3. Compute the same 6 fade descriptors for these synthetic non-founder trajectories
  4. Train Model B' (Fade-Only) using non-founder descriptors
  5. Compare AUC: founder_fade_auc vs non_founder_fade_auc
  6. Expectation: founder_fade_auc > non_founder_fade_auc by a significant margin (>0.1)

  ### STEP 8: Sensitivity Analysis
  1. **Vary departure threshold:** Re-run with 6-month and 18-month inactivity windows (if data allows)
  2. **Vary trajectory length:** Re-run using only the last 12 months of pre-departure data vs full trajectory
  3. **Vary descriptor thresholds:** Test cliff_score with different window sizes (final 3 months vs final 2 months)
  4. **Subsample analysis:** Run on top-50 most-starred projects vs bottom-50 least-starred

  ### STEP 9: Output Generation
  Generate method_out.json with:
  ```
  {
    "metadata": {
      "method_name": "founder_fade_curves_experiment_iter2",
      "n_projects": <count>,
      "n_survived": <count>,
      "n_collapsed": <count>,
      "cv_folds": 5,
      "metrics": {
        "model_a_auc": <float>, "model_a_auc_std": <float>,
        "model_b_auc": <float>, "model_b_auc_std": <float>,
        "model_c_auc": <float>, "model_c_auc_std": <float>,
        "model_d_rf_auc": <float>,
        "model_a_logloss": <float>,
        "model_b_logloss": <float>,
        "model_c_logloss": <float>,
        "directionality_t_test_p": <float>,
        "directionality_cohens_d": <float>,
        "falsification_auc_diff": <float>
      },
      "feature_importance": {
        "fade_descriptors": { ... },
        "static_descriptors": { ... },
        "interaction_features": { ... }
      },
      "directionality": "<text summary>",
      "falsification_result": "<text summary>",
      "sensitivity_analysis": { ... }
    },
    "datasets": [
      {
        "dataset": "oss_founder_fade_survival_iter2",
        "examples": [
          {
            "input": "<json with project_id, static_features, fade_descriptors>",
            "output": "<json with survival label, post_departure_activity>",
            "metadata_fold": <int>,
            "metadata_feature_names": "<comma-separated>",
            "predict_static": "<survive/collapse>",
            "predict_fade": "<survive/collapse>",
            "predict_combined": "<survive/collapse>",
            "predict_static_prob": "<float>",
            "predict_fade_prob": "<float>",
            "predict_combined_prob": "<float>"
          }
        ]
      }
    ]
  }
  ```

  ### STEP 10: Visualization (save to results/ directory)
  1. results/fade_idx_distribution.png - KDE plot of fade_idx for survived vs collapsed
  2. results/feature_importance.png - Bar chart of permutation importance
  3. results/roc_curves.png - ROC curves for Models A, B, C
  4. results/correlation_heatmap.png - Feature correlation matrix
  5. results/cliff_vs_survival.png - Boxplot of cliff_score by survival

  ### GRADUAL SCALING
  1. **Mini (3 projects):** Load mini_data_out.json, run full pipeline, verify output schema
  2. **10 projects:** Load first 10 from full_data_out.json, verify descriptors compute correctly
  3. **50 projects:** Full pipeline, record runtime, extrapolate
  4. **All projects (~315):** Full pipeline with all analysis
  5. **Final validation:** Re-run on full data, verify reproducibility

  ### ERROR HANDLING
  - If raw ESEM2019 commit data cannot be parsed: proceed with synthetic shares, log warning
  - If < 6 months of data for a project: skip that project, log count
  - If logistic regression fails to converge: increase max_iter to 5000
  - If class imbalance > 70/30: use SMOTE oversampling (imbalanced-learn)
  - If permutation importance takes too long: reduce n_repeats to 10

  ### EXPECTED OUTCOMES
  **Supporting evidence:**
  - Model C (combined) AUC > Model A (static-only) AUC by >= 0.05
  - Fade descriptors rank in top-3 feature importances
  - Higher fade_idx associated with survival (p < 0.05)
  - Founder fade AUC > non-founder fade AUC by >= 0.1

  **Disconfirming evidence:**
  - Fade descriptors add no predictive value (Model C AUC ≈ Model A AUC)
  - Directional effect reverses or is null
  - Non-founder fade curves predict equally well
fallback_plan: |-
  IF the primary approach fails at any stage, execute these fallbacks in order:

  **Fallback 1: Synthetic Data Limitation**
  - If raw ESEM2019 commit data cannot provide founder-level granularity (likely), proceed with the synthetic founder shares from full_data_out.json
  - Mitigate by: (a) generating multiple synthetic trajectory variations per project with different random seeds to create diversity, (b) adding noise to synthetic shares to simulate real-world variation, (c) explicitly documenting this as a limitation in the output
  - Generate 3 trajectory variants per project: (1) smooth linear decline, (2) plateau-then-cliff, (3) oscillating decline, and assign based on the project's actual survival label to create a controlled experiment

  **Fallback 2: Insufficient Sample Size**
  - If after filtering < 30 projects remain: reduce the minimum trajectory length from 6 months to 3 months
  - If still < 20 projects: use leave-one-out cross-validation instead of 5-fold
  - If < 10 projects: report descriptive statistics only (no model training)

  **Fallback 3: Model Convergence Failure**
  - If LogisticRegression fails: switch to RidgeClassifier with stronger regularization (alpha=10.0)
  - If all linear models fail: use a simple decision tree (max_depth=3) as a non-parametric baseline

  **Fallback 4: Falsification Control Issues**
  - If non-founder contributor data is unavailable: generate randomized fade curves by shuffling the founder's monthly shares within each project (preserving mean and variance but destroying temporal structure)
  - Compare original vs shuffled: if original significantly outperforms shuffled, this still supports the temporal structure hypothesis

  **Fallback 5: Time Budget Exceeded**
  - If sensitivity analysis takes too long: skip steps 8 (sensitivity) and 10 (visualization)
  - If permutation importance is too slow: reduce to n_repeats=5 and report with caveat
  - Minimum viable output: Model A, B, C AUC scores + directionality test + falsification result

  **Fallback 6: Data Schema Mismatch**
  - If full_data_out.json structure differs from expected: inspect the first 3 examples, adapt loading code dynamically
  - If survival labels are missing: fall back to using post-departure activity as a continuous target only
  - If project_id grouping fails: use row_index to reconstruct projects based on metadata_row_index patterns
testing_plan: |-
  ### TESTING PLAN: Gradual Scaling with Validation at Each Stage

  **Phase 1: Mini Data Test (3 projects from mini_data_out.json)**
  1. Load mini_data_out.json and verify structure matches expected schema
  2. Run data loading and project reconstruction - verify 3 projects loaded
  3. Compute fade descriptors for each project - verify all 6 descriptors produce finite values
  4. Train Model A (static-only) on 3 projects with 2-fold CV - verify it runs without error
  5. Verify output JSON matches exp_gen_sol_out schema
  6. Expected runtime: < 30 seconds

  **Phase 2: 10-Project Test (first 10 from full_data_out.json)**
  1. Load full_data_out.json, filter to first 10 unique project_ids
  2. Verify trajectory reconstruction: each project has >= 1 month of data
  3. Check descriptor distributions: slope should be negative (declining), cliff_score in [0,1]
  4. Run all 3 models with 5-fold CV - verify AUC scores are reasonable (0.4-1.0)
  5. Run permutation importance - verify it completes in < 2 minutes
  6. Run falsification control - verify founder AUC > shuffled AUC
  7. Expected runtime: < 2 minutes

  **Phase 3: 50-Project Test**
  1. Load first 50 unique project_ids
  2. Verify label balance (should be roughly 50/50)
  3. Run full pipeline including directionality analysis
  4. Record runtime and extrapolate: if 50 projects take X minutes, estimate time for 315
  5. If extrapolated time > 4 hours: consider reducing sensitivity analysis scope
  6. Expected runtime: < 10 minutes

  **Phase 4: Full Dataset (~315 projects)**
  1. Load all projects, filter to those with >= 6 months of data
  2. Run full pipeline: models, feature importance, directionality, falsification
  3. Run sensitivity analysis (if time permits)
  4. Generate visualizations
  5. Validate output JSON against schema
  6. Expected runtime: < 30 minutes

  **Phase 5: Final Validation**
  1. Re-run the full pipeline from scratch to verify reproducibility
  2. Check that all metrics are stable (AUC std < 0.1 across folds)
  3. Verify that method_out.json contains all required fields
  4. Verify that visualizations are readable and informative
  5. Run aii-json validation on output if available

  **Confirmation Signals to Look For:**
  - Fade descriptors produce reasonable values (slope negative, cliff_score in [0,1], fade_idx in [0,1])
  - Model C AUC >= Model A AUC (combined beats static-only)
  - Directionality test shows p < 0.1 (even weak signal is informative)
  - Falsification shows founder > non-founder (even small difference supports mechanism)
  - Feature importance shows at least one fade descriptor in top-5

  **Red Flags:**
  - All fade descriptors are identical across projects (data problem)
  - Model AUC = 1.0 (overfitting or data leakage)
  - Model AUC = 0.5 for all models (features have no signal)
  - Permutation importance takes > 10 minutes (need to reduce n_repeats)
  - Memory error (need to chunk processing)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_zNvSqNQvIA2R
type: dataset
title: OSS Founder Survival Dataset
summary: >-
  This artifact provides the ESEM2019 dataset (Avelino et al., ESEM 2019) — the seminal dataset on open-source project survival
  after founder departure. It contains 14,111 examples derived from 315 GitHub projects, each labeled as surviving or collapsed
  after the founder's 12-month inactivity window. Each example encodes monthly time-series features including founder commit/merge/review
  share, total activity, and static project metadata (stars, forks, contributors, bus factor). The dataset supports two classification
  tasks: (1) pre-departure survival prediction from founder activity decay patterns, and (2) post-departure recovery prediction
  from new contributor emergence. Label distribution: 4,132 collapsed, 4,368 not_recovered, 2,563 survived, 3,048 recovered.
  All examples follow the exp_sel_data_out.json schema with input/output fields and flat metadata_* keys. Source data from
  Zenodo (10.5281/zenodo.2546008).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
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
````

### [2] HUMAN-USER prompt · 2026-08-21 18:36:40 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-python · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-python** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-python
description: "Applies this repo's Python conventions to experiment and evaluation scripts: uv-only environment setup (never pip), loguru logging with stdout plus a rotating file sink, @logger.catch(reraise=True) with explicit exception types, pathlib file access, type hints, and a standard main() script skeleton. ALWAYS read before writing or editing any Python script that runs an experiment, evaluation, or data-processing job. Triggers: writing or refactoring a Python script, uv venv, uv pip install, pyproject dependencies, loguru, logging setup, try/except and error handling, pathlib, script structure, Python 3.12. NOT for: parallelism, GPU throughput or hardware sizing (use aii-parallel-computing and aii-use-hardware), scaling long autonomous jobs (use aii-long-running-tasks), splitting oversized output files (use aii-file-size-limit), calling LLMs (use aii-openrouter-llms), or notebooks meant for Colab (use aii-colab)."
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

### [4] SKILL-INPUT — aii-long-running-tasks · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-long-running-tasks** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-long-running-tasks
description: "Scales an experiment or evaluation up in stages — mini, 10, 50, 100, 200, then the largest run that fits — recording runtime at each step and extrapolating time-per-example against the remaining time budget before growing further, with background execution and hard RLIMIT_AS and RLIMIT_CPU caps. ALWAYS read before launching any script expected to run for many minutes or hours over a dataset. Triggers: long-running job, overnight or unattended run, time budget, how many examples fit, extrapolate runtime, start small then scale up, run in background and poll, avoid a timeout, full-dataset evaluation, resource limits. NOT for choosing the concurrency mechanism itself (aii-parallel-computing), measuring the machine's CPU, RAM or GPU (aii-use-hardware), or provisioning cloud pods (aii-runpod)."
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

### [5] SKILL-INPUT — aii-json · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-json** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-json
description: "Validates JSON files against this repo's experiment-pipeline schemas (exp_sel_data_out, exp_gen_sol_out, exp_eval_sol_out, exp_proof_out) and generates size-optimized full, mini and preview variants of any JSON array file. ALWAYS use before treating a pipeline stage output as finished, whenever a schema or required-property error must be fixed, and whenever a large JSON file needs a small truncated version safe to read. Triggers: JSON schema validation, schema compliance, required property errors, pipeline stage outputs, the exp_*_out format names, mini and preview JSON generation, shrinking a large JSON before inspection. NOT for: discovering or downloading new datasets, which aii-hf-datasets and aii-owid-datasets cover; splitting oversized output files, which aii-file-size-limit covers; plotting JSON data, which aii-data-fig-gen covers; spreadsheet and .csv tabular data, which anthropic-xlsx covers."
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

### [6] SKILL-INPUT — aii-file-size-limit · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-file-size-limit** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

```
---
name: aii-file-size-limit
description: "Splits an oversized generated output file into numbered parts that each fit a size limit: checks sizes with ls -lh, writes full_data_out_1.json, full_data_out_2.json and so on into a matching directory, deletes the original, repoints the reading code at a sorted glob, and regenerates mini and preview variants per part. ALWAYS run right after a script writes JSON output, and whenever a file is too big to keep, exceeds a stated file size limit, or gets rejected for its size. Triggers: file too large, output exceeds the size limit, oversized or huge JSON, ls -lh size check after generating results, splitting or chunking an output file into parts, output directory instead of one file. NOT for: schema validation or making mini and preview variants of a file already within the limit (use aii-json), or general Python script conventions (use aii-python)."
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

### [7] SKILL-INPUT — aii-use-hardware · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-use-hardware** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-use-hardware
description: "Detects the CPU, RAM, GPU and VRAM actually available — cgroup v1 and v2 container quotas and CPU affinity rather than misleading host values — then sets RAM and VRAM budgets via resource.setrlimit and torch.cuda.set_per_process_memory_fraction so a script raises a catchable error instead of being OOM-killed, and picks the right torch wheel for the detected device. ALWAYS read before loading a large dataset, installing torch, or sizing batches and worker counts. Triggers: how much RAM or CPU or GPU is available, container memory limit, cgroup, OOM killed, MemoryError, os.cpu_count reports host cores, nproc, VRAM, CUDA available, CPU-only torch build, dataset too big for memory, chunking. NOT for spreading work across that hardware once measured (aii-parallel-computing), staged scale-up runs against a time budget (aii-long-running-tasks), or renting cloud machines (aii-runpod)."
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

### [8] SKILL-INPUT — aii-parallel-computing · 2026-08-21 18:36:48 UTC

The agent loaded the **aii-parallel-computing** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-parallel-computing
description: "Parallelises compute-heavy Python: asyncio with aiohttp and a bounded Semaphore for I/O-bound work, ProcessPoolExecutor under the spawn start method for CPU-bound work, NumPy vectorisation and batched PyTorch on GPU with an out-of-memory halving fallback. ALWAYS read before writing any script that loops over data, issues many API calls, downloads many files, or runs heavy computation — sequential loops are the default failure mode. Triggers: parallelise, make a slow script faster, concurrency, async, aiohttp, asyncio.gather, semaphore, multiprocessing, ProcessPoolExecutor, fork deadlock with loguru, worker count, batch size, CUDA out of memory, idle GPU, retries and rate limits. NOT for detecting what hardware exists or setting RAM and VRAM budgets (aii-use-hardware), staged scale-up against a time budget (aii-long-running-tasks), or provisioning cloud pods (aii-runpod)."
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

### [9] SYSTEM-USER prompt · 2026-08-21 18:57:30 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/file.py`, `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>
<artifact_plan>
id: gen_plan_experiment_1_idx2
type: experiment
title: Founder Fade Curves Predict OSS Survival
summary: >-
  Test whether founder involvement fade curve descriptors provide complementary predictive value beyond static features in
  predicting OSS project survival after founder departure, using the ESEM2019 dataset.
runpod_compute_profile: cpu_light
implementation_pseudocode: |-
  ## EXPERIMENT PLAN: Founder Fade Curve Descriptors for OSS Survival Prediction

  ### OVERVIEW
  This experiment tests whether the SHAPE of a founder's involvement trajectory (fade curve) provides complementary predictive value beyond static project metrics in predicting whether an open-source project survives after the founder departs. We use the ESEM2019 dataset (Avelino et al., 315 GitHub projects) with pre-computed monthly founder involvement shares and survival labels.

  ### DATA SOURCE
  - Primary: full_data_out.json from dataset artifact (art_zNvSqNQvIA2R) at:
    /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/full_data_out.json
  - Raw ESEM2019 CSVs available at:
    /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1/temp/datasets/esem2019/data/
    (tfprojects_commits_new.csv, leavers.csv, tfdevelopers.csv, projectinfo.csv, measures.csv)

  ### STEP 0: Environment Setup
  ```
  uv venv .venv --python=3.12
  source .venv/bin/activate
  uv pip install pandas numpy scikit-learn scipy loguru matplotlib seaborn lifelines
  ```

  ### STEP 1: Data Loading and Project Reconstruction
  1. Load full_data_out.json
  2. Group examples by project_id to reconstruct per-project time series
  3. For each project, extract:
     - Pre-departure monthly time series: founder_commit_share, founder_merge_share, founder_review_share
     - Static features at departure: stars, forks, contributor_count, file_count, bus_factor, repo_age_days
     - Survival label (binary: survived vs collapsed)
  4. Compute combined founder share per month: mean(commit_share, merge_share, review_share)
  5. Attempt to enrich with raw ESEM2019 commit data:
     - Load tfprojects_commits_new.csv to get per-developer commit counts per month
     - If founder-level granularity exists, replace synthetic shares with real ratios
     - If not, proceed with synthetic shares but document limitation
  6. Filter to projects with >= 6 months of pre-departure data (need sufficient trajectory for curve fitting)
  7. Verify label balance (expect ~50/50 survived/collapsed)

  ### STEP 2: Fade Curve Descriptor Computation
  For each project's pre-departure time series (t=0 to t=T, where T = months to departure):

  Let y[t] = combined founder share at month t.

  **Descriptor 1: Linear Slope (S_slope)**
  - Fit y[t] = a + b*t via OLS
  - S_slope = b (negative = declining, positive = increasing)
  - Normalized by dividing by initial share: S_slope_norm = b / y[0]

  **Descriptor 2: Convexity (S_convex)**
  - Fit quadratic: y[t] = a + b*t + c*t^2
  - S_convex = c (positive = convex/accelerating decline, negative = concave/decelerating)
  - Normalized: S_convex_norm = c / y[0]

  **Descriptor 3: Decline Onset Time (S_decline_start)**
  - Compute first derivative: dy/dt = gradient(y)
  - Find first index where dy/dt < -threshold (threshold = 0.01 share/month)
  - S_decline_start = index / T (normalized to [0,1], where 0 = immediate decline, 1 = never declined)

  **Descriptor 4: Cliff Score (S_cliff)**
  - Compare final 2-month average to prior 6-month average
  - S_cliff = (avg[y[T-6:T-2]] - avg[y[T-2:T]]) / avg[y[T-6:T-2]]
  - Clipped to [0, 1]. High = abrupt cliff, low = smooth ending

  **Descriptor 5: Plateau-then-Cliff Indicator (S_plateau)**
  - If decline_start > 0.5 (decline started in second half) AND variance of pre-decline period < 0.5 * total variance:
    S_plateau = 1 (plateau-then-cliff pattern)
  - Else S_plateau = 0

  **Descriptor 6: Composite Fade Index (S_fade_idx)**
  - S_fade_idx = 1.0 - S_cliff + (0.3 if S_slope < 0 else 0) - (0.2 if S_plateau else 0)
  - Clipped to [0, 1]
  - Interpretation: 1.0 = perfect smooth fade, 0.0 = abrupt cliff

  ### STEP 3: Feature Engineering
  **Static Features (at departure):**
  - bus_factor_at_departure
  - contributor_count_at_departure
  - stars_at_departure (log-transformed)
  - file_count_at_departure (log-transformed)
  - repo_age_days_at_departure (converted to years)
  - commits_before_departure (log-transformed)
  - commits_after_departure (log-transformed)

  **Fade Features:**
  - S_slope_norm, S_convex_norm, S_decline_start, S_cliff, S_plateau, S_fade_idx

  **Interaction Features (for combined model):**
  - S_fade_idx * contributor_count (does fade matter more with more contributors?)
  - S_cliff * bus_factor (does cliff matter more with low bus factor?)

  ### STEP 4: Model Training and Evaluation

  **Model A: Static-Only Baseline**
  - Logistic Regression (L2 penalty, C=1.0, class_weight='balanced')
  - Features: static features only
  - Cross-validation: Stratified 5-fold (use metadata_fold from dataset)

  **Model B: Fade-Only**
  - Logistic Regression (same hyperparameters)
  - Features: fade descriptors only
  - Cross-validation: Stratified 5-fold

  **Model C: Combined**
  - Logistic Regression (same hyperparameters)
  - Features: static + fade + interaction features
  - Cross-validation: Stratified 5-fold

  **Model D: Regularization Comparison**
  - Ridge Regression for continuous target (post-departure activity)
  - Random Forest (n_estimators=100, max_depth=5) for binary classification
  - Compare with logistic regression to check for non-linear effects

  **Metrics:**
  - Primary: AUC-ROC (mean and std across folds)
  - Secondary: Log-loss, Accuracy, F1-score
  - Continuous: R-squared (for post-departure activity prediction)
  - Statistical: McNemar's test comparing Model A vs Model C predictions

  ### STEP 5: Feature Importance Analysis
  1. **Permutation Feature Importance** (n_repeats=30, random_state=42)
     - Run on Model C (combined) with 5-fold CV
     - Report mean importance and std for each feature
     - Compare fade feature importance vs static feature importance

  2. **Coefficient Analysis**
     - Extract logistic regression coefficients
     - Report standardized coefficients (coefficient * feature_std)
     - Check directionality: does higher fade_idx correlate with survival?

  3. **Univariate Analysis**
     - For each fade descriptor: compute point-biserial correlation with survival
     - Report p-values
     - Create boxplots (survived vs collapsed) for each descriptor

  ### STEP 6: Directionality Analysis
  1. **Fade Index vs Survival**
     - Compute mean fade_idx for survived vs collapsed projects
     - Two-sample t-test (or Mann-Whitney U if non-normal)
     - Report effect size (Cohen's d)

  2. **Cliff Score vs Survival**
     - Same analysis for cliff_score
     - Expect: collapsed projects have higher cliff scores

  3. **Slope vs Survival**
     - Expect: survived projects have more negative slopes (gradual decline)

  4. **Visualize**
     - Kernel density plots of fade_idx for survived vs collapsed
     - Scatter plot: fade_idx vs post-departure activity
     - Heatmap: correlation matrix of all features with survival

  ### STEP 7: Falsification Control (Founder-Specificity Test)
  **Purpose:** Verify that the fade curve's predictive power is founder-specific, not just a property of any high-activity contributor.

  1. For each project, identify the second-most-active contributor (not the founder)
  2. Generate synthetic "non-founder" involvement trajectories:
     - Use the same time series length as the founder
     - Randomize the shape: shuffle the founder's monthly shares, or generate random trajectories with the same mean and variance
  3. Compute the same 6 fade descriptors for these synthetic non-founder trajectories
  4. Train Model B' (Fade-Only) using non-founder descriptors
  5. Compare AUC: founder_fade_auc vs non_founder_fade_auc
  6. Expectation: founder_fade_auc > non_founder_fade_auc by a significant margin (>0.1)

  ### STEP 8: Sensitivity Analysis
  1. **Vary departure threshold:** Re-run with 6-month and 18-month inactivity windows (if data allows)
  2. **Vary trajectory length:** Re-run using only the last 12 months of pre-departure data vs full trajectory
  3. **Vary descriptor thresholds:** Test cliff_score with different window sizes (final 3 months vs final 2 months)
  4. **Subsample analysis:** Run on top-50 most-starred projects vs bottom-50 least-starred

  ### STEP 9: Output Generation
  Generate method_out.json with:
  ```
  {
    "metadata": {
      "method_name": "founder_fade_curves_experiment_iter2",
      "n_projects": <count>,
      "n_survived": <count>,
      "n_collapsed": <count>,
      "cv_folds": 5,
      "metrics": {
        "model_a_auc": <float>, "model_a_auc_std": <float>,
        "model_b_auc": <float>, "model_b_auc_std": <float>,
        "model_c_auc": <float>, "model_c_auc_std": <float>,
        "model_d_rf_auc": <float>,
        "model_a_logloss": <float>,
        "model_b_logloss": <float>,
        "model_c_logloss": <float>,
        "directionality_t_test_p": <float>,
        "directionality_cohens_d": <float>,
        "falsification_auc_diff": <float>
      },
      "feature_importance": {
        "fade_descriptors": { ... },
        "static_descriptors": { ... },
        "interaction_features": { ... }
      },
      "directionality": "<text summary>",
      "falsification_result": "<text summary>",
      "sensitivity_analysis": { ... }
    },
    "datasets": [
      {
        "dataset": "oss_founder_fade_survival_iter2",
        "examples": [
          {
            "input": "<json with project_id, static_features, fade_descriptors>",
            "output": "<json with survival label, post_departure_activity>",
            "metadata_fold": <int>,
            "metadata_feature_names": "<comma-separated>",
            "predict_static": "<survive/collapse>",
            "predict_fade": "<survive/collapse>",
            "predict_combined": "<survive/collapse>",
            "predict_static_prob": "<float>",
            "predict_fade_prob": "<float>",
            "predict_combined_prob": "<float>"
          }
        ]
      }
    ]
  }
  ```

  ### STEP 10: Visualization (save to results/ directory)
  1. results/fade_idx_distribution.png - KDE plot of fade_idx for survived vs collapsed
  2. results/feature_importance.png - Bar chart of permutation importance
  3. results/roc_curves.png - ROC curves for Models A, B, C
  4. results/correlation_heatmap.png - Feature correlation matrix
  5. results/cliff_vs_survival.png - Boxplot of cliff_score by survival

  ### GRADUAL SCALING
  1. **Mini (3 projects):** Load mini_data_out.json, run full pipeline, verify output schema
  2. **10 projects:** Load first 10 from full_data_out.json, verify descriptors compute correctly
  3. **50 projects:** Full pipeline, record runtime, extrapolate
  4. **All projects (~315):** Full pipeline with all analysis
  5. **Final validation:** Re-run on full data, verify reproducibility

  ### ERROR HANDLING
  - If raw ESEM2019 commit data cannot be parsed: proceed with synthetic shares, log warning
  - If < 6 months of data for a project: skip that project, log count
  - If logistic regression fails to converge: increase max_iter to 5000
  - If class imbalance > 70/30: use SMOTE oversampling (imbalanced-learn)
  - If permutation importance takes too long: reduce n_repeats to 10

  ### EXPECTED OUTCOMES
  **Supporting evidence:**
  - Model C (combined) AUC > Model A (static-only) AUC by >= 0.05
  - Fade descriptors rank in top-3 feature importances
  - Higher fade_idx associated with survival (p < 0.05)
  - Founder fade AUC > non-founder fade AUC by >= 0.1

  **Disconfirming evidence:**
  - Fade descriptors add no predictive value (Model C AUC ≈ Model A AUC)
  - Directional effect reverses or is null
  - Non-founder fade curves predict equally well
fallback_plan: |-
  IF the primary approach fails at any stage, execute these fallbacks in order:

  **Fallback 1: Synthetic Data Limitation**
  - If raw ESEM2019 commit data cannot provide founder-level granularity (likely), proceed with the synthetic founder shares from full_data_out.json
  - Mitigate by: (a) generating multiple synthetic trajectory variations per project with different random seeds to create diversity, (b) adding noise to synthetic shares to simulate real-world variation, (c) explicitly documenting this as a limitation in the output
  - Generate 3 trajectory variants per project: (1) smooth linear decline, (2) plateau-then-cliff, (3) oscillating decline, and assign based on the project's actual survival label to create a controlled experiment

  **Fallback 2: Insufficient Sample Size**
  - If after filtering < 30 projects remain: reduce the minimum trajectory length from 6 months to 3 months
  - If still < 20 projects: use leave-one-out cross-validation instead of 5-fold
  - If < 10 projects: report descriptive statistics only (no model training)

  **Fallback 3: Model Convergence Failure**
  - If LogisticRegression fails: switch to RidgeClassifier with stronger regularization (alpha=10.0)
  - If all linear models fail: use a simple decision tree (max_depth=3) as a non-parametric baseline

  **Fallback 4: Falsification Control Issues**
  - If non-founder contributor data is unavailable: generate randomized fade curves by shuffling the founder's monthly shares within each project (preserving mean and variance but destroying temporal structure)
  - Compare original vs shuffled: if original significantly outperforms shuffled, this still supports the temporal structure hypothesis

  **Fallback 5: Time Budget Exceeded**
  - If sensitivity analysis takes too long: skip steps 8 (sensitivity) and 10 (visualization)
  - If permutation importance is too slow: reduce to n_repeats=5 and report with caveat
  - Minimum viable output: Model A, B, C AUC scores + directionality test + falsification result

  **Fallback 6: Data Schema Mismatch**
  - If full_data_out.json structure differs from expected: inspect the first 3 examples, adapt loading code dynamically
  - If survival labels are missing: fall back to using post-departure activity as a continuous target only
  - If project_id grouping fails: use row_index to reconstruct projects based on metadata_row_index patterns
testing_plan: |-
  ### TESTING PLAN: Gradual Scaling with Validation at Each Stage

  **Phase 1: Mini Data Test (3 projects from mini_data_out.json)**
  1. Load mini_data_out.json and verify structure matches expected schema
  2. Run data loading and project reconstruction - verify 3 projects loaded
  3. Compute fade descriptors for each project - verify all 6 descriptors produce finite values
  4. Train Model A (static-only) on 3 projects with 2-fold CV - verify it runs without error
  5. Verify output JSON matches exp_gen_sol_out schema
  6. Expected runtime: < 30 seconds

  **Phase 2: 10-Project Test (first 10 from full_data_out.json)**
  1. Load full_data_out.json, filter to first 10 unique project_ids
  2. Verify trajectory reconstruction: each project has >= 1 month of data
  3. Check descriptor distributions: slope should be negative (declining), cliff_score in [0,1]
  4. Run all 3 models with 5-fold CV - verify AUC scores are reasonable (0.4-1.0)
  5. Run permutation importance - verify it completes in < 2 minutes
  6. Run falsification control - verify founder AUC > shuffled AUC
  7. Expected runtime: < 2 minutes

  **Phase 3: 50-Project Test**
  1. Load first 50 unique project_ids
  2. Verify label balance (should be roughly 50/50)
  3. Run full pipeline including directionality analysis
  4. Record runtime and extrapolate: if 50 projects take X minutes, estimate time for 315
  5. If extrapolated time > 4 hours: consider reducing sensitivity analysis scope
  6. Expected runtime: < 10 minutes

  **Phase 4: Full Dataset (~315 projects)**
  1. Load all projects, filter to those with >= 6 months of data
  2. Run full pipeline: models, feature importance, directionality, falsification
  3. Run sensitivity analysis (if time permits)
  4. Generate visualizations
  5. Validate output JSON against schema
  6. Expected runtime: < 30 minutes

  **Phase 5: Final Validation**
  1. Re-run the full pipeline from scratch to verify reproducibility
  2. Check that all metrics are stable (AUC std < 0.1 across folds)
  3. Verify that method_out.json contains all required fields
  4. Verify that visualizations are readable and informative
  5. Run aii-json validation on output if available

  **Confirmation Signals to Look For:**
  - Fade descriptors produce reasonable values (slope negative, cliff_score in [0,1], fade_idx in [0,1])
  - Model C AUC >= Model A AUC (combined beats static-only)
  - Directionality test shows p < 0.1 (even weak signal is informative)
  - Falsification shows founder > non-founder (even small difference supports mechanism)
  - Feature importance shows at least one fade descriptor in top-5

  **Red Flags:**
  - All fade descriptors are identical across projects (data problem)
  - Model AUC = 1.0 (overfitting or data leakage)
  - Model AUC = 0.5 for all models (features have no signal)
  - Permutation importance takes > 10 minutes (need to reduce n_repeats)
  - Memory error (need to chunk processing)
</artifact_plan>

<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
id: art_zNvSqNQvIA2R
type: dataset
title: OSS Founder Survival Dataset
summary: >-
  This artifact provides the ESEM2019 dataset (Avelino et al., ESEM 2019) — the seminal dataset on open-source project survival
  after founder departure. It contains 14,111 examples derived from 315 GitHub projects, each labeled as surviving or collapsed
  after the founder's 12-month inactivity window. Each example encodes monthly time-series features including founder commit/merge/review
  share, total activity, and static project metadata (stars, forks, contributors, bus factor). The dataset supports two classification
  tasks: (1) pre-departure survival prediction from founder activity decay patterns, and (2) post-departure recovery prediction
  from new contributor emergence. Label distribution: 4,132 collapsed, 4,368 not_recovered, 2,563 survived, 3,048 recovered.
  All examples follow the exp_sel_data_out.json schema with input/output fields and flat metadata_* keys. Source data from
  Zenodo (10.5281/zenodo.2546008).
workspace_path: >-
  /ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_1/gen_art/gen_art_dataset_1
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

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>

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

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/3_invention_loop/iter_2/gen_art/gen_art_experiment_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````
