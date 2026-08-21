# gen_art_research_1 — test_idea

> Phase: `invention_loop` · round 2 · `gen_art`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_art_research_1` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 00:41:22 UTC

````
Read and STRICTLY follow these skills: aii-web-tools.

<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1/`:
GOOD: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1/file.py`, `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1/results/out.json`
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

<context>
<dependencies>
Read the files in these dependency workspaces to understand what's available, then copy any you need into your working directory.

--- Dependency 1 ---
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
out_dependency_files:
  file_list:
  - research_out.json

Data files come in three sizes:
- preview_*_out.json — READ THIS to inspect the data structure
- mini_*_out.json (~3 examples) — use for prototyping/testing
- full_*_out.json (complete) — use for the final production run. NEVER open it directly (too large to read into context). Instead, extract values programmatically with shell commands (e.g. grep) or a Python script (use aii-long-running-tasks skill for scripts).
</dependencies>
</context>

<artifact_plan>
id: gen_plan_research_1_idx2
type: research
title: Verify Citations & Find Real OSS Survival Papers
summary: >-
  Verify all 15 references from iter 1, replace fabricated 2025-2026 citations with real alternatives, and find supplementary
  work on scaffolding, temporal analysis, and change-point detection in OSS.
runpod_compute_profile: cpu_light
question: >-
  Which of the 15 references in the current paper are real and accurate, which are fabricated, and what real papers should
  replace the fabricated ones to properly position the Founder Fade Curve hypothesis?
research_plan: |2

  ### PHASE 1: VERIFY THE 15 EXISTING REFERENCES (from iter_1 research_out.json)

  For each of the 15 references below, perform these checks in order:
  1. Search Semantic Scholar (mode=scholarly) for the paper by title
  2. If not found, search Google Scholar (mode=general) with the exact title in quotes
  3. If found: verify DOI resolves, confirm venue/year/authors match, verify key findings attributed to it
  4. If NOT found after both searches: mark as FABRICATED and proceed to Phase 2

  **References to verify:**

  [1] Avelino, Constantinou, Valente & Serebrenik (2019) "On the abandonment and survival of open source projects: An empirical investigation" — arXiv:1906.08058
  [2] Nourry et al. (2024) "Myth: The loss of core developers is a critical issue for OSS communities" — arXiv:2412.00313
  [3] "A Novel Approach for Estimating Truck Factors" — arXiv:1604.06766
  [4] "Defining Open-Source Software Success and Abandonment" — DOI:10.7551/mitpress/8413.003.0013
  [5] "What is the Truck Factor of popular GitHub applications? A first assessment" — DOI:10.7287/peerj.preprints.1233v2
  [6] "GHTorrent: Github's Data from a Firehose" — PDF at gousios.org
  [7] GHTorrent querying documentation — GitHub repo
  [8] GH Archive — gharchive.org
  [9] BigQuery GitHub codelab — Google codelabs
  [10] GitHub REST API rate limits — docs.github.com
  [11] GitHub GraphQL API rate limits — docs.github.com
  [12] SciPy theilslopes documentation — docs.scipy.org
  [13] ruptures library — GitHub repo
  [14] Theil-Sen estimator — Wikipedia
  [15] "Towards a Synergistic Fading Model: Adapting Scaffolding Theory for Human-AI Collaboration" — DOI:10.35542/osf.io/5eutb_v1

  **Priority checks (these are most likely fabricated):**
  - [4] MIT Press chapter — verify this exact title exists in the book "The Perils of GitHub Data" or similar
  - [5] PeerJ preprint — verify DOI resolves
  - [15] OSF preprint on scaffolding — verify DOI resolves and content matches

  ### PHASE 2: VERIFY THE 7 HYPOTHESIS RELATED_WORKS (these are the CRITICAL ones)

  The hypothesis cites 7 related works. The previous research already flagged 4 as potentially fabricated. Verify each:

  **HIGH PRIORITY — Previously Flagged as Likely Fabricated:**

  A. Kaushik & Chahal (2026) "The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics" — claimed Journal of Systems and Software
     - Search: "death spiral" "open source" "pull request" workflow
     - Search: Kaushik Chahal "death spiral" GitHub
     - Search: "death spiral" OSS PR backlog merge latency
     - If not found: this is FABRICATED — find real replacement

  B. Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) "How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment"
     - Search: Chen Stol Santos German Trinkenreich ICSE contributor disengagement
     - Search: "core contributor disengagement" ICSE quasi-experiment
     - Search: ICSE 2026 proceedings "contributor disengagement"
     - If not found: this is FABRICATED — find real replacement

  C. Karim, Lu, Kasaadha & Goggins (2026) "Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI"
     - Search: Karim Lu Kasaadha Goggins OSS sustainability transformer
     - Search: "deep temporal neural" OSS sustainability
     - Search: ICSME 2026 proceedings OSS sustainability
     - If not found: this is FABRICATED — find real replacement

  D. Noori, Chakraborti, Zhang & Frey (2025) "Patterns in the Transition From Founder-Leadership to Community Governance of Open Source"
     - Search: Noori Chakraborti Zhang Frey governance OSS
     - Search: "founder-leadership" "community governance" open source
     - Search: GOVERNANCE.md textual analysis OSS
     - If not found: this is FABRICATED — find real replacement

  **LOWER PRIORITY — More Likely Real:**

  E. Avelino et al. (2019) — same as [1] above, should be verifiable via arXiv
  F. Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory — these are classic educational psychology papers, should be verifiable
  G. Management literature on founder-CEO succession (Haveman et al., Honjo & Kato 2022) — verify these exist

  ### PHASE 3: FIND REAL REPLACEMENT PAPERS FOR FABRICATED ONES

  For each fabricated paper, find 1-2 real replacements by searching:

  **For the "Death Spiral" replacement (Kaushik & Chahal 2026):**
  - Search (scholarly): "open source project abandonment" "pull request" workflow dynamics
  - Search (scholarly): "OSS death spiral" OR "project decline" PR backlog merge latency
  - Search (scholarly): "open source" "inactive" "active" PR throughput decline
  - Target venues: ICSE, FSE, ESEM, TSE, JSS, EMSE (2020-2026)
  - Look for: papers analyzing PR workflow metrics as predictors of project survival

  **For the "Core Contributor Disengagement" replacement (Chen et al. ICSE 2026):**
  - Search (scholarly): "core contributor" disengagement OR departure OR turnover OSS
  - Search (scholarly): "contributor departure" impact "open source" activity
  - Search (scholarly): ICSE OR FSE OR ESEM "contributor turnover" OR "developer departure"
  - Target venues: ICSE, FSE, ESEM, TSE, JSS (2019-2026)
  - Look for: papers measuring the impact of key contributor departure on project activity

  **For the "Deep Temporal" replacement (Karim et al. 2026):**
  - Search (scholarly): "open source" sustainability prediction temporal machine learning
  - Search (scholarly): "OSS lifecycle" prediction deep learning OR transformer
  - Search (scholarly): "project sustainability" prediction time series GitHub
  - Target venues: ICSE, FSE, ESEM, TSE, JSS, ICSME (2020-2026)
  - Look for: papers using temporal/sequence models to predict OSS project outcomes

  **For the "Governance Transition" replacement (Noori et al. 2025):**
  - Search (scholarly): "open source" governance transition founder community
  - Search (scholarly): "GOVERNANCE.md" OR "governance file" analysis OSS
  - Search (scholarly): "founder succession" OR "leadership transition" open source
  - Target venues: ICSE, FSE, ESEM, TSE, JSS, CSCW (2020-2026)
  - Look for: papers on how OSS projects transition from founder-led to community-governed

  ### PHASE 4: FIND SUPPLEMENTARY WORK ON KEY TOPICS

  Search for additional papers to strengthen the paper's positioning:

  **4A. Scaffolding theory applied to software engineering:**
  - Search (scholarly): "scaffolding" "software engineering" OR "software development"
  - Search (scholarly): "scaffolding" "mentorship" "open source" OR "oss"
  - Search (scholarly): "knowledge transfer" "gradual" "open source" mentorship

  **4B. Temporal analysis of contributor trajectories in OSS:**
  - Search (scholarly): "contributor trajectory" OR "developer trajectory" open source temporal
  - Search (scholarly): "contributor activity" time series analysis GitHub
  - Search (scholarly): "developer involvement" trend analysis "open source"

  **4C. Change-point detection in software repository mining:**
  - Search (scholarly): "change point detection" "software repository" OR "GitHub"
  - Search (scholarly): "anomaly detection" "contributor activity" "open source"
  - Search (scholarly): "trend detection" "commit history" prediction

  ### PHASE 5: SYNTHESIZE FINDINGS

  Produce a comprehensive research report containing:

  1. **Verification Table**: For each of the 15 references + 7 hypothesis related_works:
     - Status: VERIFIED / FABRICATED / PARTIAL (found but details don't match)
     - Corrected citation (if needed)
     - Accurate summary of findings (1-2 sentences)
     - DOI/URL that resolves

  2. **Replacement Recommendations**: For each fabricated paper:
     - 1-2 real replacement papers with full citation
     - Why the replacement is relevant (what it actually studies)
     - How to rephrase the paper's positioning to use the real paper

  3. **Supplementary References**: Real papers found in Phase 4, organized by topic

  4. **Positioning Analysis**: A paragraph clarifying how the Founder Fade Curve hypothesis differs from:
     - Static predictor approaches (Avelino, Nourry)
     - Aggregate temporal approaches (any real papers found on temporal OSS analysis)
     - Governance transition work (any real papers found)
     - What gaps remain that the hypothesis addresses

  5. **Verified BibTeX**: A complete .bib file with all verified and replacement references

  ### EXECUTION ORDER AND BUDGET

  - Run Phase 1 and Phase 2 searches in parallel (they are independent)
  - Run Phase 3 searches after identifying which papers are fabricated
  - Run Phase 4 searches in parallel with Phase 3
  - Phase 5 is synthesis (no additional searches needed)
  - Budget: ~$10 for OpenRouter API calls (use scholarly mode for academic searches, general mode for verification of URLs/docs)
  - Time: 3 hours total for all phases

  ### FAILURE SCENARIOS

  - If a fabricated paper cannot be replaced with a direct match: find the CLOSEST real paper on the same topic and note the difference explicitly
  - If searches return no results for a specific query: try broader queries (e.g., remove year constraint, broaden venue list)
  - If a DOI doesn't resolve: try searching by title alone, then by author+topic
  - If Semantic Scholar returns no results: fall back to Google Scholar via general web search
explanation: >-
  The previous research iteration identified 4 papers (Kaushik & Chahal 2026, Chen et al. ICSE 2026, Karim et al. 2026, Noori
  et al. 2025) as potentially fabricated — they have future dates (2025-2026) and could not be located. This research will
  systematically verify all 15 existing references plus the 7 hypothesis related_works, replace any fabricated citations with
  real, verifiable alternatives from top software engineering venues, and find supplementary work on scaffolding theory, temporal
  analysis, and change-point detection to strengthen the paper's positioning. The output will be a verified bibliography and
  positioning analysis that the paper writer can use directly.
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

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json`

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

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/3_invention_loop/iter_2/gen_art/gen_art_research_1/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 00:41:22 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-tools · 2026-08-21 00:41:30 UTC

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
