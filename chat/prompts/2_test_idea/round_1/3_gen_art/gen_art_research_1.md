# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 1 · `gen_art`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-20 20:39:26 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: 'Literature Survey: Founder Fade & OSS Survival'
summary: >-
  Comprehensive literature survey across four areas to ground the Founder Fade Curve hypothesis in existing methods, data
  sources, and analytical techniques.
runpod_compute_profile: cpu_light
question: >-
  What does the existing literature tell us about (1) how OSS project survival after founder departure is measured, (2) how
  to reliably identify founders from git history, (3) what large-scale GitHub data sources are available for building a departed-founder
  cohort, and (4) how to quantify trajectory shape descriptors from time-series involvement data?
research_plan: |-
  ## OVERALL STRATEGY

  Conduct systematic web and scholarly research across FOUR areas. For each area: (a) run targeted scholarly searches to find primary papers, (b) fetch full papers (PDFs via arXiv or journal pages) for methodological detail, (c) use fetch_grep to extract exact numbers, definitions, and methodology sections, (d) synthesize into a structured report with concrete recommendations.

  Work through areas sequentially within each batch but parallelize independent searches.

  ---

  ## AREA 1: OSS Project Abandonment and Survival Measurement

  Goal: Establish the best survival/abandonment definition for cohort labeling, understand strengths/weaknesses of each approach, and decide which to adopt.

  ### Step 1.1: Find and read Avelino et al. (2019)
  - Search (scholarly): Avelino Constantinou Valente Serebrenik 2019 abandonment survival open source truck factor
  - Search (scholarly): truck-factor-developer detachment TFDD surviving system Avelino
  - Fetch the full PDF (likely at arXiv or journal page). Use fetch_grep to extract:
    - Exact definition of truck-factor developer and how they identify them
    - The TFDD event definition and inactivity threshold (how many months?)
    - The surviving system criterion: what exactly counts as survival?
    - The static features they tested and their predictive power (AUC, accuracy, effect sizes)
    - Sample size: how many projects? What repositories? What time window?
    - Any discussion of limitations, especially around snapshot vs. dynamic measures

  ### Step 1.2: Find and read Chen et al. (ICSE 2026)
  - Search (scholarly): Chen Stol Santos German Trinkenreich 2026 core contributor disengagement open source ICSE
  - Search (scholarly): core contributor disengagement open source difference-in-differences 2026
  - Fetch the full PDF (ICSE 2026 proceedings, likely on IEEE Xplore or arXiv).
  - Extract via fetch_grep:
    - How they define core contributor disengagement and the inactivity threshold
    - The quasi-experimental design: DiD setup, treatment vs. control, 50,804 repositories
    - Outcome measures: PR throughput, acceptance rate, merge time
    - Static contributor profile features (commit-share, tenure) and their findings
    - Any discussion of founder vs. non-founder effects
    - Limitations and future work that might relate to our trajectory approach

  ### Step 1.3: Find and read Kaushik and Chahal (2026)
  - Search (scholarly): Kaushik Chahal 2026 death spiral open source pull request workflow
  - Search (scholarly): death spiral open source projects pull request friction backlog 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - How they define inactive vs active projects
    - The death spiral signals: friction, backlog growth, falling innovation, rising merge latency
    - Their finding that popularity/innovation are causes of survival while workflow friction is a byproduct
    - Aggregate community-level dynamics vs. founder-specific analysis
    - Time windows and thresholds used

  ### Step 1.4: Find and read Karim et al. (2026)
  - Search (scholarly): Karim Lu Kasaadha Goggins 2026 predicting open source sustainability deep temporal hierarchical
  - Search (scholarly): predicting open source sustainability transformer temporal architecture 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - The hierarchical Transformer model architecture
    - 24-month aggregate activity sequences: what features, how computed
    - Lifecycle stage classification: what stages, how labeled
    - Performance metrics and baselines
    - Whether they mention founders, succession, or individual developer trajectories

  ### Step 1.5: Find and read Noori et al. (2025)
  - Search (scholarly): Noori Chakraborti Zhang Frey 2025 founder leadership community governance open source
  - Search (scholarly): governance.md textual governance evolution open source 2025
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - NLP pipeline for governance.md analysis: roles, actions, deontics
    - 637 repositories: selection criteria
    - How they characterize institutional maturation
    - Connection between governance text and actual project survival

  ### Step 1.6: Broader survival measurement survey
  - Search (scholarly): open source project abandonment definition criteria survey 2020 2021 2022 2023 2024
  - Search (scholarly): OSS project survival prediction machine learning review
  - Search (scholarly): abandoned open source projects GitHub empirical study
  - Fetch 2-3 of the most relevant papers to understand the landscape of survival definitions.
  - Extract: Alternative survival definitions and their trade-offs.

  ### Step 1.7: Synthesis for Area 1
  - Compare all survival definitions: which is most rigorous, most reproducible, best suited for our hypothesis?
  - Recommend a primary survival label (binary) and a continuous survival metric.
  - Flag validity concerns: does the Avelino criterion miss projects that survive without new truck-factor developers? Does a 12-month inactivity window capture all departures?

  ---

  ## AREA 2: Founder Identification and Key-Developer Attribution

  Goal: Find reliable methods for identifying the founder from git history, handling edge cases (email aliases, organizational accounts, multi-founder projects).

  ### Step 2.1: Search for founder identification methods
  - Search (scholarly): founder identification git history open source project creator
  - Search (scholarly): key developer identification open source contribution analysis
  - Search (scholarly): truck factor calculation methodology Cosentino
  - Search (scholarly): developer identity resolution email alias merging git
  - Fetch 3-5 most relevant papers.

  ### Step 2.2: Extract founder identification methodologies
  - For each relevant paper, use fetch_grep to extract:
    - How they define and identify the founder or principal early developer
    - Methods for handling multiple email addresses per developer
    - How they separate founders from other early key contributors
    - Reliability metrics: how often does the method misidentify?
    - Edge cases handled: organizational accounts, multi-founder repos, repos with early forking

  ### Step 2.3: Search for identity resolution tools
  - Search (general): git author email alias resolution tool
  - Search (general): GitHub contributor identity merging algorithm
  - Search (scholarly): software developer identity resolution empirical study
  - Fetch and extract: Available tools and their accuracy.

  ### Step 2.4: Search for multi-founder and organizational account handling
  - Search (scholarly): multi-founder open source project identification
  - Search (scholarly): organizational account bot detection GitHub commits
  - Fetch and extract: Methods for detecting and handling these edge cases.

  ### Step 2.5: Synthesis for Area 2
  - Recommend a concrete founder identification protocol:
    - Primary method: earliest sustained commit/merge activity + repository creator
    - Fallback: manual verification for ambiguous cases
    - Email alias merging strategy
    - Edge case handling rules (org accounts, bots, multi-founder)
  - Flag validity threats: founder misidentification rate, impact on trajectory shape

  ---

  ## AREA 3: Available Large-Scale GitHub Data Sources

  Goal: Identify feasible data sources for building a departed-founder cohort, including access methods, rate limits, costs, and extraction strategies.

  ### Step 3.1: GHTorrent dataset
  - Search (scholarly): GHTorrent dataset GitHub repository mining 2024 2025
  - Search (general): GHTorrent current status 2024 2025 download
  - Search (general): GHTorrent MongoDB schema repository commits pulls
  - Fetch the GHTorrent website (ghtorrent.org) and any recent papers about it.
  - Extract via fetch_grep:
    - Current status: is it still maintained? Last update date?
    - Data coverage: how many repositories? What time range?
    - Schema: what fields are available for commits, pulls, reviews, authors?
    - Download method and size
    - Known limitations (incomplete data, missing fields)

  ### Step 3.2: GH Archive and Google BigQuery
  - Search (general): GH Archive Google BigQuery public dataset GitHub events 2024 2025
  - Search (general): bigquery publicdata github archives schema
  - Search (scholarly): using Google BigQuery GitHub data open source research
  - Fetch the GH Archive website (www.gharchive.org) and BigQuery documentation.
  - Extract via fetch_grep:
    - Available event types: PushEvent, PullRequestEvent, IssuesEvent, etc.
    - Time coverage and granularity
    - Query costs and free tier limits
    - Rate limits and best practices for large queries
    - Can we get per-author per-month commit counts from BigQuery?

  ### Step 3.3: GitHub REST and GraphQL APIs
  - Search (general): GitHub REST API rate limiting best practices 2024 2025
  - Search (general): GitHub GraphQL API commits pulls reviews pagination
  - Search (general): GitHub API token authentication rate limit increase
  - Fetch GitHub API documentation pages.
  - Extract via fetch_grep:
    - REST API rate limits: unauthenticated vs. authenticated (token)
    - GraphQL API rate limits: node-based throttling
    - Pagination strategies for large repositories
    - Available endpoints for: commits (author, date), pull requests (merged_by, reviews), code reviews (state, user)
    - Can we get the founder share of merges/reviews per month?
    - Cost of API tokens (free tier limits)

  ### Step 3.4: Direct git-log parsing
  - Search (general): git log parse author date commit count per month
  - Search (scholarly): git history mining open source project analysis methodology
  - Fetch and extract: Best practices for cloning and parsing git history at scale.

  ### Step 3.5: Published OSS dataset curation methodologies
  - Search (scholarly): open source repository dataset curation methodology GitHub
  - Search (scholarly): building cohort abandoned open source projects GitHub
  - Fetch 2-3 relevant papers.
  - Extract: How previous studies built their cohorts: selection criteria, sampling strategy, data collection pipeline.

  ### Step 3.6: Synthesis for Area 3
  - Rank data sources by feasibility for our specific needs:
    1. Can we get per-author per-month commit/merge/review shares?
    2. Can we identify projects where the founder departed?
    3. What is the cost (time, money, infrastructure)?
    4. What is the maximum cohort size feasible within budget?
  - Recommend a primary data source + fallback strategy.
  - Provide concrete access details: URLs, API endpoints, authentication requirements, estimated costs.

  ---

  ## AREA 4: Trajectory Shape Analysis and Quantitative Curve Classification

  Goal: Find validated methods for converting a per-month involvement-share time series into the required descriptors: slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator, and a bounded 0-1 fade index.

  ### Step 4.1: Trend estimation methods
  - Search (scholarly): Theil-Sen estimator trend detection time series robust
  - Search (scholarly): OLS vs Theil-Sen trend estimation time series comparison
  - Search (scholarly): trend slope estimation small sample time series
  - Fetch 2-3 relevant papers.
  - Extract via fetch_grep:
    - When to use Theil-Sen vs. OLS for trend estimation
    - Minimum sample size requirements
    - Robustness to outliers (important for monthly data with zero-activity months)
    - Implementation in Python (scipy.stats.theilsen)

  ### Step 4.2: Change-point detection for cliff events
  - Search (scholarly): change point detection abrupt transition time series
  - Search (scholarly): ruptures Python change point detection
  - Search (scholarly): binary segmentation change point detection
  - Search (scholarly): PELT change point detection algorithm
  - Fetch and extract:
    - Available algorithms: Binary Segmentation, PELT, Wild Binary Segmentation
    - How to detect a single abrupt drop (cliff) vs. gradual decline
    - Python libraries: ruptures, spts, changepoint
    - Minimum signal length requirements
    - How to quantify abruptness of a change point

  ### Step 4.3: Convexity and curvature analysis
  - Search (scholarly): convexity concavity time series quadratic fit
  - Search (scholarly): second derivative time series curvature analysis
  - Search (scholarly): trajectory shape classification convex concave linear
  - Fetch and extract:
    - Methods for measuring convexity/concavity of a trajectory
    - Quadratic fit: how to interpret the quadratic coefficient
    - Discrete second derivative for noisy data
    - Connection to scaffolding fade shape (concave = accelerating fade, convex = decelerating fade)

  ### Step 4.4: Plateau detection
  - Search (scholarly): plateau detection time series flat region
  - Search (scholarly): detecting stationary periods time series
  - Search (scholarly): run test stationarity time series
  - Fetch and extract:
    - Methods for detecting extended flat regions (plateaus)
    - Statistical tests for stationarity in sub-segments
    - How to define plateau-then-cliff pattern quantitatively

  ### Step 4.5: Half-life and decay rate analysis
  - Search (scholarly): half-life decay rate time series analysis
  - Search (scholarly): exponential decay fitting time series involvement
  - Search (scholarly): time-to-onset decline detection
  - Fetch and extract:
    - How to estimate half-life of involvement decline
    - Exponential decay fitting: when appropriate, how to implement
    - Detecting the onset of decline (when does the fade begin?)

  ### Step 4.6: Scaffolding theory and fading index operationalization
  - Search (scholarly): scaffolding fading index educational psychology operationalization
  - Search (scholarly): Vygotsky scaffolding fading measurement quantitative
  - Search (scholarly): Wood Bruner Ross scaffolding fading operationalization
  - Search (scholarly): teacher support withdrawal trajectory measurement
  - Fetch and extract:
    - Has anyone quantified fading in educational settings?
    - Any existing fading index or withdrawal index from psychology literature?
    - How do they measure the smoothness of support withdrawal?
    - Connection between fade smoothness and learner outcomes

  ### Step 4.7: Composite index construction
  - Search (scholarly): composite index construction time series features
  - Search (scholarly): normalizing multiple features bounded index 0 to 1
  - Fetch and extract:
    - Methods for combining multiple shape descriptors into a single bounded index
    - Normalization techniques (min-max, z-score, rank-based)
    - Weighting schemes for composite indices

  ### Step 4.8: Synthesis for Area 4
  - Recommend a concrete feature extraction pipeline:
    1. Input: per-month founder involvement share (0-1) over project lifespan
    2. Feature 1: Linear slope (Theil-Sen estimator)
    3. Feature 2: Convexity (quadratic coefficient from polynomial fit)
    4. Feature 3: Time-to-onset-of-decline (change-point detection)
    5. Feature 4: Abrupt-cliff indicator (binary: largest single-month drop exceeds threshold)
    6. Feature 5: Plateau-then-cliff indicator (binary: extended flat region followed by cliff)
    7. Feature 6: Composite fade index (0-1, combining smoothness and gradualness)
  - Provide Python library recommendations for each feature
  - Flag validity concerns: small sample sizes, noisy monthly data, edge cases

  ---

  ## FINAL SYNTHESIS AND REPORT STRUCTURE

  After completing all four areas, produce a structured report (research_report.md) with:

  1. Executive Summary: One-page overview of key findings and recommendations
  2. Area 1 Report: Survival measurement - recommended definition, rationale, trade-offs
  3. Area 2 Report: Founder identification - recommended protocol, edge cases, reliability
  4. Area 3 Report: Data sources - ranked list with access details, cost estimates, feasibility
  5. Area 4 Report: Trajectory features - recommended feature extraction pipeline with Python libraries
  6. Validity Threats Matrix: Ranked list of all validity concerns with proposed mitigations:
     - Founder misidentification
     - Survival label ambiguity
     - Bus-factor confound with moderate fade
     - Project age confound (older projects have more time to fade)
     - Popularity confound (popular projects attract more contributors regardless of fade)
     - Small sample size for departed-founder cohort
     - Selection bias (only public GitHub projects)
     - Founder re-engagement (founder returns after departure)
     - Multi-founder projects
  7. Recommended Next Steps: Concrete action items for the next phase (data collection)
  8. Bibliography: Complete list of all sources with citations

  ## OUTPUT FORMAT

  Produce two files:
  1. research_out.json: Structured JSON with answer, sources, follow_up_questions
     - answer: synthesized findings for each area
     - sources: list of all papers/sources with URLs and key findings
     - follow_up_questions: open questions that need resolution before data collection
  2. research_report.md: Full structured report as described above

  ## TIME BUDGET (3 hours total)
  - Area 1 (Survival measurement): 45 minutes
  - Area 2 (Founder identification): 30 minutes
  - Area 3 (Data sources): 45 minutes
  - Area 4 (Trajectory features): 45 minutes
  - Final synthesis and report writing: 15 minutes

  ## BUDGET CONSTRAINTS
  - Web search and fetch are free (keyless engines)
  - No code execution needed - pure research
  - Focus on quality of synthesis over quantity of sources
  - Prioritize fetching full PDFs of the 6 key papers from the hypothesis (Avelino 2019, Chen ICSE 2026, Kaushik and Chahal 2026, Karim et al. 2026, Noori et al. 2025, and one scaffolding theory paper)

  ## FAILURE SCENARIOS AND MITIGATIONS
  - If a key paper is not findable: Search by author name + topic keywords; try arXiv directly; look for preprint versions; note the gap in the report
  - If PDF fetch fails: Try the HTML abstract page; use fetch_grep on the abstract to get key details; note limitations
  - If data source is no longer available: Find alternatives; note the change; recommend the next best option
  - If trajectory methods are too complex for our data: Simplify to the most robust features (slope + cliff indicator) and note the trade-off
  - If cohort size estimates are too small: Recommend broader inclusion criteria or alternative data sources
