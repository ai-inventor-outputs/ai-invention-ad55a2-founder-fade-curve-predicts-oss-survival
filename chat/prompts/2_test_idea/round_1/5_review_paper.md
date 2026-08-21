# review_paper — test_idea

> Phase: `invention_loop` · round 1 · `review_paper`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Predict Open-Source Project Survival: A Methodological Framework for Empirical Validation
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `review_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 16:41:13 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/review_paper/review_paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 16:41:13 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-web-tools · 2026-08-21 16:45:08 UTC

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

### [4] SYSTEM-USER prompt · 2026-08-21 17:17:43 UTC

````
<role>
You are a very experienced and critical conference reviewer specialized in the domain of the work under review.
You have reviewed for top-tier venues in the relevant field. Your reviews are known for
being thorough, fair, and grounded in the actual state of the field.
</role>

<paper>
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

</paper>

<supplementary_materials>
The authors' code, data, and experimental artifacts. You may read these to verify
claims made in the paper — check if the code matches the described methodology,
if the results are reproducible, and if the data supports the conclusions.

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
</supplementary_materials>

<available_domain_handbooks>
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for judging whether the paper's contribution is genuinely novel versus already-done or a known dead end in this field.

- **aii-handbook-auto-computational-linguistics** — Field handbook for computational linguistics as a SCIENCE of language — grammaticality and minimal pairs (BLiMP), surprisal versus reading times, linguistic structure in LMs, annotator disagreement an
- **aii-handbook-auto-mechanistic-interpretability** — Field handbook for mechanistic interpretability of neural networks — circuit discovery, activation and attribution patching, sparse autoencoders, transcoders, attribution graphs, steering vectors, pro
- **aii-handbook-auto-multi-agent-llm-systems** — Field handbook for multi-agent LLM systems (MAS) — orchestration topology, multi-agent debate, mixture-of-agents, verifier and critic agents, inter-agent protocols (MCP/A2A), failure attribution and s
- **aii-handbook-auto-neurosymbolic** — Field handbook for neuro-symbolic AI — text-to-logic autoformalization (NL to FOL), LLM-plus-solver and prover pipelines (Prolog, ASP, SMT), probabilistic-differentiable NeSy (DeepProbLog, Scallop), r
</available_domain_handbooks>



<task>
Review this paper as you would for a top-tier venue submission.

STEP 1 — READ THE PAPER: Read it carefully. Note claims, methodology, and results.

STEP 2 — CHECK THE CODE: Read the supplementary materials to verify the paper's claims.
Do the experiments match what's described? Are there discrepancies between code and paper?

STEP 3 — SEARCH THE LITERATURE: Ground your review in evidence.
- Search for the closest existing work — is this genuinely novel or incremental?
- Check if the proposed methodology has known failure modes
- What level of contribution gets accepted at top venues in this area?

STEP 4 — WRITE YOUR REVIEW:
For each critique:
1. Categorize: methodology, evidence, novelty, clarity, scope, or rigor
2. Rate severity: major (would cause rejection) or minor (polish)
3. Describe the issue clearly
4. Suggest a concrete action to address it

Focus on the most impactful issues. Provide your review via structured output.
</task><user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/review_paper/review_paper/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "Critique": {
      "description": "A single actionable critique from the reviewer.",
      "properties": {
        "category": {
          "description": "Category: 'methodology', 'evidence', 'novelty', 'clarity', 'scope', or 'rigor'",
          "title": "Category",
          "type": "string"
        },
        "severity": {
          "description": "Severity: 'major' or 'minor'",
          "title": "Severity",
          "type": "string"
        },
        "description": {
          "description": "Clear description of the issue",
          "title": "Description",
          "type": "string"
        },
        "suggested_action": {
          "description": "Concrete suggestion for how to address this critique",
          "title": "Suggested Action",
          "type": "string"
        }
      },
      "required": [
        "category",
        "severity",
        "description",
        "suggested_action"
      ],
      "title": "Critique",
      "type": "object"
    },
    "DimensionScore": {
      "description": "Score for a single review dimension with improvement suggestions.",
      "properties": {
        "dimension": {
          "description": "Dimension name: 'soundness', 'presentation', or 'contribution'",
          "title": "Dimension",
          "type": "string"
        },
        "score": {
          "description": "Score from 1 (poor) to 4 (excellent)",
          "title": "Score",
          "type": "integer"
        },
        "justification": {
          "description": "Brief justification for this score",
          "title": "Justification",
          "type": "string"
        },
        "improvements": {
          "description": "Specific improvements to raise the score (what + how + why)",
          "items": {
            "type": "string"
          },
          "title": "Improvements",
          "type": "array"
        }
      },
      "required": [
        "dimension",
        "score",
        "justification"
      ],
      "title": "DimensionScore",
      "type": "object"
    }
  },
  "description": "Adversarial review of the paper draft.\n\nID format: review_it{iteration}__{model}",
  "properties": {
    "overall_assessment": {
      "description": "Overall assessment of the paper's quality and readiness",
      "title": "Overall Assessment",
      "type": "string"
    },
    "strengths": {
      "description": "Key strengths of the paper",
      "items": {
        "type": "string"
      },
      "title": "Strengths",
      "type": "array"
    },
    "dimension_scores": {
      "description": "Scores (1-4) for: soundness, presentation, contribution",
      "items": {
        "$ref": "#/$defs/DimensionScore"
      },
      "title": "Dimension Scores",
      "type": "array"
    },
    "critiques": {
      "description": "Actionable critiques \u2014 specific issues with concrete suggestions",
      "items": {
        "$ref": "#/$defs/Critique"
      },
      "title": "Critiques",
      "type": "array"
    },
    "score": {
      "description": "Overall quality score from 1 (very strong reject) to 10 (award quality)",
      "title": "Score",
      "type": "integer"
    },
    "confidence": {
      "default": 3,
      "description": "Confidence in assessment from 1 (educated guess) to 5 (absolutely certain)",
      "title": "Confidence",
      "type": "integer"
    }
  },
  "required": [
    "overall_assessment",
    "strengths",
    "critiques",
    "score"
  ],
  "title": "ReviewerFeedback",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_mKQ84TZTBrTU/3_invention_loop/iter_1/review_paper/review_paper/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [5] HUMAN-USER prompt · 2026-08-21 17:17:43 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [6] SKILL-INPUT — aii-web-research-tools · 2026-08-21 17:19:20 UTC

The agent loaded the **aii-web-research-tools** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-web-research-tools
description: "Runs multi-source web research campaigns — literature reviews, deep cross-verification of many claims or citations, paper and PDF mining — by escalating WebSearch for discovery, WebFetch for the gist, then aii_web_tools__fetch_grep for exact regex extraction with context windows over HTML or PDFs. Use whenever a task needs far more than a handful of lookups: comprehensive or deep research, surveying a field, cross-referencing sources against each other, or checking many references at once. Triggers: literature review, comprehensive or extensive or deep research, survey the field, multi-source investigation, verify many citations, arXiv paper mining. NOT for: a single quick lookup, which raw WebSearch and WebFetch already handle; NOT for the script-level search, fetch, and grep tooling or running without built-in web tools — use aii-web-tools; NOT for fetching BibTeX into references.bib (use aii-semscholar-bib) or judging whether a draft's claims hold up (use amg-paper-verification)."
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

### [7] SKILL-INPUT — web search · 2026-08-21 17:19:24 UTC

The agent loaded the **web search** skill.

```
Tool: invoke_skill
{
  "command": "founder involvement trajectory open source project survival fading scaffolding",
  "name": "web search",
  "scope": "scholarly"
}
```

### [8] SYSTEM-USER prompt · 2026-08-21 17:23:55 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