explanation: >-
  This research is the foundational literature survey for the Founder Fade Curve hypothesis. Before any data collection or
  experiment, we must ground our methodology in established work: adopt the right survival definition from Avelino et al.
  (2019) and newer 2025-2026 studies, identify reliable founder-detection methods, select feasible data sources within our
  budget constraints, and choose validated trajectory-shape descriptors. The survey will produce concrete operational definitions,
  a ranked list of data sources with access details, recommended feature extraction methods, and a thorough list of validity
  threats with mitigations.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-20 20:39:26 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SYSTEM-USER prompt · 2026-08-20 20:39:29 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST N
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: 'Literature Survey: Founder Fade & OSS Survival'
summary: >-
  Comprehensive literature survey across four areas to ground the Founder Fade Curve hypothesis in existing methods, data
  sources, and analytical techniques.
runpod_compute_profile: cpu_light
question: >-
  What does the existing literature tell us about (1) how OSS project survival after founder departure is measured, (2) how
  to reliably identify founders from git history, (3) what large-scale GitHub data sources are available for building a departed-founder
  cohort, and (4) how to quantify trajectory shape descriptors from time-series involvement data?
research_plan: |-
  ## OVERALL STRATEGY

  Conduct systematic web and scholarly research across FOUR areas. For each area: (a) run targeted scholarly searches to find primary papers, (b) fetch full papers (PDFs via arXiv or journal pages) for methodological detail, (c) use fetch_grep to extract exact numbers, definitions, and methodology sections, (d) synthesize into a structured report with concrete recommendations.

  Work through areas sequentially within each batch but parallelize independent searches.

  ---

  ## AREA 1: OSS Project Abandonment and Survival Measurement

  Goal: Establish the best survival/abandonment definition for cohort labeling, understand strengths/weaknesses of each approach, and decide which to adopt.

  ### Step 1.1: Find and read Avelino et al. (2019)
  - Search (scholarly): Avelino Constantinou Valente Serebrenik 2019 abandonment survival open source truck factor
  - Search (scholarly): truck-factor-developer detachment TFDD surviving system Avelino
  - Fetch the full PDF (likely at arXiv or journal page). Use fetch_grep to extract:
    - Exact definition of truck-factor developer and how they identify them
    - The TFDD event definition and inactivity threshold (how many months?)
    - The surviving system criterion: what exactly counts as survival?
    - The static features they tested and their predictive power (AUC, accuracy, effect sizes)
    - Sample size: how many projects? What repositories? What time window?
    - Any discussion of limitations, especially around snapshot vs. dynamic measures

  ### Step 1.2: Find and read Chen et al. (ICSE 2026)
  - Search (scholarly): Chen Stol Santos German Trinkenreich 2026 core contributor disengagement open source ICSE
  - Search (scholarly): core contributor disengagement open source difference-in-differences 2026
  - Fetch the full PDF (ICSE 2026 proceedings, likely on IEEE Xplore or arXiv).
  - Extract via fetch_grep:
    - How they define core contributor disengagement and the inactivity threshold
    - The quasi-experimental design: DiD setup, treatment vs. control, 50,804 repositories
    - Outcome measures: PR throughput, acceptance rate, merge time
    - Static contributor profile features (commit-share, tenure) and their findings
    - Any discussion of founder vs. non-founder effects
    - Limitations and future work that might relate to our trajectory approach

  ### Step 1.3: Find and read Kaushik and Chahal (2026)
  - Search (scholarly): Kaushik Chahal 2026 death spiral open source pull request workflow
  - Search (scholarly): death spiral open source projects pull request friction backlog 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - How they define inactive vs active projects
    - The death spiral signals: friction, backlog growth, falling innovation, rising merge latency
    - Their finding that popularity/innovation are causes of survival while workflow friction is a byproduct
    - Aggregate community-level dynamics vs. founder-specific analysis
    - Time windows and thresholds used

  ### Step 1.4: Find and read Karim et al. (2026)
  - Search (scholarly): Karim Lu Kasaadha Goggins 2026 predicting open source sustainability deep temporal hierarchical
  - Search (scholarly): predicting open source sustainability transformer temporal architecture 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - The hierarchical Transformer model architecture
    - 24-month aggregate activity sequences: what features, how computed
    - Lifecycle stage classification: what stages, how labeled
    - Performance metrics and baselines
    - Whether they mention founders, succession, or individual developer trajectories

  ### Step 1.5: Find and read Noori et al. (2025)
  - Search (scholarly): Noori Chakraborti Zhang Frey 2025 founder leadership community governance open source
  - Search (scholarly): governance.md textual governance evolution open source 2025
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - NLP pipeline for governance.md analysis: roles, actions, deontics
    - 637 repositories: selection criteria
    - How they characterize institutional maturation
    - Connection between governance text and actual project survival

  ### Step 1.6: Broader survival measurement survey
  - Search (scholarly): open source project abandonment definition criteria survey 2020 2021 2022 2023 2024
  - Search (scholarly): OSS project survival prediction machine learning review
  - Search (scholarly): abandoned open source projects GitHub empirical study
  - Fetch 2-3 of the most relevant papers to understand the landscape of survival definitions.
  - Extract: Alternative survival definitions and their trade-offs.

  ### Step 1.7: Synthesis for Area 1
  - Compare all survival definitions: which is most rigorous, most reproducible, best suited for our hypothesis?
  - Recommend a primary survival label (binary) and a continuous survival metric.
  - Flag validity concerns: does the Avelino criterion miss projects that survive without new truck-factor developers? Does a 12-month inactivity window capture all departures?

  ---

  ## AREA 2: Founder Identification and Key-Developer Attribution

  Goal: Find reliable methods for identifying the founder from git history, handling edge cases (email aliases, organizational accounts, multi-founder projects).

  ### Step 2.1: Search for founder identification methods
  - Search (scholarly): founder identification git history open source project creator
  - Search (scholarly): key developer identification open source contribution analysis
  - Search (scholarly): truck factor calculation methodology Cosentino
  - Search (scholarly): developer identity resolution email alias merging git
  - Fetch 3-5 most relevant papers.

  ### Step 2.2: Extract founder identification methodologies
  - For each relevant paper, use fetch_grep to extract:
    - How they define and identify the founder or principal early developer
    - Methods for handling multiple email addresses per developer
    - How they separate founders from other early key contributors
    - Reliability metrics: how often does the method misidentify?
    - Edge cases handled: organizational accounts, multi-founder repos, repos with early forking

  ### Step 2.3: Search for identity resolution tools
  - Search (general): git author email alias resolution tool
  - Search (general): GitHub contributor identity merging algorithm
  - Search (scholarly): software developer identity resolution empirical study
  - Fetch and extract: Available tools and their accuracy.

  ### Step 2.4: Search for multi-founder and organizational account handling
  - Search (scholarly): multi-founder open source project identification
  - Search (scholarly): organizational account bot detection GitHub commits
  - Fetch and extract: Methods for detecting and handling these edge cases.

  ### Step 2.5: Synthesis for Area 2
  - Recommend a concrete founder identification protocol:
    - Primary method: earliest sustained commit/merge activity + repository creator
    - Fallback: manual verification for ambiguous cases
    - Email alias merging strategy
    - Edge case handling rules (org accounts, bots, multi-founder)
  - Flag validity threats: founder misidentification rate, impact on trajectory shape

  ---

  ## AREA 3: Available Large-Scale GitHub Data Sources

  Goal: Identify feasible data sources for building a departed-founder cohort, including access methods, rate limits, costs, and extraction strategies.

  ### Step 3.1: GHTorrent dataset
  - Search (scholarly): GHTorrent dataset GitHub repository mining 2024 2025
  - Search (general): GHTorrent current status 2024 2025 download
  - Search (general): GHTorrent MongoDB schema repository commits pulls
  - Fetch the GHTorrent website (ghtorrent.org) and any recent papers about it.
  - Extract via fetch_grep:
    - Current status: is it still maintained? Last update date?
    - Data coverage: how many repositories? What time range?
    - Schema: what fields are available for commits, pulls, reviews, authors?
    - Download method and size
    - Known limitations (incomplete data, missing fields)

  ### Step 3.2: GH Archive and Google BigQuery
  - Search (general): GH Archive Google BigQuery public dataset GitHub events 2024 2025
  - Search (general): bigquery publicdata github archives schema
  - Search (scholarly): using Google BigQuery GitHub data open source research
  - Fetch the GH Archive website (www.gharchive.org) and BigQuery documentation.
  - Extract via fetch_grep:
    - Available event types: PushEvent, PullRequestEvent, IssuesEvent, etc.
    - Time coverage and granularity
    - Query costs and free tier limits
    - Rate limits and best practices for large queries
    - Can we get per-author per-month commit counts from BigQuery?

  ### Step 3.3: GitHub REST and GraphQL APIs
  - Search (general): GitHub REST API rate limiting best practices 2024 2025
  - Search (general): GitHub GraphQL API commits pulls reviews pagination
  - Search (general): GitHub API token authentication rate limit increase
  - Fetch GitHub API documentation pages.
  - Extract via fetch_grep:
    - REST API rate limits: unauthenticated vs. authenticated (token)
    - GraphQL API rate limits: node-based throttling
    - Pagination strategies for large repositories
    - Available endpoints for: commits (author, date), pull requests (merged_by, reviews), code reviews (state, user)
    - Can we get the founder share of merges/reviews per month?
    - Cost of API tokens (free tier limits)

  ### Step 3.4: Direct git-log parsing
  - Search (general): git log parse author date commit count per month
  - Search (scholarly): git history mining open source project analysis methodology
  - Fetch and extract: Best practices for cloning and parsing git history at scale.

  ### Step 3.5: Published OSS dataset curation methodologies
  - Search (scholarly): open source repository dataset curation methodology GitHub
  - Search (scholarly): building cohort abandoned open source projects GitHub
  - Fetch 2-3 relevant papers.
  - Extract: How previous studies built their cohorts: selection criteria, sampling strategy, data collection pipeline.

  ### Step 3.6: Synthesis for Area 3
  - Rank data sources by feasibility for our specific needs:
    1. Can we get per-author per-month commit/merge/review shares?
    2. Can we identify projects where the founder departed?
    3. What is the cost (time, money, infrastructure)?
    4. What is the maximum cohort size feasible within budget?
  - Recommend a primary data source + fallback strategy.
  - Provide concrete access details: URLs, API endpoints, authentication requirements, estimated costs.

  ---

  ## AREA 4: Trajectory Shape Analysis and Quantitative Curve Classification

  Goal: Find validated methods for converting a per-month involvement-share time series into the required descriptors: slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator, and a bounded 0-1 fade index.

  ### Step 4.1: Trend estimation methods
  - Search (scholarly): Theil-Sen estimator trend detection time series robust
  - Search (scholarly): OLS vs Theil-Sen trend estimation time series comparison
  - Search (scholarly): trend slope estimation small sample time series
  - Fetch 2-3 relevant papers.
  - Extract via fetch_grep:
    - When to use Theil-Sen vs. OLS for trend estimation
    - Minimum sample size requirements
    - Robustness to outliers (important for monthly data with zero-activity months)
    - Implementation in Python (scipy.stats.theilsen)

  ### Step 4.2: Change-point detection for cliff events
  - Search (scholarly): change point detection abrupt transition time series
  - Search (scholarly): ruptures Python change point detection
  - Search (scholarly): binary segmentation change point detection
  - Search (scholarly): PELT change point detection algorithm
  - Fetch and extract:
    - Available algorithms: Binary Segmentation, PELT, Wild Binary Segmentation
    - How to detect a single abrupt drop (cliff) vs. gradual decline
    - Python libraries: ruptures, spts, changepoint
    - Minimum signal length requirements
    - How to quantify abruptness of a change point

  ### Step 4.3: Convexity and curvature analysis
  - Search (scholarly): convexity concavity time series quadratic fit
  - Search (scholarly): second derivative time series curvature analysis
  - Search (scholarly): trajectory shape classification convex concave linear
  - Fetch and extract:
    - Methods for measuring convexity/concavity of a trajectory
    - Quadratic fit: how to interpret the quadratic coefficient
    - Discrete second derivative for noisy data
    - Connection to scaffolding fade shape (concave = accelerating fade, convex = decelerating fade)

  ### Step 4.4: Plateau detection
  - Search (scholarly): plateau detection time series flat region
  - Search (scholarly): detecting stationary periods time series
  - Search (scholarly): run test stationarity time series
  - Fetch and extract:
    - Methods for detecting extended flat regions (plateaus)
    - Statistical tests for stationarity in sub-segments
    - How to define plateau-then-cliff pattern quantitatively

  ### Step 4.5: Half-life and decay rate analysis
  - Search (scholarly): half-life decay rate time series analysis
  - Search (scholarly): exponential decay fitting time series involvement
  - Search (scholarly): time-to-onset decline detection
  - Fetch and extract:
    - How to estimate half-life of involvement decline
    - Exponential decay fitting: when appropriate, how to implement
    - Detecting the onset of decline (when does the fade begin?)

  ### Step 4.6: Scaffolding theory and fading index operationalization
  - Search (scholarly): scaffolding fading index educational psychology operationalization
  - Search (scholarly): Vygotsky scaffolding fading measurement quantitative
  - Search (scholarly): Wood Bruner Ross scaffolding fading operationalization
  - Search (scholarly): teacher support withdrawal trajectory measurement
  - Fetch and extract:
    - Has anyone quantified fading in educational settings?
    - Any existing fading index or withdrawal index from psychology literature?
    - How do they measure the smoothness of support withdrawal?
    - Connection between fade smoothness and learner outcomes

  ### Step 4.7: Composite index construction
  - Search (scholarly): composite index construction time series features
  - Search (scholarly): normalizing multiple features bounded index 0 to 1
  - Fetch and extract:
    - Methods for combining multiple shape descriptors into a single bounded index
    - Normalization techniques (min-max, z-score, rank-based)
    - Weighting schemes for composite indices

  ### Step 4.8: Synthesis for Area 4
  - Recommend a concrete feature extraction pipeline:
    1. Input: per-month founder involvement share (0-1) over project lifespan
    2. Feature 1: Linear slope (Theil-Sen estimator)
    3. Feature 2: Convexity (quadratic coefficient from polynomial fit)
    4. Feature 3: Time-to-onset-of-decline (change-point detection)
    5. Feature 4: Abrupt-cliff indicator (binary: largest single-month drop exceeds threshold)
    6. Feature 5: Plateau-then-cliff indicator (binary: extended flat region followed by cliff)
    7. Feature 6: Composite fade index (0-1, combining smoothness and gradualness)
  - Provide Python library recommendations for each feature
  - Flag validity concerns: small sample sizes, noisy monthly data, edge cases

  ---

  ## FINAL SYNTHESIS AND REPORT STRUCTURE

  After completing all four areas, produce a structured report (research_report.md) with:

  1. Executive Summary: One-page overview of key findings and recommendations
  2. Area 1 Report: Survival measurement - recommended definition, rationale, trade-offs
  3. Area 2 Report: Founder identification - recommended protocol, edge cases, reliability
  4. Area 3 Report: Data sources - ranked list with access details, cost estimates, feasibility
  5. Area 4 Report: Trajectory features - recommended feature extraction pipeline with Python libraries
  6. Validity Threats Matrix: Ranked list of all validity concerns with proposed mitigations:
     - Founder misidentification
     - Survival label ambiguity
     - Bus-factor confound with moderate fade
     - Project age confound (older projects have more time to fade)
     - Popularity confound (popular projects attract more contributors regardless of fade)
     - Small sample size for departed-founder cohort
     - Selection bias (only public GitHub projects)
     - Founder re-engagement (founder returns after departure)
     - Multi-founder projects
  7. Recommended Next Steps: Concrete action items for the next phase (data collection)
  8. Bibliography: Complete list of all sources with citations

  ## OUTPUT FORMAT

  Produce two files:
  1. research_out.json: Structured JSON with answer, sources, follow_up_questions
     - answer: synthesized findings for each area
     - sources: list of all papers/sources with URLs and key findings
     - follow_up_questions: open questions that need resolution before data collection
  2. research_report.md: Full structured report as described above

  ## TIME BUDGET (3 hours total)
  - Area 1 (Survival measurement): 45 minutes
  - Area 2 (Founder identification): 30 minutes
  - Area 3 (Data sources): 45 minutes
  - Area 4 (Trajectory features): 45 minutes
  - Final synthesis and report writing: 15 minutes

  ## BUDGET CONSTRAINTS
  - Web search and fetch are free (keyless engines)
  - No code execution needed - pure research
  - Focus on quality of synthesis over quantity of sources
  - Prioritize fetching full PDFs of the 6 key papers from the hypothesis (Avelino 2019, Chen ICSE 2026, Kaushik and Chahal 2026, Karim et al. 2026, Noori et al. 2025, and one scaffolding theory paper)

  ## FAILURE SCENARIOS AND MITIGATIONS
  - If a key paper is not findable: Search by author name + topic keywords; try arXiv directly; look for preprint versions; note the gap in the report
  - If PDF fetch fails: Try the HTML abstract page; use fetch_grep on the abstract to get key details; note limitations
  - If data source is no longer available: Find alternatives; note the change; recommend the next best option
  - If trajectory methods are too complex for our data: Simplify to the most robust features (slope + cliff indicator) and note the trade-off
  - If cohort size estimates are too small: Recommend broader inclusion criteria or alternative data sources
explanation: >-
  This research is the foundational literature survey for the Founder Fade Curve hypothesis. Before any data collection or
  experiment, we must ground our methodology in established work: adopt the right survival definition from Avelino et al.
  (2019) and newer 2025-2026 studies, identify reliable founder-detection methods, select feasible data sources within our
  budget constraints, and choose validated trajectory-shape descriptors. The survey will produce concrete operational definitions,
  a ranked list of data sources with access details, recommended feature extraction methods, and a thorough list of validity
  threats with mitigations.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-20 20:39:29 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [5] SYSTEM-USER prompt · 2026-08-20 20:41:41 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST N
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_resea
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: 'Literature Survey: Founder Fade & OSS Survival'
summary: >-
  Comprehensive literature survey across four areas to ground the Founder Fade Curve hypothesis in existing methods, data
  sources, and analytical techniques.
runpod_compute_profile: cpu_light
question: >-
  What does the existing literature tell us about (1) how OSS project survival after founder departure is measured, (2) how
  to reliably identify founders from git history, (3) what large-scale GitHub data sources are available for building a departed-founder
  cohort, and (4) how to quantify trajectory shape descriptors from time-series involvement data?
research_plan: |-
  ## OVERALL STRATEGY

  Conduct systematic web and scholarly research across FOUR areas. For each area: (a) run targeted scholarly searches to find primary papers, (b) fetch full papers (PDFs via arXiv or journal pages) for methodological detail, (c) use fetch_grep to extract exact numbers, definitions, and methodology sections, (d) synthesize into a structured report with concrete recommendations.

  Work through areas sequentially within each batch but parallelize independent searches.

  ---

  ## AREA 1: OSS Project Abandonment and Survival Measurement

  Goal: Establish the best survival/abandonment definition for cohort labeling, understand strengths/weaknesses of each approach, and decide which to adopt.

  ### Step 1.1: Find and read Avelino et al. (2019)
  - Search (scholarly): Avelino Constantinou Valente Serebrenik 2019 abandonment survival open source truck factor
  - Search (scholarly): truck-factor-developer detachment TFDD surviving system Avelino
  - Fetch the full PDF (likely at arXiv or journal page). Use fetch_grep to extract:
    - Exact definition of truck-factor developer and how they identify them
    - The TFDD event definition and inactivity threshold (how many months?)
    - The surviving system criterion: what exactly counts as survival?
    - The static features they tested and their predictive power (AUC, accuracy, effect sizes)
    - Sample size: how many projects? What repositories? What time window?
    - Any discussion of limitations, especially around snapshot vs. dynamic measures

  ### Step 1.2: Find and read Chen et al. (ICSE 2026)
  - Search (scholarly): Chen Stol Santos German Trinkenreich 2026 core contributor disengagement open source ICSE
  - Search (scholarly): core contributor disengagement open source difference-in-differences 2026
  - Fetch the full PDF (ICSE 2026 proceedings, likely on IEEE Xplore or arXiv).
  - Extract via fetch_grep:
    - How they define core contributor disengagement and the inactivity threshold
    - The quasi-experimental design: DiD setup, treatment vs. control, 50,804 repositories
    - Outcome measures: PR throughput, acceptance rate, merge time
    - Static contributor profile features (commit-share, tenure) and their findings
    - Any discussion of founder vs. non-founder effects
    - Limitations and future work that might relate to our trajectory approach

  ### Step 1.3: Find and read Kaushik and Chahal (2026)
  - Search (scholarly): Kaushik Chahal 2026 death spiral open source pull request workflow
  - Search (scholarly): death spiral open source projects pull request friction backlog 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - How they define inactive vs active projects
    - The death spiral signals: friction, backlog growth, falling innovation, rising merge latency
    - Their finding that popularity/innovation are causes of survival while workflow friction is a byproduct
    - Aggregate community-level dynamics vs. founder-specific analysis
    - Time windows and thresholds used

  ### Step 1.4: Find and read Karim et al. (2026)
  - Search (scholarly): Karim Lu Kasaadha Goggins 2026 predicting open source sustainability deep temporal hierarchical
  - Search (scholarly): predicting open source sustainability transformer temporal architecture 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - The hierarchical Transformer model architecture
    - 24-month aggregate activity sequences: what features, how computed
    - Lifecycle stage classification: what stages, how labeled
    - Performance metrics and baselines
    - Whether they mention founders, succession, or individual developer trajectories

  ### Step 1.5: Find and read Noori et al. (2025)
  - Search (scholarly): Noori Chakraborti Zhang Frey 2025 founder leadership community governance open source
  - Search (scholarly): governance.md textual governance evolution open source 2025
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - NLP pipeline for governance.md analysis: roles, actions, deontics
    - 637 repositories: selection criteria
    - How they characterize institutional maturation
    - Connection between governance text and actual project survival

  ### Step 1.6: Broader survival measurement survey
  - Search (scholarly): open source project abandonment definition criteria survey 2020 2021 2022 2023 2024
  - Search (scholarly): OSS project survival prediction machine learning review
  - Search (scholarly): abandoned open source projects GitHub empirical study
  - Fetch 2-3 of the most relevant papers to understand the landscape of survival definitions.
  - Extract: Alternative survival definitions and their trade-offs.

  ### Step 1.7: Synthesis for Area 1
  - Compare all survival definitions: which is most rigorous, most reproducible, best suited for our hypothesis?
  - Recommend a primary survival label (binary) and a continuous survival metric.
  - Flag validity concerns: does the Avelino criterion miss projects that survive without new truck-factor developers? Does a 12-month inactivity window capture all departures?

  ---

  ## AREA 2: Founder Identification and Key-Developer Attribution

  Goal: Find reliable methods for identifying the founder from git history, handling edge cases (email aliases, organizational accounts, multi-founder projects).

  ### Step 2.1: Search for founder identification methods
  - Search (scholarly): founder identification git history open source project creator
  - Search (scholarly): key developer identification open source contribution analysis
  - Search (scholarly): truck factor calculation methodology Cosentino
  - Search (scholarly): developer identity resolution email alias merging git
  - Fetch 3-5 most relevant papers.

  ### Step 2.2: Extract founder identification methodologies
  - For each relevant paper, use fetch_grep to extract:
    - How they define and identify the founder or principal early developer
    - Methods for handling multiple email addresses per developer
    - How they separate founders from other early key contributors
    - Reliability metrics: how often does the method misidentify?
    - Edge cases handled: organizational accounts, multi-founder repos, repos with early forking

  ### Step 2.3: Search for identity resolution tools
  - Search (general): git author email alias resolution tool
  - Search (general): GitHub contributor identity merging algorithm
  - Search (scholarly): software developer identity resolution empirical study
  - Fetch and extract: Available tools and their accuracy.

  ### Step 2.4: Search for multi-founder and organizational account handling
  - Search (scholarly): multi-founder open source project identification
  - Search (scholarly): organizational account bot detection GitHub commits
  - Fetch and extract: Methods for detecting and handling these edge cases.

  ### Step 2.5: Synthesis for Area 2
  - Recommend a concrete founder identification protocol:
    - Primary method: earliest sustained commit/merge activity + repository creator
    - Fallback: manual verification for ambiguous cases
    - Email alias merging strategy
    - Edge case handling rules (org accounts, bots, multi-founder)
  - Flag validity threats: founder misidentification rate, impact on trajectory shape

  ---

  ## AREA 3: Available Large-Scale GitHub Data Sources

  Goal: Identify feasible data sources for building a departed-founder cohort, including access methods, rate limits, costs, and extraction strategies.

  ### Step 3.1: GHTorrent dataset
  - Search (scholarly): GHTorrent dataset GitHub repository mining 2024 2025
  - Search (general): GHTorrent current status 2024 2025 download
  - Search (general): GHTorrent MongoDB schema repository commits pulls
  - Fetch the GHTorrent website (ghtorrent.org) and any recent papers about it.
  - Extract via fetch_grep:
    - Current status: is it still maintained? Last update date?
    - Data coverage: how many repositories? What time range?
    - Schema: what fields are available for commits, pulls, reviews, authors?
    - Download method and size
    - Known limitations (incomplete data, missing fields)

  ### Step 3.2: GH Archive and Google BigQuery
  - Search (general): GH Archive Google BigQuery public dataset GitHub events 2024 2025
  - Search (general): bigquery publicdata github archives schema
  - Search (scholarly): using Google BigQuery GitHub data open source research
  - Fetch the GH Archive website (www.gharchive.org) and BigQuery documentation.
  - Extract via fetch_grep:
    - Available event types: PushEvent, PullRequestEvent, IssuesEvent, etc.
    - Time coverage and granularity
    - Query costs and free tier limits
    - Rate limits and best practices for large queries
    - Can we get per-author per-month commit counts from BigQuery?

  ### Step 3.3: GitHub REST and GraphQL APIs
  - Search (general): GitHub REST API rate limiting best practices 2024 2025
  - Search (general): GitHub GraphQL API commits pulls reviews pagination
  - Search (general): GitHub API token authentication rate limit increase
  - Fetch GitHub API documentation pages.
  - Extract via fetch_grep:
    - REST API rate limits: unauthenticated vs. authenticated (token)
    - GraphQL API rate limits: node-based throttling
    - Pagination strategies for large repositories
    - Available endpoints for: commits (author, date), pull requests (merged_by, reviews), code reviews (state, user)
    - Can we get the founder share of merges/reviews per month?
    - Cost of API tokens (free tier limits)

  ### Step 3.4: Direct git-log parsing
  - Search (general): git log parse author date commit count per month
  - Search (scholarly): git history mining open source project analysis methodology
  - Fetch and extract: Best practices for cloning and parsing git history at scale.

  ### Step 3.5: Published OSS dataset curation methodologies
  - Search (scholarly): open source repository dataset curation methodology GitHub
  - Search (scholarly): building cohort abandoned open source projects GitHub
  - Fetch 2-3 relevant papers.
  - Extract: How previous studies built their cohorts: selection criteria, sampling strategy, data collection pipeline.

  ### Step 3.6: Synthesis for Area 3
  - Rank data sources by feasibility for our specific needs:
    1. Can we get per-author per-month commit/merge/review shares?
    2. Can we identify projects where the founder departed?
    3. What is the cost (time, money, infrastructure)?
    4. What is the maximum cohort size feasible within budget?
  - Recommend a primary data source + fallback strategy.
  - Provide concrete access details: URLs, API endpoints, authentication requirements, estimated costs.

  ---

  ## AREA 4: Trajectory Shape Analysis and Quantitative Curve Classification

  Goal: Find validated methods for converting a per-month involvement-share time series into the required descriptors: slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator, and a bounded 0-1 fade index.

  ### Step 4.1: Trend estimation methods
  - Search (scholarly): Theil-Sen estimator trend detection time series robust
  - Search (scholarly): OLS vs Theil-Sen trend estimation time series comparison
  - Search (scholarly): trend slope estimation small sample time series
  - Fetch 2-3 relevant papers.
  - Extract via fetch_grep:
    - When to use Theil-Sen vs. OLS for trend estimation
    - Minimum sample size requirements
    - Robustness to outliers (important for monthly data with zero-activity months)
    - Implementation in Python (scipy.stats.theilsen)

  ### Step 4.2: Change-point detection for cliff events
  - Search (scholarly): change point detection abrupt transition time series
  - Search (scholarly): ruptures Python change point detection
  - Search (scholarly): binary segmentation change point detection
  - Search (scholarly): PELT change point detection algorithm
  - Fetch and extract:
    - Available algorithms: Binary Segmentation, PELT, Wild Binary Segmentation
    - How to detect a single abrupt drop (cliff) vs. gradual decline
    - Python libraries: ruptures, spts, changepoint
    - Minimum signal length requirements
    - How to quantify abruptness of a change point

  ### Step 4.3: Convexity and curvature analysis
  - Search (scholarly): convexity concavity time series quadratic fit
  - Search (scholarly): second derivative time series curvature analysis
  - Search (scholarly): trajectory shape classification convex concave linear
  - Fetch and extract:
    - Methods for measuring convexity/concavity of a trajectory
    - Quadratic fit: how to interpret the quadratic coefficient
    - Discrete second derivative for noisy data
    - Connection to scaffolding fade shape (concave = accelerating fade, convex = decelerating fade)

  ### Step 4.4: Plateau detection
  - Search (scholarly): plateau detection time series flat region
  - Search (scholarly): detecting stationary periods time series
  - Search (scholarly): run test stationarity time series
  - Fetch and extract:
    - Methods for detecting extended flat regions (plateaus)
    - Statistical tests for stationarity in sub-segments
    - How to define plateau-then-cliff pattern quantitatively

  ### Step 4.5: Half-life and decay rate analysis
  - Search (scholarly): half-life decay rate time series analysis
  - Search (scholarly): exponential decay fitting time series involvement
  - Search (scholarly): time-to-onset decline detection
  - Fetch and extract:
    - How to estimate half-life of involvement decline
    - Exponential decay fitting: when appropriate, how to implement
    - Detecting the onset of decline (when does the fade begin?)

  ### Step 4.6: Scaffolding theory and fading index operationalization
  - Search (scholarly): scaffolding fading index educational psychology operationalization
  - Search (scholarly): Vygotsky scaffolding fading measurement quantitative
  - Search (scholarly): Wood Bruner Ross scaffolding fading operationalization
  - Search (scholarly): teacher support withdrawal trajectory measurement
  - Fetch and extract:
    - Has anyone quantified fading in educational settings?
    - Any existing fading index or withdrawal index from psychology literature?
    - How do they measure the smoothness of support withdrawal?
    - Connection between fade smoothness and learner outcomes

  ### Step 4.7: Composite index construction
  - Search (scholarly): composite index construction time series features
  - Search (scholarly): normalizing multiple features bounded index 0 to 1
  - Fetch and extract:
    - Methods for combining multiple shape descriptors into a single bounded index
    - Normalization techniques (min-max, z-score, rank-based)
    - Weighting schemes for composite indices

  ### Step 4.8: Synthesis for Area 4
  - Recommend a concrete feature extraction pipeline:
    1. Input: per-month founder involvement share (0-1) over project lifespan
    2. Feature 1: Linear slope (Theil-Sen estimator)
    3. Feature 2: Convexity (quadratic coefficient from polynomial fit)
    4. Feature 3: Time-to-onset-of-decline (change-point detection)
    5. Feature 4: Abrupt-cliff indicator (binary: largest single-month drop exceeds threshold)
    6. Feature 5: Plateau-then-cliff indicator (binary: extended flat region followed by cliff)
    7. Feature 6: Composite fade index (0-1, combining smoothness and gradualness)
  - Provide Python library recommendations for each feature
  - Flag validity concerns: small sample sizes, noisy monthly data, edge cases

  ---

  ## FINAL SYNTHESIS AND REPORT STRUCTURE

  After completing all four areas, produce a structured report (research_report.md) with:

  1. Executive Summary: One-page overview of key findings and recommendations
  2. Area 1 Report: Survival measurement - recommended definition, rationale, trade-offs
  3. Area 2 Report: Founder identification - recommended protocol, edge cases, reliability
  4. Area 3 Report: Data sources - ranked list with access details, cost estimates, feasibility
  5. Area 4 Report: Trajectory features - recommended feature extraction pipeline with Python libraries
  6. Validity Threats Matrix: Ranked list of all validity concerns with proposed mitigations:
     - Founder misidentification
     - Survival label ambiguity
     - Bus-factor confound with moderate fade
     - Project age confound (older projects have more time to fade)
     - Popularity confound (popular projects attract more contributors regardless of fade)
     - Small sample size for departed-founder cohort
     - Selection bias (only public GitHub projects)
     - Founder re-engagement (founder returns after departure)
     - Multi-founder projects
  7. Recommended Next Steps: Concrete action items for the next phase (data collection)
  8. Bibliography: Complete list of all sources with citations

  ## OUTPUT FORMAT

  Produce two files:
  1. research_out.json: Structured JSON with answer, sources, follow_up_questions
     - answer: synthesized findings for each area
     - sources: list of all papers/sources with URLs and key findings
     - follow_up_questions: open questions that need resolution before data collection
  2. research_report.md: Full structured report as described above

  ## TIME BUDGET (3 hours total)
  - Area 1 (Survival measurement): 45 minutes
  - Area 2 (Founder identification): 30 minutes
  - Area 3 (Data sources): 45 minutes
  - Area 4 (Trajectory features): 45 minutes
  - Final synthesis and report writing: 15 minutes

  ## BUDGET CONSTRAINTS
  - Web search and fetch are free (keyless engines)
  - No code execution needed - pure research
  - Focus on quality of synthesis over quantity of sources
  - Prioritize fetching full PDFs of the 6 key papers from the hypothesis (Avelino 2019, Chen ICSE 2026, Kaushik and Chahal 2026, Karim et al. 2026, Noori et al. 2025, and one scaffolding theory paper)

  ## FAILURE SCENARIOS AND MITIGATIONS
  - If a key paper is not findable: Search by author name + topic keywords; try arXiv directly; look for preprint versions; note the gap in the report
  - If PDF fetch fails: Try the HTML abstract page; use fetch_grep on the abstract to get key details; note limitations
  - If data source is no longer available: Find alternatives; note the change; recommend the next best option
  - If trajectory methods are too complex for our data: Simplify to the most robust features (slope + cliff indicator) and note the trade-off
  - If cohort size estimates are too small: Recommend broader inclusion criteria or alternative data sources
explanation: >-
  This research is the foundational literature survey for the Founder Fade Curve hypothesis. Before any data collection or
  experiment, we must ground our methodology in established work: adopt the right survival definition from Avelino et al.
  (2019) and newer 2025-2026 studies, identify reliable founder-detection methods, select feasible data sources within our
  budget constraints, and choose validated trajectory-shape descriptors. The survey will produce concrete operational definitions,
  a ranked list of data sources with access details, recommended feature extraction methods, and a thorough list of validity
  threats with mitigations.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [6] HUMAN-USER prompt · 2026-08-20 20:41:41 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [7] SYSTEM-USER prompt · 2026-08-20 20:43:52 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST N
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_resea
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]
  - [agent_system_user_prompt]: PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_resea
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>
<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for prior work and the field's landscape to ground your research.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<artifact_plan>
id: gen_plan_research_1_idx1
type: research
title: 'Literature Survey: Founder Fade & OSS Survival'
summary: >-
  Comprehensive literature survey across four areas to ground the Founder Fade Curve hypothesis in existing methods, data
  sources, and analytical techniques.
runpod_compute_profile: cpu_light
question: >-
  What does the existing literature tell us about (1) how OSS project survival after founder departure is measured, (2) how
  to reliably identify founders from git history, (3) what large-scale GitHub data sources are available for building a departed-founder
  cohort, and (4) how to quantify trajectory shape descriptors from time-series involvement data?
research_plan: |-
  ## OVERALL STRATEGY

  Conduct systematic web and scholarly research across FOUR areas. For each area: (a) run targeted scholarly searches to find primary papers, (b) fetch full papers (PDFs via arXiv or journal pages) for methodological detail, (c) use fetch_grep to extract exact numbers, definitions, and methodology sections, (d) synthesize into a structured report with concrete recommendations.

  Work through areas sequentially within each batch but parallelize independent searches.

  ---

  ## AREA 1: OSS Project Abandonment and Survival Measurement

  Goal: Establish the best survival/abandonment definition for cohort labeling, understand strengths/weaknesses of each approach, and decide which to adopt.

  ### Step 1.1: Find and read Avelino et al. (2019)
  - Search (scholarly): Avelino Constantinou Valente Serebrenik 2019 abandonment survival open source truck factor
  - Search (scholarly): truck-factor-developer detachment TFDD surviving system Avelino
  - Fetch the full PDF (likely at arXiv or journal page). Use fetch_grep to extract:
    - Exact definition of truck-factor developer and how they identify them
    - The TFDD event definition and inactivity threshold (how many months?)
    - The surviving system criterion: what exactly counts as survival?
    - The static features they tested and their predictive power (AUC, accuracy, effect sizes)
    - Sample size: how many projects? What repositories? What time window?
    - Any discussion of limitations, especially around snapshot vs. dynamic measures

  ### Step 1.2: Find and read Chen et al. (ICSE 2026)
  - Search (scholarly): Chen Stol Santos German Trinkenreich 2026 core contributor disengagement open source ICSE
  - Search (scholarly): core contributor disengagement open source difference-in-differences 2026
  - Fetch the full PDF (ICSE 2026 proceedings, likely on IEEE Xplore or arXiv).
  - Extract via fetch_grep:
    - How they define core contributor disengagement and the inactivity threshold
    - The quasi-experimental design: DiD setup, treatment vs. control, 50,804 repositories
    - Outcome measures: PR throughput, acceptance rate, merge time
    - Static contributor profile features (commit-share, tenure) and their findings
    - Any discussion of founder vs. non-founder effects
    - Limitations and future work that might relate to our trajectory approach

  ### Step 1.3: Find and read Kaushik and Chahal (2026)
  - Search (scholarly): Kaushik Chahal 2026 death spiral open source pull request workflow
  - Search (scholarly): death spiral open source projects pull request friction backlog 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - How they define inactive vs active projects
    - The death spiral signals: friction, backlog growth, falling innovation, rising merge latency
    - Their finding that popularity/innovation are causes of survival while workflow friction is a byproduct
    - Aggregate community-level dynamics vs. founder-specific analysis
    - Time windows and thresholds used

  ### Step 1.4: Find and read Karim et al. (2026)
  - Search (scholarly): Karim Lu Kasaadha Goggins 2026 predicting open source sustainability deep temporal hierarchical
  - Search (scholarly): predicting open source sustainability transformer temporal architecture 2026
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - The hierarchical Transformer model architecture
    - 24-month aggregate activity sequences: what features, how computed
    - Lifecycle stage classification: what stages, how labeled
    - Performance metrics and baselines
    - Whether they mention founders, succession, or individual developer trajectories

  ### Step 1.5: Find and read Noori et al. (2025)
  - Search (scholarly): Noori Chakraborti Zhang Frey 2025 founder leadership community governance open source
  - Search (scholarly): governance.md textual governance evolution open source 2025
  - Fetch the full PDF.
  - Extract via fetch_grep:
    - NLP pipeline for governance.md analysis: roles, actions, deontics
    - 637 repositories: selection criteria
    - How they characterize institutional maturation
    - Connection between governance text and actual project survival

  ### Step 1.6: Broader survival measurement survey
  - Search (scholarly): open source project abandonment definition criteria survey 2020 2021 2022 2023 2024
  - Search (scholarly): OSS project survival prediction machine learning review
  - Search (scholarly): abandoned open source projects GitHub empirical study
  - Fetch 2-3 of the most relevant papers to understand the landscape of survival definitions.
  - Extract: Alternative survival definitions and their trade-offs.

  ### Step 1.7: Synthesis for Area 1
  - Compare all survival definitions: which is most rigorous, most reproducible, best suited for our hypothesis?
  - Recommend a primary survival label (binary) and a continuous survival metric.
  - Flag validity concerns: does the Avelino criterion miss projects that survive without new truck-factor developers? Does a 12-month inactivity window capture all departures?

  ---

  ## AREA 2: Founder Identification and Key-Developer Attribution

  Goal: Find reliable methods for identifying the founder from git history, handling edge cases (email aliases, organizational accounts, multi-founder projects).

  ### Step 2.1: Search for founder identification methods
  - Search (scholarly): founder identification git history open source project creator
  - Search (scholarly): key developer identification open source contribution analysis
  - Search (scholarly): truck factor calculation methodology Cosentino
  - Search (scholarly): developer identity resolution email alias merging git
  - Fetch 3-5 most relevant papers.

  ### Step 2.2: Extract founder identification methodologies
  - For each relevant paper, use fetch_grep to extract:
    - How they define and identify the founder or principal early developer
    - Methods for handling multiple email addresses per developer
    - How they separate founders from other early key contributors
    - Reliability metrics: how often does the method misidentify?
    - Edge cases handled: organizational accounts, multi-founder repos, repos with early forking

  ### Step 2.3: Search for identity resolution tools
  - Search (general): git author email alias resolution tool
  - Search (general): GitHub contributor identity merging algorithm
  - Search (scholarly): software developer identity resolution empirical study
  - Fetch and extract: Available tools and their accuracy.

  ### Step 2.4: Search for multi-founder and organizational account handling
  - Search (scholarly): multi-founder open source project identification
  - Search (scholarly): organizational account bot detection GitHub commits
  - Fetch and extract: Methods for detecting and handling these edge cases.

  ### Step 2.5: Synthesis for Area 2
  - Recommend a concrete founder identification protocol:
    - Primary method: earliest sustained commit/merge activity + repository creator
    - Fallback: manual verification for ambiguous cases
    - Email alias merging strategy
    - Edge case handling rules (org accounts, bots, multi-founder)
  - Flag validity threats: founder misidentification rate, impact on trajectory shape

  ---

  ## AREA 3: Available Large-Scale GitHub Data Sources

  Goal: Identify feasible data sources for building a departed-founder cohort, including access methods, rate limits, costs, and extraction strategies.

  ### Step 3.1: GHTorrent dataset
  - Search (scholarly): GHTorrent dataset GitHub repository mining 2024 2025
  - Search (general): GHTorrent current status 2024 2025 download
  - Search (general): GHTorrent MongoDB schema repository commits pulls
  - Fetch the GHTorrent website (ghtorrent.org) and any recent papers about it.
  - Extract via fetch_grep:
    - Current status: is it still maintained? Last update date?
    - Data coverage: how many repositories? What time range?
    - Schema: what fields are available for commits, pulls, reviews, authors?
    - Download method and size
    - Known limitations (incomplete data, missing fields)

  ### Step 3.2: GH Archive and Google BigQuery
  - Search (general): GH Archive Google BigQuery public dataset GitHub events 2024 2025
  - Search (general): bigquery publicdata github archives schema
  - Search (scholarly): using Google BigQuery GitHub data open source research
  - Fetch the GH Archive website (www.gharchive.org) and BigQuery documentation.
  - Extract via fetch_grep:
    - Available event types: PushEvent, PullRequestEvent, IssuesEvent, etc.
    - Time coverage and granularity
    - Query costs and free tier limits
    - Rate limits and best practices for large queries
    - Can we get per-author per-month commit counts from BigQuery?

  ### Step 3.3: GitHub REST and GraphQL APIs
  - Search (general): GitHub REST API rate limiting best practices 2024 2025
  - Search (general): GitHub GraphQL API commits pulls reviews pagination
  - Search (general): GitHub API token authentication rate limit increase
  - Fetch GitHub API documentation pages.
  - Extract via fetch_grep:
    - REST API rate limits: unauthenticated vs. authenticated (token)
    - GraphQL API rate limits: node-based throttling
    - Pagination strategies for large repositories
    - Available endpoints for: commits (author, date), pull requests (merged_by, reviews), code reviews (state, user)
    - Can we get the founder share of merges/reviews per month?
    - Cost of API tokens (free tier limits)

  ### Step 3.4: Direct git-log parsing
  - Search (general): git log parse author date commit count per month
  - Search (scholarly): git history mining open source project analysis methodology
  - Fetch and extract: Best practices for cloning and parsing git history at scale.

  ### Step 3.5: Published OSS dataset curation methodologies
  - Search (scholarly): open source repository dataset curation methodology GitHub
  - Search (scholarly): building cohort abandoned open source projects GitHub
  - Fetch 2-3 relevant papers.
  - Extract: How previous studies built their cohorts: selection criteria, sampling strategy, data collection pipeline.

  ### Step 3.6: Synthesis for Area 3
  - Rank data sources by feasibility for our specific needs:
    1. Can we get per-author per-month commit/merge/review shares?
    2. Can we identify projects where the founder departed?
    3. What is the cost (time, money, infrastructure)?
    4. What is the maximum cohort size feasible within budget?
  - Recommend a primary data source + fallback strategy.
  - Provide concrete access details: URLs, API endpoints, authentication requirements, estimated costs.

  ---

  ## AREA 4: Trajectory Shape Analysis and Quantitative Curve Classification

  Goal: Find validated methods for converting a per-month involvement-share time series into the required descriptors: slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator, and a bounded 0-1 fade index.

  ### Step 4.1: Trend estimation methods
  - Search (scholarly): Theil-Sen estimator trend detection time series robust
  - Search (scholarly): OLS vs Theil-Sen trend estimation time series comparison
  - Search (scholarly): trend slope estimation small sample time series
  - Fetch 2-3 relevant papers.
  - Extract via fetch_grep:
    - When to use Theil-Sen vs. OLS for trend estimation
    - Minimum sample size requirements
    - Robustness to outliers (important for monthly data with zero-activity months)
    - Implementation in Python (scipy.stats.theilsen)

  ### Step 4.2: Change-point detection for cliff events
  - Search (scholarly): change point detection abrupt transition time series
  - Search (scholarly): ruptures Python change point detection
  - Search (scholarly): binary segmentation change point detection
  - Search (scholarly): PELT change point detection algorithm
  - Fetch and extract:
    - Available algorithms: Binary Segmentation, PELT, Wild Binary Segmentation
    - How to detect a single abrupt drop (cliff) vs. gradual decline
    - Python libraries: ruptures, spts, changepoint
    - Minimum signal length requirements
    - How to quantify abruptness of a change point

  ### Step 4.3: Convexity and curvature analysis
  - Search (scholarly): convexity concavity time series quadratic fit
  - Search (scholarly): second derivative time series curvature analysis
  - Search (scholarly): trajectory shape classification convex concave linear
  - Fetch and extract:
    - Methods for measuring convexity/concavity of a trajectory
    - Quadratic fit: how to interpret the quadratic coefficient
    - Discrete second derivative for noisy data
    - Connection to scaffolding fade shape (concave = accelerating fade, convex = decelerating fade)

  ### Step 4.4: Plateau detection
  - Search (scholarly): plateau detection time series flat region
  - Search (scholarly): detecting stationary periods time series
  - Search (scholarly): run test stationarity time series
  - Fetch and extract:
    - Methods for detecting extended flat regions (plateaus)
    - Statistical tests for stationarity in sub-segments
    - How to define plateau-then-cliff pattern quantitatively

  ### Step 4.5: Half-life and decay rate analysis
  - Search (scholarly): half-life decay rate time series analysis
  - Search (scholarly): exponential decay fitting time series involvement
  - Search (scholarly): time-to-onset decline detection
  - Fetch and extract:
    - How to estimate half-life of involvement decline
    - Exponential decay fitting: when appropriate, how to implement
    - Detecting the onset of decline (when does the fade begin?)

  ### Step 4.6: Scaffolding theory and fading index operationalization
  - Search (scholarly): scaffolding fading index educational psychology operationalization
  - Search (scholarly): Vygotsky scaffolding fading measurement quantitative
  - Search (scholarly): Wood Bruner Ross scaffolding fading operationalization
  - Search (scholarly): teacher support withdrawal trajectory measurement
  - Fetch and extract:
    - Has anyone quantified fading in educational settings?
    - Any existing fading index or withdrawal index from psychology literature?
    - How do they measure the smoothness of support withdrawal?
    - Connection between fade smoothness and learner outcomes

  ### Step 4.7: Composite index construction
  - Search (scholarly): composite index construction time series features
  - Search (scholarly): normalizing multiple features bounded index 0 to 1
  - Fetch and extract:
    - Methods for combining multiple shape descriptors into a single bounded index
    - Normalization techniques (min-max, z-score, rank-based)
    - Weighting schemes for composite indices

  ### Step 4.8: Synthesis for Area 4
  - Recommend a concrete feature extraction pipeline:
    1. Input: per-month founder involvement share (0-1) over project lifespan
    2. Feature 1: Linear slope (Theil-Sen estimator)
    3. Feature 2: Convexity (quadratic coefficient from polynomial fit)
    4. Feature 3: Time-to-onset-of-decline (change-point detection)
    5. Feature 4: Abrupt-cliff indicator (binary: largest single-month drop exceeds threshold)
    6. Feature 5: Plateau-then-cliff indicator (binary: extended flat region followed by cliff)
    7. Feature 6: Composite fade index (0-1, combining smoothness and gradualness)
  - Provide Python library recommendations for each feature
  - Flag validity concerns: small sample sizes, noisy monthly data, edge cases

  ---

  ## FINAL SYNTHESIS AND REPORT STRUCTURE

  After completing all four areas, produce a structured report (research_report.md) with:

  1. Executive Summary: One-page overview of key findings and recommendations
  2. Area 1 Report: Survival measurement - recommended definition, rationale, trade-offs
  3. Area 2 Report: Founder identification - recommended protocol, edge cases, reliability
  4. Area 3 Report: Data sources - ranked list with access details, cost estimates, feasibility
  5. Area 4 Report: Trajectory features - recommended feature extraction pipeline with Python libraries
  6. Validity Threats Matrix: Ranked list of all validity concerns with proposed mitigations:
     - Founder misidentification
     - Survival label ambiguity
     - Bus-factor confound with moderate fade
     - Project age confound (older projects have more time to fade)
     - Popularity confound (popular projects attract more contributors regardless of fade)
     - Small sample size for departed-founder cohort
     - Selection bias (only public GitHub projects)
     - Founder re-engagement (founder returns after departure)
     - Multi-founder projects
  7. Recommended Next Steps: Concrete action items for the next phase (data collection)
  8. Bibliography: Complete list of all sources with citations

  ## OUTPUT FORMAT

  Produce two files:
  1. research_out.json: Structured JSON with answer, sources, follow_up_questions
     - answer: synthesized findings for each area
     - sources: list of all papers/sources with URLs and key findings
     - follow_up_questions: open questions that need resolution before data collection
  2. research_report.md: Full structured report as described above

  ## TIME BUDGET (3 hours total)
  - Area 1 (Survival measurement): 45 minutes
  - Area 2 (Founder identification): 30 minutes
  - Area 3 (Data sources): 45 minutes
  - Area 4 (Trajectory features): 45 minutes
  - Final synthesis and report writing: 15 minutes

  ## BUDGET CONSTRAINTS
  - Web search and fetch are free (keyless engines)
  - No code execution needed - pure research
  - Focus on quality of synthesis over quantity of sources
  - Prioritize fetching full PDFs of the 6 key papers from the hypothesis (Avelino 2019, Chen ICSE 2026, Kaushik and Chahal 2026, Karim et al. 2026, Noori et al. 2025, and one scaffolding theory paper)

  ## FAILURE SCENARIOS AND MITIGATIONS
  - If a key paper is not findable: Search by author name + topic keywords; try arXiv directly; look for preprint versions; note the gap in the report
  - If PDF fetch fails: Try the HTML abstract page; use fetch_grep on the abstract to get key details; note limitations
  - If data source is no longer available: Find alternatives; note the change; recommend the next best option
  - If trajectory methods are too complex for our data: Simplify to the most robust features (slope + cliff indicator) and note the trade-off
  - If cohort size estimates are too small: Recommend broader inclusion criteria or alternative data sources
explanation: >-
  This research is the foundational literature survey for the Founder Fade Curve hypothesis. Before any data collection or
  experiment, we must ground our methodology in established work: adopt the right survival definition from Avelino et al.
  (2019) and newer 2025-2026 studies, identify reliable founder-detection methods, select feasible data sources within our
  budget constraints, and choose validated trajectory-shape descriptors. The survey will produce concrete operational definitions,
  a ranked list of data sources with access details, recommended feature extraction methods, and a thorough list of validity
  threats with mitigations.
</artifact_plan>

<investigation_process>
1. DIVERGE: Brainstorm multiple angles/framings of the question before searching. Think across fields — what adjacent domains might have relevant insights?
2. SEARCH: Multiple queries per angle with different phrasings to discover the landscape
3. FETCH: Read promising URLs at high level. Snippets are NOT enough — fetch full pages
4. DETAIL: aii-web-tools fetch_grep for specifics from key pages/PDFs
5. CONTRAST: Actively try to disprove your emerging conclusions. Search with different phrasings, "[topic] criticism", "[topic] limitations". Check across fields — the same finding may exist under different names
6. SYNTHESIZE: Integrate into balanced conclusion
7. ITERATE: Expect to repeat steps 2-6 if findings are incomplete or one-sided. Don't settle on first results
8. SUMMARIZE: Output JSON must include 'title' and 'summary' fields
</investigation_process>

<output_requirements>
- Write research_out.json to your workspace with all findings
- Provide your finding as clear prose WITH NUMBERED CITATIONS
- EVERY factual claim must have a citation number in brackets: [1], [2], [1, 3], etc.
- Include BOTH supporting AND contradicting evidence
- Be explicit about confidence level and what would change it
- End with follow-up questions for further investigation
</output_requirements>

<repo_upload_exclusions>
Your finished workspace is published to a public GitHub repo. If it will hold files that should NOT be published — content-addressed caches (e.g. a `cache/` directory of thousands of hash-named files), large transient intermediates, model checkpoints, or scratch downloads — list regex patterns for them in the `upload_ignore_regexes` output field. Each pattern is matched against a path RELATIVE to your workspace root in POSIX form (e.g. `(^|/)cache/`, `(^|/)checkpoints/`). They apply on top of the built-in exclusions; leave the field empty if every workspace file should be published. Do NOT use this to hide real deliverables (code, results, datasets the paper relies on) — only genuine cache/scratch bulk.
</repo_upload_exclusions>

Research everything specified in the artifact plan, but you may also investigate additional relevant aspects beyond what's listed. Investigate this question thoroughly.

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "ResearchExpectedFiles": {
      "description": "All expected output files from research artifact.",
      "properties": {
        "output": {
          "description": "Path to research output JSON. Example: 'research_out.json'",
          "title": "Output",
          "type": "string"
        }
      },
      "required": [
        "output"
      ],
      "title": "ResearchExpectedFiles",
      "type": "object"
    },
    "Source": {
      "description": "A source used in the research.",
      "properties": {
        "index": {
          "description": "Citation number (1, 2, 3, ...)",
          "title": "Index",
          "type": "integer"
        },
        "url": {
          "description": "Full URL of the source",
          "title": "Url",
          "type": "string"
        },
        "title": {
          "description": "Title of the article/page",
          "title": "Title",
          "type": "string"
        },
        "summary": {
          "description": "Brief summary of what this source contributed",
          "title": "Summary",
          "type": "string"
        }
      },
      "required": [
        "index",
        "url",
        "title",
        "summary"
      ],
      "title": "Source",
      "type": "object"
    }
  },
  "description": "Research artifact \u2014 structured output + file metadata.\n\nConducts thorough web research using the aii-web-tools skill.\nReturns structured JSON output with citations.",
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
      "$ref": "#/$defs/ResearchExpectedFiles",
      "description": "All output files you created. Must include research_out.json with your research findings."
    },
    "upload_ignore_regexes": {
      "description": "Regex patterns for workspace paths that must NOT be published to the GitHub repo, matched against each file's path relative to this artifact's workspace root (POSIX form, e.g. 'cache/abc.json'). Applied ON TOP OF the deploy step's built-in exclusions. Use this for executor-specific caches, large transient intermediates, or content-addressed blob stores (e.g. a cache/ dir of thousands of hash-named files) that would bloat the repo. Examples: ['(^|/)cache/', '(^|/)\\\\.weight_cache/', '(^|/)checkpoints/']. Leave empty if every workspace file should be published.",
      "items": {
        "type": "string"
      },
      "title": "Upload Ignore Regexes",
      "type": "array"
    },
    "answer": {
      "description": "Comprehensive answer with NUMBERED CITATIONS. Cite sources by number: 'Claim [1].' or 'According to [2, 3]...'",
      "title": "Answer",
      "type": "string"
    },
    "sources": {
      "description": "All sources used, with index matching citation numbers in answer",
      "items": {
        "$ref": "#/$defs/Source"
      },
      "title": "Sources",
      "type": "array"
    },
    "follow_up_questions": {
      "description": "2-3 follow-up questions that emerged from the investigation",
      "items": {
        "type": "string"
      },
      "title": "Follow Up Questions",
      "type": "array"
    }
  },
  "required": [
    "out_expected_files",
    "answer",
    "sources",
    "follow_up_questions"
  ],
  "title": "ResearchArtifact",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_1/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [8] HUMAN-USER prompt · 2026-08-20 20:43:52 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [9] SKILL-INPUT — aii-web-tools · 2026-08-20 20:43:56 UTC

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

### [10] SKILL-INPUT — aii-web-research-tools · 2026-08-20 20:43:56 UTC

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

### [11] SKILL-INPUT — aii-python · 2026-08-20 20:43:56 UTC

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

### [12] SYSTEM-USER prompt · 2026-08-20 20:54:09 UTC

```
<validation-feedback>
Attempt 1 failed validation.

Schema validation found 3 problems — fix ALL of them at once:
  - at `<root>`: 'answer' is a required property
  - at `<root>`: 'sources' is a required property
  - at `<root>`: 'follow_up_questions' is a required property
Every required field must be present and every field type must match the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
