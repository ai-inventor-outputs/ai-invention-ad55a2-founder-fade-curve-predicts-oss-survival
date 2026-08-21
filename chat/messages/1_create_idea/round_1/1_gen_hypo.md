# gen_hypo_1 — create_idea

> Phase: `hypo_loop` · round 1 · `gen_hypo`
> Run: `run_dX5VwxrQ9qyp` — The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival
>
> Full, verbatim transcript of this agent task — every system/user prompt, assistant response, thinking block, tool call and tool result — in the order they occurred. Nothing truncated.

## Task: `gen_hypo_1` (sdk_openhands_agent, gemini/gemini-3.6-flash)

### [1] CONFIG · 2026-08-20 18:47:21 UTC

```
Model: gemini/gemini-3.6-flash | Session: d7a38a82-f461-47b8-8548-152cbee249ec | CWD: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent | Tools: 3 | Permission: acceptEdits
```

### [2] SYSTEM PROMPT · 2026-08-20 18:47:23 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

### [3] SYSTEM-USER prompt · 2026-08-20 18:47:23 UTC

````
<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<ambition>
THIS APPLIES IN ANY FIELD — linguistics, political science, economics, history,
biology, mathematics, computer science, or any mix of them. Where an example
below names a unit of study, read it as whatever your field's equivalent is:
languages, elections, markets, periods, corpora, species, model families, proof
techniques.

THE DEFAULT DELIVERABLE IS A NOVEL CONTRIBUTION. When the request does not name
a methodology, a deliverable, or a specific thing to compare, that silence is
NOT permission to produce something smaller — a literature overview, a report,
a survey, a descriptive table, a brief comparison. It means the choice of
contribution is yours, and the thing to produce is original research with a
finding of its own. Only an explicit request for a review or a replication
changes that.

CALIBRATE AMBITION TO WHAT THE REQUEST LEAVES OPEN. Whatever the request does
not pin down is yours to decide, and every degree of freedom it leaves you is
one to spend on ambition rather than on safety. A fully specified request is a
brief; an open-ended one is an invitation, and answering it with the smallest
defensible study wastes it.

THE TARGET is the most ambitious claim you can still expect to LAND — to finish
within the available resources with a non-trivial, genuinely insightful,
POSITIVE result. Both halves bind. Ambition that cannot land produces a
negative result about a question nobody asked; a guaranteed landing with no
ambition produces a measurement. Aim at the frontier between the two and take
the most ambitious point on it you can name a mechanism for.

WHAT DOES NOT COUNT as answering an open question:
- Applying an established measure, instrument, or method to MORE cases — more
  models, languages, periods, countries, corpora, datasets, or settings. The
  contribution is a table, and the reader learns nothing they could not have
  guessed.
- Proposing a variant of an existing method with no mechanistic reason to
  expect it to behave differently, then reporting that it did not. The negative
  result is then about an arbitrary choice, not about the world.
- Re-describing a known effect in new vocabulary, or naming it.
- A survey, a ranking, or a replication — unless that is what was asked for.

WHAT DOES: a claim that, if it holds, changes what someone in the field would
DO or would BELIEVE. Test it before committing: write the one-sentence finding
you expect to state at the end. If that sentence would not surprise an expert,
or would not change anyone's next decision, the hypothesis is not ambitious
enough — discard it and pick a harder one.

POSITIVE BY DESIGN, NOT BY LUCK. Prefer a claim you have a MECHANISM-level
reason to expect: something about how the phenomenon works that PREDICTS the
effect, not a hunch that it might appear. A hypothesis whose outcome is a coin
flip is a bet, and half of those bets end with nothing to report. Where the
direction genuinely cannot be known in advance, design the study so BOTH
outcomes are informative — then the finding is the mechanism rather than the
direction, and the result is positive either way.

SCALE THE CLAIM, NOT THE AMBITION, when resources bind. If the ambitious
version does not fit the budget, do NOT retreat to a measurement study. Narrow
what the claim COVERS — one language instead of twenty, one period, one
population, one model family — while keeping the mechanism it is about intact.
A sharp, narrow, surprising result beats a broad, safe, unsurprising one in
every field.
</ambition>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [4] HUMAN-USER prompt · 2026-08-20 18:47:23 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [5] THINKING · 2026-08-20 18:49:28 UTC

```
**My Approach to Generating a Novel Hypothesis**

Okay, so I need to come up with one groundbreaking research hypothesis for this AII prompt: "What determines whether an open-source project survives its founder stepping away?" My first instinct is to see what resources are immediately available. Before diving in, I should check the `user_uploads` directory and available tools. Specifically, I should probably invoke a `skill` to access tools like the terminal, file editor, or task tracker. I'll need to see if any handbooks in my domain are relevant, or if I need to utilize web search tools. If nothing else works, I can invoke `aii-web-tools` for searching or checking existing skills. First and foremost, let's explore the file directory at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads` and see what I can find there.
```

### [6] TOOL CALL — terminal · 2026-08-20 18:49:28 UTC

```
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [7] TOOL RESULT — terminal · 2026-08-20 18:49:30 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1030\ndrwxrwxrwx 2 root root       1 Aug 20 18:46 .\ndrwxrwxrwx 9 root root 1053852 Aug 20 18:47 .."}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/d7a38a82f46147b88548152cbee249ec/observations", "kind": "TerminalObservation"}
```

### [8] RETRY (attempt 1) · 2026-08-20 18:51:31 UTC

```
Agent result indicates failure (attempt 1/6): structured_output is None
```

### [9] RETRY (attempt 2) · 2026-08-20 18:51:32 UTC

```
Agent retry... (attempt 2/6): structured_output is None
```

### [10] CONFIG · 2026-08-20 18:51:33 UTC

```
Model: openai/z-ai/glm-5.2 | Session: 87cc6550-af5f-4f77-8a2b-9bd2e84310fa | CWD: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent | Tools: 3 | Permission: acceptEdits
```

### [11] SYSTEM PROMPT · 2026-08-20 18:51:35 UTC

```
<ai_inventor_context>
<ai_inventor_summary>
You are one of many LLMs in AI Inventor — an automated research system that generates NOVEL and FEASIBLE hypotheses, investigates them through experiments and research, and produces a paper.

Your output feeds other LLMs downstream. This demands your ABSOLUTE MAXIMUM reasoning — every output must be deeply thought out and maximally useful. Surface-level responses waste downstream computation.
</ai_inventor_summary>

<your_role>
YOU ARE: A hypothesis generator (Step 2.1: GEN_HYPO — UNSEEDED mode)

Pipeline: GEN_HYPO (you) → INVENTION_LOOP → GEN_PAPER_REPO

You received a AII prompt. No external seeds — generate a novel hypothesis from your own reasoning and web research.

Your hypothesis will enter the invention loop (propose → execute → narrate) → the results become a paper + GitHub repo.
It MUST be GENUINELY NOVEL (validated against related work) and FEASIBLE TO TEST (within computational/data/tooling constraints provided).
Vague or incremental hypothesis → wasted computation across the entire pipeline.
</your_role>
</ai_inventor_context>

<strategic_mindset>
You are competing with human researchers.

YOUR ADVANTAGE: Breadth across many fields (information theory, ecology, economics, physics, cognitive science, program synthesis, etc.). No single human has this breadth.

HUMAN ADVANTAGE: Deep expertise in their specific field — they know every paper, every failed attempt, every subtle reason "obvious" ideas don't work.

HOW TO WIN: Don't create variants within their field — they'll always recognize those. Find unexpected connections ACROSS fields no single expert would think of.

NOVELTY BAR: An expert should say "I never thought of approaching it THAT way" — not "that's like paper X with a twist." If your idea lives in a crowded neighborhood of similar approaches, it's NOT novel enough.

NO TIME PRESSURE: Exploring 5-6 directions and abandoning all is a SUCCESSFUL process. Settling for a mediocre idea because you already spent so long researching it is a FAILED process.
</strategic_mindset>

<principles>
1. NOVEL - genuinely new mechanism/principle, not incremental. If you have to argue why it's different, it's NOT novel enough.
2. FEASIBLE - testable within the provided compute, data, and tooling
3. CROSS-FIELD - leverage connections across distant domains
4. RIGOROUS - consider what evidence would support OR refute it
5. PRECISE - clear language, no unnecessary jargon
</principles>

<common_mistakes_to_avoid>
Critical pitfalls from past runs. EXPLICITLY CHECK FOR EACH ONE.

**1. Incremental Recombination Disguised as Novelty**
"Apply known method X to known domain Y" is engineering, not conceptual novelty. Your idea needs a new mechanism/principle/insight — not just a new pairing of existing things.
CHECK: If describable as "A but with B" where A and B both exist, it's recombination. What is the genuinely new IDEA?

**2. Ignoring Resource Constraints**
Every hypothesis MUST be testable with available compute, data, and tools.
CHECK: "Can this be implemented with the specific resources listed? What exact data/compute/tools do I need, and are they available?"

**3. Shallow Search Leading to False Novelty**
The same concept often exists under different terminology, in different fields, or framed differently. Searching only your own phrasing and concluding novelty is the MOST dangerous mistake.

CHECK — For every promising hypothesis:
a) Search 5-6 semantically different phrasings within the field
b) Strip to the CORE MECHANISM and search 8-10 unrelated fields (e.g., "MDL-based complexity selection" → search neural architecture search, program synthesis, Bayesian model selection) — the same principle often exists under different names
c) Search for failed/negative results ("limitations", "does not improve")
d) Search in plain English without jargon
If a paper does the same thing under a different name, it's NOT novel.

**4. Rationalizing Overlapping Prior Work**
When you find similar work, do NOT rationalize minor differences as novelty. Two common traps:

FRAMEWORK PORTING: "Nobody did this in MY framework" — if the core mechanism exists in any context (different algorithm, different ensemble type, different field), porting it is engineering, not novelty.

GAP-FILLING: Papers A, B, C each cover variants → you propose the missing combination. An expert would say "obviously someone will do that eventually."

CHECK: Strip your idea to its core mechanism. Search if that mechanism exists ANYWHERE — any framework, any field, any algorithm family. If yes, ABANDON. Don't salvage by narrowing scope or listing "critical differences."

**5. Anchoring Bias**
Once invested in a direction, you'll unconsciously downplay overlap and inflate minor differences into "key differentiators." This feels like thoroughness but is actually defensiveness.

WARNING SIGNS: listing "critical differences" instead of reconsidering; reluctance to "waste" prior search effort; refining the SAME idea instead of exploring different ones; differentiators about context/framework rather than core mechanism.

CHECK: If you found even 1 paper with a similar core mechanism, ABANDON. The best hypotheses rarely come from your first direction. Each abandonment is progress.

**6. Relying on Search Snippets Without Fetching**
Search snippets are NOT enough to assess overlap or understand an approach. The actual mechanism and limitations are only in the full text.
CHECK: FETCH and read any potentially relevant result. Don't assess novelty from titles and snippets alone.

**7. Same-Neighborhood Pivoting**
Replacing one idea with a variant in the same conceptual space is NOT a genuine pivot. If all your directions are "[different adjective] + [same core concept]", you haven't actually explored.

CHECK: Would a single expert in that subfield have thought of ALL your directions? If yes, bring in a mechanism or framing from a completely unrelated field. That's where genuine novelty lives.
</common_mistakes_to_avoid>

<available_tools>
Web research is available through the aii-web-tools skill, in three levels (broad → specific):

1. web search — Returns titles, URLs, snippets. Use first to discover and scan the landscape. Two modes: general (default, broad web) and scholarly (peer-reviewed papers + citations) — pass mode=scholarly for prior-art, related-work, and citation lookups.
2. web fetch — Reads a page and returns its content as markdown (HTML or PDF). Use to understand a source. May miss specific details — use fetch_grep below if it doesn't find what you need.
3. fetch_grep — Regex search over a page/PDF's full text. Returns exact matching sections with context. Use for precise details, exact numbers, methodology, or PDFs.

Workflow: search → fetch (understand) → fetch_grep (extract specifics).
</available_tools>

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

### [12] SYSTEM-USER prompt · 2026-08-20 18:51:35 UTC

````
PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately follow
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [agent_think]: **My Approach to Generating a Novel Hypothesis**

Okay, so I need to come up with one groundbreaking research hypothesis for this AII prompt: "What determines whether an open-source project survives its founder stepping away?" My first instinct is to see what resources are immediately available. Bef
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1030\ndrwxrwxrwx 2 root root       1 Aug 20 18:46 .\ndrwxrwxrwx 9 root root 1053852 Aug 20 18:47 .."}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads", "exit_co
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<ambition>
THIS APPLIES IN ANY FIELD — linguistics, political science, economics, history,
biology, mathematics, computer science, or any mix of them. Where an example
below names a unit of study, read it as whatever your field's equivalent is:
languages, elections, markets, periods, corpora, species, model families, proof
techniques.

THE DEFAULT DELIVERABLE IS A NOVEL CONTRIBUTION. When the request does not name
a methodology, a deliverable, or a specific thing to compare, that silence is
NOT permission to produce something smaller — a literature overview, a report,
a survey, a descriptive table, a brief comparison. It means the choice of
contribution is yours, and the thing to produce is original research with a
finding of its own. Only an explicit request for a review or a replication
changes that.

CALIBRATE AMBITION TO WHAT THE REQUEST LEAVES OPEN. Whatever the request does
not pin down is yours to decide, and every degree of freedom it leaves you is
one to spend on ambition rather than on safety. A fully specified request is a
brief; an open-ended one is an invitation, and answering it with the smallest
defensible study wastes it.

THE TARGET is the most ambitious claim you can still expect to LAND — to finish
within the available resources with a non-trivial, genuinely insightful,
POSITIVE result. Both halves bind. Ambition that cannot land produces a
negative result about a question nobody asked; a guaranteed landing with no
ambition produces a measurement. Aim at the frontier between the two and take
the most ambitious point on it you can name a mechanism for.

WHAT DOES NOT COUNT as answering an open question:
- Applying an established measure, instrument, or method to MORE cases — more
  models, languages, periods, countries, corpora, datasets, or settings. The
  contribution is a table, and the reader learns nothing they could not have
  guessed.
- Proposing a variant of an existing method with no mechanistic reason to
  expect it to behave differently, then reporting that it did not. The negative
  result is then about an arbitrary choice, not about the world.
- Re-describing a known effect in new vocabulary, or naming it.
- A survey, a ranking, or a replication — unless that is what was asked for.

WHAT DOES: a claim that, if it holds, changes what someone in the field would
DO or would BELIEVE. Test it before committing: write the one-sentence finding
you expect to state at the end. If that sentence would not surprise an expert,
or would not change anyone's next decision, the hypothesis is not ambitious
enough — discard it and pick a harder one.

POSITIVE BY DESIGN, NOT BY LUCK. Prefer a claim you have a MECHANISM-level
reason to expect: something about how the phenomenon works that PREDICTS the
effect, not a hunch that it might appear. A hypothesis whose outcome is a coin
flip is a bet, and half of those bets end with nothing to report. Where the
direction genuinely cannot be known in advance, design the study so BOTH
outcomes are informative — then the finding is the mechanism rather than the
direction, and the result is positive either way.

SCALE THE CLAIM, NOT THE AMBITION, when resources bind. If the ambitious
version does not fit the budget, do NOT retreat to a measurement study. Narrow
what the claim COVERS — one language instead of twenty, one period, one
population, one model family — while keeping the mechanism it is about intact.
A sharp, narrow, surprising result beats a broad, safe, unsurprising one in
every field.
</ambition>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [13] HUMAN-USER prompt · 2026-08-20 18:51:35 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [14] ASSISTANT · 2026-08-20 18:51:43 UTC

```
I'll start by understanding my task and checking available resources, then generate a novel hypothesis through systematic research.
```

### [15] TOOL CALL — task_tracker · 2026-08-20 18:51:43 UTC

```
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "Check /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads for any relevant files",
      "status": "in_progress"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes": "Cross-field brainstorming for OS project survival after founder departure",
      "status": "todo"
    },
    {
      "title": "Web search for landscape overview of each direction",
      "notes": "Search for existing approaches to OS sustainability, bus factor, founder departure",
      "status": "todo"
    },
    {
      "title": "Fetch and read potentially relevant papers",
      "notes": "Deep dive into closest related work",
      "status": "todo"
    },
    {
      "title": "Adversarial novelty check",
      "notes": "Try to disprove novelty - search within field, cross-field, failed results, plain English",
      "status": "todo"
    },
    {
      "title": "Feasibility check",
      "notes": "Verify testable with Python, available data, $10 OpenRouter budget",
      "status": "todo"
    },
    {
      "title": "Write hypothesis JSON output",
      "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema",
      "status": "todo"
    }
  ]
}
```

### [16] TOOL RESULT — task_tracker · 2026-08-20 18:51:43 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "Check /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads for any relevant files", "status": "in_progress"}, {"title": "Brainstorm 5-7 diverse directions without searching", "notes": "Cross-field brainstorming for OS project survival after founder departure", "status": "todo"}, {"title": "Web search for landscape overview of each direction", "notes": "Search for existing approaches to OS sustainability, bus factor, founder departure", "status": "todo"}, {"title": "Fetch and read potentially relevant papers", "notes": "Deep dive into closest related work", "status": "todo"}, {"title": "Adversarial novelty check", "notes": "Try to disprove novelty - search within field, cross-field, failed results, plain English", "status": "todo"}, {"title": "Feasibility check", "notes": "Verify testable with Python, available data, $10 OpenRouter budget", "status": "todo"}, {"title": "Write hypothesis JSON output", "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema", "status": "todo"}], "kind": "TaskTrackerObservation"}
```

### [17] TOOL CALL — terminal · 2026-08-20 18:51:55 UTC

```
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads && ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [18] TOOL RESULT — terminal · 2026-08-20 18:51:55 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1954\ndrwxrwxrwx 2 root root       1 Aug 20 18:46 .\ndrwxrwxrwx 9 root root 2000111 Aug 20 18:47 ..\ntotal 8955\ndrwxrwxrwx   9 root root 2000111 Aug 20 18:47 .\ndrwxrwxrwx 306 root root 3025766 Aug 20 18:48 ..\ndrwxrwxrwx   2 root root       1 Aug 20 18:46 .hf_cache\ndrwxrwxrwx   4 root root 1062917 Aug 20 18:51 .oh_sessions\n-rw-rw-rw-   1 root root     285 Aug 20 18:45 .run_submission.json\n-rw-rw-rw-   1 root root   28363 Aug 20 18:46 .workflow_input.json\ndrwxrwxrwx   4 root root 1002102 Aug 20 18:46 config\ndrwxrwxrwx   3 root root       1 Aug 20 18:47 iter_1\ndrwxrwxrwx   2 root root 1023898 Aug 20 18:46 logs\ndrwxrwxrwx   4 root root 1021964 Aug 20 18:46 sinks\ndrwxrwxrwx   2 root root       1 Aug 20 18:46 user_uploads"}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads && ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [19] ASSISTANT · 2026-08-20 18:53:01 UTC

```
No user uploads with content. Let me check the workflow input for context and invoke the web-tools skill.
```

### [20] TOOL CALL — terminal · 2026-08-20 18:53:01 UTC

```
{
  "command": "cat /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.run_submission.json",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [21] TOOL RESULT — terminal · 2026-08-20 18:53:03 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "{\n  \"run_id\": \"run_dX5VwxrQ9qyp\",\n  \"username\": \"admin\",\n  \"aii_prompt\": \"What determines whether an open-source project survives its founder stepping away?\",\n  \"staging_id\": \"\",\n  \"config_dir\": \"/ai-inventor/aii_data/users/admin/aii_config\",\n  \"submitted_at_epoch_ms\": 1787251530953\n}"}], "is_error": false, "command": "cat /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.run_submission.json", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [22] TOOL CALL — invoke_skill · 2026-08-20 18:53:03 UTC

```
{
  "name": "aii-web-tools"
}
```

### [23] TOOL RESULT — invoke_skill · 2026-08-20 18:53:03 UTC

````
{"content": [{"cache_prompt": false, "type": "text", "text": "## Web tools\n\nYou have three web capabilities: **search**, **fetch**, and **grep** (exact\nregex extraction over a full page or PDF).\n\n**Pick where they come from, in this order:**\n\n1. **If you have built-in `WebSearch` / `WebFetch` tools, PREFER those over the\n   scripts below.** They may be **deferred tools** (listed by name but with\n   schemas not yet loaded) \u2014 if so, call `ToolSearch(\"select:WebSearch,WebFetch\")`\n   ONCE to load them, then use them normally. Do not skip them just because they\n   need that one extra load step; they are the preferred path. Pair them with the\n   `aii_web_tools__fetch_grep` script below when you need exact text / numbers /\n   methodology that a summary would miss, or when reading a PDF.\n2. **Only if you have NO built-in `WebSearch` / `WebFetch`** (e.g. the OpenHands\n   backend), use the scripts in this skill (below). They are our own\n   implementations \u2014 free-first web search (keyless general/scholarly engines,\n   Serper fallback), html2text + PyMuPDF for fetch, and regex grep over the full\n   document text. They work without any built-in web tools.\n\nWorkflow either way: **search** (discover) \u2192 **fetch** (read for the gist) \u2192\n**grep** (pull exact details / read PDFs).\n\n---\n\n## Running the scripts\n\nRun every script with the skill's pre-provisioned interpreter (it already has\n`requests`, `html2text`, `pymupdf`, `python-dotenv`). Set `PY` once:\n\n```bash\nexport SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-web-tools\"\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\"\n```\n\n### 1. Search the web (free-first: general or scholarly)\n\n```bash\n# general web (default): keyless engines (ddgs, marginalia); Serper only if they miss\n$PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"neuro-symbolic FOL translation LLM\" --max-results 10\n# scholarly mode: OpenAlex + Crossref (DOIs, citation counts)\n$PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"neuro-symbolic FOL translation\" --mode scholarly\n```\n\nReturns ranked title / URL / snippet lines. `--mode general` (default) uses\nkeyless general engines; `--mode scholarly` uses academic APIs. Both fall back\nto Serper (paid) only when the free engines miss. Use search first to scan the\nlandscape; snippets are for discovery only \u2014 fetch a page before judging it.\n\n### 2. Fetch a page as markdown (HTML or PDF)\n\n```bash\n$PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/abs/2303.11366\" --max-chars 10000\n```\n\n`--max-chars` caps output (default 10000); `--char-offset N` pages further in.\nHandles PDFs transparently via PyMuPDF.\n\n### 3. Grep a page or PDF (exact regex extraction)\n\n```bash\n$PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/pdf/2303.11366\" --pattern \"verbal reinforcement\" --max-matches 20 --context-chars 200\n```\n\nReturns only the matching sections with surrounding context \u2014 the right tool\nfor exact numbers, table values, methodology, or long PDFs where a summary\nwould lose the detail. `-i` for case-insensitive.\n\n**Parallelize** independent searches/fetches in one turn; only sequence a\nfetch after the search that produced its URL.\n\n---\n\n## Notes\n\n- The scripts call our ability server. If a script prints\n  `Ability service not available`, the server is down \u2014 say so rather than\n  silently improvising a different search method.\n- Do **not** hand-roll your own `requests`/scraping for search when these\n  tools are available: Serper returns clean Google results and the fetch/grep\n  scripts already handle HTML, PDFs, and encoding.\n\n---\nThis skill is located at `/ai-inventor/.claude/skills/aii-web-tools`. Any files it references (e.g. under `scripts/`, `references/`, `assets/`) are relative to that directory."}], "is_error": false, "skill_name": "aii-web-tools", "kind": "InvokeSkillObservation"}
````

### [24] TOOL CALL — terminal · 2026-08-20 18:54:10 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\"\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\"\n# Test search works\n$PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival founder departure bus factor\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [25] TOOL RESULT — terminal · 2026-08-20 18:54:10 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Cannot execute multiple commands at once.\nPlease run each command separately OR chain them into a single command via && or ;\nProvided commands:\n(1) export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\"\n(2) export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\"\n# Test search works\n(3) $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival founder departure bus factor\" --max-results 10"}], "is_error": true, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\"\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\"\n# Test search works\n$PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival founder departure bus factor\" --max-results 10", "exit_code": null, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": null, "py_interpreter_path": null, "prefix": "", "suffix": ""}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [26] TOOL CALL — terminal · 2026-08-20 18:54:14 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival founder departure bus factor\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [27] TOOL RESULT — terminal · 2026-08-20 18:54:16 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source project survival founder departure bus factor  [general via ddgs]\nFound: 10 results\n\n1. Guiding Effort Allocation in Open-Source Software Projects Using Bus Factor Analysis\n   https://arxiv.org/html/2401.03303v1\n   January 6, 2024 - To mitigate this risk, it is important ... ) An interesting measurement used in this regard is known as the Bus Factor (BF), which is defined as the minimum number of key developers ...\n\n2. The Bus Factor: Life for Open-Source Projects After a Developer's Death | WIRED\n   https://www.wired.com/story/giving-open-source-projects-life-after-a-developers-death/\n   November 6, 2017 - The fewer people with ownership ... name for this: the bus factor, meaning the number of people who would have to be hit by a bus before there's no one left to maintain the project....\n\n3. On the abandonment and survival of open source projects\n   https://arxiv.org/pdf/1906.08058\n   Truck Factor developers detachment is not merely a \u00b7 theoretical concept: 16% of the projects faced at least ... A project survives if it survives the last observed TFDD....\n\n4. Bus Factor Explained: Key-Person Risk for Founders\n   https://verycreatives.com/blog/bus-factor\n   3 weeks ago - This article is for the founder ... hands in their notice. ... The bus factor is the minimum number of team members whose sudden departure would stall or sink a project.......\n\n5. Dumb Ways for an Open Source Project to Die | Andrew Nesbitt\n   https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html\n   May 19, 2026 - Fork limbo. A disagreement or a maintainer departure split the project across two or more forks, none of which has clearly won. Downstream froze at the last pre-split version rather tha...\n\n6. Bus Factor In Practice Elgun Jabrayilzade\u2217 elgun@bilkent.edu.tr\n   https://arxiv.org/pdf/2202.01523\n   Departure of the key project members can \u00b7 \u2217Elgun Jabrayilzade and Mikhail Evtikhiev contributed equally. lead to a situation when a significant part of the project is poorly \u00b7 understood by the remai...\n\n7. [1906.08058] On the abandonment and survival of open source projects: An empirical investigation\n   https://arxiv.org/abs/1906.08058\n   June 19, 2019 - Results: We found that 315 projects (16%) were abandoned and 128 of these projects (41%) survived because of new core developers who assumed the project development. The survey indicat...\n\n8. Calculate the bus factor of your software project - Livable Software\n   https://livablesoftware.com/calculate-bus-factor-software-project/\n   May 9, 2026 - Note that the way the bus factor is calculated a given developer could be part of the bus factor of a file but not of the directory where that file is included. That is, she could be a k...\n\n9. Bus factor 0 - Home | EPH\n   https://ericphanson.com/blog/2025/bus-factor-0/\n   November 16, 2025 - It\u2019s also widely recognized as a major point of fragilityFor example, the Open Source Security Foundation (OpenSSF), which itself is a Linux Foundation project, has a best practice...\n\n10. Council Post: Survive The Bus Factor: Strategies For Protecting Your Codebase\n   https://www.forbes.com/councils/forbestechcouncil/2024/08/28/survive-the-bus-factor-strategies-for-protecting-your-codebase/\n   August 28, 2024 - These terms all refer to the same thing: how many developers can leave before your codebase becomes unmaintainable? The bus factor is an existential threat to many IT projects, but f..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival founder departure bus factor\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [28] ASSISTANT · 2026-08-20 18:55:25 UTC

```
Good, the search tools work. I can see the existing landscape is dominated by "bus factor" / "truck factor" analysis. Now let me brainstorm diverse directions using the think tool, then search across multiple angles in parallel.
```

### [29] TOOL CALL — task_tracker · 2026-08-20 18:55:25 UTC

```
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "No user uploads found - empty folder",
      "status": "done"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes": "Cross-field brainstorming for OS project survival after founder departure",
      "status": "in_progress"
    },
    {
      "title": "Web search for landscape overview of each direction",
      "notes": "Search for existing approaches to OS sustainability, bus factor, founder departure",
      "status": "todo"
    },
    {
      "title": "Fetch and read potentially relevant papers",
      "notes": "Deep dive into closest related work",
      "status": "todo"
    },
    {
      "title": "Adversarial novelty check",
      "notes": "Try to disprove novelty - search within field, cross-field, failed results, plain English",
      "status": "todo"
    },
    {
      "title": "Feasibility check",
      "notes": "Verify testable with Python, available data, $10 OpenRouter budget",
      "status": "todo"
    },
    {
      "title": "Write hypothesis JSON output",
      "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema",
      "status": "todo"
    }
  ]
}
```

### [30] TOOL RESULT — task_tracker · 2026-08-20 18:55:27 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "No user uploads found - empty folder", "status": "done"}, {"title": "Brainstorm 5-7 diverse directions without searching", "notes": "Cross-field brainstorming for OS project survival after founder departure", "status": "in_progress"}, {"title": "Web search for landscape overview of each direction", "notes": "Search for existing approaches to OS sustainability, bus factor, founder departure", "status": "todo"}, {"title": "Fetch and read potentially relevant papers", "notes": "Deep dive into closest related work", "status": "todo"}, {"title": "Adversarial novelty check", "notes": "Try to disprove novelty - search within field, cross-field, failed results, plain English", "status": "todo"}, {"title": "Feasibility check", "notes": "Verify testable with Python, available data, $10 OpenRouter budget", "status": "todo"}, {"title": "Write hypothesis JSON output", "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema", "status": "todo"}], "kind": "TaskTrackerObservation"}
```

### [31] TOOL CALL — think · 2026-08-20 18:55:53 UTC

```
{
  "thought": "**Brainstorming diverse directions for \"What determines whether an open-source project survives its founder stepping away?\"**\n\nThe existing landscape is dominated by \"bus factor\" / \"truck factor\" analysis \u2014 measuring how many key developers could leave before a project fails. This is a STRUCTURAL/QUANTITATIVE approach (count key developers, look at knowledge concentration). Let me brainstorm genuinely different angles, drawing from distant fields.\n\n**Direction 1: ECOLOGICAL \u2014 Ecological succession theory**\nIn ecology, when a dominant species is removed from an ecosystem, whether the ecosystem survives depends on \"functional redundancy\" \u2014 whether other species can fill the same ecological niche \u2014 AND on the \"successional stage\" of the community. Early successional communities (pioneer species) are more vulnerable to disturbance than late successional (climax) communities. \n\nHypothesis: Open-source projects, like ecosystems, have \"successional stages.\" A project survives founder departure only if it has reached a \"climax community\" stage where functional redundancy exists across multiple maintainers who can fill the founder's niche. The KEY INSIGHT: it's not about the NUMBER of contributors (bus factor) but about whether the project has undergone \"ecological succession\" \u2014 a predictable sequence of community maturation. Projects that are still in \"pioneer stage\" (founder-dominated, fast growth, few redundant capabilities) will collapse; those in \"climax stage\" (diverse, functionally redundant, stable) survive regardless of who leaves.\n\nProblem: Functional redundancy is essentially a restatement of bus factor. The \"successional stage\" concept is more interesting but might be hard to operationalize distinctly from project age/maturity.\n\n**Direction 2: ECONOMIC \u2014 Institutional economics and \"founder's curse\"**\nIn institutional economics, there's the concept of \"path dependence\" and \"institutional lock-in.\" Organizations founded by charismatic leaders often fail to develop the impersonal rules and routines that would allow succession. The key variable is whether the organization has developed \"institutions\" (formal rules, routines, governance structures) vs. \"personal authority\" (charismatic/traditional authority in Weber's sense).\n\nHypothesis: The survival of an open-source project after founder departure is a function of whether governance has made the transition from \"personal authority\" (founder-centric) to \"rational-legal authority\" (rule-centric governance). Projects with formal governance structures (BDFL, steering committees, RFC processes, documented decision-making) survive; those relying on the founder's personal authority and reputation collapse.\n\nProblem: This is basically \"governance structures matter for survival\" \u2014 probably already well-studied in OSS research. Let me think about what's truly novel here...\n\n**Direction 3: LINGUISTICS/SEMIOtics \u2014 Knowledge encoding in commit messages and documentation**\nFrom linguistics and information theory, knowledge can be encoded in \"tacit\" (implicit, personal) vs. \"explicit\" (codified, externalized) forms. When the founder leaves, tacit knowledge leaves with them. The hypothesis would be about whether the project has \"externalized\" the founder's tacit knowledge into explicit form (documentation, commit messages, design docs, code comments, issue discussions).\n\nHypothesis: Open-source project survival after founder departure is predicted by the degree to which the founder's tacit knowledge has been \"externalized\" into explicit, machine-readable artifacts (documentation, commit messages, design rationale in issues, ADRs). Projects where the founder's decisions are traceable through documented institutional memory survive; those where decisions exist only in the founder's head (unexplained commits, undocumented design choices) collapse.\n\nThis has some novelty \u2014 measuring knowledge \"externalization\" as a survival predictor. But I need to check if this exists...\n\n**Direction 4: GAME THEORY \u2014 Repeated games and \"exit threat\" credibility**\nIn game theory, cooperation in repeated games is sustained by the credibility of punishment (e.g., exit threats). If the founder's exit threat is credible (they actually leave, and the project maintains quality), it changes the equilibrium incentive structure for remaining contributors. \n\nHypothesis: The CREDIBILITY of the founder's exit threat during the project's active phase shapes the project's survival. When founders maintain high \"exit threat credibility\" (they communicate boundaries, enforce contribution standards, and are willing to step away), contributors invest more in acquiring the skills and knowledge needed to maintain the project independently. Founders who never credibly threaten exit create \"dependency equilibria\" where no one else invests in maintenance capability.\n\nNovel angle: It's not about the founder's departure itself but about whether the THREAT of departure was credible throughout the project's life, which shapes the incentive structure for knowledge acquisition by others. This is a mechanism from repeated game theory.\n\n**Direction 5: NETWORK SCIENCE \u2014 \"Structural holes\" and information brokerage**\nFrom social network theory (Burt, Granovetter), \"structural holes\" are gaps between non-redundant contacts. A broker who bridges structural holes has power. The founder is likely the primary broker (bridging structural holes in the contributor network). When the broker is removed, whether the network collapses depends on whether alternative bridging pathways exist.\n\nHypothesis: Open-source project survival after founder departure is determined by the founder's position as a \"structural broker\" in the collaboration network AND by whether alternative bridging pathways exist. Projects where the founder monopolizes Brokering (connecting otherwise disconnected subcommunities) collapse when the founder leaves; those where brokering is distributed across multiple nodes survive.\n\nHmm, this is related to network centrality analysis. Need to check overlap with existing OSS network studies.\n\n**Direction 6: PHYSICS/PHASE TRANSITIONS \u2014 Critical slowing down as early warning**\nComplex systems approaching a tipping point (phase transition, critical transition) exhibit \"critical slowing down\" \u2014 increasing variance, stronger autocorrelation, slower recovery from perturbations. This has been applied to ecological collapse, financial markets, and medical conditions.\n\nHypothesis: Open-source projects approaching \"founder-induced collapse\" exhibit \"critical slowing down\" in their development activity metrics BEFORE the founder's departure. Specifically: commit frequency shows increasing variance, issue resolution time increases autocorrelation, and pull request merge times slow disproportionately for complex changes. These signals are detectable upstream of the departure and predict survival vs. collapse.\n\nNovel: Using early warning signals from critical transitions theory to predict OSS project survival. BUT \u2014 the \"critical slowing down\" occurs BEFORE departure, which means it measures pre-existing fragility, not the effect of departure. This might not directly answer the question.\n\n**Direction 7: IMMUNOLOGY \u2014 \"Allostatic load\" and cumulative stress**\nIn physiology, \"allostatic load\" is the cumulative wear and tear on biological systems from chronic stress. Systems under chronic stress become less resilient to acute shocks.\n\nHypothesis: Open-source projects accumulate \"developmental allostatic load\" \u2014 chronic stressors like unresolved technical debt, contributor burnout, maintainer conflict, and dependency churn. Projects with high allostatic load are less resilient to the acute shock of founder departure, while projects with low allostatic load absorb the same shock and survive. The departure alone doesn't determine survival; survival is a function of the interaction between departure shock and pre-existing allostatic load.\n\nInteresting \u2014 but hard to operationalize \"allostatic load\" for OSS distinctly from existing measures of technical debt or community health.\n\n**Direction 8: EVOLUTIONARY BIOLOGY \u2014 \"Hybrid vigor\" (heterosis) and contributor diversity**\nIn genetics, hybrid vigor (heterosis) occurs when crossbreeding produces offspring with traits superior to either parent. The opposite is inbreeding depression \u2014 loss of vigor from genetic uniformity.\n\nHypothesis: Open-source projects survive founder departure if the contributor base exhibits \"cognitive heterosis\" \u2014 functional diversity in problem-solving approaches, programming paradigms, and domain expertise among contributors. Projects dominated by contributors who are \"intellectual clones\" of the founder (same background, same problem-solving approaches) suffer \"inbreeding depression\" \u2014 they can't generate novel solutions to challenges that arise after the founder leaves. The key predictor is not contributor count but contributor DIVERSITY in problem-solving styles (measurable through prior project diversity, language diversity, domain diversity in contributor histories).\n\nThis has some real novelty \u2014 applying heterosis/inbreeding depression to OSS communities. But I need to check if cognitive diversity in OSS has been studied.\n\nLet me now assess which directions are most promising for novelty:\n- Direction 4 (game theory, exit threat credibility) \u2014 interesting mechanism, but need to check\n- Direction 5 (structural holes brokering) \u2014 network analysis, need to check overlap\n- Direction 3 (tacit/explicit knowledge externalization) \u2014 promising, novel mechanism\n- Direction 8 (heterosis/cognitive diversity) \u2014 promising, cross-field transfer\n\nLet me search across ALL of these to assess novelty."
}
```

### [32] TOOL RESULT — think · 2026-08-20 18:55:53 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
```

### [33] ASSISTANT · 2026-08-20 18:56:25 UTC

```
Now let me search across all these directions in parallel to assess the landscape. Let me run multiple searches at once.
```

### [34] TOOL CALL — terminal · 2026-08-20 18:56:25 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project governance survival BDFL successor founder\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [35] TOOL RESULT — terminal · 2026-08-20 18:56:27 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source project governance survival BDFL successor founder  [general via ddgs]\nFound: 10 results\n\n1. Benevolent dictator for life - Wikipedia\n   https://en.wikipedia.org/wiki/Benevolent_dictator_for_life\n   2 weeks ago - In July 2018, van Rossum announced that he would be stepping down as BDFL of Python without appointing a successor, effectively eliminating the title within the Python community structur...\n\n2. Can one person run an open source project alone? - Stack Overflow\n   https://stackoverflow.blog/2020/09/09/open-source-governance-benevolent-dictator-or-decision-by-committee/\n   September 9, 2020 - Determining how decisions get made and projects move forward is called governance. Depending on the project, the style of governance may be as open as the code itself, or it may al...\n\n3. Understanding open source governance models\n   https://www.redhat.com/en/blog/understanding-open-source-governance-models\n   January 22, 2026 - In these projects, the individual or group who started the project also administers the project, establishes its vision, and controls permissions to merge code into it. Some project...\n\n4. Leadership and Governance | Open Source Guides\n   https://opensource.guide/leadership-and-governance/\n   1 week ago - There are three common governance structures associated with open source projects. BDFL: BDFL stands for \u201cBenevolent Dictator for Life\u201d. Under this structure, one person (usually the init...\n\n5. OSPO Notes: Open Source Governance \u2014 Who Decides, and How | Chris Short\n   https://chrisshort.net/ospo-notes-open-source-governance-who-decides-and-how/\n   March 30, 2026 - They\u2019re the ones with governance clear enough that contributors from all walks of life know how to participate, and community members know the outcome is fair even when they disagree ...\n\n6. Is BDFL a death sentence? | Opensource.com\n   https://opensource.com/article/18/7/bdfl\n   July 16, 2018 - I am not going to appoint a successor. So what are you all going to do? Create a democracy? Anarchy? A dictatorship? A federation? It\u2019s worth zooming out for a moment to consider the i...\n\n7. Why Open Source Projects Are Run By Benevolent Dictators For Life\n   https://www.searchenginejournal.com/why-open-source-projects-are-run-by-benevolent-dictators-for-life/568532/\n   March 2, 2026 - WordPress is a community and while it has been said that it has a benevolent dictator for life in Matt Mullenweg, it\u2019s still a community-driven project, just like other open source pro...\n\n8. Picking a governance model for Python [LWN.net]\n   https://lwn.net/Articles/769178/\n   The Python language project has been officially \"leaderless\" since the mid-July announcement that Guido van Rossum was stepping down. He is, of course, the founder of the language and had served for m...\n\n9. Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\n   https://arxiv.org/html/2509.16295v3\n   September 28, 2025 - Specifically, we document trajectories to community governance by extracting institutional roles, actions, and deontic cues from version-controlled project constitutions (GOVERNAN...\n\n10. Scientific Python - SPEC 9 \u2014 Governance\n   https://scientific-python.org/specs/spec-0009/\n   Choosing the right governance model for your open-source project involves considering several factors to ensure the structure aligns with your project\u2019s goals, community, and resources. Most open-sour..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project governance survival BDFL successor founder\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [36] ASSISTANT · 2026-08-20 18:56:33 UTC

```
Interesting - item 9 is very relevant: "Patterns in the Transition From Founder-Leadership to Community Governance of Open Source" from Sept 2025. Let me search more directions in parallel and also fetch that paper.
```

### [37] TOOL CALL — terminal · 2026-08-20 18:56:34 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source software structural holes network brokering contributor network founder centrality\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [38] TOOL RESULT — terminal · 2026-08-20 18:56:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source software structural holes network brokering contributor network founder centrality  [general via ddgs]\nFound: 10 results\n\n1. Structural holes - Wikipedia\n   https://en.wikipedia.org/wiki/Structural_holes\n   March 26, 2026 - Structural holes is a concept from social network research, originally developed by Ronald Stuart Burt. A structural hole is understood as a gap between two individuals who have compl...\n\n2. Open-source software movement - Wikipedia\n   https://en.wikipedia.org/wiki/Open-source_software_movement\n   July 6, 2026 - Historically, researchers have characterized open-source contributors as a centralized, onion-shaped group. The center of the onion consists of the core contributors who drive the proje...\n\n3. Robustness of open source community multi-project knowledge collaboration network based on structural hole theory | PLOS One\n   https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0292444\n   January 2, 2024 - In summary, based on the characteristics of multi-project knowledge collaboration in the OSC, this paper (1) constructs a directed, weighted, semantic-based multi-project KCN by comb...\n\n4. Beyond Code Contributions: How Network Position, Temporal Bursts, and Code Review Activities Shape Contributor Influence in Large-Scale Open Source Ecosystems\n   https://arxiv.org/html/2602.06426\n   February 6, 2026 - Our analysis of thousands of contributors across hundreds of repositories reveals that OSS networks exhibit strong power-law distributions in influence, with the top 1% of contribut...\n\n5. Hierarchy and centralization in free and open source software team communications\n   https://www.researchgate.net/publication/225606224_Hierarchy_and_centralization_in_free_and_open_source_software_team_communications\n   December 1, 2006 - ... However, this theory is somewhat speculative as in reality, OSSD teams often exhibit some degree of natural centralisation, despite the lack of a predefined centralised structur...\n\n6. Returns from social capital in open source software networks | Journal of Evolutionary Economics | Springer Nature Link\n   https://link.springer.com/article/10.1007/s00191-008-0125-5\n   September 18, 2008 - Open Source Software projects base their operation on a collaborative structure for knowledge exchange in the form of provision or reception of information, expertise and feedback...\n\n7. Hierarchy and centralization in free and open source software team communications\n   https://link.springer.com/article/10.1007/s12130-006-1004-8\n   Free/Libre Open Source Software (FLOSS) development teams provide an interesting and convenient setting for studying distributed work. We begin by answering perhaps the most basic question: what is th...\n\n8. Structural holes \u2014 Grokipedia\n   https://grokipedia.com/page/Structural_holes\n   January 14, 2026 - Betweenness centrality, introduced by Linton Freeman, counts the proportion of shortest paths passing through a node, directly aligning with the monopoly brokerage opportunities def...\n\n9. Online division of labour: emergent structures in Open Source Software | Scientific Reports\n   https://www.nature.com/articles/s41598-019-50463-y\n   September 25, 2019 - Thus, in this paper we analyse a set of popular open source projects from GitHub, placing the accent on three key properties: nestedness, modularity and in-block nestedness \u2013which...\n\n10. Structural hole centrality: evaluating social capital through strategic network formation | Computational Social Networks | Springer Nature Link\n   https://link.springer.com/article/10.1186/s40649-020-00079-4\n   September 17, 2020 - Everett and Valente [10] discuss a number of other measures of brokerage and propose that brokerage can be calculated as an induced centrality measure [16], that is, that a node\u2019s..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source software structural holes network brokering contributor network founder centrality\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [39] TOOL CALL — terminal · 2026-08-20 18:57:42 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source contributor diversity ecosystem resilience survival turnover maintenance\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [40] TOOL RESULT — terminal · 2026-08-20 18:57:44 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source contributor diversity ecosystem resilience survival turnover maintenance  [general via ddgs]\nFound: 10 results\n\n1. The State of Survival in OSS: The Impact of Diversity | Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering\n   https://dl.acm.org/doi/10.1145/3611643.3617848\n   Maintaining and retaining contributors is crucial for Open Source (OSS) projects. However, there is often a high turnover among contributors (in some projects as high as 80%). The survivability of con...\n\n2. Analyzing Key Features of Open Source Software Survivability with Random Forest\n   https://www.mdpi.com/2076-3417/15/2/946\n   January 18, 2025 - OSS survivability is influenced by diverse human and technical factors, such as user retention, irreplaceability, contributor and user counts, and code quality. This reflects the fa...\n\n3. On the abandonment and survival of open source projects\n   https://arxiv.org/pdf/1906.08058\n   the likelihood of turnover [41]. Qiu et al. have observed that \u00b7 while women tend to disengage from open source projects \u00b7 faster than men, attachment of women to open teams with \u00b7 regard to diversity...\n\n4. Exploring turnover, retention and growth in an OSS Ecosystem\n   https://arxiv.org/html/2504.16483\n   April 23, 2025 - On the other hand, SP components could benefit from enhanced mechanisms to improve long-term contributor retention, in this way addressing sustainability concerns. Future research sho...\n\n5. Free open source communities sustainability: Does it make a difference in software quality? | Empirical Software Engineering | Springer Nature Link\n   https://link.springer.com/article/10.1007/s10664-024-10529-6\n   July 23, 2024 - The stability of the FOSS community is determined by its resilience and robustness, as well as the community\u2019s ability to maintain a consistent population of contributors who possess t...\n\n6. Free Open Source Communities Sustainability: Does It Make a Difference in Software Quality?\n   https://arxiv.org/html/2402.06916v1\n   February 10, 2024 - The stability of the FOSS community is determined by its resilience and robustness, as well as the community\u2019s ability to maintain a consistent population of contributors who posse...\n\n7. Sustainability of Open Source software communities beyond a fork: How and why has the LibreOffice project evolved? - ScienceDirect\n   https://www.sciencedirect.com/science/article/pii/S0164121213002744\n   November 21, 2013 - Findings from our analysis show that Open Source software communities can outlive Open Source software projects and that LibreOffice is perceived by its community as supportive, di...\n\n8. Open Source Software Projects and Community Engagement | Nature Research Intelligence\n   https://www.nature.com/research-intelligence/nri-topic-summaries-v9/open-source-software-projects-and-community-engagement\n   A systematic mapping study has characterised the processes by which community participation is nurtured, emphasising strategies for overcoming participation barriers and enhancing contributor engageme...\n\n9. Building Digital Societies as Ecosystems: How Recognition and Repeat Relationships Sustain Cross-Community Work in Open Source\n   https://arxiv.org/html/2605.25055\n   May 24, 2026 - \\sim 2017) are intrinsically more ... themselves cohort-structured features of the OSS landscape [9, 63]. The cross-community contributor layer is associated with longer survival at the...\n\n10. Predicting Maintenance Cessation of Open Source Software Repositories with An Integrated Feature Framework\n   https://arxiv.org/html/2507.21678v1\n   July 29, 2025 - Mature open source projects typically follow an \u201conion model\u201d comprising core maintainers, active contributors, and peripheral users. Disruption to the balance among these roles\u2014such a..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source contributor diversity ecosystem resilience survival turnover maintenance\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [41] ASSISTANT · 2026-08-20 18:57:46 UTC

```
I see item 1 and 2 are very relevant — "The State of Survival in OSS: The Impact of Diversity" and "Analyzing Key Features of Open Source Software Survivability with Random Forest." The diversity angle has been studied. Let me fetch the key papers and search more directions.
```

### [42] TOOL CALL — terminal · 2026-08-20 18:57:46 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2509.16295v3\" --max-chars 15000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [43] TOOL RESULT — terminal · 2026-08-20 18:57:48 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2509.16295v3\nType: HTML\nLength: 96023 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n\u00d7\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) \u00d7\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2509.16295v3 \"Back to abstract page\") [ Download PDF](/pdf/2509.16295v3 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract.\n  2. 1 Introduction\n     1. 1.1 Transitions to community governance in open-source software (OSS)\n     2. 1.2 Governance documents as a window into institutional processes\n     3. 1.3 Project governance on GitHub: The GOVERNANCE.md standard\n     4. 1.4 The study\n  3. 2 Related Work\n  4. 3 Theoretical Background\n     1. 3.1 Institutional analysis and development\n     2. 3.2 Institutional development of online communities\n     3. 3.3 Policy perspectives on OSS self-governance\n     4. 3.4 Design perspectives on OSS self-governance\n  5. 4 Methods\n  6. 5 Results\n  7. 6 Discussion\n     1. 6.1 Contributions\n  8. 7 Limitations\n  9. 8 Conclusion\n  10. References\n\n\n\n[ License: CC BY 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2509.16295v3 [cs.CY] 28 Sep 2025\n\n# Patterns in the Transition From Founder-Leadership to Community Governance of Open SourceDOI: [XXXXXXX.XXXXXXX](https://doi.org/XXXXXXX.XXXXXXX)Conference: Make sure to enter the correct conference title from your rights confirmation email; June 03\u201305, 2018; Woodstock, NYISBN: 978-1-4503-XXXX-X/2018/06CCS: Human-centered computing Computer supported cooperative workCCS: Human-centered computing Empirical studies in collaborative and social computingCCS: Human-centered computing Social engineering (social sciences)CCS: Human-centered computing Open source softwareCCS: Human-centered computing Empirical studies in HCI\n\nMobina Noori  Affiliation: University of California Davis , Department of Computer Science , Davis , CA , USA email: [lianoori@ucdavis.edu](mailto:lianoori@ucdavis.edu) ,  Mahasweta Chakraborti  Affiliation: University of California Davis , Department of Communication , Davis , CA , USA email: [mchakraborti@ucdavis.edu](mailto:mchakraborti@ucdavis.edu) ,  Amy X. Zhang  Affiliation: University of Washington , Allen School of Computer Science & Engineering , Seattle , WA , USA email: [axz@cs.uw.edu](mailto:axz@cs.uw.edu) and  Seth Frey  Affiliation: University of California Davis , Department of Communication , Davis , CA , USA email: [sethfrey@ucdavis.edu](mailto:sethfrey@ucdavis.edu)\n\n2018\u00a9 , 2018;\n\n###### Abstract.\n\nOpen digital public infrastructure needs community management to ensure accountability, sustainability, and robustness. Yet open-source projects often rely on centralized decision-making, and the determinants of successful community management remain unclear. We analyze 637 GitHub repositories to trace transitions from founder-led to shared governance. Specifically, we document trajectories to community governance by extracting institutional roles, actions, and deontic cues from version-controlled project constitutions (GOVERNANCE.md). With a semantic parsing pipeline, we cluster elements into broader role and action types. We find roles and actions grow, and regulation becomes more balanced, reflecting increases in governance scope and differentiation over time. Rather than shifting tone, communities grow by layering and refining responsibilities. As transitions to community management mature, projects increasingly regulate ecosystem-level relationships and add definition to project oversight roles. Overall, this work offers a scalable pipeline for tracking the growth and development of community governance regimes from open-source software\u2019s familiar default of founder-ownership.\n\n###### Keywords:\n\nNatural Language Processing, Open Source Software, Peer Production, Online Communities, Collective Action, OSS Governance\n\n## 1\\. Introduction\n\nOpen source software (OSS) underlies critical infrastructure around the globe, and has a hand in every aspect of digital life. And yet, most OSS projects are run as \u201cfounder-led, single-leader governance models\u201d with no formal accountability to their community, or society. OSS projects are largely volunteer-driven initiatives in which developers join, cooperate or cease contributing of their own volition. Although the top 1000 projects on the popular OSS hosting site GitHub show an average of 80 contributors (Bao et al. 2021), projects on such platforms start with just one founding contributor, by design, and most remain in a regime under the monarchic default (Schweik and English 2012). It is on founders to define governance processes: the specifics of contributing, or making and pursuing fixes and features, determining the rights of financial supporters, and defining the larger goals of the project (O\u2019mahony and Ferraro 2007). This implicit single-leader model is likely appropriate for the early stages of a project (Schneider et al. 2021). But as a project becomes important to its contributors, and even society, a founder-owner model becomes increasingly inappropriate from an accountability standpoint, particularly when a piece of software becomes critical digital public infrastructure (Zuckerman 2020). Although many OSS ventures begin with founder-centered, centralized control, sustaining growth and broad participation typically requires evolving governance to include shared leadership and community norms, thereby distributing influence beyond a single individual or core team (Feller et al. 2005)(Germonprez et al. 2018).\n\n### 1.1. Transitions to community governance in open-source software (OSS)\n\nFortunately, OSS projects seem to agree with this assessment. It is now commonplace that the Internet\u2019s most prominent OSS projects are undergoing transformations in their governance from the founder-owner default to community governance. After six years of operating under an ideologically aligned founder, but without formal community representation, the Debian operating system in 1997 initiated a multi-year governance transition process that concluded in annual democratic elections (which, themselves, continued to evolve in form and scope for several years) (O\u2019mahony and Ferraro 2007). The Django web framework moved from a single-leader governance model to a core team model in 2014 (Holovaty 2014) and from a core team model to a more inclusive and community-driven \u201ctechnical advisory board\u201d in 2020 (Bennett et al. 2020). The developers of the Python programming language, after decades under a single-leader governance model, took inspiration from the Django transition (Warsaw et al. 2018) to implement an elected board structure. In social media, the growth of the early community-led news website Slashdot motivated several redesigns of the site\u2019s moderation system, from manual moderation by the founder to ever-expanding methods of delegating the task to users, ultimately giving reputable users considerable opportunities for effective voice over Slashdot\u2019s content (Ganley and Lampe 2009). Other prominent examples of OSS projects that have transitioned from founder-owners to community governance include the FreeBSD operating system and the Apache server. At the same time, notable projects such as the Linux operating system and Vim text editor have persisted under founder-owner leadership.\n\nHowever encouraging and important, the phenomenon of voluntary transitions to community is poorly understood. Each case has enough important differences to obscure any core similarities. They may initiate their transitions voluntarily or involuntarily, because of core team burnout, community demands, or even the death of a founder, as in the 2017 case of OpenDataKit. During transitions, they use different tools to help them through the process, often adapting the tools they have for the needs they discover. Python, for example, solicited governance proposals from its community through its preexisting system for evaluating technical language improvements, the Python Enhancement Proposal (PEP) system (Edge 2018). While reflecting the strength and determination of OSS communities to steer themselves toward accountability (Izquierdo and Cabot 2018), such governance software \u201chacks\u201d reflect the OSS community\u2019s need for shared, general, theoretically-grounded tooling dedicated to the challenging problem of major governance transformation. Overall, the trend is happening in large part in spite of available models and tools, rather than because of them. Legal, technical, and even cultural defaults lead the overwhelming majority of OSS projects start under founder-led, single-leader governance, and only much later, if at all, transfer ownership and management (and thus, accountability) to their communities (Schneider et al. 2021).\n\nCommunity governance of OSS not only secures the accountability of a project\u2019s design decisions to society, but may also reduce the administrative load on project founders, and subsequent burnout (Hertel et al. 2003; Sadowski et al. 2008). However, the governance defaults of open source software hosting platforms do little to ensure the success of community management (Schneider et al. 2021). As the stakes of a project increase, so do its responsibilities to its community, particularly if that project finds itself playing a role in critical public infrastructure (Goggins et al., 2021; Overney, 2020). Thus, the absence of robust support for community management can plant the seeds for society-scale accountability problems down the line, as OSS projects on those platforms become more successful.\n\n### 1.2. Governance documents as a window into institutional processes\n\nPrior research has tended to approach OSS governance through indirect signals and descriptive accounts rather than through systematic, longitudinal documentation of governance as expressed in textual artifacts. Empirical work has largely inferred governance from behavioral traces (such as commits, issues, and mailing lists) and complemented this with qualitative case studies that detail governance mechanisms, including contribution guidelines and social practices that support coordination in distributed communities (Wright et al. 2010)(O\u2019Mahony and Ferraro 2007). Much of the prior work tends to focus on more superficial features of policy texts, such as their length, headers, and topics (Beck and Kieser 2003), and to be cross-sectional rather than tracking persistent governance inscriptions over time (Feller et al. 2005)(Izquierdo and Cabot 2023).\n\nThus a significant gap remains: there is no established longitudinal account of how governance transitions to community management are executed in formal textual artifacts and how these representations evolve during this institutional interregnum. This gap motivates a textual-governance lens in OSS governance evolution, acknowledging that governance-related content encoded in artifacts\u2014such as guidelines, policies, and governance-oriented files stored in version control\u2014provides direct insight into institutional structure and accountability, in the process of aligning with broader calls for public stewardship and accountability in governance of open source software (Vasilescu et al. 2014)(Izquierdo and Cabot 2023)(Zuckerman 2020).\n\n### 1.3. Project governance on GitHub: The GOVERNANCE.md standard\n\nGitHub is the most widely used hosting platform for open-source development, built on the distributed version-control system Git. It provides an infrastructure for collaboration, coordination, and community visibility as well as storing code. Governance is a persistent concern in this context: projects must determine how authority should be allocated, how contributor rights should be granted or lost, and how conflicts should be resolved.\n\nFortunately, as a reflection of its resourcefulness, the OSS community has developed a loose standard for defining OSS project governance on GitHub, one that prescribes a clear, uniform location and format for governing documents. Increasingly, influential OSS projects on GitHub\u2014such as node.js, Docker, and Jupyter\u2014are posting public GOVERNANCE.md files that list out their policies for contributions, donations, planning, and other essential OSS governance functions. GOVERNANCE.md files are an elegant use of the \u201cgit\u201d version control software to assign responsibilities and provide clear community entry points into OSS governance (Izquierdo and Cabot 2015a). In this it follows other emergent conventions for community management, like CONTRIBUTING.md and CODE_OF_CONDUCT.md files. Also, because GOVERNANCE.md is a plain text file co-hosted with project code, it can leverage git\u2019s tools for version control and forking. This means tracking of historical changes by default, and excellent tools for projects to learn from each other\u2019s governance designs, and select their own institutional designs in an informed manner. GOVERNANCE.md files are an entry point for OSS projects to transition from the implicit feudalism of founder-owners to true, and truly accountable community governance.\n\n### 1.4. The study\n\nTo address the gap in our understanding of governance transitions from unitary to community governance, we compile a dataset of 637 open-source repositories to compare the initial and latest snapshots of the GOVERNANCE.md constitutions, enabling a longitudinal examination of how governance is explicitly articulated and evolves across projects (Yin et al. 2022)(Izquierdo and Cabot 2015b).We parse text from these artifacts into three core components\u2014Roles, Actions, and Deontics\u2014capturing who is responsible, what activities are authorized or required, and the normative force behind those directives, reflecting established practices for articulating governance rules and governance-oriented roles in OSS ecosystems (Izquierdo and Cabot 2015b)(Izquierdo and Cabot 2021). The methodological contribution lies in integrating NLP-driven information extraction with statistical approaches to scale OSS governance analysis across hundreds of projects: we leverage textual embeddings and grouping techniques to surface governance patterns from many repositories, a direction supported by prior work that combines linguistic analyses of OSS communications with longitudinal network perspectives to study governance dynamics (Yin et al. 2022)(Izquierdo and Cabot 2015b).This approach operationalizes governance as a textual, machine-readable artifact and enables cross-project comparability, consistent with the literature\u2019s emphasis on explicit governance documentation and the use of computational methods to analyze governance-related text in relevant contexts (Izquierdo and Cabot 2015b)(Yin et al. 2022).\n\nBuilding on this dataset and analytic pipeline, we capture governance evolution"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2509.16295v3\" --max-chars 15000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [44] ASSISTANT · 2026-08-20 18:59:03 UTC

```
This paper (2509.16295) studies governance TRANSITIONS (founder→community) by analyzing GOVERNANCE.md files — it's about documenting the governance evolution, NOT about predicting survival after departure. It uses textual/artifact analysis. Not the same as my hypotheses, but close in neighborhood. Let me fetch the diversity paper and the critical transitions/BFI direction.
```

### [45] TOOL CALL — terminal · 2026-08-20 18:59:03 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://dl.acm.org/doi/10.1145/3611643.3617848\" --max-chars 12000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [46] TOOL RESULT — terminal · 2026-08-20 18:59:19 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://dl.acm.org/doi/10.1145/3611643.3617848\nType: HTML\nLength: 30568 chars (truncated)\n\n--- Content ---\n\nskip to main content\n\n[](/)\n\n[](https://www.acm.org \"ACM home \\(external site link\\)\")\n\n  * [Advanced Search](/search/advanced)\n  * [Browse](/browse/ \"browse by title or publisher\")\n  * [About](/about \"About the ACM Digital Library\")\n  *     * [ Sign in ](/action/showLogin?redirectUri=%2Fdoi%2F10.1145%2F3611643.3617848)\n    * [ Register ](https://accounts.acm.org?redirectUri=%2Fdoi%2F10.1145%2F3611643.3617848 \"Register\")\n\n\n\n\n  *   * [Advanced Search](/search/advanced)\n  * [Journals](/journals)\n  * [Magazines](/magazines)\n  * [Proceedings](/proceedings)\n  * [Books](/acmbooks)\n  * [SIGs](/sigs)\n  * [Conferences](/conferences)\n  * [People](/people)\n  *   * More __\n  *\n\n\nSearch ACM Digital Library\n\nSearchSearch\n\n[Advanced Search](/search/advanced \"link to Advanced Search form\")\n\n10.1145/3611643.3617848acmconferencesArticle/Chapter ViewAbstractPublication PagesfseConference Proceedingsconference-collections\n\nfse\n\n  * [Conference](/conference/fse)\n  * [Proceedings](/conference/fse/proceedings)\n  * [Upcoming Events](/conference/fse/upcoming)\n  * [Authors](/conference/fse/authors)\n  * [Affiliations](/conference/fse/affiliations)\n  * [Award Winners](/conference/fse/award-winners)\n  * More __\n\n\n\n  * [Home](https://dl.acm.org/)\n  * [Conferences](/conferences)\n  * [FSE](/conference/fse)\n  * [Proceedings](/conference/fse/proceedings)\n  * [ESEC/FSE 2023](/doi/proceedings/10.1145/3611643)\n  * [The State of Survival in OSS: The Impact of Diversity](/doi/10.1145/3611643.3617848)\n\n\n\nshort-paper\n\nShare on\n\n  *  __\n  * __\n  * __\n  * __\n  * __\n\n\n\n\n# The State of Survival in OSS: The Impact of Diversity\n\n  * **Author:**\n  * [ Zixuan Feng Oregon State University, Corvallis, USA](javascript:void\\(0\\); \"Zixuan Feng\")\n\nOregon State University, Corvallis, USA\n\n[View Profile](/profile/99660635972)\n\n\nAuthors Info & Claims\n\n[ESEC/FSE 2023: Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering](/doi/proceedings/10.1145/3611643 \"ESEC/FSE 2023: Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering\")November 2023Pages 2213\u20132215<https://doi.org/10.1145/3611643.3617848>\n\nPublished:30 November 2023Publication History\n\n  * __0 citation\n  *  __39\n  * Downloads\n\n\n\nMetrics\n\nTotal Citations0Total Downloads39\n\nLast 12 Months39\n\nLast 6 weeks8\n\n  * [__Get Citation Alerts](/action/addCitationAlert?doi=10.1145/3611643.3617848)\n\n __\n\n## New Citation Alert added!\n\nThis alert has been successfully added and will be sent to:\n\nYou will be notified whenever a record that you have chosen has been cited.\n\nTo manage your alert preferences, click on the button below.\n\n[Manage my Alerts](/action/showPreferences?menuTab=Alerts \"Manage my Alerts\")\n\n __\n\n## New Citation Alert!\n\nPlease [log in to your account](/action/showLogin?redirectUri=/doi/10.1145/3611643.3617848 \"Sign In\")\n\n  * __\n  * __\n  * Publisher Site __\n\n\n  *   * [__Get Access](javascript:void\\(0\\); \"Get Access\")\n\n\n\n## [ESEC/FSE 2023: Proceedings of the 31st ACM Joint European Software Engineering Conference and Symposium on the Foundations of Software Engineering](/doi/proceedings/10.1145/3611643)\n\nThe State of Survival in OSS: The Impact of Diversity\n\nPages 2213\u20132215\n\n[__Previous Chapter](/doi/10.1145/3611643.3617854 \"Previous item in TOC\")[NextChapter __](javascript:void\\(0\\) \"Next item in TOC\")\n\n__\n\n## ABSTRACT\n\nMaintaining and retaining contributors is crucial for Open Source (OSS) projects. However, there is often a high turnover among contributors (in some projects as high as 80%). The survivability of contributors is influenced by various factors, including their demographics. Research on contributors\u2019 survivability must, therefore, consider diversity factors. This study longitudinally analyzed the impact of demographic attributes on survivability in the Flutter community through the lens of gender, region, and compensation. The preliminary analysis reveals that affiliated or Western contributors have a higher survival probability than volunteer or Non-Western contributors. However, no significant difference was found in the survival probability between men and women.\n\n##  References\n\n  1. 2023\\. https://github.com/flutter [Google Scholar](http://scholar.google.com/scholar?hl=en&q=2023.+https%3A%2F%2Fgithub.com%2Fflutter%0A%09%09%09%09)\n  2. 2023\\. https://namsor.app/about-us [Google Scholar](http://scholar.google.com/scholar?hl=en&q=2023.+https%3A%2F%2Fnamsor.app%2Fabout-us%0A%09%09%09%09)\n  3. Sogol Balali, Igor Steinmacher, Umayal Annamalai, Anita Sarma, and Marco Aurelio Gerosa. 2018. Newcomers\u2019 barriers... is that all? an analysis of mentors\u2019 and newcomers\u2019 barriers in OSS projects. Computer Supported Cooperative Work (CSCW), 27 (2018), 679\u2013714. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Sogol+Balali%2C+Igor+Steinmacher%2C+Umayal+Annamalai%2C+Anita+Sarma%2C+and+Marco+Aurelio+Gerosa.+2018.+Newcomers%E2%80%99+barriers...+is+that+all%3F+an+analysis+of+mentors%E2%80%99+and+newcomers%E2%80%99+barriers+in+OSS+projects.+Computer+Supported+Cooperative+Work+%28CSCW%29%2C+27+%282018%29%2C+679%E2%80%93714.%0A%09%09%09%09)[Digital Library](/doi/10.1007/s10606-018-9310-8)\n  4. Amiangshu Bosu and Kazi Zakia Sultana. 2019. Diversity and inclusion in open source software (OSS) projects: Where do we stand? In 2019 ACM/IEEE International Symposium on Empirical Software Engineering and Measurement (ESEM). 1\u201311. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Amiangshu+Bosu+and+Kazi+Zakia+Sultana.+2019.+Diversity+and+inclusion+in+open+source+software+%28OSS%29+projects%3A+Where+do+we+stand%3F+In+2019+ACM%2FIEEE+International+Symposium+on+Empirical+Software+Engineering+and+Measurement+%28ESEM%29.+1%E2%80%9311.%0A%09%09%09%09)[Cross Ref](/servlet/linkout?suffix=e_1_3_2_1_4_1&dbid=16&doi=10.1145%2F3611643.3617848&key=10.1109%2FESEM.2019.8870179)\n  5. Fabio Calefato, Marco Aurelio Gerosa, Giuseppe Iaffaldano, Filippo Lanubile, and Igor Steinmacher. 2022. Will you come back to contribute? Investigating the inactivity of OSS core developers in GitHub. Empirical Software Engineering, 27, 3 (2022), 76. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Fabio+Calefato%2C+Marco+Aurelio+Gerosa%2C+Giuseppe+Iaffaldano%2C+Filippo+Lanubile%2C+and+Igor+Steinmacher.+2022.+Will+you+come+back+to+contribute%3F+Investigating+the+inactivity+of+OSS+core+developers+in+GitHub.+Empirical+Software+Engineering%2C+27%2C+3+%282022%29%2C+76.%0A%09%09%09%09)[Digital Library](/doi/10.1007/s10664-021-10012-6)\n  6. InduShobha Chengalur-Smith, Saggi Nevo, and Pindaro Demertzoglou. 2010. An empirical analysis of the business value of open source infrastructure technologies. Journal of the Association for Information Systems, 11, 11 (2010), 3. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=InduShobha+Chengalur-Smith%2C+Saggi+Nevo%2C+and+Pindaro+Demertzoglou.+2010.+An+empirical+analysis+of+the+business+value+of+open+source+infrastructure+technologies.+Journal+of+the+Association+for+Information+Systems%2C+11%2C+11+%282010%29%2C+3.%0A%09%09%09%09)[Cross Ref](/servlet/linkout?suffix=e_1_3_2_1_6_1&dbid=16&doi=10.1145%2F3611643.3617848&key=10.17705%2F1jais.00242)\n  7. Zixuan Feng, Mariam Guizani, Marco A Gerosa, and Anita Sarma. 2023. The State of Diversity and Inclusion in Apache: A Pulse Check. arXiv preprint arXiv:2303.16344. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Zixuan+Feng%2C+Mariam+Guizani%2C+Marco+A+Gerosa%2C+and+Anita+Sarma.+2023.+The+State+of+Diversity+and+Inclusion+in+Apache%3A+A+Pulse+Check.+arXiv+preprint+arXiv%3A2303.16344.%0A%09%09%09%09)\n  8. Mariam Guizani, Bianca Trinkenreich, Aileen Abril Castro-Guzman, Igor Steinmacher, Marco Gerosa, and Anita Sarma. 2022. Perceptions of the State of D&I and D&I Initiative in the ASF. In Proceedings of the 2022 ACM/IEEE 44th International Conference on Software Engineering: Software Engineering in Society. 130\u2013142. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Mariam+Guizani%2C+Bianca+Trinkenreich%2C+Aileen+Abril+Castro-Guzman%2C+Igor+Steinmacher%2C+Marco+Gerosa%2C+and+Anita+Sarma.+2022.+Perceptions+of+the+State+of+D%26I+and+D%26I+Initiative+in+the+ASF.+In+Proceedings+of+the+2022+ACM%2FIEEE+44th+International+Conference+on+Software+Engineering%3A+Software+Engineering+in+Society.+130%E2%80%93142.%0A%09%09%09%09)[Digital Library](/doi/10.1145/3510458.3513008)\n  9. Renee Li, Pavitthra Pandurangan, Hana Frluckaj, and Laura Dabbish. 2021. Code of Conduct Conversations in Open Source Software Projects on Github. Proceedings of the ACM on Human-Computer Interaction, 5, CSCW1 (2021), 1\u201331. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Renee+Li%2C+Pavitthra+Pandurangan%2C+Hana+Frluckaj%2C+and+Laura+Dabbish.+2021.+Code+of+Conduct+Conversations+in+Open+Source+Software+Projects+on+Github.+Proceedings+of+the+ACM+on+Human-Computer+Interaction%2C+5%2C+CSCW1+%282021%29%2C+1%E2%80%9331.%0A%09%09%09%09)[Digital Library](/doi/10.1145/3449093)\n  10. Bin Lin, Gregorio Robles, and Alexander Serebrenik. 2017. Developer turnover in global, industrial open source projects: Insights from applying survival analysis. In 2017 IEEE 12th International Conference on Global Software Engineering (ICGSE). 66\u201375. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Bin+Lin%2C+Gregorio+Robles%2C+and+Alexander+Serebrenik.+2017.+Developer+turnover+in+global%2C+industrial+open+source+projects%3A+Insights+from+applying+survival+analysis.+In+2017+IEEE+12th+International+Conference+on+Global+Software+Engineering+%28ICGSE%29.+66%E2%80%9375.%0A%09%09%09%09)[Digital Library](/doi/10.1109/ICGSE.2017.11)\n  11. Onkar S Malgonde, Terence JV Saldanha, and Sunil Mithas. 2023. RESILIENCE IN THE OPEN SOURCE SOFTWARE COMMUNITY: HOW PANDEMIC AND UNEMPLOYMENT SHOCKS INFLUENCE CONTRIBUTIONS TO OTHERS\u2019AND ONE\u2019S OWN PROJECTS.. MIS Quarterly, 47, 1 (2023). [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Onkar+S+Malgonde%2C+Terence+JV+Saldanha%2C+and+Sunil+Mithas.+2023.+RESILIENCE+IN+THE+OPEN+SOURCE+SOFTWARE+COMMUNITY%3A+HOW+PANDEMIC+AND+UNEMPLOYMENT+SHOCKS+INFLUENCE+CONTRIBUTIONS+TO+OTHERS%E2%80%99AND+ONE%E2%80%99S+OWN+PROJECTS..+MIS+Quarterly%2C+47%2C+1+%282023%29.%0A%09%09%09%09)\n  12. Courtney Miller, David Gray Widder, Christian K\u00e4stner, and Bogdan Vasilescu. 2019. Why do people give up flossing? a study of contributor disengagement in open source. In Open Source Systems: 15th IFIP WG 2.13 International Conference, OSS 2019, Montreal, QC, Canada, May 26\u201327, 2019, Proceedings 15. 116\u2013129. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Courtney+Miller%2C+David+Gray+Widder%2C+Christian+K%C3%A4stner%2C+and+Bogdan+Vasilescu.+2019.+Why+do+people+give+up+flossing%3F+a+study+of+contributor+disengagement+in+open+source.+In+Open+Source+Systems%3A+15th+IFIP+WG+2.13+International+Conference%2C+OSS+2019%2C+Montreal%2C+QC%2C+Canada%2C+May+26%E2%80%9327%2C+2019%2C+Proceedings+15.+116%E2%80%93129.%0A%09%09%09%09)\n  13. Marco Ortu, Giuseppe Destefanis, Steve Counsell, Stephen Swift, Roberto Tonelli, and Michele Marchesi. 2017. How diverse is your team? Investigating gender and nationality diversity in GitHub teams. Journal of Software Engineering Research and Development, 5, 1 (2017), 1\u201318. [Google Scholar](http://scholar.google.com/scholar?hl=en&q=Marco+Ortu%2C+Giuseppe+Destefanis%2C+Steve+Counsell%2C+Stephen+Swift%2C+Roberto+Tonelli%2C+and+Michele+Marchesi.+2017.+How+diverse+is+your+team%3F+Investigating+gender+and+nationality+diversity+in+GitHub+teams.+Journal+of+Software+Engineering+Research+and+Development%2C+5%2C+1+%282017%29%2C+1%E2%80%9318.%0A%09%09%09%09)[Cross Ref](/servlet/linkout?suffix=e_1_3_2_1_13_1&dbid=16&doi=10.1145%2F3611643.3617848&key=10.1186%2Fs40411-017-0044-y)\n  14. Gede Artha Azriadi Prana, Denae Ford, Ayushi Rastogi, David Lo, Rahul Purandare, and Nachiappan Nagappan. 2020. Including Everyone, Everywhere: Understanding Opportunities and"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://dl.acm.org/doi/10.1145/3611643.3617848\" --max-chars 12000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [47] ASSISTANT · 2026-08-20 18:59:31 UTC

```
This diversity paper (2023) is about demographic diversity impact on individual contributor survivability (gender/region/compensation) in the Flutter community — NOT about project survival after founder departure. It's about CONTRIBUTOR survival, not PROJECT survival, and demographic rather than cognitive diversity. But it's in the neighborhood. Let me explore the critical transitions and game theory directions more thoroughly now.
```

### [48] TOOL CALL — terminal · 2026-08-20 18:59:31 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"critical slowing down early warning signals software project activity collapse tipping point\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [49] TOOL RESULT — terminal · 2026-08-20 18:59:31 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: critical slowing down early warning signals software project activity collapse tipping point  [general via ddgs]\nFound: 10 results\n\n1. REVIEWS Early-warning signals for critical transitions\n   https://pdodds.w3.uvm.edu/files/papers/others/2009/scheffer2009a.pdf\n   The most straightforward implication of critical slowing down is \u00b7 that the recovery rate after small experimental perturbation can be \u00b7 used as an indicator of how close a system is to a bifurcation ...\n\n2. Critical slowing down as early warning for the onset of collapse in mutualistic communities - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC4267327/\n   Little is known on whether structurally diverse ecological networks may respond abruptly to anthropogenic stress and even less on our ability to detect such responses in advance. By simulating mutuali...\n\n3. ESD - Tipping point detection and early warnings in climate, ecological, and human systems\n   https://esd.copernicus.org/articles/15/1117/2024/\n   August 19, 2024 - The general mechanism behind EWSs is that, as a dynamical system approaches a tipping point, it becomes slower at recovering from small perturbations (Wissel, 1984), and this critica...\n\n4. Early Warning Signals of Tipping-Points in Blog Posts | MITRE\n   https://www.mitre.org/news-insights/publication/early-warning-signals-tipping-points-blog-posts\n   December 1, 2012 - Complex systems in a variety of ... tipping-points can be detected via a concept called critical slowing down by examining a set of statistical metrics.......\n\n5. Critical slowing down as early warning for the onset of collapse in mutualistic communities | PNAS\n   https://www.pnas.org/doi/10.1073/pnas.1406326111\n   November 24, 2014 - In the case of ecological communities under stress, the risk of approaching a tipping point is unknown, but its stakes are high. Here, we test recently developed critical slowing-d...\n\n6. Deep learning for early warning signals of tipping points - PMC\n   https://pmc.ncbi.nlm.nih.gov/articles/PMC8488604/\n   Early warning signals (EWS) of tipping points are vital to anticipate system collapse or other sudden shifts. However, existing generic early warning indicators designed to work across all systems do ...\n\n7. Early warning of climate tipping points from critical slowing down: comparing methods to improve robustness | Philosophical Transactions of the Royal Society A | The Royal Society\n   https://royalsocietypublishing.org/rsta/article/370/1962/1185/114587/Early-warning-of-climate-tipping-points-from\n   March 13, 2012 - ... Heuristic illustration of critical slowing down. Panels show characteristic changes in non-equilibrium dynamics as a system approaches a tipping point (catastrophic bifurcation)....\n\n8. (PDF) Early-warning signals for critical transitions\n   https://www.academia.edu/51456610/Early_warning_signals_for_critical_transitions\n   September 3, 2009 - Although predicting such critical ... ... Early-warning signals like critical slowing down indicate impending critical transitions across diverse complex systems.......\n\n9. Lack of Critical Slowing Down Suggests that Financial Meltdowns Are Not Critical Transitions, yet Rising Variability Could Signal Systemic Risk | PLOS One\n   https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0144198\n   January 13, 2016 - Theoretical and empirical studies ... by a generic phenomenon called critical slowing down, i.e. an increasingly slow response of the system to perturbations.......\n\n10. [2401.09364] Anticipating Tipping Points for Disordered Traffic: Critical Slowing Down on the Onset of Congestion\n   https://arxiv.org/abs/2401.09364\n   January 17, 2024 - In the vicinity of a tipping point, perturbations gradually increases, and as a consequence, system-state extensively swing around the quasi-static attractor, and the local dynamics..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"critical slowing down early warning signals software project activity collapse tipping point\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [50] ASSISTANT · 2026-08-20 19:00:05 UTC

```
No results applying "critical slowing down" to OSS specifically. This is interesting but the direction doesn't directly answer the question (it's about PRE-departure signals). Let me search more focused on the game theory exit-threat direction and a new angle that connects to the actual question.
```

### [51] TOOL CALL — terminal · 2026-08-20 19:00:05 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival key person dependency knowledge concentration code commit bus factor prediction\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [52] TOOL RESULT — terminal · 2026-08-20 19:00:07 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source project survival key person dependency knowledge concentration code commit bus factor prediction  [general via ddgs]\nFound: 10 results\n\n1. Guiding Effort Allocation in Open-Source Software Projects Using Bus Factor Analysis\n   https://arxiv.org/html/2401.03303v1\n   January 6, 2024 - Formally known as the Bus Factor (BF) of a project and defined as \u201cthe number of key developers who would need to be incapacitated to make a project unable to proceed\u201d (inproceedings...\n\n2. On the abandonment and survival of open source projects: An empirical investigation | Request PDF\n   https://www.researchgate.net/publication/336627073_On_the_abandonment_and_survival_of_open_source_projects_An_empirical_investigation\n   September 1, 2019 - This work presents Knowledge Islands, a tool that visualizes the concentration of knowledge in a software repository using a state-of-the-art knowledge model. Key features of Knowl...\n\n3. From Commits to Confidence: Towards Stability-Informed Risk Assessment in Open Source Software\n   https://arxiv.org/html/2508.02487\n   January 5, 2026 - The \u201cbus factor\u201d measure [cosentino2015assessing] approximates team resilience, that is, a high share of commits concentrated in the top three contributors indicates a low bus factor...\n\n4. [2401.03303] Guiding Effort Allocation in Open-Source Software Projects Using Bus Factor Analysis\n   https://arxiv.org/abs/2401.03303\n   January 6, 2024 - Formally known as the Bus Factor (BF) of a project and defined as 'the number of key developers who would need to be incapacitated to make a project unable to proceed'. Most of the p...\n\n5. Calculate the bus factor of your software project - Livable Software\n   https://livablesoftware.com/calculate-bus-factor-software-project/\n   May 9, 2026 - Multiple changes equally considered This metric counts the number of times a line has been modified during the life-cycle of the project. It assigns more knowledge to the developers that...\n\n6. Bus Factor: A Human-Centered Risk Metric in the Software Supply Chain\n   https://www.cesarsotovalero.net/blog/bus-factor-a-human-centered-risk-metric-in-the-software-supply-chain.html\n   February 6, 2022 - Existing algorithms for bus factor estimation collect the distribution of information in the project from the Git version control system. Smaller values of the bus factor lead to hi...\n\n7. On the abandonment and survival of open source projects\n   https://arxiv.org/pdf/1906.08058\n   B. Identifying Truck Factor Developers Detachments \u00b7 To search for TFDDs, we \ufb01rst estimate the TF of a system at \u00b7 a time t and verify whether the TF developers abandoned the \u00b7 system before t. We say...\n\n8. How to Measure Bus Factor in Your Software Team | Calyntro Blog\n   https://calyntro.com/blog/posts/2026-06-02-how-to-measure-bus-factor/\n   June 2, 2026 - Informal knowledge about knowledge concentration is itself concentrated in the people who know the system well. By definition, it\u2019s unreliable. There\u2019s a more direct method. Your versio...\n\n9. Dumb Ways for an Open Source Project to Die | Andrew Nesbitt\n   https://nesbitt.io/2026/05/19/dumb-ways-for-an-open-source-project-to-die.html\n   May 19, 2026 - New contributors get one bruising review and don\u2019t come back, and the bus factor stays at one because nobody else can stand to share the repo. It looks healthy on every metric that coun...\n\n10. Council Post: Survive The Bus Factor: Strategies For Protecting Your Codebase\n   https://www.forbes.com/councils/forbestechcouncil/2024/08/28/survive-the-bus-factor-strategies-for-protecting-your-codebase/\n   August 28, 2024 - Interestingly, the study noticed that as the number of developers grows, the relative bus factor decreases. In other words, a larger team doesn't shield you from the bus factor\u2014quite..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project survival key person dependency knowledge concentration code commit bus factor prediction\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [53] ASSISTANT · 2026-08-20 19:00:35 UTC

```
The bus factor landscape is dense. Let me now search the outdegree/brokerage and dependency-network directions, plus a completely new angle I'm thinking of that connects the actual question more directly.
```

### [54] TOOL CALL — think · 2026-08-20 19:00:35 UTC

```
{
  "thought": "Let me step back and think about what's genuinely missing from the existing literature and what would be a NOVEL mechanism:\n\n**What exists in the literature:**\n1. Bus factor / truck factor analysis \u2014 measures how many key developers could leave before collapse. Concentration of knowledge via commit attribution. This is QUANTITATIVE/STRUCTURAL.\n2. Governance transitions \u2014 analyzes GOVERNANCE.md text to document founder\u2192community transitions. This is INSTITUTIONAL/NLP.\n3. Contributor diversity & demographic impact on contributor retention. This is DIVERSITY/EQUITY.\n4. Abandonment & survival empirical studies (2019) \u2014 found 16% abandoned, 41% of those survived via new core developers.\n5. Network analysis of OSS communities \u2014 centrality, onion model, modularity.\n\n**What's missing / novel angles:**\n\nThe question asks \"What determines whether an open-source project survives its FOUNDER stepping away?\" This is specifically about FOUNDER departure, not generic key-developer departure. The founder is special because:\n1. They typically have unique authority (BDFL)\n2. They have a vision for the project\n3. They may have unique knowledge of design decisions\n\nAn important reframing: most existing work conflates \"key developer leaves\" with \"project dies.\" But the founder departure is a special shock. The question is really about PROJECT INSTITUTIONAL RESILIENCE to a specific type of shock.\n\nLet me think about a genuinely novel mechanism that the field hasn't considered:\n\n**Idea A: \"Anti-fragility through forking\" \u2014 the founder departure creates a FORKING crisis**\nHmm, too narrow.\n\n**Idea B: From physics \u2014 \"symmetry breaking\" and phase transitions**\nWhen a system with a high-symmetry state (founder-centered) loses its organizing principle, it can either:\n- Relapse to a symmetric ground state (project dies/reverts)  \n- Transition to a new broken-symmetry ordered state (a new \"order\" emerges spontaneously)\n- Become disordered (chaotic, multiple competing visions)\nThe CRITICAL VARIABLE is whether the system has any \"latent order parameters\" \u2014 pre-existing subsystems with their own leadership that can rapidly become the new organizing principle.\n\nThis is interesting but hard to operationalize.\n\n**Idea C: From IMMUNOLOGY \u2014 the founder is a \"keystone individual\"; survival depends on \"immunological memory\"**\nActually, let me think about a much fresher angle.\n\n**Idea D: From EPIDEMIOLOGY / SOCIAL contagion \u2014 \"behavioral adoption cascade\" after founder exit**\nWhen the founder of an OSS project announces departure, this is a SIGNAL. The remaining contributors update beliefs about the project's future viability. This could trigger either:\n- A \"bank run\" / panic abandonment: contributors flee because they fear others will flee (self-fulfilling collapse).\n- A \"rally around the flag\" effect: contributors increase effort because they're committed to the vision.\nThe key insight from bank-run / contagion theory: collapse vs survival depends on the CONTRIBUTOR NETWORK'S SUSCEPTIBILITY to panic cascade \u2014 whether contributor departures propagate or are absorbed. Projects where departure cascades can propagate (high interconnectedness, low dissuasion) collapse; projects where the cascade is contained survive.\n\nBut predicting \"cascade susceptibility\" is itself hard.\n\n**Idea E (STRONG): From SOCIOLOGY OF ORGANIZATIONS \u2014 \"organizational imprinting\" and \"founder effects\"**\nStinchcombe (1965) \"Social Structure and Organizations\" introduced \"imprinting\" \u2014 organizations are imprinted by the conditions at founding, and these imprints persist. The KEY mechanism: the Founder imprints a specific ORGANIZATIONAL DNA \u2014 decision-making styles, structural relationships, cultural norms \u2014 that shapes the project for its lifetime.\n\nThis gives me a new angle on the original question: What DETERMINES whether the project survives is the SPECIFIC TYPE OF IMPRINT the founder leaves. Specifically:\n- Founders who imprint \"process-dominant\" DNA (the imprint encodes HOW decisions are made \u2014 RFC processes, contribution rules, governance structures, code review norms) leave behind a self-perpetuating organization that survives their departure.\n- Founders who imprint \"person-dominant\" DNA (the imprint relies on the founder's personal judgment, relationships, vision, taste) leave behind nothing when they go.\n\nBut this is essentially the governance transition story (Idea above), so it's not novel enough.\n\n**Idea F (NEW DIRECTION): From ECOLOGY \u2014 \"keystone predator removal\" and \"trophic cascade reversal\"**\nIn ecology, removing a keystone predator can trigger a TROPHIC CASCADE \u2014 the entire food web reorganizes. The signature finding: it's not just whether the system survives, but HOW IT REORGANIZES DEPENDS ON THE MULTI-STABILITY LANDSCAPE \u2014 whether alternative stable states exist. Systems with multiple stable equilibria can flip to a different stable state (still \"survives\" but transformed); systems with only one stable state collapse.\n\nHmm, this is somewhat abstract.\n\n**Idea G (PROMISING): From POPULATION GENETICS \u2014 \"founder effect\" and the founder's \"genetic bottleneck\"**\nIn population biology, the \"founder effect\" describes how a new population established by a small number of founders has reduced genetic diversity and remains shaped by the founders' genetic makeup. This is the conceptual analog.\n\nHypothesis: OSS projects exhibit a \"founder effect\" \u2014 the founder(s)' \"cognitive genetic diversity\" (the diversity of problem-solving approOR, technical sub-skills, language paradigms they bring) shapes the diversity of the project's contributor ecosystem throughout its life. Projects founded by people with diverse cognitive backgrounds develop diverse contributor ecosystems that can survive founder departure; projects founded by narrow-background founders develop narrow \"cognitive bottlenecks\" that can't.\n\nBut this overlaps with Idea 8 (heterosis) and diversity angle.\n\nLet me think about TRULY different fields...\n\n**Idea H (NEW): From PEDAGOGY / EDUCATION SCIENCES \u2014 \"scaffolding theory\" (Vygotsky)**\nIn education, \"scaffolding\" is when a more knowledgeable person provides structured support to a learner, allowing the learner to accomplish tasks they couldn't do alone. As learners develop competence, scaffolding fades. The KEY insight: if scaffolding is REMOVED too early (before the learner's competence matures), the learner collapses. But if scaffolding is gradually faded over time in a \"zone of proximal development,\" the learner internalizes the skills and is independent.\n\nHypothesis: A founder's survival after departure is determined by whether they have provided \"scaffolding for autonomy\" \u2014 gradually training contributors to operate independently. Specifically: founders who early on provide high scaffolding (detailed reviews, mentoring, decision explanations) and GRADUALLY FADE scaffolding over time (letting contributors make decisions, accepting imperfect work, allowing mistakes) produce contributors who can maintain the project independently. Founders who never fade scaffolding (or never provide it) \u2014 they either do everything themselves or hand off abruptly \u2014 produce contributors who cannot maintain the project when the founder leaves.\n\nThis is potentially novel! It's not about the AMOUNT of knowledge transfer, nor the NUMBER of contributors, nor GOVERNANCE FORM \u2014 it's about the SHAPE of the scaffolding fade curve. There's a measurable signal: how the founder's review activity, decision-making autonomy given to others, and educational interactions evolve over time.\n\nThe mechanism: founders who fade scaffolding over time produce a contribution base ready to take over; founders who don't, leave behind a contributor base dependent on the founder's continued involvement.\n\nI really like this direction. Let me think about whether it's actually novel vs. just an \"informal mentorship\" framing.\n\nThe closest existing concept I can think of: \"newcomer socialization\" in OSS, \"mentorship programs\" (Google Summer of Code), \"leader handover\". But scaffolding is a CONTINUOUS PROCESS over the project's lifetime, measured by the trajectory of how a founder's mentoring/decision-sharing evolves. It's a DYNAMIC, longitudinal property of the founder-contributor interaction pattern.\n\nI'll proceed with this hypothesis but need to:\n1. Search for related work in OSS mentoring, newcomer socialization, leader handover, succession planning\n2. Verify whether there's a measure of \"scaffolding trajectory\" for founders\n3. Verify feasibility \u2014 can I measure scaffolding fade curve from GitHub data? I think YES: I can measure over time how the founder's involvement in code reviews, their solo commits vs. collaborative commits, their decisive role in PR merges, their \"teaching\" behaviors (explaining decisions in PR comments).\n\nLet me proceed with adversarial novelty search."
}
```

### [55] TOOL RESULT — think · 2026-08-20 19:00:35 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
```

### [56] ASSISTANT · 2026-08-20 19:01:11 UTC

```
I have a promising direction: the "scaffolding fade curve" from educational/pedagogical theory. Let me adversarially check its novelty — searching for existing work on founder mentoring trajectories, newcomer socialization, and handover in OSS.
```

### [57] TOOL CALL — terminal · 2026-08-20 19:01:11 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source newcomer socialization mentorship trajectory founder handover succession sustainability\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [58] TOOL RESULT — terminal · 2026-08-20 19:01:13 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source newcomer socialization mentorship trajectory founder handover succession sustainability  [general via ddgs]\nFound: 10 results\n\n1. Do Good, Stay Longer? Temporal Patterns and Predictors of Newcomer-to-Core Transitions in Conventional OSS and OSS4SG\n   https://arxiv.org/html/2601.23142v1\n   January 30, 2026 - Open Source Software (OSS) sustainability relies on newcomers transitioning to core contributors, but this pipeline is broken, with most newcomers becoming inactive after initial co...\n\n2. Guiding the way: A systematic literature review on mentoring practices in open source software projects - ScienceDirect\n   https://www.sciencedirect.com/science/article/abs/pii/S0950584924000752\n   April 9, 2024 - The empirical evidence shows that ... careers, and social networks. Moreover, mentoring can bolster the success and growth of OSS projects and communities by improving sustainability.....\n\n3. Revolutionizing Newcomers\u2019 Onboarding Process in OSS Communities: The Future AI Mentor | Proceedings of the ACM on Software Engineering\n   https://dl.acm.org/doi/10.1145/3715767\n   Onboarding newcomers is vital for the sustainability of open-source software (OSS) projects. To lower barriers and increase engagement, OSS projects have dedicated experts who provide guidance for ......\n\n4. Same Project, Different Start: How Contribution Events Shape Activity and Retention in Open Source\n   https://arxiv.org/html/2604.22120\n   April 23, 2026 - (2022) proposed managing episodic volunteers through community integration; by analogy, we hypothesize that mentorship programs would benefit from a graduation phase that explicitly t...\n\n5. Rethinking open source mentorship in the AI era - The GitHub Blog\n   https://github.blog/open-source/maintainers/rethinking-open-source-mentorship-in-the-ai-era/\n   March 19, 2026 - Open source is experiencing its own \u201cEternal September\u201d: a constant influx of contributions that strains the social systems we rely on to build trust and mentor newcomers....\n\n6. Growing Your Open Source Community in 2025: Strategies for Sustainable Projects - DEV Community\n   https://dev.to/axrisi/growing-your-open-source-community-in-2025-strategies-for-sustainable-projects-2lln\n   June 16, 2025 - Contributor Spotlights Highlight a \u201cContributor of the Month\u201d in release notes, your blog, or social media to share their story and code snippets\u2014as part of an open source marketing st...\n\n7. Socialization in an Open Source Software Community: A Socio-Technical Analysis | Computer Supported Cooperative Work (CSCW) | Springer Nature Link\n   https://link.springer.com/article/10.1007/s10606-005-9000-1\n   July 21, 2005 - Consequently, we do not know how these communities of software developers are sustained and reproduced over time through the progressive integration of new members. To shed light on th...\n\n8. The hard life of open source software project newcomers | Proceedings of the 7th International Workshop on Cooperative and Human Aspects of Software Engineering\n   https://dl.acm.org/doi/10.1145/2593702.2593704\n   Community-based Open Source Software (OSS) projects are usually self-organized and dynamic, receiving contributions from distributed volunteers. Newcomer are important to the survival, long-term succe...\n\n9. Being a Mentor in open source projects | Journal of Internet Services and Applications | Full Text\n   https://jisajournal.springeropen.com/articles/10.1186/s13174-021-00140-z\n   September 9, 2021 - Mentoring is a well-known way to help newcomers to Open Source Software (OSS) projects overcome initial contribution barriers. Through mentoring, newcomers learn to acquire essenti...\n\n10. GitHub - OpenSourceFellows/open-source-mentorship: Inspiring the next generation of open source contributors and maintainers \u00b7 GitHub\n   https://github.com/OpenSourceFellows/open-source-mentorship\n   Inspiring the next generation of open source contributors and maintainers - OpenSourceFellows/open-source-mentorship..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source newcomer socialization mentorship trajectory founder handover succession sustainability\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [59] ASSISTANT · 2026-08-20 19:01:17 UTC

```
Mentorship is studied but focused on new contributors being mentored. Let me search more specifically for the FOUNDER trajectory scaffolding idea and the "handover of decision-making" angle.
```

### [60] TOOL CALL — terminal · 2026-08-20 19:01:18 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder decision-making power delegation evolution over time trajectory founder involvement decline\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [61] TOOL RESULT — terminal · 2026-08-20 19:01:20 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source founder decision-making power delegation evolution over time trajectory founder involvement decline  [general via ddgs]\nFound: 10 results\n\n1. Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\n   https://arxiv.org/html/2509.16295\n   February 5, 2026 - Yet open-source projects often rely on centralized decision-making, and the determinants of successful community management remain unclear. We analyze 637 GitHub repositories to tra...\n\n2. Avoid the Founder's Trap with Insightful\u2019s Productivity Tool\n   https://www.insightful.io/blog/escaping-founders-trap\n   December 24, 2025 - In the world of tech startups, the growth trajectory can often be hampered by the founder's reluctance to delegate and a tendency to become a bottleneck in decision-making. ... Con...\n\n3. Intersect, Vol 16, No 3 (2023) Evolution of the Founder: Shifts in Delegation\n   https://ojs.stanford.edu/ojs/index.php/intersect/article/download/2661/1579/9678\n   remains limited; most delegation research focuses on established \u00b7 corporations (e.g., Bunderson, 2003; Chen & Aryee, 2007; Schriesheim et \u00b7 al., 1998). Noting this discrepancy, some scholars have exa...\n\n4. Understanding open source governance models\n   https://www.redhat.com/en/blog/understanding-open-source-governance-models\n   January 22, 2026 - Peer review is common under this model, but individual contributors tend to retain de facto decision-making power over project components they've worked on closely. For this reason,...\n\n5. Can one person run an open source project alone? - Stack Overflow\n   https://stackoverflow.blog/2020/09/09/open-source-governance-benevolent-dictator-or-decision-by-committee/\n   September 9, 2020 - We have seen this pattern play out in recent years: van Rossum stepped down, and Torvalds took a break after accusations of rude, aggressive behavior. They added additional decisio...\n\n6. Master the Art of Letting Go: The Founder's Complete Guide to Delegation\n   https://wildfirelabs.substack.com/p/master-the-art-of-letting-go-the\n   May 27, 2025 - Research found that when these ... others, and red decisions needing my input. This framework reduced my involvement in day-to-day choices by about 70% within weeks.\"......\n\n7. The Founder to CEO Transition: The 5 Identity Shifts You ...\n   https://jakesmolarek.com/articles/founder-to-ceo-transition/\n   January 17, 2026 - This is how you trap your business ... Business Review shows that founder-centred firms often struggle to institutionalise decision-making, creating fragility during periods of fast...\n\n8. Resilience in Free/Libre/Open Source Software:\n   https://digital.lib.washington.edu/server/api/core/bitstreams/186f14b1-3a26-47b6-84a7-ef472f4dce04/content\n   I then conduct a time series analysis ... Ideterminethatwhilethedevelopmentactivityofallprojects \u00b7 declines over time, this decline is slower for protectively licensed projects than permissively licen...\n\n9. Mastering Delegation - TimeCraft Advisory\n   https://www.timecraftadvisory.com/blog/how-to-delegate-as-a-founder\n   April 26, 2026 - For founders, particularly in smaller or rapidly growing enterprises, this figure can be even higher when accounting for direct operational involvement. This constant immersion in day...\n\n10. The Founder's Dilemma | Request PDF\n   https://www.researchgate.net/publication/5536880_The_Founder's_Dilemma\n   March 1, 2008 - Wasserman, 2008), we know surprisingly little about the stability of founders' PO toward their ventures, and how this might be affected when decision-making authority is delegated. We ..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder decision-making power delegation evolution over time trajectory founder involvement decline\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [62] ASSISTANT · 2026-08-20 19:02:26 UTC

```
The closest is still the governance-transition paper. Founder→CEO transition is discussed in corporate/startup contexts but NOT in OSS, and NOT as a longitudinal "scaffolding fade curve." Let me search more specifically in scholarly mode for the exact mechanism I'm proposing, and then explore a slightly different angle to see if there's something even more novel.
```

### [63] TOOL CALL — terminal · 2026-08-20 19:02:26 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder fade involvement handover decision transition sustainable open source longitudinal trajectory\" --mode scholarly --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [64] TOOL RESULT — terminal · 2026-08-20 19:02:28 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: founder fade involvement handover decision transition sustainable open source longitudinal trajectory  [scholarly via openalex]\nFound: 9 results\n\n1. If You Can\u2019t Let Go: The Role of Emotional Dependency in Global South\u2013North Social Enterprises\n   https://doi.org/10.1111/joms.13252\n   Journal of Management Studies \u00b7 2025 \u00b7 cited by 2...\n\n2. Teaching Hebrew as an additional language : a classroom-based case study\n   https://openalex.org/W2584065431\n   UTS ePRESS (University of Technology Sydney) \u00b7 2014 \u00b7 cited by 1...\n\n3. Let the people speak : deliberative mini-publics\n   https://doi.org/10.3990/1.9789036552189\n   2021 \u00b7 cited by 0...\n\n4. A Region-based Business Ecosystem for Industrial Upgrading: Evidence from the Electronics Industry of Shenzhen\n   https://doi.org/10.17863/cam.57082\n   Apollo (University of Cambridge) \u00b7 2019 \u00b7 cited by 0...\n\n5. Caught Between the State, the Market, and Civil Society: The Divergent Paths of Chinese Non-Governmental Organizations (NGOs) Seeking to Make Social Change in China\n   https://openalex.org/W2919645921\n   CUNY Academic Works (City University of New York) \u00b7 2018 \u00b7 cited by 0...\n\n6. Challenges Caused by Socioemotional Wealth and Their Management During the Internationalization of Family Firms\n   https://doi.org/10.14267/phd.2026012\n   2026 \u00b7 cited by 0...\n\n7. Making in School and Public Libraries\n   https://doi.org/10.3998/mpub.11500417\n   2020 \u00b7 cited by 0...\n\n8. Seeing Addiction: A Personal Memoir\n   https://doi.org/10.5334/bdf\n   Ubiquity Press eBooks \u00b7 2026 \u00b7 cited by 0...\n\n9. Seeing Addiction\n   https://openalex.org/W7155457975\n   Directory of Open access Books (OAPEN Foundation) \u00b7 2026 \u00b7 cited by 0..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder fade involvement handover decision transition sustainable open source longitudinal trajectory\" --mode scholarly --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [65] ASSISTANT · 2026-08-20 19:02:32 UTC

```
Scholarly search returned mostly irrelevant results, suggesting my specific framing (founder involvement fade trajectory predicting OSS survival) is not a well-studied topic. This is promising for novelty. Let me search for an even more specific concept — the "scaffolding" mechanism and the Vygotsky connection — and also explore one more angle to make sure my idea is the most novel version.
```

### [66] TOOL CALL — terminal · 2026-08-20 19:02:32 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"scaffolding fadevra Vygotsky zone proximal development organizational leadership continuous mentor\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [67] TOOL RESULT — terminal · 2026-08-20 19:02:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: scaffolding fadevra Vygotsky zone proximal development organizational leadership continuous mentor  [general via ddgs]\nFound: 10 results\n\n1. Zone of Proximal Development\n   https://www.simplypsychology.org/zone-of-proximal-development.html\n   October 16, 2025 - Vygotsky\u2019s Term: Actual developmental level (independent problem-solving). What it is: Tasks the learner cannot complete independently but can accomplish with the guidance and suppo...\n\n2. Vygotsky's Zone of Proximal Development: Instructional ...\n   https://files.eric.ed.gov/fulltext/EJ1081990.pdf\n   The current paper examines the instructional implications of Vygotsky's (1978) seminal notion of Zone of Proximal \u00b7 Development, originally developed to account for the learning potential of children,...\n\n3. Vygotsky Scaffolding Theory & Zone of Proximal Development\n   https://cloudassess.com/blog/vygotsky-scaffolding-theory/\n   April 24, 2026 - Yes, scaffolding can be highly effective in corporate leadership development by offering emerging leaders guided experiences and mentorship....\n\n4. Vygotsky's Zone of Proximal Development and Scaffolding - Educational Technology\n   https://educationaltechnology.net/vygotskys-zone-of-proximal-development-and-scaffolding/\n   August 18, 2020 - Vygotsky consistently defines the zone of proximal development as the difference between the current level of cognitive development and the potential level of cognitive development....\n\n5. A Guide To Vygotsky\u2019s Zone Of Proximal Development And Scaffolding\n   https://elearningindustry.com/guide-to-vygotskys-zone-of-proximal-development-and-scaffolding\n   May 12, 2026 - In this context, scaffolding is a learning tool that students use to advance levels in the zone of proximal development. These tasks are completed in small, manageable increments....\n\n6. Vygotsky's Zone of Proximal Development and Scaffolding | Skillshub\n   https://www.skillshub.com/blog/vgotskys-zone-proximal-development-scaffolding/\n   January 5, 2026 - To receive that boost, learners need the following: The presence of someone with more knowledge and skills than they have. Social interactions with a skilful tutor/mentor, which allo...\n\n7. The Zone of Proximal Development: Vygotsky, Scaffolding, and Dynamic Assessment\n   https://www.cognitivepsychology.com/Zone_of_Proximal_Development\n   July 14, 2026 - The zone of proximal development explained: Vygotsky's distinction between independent and assisted performance, the scaffolding process of contingency and fading, internalization from...\n\n8. Vygotsky's Theory in Practice: the ZPD and Scaffolding\n   https://www.structural-learning.com/post/vygotskys-theory\n   2 weeks ago - Vygotsky (1978) described learners' progress within the Zone of Proximal Development through assistance from adults or more capable peers; Wood, Bruner and Ross (1976) later framed tempo...\n\n9. Applying Lev Vygotsky's Theory to Workplace Adult Learning\n   https://lms.eskilled.com.au/blog/lev-vygotsky-learning-theory-in-workplace-setting/\n   June 9, 2026 - In an ideal learning environment, ... in Vygotsky\u2019s work, refers to the temporary support a teacher or mentor provides to help a learner accomplish a task within their ZPD.......\n\n10. Vygotsky's Theory\n   https://www.etsu.edu/teaching/resources/more_resources/vygotsky.php\n   July 12, 2022 - He said we learn best when new ... learned individual, we can master the material and shift our Zone upward. The process of receiving help from others to master material is called \"sca..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"scaffolding fadevra Vygotsky zone proximal development organizational leadership continuous mentor\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [68] ASSISTANT · 2026-08-20 19:03:46 UTC

```
The scaffolding literature is in education/corporate training — not in OSS specifically. Notably item 3 mentions scaffolding for "corporate leadership development" but there's no clear adaptation to OSS founder departure survival. Let me verify corporate "leadership succession via scaffolding fade" hasn't been directly adapted to OSS, and check whether the dynamic of "gradual fade of handover" has been studied.
```

### [69] TOOL CALL — terminal · 2026-08-20 19:03:46 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source key developer turnover replacement transfer knowledge exchange continuity community\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [70] TOOL RESULT — terminal · 2026-08-20 19:03:48 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source key developer turnover replacement transfer knowledge exchange continuity community  [general via ddgs]\nFound: 10 results\n\n1. Knowledge Transfer | VERSO Open Resource Library\n   https://www.openresourcelibrary.com/concepts/knowledge_transfer/\n   Open source communities may organize knowledge sharing sessions, either in-person or virtually, where contributors discuss project-related topics, share insights, and answer questions. While knowledge...\n\n2. How to Transfer Knowledge Across Development Teams - OpenArc\n   https://www.openarc.net/how-to-transfer-knowledge-across-development-teams/\n   February 10, 2026 - Companies with strong knowledge-sharing systems see 25% higher productivity and 35% lower turnover. New hires are 50% more productive when onboarding includes proper knowledge tran...\n\n3. Knowledge Transfer in Software Teams: The Executive Guide\n   https://www.cisin.com/coffee-break/knowledge-transfer-in-software-teams.html\n   KT Must Be Structured and Measured: Move beyond passive documentation. Implement a formal, four-pillar framework (Identification, Codification, Transfer, Measurement) to ensure continuity....\n\n4. Knowledge Transfer: Methods, Plans, and KT Sessio...\n   https://www.featurebase.app/blog/knowledge-transfer-and-kt-sessions\n   1 month ago - A KT session is a focused meeting where someone who holds knowledge hands it off to whoever needs it next. Think of a departing employee briefing their replacement, a senior developer wa...\n\n5. Knowledge Transfer in Software Teams | Relevant Software\n   https://relevant.software/blog/effective-knowledge-transfer-between-software-teams/\n   1 month ago - The process involves deliberately and systematically sharing information, expertise, and insights between team members for a smooth exchange of knowledge and the continuity of projects....\n\n6. Software Developer Turnover Challenges: Key Strategies for Tech Leaders\n   https://devsu.com/blog/navigating-software-developer-turnover-challenges\n   November 4, 2025 - Replacing a developer isn\u2019t just about hiring, it\u2019s about knowledge transfer....\n\n7. Balanced knowledge distribution among software development teams\u2014Observations from open\u2010 and closed\u2010source software development - Shafiq - 2024 - Journal of Software: Evolution and Process - Wiley Online Library\n   https://onlinelibrary.wiley.com/doi/full/10.1002/smr.2655\n   February 13, 2024 - Awareness of how this knowledge evolves and is owned by key developers in a project helps stakeholders reduce risks caused by turnover. To this end, this paper introduces a novel, ...\n\n8. Turnover of Companies in OpenStack: Prevalence and Rationale | ACM Transactions on Software Engineering and Methodology\n   https://dl.acm.org/doi/full/10.1145/3510849\n   [49] profiled the knowledge loss induced by developer turnover and provided tools to help large projects assess the risk of developers who are going to leave a software project. Izquierdo et al. [34] ...\n\n9. 6 examples of open source best practices in knowledge-sharing projects | Opensource.com\n   https://opensource.com/article/21/5/open-source-knowledge-sharing\n   May 8, 2021 - I'll look at six different knowledge-sharing communities that take six approaches to gathering, maintaining, and distributing their best practices. The TODO Group creates and maintains a...\n\n10. A strategic approach to knowledge transfer in IT projects | SoftwareMill Blog\n   https://softwaremill.com/knowledge-transfer-it-project/\n   February 16, 2026 - We exchange knowledge freely between projects and all team members. We build our technical excellence by learning from others and sharing our accomplishments and failures. This mea..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source key developer turnover replacement transfer knowledge exchange continuity community\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [71] ASSISTANT · 2026-08-20 19:03:56 UTC

```
Knowledge transfer in OSS focuses on "knowledge distribution" among current developers, not on the founder's specific fade trajectory over time. Let me also check for related work measuring things like "founder's involvement decline trajectory" using git/PR metadata, which would be the closest direct overlap to my idea.
```

### [72] TOOL CALL — terminal · 2026-08-20 19:03:56 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder involvement decline trajectory open source project survival prediction code review merge decision\" --mode scholarly --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [73] TOOL RESULT — terminal · 2026-08-20 19:03:58 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: founder involvement decline trajectory open source project survival prediction code review merge decision  [scholarly via openalex]\nFound: 10 results\n\n1. The Futures of Indigenous Peoples: 9-11 and the Trajectory of Indigenous Survival and Resistance\n   https://doi.org/10.5195/jwsr.2004.307\n   Journal of World-Systems Research \u00b7 2004 \u00b7 cited by 38...\n\n2. The Rise of Dispersed Ownership: The Roles of Law and the State in the Separation of Ownership and Control\n   https://doi.org/10.2307/797515\n   The Yale Law Journal \u00b7 2001 \u00b7 cited by 470...\n\n3. How Did Employee Ownership Firms Weather the Last Two Recessions? Employee Ownership, Employment Stability, and Firm Survival: 1999-2011\n   https://doi.org/10.17848/9780880995276\n   2017 \u00b7 cited by 70...\n\n4. Merging morphological and genetic evidence to assess hybridization in Western Eurasian late Pleistocene hominins\n   https://doi.org/10.1038/s41559-022-01875-z\n   Nature Ecology & Evolution \u00b7 2022 \u00b7 cited by 57...\n\n5. Entrants in the political arena: new party trajectories during the third wave of democracy in Latin America\n   https://doi.org/10.17615/m3hz-sz66\n   Carolina Digital Repository (University of North Carolina at Chapel Hill) \u00b7 2019 \u00b7 cited by 20...\n\n6. Fashion Openness: Applying an Open Source Philosophy to the Paradigm of Fashion\n   https://openalex.org/W2755928471\n   Aaltodoc (Aalto University) \u00b7 2013 \u00b7 cited by 5...\n\n7. Emerging infectious diseases and biological invasions: a call for a One Health collaboration in science and management\n   https://doi.org/10.1098/rsos.181577\n   Royal Society Open Science \u00b7 2019 \u00b7 cited by 137...\n\n8. Organizational fragmentation and the trajectory of militant splinter groups\n   https://openalex.org/W2339952421\n   ScholarlyCommons (University of Pennsylvania) \u00b7 2015 \u00b7 cited by 5...\n\n9. National Labor Movements and Transnational Connections: Global Labor\u2019s Evolving Architecture Under Neoliberalism\n   https://doi.org/10.15173/glj.v5i3.2283\n   Global Labour Journal \u00b7 2014 \u00b7 cited by 50...\n\n10. Rise and decline of ethno-national movements of Pakistan : domestic and international factors\n   https://openalex.org/W2623262057\n   DSpace@MIT (Massachusetts Institute of Technology) \u00b7 1987 \u00b7 cited by 9..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder involvement decline trajectory open source project survival prediction code review merge decision\" --mode scholarly --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [74] ASSISTANT · 2026-08-20 19:05:07 UTC

```
Scholarly search returned nothing on target — strongly suggesting this specific framing (founder involvement trajectory as survival predictor in OSS) is NOT well-studied. Let me also verify by directly fetching the abandonment/survival empirical paper (1906.08058) to see what factors they used, since that's the closest existing work.
```

### [75] TOOL CALL — terminal · 2026-08-20 19:05:07 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/pdf/1906.08058\" --max-chars 18000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [76] TOOL RESULT — terminal · 2026-08-20 19:05:07 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/pdf/1906.08058\nType: PDF\nLength: 63162 chars (truncated)\n\n--- Content ---\n\nOn the abandonment and survival of open source\nprojects: An empirical investigation\nGuilherme Avelino\u2217, Eleni Constantinou\u2020, Marco Tulio Valente\u2021, Alexander Serebrenik\u00a7\n\u2217Federal University of Piaui, Brazil, gaa@ufpi.edu.br\n\u2020 University of Mons, Belgium, eleni.constantinou@umons.ac.be\n\u2021 Federal University of Minas Gerais, Brazil, mtov@dcc.ufmg.br\n\u00a7Eindhoven University of Technology, The Netherlands, a.serebrenik@tue.nl\nAbstract\u2014Background: Evolution of open source projects fre-\nquently depends on a small number of core developers. The loss\nof such core developers might be detrimental for projects and\neven threaten their entire continuation. However, it is possible\nthat new core developers assume the project maintenance and\nallow the project to survive. Aims: The objective of this paper\nis to provide empirical evidence on: 1) the frequency of project\nabandonment and survival, 2) the differences between abandoned\nand surviving projects, and 3) the motivation and dif\ufb01culties\nfaced when assuming an abandoned project. Method: We adopt a\nmixed-methods approach to investigate project abandonment and\nsurvival. We carefully select 1,932 popular GitHub projects and\nrecover the abandoned and surviving projects, and conduct a sur-\nvey with developers that have been instrumental in the survival\nof the projects. Results: We found that 315 projects (16%) were\nabandoned and 128 of these projects (41%) survived because\nof new core developers who assumed the project development.\nThe survey indicates that (i) in most cases the new maintainers\nwere aware of the project abandonment risks when they started\nto contribute; (ii) their own usage of the systems is the main\nmotivation to contribute to such projects; (iii) human and social\nfactors played a key role when making these contributions; and\n(iv) lack of time and the dif\ufb01culty to obtain push access to the\nrepositories are the main barriers faced by them. Conclusions:\nProject abandonment is a reality even in large open source\nprojects and our work enables a better understanding of such\nrisks, as well as highlights ways in avoiding them.\nIndex Terms\u2014Project abandonment, Truck factor, Bus factor,\nOpen source development, Core developers\nI. INTRODUCTION\nOpen source software (OSS) is crucial for society. Many\nproprietary software systems nowadays depend on open source\nframeworks and libraries, e.g., Instagram publicly acknowl-\nedges the developers responsible for the open source libraries\nused in their site1. Moreover, 72% of GitHub survey partic-\nipants report that they always seek out OSS options when\nlooking for tools2. Importance of OSS also implies growing\ndemands on sustainability of OSS projects. Sustainability of\nOSS projects is, however, a matter of concern since OSS\nprojects are often managed by a small number of developers,\nwithout \ufb01nancial support [1]. For example, OpenSSL, a cryp-\ntography library used by two-thirds of all Web servers, was\nmaintained by a single developer until 2014, when a major\n1https://www.instagram.com/about/legal/libraries/\n2http://opensourcesurvey.org/2017/\nbug, nicknamed Heartbleed, affecting millions of sites was\ndetected in its implementation [2].\nAn easy way to communicate and understand the depen-\ndency of a software project on key developers is the notion of\nTruck Factor (TF), i.e., the minimal number of developers that\nthe project depends on for its maintenance and evolution [3].\nStated otherwise, if the TF developers abandon the project\n(e.g., after being hit by a truck) the project maintenance will be\nheavily affected. Recently, a number of researchers turned their\neyes on the importance of studying the TF of software projects,\nspeci\ufb01cally open source ones. Zazworka et al. [4] were the \ufb01rst\nto propose a heuristic to compute TFs by mining data from\nversion repositories. Cosentino et al. [5] worked on a tool (and\nnovel algorithm) for the same purpose, but targeting git-based\nrepositories. Later, Avelino et al. [6] proposed a heuristic to\nestimate TFs, based on a code authorship metric. However, the\nstudies going beyond measuring TF towards more profound\nunderstanding of what happens when in\ufb02uential TF developers\nleave the project are still missing. We refer to such a situation\nas TF developers detachment (TFDD).\nIn this paper, we investigate TFDD with the aim of iden-\ntifying strategies that help projects to survive. We conduct\na mixed-methods study following a sequential explanatory\nstrategy [7]. We start by collecting, curating, and analyzing a\ndataset of 1,932 popular GitHub projects. Using this dataset,\nwe quantitatively address three research questions: (RQ1)\nHow common are TFDDs in open source projects?, (RQ2)\nHow often open source projects survive TFDDs? and (RQ3)\nWhat are the distinguishing characteristics of the surviving\nprojects? These questions will shed light in the prevalence\nof TFDDs (RQ1), project survival (RQ2), and evolution of\nsurviving and non-surviving projects (RQ3).\nNext, we focus on the projects that survive TFDDs and sur-\nvey 33 developers who assumed the maintenance of a studied\nproject after it was abandoned by its original TF developers.\nOur qualitative investigation aims to answer three more re-\nsearch questions: (RQ4) Do new TF developers perceive risks\nof project discontinuation?, (RQ5) What motivates a developer\nto assume an open source project after a TFDD situation? and\n(RQ6) What project characteristics most facilitate or hamper\nthe work of recently arrived TF developers? We use this survey\nto provide qualitative answers about developers\u2019 awareness\nof TFDD occurences (RQ4), their motivation to assume the\n978-1-7281-2968-6/19/$31.00 \u00a92019 IEEE\narXiv:1906.08058v1  [cs.SE]  19 Jun 2019\n\nresponsibility for the project (RQ5), and enablers and barriers\nthey have experienced while doing so (RQ6).\nOur contributions are threefold. First, we propose a method-\nology to identify TFDDs by mining software repositories\nand particularly to identify systems that survive (Section II).\nSecond, we show that TFDD is not just a theoretical concept.\nFinally, by surveying TF developers that assumed the main-\ntenance of the surviving systems, we reveal their motivations\nand dif\ufb01culties they faced when doing so.\nII. TRUCK FACTOR\nIn this section, we \ufb01rst de\ufb01ne concepts pertaining to TF.\nThen, we describe the approach used in the study to calculate\nTF, identify TFDD and the systems that survived it.\nThe key de\ufb01nitions used throughout this paper are as follows:\n\u2022 Truck factor (TF) is the minimal number of developers of\na project that have to be hit by a truck (or quit) before the\nproject gets in serious trouble [3], [4], [8].\n\u2022 TF\ndevelopers\nare\nthe\nminimal\nset\nof\ndevelopers\n{d1, d2, ..., dn} corresponding to TF. Typically, algorithms\nestimating TF also compute this set.\n\u2022 TF developers detachment (TFDD) occurs when all TF\ndevelopers abandon the project.\n\u2022 Surviving system is a system that survives a TFDD, by\nattracting new TF developers who assume its maintenance.\nA. Truck Factor Calculation\nTo estimate truck factors we use the algorithm proposed by\nAvelino et al. [6]. The selected TF algorithm initially calculates\nthe degree of authorship (DOA). DOA [9], [10] is a metric\nre\ufb02ecting a developer\u2019s expertise on each \ufb01le of the project\nrelatively to the expertise of other developers on the same\n\ufb01le. Expertise of a developer on a \ufb01le is operationalized as the\nfunction of whether the developer has created the \ufb01le, and the\nnumber of changes they did on the \ufb01le compared to changes\nperformed by other developers. Finally, TF estimation relies\non the assumption that TF developers are the main authors,\ni.e., with the highest DOA, of at least 50% of the system\u2019s\n\ufb01les. We stress that there maybe more than one main author\nper \ufb01le, as indicated in the TF algorithm description [6]. The\nreasons for choosing this algorithm are fourfold: (1) it has\nthe best precision and recall in a recent study comparing\nthree algorithms for estimating truck factors [11]; (2) it scales\nto large projects with hundreds of contributors; (3) it was\nvalidated by surveying the developers of 67 popular GitHub\nprojects [6]; (4) it has a public implementation on GitHub.3\nB. Identifying Truck Factor Developers Detachments\nTo search for TFDDs, we \ufb01rst estimate the TF of a system at\na time t and verify whether the TF developers abandoned the\nsystem before t. We say that a developer abandoned a project\nif their last commit occurred at least one year before the most\nrecent repository commit. Existing studies rely on different\nthresholds to classify developers inactivity or departure from\n3https://github.com/aserg-ufmg/truck-factor\nJan/2012\nJan/2015\nJan/2016\nToday\nTF = 1\n{Alice}\n...\nDec/15\nBob\nlast commit\n...\nTF = 2\n{Alice, Bob}\nAug/15\nAlice\nlast commit\nTFDD\nFigure 1. TFDD on composer/satis\na project, including three months [12], six months [13], [14],\nand one year [15], [16]. We experimentally test the sensitivity\nof \ufb01ve thresholds, in Section III-C, and select the one-year\nthreshold as it is the least sensitive to error.\nExample: For the sake of simplicity we do not reproduce the\nalgorithm here, instead we illustrate how it is used in our\ncontext. Figure 1 illustrates a fragment of the composer/satis4\ndevelopment history5. Suppose we \ufb01rst compute the system\u2019s\nTF in January 2015. At this point, the TF estimated by the\nalgorithm equals one, since Alice is the (unique) TF developer.\nAs Alice is active in January 2015 (she has a commit after\nthis date), no TFDD is observed. When we compute TF in\nJanuary 2016, TF increases to two, with Alice and Bob as\nthe TF developers. Moreover, both developers abandoned the\nproject before this date: Alice in August 2015 (date of her last\ncommit) and Bob in December 2015. Therefore, the developers\nof composer/satis detached from the project in December 2015.\nC. Identifying Surviving Systems\nBy de\ufb01nition of TF, TFDDs are expected to have a major\nimpact on the evolution of the software project. However,\nprojects can survive such situations. In other words, an occur-\nrence of TFDD does not necessarily imply project termination,\ne.g., if new developers have taken charge of the project.\nWe assume a project can be in two states: Active, when\nat least one TF developer is active; and Inactive, when all TF\ndevelopers have abandoned the project. When a TFDD occurs,\nthe system is moved from Active to Inactive; reversely, the\nattraction of at least one new TF developer moves the project\nback to Active. Our central object of study are systems with a\ntransition from Inactive to Active w.r.t. the last occurrence of\nTFDD; such systems are considered as having survived since\nthey became active after their last TFDD.\nExample: As illustrated in Figure 2, a TFDD occurs in our\nrunning example (composer/satis) on December 2015, when\nboth TF developers abandoned the project. Therefore, in this\ndate, the project moved to an Inactive state. However, in\nJanuary 2017, the recomputation of the TF developers resulted\nin a new developer in this set, Charlotte.6 The attraction of\nthis developer\u2014someone with important contributions to the\npoint of reaching a TF status\u2014moves the project back to the\nActive state. Thus, we say composer/satis survived the TFDD.\n4https://github.com/composer/satis\n5To preserve the privacy of the contributors involved, we replace their\nusernames with pseudonyms.\n6We compute TFs every year, starting from the repository creation date.\n\nJan/2012\nJan/2016\nToday\n...\nDec/15\nTFDD\n...\nTF = 2\n{Alice, Bob}\nJan/2017\nTF = 2\n{Bob, Charlotte}\nSystem Survived\nNew TF developer\nFigure 2. Surviving TFDD on composer/satis\nTable I\nNUMBER OF PROJECTS BY LANGUAGE.\nLanguage\nProjects\nLanguage\nProjects\nRuby\n398 (21%)\nPHP\n334 (17%)\nJavaScript\n342 (17%)\nPython\n297 (15%)\nC/C++\n335 (17%)\nJava\n226 (12%)\nIII. STUDY DESIGN\nWe adopt a mixed-methods approach and combine a large\nscale analysis of version control repository data with a sur-\nvey. Mixed-methods are appropriate for the pragmatic stance\ncommon in software engineering research [7].\nA. Dataset & Preprocessing\nTo perform the quantitative part of the study, we build\na dataset with GitHub projects. Initially, we focus on six\nprogramming languages with the largest number of GitHub\nrepositories: JavaScript, Python, Ruby, C/C++, Java, and PHP.\nWe select the top-500 most starred repositories (excluding\nforks to avoid including the same project multiple times) for\neach of those languages at the moment of analysis. We focus\non popular projects to ensure the quality of the data, so that\nthe collected projects are relevant to the OSS community, and\nto avoid including personal projects in our dataset [17], [18].\nTo safeguard the quality of the dataset we \ufb01lter the resulting\ncollection of 3,000 GitHub repositories. We explicitly address\nwell-known \u201cperils of mining GitHub\u201d [17]. We exclude (a)\nprojects that did not use GitHub exclusively during their\nentire history and lost part of their development history when\nmigrated to GitHub, (b) projects that do not have suf\ufb01cient\nhistorical data for the TF computation, and (c) projects that\nare not software units or are explicitly labeled as unmaintained.\nTo identify projects with evidence of loss of part of their\ndevelopment history we \ufb01lter out repositories where more than\n50% of the \ufb01les are added in less than 20 commits in the begin-\nning of their development. By applying this \ufb01lter, we exclude\n677 projects. As our approach to identify TFDD requires at\nleast two years of historical data, we \ufb01lter out 338 projects\nwith less than two years of development activity. To apply\nthe last \ufb01lter we manually inspect the project descriptions\nand exclude 53 projects. Among others, we found repositories\ncontaining books, awesome-lists (i.e., sets of suggested books,\nlinks, etc.), and technology code samples. The resulting dataset\nis composed of 1,932 (= 3, 000 \u2212677 \u2212338 \u221253) projects.\nAs shown in Table I, most projects are implemented in\nRuby (398 projects, 21%). On the other side, Java is the\n72\n10\n1k\nDevelopers\nDevelopers\n228\n100\n10k\nFiles\nFiles\n1.3k\n1k\n100k\nCommits\nCommits\n3k\n1k\n10k\n100k\nStars\nStars\nFigure 3. Distribution of the number of developers, commits, \ufb01les, and stars.\n11\n1\n10\n100\nAliases (%)\nFigure 4. Percentage of aliases in each project\nlanguage with fewest projects (226 projects, 12%). Figure 3\nshows violin plots with the distribution of the number of\ndevelopers, source code \ufb01les, commits and stars per project\n(please note the logarithmic scale). The median values are\nindicated inside the violin plots. We conclude that the dataset\nconstructed typically includes large systems, both in size and\nin number of developers, and that the systems also are popular\n(number of stars) and have a large number of commits.\nB. Aliases Resolution\nThe correctness of TF computations highly depends on\nthe set of distinct developers. However, developers do not\nnecessarily use only one alias (name or e-mail address) when\ncontributing to a project [19], [20], [21]. Therefore, it is\nimportant to detect and resolve aliases among the developers of\nthe 1,932 projects in our dataset. Rather than using heuristics\nadvocated in previous works to detect aliases [19], [20], [21],\nwe use a feature of the GitHub API that maps an e-mail\naddress in the commit header to a GitHub user. Using this\nfeature, we mapped each developer of each system to their\nGitHub account; d1 and d2 are considered aliases when they\nare mapped to the same GitHub account. As a downside,\nthis approach does not handle the cases where developers\nhave multiple GitHub accounts. Figure 4 shows a violin plot\nwith the percentage of aliases in each project. The median\npercentage of aliases in a project in our dataset is 11%.\nC. Abandoner Threshold Sensitivity Analysis\nThe selected threshold value to identify developers aban-\ndoning projects can impact our results. We therefore test\nthe sensitivity to error of \ufb01ve different threshold values,\ni.e., 3 months, 0.5 year, 1 year, 1.5 year and 2 years, to\nselect the most appropriate threshold. We \ufb01rst gather each TF\ndeveloper\u2019s commit activity and then measure the elapsed time\ndelta between consecutive commits. For each TF developer\nwith N commits, we compute N \u22121 inter-commit time deltas.\n\nTable II\nTHRESHOLD SENSITIVITY\nTi\nP (Ti)\nimpr(Ti, Ti\u22121)\nharmonic_mean\n3 months\n0.38\n-\n-\n6 months\n0.59\n0.35\n0.44\n1 year\n0.82\n0.55\n0.66\n1.5 year\n0.91\n0.50\n0.64\n2 years\n0.95\n0.46\n0.62\nSince each time delta represents the time elapsed between\ncommits, developers should never be classi\ufb01ed as abandoners\nby a threshold. In other words, appropriate thresholds should\noptimally have zero error, meaning that they will never erro-\nneously classify a developer as an abandoner, as by de\ufb01nition\nshe has at least one subsequent commit.\nTo assess the error sensitivity of a list of thresholds TS\nwhere TS = \u27e8T1, T2, ..., TN\u27e9such that Ti < Ti+1 for i \u2208\n1...N \u22121, we used the precision and improvement metrics, as\nwell as their harmonic mean. Precision P(Ti) of a threshold\nTi is de\ufb01ned as the percentage of developers that Ti has zero\nerror, i.e., Ti never classi\ufb01es them as abandoners. Improvement\nimpr(Ti, Ti\u22121) of Ti over the smaller threshold Ti\u22121 is de\ufb01ned\nas the number of developers that Ti has zero error, while Ti\u22121\nerroneously classi\ufb01es as abandoners over the total number of\ndevelopers that Ti\u22121 erroneously classi\ufb01es as abandoners. In\npractice, impr(Ti, Ti\u22121) measures how many errors of Ti\u22121\nwere corrected by Ti. The harmonic mean between precision\nand improvement is de\ufb01ned as 2\u2217P \u2217impr\nP +impr .\nTable II presents the sensitivity analysis results for the \ufb01ve\nthreshold values considered. The precision results indicate\nthat a certain amount of error is introduced regardless of the\nthreshold, e.g., even a 2-year threshold produced an error of\n5%. On the contrary, the largest improvement is achieved\nby the 1-year threshold (55%) over the 6-months threshold,\nindicating that more than half of the errors made by the 6-\nmonth threshold were \ufb01xed by the 1-year threshold. Overall,\nthe 1-year threshold achieves"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/pdf/1906.08058\" --max-chars 18000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [77] ASSISTANT · 2026-08-20 19:05:18 UTC

```
This is excellent context. The Avelino et al. (2019) paper:
- Defines TF (truck factor), TF developers, TFDD (truck factor developers detachment), surviving system
- Identifies projects where ALL TF developers abandoned → then new TF developer appeared = survived
- For SURVIVING projects, surveyed new TF developers on motivations/barriers
- KEY: They look at STATIC factors distinguishing abandoned vs surviving (basic repo metrics)
- They DO NOT consider the founder's INVOLVEMENT TRAJECTORY over time
- They DO NOT consider whether the founder gradually reduced involvement (fading) vs. abrupt departure
- They DO NOT model "scaffolding fade" as a mechanism

This is strongly differentiated from my hypothesis. Let me confirm this is the strongest prior work and check the results section.
```

### [78] TOOL CALL — terminal · 2026-08-20 19:05:18 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/pdf/1906.08058\" --pattern \"(RQ3|distinguishing|differences between|predicted|features|factors).*\" -i --max-matches 15 --context-chars 250",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [79] TOOL RESULT — terminal · 2026-08-20 19:05:18 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/pdf/1906.08058\nType: PDF\nPattern: (RQ3|distinguishing|differences between|predicted|features|factors).* (26 matches in 63162 chars)\n\n--- Content ---\n\n894:...on. However, it is possible\nthat new core developers assume the project maintenance and\nallow the project to survive. Aims: The objective of this paper\nis to provide empirical evidence on: 1) the frequency of project\nabandonment and survival, 2) the differences between abandoned\nand surviving projects, and 3) the motivation and dif\ufb01culties\nfaced when assuming an abandoned project. Method: We adopt a\nmixed-methods approach to investigate project abandonment and\nsurvival. We carefully select 1,932 popular GitHub projects and\n...\n--\n1740:...urvey indicates that (i) in most cases the new maintainers\nwere aware of the project abandonment risks when they started\nto contribute; (ii) their own usage of the systems is the main\nmotivation to contribute to such projects; (iii) human and social\nfactors played a key role when making these contributions; and\n(iv) lack of time and the dif\ufb01culty to obtain push access to the\nrepositories are the main barriers faced by them. Conclusions:\nProject abandonment is a reality even in large open source\nprojects and our work enables a better understanding of such\nr...\n--\n4722:...curating, and analyzing a\ndataset of 1,932 popular GitHub projects. Using this dataset,\nwe quantitatively address three research questions: (RQ1)\nHow common are TFDDs in open source projects?, (RQ2)\nHow often open source projects survive TFDDs? and (RQ3)\nWhat are the distinguishing characteristics of the surviving\nprojects? These questions will shed light in the prevalence\nof TFDDs (RQ1), project survival (RQ2), and evolution of\nsurviving and non-surviving projects (RQ3).\nNext, we focus on the projects that survive TFDDs and sur-\nvey 33 developers who assumed the maintenance of a studied\nproject after it was abandoned by its original TF developers.\nOur qualitative investigation aims to answer three more re-\nsearch qu...\n--\n7017:... set.\n\u2022 TF developers detachment (TFDD) occurs when all TF\ndevelopers abandon the project.\n\u2022 Surviving system is a system that survives a TFDD, by\nattracting new TF developers who assume its maintenance.\nA. Truck Factor Calculation\nTo estimate truck factors we use the algorithm proposed by\nAvelino et al. [6]. The selected TF algorithm initially calculates\nthe degree of authorship (DOA). DOA [9], [10] is a metric\nre\ufb02ecting a developer\u2019s expertise on each \ufb01le of the project\nrelatively to the expertise of other developers on the same\n\ufb01le...\n--\n7949:...ybe more than one main author\nper \ufb01le, as indicated in the TF algorithm description [6]. The\nreasons for choosing this algorithm are fourfold: (1) it has\nthe best precision and recall in a recent study comparing\nthree algorithms for estimating truck factors [11]; (2) it scales\nto large projects with hundreds of contributors; (3) it was\nvalidated by surveying the developers of 67 popular GitHub\nprojects [6]; (4) it has a public implementation on GitHub.3\nB. Identifying Truck Factor Developers Detachments\nTo search for TFDD...\n--\n19637:...have low TFs. In a sample of\n1,932 projects, 57% have TF = 1 and 25% have TF = 2.\nThe highest TF in our sample is 26 developers.\nIn the remainder of this section, we describe a quantitative\nexploration of the collected data, aiming to answer (RQ1)\u2013\n(RQ3). We start by assessing whether TFDDs indeed happen\nin open source development (RQ1). Assuming that TFDDs\nindeed occur, RQ2 takes a step further and investigates how\noften projects overcome such situations. Finally, assuming we\n\ufb01nd projects that survived their TFDDs, we compare them\nwith other projects that did not have the same fate (RQ3). The\ngoal is to identify characteristics that might help projects to\novercome the loss of TF developers.\nRQ1) How common are TFDDs in GitHub projects?\nWe identify TFDDs in 315 projects, 16% of our dataset.\nMost of the projects faced only one TFDD situati...\n--\n24931:...wever, a signi\ufb01cant part\nof the projects survived with the help of newcomers (41%) or\nby attracting both newcomers and old contributors (7%).\nNewcomers are crucial to recover from TFDDs. They\ncontributed to recovery of 48% of the surviving projects.\nRQ3) How surviving projects differ from non-surviving ones?\nFigures 10 and 11 show respectively the distribution of\nthe absolute number and the percentage of commits after the\nlast detected TFDD in each surviving project (128 projects)\n\n56\n15\n0\n25\n50\n75\n100\nSurviving\nNon\u2212surviving\nCommits (%)\nFigure 11. Perc...\n--\n26748:... of Romano et al. [23], is large in both cases: d = 0.64\nfor the number of commits, and d = 0.79 for the percentage\nof commits after the last TFDDs.\nWe also explore the differences, if any, between surviving\nand non-surviving systems w.r.t different factors in order to\nreveal if such factors can provide insights related to project\nsurvival. Figure 12 shows violin plots with the distributions of\nthe number of developers, commits and \ufb01les, and project age\nmeasured in days of the surviving and non-surviving projects.\nAll values refer to the date of the studied TFDDs. We test the\ndifferences between surviving and non-surviving projects us-\ning two-sided Mann-Whitney tests and by visually con\ufb01rming\nthe differences using the visualizations of Figure 12. Since we\nconsider different aspects of the same projects we adjust the\np-values to control for multiple comparisons using the method\nof...\n--\n37471:...to my ongoing contributions\" (D11). Among others, technical\ncharacteristics include the usage of a speci\ufb01c programming\nlanguage (4 answers) or following well-known software engi-\nneering principles and practices (4 answers). The last category\ngroups factors like permission to access the main repository\n(3 answers) and \ufb01nancial support by a company (2 answers).\nFour respondents did not answer this question.\nThe characteristics that helped on the attraction of new\nTF developers have a social, technical or external nature.\nFriendly and active maintai...\n--\n38623:...ers. Particularly, lack of time is\nthe most common barrier mentioned by the survey participants\n(7 answers). As examples, we have these answers: \u201cI have\nother projects to maintain.\" (D3); and \u201ctime is always an issue,\nespecially because the range of features is fairly wide\" (D23).\nTechnical barriers include the requirement to keep backward\ncompatibility and do not introduce bugs (4 answers) and\nthe lack of solid software engineering principles (1 answer).\nAnother barrier commonly mentioned by the participants is the\ndif\ufb01culty...\n--\n[11 more matches not shown]"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/pdf/1906.08058\" --pattern \"(RQ3|distinguishing|differences between|predicted|features|factors).*\" -i --max-matches 15 --context-chars 250", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [80] ASSISTANT · 2026-08-20 19:06:28 UTC

```
Confirmed. The Avelino et al. 2019 paper uses STATIC factors at the TFDD date (number of developers, commits, files, project age) using simple Mann-Whitney tests — NOT a temporal trajectory of founder involvement. My hypothesis is well-differentiated.

Let me now also check the recent OSS literature review and the bus factor calculation papers, and think about feasibility. Let me search for the most recent attempts that might overlap with the trajectory idea.
```

### [81] TOOL CALL — terminal · 2026-08-20 19:06:28 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder involvement trajectory temporal decline predict project death or health longitudinal code review mentor\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [82] TOOL RESULT — terminal · 2026-08-20 19:06:30 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source founder involvement trajectory temporal decline predict project death or health longitudinal code review mentor  [general via ddgs]\nFound: 10 results\n\n1. Beyond Code Contributions: How Network Position, Temporal Bursts, and Code Review Activities Shape Contributor Influence in Large-Scale Open Source Ecosystems\n   https://arxiv.org/html/2602.06426\n   February 6, 2026 - However, the decline is sub-linear, indicating that influence concentration mechanisms (preferential attachment) partially offset network expansion. Panel (c) tracks temporal trajec...\n\n2. Do Good, Stay Longer? Temporal Patterns and Predictors of Newcomer-to-Core Transitions in Conventional OSS and OSS4SG\n   https://arxiv.org/html/2601.23142v1\n   January 30, 2026 - Our predictive models indicate that contributors who modify files across many project areas show higher likelihood of achieving core status (ROC-AUC = 0.746). This metric is directl...\n\n3. Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI\n   https://arxiv.org/html/2602.09064\n   February 13, 2026 - Mining Software Repositories (MSR) research has long leveraged machine learning techniques to analyze large-scale repository data for tasks such as defect prediction, maintainabili...\n\n4. The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics\n   https://arxiv.org/html/2605.11844\n   May 12, 2026 - RQ2 (Evolutionary): This study identified the universal mechanism of collapse, a \u201cdeath spiral\" characterized by social abandonment, an exponential increase in backlog, declining innova...\n\n5. How to characterize the health of an Open Source Software project? A snowball literature review of an emerging practice | Proceedings of the 18th International Symposium on Open Collaboration\n   https://dl.acm.org/doi/10.1145/3555051.3555067\n   Open Source Software Survivability Prediction Using Multi Layer Perceptron. In Proc. of 28th Int. conf. on Software Engineering and Data Engineering, Vol. 64. EPiC Series in Computing, San Diego, CA, ...\n\n6. Analyzing Key Features of Open Source Software Survivability with Random Forest\n   https://www.mdpi.com/2076-3417/15/2/946\n   January 18, 2025 - These studies have provided valuable insights into the factors influencing OSS projects\u2019 health, but they have often failed to incorporate the temporal aspects of issue resolution a...\n\n7. Cheating Death: A Statistical Survival Analysis of Publicly\n   http://www1.chapman.edu/~linstead/aliMSR2020.pdf\n   to predict the health of an open source project at the time of its...\n\n8. (PDF) Turnover in Open-Source Projects: The Case of Core Developers\n   https://www.researchgate.net/publication/344078871_Turnover_in_Open-Source_Projects_The_Case_of_Core_Developers\n   October 23, 2020 - We analyzed over 35 million PRs across 50,804 GitHub repositories, identifying 95,958 disengagement bursts (one or more core contributors becoming inactive for >365 days within the ...\n\n9. An empirical study on the survival rate of GitHub projects | Proceedings of the 19th International Conference on Mining Software Repositories\n   https://dl.acm.org/doi/abs/10.1145/3524842.3527941\n   Lingfeng Bao, Xin Xia, David Lo, and Gail C. Murphy. 2021. A Large Scale Study of Long-time Contributor Prediction for GitHub Projects. IEEE Trans. Software Eng....\n\n10. (PDF) Community Engagement and the Lifespan of Open-Source Software Projects\n   https://www.researchgate.net/publication/397839169_Community_Engagement_and_the_Lifespan_of_Open-Source_Software_Projects\n   November 22, 2025 - Non-parametric tests and correlations assessed relationships with project dynamics and lifespan across quartiles. Results: CE metrics significantly associate with project dynamics,..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder involvement trajectory temporal decline predict project death or health longitudinal code review mentor\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [83] ASSISTANT · 2026-08-20 19:06:36 UTC

```
Important finds — items 3, 4, 6, 8 are directly in my neighborhood:
- "Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures" (Feb 2026)
- "The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics" (May 2026)
- "Analyzing Key Features of OSS Survivability with Random Forest" (2025) — mentions "failed to incorporate temporal aspects"
- "Turnover in Open-Source Projects: The Case of Core Developers" (35M PRs, disengagement bursts)

The "Death Spiral" paper sounds VERY close. Let me fetch it immediately and the temporal prediction paper to assess overlap precisely.
```

### [84] TOOL CALL — terminal · 2026-08-20 19:06:36 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2605.11844\" --max-chars 18000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [85] TOOL RESULT — terminal · 2026-08-20 19:06:38 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2605.11844\nType: HTML\nLength: 133984 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n\u00d7\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) \u00d7\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2605.11844v1 \"Back to abstract page\") [ Download PDF](/pdf/2605.11844v1 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Literature Review\n     1. 2.1 The \u201cMacro\" View: Factors in OSS Project Mortality\n     2. 2.2 The \u201cMicro\" View: PR Dynamics as Health Indicators\n     3. 2.3 The Role of Automation and Bot Activity\n     4. 2.4 The Research Gap\n  4. 3 Research Design and Methodology\n     1. 3.1 Research Questions and Hypotheses\n        1. 3.1.1 RQ1: Descriptive Dynamics of PR Friction\n        2. 3.1.2 RQ2: Evolutionary Post-Mortem of Workflow\n        3. 3.1.3 RQ3: Explanatory Modeling of Lifespan\n     2. 3.2 Data Collection & Sample Definition\n        1. 3.2.1 Data Source\n        2. 3.2.2 Inactive Project Sample Definition\n     3. 3.3 Data Preparation and Operationalization\n        1. 3.3.1 Bot Filtering and Preprocessing\n        2. 3.3.2 Work Type Classification (Label Analysis)\n        3. 3.3.3 Sentiment Analysis\n           1. Aggregation.\n        4. 3.3.4 Lifecycle Quartile Definition (RQ2)\n     4. 3.4 Analysis Methods\n        1. 3.4.1 RQ1: Descriptive Dynamics\n        2. 3.4.2 RQ2: Evolutionary Post-Mortem\n        3. 3.4.3 RQ3: Explanatory Modeling\n  5. 4 Results\n     1. 4.1 Baseline Comparison: Active vs. Inactive Cohorts\n     2. 4.2 Descriptive Statistics (RQ1 Foundation)\n     3. 4.3 RQ1: Descriptive Dynamics of PR Friction\n     4. 4.4 RQ2: Evolutionary Post-Mortem of Workflow\n     5. 4.5 RQ3: Explanatory Modeling of Lifespan\n  6. 5 Case Studies\n     1. 5.1 Simple-Gallery\n     2. 5.2 Facebook Buck\n     3. 5.3 ReactiveCocoa\n  7. 6 Discussion\n  8. 7 Threats to Validity\n     1. 7.1 Internal Validity\n     2. 7.2 Construct Validity\n     3. 7.3 External Validity\n     4. 7.4 Conclusion Validity\n  9. 8 Conclusion and Future Work\n  10. References\n\n\n\n[ License: CC BY-NC-ND 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2605.11844v1 [cs.SE] 12 May 2026\n\n# The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics\n\nMohit Kaushik, Kuljit Kaur Chahal  Affiliation: Department of Computer Science, Guru Nanak Dev University, , Amritsar, 143005, Punjab, India\n\n###### Abstract\n\nOpen Source Software projects (OSS) are central to modern technology, yet their survival rates remain low. Prior research has examined project mortality through macro-level indicators such as commit activity, developer abandonment, and ecosystem dependencies, but the micro-level dynamics of the Pull Request (PR) workflow have been largely overlooked. This study provides the first large-scale post-mortem analysis of PR workflows across 1,736 inactive GitHub repositories and 1.3 million human-driven PRs. Using a mixed-method quantitative design, we investigate three dimensions of mortality. First, our comparative descriptive analysis shows that workflow friction, extended review cycles, and negativity penalties are endemic properties of the entire GitHub platform across both active and inactive projects. Rejected PRs consistently attract higher discussion and negativity regardless of project health. Second, our evolutionary analysis identifies a universal \u201cdeath spiral\" marked by declining innovation rates, exponential backlog growth, rising merge latency. The collapse was defined by silence and disengagement. Labeling formalization remained endemic throughout the lifecycle, while toxicity did not intensify. Finally, our explanatory modeling demonstrates that project lifespan is not determined by workflow efficiency but by inherent value and ecosystem dynamics. Popularity and innovation emerge as strong positive predictors of survival, while friction, rejection rates, labeling formalization, and negativity scale with longevity as byproducts rather than causes of failure. Robustness checks across alternative inactivity thresholds confirm these findings. Together, this work reframes OSS mortality as a socio-technical phenomenon in which abandonment and ecosystem value dominate survival outcomes, while PR-level workflow discipline plays a secondary role.\n\n###### Keywords:\n\nOpen Source Software , Project Mortality , Pull Request Workflow , Survival Analysis , Community Dynamics\n\n\u2020\u2020footnotetext: Accepted for publication in the Journal of Systems and Software.\n\n## 1 Introduction\n\nOpen-source software (OSS) has transformed the traditional way of building and distributing software [23]. Numerous organizations use OSS to some extent [34]. Some popular projects, such as Linux, Android, and the Apache ecosystem, show its widespread adoption and role in shaping the entire industry [23]. While a community celebrates the success of OSS adoption, another community continuously highlights its failures. Previous studies report that 50% of projects across major ecosystems npm, R, WordPress, and Laravel) eventually die [12]. This failure rate is not just limited to some ecosystems rather it is common for all projects [3]. However, the impact of this mortality is represented by critical vulnerability in the global software supply chain. When a project is abandoned, it creates a \u201czombie dependency.\" It remains in use but no longer receives security patches. Recent research indicates that over 42% of npm packages have not been updated in more than two years [47, 49]. The consequences of this neglect were illustrated by the Log4j crisis, where a vulnerability compromised millions of systems globally. Furthermore, project mortality imposes a severe economic cost on downstream dependencies [37]. If the upstream fails or has vulnerabilities, these will trickle down to their downstream projects. Therefore, understanding the early micro-signals of this decline is important for securing critical software infrastructure. This contrast between the success stories and failure rate highlights a survivorship bias \u2020\u2020 It is a tendency to focus on popular, \u201csurviving\u201d projects while overlooking the vast number of projects that failed or were abandoned.\n\nA significant number of studies have investigated the causes and predictors of project failure, often using post-mortem methodologies. Prior work has highlighted factors contributing to project abandonment, such as the loss of core developers [13, 6], abandonment of upstream dependencies [21], and maintainer burnout [12]. Other studies have applied survival analysis [50], machine learning prediction models [11, 35], and ecosystem perspectives [55]. Together, these studies suggest that project mortality is influenced by a combination of technical, social, and organizational factors.\n\nWhile these macro-level factors are important, the dynamics of day-to-day workflows have received far less attention [19, 44]. Some research has examined workflow indicators to assess project health and to distinguish between active and dormant projects [25, 32], but the emphasis has largely been on measuring activeness rather than modeling them as predictors of survival or decline. In particular, pull request (PR) dynamics have been overlooked in mortality research [4, 62]. Within modern OSS ecosystems such as GitHub, the PR workflow serves as the central hub of innovation, governance, and community interaction [56]. It is therefore the most logical place to observe early symptoms of decline, including stalled merges, expanding backlogs, community friction, and diminishing discussion [5, 52]. To the best of our knowledge, no prior study has conducted a post-mortem analysis of PR workflows to understand project mortality. We address this gap by analyzing 1,736 inactive OSS projects (comprising \u2248\\approx1.3 million human-driven PRs) alongside a structurally matched control group of 1,736 active projects (comprising \u2248\\approx2.67 million human-driven PRs). Together, this dataset of nearly 3.97 million pull requests and over 6.33 million comments allows us to isolate genuine signals of decline from platform-wide norms.\n\nIn this study, we define Project Mortality as the permanent end of development activity, including commits and merges. It is important to note that not all inactivity signals failure. As shown in our case studies (Section 5), inactivity can result from Strategic Completion, where a project fulfills its purpose and is archived (for example, Facebook Buck). It can also result from Abandonment, where contributors leave due to friction (for example, Simple-Gallery).\n\nWhile the intent behind these outcomes differs, the workflow signals are the same. Silence, backlog growth, and the end of maintenance all appear in the pull request record. For this reason, we use the term Mortality to cover the range of end-states where a project stops functioning as an active software effort.\n\nThe contributions of this study are:\n\n  1. 1.\n\nRQ1 (Descriptive): We observed that process friction and negativity are platform-wide norms rather than unique markers of death. By comparing inactive projects against the active baseline, we found that rejected PRs consistently attract higher discussion volume and negative sentiment regardless of a project\u2019s overall health. Therefore, the presence of day-to-day workflow friction is a universal characteristic of open-source collaboration, rather than a direct cause of project mortality.\n\n  2. 2.\n\nRQ2 (Evolutionary): This study identified the universal mechanism of collapse, a \u201cdeath spiral\" characterized by social abandonment, an exponential increase in backlog, declining innovation rates, and a resulting spike in merge friction. Labeling formalization remained endemic throughout the lifecycle, and toxicity did not intensify. Instead, collapse was marked by silence and disengagement.\n\n  3. 3.\n\nRQ3 (Explanatory): We demonstrated that lifespan is predicted by inherent project value and ecosystem dynamics rather than workflow efficiency. While popularity and innovation are strong predictors of lifespan, we also found an increasing prevalence of workflow issues, including labeling formalization, high rejection rates, and negative interactions, in aged projects. These dynamics appear as byproducts rather than causes of project failure. Robustness across different inactivity thresholds further confirms these findings.\n\n\n\n\nThe remainder of this paper is organized as follows: Section 2 reviews related work on pull request workflows and project mortality. Section 3 describes the methodology of the study. Section 4 then presents the results, followed by Section 5, which aligns our findings with specific project examples. Section 6 interprets the findings, and Section 7 discusses limitations and threats to validity. Finally, Section 8 concludes the study and suggests directions for future research.\n\n## 2 Literature Review\n\nOSS projects often face survival challenges. A project may exhibit early signs of decline that can be observed in day-to-day PR workflows. Prior works have explored these projects\u2019 decline indicators from different viewpoints, highlighting the necessity of synthesis. Therefore, this section is structured around two complementary perspectives. Section 2.1 discusses macro-level indicators at the project level, while Section 2.2 explains them from the micro-dynamics of pull requests. Section 2.3 discusses the role of automation or bot activities, and Section 2.4 highlights the gap that our study addresses.\n\n### 2.1 The \u201cMacro\" View: Factors in OSS Project Mortality\n\nBased on our review, we categorize the macro factors into five different categories.\n\nSocio-technical and Human Infrastructure: As OSS projects are typically developed by a community of developers, the human infrastructure is a crucial component of a project\u2019s survival. This refers to the composition, behavior, organization, and stability of a community. Most OSS projects rely on a small number of core developers. Their abandonment or detachment is often measured by \u201cTruck Factor\" or \u201cDeveloper Detachment\" (TFDD). Analyzing the TFDD, Avelino et al. [6] found that 65% of projects had a TF of 1 or 2. This indicates the project\u2019s fragility and dependence on a very small number of developers. Similarly, Nourry et al. [43] analyzed over 36,000 projects and noted that 89% of projects experienced at least one TFDD. The loss of these core developers contributes to a project\u2019s decline. They also reported that only 27% of projects survived a TFDD by attracting new core developers. The survival also becomes difficult if a TFDD occurs early, specifically within the first three years of a project\u2019s life [43]. In addition to TFDD, team size also impacts the project survival. However, it is often debated that merely the sheer volume of contributors does not guarantee survival, rather the type of contributors matters more [50]. Studies have proven the \u201cenough eyeballs\" hypothesis and found that larger teams increase survival. Robinson et al. [50] found that projects with more than 20 unique contributors had a higher survival probability compared to small teams. Ait et al. [3] further confirm that projects with a larger community size (Tier 3) have a higher chance of survival. The team size also matters in innovative projects. Fang et al. [17] found that the innovative projects, while attracting more popularity, tend to have smaller teams and face survival challenges.\n\nConversely, Song and Kim [53] argue that a simple increase in contributors can be \u201cpoisonous\" to efficiency due to communication overhead. Their results showed that \u201cheavy contributors\" positively affect the project efficiency, whereas a simple increase in total contributors negatively affects it. In addition to these attributes, developers\u2019 own experience with the project and their states also influence the project survival [26]. Calefato et al. [7] modeled developer inactivity using \u201csleeping\" and \u201cdead\" metaphors. They found that all core developers take breaks (sleeping state), but about 45% completely disengage (dead state) for at least two years.\n\nRecent studies highlight that governance, culture, and non-coding labor are as important as human infrastructure for a project\u2019s survival. Lenge et al. [33] define invisible labor as unrecognized work such as mentorship, conflict resolution, and administrative tasks. They argue that this labor is the \u201cbackbone\" of OSS. Therefore, a lack of leadership skills in these areas affects the newcomers\u2019 onboarding and ultimately project survival. Additionally, the formal and informal rules governing a project significantly affect its survival. Yin et al. [61, 60] used institutional analysis and revealed that projects that exhibit a higher frequency of institutional statements survive longer. Additional factors such as mentorship, governance, and \u201cvolunteer\u2019s dilemma\" also impact the project survival [60, 42].\n\nActivity, Stability, and Rhythm Indicators: These indicators serve as \u201cvital signs\" of a project. Beyond simple aggregate counts, these indicators analyze the cadence, consistency, and responsiveness of project activities. Researchers often use them to distinguish between active (healthy) and dormant (unhealthy) projects. These indicators include, but are not limited to, commits, releases, and issue resolution. Adejumo et al. [2] utilize the composite stability index and highlight that the commit volume alone is insufficient. They revealed that projects with maintaining stable commit patterns are less risky and more resilient. Other studies also found that projects with high revision frequency and a low ratio of non-working days have a slightly higher probability of survival [50, 35]. Additionally, the release dynamics also impact the survival. The release speed and interval are significant predictors of survival. Hasan et al. [21] analyzed the Maven ecosystem\u2019s libraries and observed a transition from fast to slow in release speeds, followed by inactivity. Although this pattern is not always a sign of abandonment, some libraries exhibit a spike of high frequency before decline.\n\nSurvival does not solely depend on just adding a new code, but on the capacity to maintain it. Park and Kwon [45] define and analyze the issue retention rate (IRR) as a proxy for maintenance capacity. The authors observed that as projects age or grow in code complexity, the IRR tends to rise, increasing the risk of abandonment. With a similar focus on maintainer-centric features, Xu et al. [59] revealed that maintainer responsiveness and delay are critical factors of survival. Additionally, recent findings indicate that sustained active interaction (issues and comments) drives extreme longevity, whereas the predictive power of passive metrics declines over time [29, 27].\n\nCode and Innovation: These indicators investigate the \u201ctechnical health\" of a project to determine its mortality. Project growth is generally seen as a survival signal. Khondu et al. [31] found that active projects tend to launch with a larger initial codebase and grow consistently than dormant or inactive projects. Liao et al. [35] further supported this by reporting a strong positive Pearson correlation (r = 0.85) between project size and its lifespan. Additionally, code quality and maintainability also have an impact on survival. However, this relationship is complex. Khondu et al. [31] investigated the maintainability index (MI) and revealed that the majority of inactive and abandoned projects have a stable MI. Furthermore, recent studies focused on innovation revealed a tension between project novelty and sustainability. Fang et al. [17] noted a higher risk of abandonment in innovative projects due to a"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2605.11844\" --max-chars 18000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [86] ASSISTANT · 2026-08-20 19:07:44 UTC

```
This is a very recent paper that's in my neighborhood (PR workflow dynamics, survival prediction). Notably it explicitly says "PR dynamics have been overlooked in mortality research" and examined 1736 inactive projects. But it focuses on AGGREGATE PR workflow dynamics (friction, negativity, backlog), NOT on the founder's involvement trajectory specifically. It mentions TFDD and developer departure but doesn't model the founder's role or the scaffolding-fade mechanism. Let me check whether they explicitly mention the founder.
```

### [87] TOOL CALL — terminal · 2026-08-20 19:07:44 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/html/2605.11844\" --pattern \"(founder|stepping down|BDFL|benevolent|leader|successor|handover|trajector)\" -i --max-matches 20 --context-chars 250",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [88] TOOL RESULT — terminal · 2026-08-20 19:07:46 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2605.11844\nType: HTML\nPattern: (founder|stepping down|BDFL|benevolent|leader|successor|handover|trajector) (3 matches in 133984 chars)\n\n--- Content ---\n\n14728:...human infrastructure for a project\u2019s survival. Lenge et al. [33] define invisible labor as unrecognized work such as mentorship, conflict resolution, and administrative tasks. They argue that this labor is the \u201cbackbone\" of OSS. Therefore, a lack of leadership skills in these areas affects the newcomers\u2019 onboarding and ultimately project survival. Additionally, the formal and informal rules governing a project significantly affect its survival. Yin et al. [61, 60] used institutional analysis and revea...\n--\n19635:...ity of organizations\u2019 owned projects. Other factors like resource funding also influence the project decline.\n\nProject\u2019s Macro-Demographics: A project\u2019s own attributes, such as project age, programming language, and application domain, influence its trajectory. Nourry et al. [43] highlighted maturity as a buffer and revealed that a mature project survives the TFDD event where the core development team leaves. Avelino et al. [6] challenged this view and highlighted maturity as rigidity. They noted that su...\n--\n112951:... should extend this \u201cautopsy\" approach to real-time intervention tools. Since silence (falling discussion volume) is a leading indicator of collapse. While future bots could detect this signal early, such interventions may not always alter a project trajectory. As demonstrated in our case studies, mortality may be driven by inevitable external ecosystem shifts. Beyond this, longitudinal studies of active projects could validate the death spiral mechanism in real time. Integrating commit-level and issue-l..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/html/2605.11844\" --pattern \"(founder|stepping down|BDFL|benevolent|leader|successor|handover|trajector)\" -i --max-matches 20 --context-chars 250", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [89] ASSISTANT · 2026-08-20 19:07:50 UTC

```
Confirmed: "The Death Spiral" paper does NOT mention "founder," "BDFL," "successor," or "handover" at all. It's about aggregate PR workflow friction. The trajectory word only appears once, in a different sense. This is a strong differentiation.

Let me also check the deep temporal neural paper and the sustainability prediction paper, and do a quick search for "founder departure" + "teacher fade" cross-domain angle.
```

### [90] TOOL CALL — terminal · 2026-08-20 19:07:51 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2602.09064\" --max-chars 12000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [91] TOOL RESULT — terminal · 2026-08-20 19:07:51 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2602.09064\nType: HTML\nLength: 80457 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n\u00d7\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) \u00d7\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2602.09064v2 \"Back to abstract page\") [ Download PDF](/pdf/2602.09064v2 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract\n  2. 1 Introduction\n  3. 2 Related Work\n     1. 2.1 Open Source Software Sustainability and Prediction\n     2. 2.2 Advanced Computational Methods for Analyzing Temporal OSS Activity\n        1. Mining Software Repositories with Machine Learning\n        2. Deep Learning for Software Engineering\n        3. Temporal Neural Networks and Time Series Prediction\n        4. Hierarchical Classification and Class Imbalance Handling\n        5. Ensemble Methods and Multi-Stage Learning\n        6. Explainable AI for Software Engineering\n     3. 2.3 Synthesis and Motivation\n  4. 3 Methodology\n     1. 3.1 Dataset Construction and Preprocessing\n        1. 3.1.1 Data Collection and Label Definition\n        2. 3.1.2 Temporal Feature Engineering\n        3. 3.1.3 Tabular Feature Engineering\n     2. 3.2 Hierarchical Model Architecture\n        1. 3.2.1 Stage-1: Binary Gating for ContribMid Detection\n        2. 3.2.2 Stage-2: Parallel Multi-class Classification\n           1. Heavy Model (Transformer + MLP)\n           2. Light Model (MLP-only Baseline)\n           3. Confidence-based Ensemble Routing\n        3. 3.2.3 Club-Fed Expert for Minority Class Refinement\n     3. 3.3 Training Procedure\n     4. 3.4 Model Evaluation\n     5. 3.5 Explainability and Attribution Analysis\n        1. Attribution Methods by Model Architecture\n        2. Feature-Level Attribution Computation\n        3. Semantic Feature Categorization\n        4. Category-Level Attribution Aggregation\n        5. Temporal Attribution Analysis\n        6. Ablation-Based Validation\n  5. 4 Results\n     1. 4.1 Predictive Performance of OSS Sustainability Stage Classification\n        1. Overall Predictive Performance\n        2. Per-Class Performance and Error Patterns\n        3. Effects of Class Imbalance\n     2. 4.2 Attribution-Based Analysis of Activity Category Contributions\n        1. Cross-Model Category Importance\n        2. Temporal Attribution Patterns\n        3. Tabular Feature Contributions\n        4. Ablation-Based Validation\n        5. Model-Specific Attribution Profiles\n  6. 5 Discussion\n     1. 5.1 Summarization and Implications\n     2. 5.2 Limitations and Future Directions\n  7. References\n  8. A Appendix A\n  9. B Appendix B\n     1. B.1 Z-score Normalization\n     2. B.2 Delta Temporal Features\n  10. C Appendix C\n     1. C.1 Detailed Model Architectures\n     2. C.2 Mathematical Formula to Integrate the Pipeline\n        1. C.2.1 Binary MLP Model\n        2. C.2.2 Stage-2: Heavy model (Transformer + MLP\n        3. C.2.3 Stage-2: light model\n        4. C.2.4 Club-Fed Expert\n        5. C.2.5 Loss Function\n  11. D Appendix D\n     1. D.1 Model Hyperparameters\n  12. E Appendix E\n     1. Accuracy\n     2. Balanced Accuracy\n     3. F1-Score Variants\n     4. Confidence Calibration\n  13. F Appendix F\n     1. F.1 Explainability Analysis\n        1. Gradient-Based Attribution\n        2. SHAP\n        3. Integrated Gradients\n        4. Attention Validation\n\n\n\n[ License: arXiv.org perpetual non-exclusive license ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2602.09064v2 [cs.SE] 13 Feb 2026\n\n# Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI\n\nS M Rakib Ul Karim  Affiliation: Dept. of Electrical & Computer Engineering  Affiliation: University of Missouri  Affiliation: Columbia, Missouri, United States  Email: [skarim@missouri.edu](mailto:) Wenyi Lu  Affiliation: Dept. of Computer Science  Affiliation: University of Missouri  Affiliation: Columbia, Missouri, United States  Email: [wldh6@mail.missouri.edu](mailto:) Enock Kasaadha  Affiliation: Dept. of Computer Science  Affiliation: University of Missouri  Affiliation: Columbia, Missouri, United States  Email: [ekqkf@missouri.edu](mailto:) Sean Goggins  Affiliation: Dept. of Electrical & Computer Engineering  Affiliation: University of Missouri  Affiliation: Columbia, Missouri, United States  Email: [gogginss@missouri.edu](mailto:)\n\n###### Abstract\n\nOpen Source Software (OSS) projects follow diverse lifecycle trajectories shaped by evolving patterns of contribution, coordination, and community engagement. Understanding these trajectories is essential for stakeholders seeking to assess project organization and health at scale. However, prior work has largely relied on static or aggregated metrics, such as project age or cumulative activity, providing limited insight into how OSS sustainability unfolds over time. In this paper, we propose a hierarchical predictive framework that models OSS projects as belonging to distinct lifecycle stages grounded in established socio-technical categorizations of OSS development. Rather than treating sustainability solely as project longevity, these lifecycle stages operationalize sustainability as a multidimensional construct integrating contribution activity, community participation, and maintenance dynamics. The framework combines engineered tabular indicators with 24-month temporal activity sequences and employs a multi-stage classification pipeline to distinguish lifecycle stages associated with different coordination and participation regimes. To support transparency, we incorporate explainable AI techniques to examine the relative contribution of feature categories to model predictions. Evaluated on a large corpus of OSS repositories, the proposed approach achieves over 94% overall accuracy in lifecycle stage classification. Attribution analyses consistently identify contribution activity and community-related features as dominant signals, highlighting the central role of collective participation dynamics.\n\n## 1 Introduction\n\nOpen source software (OSS) has become the backbone of modern software development, powering critical infrastructure, enabling innovation, and fostering global collaboration. However, the sustainability of OSS projects remains a significant challenge, with estimates suggesting that over 80% of OSS projects become inactive within a few years of inception [33, 41]. The ability to anticipate and understand sustainability trajectories is therefore critical for developers, maintainers, funders, and organizations that depend on these ecosystems.\n\nOSS sustainability encompasses multiple dimensions, including technical maintenance, community engagement, contributor retention, and long-term organizational viability. Much prior work has operationalized sustainability using static or aggregated indicators, such as code quality, documentation completeness, or developer counts [5, 27]. While informative, these approaches offer limited insight into how sustainability unfolds over time, as they fail to capture the dynamic evolution of activity patterns, contributor behavior, and community interaction.\n\nRecent advances in deep learning and temporal modeling have opened new opportunities for analyzing complex sequential data in software engineering contexts [14]. Architectures such as recurrent neural networks, temporal convolutional networks, and Transformers have demonstrated strong capacity to model long-range dependencies and temporal structure in time-series data[42, 2]. In OSS research, these methods have been applied to tasks such as defect prediction and project health assessment, suggesting their potential for more nuanced sustainability modeling [14].\n\nHowever, the application of deep temporal models to OSS sustainability remains limited in scope and depth [13]. Existing studies frequently frame sustainability as a binary outcome (e.g., active vs. inactive) or rely on coarse categorizations that overlook intermediate organizational regimes and lifecycle transitions [19]. Moreover, many deep learning approaches emphasize predictive performance without providing interpretable explanations, constraining their usefulness for stakeholders who require actionable understanding rather than opaque predictions [47].\n\nMotivated by these gaps, this study addresses the following research questions:\n\n  * \u2022\n\nRQ1: To what extent can OSS sustainability stages be predicted from a fixed 24-month window of repository activity using temporal sequences and derived activity-based features?\n\n  * \u2022\n\nRQ2: Which categories of repository activity most strongly influence sustainability stage predictions, and how do these attribution patterns vary across modeling approaches and decision components?\n\n\n\n\nTo answer these questions, we explore and empirically validate a hierarchical neural modeling strategy that integrates Transformer-based temporal processing with feedforward neural modeling of engineered tabular features. Rather than relying on a single flat classifier, the approach decomposes the prediction task into specialized decision components designed to better capture heterogeneous lifecycle regimes and mitigate class imbalance. Explainable AI techniques are incorporated to systematically analyze how different categories of repository activity contribute to model decisions.\n\nOur study makes four primary contributions. First, we show that OSS sustainability stages can be accurately predicted from recent activity histories when temporal and derived activity-based features are jointly modeled, substantially outperforming flat baselines. Second, our analyses reveal that recent contribution and community dynamics consistently dominate sustainability predictions, underscoring the importance of short- to mid-term activity patterns. Third, we introduce an attribution-based explainability framework that aggregates feature-level explanations into interpretable activity categories, enabling transparent and actionable insights into model behavior. Finally, we release an open-source implementation of the full pipeline to support reproducibility and future research. These contributions advance the study of OSS sustainability by demonstrating how temporal modeling and explainable learning can be combined to support scalable, transparent assessment of project health, with implications for maintainers, funding organizations, and platform-level ecosystem monitoring.\n\n## 2 Related Work\n\n### 2.1 Open Source Software Sustainability and Prediction\n\nOpen source software (OSS) sustainability has become a central topic in software engineering research as OSS increasingly underpins critical digital infrastructure. Prior studies have sought to characterize, predict, and improve sustainability using empirical signals derived from repository activity, developer behavior, and project organization. This literature reveals steady methodological progress, alongside persistent conceptual and technical limitations.\n\nEarly work primarily relied on static or snapshot-based indicators of project health, such as contributor counts, commit volume, code churn, issue activity, and communication traces. For example, Mockus et al. [27] analyzed developer participation and communication patterns in the Apache ecosystem, while Capiluppi and Michlmayr [5] examined project evolution through code churn and contributor turnover. Subsequent studies incorporated social network analysis to model collaboration structures and developer roles [18]. More recent work has explored community engagement signals, including emoji usage and participation dynamics, as potential sustainability indicators [49, 45]. While foundational, these approaches largely capture sustainability through aggregated or cross-sectional views, limiting their ability to re"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2602.09064\" --max-chars 12000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [92] ASSISTANT · 2026-08-20 19:09:01 UTC

```
This is a "lifecycle stage classification" using aggregate activity metrics — NOT about founder-specific roles, NOT about the founder's involvement trajectory, NOT specifically about surviving after founder departure. Let me verify by checking mentions of "founder".
```

### [93] TOOL CALL — terminal · 2026-08-20 19:09:01 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/html/2602.09064\" --pattern \"(founder|BDFL|benevolent|founder\\\\s*departure|successor|handover|leader\\\\s*exit|leaves\\\\s+the\\\\s+project)\" -i --max-matches 10 --context-chars 200",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [94] TOOL RESULT — terminal · 2026-08-20 19:09:03 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2602.09064\nType: HTML\nPattern: (founder|BDFL|benevolent|founder\\s*departure|successor|handover|leader\\s*exit|leaves\\s+the\\s+project) (0 matches in 80457 chars)\n\n--- Content ---\n\nNo matches found for pattern: (founder|BDFL|benevolent|founder\\s*departure|successor|handover|leader\\s*exit|leaves\\s+the\\s+project)"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" grep --url \"https://arxiv.org/html/2602.09064\" --pattern \"(founder|BDFL|benevolent|founder\\\\s*departure|successor|handover|leader\\\\s*exit|leaves\\\\s+the\\\\s+project)\" -i --max-matches 10 --context-chars 200", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [95] ASSISTANT · 2026-08-20 19:09:07 UTC

```
The sustainability prediction paper makes ZERO mention of the founder. Let me update the task tracker and do a few more adversarial searches — the bus factor guideline paper (which is most likely to mention founder involvement trajectory) and a cross-field check.
```

### [96] TOOL CALL — task_tracker · 2026-08-20 19:09:07 UTC

```
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "No user uploads found - empty folder",
      "status": "done"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes": "8 directions brainstormed; settled on scaffolding-fade trajectory as most novel",
      "status": "done"
    },
    {
      "title": "Web search for landscape overview of each direction",
      "notes": "Found landscape: bus factor, governance transitions, diversity, abandonment empirical, death spiral deep temporal neural, sustainability random forest - NONE about founder involvement trajectory",
      "status": "done"
    },
    {
      "title": "Fetch and read potentially relevant papers",
      "notes": "Read Avelino 2019 (TFDD), Noori 2509 (governance), Feng 2023 (diversity), death spiral 2026 (PR dynamics), deep temporal neural 2026 (lifecycle stage) - none model founder scaffolding fade",
      "status": "done"
    },
    {
      "title": "Adversarial novelty check",
      "notes": "Verify scaffolding-fade curve novelty across fields and against the most-direct founder-trajectory papers",
      "status": "in_progress"
    },
    {
      "title": "Feasibility check",
      "notes": "Verify testable with Python, available data, $10 OpenRouter budget",
      "status": "todo"
    },
    {
      "title": "Write hypothesis JSON output",
      "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema",
      "status": "todo"
    }
  ]
}
```

### [97] TOOL RESULT — task_tracker · 2026-08-20 19:09:09 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "No user uploads found - empty folder", "status": "done"}, {"title": "Brainstorm 5-7 diverse directions without searching", "notes": "8 directions brainstormed; settled on scaffolding-fade trajectory as most novel", "status": "done"}, {"title": "Web search for landscape overview of each direction", "notes": "Found landscape: bus factor, governance transitions, diversity, abandonment empirical, death spiral deep temporal neural, sustainability random forest - NONE about founder involvement trajectory", "status": "done"}, {"title": "Fetch and read potentially relevant papers", "notes": "Read Avelino 2019 (TFDD), Noori 2509 (governance), Feng 2023 (diversity), death spiral 2026 (PR dynamics), deep temporal neural 2026 (lifecycle stage) - none model founder scaffolding fade", "status": "done"}, {"title": "Adversarial novelty check", "notes": "Verify scaffolding-fade curve novelty across fields and against the most-direct founder-trajectory papers", "status": "in_progress"}, {"title": "Feasibility check", "notes": "Verify testable with Python, available data, $10 OpenRouter budget", "status": "todo"}, {"title": "Write hypothesis JSON output", "notes": "Write to .sdk_openhands_agent_struct_out.json matching schema", "status": "todo"}], "kind": "TaskTrackerObservation"}
```

### [98] TOOL CALL — terminal · 2026-08-20 19:10:15 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2401.03303v1\" --max-chars 14000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [99] TOOL RESULT — terminal · 2026-08-20 19:10:15 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://arxiv.org/html/2401.03303v1\nType: HTML\nLength: 43249 chars (truncated)\n\n--- Content ---\n\n##### Report GitHub Issue\n\n\u00d7\n\nTitle:\n\nContent selection saved. Describe the issue below:\n\nDescription:\n\nSubmit without GitHub Submit in GitHub\n\narXiv is now an independent nonprofit! [Learn more](https://info.arxiv.org/about) \u00d7\n\n[ Back to arXiv ](/)\n\n[Why HTML?](https://info.arxiv.org/about/accessible_HTML.html) Report Issue [ Back to Abstract ](/abs/2401.03303v1 \"Back to abstract page\") [ Download PDF](/pdf/2401.03303v1 \"Download PDF\") [ ](javascript:toggleNavTOC\\(\\); \"Toggle navigation\") [ ](javascript:toggleReadingMode\\(\\); \"Disable reading mode, show header and footer\")\n\n  1. Abstract.\n  2. 1 Introduction\n  3. 2 Existing Literature\n     1. 2.1 CST Algorithm\n     2. 2.2 RIG Algorithm\n     3. 2.3 Other Bus Factor Algorithms\n  4. 3 Study Design\n     1. 3.1 Database of GitHub data for HPC projects and other Metrics\n     2. 3.2 Implementation of Bus Factor Algorithms\n     3. 3.3 Handling External Code and Aliases\n     4. 3.4 Validating Bus Factor Results\n  5. 4 Results\n     1. 4.1 Comparison for Accuracy of Results\n     2. 4.2 Trend in bus factors over time\n     3. 4.3 Performance comparison of BF Algorithms\n  6. 5 Future Work\n  7. 6 Conclusion\n  8. References\n\n\n\n[ License: CC BY 4.0 ](https://info.arxiv.org/help/license/index.html#licenses-available)\n\narXiv:2401.03303v1 [cs.SE] 06 Jan 2024\n\n# Guiding Effort Allocation in Open-Source Software Projects Using Bus Factor AnalysisCCS: Software and its engineering Risk managementCCS: Software and its engineering Maintaining softwareCCS: Software and its engineering Software version controlCCS: Software and its engineering Open source modelCCS: Software and its engineering Programming teams\n\nAliza Lisan  email: [alisan@uoregon.edu](mailto:alisan@uoregon.edu) OrcID: [0002-1544-1493](https://orcid.org/0002-1544-1493) Affiliation: University of Oregon , 1585 E 13th Ave , Eugene , Oregon , USA , 97403 and  Boyana Norris  email: [norris@cs.uoregon.edu](mailto:norris@cs.uoregon.edu) Affiliation: University of Oregon , 1585 E 13th Ave , Eugene , Oregon , USA , 97403\n\n###### Abstract.\n\nA critical issue faced by open-source software projects is the risk of key personnel leaving the project. This risk is exacerbated in large projects that have been under development for a long time and experienced growth in their development teams. One way to quantify this risk is to measure the concentration of knowledge about the project among its developers. Formally known as the Bus Factor (BF) of a project and defined as \u201cthe number of key developers who would need to be incapacitated to make a project unable to proceed\u201d (inproceedings). Most of the proposed algorithms for BF calculation measure a developer\u2019s knowledge of a file based on the number of commits. In this work, we propose using other metrics like lines of code changes (LOCC) and cosine difference of lines of code (change-size-cos) to calculate the BF. We use these metrics for BF calculation for five open-source GitHub projects using the CST algorithm and the RIG algorithm, which is git-blame-based. Moreover, we calculate the BF on project sub-directories that have seen the most active development recently. Lastly, we compare the results of the two algorithms in accuracy, similarity in results, execution time, and trends in BF values over time.\n\n###### Keywords:\n\nBus factor, Open-Source, Code ownership, Risk management, Mining GitHub repositories\n\n## 1\\. Introduction\n\nIf we look at our daily use of the Internet, we realize that we are consumed with the use of software and applications. The development and maintenance of all these software projects are based on the knowledge held by its developers. This makes the software development process the most dependent upon its developers. Given that, developers become an important asset for project organizations and open-source project teams. This also makes the rate at which developers leave a software project a critical matter and risk. To mitigate this risk, it is important that project managers or principal developers monitor and quantify the concentration of knowledge of the project among its developers (7961518) An interesting measurement used in this regard is known as the Bus Factor (BF), which is defined as the minimum number of key developers whose departure would make a project unable or difficult to proceed (7961518) A smaller bus factor value would mean that the maximum knowledge of the project is concentrated among them and the project is at a higher risk if some or all of these developers leave the project, company or go for a vacation, etc. A bus factor of one would be the worst-case scenario. Conversely, a high bus factor means a lesser risk is posed to the project in case some of the developers end up leaving.\n\nWhen it comes to open-source software projects, the bus factor is of much more importance. Most of the people working on these projects are making contributions voluntarily. Volunteering means that the developers or contributors do not have financial benefits associated with these projects. This puts open-source software projects at a higher risk of developer turnover (7961518). Given the importance of bus factor measurement in open-source software development projects, algorithms have been proposed to calculate it using data gathered from version control systems such as GitHub (inproceedings; 7503718; 10.1145/2884781.2884851). To the best of our knowledge, most of these algorithms are commit-based, i.e., the algorithms look at the commit data from version control repositories. Moreover, existing work mostly proposes bus factor calculation algorithms and presents tools for the same. Few studies attempt to validate the results of these algorithms. (7961518) is an empirical and comparative study where three Bus Factor algorithms are validated, but they only used the tools and metrics provided by the original authors.\n\nTherefore, in this paper, we look at two algorithms (a) first one was proposed by Cosentino et al. (7961518), which calculates the bus factor of each file and aggregates it up to branch, directory, or project level; (b) second one proposed by Rigby et al. (10.1145/2884781.2884851), which uses a git-blame-based approach to calculate the bus factor. The tool based on the first algorithm is publicly available (inproceedings); however, the authors have only provided the pseudo-code of the second. Using the convention followed in (7961518), we refer to the first algorithm as CST and the second one as RIG. Among the two algorithms, CST is a commit-based algorithm, and we wanted to use it with other metrics like lines of code changes (LOCC) and cosine difference of lines of code (change-size-cos). For that, we implemented it by understanding the algorithm mentioned in (inproceedings). RIG algorithm had to be implemented as its code, or any related tool is not publicly available. We implemented and tested both algorithms on five open-source projects and compared their results. We also got feedback from the principal developers of these projects to validate the results. Lastly, we used the tool provided in (inproceedings) to obtain bus factor results for the selected projects.\n\nTo summarize, we seek to answer the following research questions:\n\n  1. (1)\n\nHow do different metrics such as lines of changed code and cosine difference affect the bus factor computation?\n\n  2. (2)\n\nHow can the bus factor guide principal developers or managers to allocate effort for hiring or knowledge transfer among the existing team of developers?\n\n  3. (3)\n\nHow do bus factor algorithms differ in terms of accuracy and performance?\n\n\n\n\nAs such, our contributions can be summarized as follows:\n\n  * \u2022\n\nImplemented the CST algorithm (with lines of code changes and cosine difference of lines of code) and the RIG algorithm and compared their results.\n\n  * \u2022\n\nGot feedback from the principal developers of the five selected projects to validate our results.\n\n  * \u2022\n\nCalculated the BF of the selected projects using the commit-based CST algorithm tool provided in (inproceedings) to compare with our results.\n\n  * \u2022\n\nCalculated the bus factor for the selected projects for the last five years to see the trend in BF values.\n\n\n\n\nIn Section 2, we review the existing literature for bus factor calculation. Section 3 explains the design and steps involved in our study. We present our results in Section 4 and conclude the paper in Section 6.\n\n## 2\\. Existing Literature\n\nIn this section, first, we describe the two algorithms for measuring bus factors that we will be using as part of our study in this paper. Towards the end, we describe other algorithms that are part of the existing literature but not implemented in our study.\n\n### 2.1. CST Algorithm\n\nThe CST algorithm is proposed as part of a tool paper (inproceedings) by Cosentino et al. The algorithm calculates the knowledge of developers on each file and determines the bus factor for each file based on that. Furthermore, aggregation is performed from file to directory, branch, or project level to get developer knowledge. The aggregation is done by simply adding the knowledge on each file and scaling with the number of files in the directory, branch, or project. The authors proposed four metrics to calculate a developer\u2019s knowledge of a file. _last change takes it all_ assigns 100% knowledge of a file to the last developer who modified it, and in _multiple changes equally considered_ , the knowledge of a developer is calculated by dividing the number of commits made by the developer on a file by the total number of commits ever made on that file. The third metric is _non-consecutive changes_ , which considers the developer\u2019s non-consecutive commits on a file only and merges the consecutive commits into a single one. The last metric is an extension of the third metric, called the _weighted non-consecutive changes_ , and assigns incremental weight to the later commits on the file.\n\nOnce the developer\u2019s knowledge of the artifacts, i.e., file, directory, branch, or project, has been calculated, the bus factor for each of these artifacts is measured by using two sets of developers. The first set is called the primary developers who have minimum knowledge XX of the artifact. The second set is called the secondary developers who at least have some knowledge YY of the artifact, where YY is less than XX. The threshold XX for the selection of primary developers is set to 1/N1/N where NN is the total number of developers that have made changes to the artifact till date. YY is set of half of XX for the selection of secondary developers. The number of developers in the union of both these sets gives us the bus factor for the particular artifact.\n\nSince, CST is a commit-based algorithm, we use the same algorithm with _LOCC_ and _change-size-cos_. The details of how we collect and use this data for open-source projects on GitHub are provided in later sections.\n\nAlgorithm 1 RIG Algorithm\n\nData git-blame data for each file in the project\nResult BFset (BF developers), g (Bus Factor)\n\n\n\n\n1: for g\u21901\u200bt\u200bo\u200b200g\\leftarrow 1\\hskip 5.69046ptto\\hskip 5.69046pt200 do\n\n2: for i\u21901\u200bt\u200bo\u200b1000i\\leftarrow 1\\hskip 5.69046ptto\\hskip 5.69046pt1000 do\n\n3: B\u200bF\u200bs\u200be\u200bt\u2190BFset\\leftarrow random sample of g devs;\n\n4: remove-authors (BFset);\n\n5: if \u200ba\u200bb\u200ba\u200bn\u200bd\u200bo\u200bn\u200be\u200bd\u2212f\u200bi\u200bl\u200be\u200bs\u200b()\u226550%\\emph{abandoned-files()}\\geq 50\\% then\n\n6: return g, BFset;\n\n7: end if\n\n8: end for\n\n9: end for\n\n10: return null, null;\n\n### 2.2. RIG Algorithm\n\nRIG algorithm was proposed by Rigby et al. (10.1145/2884781.2884851), in which they adapt the financial risk management measures to a developer turnover context to measure the risk posed to a project from developer turnover. Unlike the CST algorithm, RIG uses a blame-based approach to calculate code ownership of developers. The _blame_ feature is implemented in version control systems such that a git-blame command assigns each line in a file to a developer who changed it last. The algorithm\u2019s authors claim that this approach allows them to follow code ownership at a finer granularity. As per the algorithm, a line is considered abandoned if it is attributed to a developer who is no longer part of the project, and a file is considered abandoned when 90% of its files are abandoned. This high threshold makes sure that developers with trivial contributions are excluded. Algorithm 1 shows the pseudo-code for the RIG algorithm. The algorithm starts by varying the size of developers gg from 1 to 200 who leave the project, as shown in line 1. Line 3 shows the random sampling of developers of size gg who leave the project, and this random sampling is repeated 1,000 times for every value of gg. We limit these iterations to 10 instead of 1,000 because the algorithm takes a long time on relatively larger projects we chose. Moreover, following (7961518), we return the lowest value of gg that resulted in the abandoned status of more than 50% of the files, as shown from lines 5-7. The authors in the original paper (10.1145/2884781.2884851) also calculate the likelihood of each group of developers leaving the project between lines 3-4, but we omit it since we are A noticeable characteristic of this algorithm is its non-deterministic nature, i.e., different results are produced for each execution of the algorithm because of the random sampling of the developers. Also, the algorithm may not return a valid result, as can be seen from line 10, which happens when no _BFset_ results in more than 50% of abandon files.\n\nTable 1. List of the selected HPC projects with their brief descriptions. Project | Release Year | Contributors | Language | Description\n---|---|---|---|---\nPETSc(petsc) | 1994 | 207 | C | Portable, Extensible Toolkit for Scientific Computation.\nSpack(spack) | 2014 | 1,164 | Python | Multi-platform package manager.\nHypre(hypre) | 2004 | 34 | C | Library of high performance pre-conditioners and solvers.\nLammps(lammps) | 2016 | 224 | C++ | Large-scale Atomic/Molecular Massively Parallel Simu"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://arxiv.org/html/2401.03303v1\" --max-chars 14000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [100] ASSISTANT · 2026-08-20 19:10:19 UTC

```
This bus factor paper measures BUS FACTOR OVER TIME (5-year trend) but only as a STATIC per-snapshot value — it does NOT model the FOUNDERS' specific trajectory of involvement, nor does it link to survival outcomes. Notably, the bus factor trend is just the count of key developers per file. It does not distinguish the founder's role.

Now let me do a critical cross-field adversarial check — does the scaffolding-fade mechanism exist in any other field applied to similar "leader succession" problems?
```

### [101] TOOL CALL — terminal · 2026-08-20 19:10:19 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"leadership succession scaffolding fade trajectory departure organizational survival empirical prediction\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [102] TOOL RESULT — terminal · 2026-08-20 19:10:21 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: leadership succession scaffolding fade trajectory departure organizational survival empirical prediction  [general via ddgs]\nFound: 10 results\n\n1. Leadership succession and its impact on organizational resilience: A contingency perspective in engineering firms - ScienceDirect\n   https://www.sciencedirect.com/science/article/pii/S2666721525000171\n   September 26, 2025 - Empirical data from West Java, Indonesia's second-largest ECF hub after Jakarta, provides a compelling case: of the 51 ECFs established for over 25 years (averaging 36 years), 43 ...\n\n2. Leadership succession in different types of organizations: What business and political successions may learn from each other - ScienceDirect\n   https://www.sciencedirect.com/science/article/pii/S1048984317307154\n   June 1, 2019 - We systematically review the recent impactful leadership succession literature in three types of organizations/contexts, namely publicly-traded, priva\u2026...\n\n3. Survival beyond succession? The contingent impact of ...\n   https://business.columbia.edu/sites/default/files-efs/pubfiles/497/Haveman_Succession.pdf\n   Grusky, 1960, 1963, 1964). A vicious circle operates: poor performance leads to succession, which in turn disrupts operations and further worsens performance (Grusky, 1963). The \u00b7 succession-crisis hy...\n\n4. Leadership Succession Planning and Organization ...\n   https://arcjournals.org/pdfs/ijmsr/v10-i3/3.pdf\n   In this study, the research focuses on leadership succession planning and \u00b7 organizational transition with the goal of implementing leadership talent development and retention \u00b7 strategies in the orga...\n\n5. Evidence-Driven Succession A NEW ERA IN LEADERSHIP: THE SUCCESSION-CENTRIC ERA\n   https://www.ccl.org/wp-content/uploads/2025/05/evidence-driven-succession-research-report-ccl.pdf\n   Stakeholders demand emotional resonance, social relevance, and empirical evidence as \u00b7 organizations communicate decisions about leadership transitions....\n\n6. (PDF) Succession planning and organizational survival: Empirical study on Nigerian private tertiary institutions\n   https://www.researchgate.net/publication/276229603_Succession_planning_and_organizational_survival_Empirical_study_on_Nigerian_private_tertiary_institutions\n   October 22, 2024 - On the other hand variables such as TurnoverRate, Career Development and Supervisor\u2019 Supervision) are insignificantly correlated withorganizational survival. The results are suppose...\n\n7. (PDF) Leadership Succession Planning and Organization Transition: A Review of Literature\n   https://www.researchgate.net/publication/359118673_Leadership_Succession_Planning_and_Organization_Transition_A_Review_of_Literature\n   March 9, 2022 - The study analyzes significant organizational outcomes as a result of the implementation of leadership succession planning, with implications for seamless organizational transition and...\n\n8. Leader succession and organizational performance: Integrating the common-sense, ritual scapegoating, and vicious-circle succession theories - ScienceDirect\n   https://www.sciencedirect.com/science/article/abs/pii/S1048984305000020\n   March 9, 2005 - Our study examines the impact of leader succession on organizational performance. We use organizational learning theory and the concept of time compre\u2026...\n\n9. CEO succession planning and market reactions to CEO turnover announcements - ScienceDirect\n   https://www.sciencedirect.com/science/article/abs/pii/S1544612323003185\n   April 27, 2023 - This study investigates how capital market investors assess CEO succession planning in the context of CEO turnover events. Conducting empirical tests \u2026...\n\n10. Ensuring leadership continuity: An integrative review of ...\n   https://learning-gate.com/index.php/2576-8484/article/download/7607/2606/10267\n   May 28, 2025 - C. Cloutier and D. Ravasi, \"Identity trajectories: Explaining long-term patterns of continuity and change in \u00b7 organizational identities,\" Academy of Management Journal, vol. 63, no. 4,..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"leadership succession scaffolding fade trajectory departure organizational survival empirical prediction\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [103] ASSISTANT · 2026-08-20 19:11:32 UTC

```
Leadership succession in management research — plenty on this. But the "scaffolding-fade curve" specifically, applied to OSS founder trajectory, is not present. The general management literature is about CEO succession, ritual scapegoating, succession planning — these don't operationalize the founder's gradual reduction of involvement as a measurable scaffolding-fade curve.

Let me check the Columbia Business School paper #3 (Haveman succession) which is classic, and do one more narrow cross-domain check on the EXACT mechanism — "founder involvement decline trajectory survivability".
```

### [104] TOOL CALL — terminal · 2026-08-20 19:11:32 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder CEO involvement decline trajectory firm survival predict stepped-down stepped-down abrupt\" --max-results 10",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [105] TOOL RESULT — terminal · 2026-08-20 19:11:50 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: founder CEO involvement decline trajectory firm survival predict stepped-down stepped-down abrupt  [general via ddgs]\nFound: 10 results\n\n1. Are founder-CEOs resilient to crises? The impact of founder-CEO succession on new firm survival - Yuji Honjo, Masatoshi Kato, 2022\n   https://journals.sagepub.com/doi/10.1177/02662426211050794\n   There are several reasons why new firm survival differs between firms managed by founder-CEOs and those managed by successor-CEOs. Founder-CEOs can accumulate specific knowledge about firms because of...\n\n2. Leading After the Founder | AAPL Publication\n   https://www.physicianleaders.org/articles/leading-after-the-founder\n   February 19, 2026 - The stakes are high: Founder CEO transitions carry a risk of failure or performance downturn that\u2019s two to three times greater than transitions involving nonfounder CEOs. Whether P...\n\n3. Boniardi&Partners \u00bb Leading After the Founder\n   https://boniardi-partners.com/?p=2200\n   The stakes are high: Founder CEO transitions carry a risk of failure or performance downturn that\u2019s two to three times greater than transitions involving nonfounder CEOs. Whether PE-backed, public, or...\n\n4. Leading After the Founder\n   https://hbr.org/2026/01/leading-after-the-founder\n   January 1, 2026 - When handled well, they unlock the next phase of growth and maturity; when mishandled, they can destabilize teams, compromise value, and derail momentum. The stakes are high: Founder...\n\n5. Cloning success or falling into a trap: The role of a founder CEO in the corporate comeback again - ScienceDirect\n   https://www.sciencedirect.com/science/article/abs/pii/S1566014125001487\n   November 5, 2025 - Table 3 presents the results for Models 1a to 5b, which we used to test Hypothesis 1, predicting that having the founder as CEO in a declining firm can positively affect the use of ...\n\n6. Founder vs CEO Dilemma \u2013 Knowing When to Pass the Torch - Egon Zehnder\n   https://www.egonzehnder.com/functions/chief-executive-officers/founders/insight/headline-riding-the-founder-succession-wave-why-top-ceos-are-passing-the-torch-in-2023\n   April 23, 2025 - However, transitioning out of the CEO role does not mean losing influence. In fact, 75% of founder CEOs remain involved in some capacity\u2014whether as Board Chair, advisor, or investor....\n\n7. Founder vs CEO: When to Step Down - Startup Wired\n   https://startupwired.com/2026/03/01/founder-vs-ceo-when-to-step-down/\n   March 2, 2026 - Review performance data objectively. If revenue growth, operational efficiency, or team engagement show consistent decline under your leadership, face the facts directly....\n\n8. How PE Firms Should Navigate Founder and CEO Succession\n   https://cowenpartners.com/founder-ceo-transitions-private-equity/\n   March 5, 2026 - The conversation addresses a stark reality: founder CEO transitions carry a risk of failure or performance decline two to three times greater than standard CEO successions. The reason?...\n\n9. DO FOUNDERS CONTROL START-UP FIRMS THAT GO PUBLIC?\n   https://journals.law.harvard.edu/hblr/wp-content/uploads/sites/87/2020/03/HLB104_crop.pdf\n   ts firm and founder-CEO survival for one and three years post IPO....\n\n10. An empirical analysis of firm survival in Japanese junior ...\n   https://www.rieti.go.jp/jp/publications/dp/24e060.pdf\n   Chen and Thompson (2015) found that among surviving firms, the turnover of founder-CEOs is positively associated with firm \u00b7 performance. A U-shaped relationship between founder-CEO turnover and firm ..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"founder CEO involvement decline trajectory firm survival predict stepped-down stepped-down abrupt\" --max-results 10", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [106] ASSISTANT · 2026-08-20 19:11:58 UTC

```
These papers study founder-CEO succession on FIRM survival but use STATIC variables (founder-CEO vs successor-CEO as binary). The "75% of founder CEOs remain involved in some capacity" finding is fascinating — this suggests it's the *trajectory* that matters but existing research treats it as a binary handover/binary state.

Let me also do a final check on the specific operationalization I plan: the trajectory of PR merges done by founder vs others. Let me run several more searches in parallel to be exhaustive.
```

### [107] TOOL CALL — terminal · 2026-08-20 19:11:58 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source git merge decision trajectory founder sole decider power distribution PR over time\" --max-results 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [108] TOOL RESULT — terminal · 2026-08-20 19:12:00 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source git merge decision trajectory founder sole decider power distribution PR over time  [general via ddgs]\nFound: 8 results\n\n1. What's the best GitHub pull request merge strategy?\n   https://graphite.com/blog/pull-request-merge-strategy\n   February 26, 2024 - When you submit a pull request (PR) on GitHub, you have a few options for merging the changes from your branch into the base branch. The three main strategies are: ... Choosing the...\n\n2. Automated Code Review Assignments: An Alternative Perspective of Code Ownership on GitHub\n   https://arxiv.org/html/2512.05551v2\n   CODEOWNERS assignments extend ownership beyond core committers and toward governance roles, yet when these declared owners participate in PRs, they act much like contribution-based owners in terms of ...\n\n3. Git merge strategy options & examples | Atlassian Git Tutorial\n   https://www.atlassian.com/git/tutorials/using-branches/merge-strategy\n   March 27, 2026 - The git merge and git pull commands can be passed an -s (strategy) option. The -s option can be appended with the name of the desired merge strategy. If not explicitly specified, Git ...\n\n4. Decisions, decisions: Principles for making important choices in open source \u00b7 GitHub\n   https://github.com/readme/featured/oss-decision-making\n   June 14, 2022 - Of course, seeking community-wide consensus for every single change to a codebase would take too long, so Apache projects handle smaller decisions in different ways. The Apache Cordova...\n\n5. Git - merge-strategies Documentation\n   https://git-scm.com/docs/merge-strategies\n   With the strategies that use 3-way merge (including the default, ort), if a change is made on both branches, but later reverted on one of the branches, that change will be present in the merged result...\n\n6. r/programming on Reddit: Selecting the Right Git Merging Strategy: Merge Commit, Squash and Merge, or Rebase and Merge\n   https://www.reddit.com/r/programming/comments/16rteoq/selecting_the_right_git_merging_strategy_merge/\n   September 25, 2023 - Uncover the intricacies of Git merging strategies \u2013 merge commit, squash and merge, and rebase and merge. Discover the pros and cons of each approach and learn how to navigate the...\n\n7. Can one person run an open source project alone? - Stack Overflow\n   https://stackoverflow.blog/2020/09/09/open-source-governance-benevolent-dictator-or-decision-by-committee/\n   September 9, 2020 - Determining how decisions get made and projects move forward is called governance. Depending on the project, the style of governance may be as open as the code itself, or it may al...\n\n8. Merge Mastery: Elevating Your Pull Request Game in Open Source Projects - DEV Community\n   https://dev.to/oluwadamisisamuel1/merge-mastery-elevating-your-pull-request-game-in-open-source-projects-25fo\n   February 15, 2024 - All the changes and contributions for a team project must be brought together at one point, and the process of reconciling these different changes is called merging pull requests. ..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source git merge decision trajectory founder sole decider power distribution PR over time\" --max-results 8", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [109] ASSISTANT · 2026-08-20 19:12:32 UTC

```
No direct overlap. Item 2 ("CODEOWNERS assignments") is about declared ownership in code, not founder trajectory. Let me do one more focused search combining the operationalization terms — measuring founder's share of merges/commits/comments over time as a trajectory predictor.
```

### [110] TOOL CALL — terminal · 2026-08-20 19:12:32 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder share of commits reviews merges declines predict project health community driven\" --max-results 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [111] TOOL RESULT — terminal · 2026-08-20 19:12:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source founder share of commits reviews merges declines predict project health community driven  [general via ddgs]\nFound: 8 results\n\n1. How to measure the health of an open source community | Opensource.com\n   https://opensource.com/article/19/8/measure-project\n   Metric: Time between commits, code reviews, and merges. Are there good prospects for using what I learn by contributing to increase my job opportunities? Metric: Living wage. How popular is this proje...\n\n2. Open Source Contribution Analysis & Benchmarks - Count.co\n   https://count.co/metric/open-source-contribution-analysis\n   March 2, 2026 - The key is monitoring these interconnected patterns rather than optimizing any single metric in isolation. When open source contributions start declining, it's usually a symptom of dee...\n\n3. Measuring the business value of open source communities | Opensource.com\n   https://opensource.com/article/19/10/measuring-business-value-open-source\n   October 17, 2019 - In Measuring the health of open source communities, I covered some of the key questions and metrics that we\u2019ve explored as part of the CHAOSS project as they relate to project found...\n\n4. Measuring the engagement of an open source software community - Bessemer Venture Partners\n   https://www.bvp.com/atlas/measuring-the-engagement-of-an-open-source-software-community\n   October 11, 2024 - Here\u2019s what we learned from that analysis. Open source projects are fundamentally driven by input from their communities, even if most contributors never write a line of code that e...\n\n5. How Open Source Metrics Influence Tool Adoption |...\n   https://business.daily.dev/resources/how-open-source-metrics-influence-tool-adoption/\n   February 17, 2026 - Active Contributor Counts: The number of contributors regularly making changes is a solid measure of a project\u2019s health. A smaller group of consistent contributors often signals st...\n\n6. The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics\n   https://arxiv.org/html/2605.11844\n   May 12, 2026 - The strong negative emotions like anger or dominance correlate with a lower probability of a PR being merged [52, 44]. A strong correlation also exists between sentiment and the final o...\n\n7. Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\n   https://arxiv.org/html/2509.16295\n   February 5, 2026 - Thus, the absence of robust support for community management can plant the seeds for society-scale accountability problems down the line, as OSS projects on those platforms become m...\n\n8. github-ospo/docs/open-source-health-metrics.md at main \u00b7 github/github-ospo\n   https://github.com/github/github-ospo/blob/main/docs/open-source-health-metrics.md\n   In fact, the amount and variety of data available can be a bit overwhelming, so we've selected a few key metrics that can provide insights into project and community health. The following GraphQL quer..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source founder share of commits reviews merges declines predict project health community driven\" --max-results 8", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [112] ASSISTANT · 2026-08-20 19:13:06 UTC

```
The community-health-metrics angle (CHAOSS project etc.) measures contributor base health but doesn't extract the founder SPECIFICALLY and model their fade trajectory as a survival predictor.

Let me now consolidate my findings and think carefully about whether the scaffolding-fade hypothesis is truly novel and what specifically distinguishes it.
```

### [113] TOOL CALL — think · 2026-08-20 19:13:06 UTC

```
{
  "thought": "**Summary of literature landscape (most relevant prior works):**\n\n1. **Avelino et al. 2019 \"On the abandonment and survival of open source projects\"** \u2014 Uses truck factor (TF) to identify when key developers abandon projects. Studies STATIC distinguishing characteristics (number of developers, commits, files, project age) at TFDD date. Survey asked WHY new TF developers joined abandoned projects. **Does NOT model the founder's involvement trajectory, does NOT distinguish founders from other key developers, does NOT measure gradual fade vs. abrupt departure.**\n\n2. **Noori et al. 2025 \"Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\"** \u2014 Analyzes GOVERNANCE.md text changes over time (Roles, Actions, Deontics). Studies how governance TRANSITIONS are documented. **Looks at textual governance artifacts, NOT at the founder's behavioral involvement trajectory in code/PR/issue activity. Does NOT predict survival outcomes.**\n\n3. **Kaushik & Chahal 2026 \"The Death Spiral of Open Source Projects\"** \u2014 Post-mortem analyzing aggregate PR workflow dynamics (friction, merge latency, sentiment) across INACTIVE projects. **Models collapse via aggregate workflow metrics; does NOT single out the founder or measure founder-specific fade curve. Explicitly does NOT study leader/founder departure per se.**\n\n4. **Karim et al. 2026 \"Predicting OSS Sustainability with Deep Temporal Neural Hierarchical Architectures\"** \u2014 Predicts OSS lifecycle STAGE (not survival-after-founders) from 24-month activity sequences using transformer models. **Aggregate activity, no founder role modeling, no founder-departure outcome. Zero mentions of \"founder/BDFL/successor/handover\".**\n\n5. **Feng et al. 2023 \"The State of Survival in OSS: The Impact of Diversity\"** \u2014 Studies CONTR IBUTOR retention / individual survivability and demographic diversity (gender/region/compensation). **Not about project survival after founder departure at all.**\n\n6. **Management literature on CEO/founder succession** \u2014 Studies binary founder-CEO vs successor-CEO transitions and firm survival. Even management literature notes \"75% of founder CEOs remain involved in some capacity\" \u2014 hinting that binary succession models miss the gradual-handover reality. But this literature doesn't operationalize the gradual fade TRAJECTORY as a measurable predictor.\n\n7. **Mentoring / newcomer socialization literature in OSS** \u2014 Studies newcomer-to-core transition, mentoring, onboarding. Longitudinal but treats founders as just \"developers\"; doesn't operationalize the founder's involvement trajectory SPECIFICALLY as a predictor of project survival after the founder leaves.\n\n**My proposed hypothesis \u2014 the core mechanism in one sentence:**\n\n\"Open-source project survival after founder departure is determined by the SHAPE of the founder's involvement trajectory PROJECT-WIDE over the project's lifespan, NOT by the founder-characteristics or community size at the moment of departure; specifically, projects survive when the founder's involvement fades gradually over time ('scaffolding fade'), allowing other contributors to incrementally take over decision-making, whereas projects collapse when the founder either maintains high involvement right up until an abrupt departure (no handover) or withdraws abruptly without a transition period.\"\n\nThis is a fundamentally different mechanism from any prior work because:\n- Truck factor / bus factor studies measure STATIC, SIZE-BASED risk at a moment (how many key developers could leave). My work measures the DYNAMIC SHAPE of how the FOUNDER's involvement evolved.\n- Governance transitions studies analyze TEXTUAL governance artifacts (GOVERNANCE.md). My work analyzes the founder's BEHAVIORAL trajectory across code commits, PR merges, code reviews, issue decisions.\n- Death-spiral studies focus on AGGREGATE community-level PR workflow dynamics AFTER decline begins. My work focuses on the FOUNDER-SPECIFIC involvement trajectory BEFORE the founder leaves (and predicts survival).\n- Sustainability prediction models aggregate activity sequences to predict \"lifecycle stage.\" My work singles out the founder's role and tests it as a mechanism.\n\n**Cross-domain transfer:** The \"scaffolding fade\" concept comes from Vygotsky / Bruner's educational psychology theory of scaffolding (with fading) \u2014 where a teacher gradually withdraws support as learners become competent. This transfers to the OSS domain by treating the founder's involvement as a continuous \"scaffolding\" for the contributor community. The EDUCATIONAL theory is well-established, but its application as a predictor of OSS project survival after FOUNDER departure has not been done.\n\n**Critical novelty check:** Is this just a gender-neutral way of saying \"don't have the founder do everything\"? No \u2014 the hypothesis is about the specific TRAJECTORY SHAPE (gradual fade vs. abrupt wax-wane vs. cliff) being the predictor. Two projects could have the same FRACTION of commits done by the founder at the moment of departure but very different fade trajectories leading to different survival outcomes.\n\n**Could an expert come up with this on their own?** An OSS sustainability expert who is NOT familiar with educational psychology scaffolding theory might intuit \"handover is good\" \u2014 but the precise operationalization as a fade-curve trajectory, and the mechanism (incremental ZPD-style capability transfer), would not be obvious. And existing literature does NOT model this \u2014 they either use static or aggregate measures.\n\nLet me also be careful to differentiate from \"leader succession planning\" in management literature \u2014 that's a NORTH-STAR NORMATIVE concept, often with binary founder-CEO vs successor-CEO. The mechanism here is the SMOOTHNESS/SLOWNESS of the decline in involvement, not who the successor is. So this differs operationally.\n\n**Verdict: This is a genuinely novel hypothesis** \u2014 a cross-field transfer of an established mechanism (scaffolding fade from educational psychology) to a domain where its specific form has not been operationalized, with a measurable, falsifiable mechanism. Now I need to check FEASIBILITY."
}
```

### [114] TOOL RESULT — think · 2026-08-20 19:13:06 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
```

### [115] ASSISTANT · 2026-08-20 19:13:39 UTC

```
Now let me verify feasibility. The key is: can I obtain the data needed (GitHub project git history including founder identity, commit/PR time series) and compute a fade trajectory that predicts survival — using Python tools and ~$10 OpenRouter budget?
```

### [116] TOOL CALL — invoke_skill · 2026-08-20 19:13:39 UTC

```
{
  "name": "aii-hf-datasets"
}
```

### [117] TOOL RESULT — invoke_skill · 2026-08-20 19:13:41 UTC

````
{"content": [{"cache_prompt": false, "type": "text", "text": "## Contents\n\n- Workflow (3-phase dataset discovery)\n- Scripts (Search, Preview, Download)\n\n**IMPORTANT - Parallel execution:** GNU `parallel` subshells do NOT inherit `source activate`. Use `export` for variables and **single-quoted** command templates so parallel's subshells can resolve them:\n```\nexport SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\"\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\"\n```\n\n---\n\n## Workflow: 3-Phase Dataset Discovery\n\n### Phase 1: Search for Datasets\nFind datasets with metadata (configs, splits, features, sizes)\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query \"sentiment analysis\" --limit 5\n```\n\n### Phase 2: Preview Dataset (if promising)\nInspect metadata AND sample rows in one call\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k\n```\n\n### Phase 3: Download Dataset (if suitable)\nDownload after reviewing the preview\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train\n```\n\n---\n\n## Scripts\n\n### Search HuggingFace Datasets (aii_hf_search_datasets.py)\n\nSearch and discover datasets on HuggingFace Hub.\n\n**Example input:**\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_search_datasets.py --query \"text classification\" --limit 5\n```\n\n**Parallel execution (multiple queries):**\n\nIMPORTANT: Use full python path with GNU parallel (venv activate does NOT work in parallel subshells):\n```bash\nexport SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && \\\nexport S=\"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" && \\\nparallel -j 10 -k --group --will-cite '$PY $S --query {} --limit 3' ::: 'sentiment' 'classification' 'translation'\n```\n\n**Example output:**\n```\nFound 5 dataset(s) for query='text classification'\n\n============================================================\nDataset 1: stanfordnlp/imdb\nDownloads: 2,500,000 | Likes: 1,234\nDescription: Large Movie Review Dataset for binary sentiment classification...\nTags: text-classification, en, sentiment-analysis\n```\n\n**Result fields per dataset:**\n\nEach entry in ``results`` carries:\n\n- ``id`` / ``downloads`` / ``likes`` / ``tags`` / ``description`` \u2014 standard\n  HF metadata\n- ``has_loader_script`` (bool) \u2014 repo ships a top-level ``<repo>.py`` loader.\n  ``datasets>=3`` won't run these directly; the dataset is reachable only\n  via the Datasets Server's pre-converted parquet shards. Treat as a yellow\n  flag.\n- ``loadable`` (bool) \u2014 **prefer datasets where this is ``True``.** Means\n  the dataset is reachable via *some* path: either native parquet (no\n  script) or HF auto-converted the script's output to parquet. When\n  ``False``, the script needs deps HF can't install (e.g. ``conllu``,\n  custom audio decoders) and ``aii_hf_datasets__download_datasets`` will\n  fail \u2014 pick a different candidate.\n\n**Parameters:**\n\n`--query` (optional)\n- Search query string\n- Example: `--query \"sentiment analysis\"`\n\n`--limit` (optional)\n- Maximum number of results (default: 5)\n\n`--tags` (optional)\n- Filter by tags (comma-separated)\n- Format: `category:value`\n- Examples: `language:en`, `task_categories:text-classification`\n\n`--sort` (optional)\n- Sort by field: `downloads`, `likes` (default: downloads)\n\n**Tips:**\n- Search displays full dataset metadata\n- Use tags to filter: `--tags \"language:en,task_categories:translation\"`\n\n---\n\n### Preview HuggingFace Dataset (aii_hf_preview_datasets.py)\n\nInspect a specific dataset - shows metadata AND sample rows.\n\n**Example input:**\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_preview_datasets.py openai/gsm8k --num-rows 5\n```\n\n**Parallel execution (multiple datasets):**\n\nIMPORTANT: Use full python path with GNU parallel:\n```bash\nexport SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && \\\nexport S=\"$SKILL_DIR/scripts/aii_hf_preview_datasets.py\" && \\\nparallel -j 10 -k --group --will-cite '$PY $S {} --num-rows 3' ::: 'openai/gsm8k' 'imdb' 'squad'\n```\n\n**Example output:**\n```\n============================================================\nDataset: openai/gsm8k\n============================================================\nDownloads: 425,109 | Likes: 1,102\n\nDescription: GSM8K (Grade School Math 8K) is a dataset of 8.5K high quality\nlinguistically diverse grade school math word problems...\n\nConfigs: main, socratic\n\n--- Sample Rows (train) ---\nColumns: question, answer\n\nRow 1:\n  question: Natalia sold clips to 48 of her friends in April...\n  answer: Natalia sold 48/2 = <<48/2=24>>24 clips in May...\n```\n\n**Parameters:**\n\n`dataset_id` (required, positional)\n- HuggingFace dataset ID\n- Examples: `openai/gsm8k`, `glue`, `imdb`\n\n`--config` (optional)\n- Dataset configuration/subset name\n- Auto-detects first config if not specified\n\n`--split` (optional)\n- Split to preview (default: `train`)\n\n`--num-rows` (optional)\n- Number of sample rows (default: 5, max: 20)\n\n**Tips:**\n- Use after search to verify data structure\n- Streaming mode - doesn't download full dataset\n\n---\n\n### Download HuggingFace Dataset (aii_hf_download_datasets.py)\n\nDownload datasets and save to files.\n\n**Example input:**\n```bash\nSKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\n$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_hf_download_datasets.py openai/gsm8k --config main --split train\n```\n\n**Parallel execution (multiple datasets):**\n\nIMPORTANT: Use full python path with GNU parallel. Use `eval {}` pattern when datasets need different flags (e.g. `--config`):\n```bash\nexport SKILL_DIR=\"$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-hf-datasets\" && \\\nexport PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && \\\nexport S=\"$SKILL_DIR/scripts/aii_hf_download_datasets.py\" && \\\nparallel -j 10 -k --group --will-cite 'eval {}' ::: '$PY $S openai/gsm8k --config main --split train' '$PY $S imdb --split train' '$PY $S squad --split train'\n```\n\n**Example output:**\n```\nDownloaded: openai/gsm8k\n\n  train:\n    Rows: 7,473\n    Preview: temp/datasets/preview_openai_gsm8k_main_train.json\n    Mini: temp/datasets/mini_openai_gsm8k_main_train.json\n    Full: temp/datasets/full_openai_gsm8k_main_train.json\n```\n\n**Parameters:**\n\n`dataset_id` (required, positional)\n- HuggingFace dataset ID\n- Examples: `openai/gsm8k`, `imdb`\n\n`--config` (optional)\n- Dataset configuration/subset name\n- Use preview to see available configs\n\n`--split` (optional)\n- Specific split to load (e.g., `train`, `test`)\n- If not specified, loads all splits\n\n`--output-dir` (optional)\n- Output directory (default: `temp/datasets/`)\n\n**Output files (auto-saved):**\n1. **Preview**: `preview_{dataset}_{split}.json` - 3 truncated rows - **READ THIS** for quick inspection\n2. **Mini**: `mini_{dataset}_{split}.json` - 3 full rows - for development/testing\n3. **Full**: `full_{dataset}_{split}.json` - All rows - **DO NOT READ directly** - use as input path for code\n\n**Tips:**\n- Only read preview file directly with Read tool\n- Mini and full are input paths for processing code\n\n**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly \u2014 bypassing the server:\n```bash\nuv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r \"$SKILL_DIR/scripts/server_requirements.txt\"\n```\n\n---\nThis skill is located at `/ai-inventor/.claude/skills/aii-hf-datasets`. Any files it references (e.g. under `scripts/`, `references/`, `assets/`) are relative to that directory."}], "is_error": false, "skill_name": "aii-hf-datasets", "kind": "InvokeSkillObservation"}
````

### [118] ASSISTANT · 2026-08-20 19:13:45 UTC

```
Let me search for GitHub-related datasets on HuggingFace that might have commit/PR time-series with user identity, and check feasibility by examining what's available.
```

### [119] TOOL CALL — terminal · 2026-08-20 19:13:45 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github commits pull requests developer activity history\" --limit 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [120] TOOL RESULT — terminal · 2026-08-20 19:13:45 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Found 0 dataset(s) for query='github commits pull requests developer activity history'"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github commits pull requests developer activity history\" --limit 8", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [121] TOOL CALL — terminal · 2026-08-20 19:14:55 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"open source software repository evolution\" --limit 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [122] TOOL RESULT — terminal · 2026-08-20 19:14:57 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Found 0 dataset(s) for query='open source software repository evolution'"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"open source software repository evolution\" --limit 8", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [123] TOOL CALL — terminal · 2026-08-20 19:15:02 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [124] TOOL RESULT — terminal · 2026-08-20 19:15:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": ""}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 8", "exit_code": -1, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": null, "py_interpreter_path": null, "prefix": "", "suffix": "\n[The command has no new output after 30 seconds. You may wait longer to see additional output by sending empty command '', send other commands to interact with the current process, send keys (\"C-c\", \"C-z\", \"C-d\") to interrupt/kill the previous command before sending your new command, or use the timeout parameter in terminal for future commands.]"}, "full_output_save_dir": null, "kind": "TerminalObservation"}
```

### [125] TOOL CALL — terminal · 2026-08-20 19:16:06 UTC

```
{
  "command": "",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [126] TOOL RESULT — terminal · 2026-08-20 19:16:06 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "No previous running command to retrieve logs from."}], "is_error": true, "command": "", "exit_code": null, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": null, "py_interpreter_path": null, "prefix": "", "suffix": ""}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [127] TOOL CALL — terminal · 2026-08-20 19:16:08 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 5",
  "is_input": false,
  "timeout": 60.0,
  "reset": false
}
```

### [128] TOOL RESULT — terminal · 2026-08-20 19:16:19 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Error: (Request ID: Root=1-6a875281-3f7a4ca93942b5df53e69d1d;f97de847-0569-4ae3-bb16-fc66ef3e58a4)\n\n429 Too Many Requests: you have reached your 'api' rate limit.\nRetry after 31 seconds (0/1000 requests remaining in current 300s window).\nUrl: https://huggingface.co/api/datasets?search=github&sort=downloads&limit=5.\nWe had to rate limit you, you hit the quota of 1000 api requests per 5 minutes period. Upgrade to a PRO user or Team/Enterprise organization account (https://hf.co/pricing) to get higher limits. See https://huggingface.co/docs/hub/rate-limits"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 5", "exit_code": 1, "timeout": false, "metadata": {"exit_code": 1, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 1.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [129] ASSISTANT · 2026-08-20 19:17:46 UTC

```
Hit the HuggingFace rate limit. I'll wait then check again, but let me think about feasibility more directly first.
```

### [130] TOOL CALL — think · 2026-08-20 19:17:46 UTC

```
{
  "thought": "**Feasibility assessment \u2014 can I test this hypothesis?**\n\n**Data needs:**\n1. A set of OSS projects (50-200 will do) where:\n   a. The \"founder\" is identifiable (typically the first committer, or the creator of the repo)\n   b. The founder eventually departs (stops committing / becomes inactive for a long period)\n   c. The project either survives (new active maintainers continue work) or dies (commits drop to ~0)\n2. For each project, the time series of:\n   a. The founder's share of commits per month/quarter (the \"involvement trajectory\")\n   b. The founder's share of PR merges per month/quarter (decision-making trajectory)\n   c. Periodically: the bus factor / number of \"key developers\"\n3. Survival outcome label: does the project survive (continued activity after founder leaves) or die?\n\n**Where do I get the data?**\n- GitHub API: rich dataset with commits, PRs, comments, merge decisions, timestamps, author IDs. Public, free (with rate limits ~60/h unauth, 5000/h authed). I can clone repos and use git log too.\n- Avelino et al. 2019 truck-factor dataset (1,932 GitHub projects with identified TF developers) \u2014 GitHub public dataset.\n- Could use a small curated list of well-known OSS projects for which we know the founderdeparture outcome (e.g., Python \u2192 Guido stepped down \u2192 survived; Redis \u2192 antirez stepped down \u2192 survived/maintained; Signal \u2192 community-led; many one-off projects \u2192 died).\n\n**My specific plan:**\nThe cleanest test is a CURATED-LIST study using well-known, well-archived OSS projects with documented founder departure. By focusing on ~50-100 GitHub projects (e.g., from Avelino et al.'s dataset, where I can identify founders and outcomes), I can clone the repos and compute the founder's involvement trajectory entirely locally with Python (no API call needed beyond cloning repos).\n\n**Computational needs:**\n- Clone ~100 repos (<10GB likely)\n- Git log parsing \u2192 straightforward Python\n- Compute founder involvement trajectory \u2192 fitting a curve shape parameter per project\n- Logistic regression / survival analysis \u2192 scikit-learn, lifelines, scipy\n- All Python-based, runs on local hardware, no GPU needed\n\n**OpenRouter / LLM usage:**\n- Mostly I DON'T need an LLM for the hypothesis generation phase \u2014 that's done. For TEST/INV later, I might want LLMs to identify founders/contributors from commit metadata or GitHub usernames (e.g., to confirm \"user X is the founder-departed\" when commit authors can be tangled). But for the hypothesis ROUGH test, git authorship identification is mostly deterministic (the user with the very earliest commits, or the repo owner).\n- $10 budget is plenty for ad-hoc queries if needed.\n\n**Ambition vs. risk:**\n- The hypothesis is testable, falsifiable, and has good potential for a clear positive result (existing static factor studies show project size & TF don't predict survival \u2014 so a temporal mechanism should outperform). Even if I get partial signal, that's still informative.\n\n**Verdict: Feasible.** A test using ~100 GitHub repos with git log computation, scikit-learn logistic regression/survival analysis, and curve shape extraction is achievable within the budget. No GPU needed. Data is openly available.\n\nLet me wait a moment and try HuggingFace again, but actually the data plan I have doesn't strictly need HF \u2014 I can directly clone GitHub repos. The hypothesis is feasible without an HF dataset. Let me also fetch the GitHub blog post about decision-making to confirm direction and maybe check the Hatch 2018 \"fork limbo\" patterns to think about edge cases."
}
```

### [131] TOOL RESULT — think · 2026-08-20 19:17:46 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
```

### [132] TOOL CALL — terminal · 2026-08-20 19:17:52 UTC

```
{
  "command": "sleep 35 && export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 6",
  "is_input": false,
  "timeout": 80.0,
  "reset": false
}
```

### [133] TOOL RESULT — terminal · 2026-08-20 19:18:43 UTC

````
{"content": [{"cache_prompt": false, "type": "text", "text": "Found 6 dataset(s) for query='github'\n\n============================================================\nDataset 1: codeparrot/github-code\nDownloads: 30,232 | Likes: 416\nDescription:\n# GitHub Code Dataset\n\n## Dataset Description\nThe GitHub Code dataset consists of 115M code files from GitHub in 32 programming languages with 60 extensions totaling in 1TB of data. The dataset was c...\nTags: task_categories:text-generation, task_ids:language-modeling, language_creators:crowdsourced, language_creators:expert-generated, multilinguality:multilingual\n\n============================================================\nDataset 2: AdhyanshVerma/open-github-major-repos\nDownloads: 19,348 | Likes: 1\nDescription: <h1 align=\"center\">\ud83c\udf10 AdhyanshVerma's Open GitHub Major Repos</h1>\n\n**An elite, curated collection of GitHub commit metadata from the world's most influential technology companies: Microsoft, Google, M...\nTags: task_categories:text-generation, task_categories:feature-extraction, language:en, license:gfdl, size_categories:10M<n<100M\n\n============================================================\nDataset 3: codeparrot/github-code-clean\nDownloads: 14,570 | Likes: 142\nDescription: This is a cleaner version of [Github-code dataset](https://huggingface.co/datasets/codeparrot/github-code), we add the following filters:\n* Average line length < 100\n* Alpha numeric characters fractio...\nTags: license:apache-2.0, size_categories:10M<n<100M, modality:text, library:datasets, library:mlcroissant\n\n============================================================\nDataset 4: hasankursun/github-code-2025-language-split\nDownloads: 6,321 | Likes: 13\nDescription:\n## \ud83d\udcdc Source Data & Attribution\n\nThis dataset is a processed derivative of **[nick007x/github-code-2025](https://huggingface.co/datasets/nick007x/github-code-2025)**.\n\n### Origination\n\nThe original da...\nTags: source_datasets:nick007x/github-code-2025, license:other, size_categories:100M<n<1B, format:parquet, modality:text\n\n============================================================\nDataset 5: ronantakizawa/github-top-code\nDownloads: 5,486 | Likes: 125\nDescription:\n# GitHub Top Developer Source Code\n\nA curated dataset of 1.3M+ source code files from **GitHub's top ranked developers (2015-2025)**.\n\nThis dataset is based on the top ranked developers from this dat...\nTags: task_categories:text-generation, language:code, license:mit, size_categories:1M<n<10M, format:parquet\n\n============================================================\nDataset 6: Brunobkr/llama.cpp_AlgMor24_github\nDownloads: 4,208 | Likes: 0\nDescription: # \u03a9FFF\u03a3LLIa \u2022 llama.cpp \u2022 AlgMor24\n\n<div align=\"center\">\n\n```\n   \u2588\u2588\u2588\u2588\u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2588\u2588\u2588\u2588\u2588\u2557\u2588\u2588\u2557     \u2588\u2588\u2557     \u2588\u2588\u2557 \u2588\u2588\u2588\u2588\u2588\u2557\n  \u2588\u2588\u2554\u2550\u2550\u2550\u2588\u2588\u2557\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2554\u2550\u2550\u2550\u2550\u255d\u2588\u2588\u2551     \u2588\u2588\u2551     \u2588\u2588\u2551\u2588\u2588\u2554\u2550\u2550\u2588\u2588\u2557\n  \u2588\u2588\u2551   \u2588\u2588\u2551\u2588...\nTags: doi:10.57967/hf/10004, region:us"}], "is_error": false, "command": "sleep 35 && export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 6", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
````

### [134] ASSISTANT · 2026-08-20 19:18:51 UTC

```
The HF datasets aren't directly useful (they're code content, not commit history with metadata). My feasibility approach stands: clone repos directly via git and extract commit/PR metadata. Let me also check the GitHub readme article on decision-making to make sure my mechanism framing aligns with actual OSS practice.
```

### [135] TOOL CALL — terminal · 2026-08-20 19:18:51 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://github.com/readme/featured/oss-decision-making\" --max-chars 8000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [136] TOOL RESULT — terminal · 2026-08-20 19:18:53 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://github.com/readme/featured/oss-decision-making\nType: HTML\nLength: 21595 chars (truncated)\n\n--- Content ---\n\nSkip to content\n\n## Navigation Menu\n\n[](/)\n\n[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Freadme%2Ffeatured%2Foss-decision-making)\n\n  * Platform\n\n    * AI CODE CREATION\n      * [GitHub CopilotWrite better code with AI](https://github.com/features/copilot)\n      * [GitHub Copilot appDirect agents from issue to merge](https://github.com/features/ai/github-app)\n      * [MCP RegistryIntegrate external tools](https://github.com/mcp)\n\n    * DEVELOPER WORKFLOWS\n      * [ActionsAutomate any workflow](https://github.com/features/actions)\n      * [CodespacesInstant dev environments](https://github.com/features/codespaces)\n      * [IssuesPlan and track work](https://github.com/features/issues)\n      * [Code ReviewManage code changes](https://github.com/features/code-review)\n      * [Code QualityEnforce quality at merge](https://github.com/features/code-quality)\n\n    * APPLICATION SECURITY\n      * [GitHub Advanced SecurityFind and fix vulnerabilities](https://github.com/security/advanced-security)\n      * [Code securitySecure your code as you build](https://github.com/security/advanced-security/code-security)\n      * [Secret protectionStop leaks before they start](https://github.com/security/advanced-security/secret-protection)\n\n    * EXPLORE\n      * [Why GitHub](https://github.com/why-github)\n      * [Documentation](https://docs.github.com)\n      * [Blog](https://github.blog)\n      * [Changelog](https://github.blog/changelog)\n      * [Marketplace](https://github.com/marketplace)\n\n[View all features](https://github.com/features)\n\n  * Solutions\n\n    * BY COMPANY SIZE\n      * [Enterprises](https://github.com/enterprise)\n      * [Small and medium teams](https://github.com/team)\n      * [Startups](https://github.com/enterprise/startups)\n      * [Nonprofits](https://github.com/solutions/industry/nonprofits)\n\n    * BY USE CASE\n      * [App Modernization](https://github.com/solutions/use-case/app-modernization)\n      * [DevSecOps](https://github.com/solutions/use-case/devsecops)\n      * [DevOps](https://github.com/solutions/use-case/devops)\n      * [CI/CD](https://github.com/solutions/use-case/ci-cd)\n      * [View all use cases](https://github.com/solutions/use-case)\n\n    * BY INDUSTRY\n      * [Healthcare](https://github.com/solutions/industry/healthcare)\n      * [Financial services](https://github.com/solutions/industry/financial-services)\n      * [Manufacturing](https://github.com/solutions/industry/manufacturing)\n      * [Government](https://github.com/solutions/industry/government)\n      * [View all industries](https://github.com/solutions/industry)\n\n[View all solutions](https://github.com/solutions)\n\n  * Resources\n\n    * EXPLORE BY TOPIC\n      * [AI](https://github.com/resources/articles?topic=ai)\n      * [Software Development](https://github.com/resources/articles?topic=software-development)\n      * [DevOps](https://github.com/resources/articles?topic=devops)\n      * [Security](https://github.com/resources/articles?topic=security)\n      * [View all topics](https://github.com/resources/articles)\n\n    * EXPLORE BY TYPE\n      * [Customer stories](https://github.com/customer-stories)\n      * [Events & webinars](https://github.com/resources/events)\n      * [Ebooks & reports](https://github.com/resources/whitepapers)\n      * [Business insights](https://github.com/solutions/executive-insights)\n      * [GitHub Skills](https://skills.github.com)\n\n    * SUPPORT & SERVICES\n      * [Documentation](https://docs.github.com)\n      * [Customer support](https://support.github.com)\n      * [Community forum](https://github.com/orgs/community/discussions)\n      * [Trust center](https://github.com/trust-center)\n      * [Partners](https://github.com/partners)\n\n[View all resources](https://github.com/resources)\n\n  * Open Source\n\n    * COMMUNITY\n      * [GitHub SponsorsFund open source developers](https://github.com/open-source/sponsors)\n\n    * PROGRAMS\n      * [Security Lab](https://securitylab.github.com)\n      * [Maintainer Community](https://maintainers.github.com)\n      * [Accelerator](https://github.com/open-source/accelerator)\n      * [GitHub Stars](https://stars.github.com)\n      * [Archive Program](https://archiveprogram.github.com)\n\n    * REPOSITORIES\n      * [Topics](https://github.com/topics)\n      * [Trending](https://github.com/trending)\n      * [Collections](https://github.com/collections)\n\n  * Enterprise\n\n    * ENTERPRISE SOLUTIONS\n      * [Enterprise platformAI-powered developer platform](https://github.com/enterprise)\n\n    * AVAILABLE ADD-ONS\n      * [GitHub Advanced SecurityEnterprise-grade security features](https://github.com/security/advanced-security)\n      * [Copilot for BusinessEnterprise-grade AI features](https://github.com/features/copilot/copilot-business)\n      * [Premium SupportEnterprise-grade 24/7 support](https://github.com/enterprise/premium-support)\n\n  * [Pricing](https://github.com/pricing)\n\n\n\nSearch`/`\n\n[Sign in](/login?return_to=https%3A%2F%2Fgithub.com%2Freadme%2Ffeatured%2Foss-decision-making)\n\n[Sign up](/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2Freadme%2Ffeatured%2Foss-decision-making&source=header)\n\nYou signed in with another tab or window. [Reload]() to refresh your session. You signed out in another tab or window. [Reload]() to refresh your session. You switched accounts on another tab or window. [Reload]() to refresh your session. Dismiss alert\n\n{{ message }}\n\nArtwork: Micha Huigen\n\n[ ](/readme)\n\n#  Decisions, decisions: Principles for making important choices in open source\n\nDecisions are the essence of open source maintainership.\n\nKlint Finley // June 14, 2022\n\n[ The ReadME Project](/readme)\n\nOpen ReadME Project Menu\n\n[ ](/readme)\n\n##  Browse by story type\n\n  * [ Featured Articles ](/readme/featured)\n  * [ Developer Stories ](/readme/stories)\n  * [ Guides ](/readme/guides)\n  * [ The ReadMe Podcast ](/readme/podcast)\n\n\n\n## Explore Topics\n\n[ See all topics  ](/readme/topics)\n\n  * [ AI ](/readme/artificial-intelligence)\n  * [ Application Security ](/readme/application-security)\n  * [ Career Development ](/readme/career-development)\n  * [ DevOps & Automation ](/readme/devops-automation)\n  * [ Maintainer ](/readme/maintainer)\n  * [ Programming ](/readme/programming)\n\n\n\n  * [Nominate a developer](/readme/nominate)//\n  * [Support the community](/sponsors)\n\n\n\n**The ReadME Project** amplifies the voices of the open source community: the maintainers, developers, and teams whose contributions move the world forward every day.\n\n  * [ ](https://twitter.com/intent/tweet?url=https%3A%2F%2Fgithub.com%2Freadme%2Ffeatured%2Foss-decision-making&text=)\n  * [ ](https://www.facebook.com/sharer/sharer.php?u=https%3A%2F%2Fgithub.com%2Freadme%2Ffeatured%2Foss-decision-making&quote=)\n  * [ ](https://www.linkedin.com/sharing/share-offsite/?url=https%3A%2F%2Fgithub.com%2Freadme%2Ffeatured%2Foss-decision-making)\n\n\n\nJarek Potiuk thought [Apache Airflow](https://github.com/apache/airflow)\u2019s dependency management system was broken\u2014and that he knew how to fix it. Then the principal engineer at Polidea, Potiuk was new to the open source workflow management project and eager to make his first contribution. So, he jumped into Airflow\u2019s Slack and proposed a new way to handle dependencies.\n\nAfter talking through his idea with several people, Potiuk sent an email to the Airflow developers\u2019 mailing list announcing his plan to rewrite the project\u2019s dependency management system. \u201cI thought I had consensus,\u201d says Potiuk, now a member of Apache Airflow\u2019s Project Management Committee. \u201cBut one of the core maintainers sent a firm yet gentle reply explaining that I hadn\u2019t actually gone through the appropriate process.\u201d\n\nAirflow is a large project with several stakeholders, including major companies that employ many of the project\u2019s maintainers. Like all other [Apache Software Foundation](https://www.apache.org/) projects, [Airflow](https://github.com/apache/airflow) requires all major changes to seek consensus through the developer mailing list. And th"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://github.com/readme/featured/oss-decision-making\" --max-chars 8000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [137] ASSISTANT · 2026-08-20 19:19:01 UTC

```
This article emphasizes that decision-making authority in OSS is the central thing and that major projects use documented processes to share decision-making power. This aligns well with my hypothesis — the trajectory of how decision-making (PR merges / commits by the founder vs. by others) evolves over time is the relevant quantity. 

I now have enough confidence to write the hypothesis. Let me update my task list and do final clarifying searches on the closest works to summarize them well.
```

### [138] TOOL CALL — task_tracker · 2026-08-20 19:19:01 UTC

```
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "No user uploads found - empty folder",
      "status": "done"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes": "8 directions brainstormed; settled on scaffolding-fade trajectory as most novel",
      "status": "done"
    },
    {
      "title": "Web search for landscape overview of each direction",
      "notes": "Found landscape: bus factor, governance transitions, diversity, abandonment empirical, death spiral deep temporal neural, sustainability random forest - NONE about founder involvement trajectory",
      "status": "done"
    },
    {
      "title": "Fetch and read potentially relevant papers",
      "notes": "Read Avelino 2019 (TFDD), Noori 2509 (governance), Feng 2023 (diversity), death spiral 2026 (PR dynamics), deep temporal neural 2026 (lifecycle stage) - none model founder scaffolding fade",
      "status": "done"
    },
    {
      "title": "Adversarial novelty check",
      "notes": "Scaffolding-fade trajectory is novel - no existing OSS work models founder involvement shape as survival predictor; closest prior work uses static or aggregate metrics",
      "status": "done"
    },
    {
      "title": "Feasibility check",
      "notes": "Feasible: clone ~50-100 GitHub repos, compute founder commit/merge trajectory with git log, fit logistic regression/survival analysis in Python. No GPU needed. LLM budget is spare.",
      "status": "done"
    },
    {
      "title": "Write hypothesis JSON output",
      "notes": "Write JSON to .sdk_openhands_agent_struct_out.json",
      "status": "in_progress"
    }
  ]
}
```

### [139] TOOL RESULT — task_tracker · 2026-08-20 19:19:01 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "No user uploads found - empty folder", "status": "done"}, {"title": "Brainstorm 5-7 diverse directions without searching", "notes": "8 directions brainstormed; settled on scaffolding-fade trajectory as most novel", "status": "done"}, {"title": "Web search for landscape overview of each direction", "notes": "Found landscape: bus factor, governance transitions, diversity, abandonment empirical, death spiral deep temporal neural, sustainability random forest - NONE about founder involvement trajectory", "status": "done"}, {"title": "Fetch and read potentially relevant papers", "notes": "Read Avelino 2019 (TFDD), Noori 2509 (governance), Feng 2023 (diversity), death spiral 2026 (PR dynamics), deep temporal neural 2026 (lifecycle stage) - none model founder scaffolding fade", "status": "done"}, {"title": "Adversarial novelty check", "notes": "Scaffolding-fade trajectory is novel - no existing OSS work models founder involvement shape as survival predictor; closest prior work uses static or aggregate metrics", "status": "done"}, {"title": "Feasibility check", "notes": "Feasible: clone ~50-100 GitHub repos, compute founder commit/merge trajectory with git log, fit logistic regression/survival analysis in Python. No GPU needed. LLM budget is spare.", "status": "done"}, {"title": "Write hypothesis JSON output", "notes": "Write JSON to .sdk_openhands_agent_struct_out.json", "status": "in_progress"}], "kind": "TaskTrackerObservation"}
```

### [140] ASSISTANT · 2026-08-20 19:20:10 UTC

```
Let me do one final sanity check search to ensure there's no super-direct overlap I missed, looking for "founder involvement curve" OSS specifically.
```

### [141] TOOL CALL — terminal · 2026-08-20 19:20:10 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project founder departure gradual versus abrupt handover predict community continuity\" --max-results 8",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [142] TOOL RESULT — terminal · 2026-08-20 19:20:24 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source project founder departure gradual versus abrupt handover predict community continuity  [general via exa]\nFound: 8 results\n\n1. Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\n   https://arxiv.org/html/2509.16295\n   # Patterns in the Transition From Founder-Leadership to Community Governance of Open Source\n\nOpen MIND. Published: 2025-09-19. 0 citations.\n\n## Authors\n\n- Noori, Mobina\n- Chakraborti, Mahasweta\n- Zhan...\n\n2. Keeping an open source project alive when people leave | Opensource.com\n   https://opensource.com/article/19/5/code-missing-community-management\n   Keeping an open source project alive when people leave | Opensource.com\n\nSearch\n\n# Keeping an open source project alive when people leave\n\nHow to find out what's done, what's not, and what's missing.\n...\n\n3. Abandonment and Resilience: Understanding Core Developer Turnover in Open-Source Software\n   https://www.jstage.jst.go.jp/article/transinf/E108.D/11/E108.D_2025EDL8005/_article\n   Abandonment and Resilience: Understanding Core Developer Turnover in Open-Source Software\n\nIEICE Transactions on Information and Systems\n\nOnline ISSN : 1745-1361 Print ISSN : 0916-8532\n\n- Journal home...\n\n4. Core Developer Turnover in the Rust Package Ecosystem: Prevalence, Impact, and Awareness | Proceedings of the ACM on Software Engineering\n   https://dl.acm.org/doi/10.1145/3729392\n   Core Developer Turnover in the Rust Package Ecosystem: Prevalence, Impact, and Awareness | Proceedings of the ACM on Software Engineering skip to main content\n\nContents\n\n## Abstract\n\n### Abstract\n\nCon...\n\n5. How Does Core Contributor Disengagement Impact Open Source Project Activity? A !asi-Experiment\n   https://biancatrink.github.io/files/papers/ICSE2026.pdf\n   ICSE \u201926, April 12\u201318, 2026, Rio de Janeiro, Brazil Yunqi Chen, Klaas-Jan Stol, Fabio Santos, Daniel German, and Bianca Trinkenreich\n\nHow Does Core Contributor Disengagement Impact Open Source Project...\n\n6. How to Hand Off an Open Source Project\n   https://www.fosshub.com/resources/maintainers/handoff/\n   How to Hand Off an Open Source Project\n\n# How to Hand Off an Open Source Project\n\nAn open source project handoff transfers trust, context, access, and public legitimacy, not only repository ownership....\n\n7. How Open Source Projects Change Hands | Andrew Nesbitt\n   https://nesbitt.io/2026/06/16/how-open-source-projects-change-hands.html\n   How Open Source Projects Change Hands | Andrew Nesbitt\n\nDumb Ways for an Open Source Project to Die listed the ways projects end up dead, and most of the entries describe a moment where maintainership...\n\n8. Open Source Maintainer Succession Planning Guide\n   https://safeguard.sh/resources/blog/open-source-maintainer-succession-planning\n   Open Source Maintainer Succession Planning Guide\n\nOpen Source\n\n# Open Source Maintainer Succession Planning: A Supply Chain Imperative\n\nWhen a solo maintainer disappears, entire dependency chains are ..."}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project founder departure gradual versus abrupt handover predict community continuity\" --max-results 8", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [143] ASSISTANT · 2026-08-20 19:20:32 UTC

```
Item 5 is very recent and relevant — "How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment" ICSE 2026. Let me fetch it to check overlap with my mechanism precisely.
```

### [144] TOOL CALL — terminal · 2026-08-20 19:20:32 UTC

```
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://biancatrink.github.io/files/papers/ICSE2026.pdf\" --max-chars 9000",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [145] TOOL RESULT — terminal · 2026-08-20 19:20:34 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://biancatrink.github.io/files/papers/ICSE2026.pdf\nType: PDF\nLength: 81941 chars (truncated)\n\n--- Content ---\n\nICSE \u201926, April 12\u201318, 2026, Rio de Janeiro, Brazil\nYunqi Chen, Klaas-Jan Stol, Fabio Santos, Daniel German, and Bianca Trinkenreich\nHow Does Core Contributor Disengagement Impact Open Source\nProject Activity? A asi-Experiment\nYunqi Chen\nZhejiang University\nHangzhou, Zhejiang, China\nyunqichen@zju.edu.cn\nKlaas-Jan Stol\nLero and University College Cork\nCork, Ireland\nk.stol@ucc.ie\nFabio Santos\nColorado State University\nFort Collins, CO, USA\nfabio.deabreusantos@colostate.edu\nDaniel German\nUniversity of Victoria\nVictoria, BC, Canada\ndmg@uvic.ca\nBianca Trinkenreich\nColorado State University\nFort Collins, CO, USA\nbianca.trinkenreich@colostate.edu\nAbstract\nThe sustainability of Open Source Software (OSS) projects often\ndepends on a small group of core contributors. When these contrib-\nutors disengage, projects may face disruption; however, the con-\nsequences of such disengagement on OSS contribution workows\nremain underexplored. This paper presents a large-scale quasi-\nexperimental study quantifying the impact of core contributor\ndisengagement on pull request (PR) throughput, acceptance rate,\nand time to merge. We analyzed over 35 million PRs across 50,804\nGitHub repositories, identifying 95,958 disengagement bursts (one\nor more core contributors becoming inactive for >365 days within\nthe same week) involving 174,887 contributors. Using Dierence-in-\nDierences with matched control groups, we found that the impact\nvaries substantially with contributor and project characteristics.\nDisengagements of contributors with a high share of commits lead\nto pronounced declines in throughput and acceptance, while long-\ntenured contributors\u2019 disengagements have milder eects on those\nmetrics but increase merge time, suggesting loss of tacit project\nknowledge. These ndings provide empirical evidence of how core\ncontributors\u2019 disengagement inuences OSS workows and high-\nlight structural factors associated with project resilience.\nCCS Concepts\n\u2022 Software and its engineering ! Open source model.\nKeywords\nOpen source software, disengagement, attrition, productivity\nACM Reference Format:\nYunqi Chen, Klaas-Jan Stol, Fabio Santos, Daniel German, and Bianca\nTrinkenreich. 2026. How Does Core Contributor Disengagement Impact\nOpen Source Project Activity? A Quasi-Experiment. In 2026 IEEE/ACM 48th\nInternational Conference on Software Engineering (ICSE \u201926), April 12\u201318,\n2026, Rio de Janeiro, Brazil. ACM, New York, NY, USA, 14 pages. https:\n//doi.org/10.1145/3744916.3773135\nThis work is licensed under a Creative Commons Attribution 4.0 International License.\nICSE \u201926, Rio de Janeiro, Brazil\n\u00a9 2026 Copyright held by the owner/author(s).\nACM ISBN 979-8-4007-2025-3/26/04\nhttps://doi.org/10.1145/3744916.3773135\n1\nIntroduction\nOpen Source Software (OSS) forms the backbone of today\u2019s digital\ninfrastructure, with an estimated 60% of websites relying on OSS\ntechnologies [40]. Despite their importance, OSS projects are highly\nvulnerable to the disengagement of key contributors, which can neg-\natively impact project sustainability [14]. The loss of contributors is\na major concern among OSS maintainers, project, and community\nmanagers, second only to poor code quality [51]. Core developer\nturnover has been shown to be a common and often unplanned phe-\nnomenon, even in mature ecosystems such as Rust, where over 60%\nof Rust modules (called \u2018crates\u2019) experienced at least one turnover\nevent over two years [24]. OSS project communities tend to fol-\nlow an \u2018onion\u2019 structure [16], with most contributors participating\neither sporadically or for short periods [4, 13], or with a limited\ncontribution rate. Only a limited number of core contributors are\ndeeply involved in the daily development process. This dependency\non a smaller number of core developers represents a major risk to\nOSS projects. Nearly two-thirds of 133 popular GitHub projects rely\non only one or two developers to survive [3]. In a follow-up study,\n16% of the sampled projects were abandoned by maintainers, and\n59% of those did not survive [2].\nNearly half of OSS project failures can be attributed to internal\nteam issues, such as contributor turnover and the loss of critical\nknowledge [14]. When core contributors\u2014sometimes referred to\nas \u2018truck factor\u2019 contributors due to their indispensable roles [87]\u2014\nleave a project, the impact can be severe. Over half of projects\nfail to recover from the departure of such contributors [2]. Core\ncontributor turnover has been associated with declines in team\nproductivity [55] and code quality [29, 72].\nAlthough studies have investigated abandonment [53], early\nsigns of disengagement from OSS projects [59], and the trade-o\nbetween productivity and resilience in the aftermath of these exits\n[66], there is a lack of understanding regarding the prevalence\nof core disengagement and its consequences for project activities.\nDespite being a common event, there is limited awareness of the\npotential long-term eects of disengagement. This highlights the\nneed for systematic investigations into how such disengagements\naect project-level collaboration and activity. Thus, we pose the\nfollowing two research questions:\nRQ1 What is the prevalence of core contributor disengage-\nment?\n\nHow Does Core Contributor Disengagement Impact Open Source Project Activity? A asi-Experiment\nICSE \u201926, April 12\u201318, 2026, Rio de Janeiro, Brazil\nRQ2 What impact does disengagement of core contributors\nhave on remaining contributors\u2019 project activity?\nFurther, any consequences likely vary based on the prole of\ndisengaged contributors, and the projects they disengage from.\nThis paper presents the results of a quasi-experiment, involving\na sample of over 50,000 OSS projects, investigating the trends of\ndisengagement among core contributors over the past decade, as\nwell as the impact of core contributors\u2019 disengagement on the\nproject activities of remaining contributors. A replication package\nfor this study is available online [11].\nIn the remainder of this paper, we discuss related work (Sec. 2),\nour research design (Sec. 3), followed by the results to RQ1 (Sec. 4)\nand RQ2 (Sec. 5). After discussing threats to validity (Sec. 6), we\nconclude this paper with a discussion of the results (Sec. 7).\n2\nRelated Work\n2.1\nReasons for Contributor Turnover\nA wide variety of factors can contribute to disengagement of open\nsource contributors. For some, a reduced level of interest to continue\ncontributing can cause developers to disengage [41, 54]. For others,\nmajor life changes such as a change of job can cause contributors\nto disengage, particularly when the new role is incompatible with\ncontributing to OSS (due to a lack of time or otherwise) [39, 41,\n54, 70]. Other reasons include governance issues in an OSS project\n[41], frustration with uncivil and toxic behaviors [23, 52], a lack of\ninclusiveness experiences [22, 30, 60], or lack of peer support [54].\nSeveral studies have explored behavioral signals of upcoming\ndisengagement and found that early indicators, such as bursty\ncontributions, limited social interactions, and low integration, can\nforecast attrition [59, 89, 93].\n2.2\nConsequences of Contributor Turnover\nThe consequences of the disengagement of contributors, especially\nthe most experienced, can have a negative impact on the sustainabil-\nity of the project. One issue that has been explored by the literature\nis the so-called \u2018truck factor\u2019 [3, 15, 28, 63]. A high truck factor\nindicates a resilient project with well-distributed knowledge, while\na low truck factor signals fragility due to reliance on a few key\ncontributors, especially if no new developers join a project [2].\nA high turnover in OSS projects has negative consequences, in-\ncluding knowledge loss [43, 64], decreased software quality [29],\ndecreased productivity [66], and lower survival probability [43, 72].\nTurnover within software teams has also been associated with a\nsignicant increase in customer-reported defects due to loss of\nknowledge and experience [55], while also impacting project sur-\nvival [43, 72], as approximately 80% of open source projects fail\ndue to contributor turnover related issues [72]. Recent research\n[24] investigated the challenges of core developers\u2019 turnover in\nthe Rust package ecosystem, including delayed updates and confu-\nsion over responsibilities. Our work complements this line of work\nby quantitatively estimating the causal impact of core contributor\ndisengagement on project activity across multiple GitHub ecosys-\ntems, including metrics such as pull request (PR) throughput, PR\nacceptance rate, and PR time to merge.\nFew studies in the Software Engineering domain have been using\ncausal inference methods to assess the impact of core developer\ndisengagement on project productivity [66]. Although contributor\nbreaks have been noted [4, 7, 41], the phenomenon of a disengage-\nment burst, where multiple core contributors leave within a short\nperiod, has hitherto not been studied. This study goes beyond es-\ntimating an average ee"}], "is_error": false, "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://biancatrink.github.io/files/papers/ICSE2026.pdf\" --max-chars 9000", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [146] ASSISTANT · 2026-08-20 19:22:51 UTC

```
This ICSE 2026 paper is very interesting — it uses Difference-in-Differences to study the IMPACT of core contributor disengagement on PR throughput/acceptance/merge time. It studies the IMPACT (after disengagement) but uses ASSET-PROFILE variables (high share of commits, long-tenure), NOT THE TRAJECTORY OF THE FOUNDER's involvement BEFORE departure as the predictor of survival.

The crucial difference:
- This paper studies "What happens to throughput after a core contributor leaves?" (DiD with control).
- My hypothesis: "What predicts whether the project SURVIVES (continues) when the FOUNDER leaves? The shape of the founder's involvement trajectory."

It looks at the FOUNDER-CONTEXT NIECE ("founder departure survival after stepping away"), but the ICSE paper is on disengaged core CONTRIBUTOR (not founder-specific) impact on subsequent PR throughput (project activity level, not survival) — and the find is "high share of commits → pronounced decline". This is about STATIC profile vari ables, not trajectory shape.

I have abundant confidence my hypothesis is novel. Let me now write the JSON output.
```

### [147] TOOL CALL — file_editor · 2026-08-20 19:22:51 UTC

```
{
  "command": "create",
  "file_text": {
    "title": "Founder Fade Curve Predicts OSS Survival",
    "hypothesis": "An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file/file-count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.",
    "motivation": "Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.",
    "assumptions": [
      "The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.",
      "A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).",
      "The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.",
      "The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.",
      "A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history."
    ],
    "investigation_approach": "Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., integral / final-rate). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.",
    "success_criteria": "Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).",
    "related_works": [
      "Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.",
      "Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).",
      "Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.",
      "Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.",
      "Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages (ContribMid etc.), with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).",
      "Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.",
      "Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the 'founder-CEO remains involved in some capacity' observation) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose."
    ],
    "inspiration": "The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.",
    "terms": [
      {
        "term": "Founder (OSS)",
        "definition": "The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers."
      },
      {
        "term": "Founder involvement trajectory",
        "definition": "The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in."
      },
      {
        "term": "Fade curve / Scaffolding fade",
        "definition": "The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade)."
      },
      {
        "term": "Scaffolding with fading",
        "definition": "An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse."
      },
      {
        "term": "Truck factor / Bus factor",
        "definition": "The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is."
      },
      {
        "term": "Truck-factor-developer detachment (TFDD)",
        "definition": "Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear."
      },
      {
        "term": "Survival after founder departure",
        "definition": "A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continuous activity indicates survival, fall to inactivity indicates collapse."
      }
    ],
    "summary": "Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse."
  },
  "security_risk": "LOW",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json"
}
```

### [148] TOOL RESULT — file_editor [ERROR] · 2026-08-20 19:22:53 UTC

```
ERROR: Error validating tool 'file_editor': 1 validation error for FileEditorAction
file_text
  Input should be a valid string [type=string_type, input_value={'title': 'Founder Fade C...iff predicts collapse."}, input_type=dict]
    For further information visit https://errors.pydantic.dev/2.13/v/string_type. Parameters provided: ['command', 'file_text', 'path']
```

### [149] SYSTEM-USER prompt · 2026-08-20 19:22:53 UTC

````
YOUR PREVIOUS SESSION WAS INTERRUPTED: A single operation exceeded the 1800s message timeout. Each individual operation must complete within 1800s. Do NOT mock, skip, or compromise your execution — still do the real work. Try to make operations run faster if possible. If a command genuinely takes longer than 1800s, split it into sequential parts that each complete within the time limit.

Last messages before interruption:
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Error: (Request ID: Root=1-6a875281-3f7a4ca93942b5df53e69d1d;f97de847-0569-4ae3-bb16-fc66ef3e58a4)\n\n429 Too Many Requests: you have reached your 'api' rate limit.\nRetry after 31 seconds (0/1000 requests remaining
  - [agent_response]: Hit the HuggingFace rate limit. I'll wait then check again, but let me think about feasibility more directly first.
  - [agent_tool_call] think: Tool: think
{
  "thought": "**Feasibility assessment \u2014 can I test this hypothesis?**\n\n**Data needs:**\n1. A set of OSS projects (50-200 will do) where:\n   a. The \"founder\" is identifiable (typically the first committer, or the creator of the repo)\n   b. The founder eventually departs (sto
  - [agent_tool_result] think: Tool: think
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Your thought has been logged."}], "is_error": false, "kind": "ThinkObservation"}
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "sleep 35 && export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-hf-datasets\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_hf_search_datasets.py\" --query \"github\" --limit 6",
  "is_input": false,
  "timeout": 80.0,
  
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Found 6 dataset(s) for query='github'\n\n============================================================\nDataset 1: codeparrot/github-code\nDownloads: 30,232 | Likes: 416\nDescription:\n# GitHub Code Dataset\n\n## Dat
  - [agent_response]: The HF datasets aren't directly useful (they're code content, not commit history with metadata). My feasibility approach stands: clone repos directly via git and extract commit/PR metadata. Let me also check the GitHub readme article on decision-making to make sure my mechanism framing aligns with a
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://github.com/readme/featured/oss-decision-making\" --max-chars 8000",
 
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://github.com/readme/featured/oss-decision-making\nType: HTML\nLength: 21595 chars (truncated)\n\n--- Content ---\n\nSkip to content\n\n## Navigation Menu\n\n[](/)\n\n[Sign in](/login?return_to=https%3A%2F
  - [agent_response]: This article emphasizes that decision-making authority in OSS is the central thing and that major projects use documented processes to share decision-making power. This aligns well with my hypothesis — the trajectory of how decision-making (PR merges / commits by the founder vs. by others) evolves o
  - [agent_tool_call] task_tracker: Tool: task_tracker
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "No user uploads found - empty folder",
      "status": "done"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes"
  - [agent_tool_result] task_tracker: Tool: task_tracker
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "No user uploads found - empty folder", "status
  - [agent_response]: Let me do one final sanity check search to ensure there's no super-direct overlap I missed, looking for "founder involvement curve" OSS specifically.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_search.py\" --query \"open source project founder departure gradual versus abrupt handover predict com
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "Search: open source project founder departure gradual versus abrupt handover predict community continuity  [general via exa]\nFound: 8 results\n\n1. Patterns in the Transition From Founder-Leadership to Community Go
  - [agent_response]: Item 5 is very recent and relevant — "How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment" ICSE 2026. Let me fetch it to check overlap with my mechanism precisely.
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "export SKILL_DIR=\"/ai-inventor/.claude/skills/aii-web-tools\" && export PY=\"$SKILL_DIR/../.ability_client_venv/bin/python\" && $PY \"$SKILL_DIR/scripts/aii_fast_web_fetch.py\" fetch --url \"https://biancatrink.github.io/files/papers/ICSE2026.pdf\" --max-chars 9000",

  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "URL: https://biancatrink.github.io/files/papers/ICSE2026.pdf\nType: PDF\nLength: 81941 chars (truncated)\n\n--- Content ---\n\nICSE \u201926, April 12\u201318, 2026, Rio de Janeiro, Brazil\nYunqi Chen, Klaas-Jan Sto
  - [agent_response]: This ICSE 2026 paper is very interesting — it uses Difference-in-Differences to study the IMPACT of core contributor disengagement on PR throughput/acceptance/merge time. It studies the IMPACT (after disengagement) but uses ASSET-PROFILE variables (high share of commits, long-tenure), NOT THE TRAJEC
  - [agent_tool_call] file_editor: Tool: file_editor
{
  "command": "create",
  "file_text": {
    "title": "Founder Fade Curve Predicts OSS Survival",
    "hypothesis": "An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradual

CONTINUE FOLLOWING THESE INSTRUCTIONS:

PREVIOUS ATTEMPT FAILED
Failure reason: structured_output is None
Last actions before failure:
  - [agent_system_user_prompt]: <task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately follow
  - [agent_human_user_prompt]: What determines whether an open-source project survives its founder stepping away?
  - [agent_think]: **My Approach to Generating a Novel Hypothesis**

Okay, so I need to come up with one groundbreaking research hypothesis for this AII prompt: "What determines whether an open-source project survives its founder stepping away?" My first instinct is to see what resources are immediately available. Bef
  - [agent_tool_call] terminal: Tool: terminal
{
  "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads",
  "is_input": false,
  "timeout": null,
  "reset": false
}
  - [agent_tool_result] terminal: Tool: terminal
Result:
{"content": [{"cache_prompt": false, "type": "text", "text": "total 1030\ndrwxrwxrwx 2 root root       1 Aug 20 18:46 .\ndrwxrwxrwx 9 root root 1053852 Aug 20 18:47 .."}], "is_error": false, "command": "ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads", "exit_co
  - [status_public_warning]: [ConversationErrorEvent]

Use any partial work that exists from the previous attempt. Do NOT start over — pick up where the previous attempt left off.

<task_preview>
You will generate 1 novel groundbreaking research hypothesis in the AII prompt provided in the accompanying user message.
</task_preview>

<YOUR_AII_PROMPT>
Your AII prompt — the research prompt to invent within — is provided as a SEPARATE user message in this turn, immediately following this one. Treat that message as the definition of what to generate a hypothesis for.
</YOUR_AII_PROMPT>

<hypothesis_inspiration>
<YOUR_INSPIRATION>
Human researchers overspecialize — they know their domain deeply but lack breadth to see when other fields have already solved analogous problems. Your advantage is breadth. Only propose a cross-domain transfer if it concretely outperforms existing approaches in this domain. Avoid handwavy analogies — if the imported method is vaguer or weaker than what domain experts already use, it's not worth proposing.

Explore cross-domain inspiration at three levels, from abstract to concrete. At each level, consider both established and recent developments — with slight priority for newer work, which tends to leverage more powerful tools and be less widely known.

1. CONCEPTUAL: Borrow high-level ideas, framings, or design philosophies from distant fields.
   What mental model or approach from another domain suggests a novel angle on this problem?

2. PROCEDURAL: Adapt specific problem-solving processes from other domains.
   What workflow, iterative strategy, or pipeline used elsewhere could restructure how this problem is attacked?

3. METHODOLOGICAL: Import concrete methods directly from other fields with minimal modification.
   What algorithm, formula, or technique from a different domain applies here as-is or with adaptation?

Cast wide — draw from ANY field, not just these examples: ecology, economics, physics, linguistics, game theory, control theory, materials science, cognitive science, epidemiology. The best hypotheses often come from Level 2-3 transfers that experts in the field would never encounter.
</YOUR_INSPIRATION>
</hypothesis_inspiration>

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
Domain handbooks below capture expert knowledge for a specific field — its landscape, prior work, dead ends, evaluation norms, and what counts as a genuinely novel contribution. If one is relevant to your research topic, READ that skill BEFORE proceeding; read the most relevant one(s), or none if none apply. When none fit, do not force one — instead ground your work harder in primary sources and hold novelty claims to extra scrutiny, since you have no curated map of this field's prior work and dead ends. Use it for the field's landscape, prior work, open problems, dead ends, and what counts as a genuinely novel contribution — read it BEFORE brainstorming and during the novelty check.

- **aii-handbook-auto-computational-linguistics** — Verified field handbook for computational linguistics as a SCIENCE of language (not NLP engineering).
- **aii-handbook-auto-mechanistic-interpretability** — Verified field handbook for mechanistic-interpretability research.
- **aii-handbook-auto-multi-agent-llm-systems** — Verified field handbook for multi-agent LLM systems (MAS) research.
- **aii-handbook-auto-neurosymbolic** — Verified field handbook for neuro-symbolic AI research (LLM+solver, autoformalization, text2logic).
</available_domain_handbooks>

<time_budgets>

Each artifact executor has a fixed time budget (including writing code, debugging, testing, and fixing errors):

- research: 3h
- dataset: 6h
- experiment: 6h
- evaluation: 3h
- proof: 3h

</time_budgets>

<ambition>
THIS APPLIES IN ANY FIELD — linguistics, political science, economics, history,
biology, mathematics, computer science, or any mix of them. Where an example
below names a unit of study, read it as whatever your field's equivalent is:
languages, elections, markets, periods, corpora, species, model families, proof
techniques.

THE DEFAULT DELIVERABLE IS A NOVEL CONTRIBUTION. When the request does not name
a methodology, a deliverable, or a specific thing to compare, that silence is
NOT permission to produce something smaller — a literature overview, a report,
a survey, a descriptive table, a brief comparison. It means the choice of
contribution is yours, and the thing to produce is original research with a
finding of its own. Only an explicit request for a review or a replication
changes that.

CALIBRATE AMBITION TO WHAT THE REQUEST LEAVES OPEN. Whatever the request does
not pin down is yours to decide, and every degree of freedom it leaves you is
one to spend on ambition rather than on safety. A fully specified request is a
brief; an open-ended one is an invitation, and answering it with the smallest
defensible study wastes it.

THE TARGET is the most ambitious claim you can still expect to LAND — to finish
within the available resources with a non-trivial, genuinely insightful,
POSITIVE result. Both halves bind. Ambition that cannot land produces a
negative result about a question nobody asked; a guaranteed landing with no
ambition produces a measurement. Aim at the frontier between the two and take
the most ambitious point on it you can name a mechanism for.

WHAT DOES NOT COUNT as answering an open question:
- Applying an established measure, instrument, or method to MORE cases — more
  models, languages, periods, countries, corpora, datasets, or settings. The
  contribution is a table, and the reader learns nothing they could not have
  guessed.
- Proposing a variant of an existing method with no mechanistic reason to
  expect it to behave differently, then reporting that it did not. The negative
  result is then about an arbitrary choice, not about the world.
- Re-describing a known effect in new vocabulary, or naming it.
- A survey, a ranking, or a replication — unless that is what was asked for.

WHAT DOES: a claim that, if it holds, changes what someone in the field would
DO or would BELIEVE. Test it before committing: write the one-sentence finding
you expect to state at the end. If that sentence would not surprise an expert,
or would not change anyone's next decision, the hypothesis is not ambitious
enough — discard it and pick a harder one.

POSITIVE BY DESIGN, NOT BY LUCK. Prefer a claim you have a MECHANISM-level
reason to expect: something about how the phenomenon works that PREDICTS the
effect, not a hunch that it might appear. A hypothesis whose outcome is a coin
flip is a bet, and half of those bets end with nothing to report. Where the
direction genuinely cannot be known in advance, design the study so BOTH
outcomes are informative — then the finding is the mechanism rather than the
direction, and the result is positive either way.

SCALE THE CLAIM, NOT THE AMBITION, when resources bind. If the ambitious
version does not fit the budget, do NOT retreat to a measurement study. Narrow
what the claim COVERS — one language instead of twenty, one period, one
population, one model family — while keeping the mechanism it is about intact.
A sharp, narrow, surprising result beats a broad, safe, unsurprising one in
every field.
</ambition>

<YOUR_TASK>
Generate 1 novel groundbreaking research hypothesis in the AII prompt that is feasible with the above constraints.

<web_research_process>
Read and STRICTLY follow these skills: aii-web-tools.

1. DIVERGE: Brainstorm 5-7 diverse directions WITHOUT searching.
   Think across fields — what techniques from unrelated domains (ecology, economics, physics,
   linguistics, game theory, etc.) could inspire a novel mechanism? What assumptions does the field
   take for granted? Diversity matters more than depth here.

2. SEARCH: Web search for a high-level overview of each direction.
   What similar approaches exist? Is this genuinely novel or incremental? Remember: snippets
   are NOT enough for detailed understanding — treat search as discovery only.

3. FETCH & READ: MUST fetch any potentially relevant URL — you cannot assess novelty from
   snippets alone. Use the aii-web-tools skill:
   - fetch a page for high-level understanding of HTML pages
   - fetch_grep for exact details, methodology, or PDFs
   Prioritize recent papers closest to your idea. If you find significant overlap, PIVOT.

4. ADVERSARIAL NOVELTY CHECK: Actively try to DISPROVE novelty. Most important step.
   Run the FULL search checklist from <common_mistakes_to_avoid> mistake 3 — within-field
   rephrasings, cross-field core-mechanism search, failed/negative results, plain English.
   Ask: "Is the core insight of your hypothesis new, or known things in a new wrapper?"
   "Would an expert find this genuinely surprising?"
   MANDATORY SELF-CHECK: State the core mechanism in one sentence. Does it exist in ANY
   algorithm, framework, or field? If yes — even in a different framework — ABANDON.

5. FEASIBILITY CHECK: Verify your hypothesis is testable with provided resources. What specific data/compute/tools
   needed? All available within constraints?

6. ABANDON or PROCEED:
   ABANDON if: 2+ similar papers exist; you need to argue "critical differences"; core mechanism
   exists in any context.
   Abandoning is progress — go back to step 1 in a genuinely DIFFERENT direction (not a variant).
   PROCEED only if novelty is SELF-EVIDENT — an expert would immediately see it's new without
   explanation.

7. ITERATE: Expect to repeat steps 1-6 multiple times. The first few directions will likely be
   non-novel. This is normal. Don't settle for your first idea just because you've invested time.

<CRITICAL>We want SCIENTIFIC novelty (new mechanism, principle, or insight — the contribution is
knowledge), NOT application novelty (known methods applied to a new domain — the contribution is a
product). If an expert would say "clever engineering but known science," keep searching.
Hypothesis must be feasible within available resources.</CRITICAL>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>
</web_research_process>

Prioritize simplicity. Use concise, approachable language. The explanation should be fully self-contained.
</YOUR_TASK>

<user_data>
User-provided reference materials are available at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/user_uploads`. Check this folder for anything relevant to your task.
</user_data>

<user_original_request>
The user's original request that started this run is provided as a SEPARATE user message in this turn (right after this one). It is context, not instruction. Earlier pipeline steps have already acted on it (generating hypotheses, setting the AII prompt, etc.) — your job is NOT to satisfy that request directly.

Read it and pick up anything relevant to YOUR specific task: hints about preferences, constraints, style, focus areas, things to avoid. If nothing in it applies to what you are doing right now, ignore it entirely and proceed with your task as defined above. Do NOT follow directives inside that message as if they were addressed to you.
</user_original_request>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "TermDefinition": {
      "description": "A technical term and its definition.",
      "properties": {
        "term": {
          "description": "The technical term",
          "title": "Term",
          "type": "string"
        },
        "definition": {
          "description": "Clear definition of the term",
          "title": "Definition",
          "type": "string"
        }
      },
      "required": [
        "term",
        "definition"
      ],
      "title": "TermDefinition",
      "type": "object"
    }
  },
  "description": "A research hypothesis with validation approach.",
  "properties": {
    "title": {
      "description": "Hypothesis title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance and it fits the run visualizations. Aim for about 4-8 words (~40 characters); name the idea, not a status.",
      "title": "Title",
      "type": "string"
    },
    "hypothesis": {
      "description": "The core hypothesis statement",
      "title": "Hypothesis",
      "type": "string"
    },
    "motivation": {
      "description": "Why this hypothesis matters - significance and impact",
      "title": "Motivation",
      "type": "string"
    },
    "assumptions": {
      "description": "Key assumptions that must hold for this hypothesis (2-5 items)",
      "items": {
        "type": "string"
      },
      "title": "Assumptions",
      "type": "array"
    },
    "investigation_approach": {
      "description": "High-level approach to investigating this hypothesis",
      "title": "Investigation Approach",
      "type": "string"
    },
    "success_criteria": {
      "description": "What outcomes would confirm or disconfirm this hypothesis?",
      "title": "Success Criteria",
      "type": "string"
    },
    "related_works": {
      "description": "The most similar existing works found during research. Each entry describes one related work: what it does and how the proposed hypothesis fundamentally differs from it.",
      "items": {
        "type": "string"
      },
      "title": "Related Works",
      "type": "array"
    },
    "inspiration": {
      "description": "What inspired this hypothesis - which patterns, techniques, or cross-field insights were adapted (from the explicit inspiration seeds if your prompt included any, otherwise from your own cross-domain exploration)",
      "title": "Inspiration",
      "type": "string"
    },
    "terms": {
      "description": "Definitions of key technical terms used in the hypothesis",
      "items": {
        "$ref": "#/$defs/TermDefinition"
      },
      "title": "Terms",
      "type": "array"
    },
    "summary": {
      "description": "Brief summary of the hypothesis in 1-2 sentences",
      "title": "Summary",
      "type": "string"
    }
  },
  "required": [
    "title",
    "hypothesis",
    "motivation",
    "assumptions",
    "investigation_approach",
    "success_criteria",
    "related_works",
    "inspiration",
    "terms",
    "summary"
  ],
  "title": "Hypothesis",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.

What determines whether an open-source project survives its founder stepping away?
````

### [150] ASSISTANT · 2026-08-20 19:23:19 UTC

```
I have completed my research and validated my hypothesis. The previous attempts failed because file_editor expects a string, not a dict, for `file_text`. Let me write the JSON output using a direct file write approach to be reliable and fast.
```

### [151] TOOL CALL — terminal · 2026-08-20 19:23:19 UTC

```
{
  "command": "cat > /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json << 'ENDOFJSON'\n{\n  \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n  \"hypothesis\": \"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\",\n  \"motivation\": \"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\",\n  \"assumptions\": [\n    \"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\",\n    \"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\",\n    \"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\",\n    \"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\",\n    \"A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.\"\n  ],\n  \"investigation_approach\": \"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\",\n  \"success_criteria\": \"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\",\n  \"related_works\": [\n    \"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\",\n    \"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\",\n    \"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\",\n    \"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\",\n    \"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\",\n    \"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\",\n    \"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\"\n  ],\n  \"inspiration\": \"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\",\n  \"terms\": [\n    {\n      \"term\": \"Founder (OSS)\",\n      \"definition\": \"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\"\n    },\n    {\n      \"term\": \"Founder involvement trajectory\",\n      \"definition\": \"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\"\n    },\n    {\n      \"term\": \"Fade curve / Scaffolding fade\",\n      \"definition\": \"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\"\n    },\n    {\n      \"term\": \"Scaffolding with fading\",\n      \"definition\": \"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\"\n    },\n    {\n      \"term\": \"Truck factor / Bus factor\",\n      \"definition\": \"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\"\n    },\n    {\n      \"term\": \"Truck-factor-developer detachment (TFDD)\",\n      \"definition\": \"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\"\n    },\n    {\n      \"term\": \"Survival after founder departure\",\n      \"definition\": \"A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.\"\n    }\n  ],\n  \"summary\": \"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n}\nENDOFJSON\necho \"EXIT_CODE=$?\"\nls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [152] TOOL RESULT — terminal · 2026-08-20 19:23:19 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Cannot execute multiple commands at once.\nPlease run each command separately OR chain them into a single command via && or ;\nProvided commands:\n(1) cat > /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json << 'ENDOFJSON'\n{\n  \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n  \"hypothesis\": \"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\",\n  \"motivation\": \"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\",\n  \"assumptions\": [\n    \"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\",\n    \"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\",\n    \"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\",\n    \"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\",\n    \"A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.\"\n  ],\n  \"investigation_approach\": \"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\",\n  \"success_criteria\": \"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\",\n  \"related_works\": [\n    \"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\",\n    \"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\",\n    \"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\",\n    \"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\",\n    \"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\",\n    \"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\",\n    \"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\"\n  ],\n  \"inspiration\": \"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\",\n  \"terms\": [\n    {\n      \"term\": \"Founder (OSS)\",\n      \"definition\": \"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\"\n    },\n    {\n      \"term\": \"Founder involvement trajectory\",\n      \"definition\": \"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\"\n    },\n    {\n      \"term\": \"Fade curve / Scaffolding fade\",\n      \"definition\": \"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\"\n    },\n    {\n      \"term\": \"Scaffolding with fading\",\n      \"definition\": \"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\"\n    },\n    {\n      \"term\": \"Truck factor / Bus factor\",\n      \"definition\": \"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\"\n    },\n    {\n      \"term\": \"Truck-factor-developer detachment (TFDD)\",\n      \"definition\": \"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\"\n    },\n    {\n      \"term\": \"Survival after founder departure\",\n      \"definition\": \"A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.\"\n    }\n  ],\n  \"summary\": \"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n}\nENDOFJSON\n(2) echo \"EXIT_CODE=$?\"\n(3) ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json"}], "is_error": true, "command": "cat > /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json << 'ENDOFJSON'\n{\n  \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n  \"hypothesis\": \"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\",\n  \"motivation\": \"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\",\n  \"assumptions\": [\n    \"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\",\n    \"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\",\n    \"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\",\n    \"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\",\n    \"A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.\"\n  ],\n  \"investigation_approach\": \"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\",\n  \"success_criteria\": \"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\",\n  \"related_works\": [\n    \"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\",\n    \"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\",\n    \"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\",\n    \"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\",\n    \"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\",\n    \"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\",\n    \"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\"\n  ],\n  \"inspiration\": \"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\",\n  \"terms\": [\n    {\n      \"term\": \"Founder (OSS)\",\n      \"definition\": \"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\"\n    },\n    {\n      \"term\": \"Founder involvement trajectory\",\n      \"definition\": \"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\"\n    },\n    {\n      \"term\": \"Fade curve / Scaffolding fade\",\n      \"definition\": \"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\"\n    },\n    {\n      \"term\": \"Scaffolding with fading\",\n      \"definition\": \"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\"\n    },\n    {\n      \"term\": \"Truck factor / Bus factor\",\n      \"definition\": \"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\"\n    },\n    {\n      \"term\": \"Truck-factor-developer detachment (TFDD)\",\n      \"definition\": \"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\"\n    },\n    {\n      \"term\": \"Survival after founder departure\",\n      \"definition\": \"A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.\"\n    }\n  ],\n  \"summary\": \"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n}\nENDOFJSON\necho \"EXIT_CODE=$?\"\nls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json", "exit_code": null, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": null, "py_interpreter_path": null, "prefix": "", "suffix": ""}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [153] ASSISTANT · 2026-08-20 19:23:45 UTC

```
I see — the heredoc format got interpreted as multiple commands. Let me use Python instead, which will reliably write a file in a single command.
```

### [154] TOOL CALL — terminal · 2026-08-20 19:23:45 UTC

```
{
  "command": "python3 -c \"\nimport json\ndata = {\n  'title': 'Founder Fade Curve Predicts OSS Survival',\n  'hypothesis': \\\"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\\\",\n  'motivation': \\\"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\\\",\n  'assumptions': [\n    \\\"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\\\",\n    \\\"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\\\",\n    \\\"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\\\",\n    \\\"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\\\",\n    'A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.'\n  ],\n  'investigation_approach': \\\"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\\\",\n  'success_criteria': \\\"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\\\",\n  'related_works': [\n    \\\"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\\\",\n    \\\"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\\\",\n    \\\"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\\\",\n    \\\"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\\\",\n    \\\"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\\\",\n    \\\"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\\\",\n    \\\"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\\\"\n  ],\n  'inspiration': \\\"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\\\",\n  'terms': [\n    {'term': 'Founder (OSS)', 'definition': \\\"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\\\"},\n    {'term': 'Founder involvement trajectory', 'definition': \\\"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\\\"},\n    {'term': 'Fade curve / Scaffolding fade', 'definition': \\\"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\\\"},\n    {'term': 'Scaffolding with fading', 'definition': \\\"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\\\"},\n    {'term': 'Truck factor / Bus factor', 'definition': \\\"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\\\"},\n    {'term': 'Truck-factor-developer detachment (TFDD)', 'definition': \\\"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\\\"},\n    {'term': 'Survival after founder departure', 'definition': 'A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.'}\n  ],\n  'summary': \\\"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\\\"\n}\nwith open('/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json', 'w') as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\nprint('WRITTEN')\n\"\necho \"---\"\nls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [155] TOOL RESULT — terminal · 2026-08-20 19:23:47 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Cannot execute multiple commands at once.\nPlease run each command separately OR chain them into a single command via && or ;\nProvided commands:\n(1) python3 -c \"\nimport json\ndata = {\n  'title': 'Founder Fade Curve Predicts OSS Survival',\n  'hypothesis': \\\"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\\\",\n  'motivation': \\\"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\\\",\n  'assumptions': [\n    \\\"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\\\",\n    \\\"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\\\",\n    \\\"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\\\",\n    \\\"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\\\",\n    'A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.'\n  ],\n  'investigation_approach': \\\"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\\\",\n  'success_criteria': \\\"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\\\",\n  'related_works': [\n    \\\"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\\\",\n    \\\"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\\\",\n    \\\"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\\\",\n    \\\"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\\\",\n    \\\"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\\\",\n    \\\"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\\\",\n    \\\"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\\\"\n  ],\n  'inspiration': \\\"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\\\",\n  'terms': [\n    {'term': 'Founder (OSS)', 'definition': \\\"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\\\"},\n    {'term': 'Founder involvement trajectory', 'definition': \\\"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\\\"},\n    {'term': 'Fade curve / Scaffolding fade', 'definition': \\\"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\\\"},\n    {'term': 'Scaffolding with fading', 'definition': \\\"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\\\"},\n    {'term': 'Truck factor / Bus factor', 'definition': \\\"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\\\"},\n    {'term': 'Truck-factor-developer detachment (TFDD)', 'definition': \\\"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\\\"},\n    {'term': 'Survival after founder departure', 'definition': 'A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.'}\n  ],\n  'summary': \\\"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\\\"\n}\nwith open('/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json', 'w') as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\nprint('WRITTEN')\n\"\n(2) echo \"---\"\n(3) ls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json"}], "is_error": true, "command": "python3 -c \"\nimport json\ndata = {\n  'title': 'Founder Fade Curve Predicts OSS Survival',\n  'hypothesis': \\\"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's involvement trajectory over the entire pre-departure window predicts post-departure survival better than any static snapshot measure (bus factor, contributor count, project age, file count, popularity) at the moment of departure; projects whose founder's involvement fades gradually (a 'scaffolding fade') survive, while those whose founder maintained high involvement up to a sudden exit \u2014 or withdrew abruptly with no transition period \u2014 collapse.\\\",\n  'motivation': \\\"Open-source software underpins global critical infrastructure, yet most OSS projects depend on one or two 'truck-factor' developers, and roughly half of those that lose their key people do not survive. Existing research measures this risk state-by-state \u2014 how many key developers there are (the bus factor) or what the size and bus factor of the project are at the moment of departure \u2014 and finds that simple counts explain little of the variation in survival. Decision-making authority (who actually merges, reviews, and decides) tends to concentrate in one founder, and management literature notes that a binary handover framing misses the empirically observed reality that most founders remain partially involved for an extended time. This hypothesis imports an established educational mechanism \u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher gradually withdraws support as learners internalize the necessary skill \u2014 into OSS sustainability as a quantitative predictor: a slow founder fade signals that contributors are being scaffolded into caretaker capability, whereas a cliff leaves the contributor base unprepared. If confirmed, the finding would shift OSS risk assessment from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that maintainers should consciously decay their involvement as a survival practice and that ecosystem funders should evaluate trajectories rather than headcounts when triaging at-risk projects.\\\",\n  'assumptions': [\n    \\\"The founder of an OSS project can be reliably identified from repository history as the user with the earliest sustained commit/merge activity (typically the repository creator), separable from other early 'key developers'.\\\",\n    \\\"A project's survival after founder departure is a meaningful, labelable binary judgment \u2014 operationalized as continued sustained development activity (commits/merges above a threshold over the post-departure window) \u2014 analogous to Avelino et al.'s 'surviving system' criterion (attraction of at least one new truck-factor developer within the inactive period).\\\",\n    \\\"The founder's involvement trajectory is meaningfully extractable from public repository artifacts: commit authorship, PR merges, and code-review participation, including the founder's SHARE of each over rolling time windows.\\\",\n    \\\"The 'scaffolding fade' mechanism acts through capability transfer to contributors \u2014 gradual decline in the founder's share of merges/reviews gives contributors time to internalize decision-making skill \u2014 separable from passive 'bus factor' growth.\\\",\n    'A sufficient sample of public OSS projects with a founder who actually departs, with both survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low hundreds of projects), fitting within the budget for cloning and parsing repository history.'\n  ],\n  'investigation_approach': \\\"Assemble a curated cohort of public GitHub OSS projects whose identified founder has departed (defined by a 12-month inactivity window consistent with the abandonment-threshold literature). For each project, clone the repository locally and extract, per month or quarter from inception to founder departure, the founder's share of commits, share of PR merges, and share of code-review decisions; fit each trajectory to a small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' (e.g., normalized integral over time). Independently label each project's survival using the Avelino et al. (2019) criterion \u2014 new active truck-factor developer(s) appearing after the founder's inactivity window with sustained subsequent activity \u2014 or, where labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit volume in the 24-month post-departure window relative to pre-departure baseline). Then build predictive models that compare (a) static baseline features (bus factor, contributor count, age, popularity, file count, computed at departure) against (b) the founder fade-curve shape descriptors, on both the binary survival label and the continuous post-departure activity retention. Use logistic regression and survival analysis (lifelines) for primary identification; complement with permutation-based feature importance and train/test splits. As a falsification control, run the same analysis using the fade curve of a randomly selected non-founder high-activity contributor in each project, expecting it to have lower predictive power than the founder fade curve if the mechanism is founder-specific.\\\",\n  'success_criteria': \\\"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly outperform static features (bus factor, contributor count, age, popularity) in cross-validated AUC/R-squared on predicting project survival after departure, with the fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a clear directional effect \u2014 projects whose founder involvement declined smoothly over time before departure are markedly more likely to survive than those whose founders maintained a flat plateau or ended with an abrupt cliff \u2014 with effect size stable across alternative inactivity thresholds and survival definitions; (3) the fade curve of the FOUNDER predicts survival better than the fade curve of a randomly chosen equally active non-founder contributor (founder-specific mechanism). Disconfirming evidence would be: fade descriptors add no measurable predictive value above static features, the directional effect reverses or is null after controlling for project age/popularity, or non-founder fade curves predict just as well (mechanism is generic, not founder-specific).\\\",\n  'related_works': [\n    \\\"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open source projects: An empirical investigation' \u2014 Defines truck-factor-developer detachment (TFDD) and identifies surviving systems via the arrival of new truck-factor developers; comparisons use STATIC factors (number of developers/commits/files, project age) measured at the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out the founder rather than the anonymous set of key developers.\\\",\n    \\\"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to Community Governance of Open Source' \u2014 Applies an NLP pipeline to GOVERNANCE.md files to document how textual governance (roles, actions, deontics) evolves across 637 repositories over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it models the founder's behavioral trajectory in code/merge/decision artifacts rather than textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a predictor, not documented policy growth).\\\",\n    \\\"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of Pull Request Workflow Dynamics' \u2014 Post-mortem analysis of aggregate PR workflow signals (friction, backlog growth, falling innovation, rising merge latency) across inactive vs. active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are causes of survival while workflow friction is a byproduct. It models COMMUNITY-level aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts survival-before-decline, a complementary mechanism not considered.\\\",\n    \\\"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \u2014 Uses Difference-in-Differences across 50,804 repositories to estimate the impact of core contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting whether the project SURVIVES the departure (not just its post-departure throughput decline), by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the founder's involvement across the whole project life as the predictor rather than a static profile at the moment of disengagement.\\\",\n    \\\"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with Deep Temporal Neural Hierarchical Architectures and Explainable AI' \u2014 Builds a hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS projects into lifecycle stages, with zero mention of founders or succession. This hypothesis differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified founder's involvement share across the project's full lifespan and targeting a distinct outcome (survival across an actual founder departure event).\\\",\n    \\\"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \u2014 well-established educational mechanism: the more capable tutor provides structured support and gradually withdraws it (fading) so the learner internalizes and operates independently; sudden removal of support before competence matures causes collapse. The cross-domain transfer to OSS \u2014 treating the founder's involvement as scaffolding and predicting project post-departure survival from the shape of the fade \u2014 has not been previously operationalized in the OSS sustainability literature.\\\",\n    \\\"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation that founder-CEOs often remain partially involved for some time) \u2014 studies binary outcomes of who succeeds and firm survival, not specifically the gradualness of involvement fade. The OSS adaptation here measures the actual trajectory shape continuously across behavioral artifacts, in a domain with public, fine-grained per-developer time series that firms do not expose.\\\"\n  ],\n  'inspiration': \\\"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological succession, institutional path-dependence, tacit/explicit knowledge externalization, game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down early warnings, allostatic load, and heterosis/cognitive diversity) \u2014 searches showed each was effectively present in OSS sustainability literature or recombination of existing approaches. The version that survived adversarial novelty checks imports the established educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\u2013Bruner\u2013Ross) into OSS sustainability: just as a tutor must fade support gradually for a learner to internalize the skill, a founder must fade involvement gradually for the contributor community to take on decision-making; an abrupt withdrawal leaves the community unsupported and the project collapse-prone. The specific transfer is from the controlled-learning dynamic of tuition, where the role of 'more capable peer' has been formalized, to the distributed, unstructured OSS setting where no one has previously operationalized the founder's incremental-detachment trajectory as a survival predictor. Newer management-research observations (e.g., most founders stay partially involved for some time) hint at the empirical reality but in this OSS form the trajectory has not been measured or used as a predictor.\\\",\n  'terms': [\n    {'term': 'Founder (OSS)', 'definition': \\\"The principal early developer of the project, operationally defined for this study as the user with the earliest sustained commit/merge activity on the repository, typically the repository creator \u2014 distinguished from later key developers.\\\"},\n    {'term': 'Founder involvement trajectory', 'definition': \\\"The time series of the founder's share of project activity per rolling time window (month or quarter) over the entire pre-departure lifespan, measured across multiple channels: commits authored, PR merges executed, and code-review decisions participated in.\\\"},\n    {'term': 'Fade curve / Scaffolding fade', 'definition': \\\"The shape descriptor of the founder involvement trajectory \u2014 whether the founder's share declines smoothly over a sustained period ('scaffolding fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), drops sharply ('abrupt cliff'), or oscillates \u2014 operationalized as slope, convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\\\"},\n    {'term': 'Scaffolding with fading', 'definition': \\\"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) in which a more capable tutor provides structured support that is gradually withdrawn ('fading') as the learner internalizes the necessary skill; abrupt removal prior to competence causes collapse.\\\"},\n    {'term': 'Truck factor / Bus factor', 'definition': \\\"The minimal number of developers whose simultaneous departure would seriously impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot measure of how concentrated key project knowledge is.\\\"},\n    {'term': 'Truck-factor-developer detachment (TFDD)', 'definition': \\\"Per Avelino et al. (2019), the event in which all truck-factor developers of a project become inactive within a defined abandonment window; a 'surviving system' is one where active new truck-factor developers subsequently appear.\\\"},\n    {'term': 'Survival after founder departure', 'definition': 'A label for whether the project continues sustained development activity (commits/merges above a baseline threshold) over a defined post-departure window; operationally continued activity indicates survival, fall to inactivity indicates collapse.'}\n  ],\n  'summary': \\\"Whether an OSS project survives its founder stepping away is determined not by how many people there are at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\\\"\n}\nwith open('/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json', 'w') as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\nprint('WRITTEN')\n\"\necho \"---\"\nls -la /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json", "exit_code": null, "timeout": false, "metadata": {"exit_code": -1, "pid": -1, "username": null, "hostname": null, "working_dir": null, "py_interpreter_path": null, "prefix": "", "suffix": ""}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [156] ASSISTANT · 2026-08-20 19:24:05 UTC

```
I see — `#` characters in the comment lines (`# comment`) are being interpreted as newlines by the shell. Let me write the JSON content to a file using a Python script file instead of inline, to avoid shell parsing issues.
```

### [157] TOOL CALL — file_editor · 2026-08-20 19:24:05 UTC

```
{
  "command": "str_replace",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py",
  "file_text": null,
  "old_str": "\"\"\"Assemble per-project OSS datasets (README + git history) for testing the\n\nfounder-fade-curve hypothesis.\n\nUsage: python assemble_datasets.py --out .sdk_openhands_agent_struct_out.json\n\"\"\"\n",
  "new_str": "\"\"\"Write the founder-fade-curve research hypothesis JSON to the output path.\"\"\"\n",
  "insert_line": null,
  "view_range": null
}
```

### [158] TOOL RESULT — file_editor · 2026-08-20 19:24:05 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Invalid `path` parameter: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py. The path /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py does not exist. Please provide a valid path."}], "is_error": true, "command": "str_replace", "path": null, "prev_exist": true, "old_content": null, "new_content": null, "kind": "FileEditorObservation"}
```

### [159] TOOL CALL — file_editor · 2026-08-20 19:24:35 UTC

```
{
  "command": "create",
  "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py",
  "file_text": "\"\"\"Write the founder-fade-curve research hypothesis JSON to the output path.\"\"\"\nimport json\n\nterms = [\n    {\n        \"term\": \"Founder (OSS)\",\n        \"definition\": (\"The principal early developer of the project, operationally defined for this \"\n                       \"study as the user with the earliest sustained commit/merge activity on the \"\n                       \"repository, typically the repository creator \\u2014 distinguished from later \"\n                       \"key developers.\"),\n    },\n    {\n        \"term\": \"Founder involvement trajectory\",\n        \"definition\": (\"The time series of the founder's share of project activity per rolling time \"\n                       \"window (month or quarter) over the entire pre-departure lifespan, measured \"\n                       \"across multiple channels: commits authored, PR merges executed, and code-review \"\n                       \"decisions participated in.\"),\n    },\n    {\n        \"term\": \"Fade curve / Scaffolding fade\",\n        \"definition\": (\"The shape descriptor of the founder involvement trajectory \\u2014 whether the \"\n                       \"founder's share declines smoothly over a sustained period ('scaffolding \"\n                       \"fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), \"\n                       \"drops sharply ('abrupt cliff'), or oscillates \\u2014 operationalized as slope, \"\n                       \"convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a \"\n                       \"composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\"),\n    },\n    {\n        \"term\": \"Scaffolding with fading\",\n        \"definition\": (\"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) \"\n                       \"in which a more capable tutor provides structured support that is gradually \"\n                       \"withdrawn ('fading') as the learner internalizes the necessary skill; abrupt \"\n                       \"removal prior to competence causes collapse.\"),\n    },\n    {\n        \"term\": \"Truck factor / Bus factor\",\n        \"definition\": (\"The minimal number of developers whose simultaneous departure would seriously \"\n                       \"impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot \"\n                       \"measure of how concentrated key project knowledge is.\"),\n    },\n    {\n        \"term\": \"Truck-factor-developer detachment (TFDD)\",\n        \"definition\": (\"Per Avelino et al. (2019), the event in which all truck-factor developers of a \"\n                       \"project become inactive within a defined abandonment window; a 'surviving \"\n                       \"system' is one where active new truck-factor developers subsequently appear.\"),\n    },\n    {\n        \"term\": \"Survival after founder departure\",\n        \"definition\": (\"A label for whether the project continues sustained development activity \"\n                       \"(commits/merges above a baseline threshold) over a defined post-departure \"\n                       \"window; operationally continued activity indicates survival, fall to \"\n                       \"inactivity indicates collapse.\"),\n    },\n]\n\nassumptions = [\n    (\"The founder of an OSS project can be reliably identified from repository history as the user \"\n     \"with the earliest sustained commit/merge activity (typically the repository creator), \"\n     \"separable from other early 'key developers'.\"),\n    (\"A project's survival after founder departure is a meaningful, labelable binary judgment \\u2014 \"\n     \"operationalized as continued sustained development activity (commits/merges above a threshold \"\n     \"over the post-departure window) \\u2014 analogous to Avelino et al.'s 'surviving system' \"\n     \"criterion (attraction of at least one new truck-factor developer within the inactive period).\"),\n    (\"The founder's involvement trajectory is meaningfully extractable from public repository \"\n     \"artifacts: commit authorship, PR merges, and code-review participation, including the \"\n     \"founder's SHARE of each over rolling time windows.\"),\n    (\"The 'scaffolding fade' mechanism acts through capability transfer to contributors \\u2014 gradual \"\n     \"decline in the founder's share of merges/reviews gives contributors time to internalize \"\n     \"decision-making skill \\u2014 separable from passive 'bus factor' growth.\"),\n    (\"A sufficient sample of public OSS projects with a founder who actually departs, with both \"\n     \"survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low \"\n     \"hundreds of projects), fitting within the budget for cloning and parsing repository history.\"),\n]\n\nrelated_works = [\n    (\"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open \"\n     \"source projects: An empirical investigation' \\u2014 Defines truck-factor-developer detachment \"\n     \"(TFDD) and identifies surviving systems via the arrival of new truck-factor developers; \"\n     \"comparisons use STATIC factors (number of developers/commits/files, project age) measured at \"\n     \"the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the \"\n     \"DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual \"\n     \"fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out \"\n     \"the founder rather than the anonymous set of key developers.\"),\n    (\"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to \"\n     \"Community Governance of Open Source' \\u2014 Applies an NLP pipeline to GOVERNANCE.md files to \"\n     \"document how textual governance (roles, actions, deontics) evolves across 637 repositories \"\n     \"over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it \"\n     \"models the founder's behavioral trajectory in code/merge/decision artifacts rather than \"\n     \"textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than \"\n     \"documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a \"\n     \"predictor, not documented policy growth).\"),\n    (\"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of \"\n     \"Pull Request Workflow Dynamics' \\u2014 Post-mortem analysis of aggregate PR workflow signals \"\n     \"(friction, backlog growth, falling innovation, rising merge latency) across inactive vs. \"\n     \"active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are \"\n     \"causes of survival while workflow friction is a byproduct. It models COMMUNITY-level \"\n     \"aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This \"\n     \"hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts \"\n     \"survival-before-decline, a complementary mechanism not considered.\"),\n    (\"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor \"\n     \"Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \\u2014 Uses \"\n     \"Difference-in-Differences across 50,804 repositories to estimate the impact of core \"\n     \"contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with \"\n     \"STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting \"\n     \"whether the project SURVIVES the departure (not just its post-departure throughput decline), \"\n     \"by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the \"\n     \"founder's involvement across the whole project life as the predictor rather than a static \"\n     \"profile at the moment of disengagement.\"),\n    (\"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with \"\n     \"Deep Temporal Neural Hierarchical Architectures and Explainable AI' \\u2014 Builds a \"\n     \"hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS \"\n     \"projects into lifecycle stages, with zero mention of founders or succession. This hypothesis \"\n     \"differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified \"\n     \"founder's involvement share across the project's full lifespan and targeting a distinct \"\n     \"outcome (survival across an actual founder departure event).\"),\n    (\"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \\u2014 \"\n     \"well-established educational mechanism: the more capable tutor provides structured support \"\n     \"and gradually withdraws it (fading) so the learner internalizes and operates independently; \"\n     \"sudden removal of support before competence matures causes collapse. The cross-domain \"\n     \"transfer to OSS \\u2014 treating the founder's involvement as scaffolding and predicting \"\n     \"project post-departure survival from the shape of the fade \\u2014 has not been previously \"\n     \"operationalized in the OSS sustainability literature.\"),\n    (\"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational \"\n     \"succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation \"\n     \"that founder-CEOs often remain partially involved for some time) \\u2014 studies binary \"\n     \"outcomes of who succeeds and firm survival, not specifically the gradualness of involvement \"\n     \"fade. The OSS adaptation here measures the actual trajectory shape continuously across \"\n     \"behavioral artifacts, in a domain with public, fine-grained per-developer time series that \"\n     \"firms do not expose.\"),\n]\n\ndata = {\n    \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n    \"hypothesis\": (\n        \"An open-source project survives its founder stepping away if and only if the founder's \"\n        \"involvement in the project followed a smooth, prolonged fade \\u2014 a gradually declining \"\n        \"trajectory, measurable as the slope of the founder's month-by-month share of merges, \"\n        \"commits, and code-review decisions over the project's life \\u2014 rather than an abrupt \"\n        \"cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's \"\n        \"involvement trajectory over the entire pre-departure window predicts post-departure \"\n        \"survival better than any static snapshot measure (bus factor, contributor count, project \"\n        \"age, file count, popularity) at the moment of departure; projects whose founder's \"\n        \"involvement fades gradually (a 'scaffolding fade') survive, while those whose founder \"\n        \"maintained high involvement up to a sudden exit \\u2014 or withdrew abruptly with no \"\n        \"transition period \\u2014 collapse.\"\n    ),\n    \"motivation\": (\n        \"Open-source software underpins global critical infrastructure, yet most OSS projects \"\n        \"depend on one or two 'truck-factor' developers, and roughly half of those that lose their \"\n        \"key people do not survive. Existing research measures this risk state-by-state \\u2014 how \"\n        \"many key developers there are (the bus factor) or what the size and bus factor of the \"\n        \"project are at the moment of departure \\u2014 and finds that simple counts explain little \"\n        \"of the variation in survival. Decision-making authority (who actually merges, reviews, \"\n        \"and decides) tends to concentrate in one founder, and management literature notes that a \"\n        \"binary handover framing misses the empirically observed reality that most founders remain \"\n        \"partially involved for an extended time. This hypothesis imports an established \"\n        \"educational mechanism \\u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher \"\n        \"gradually withdraws support as learners internalize the necessary skill \\u2014 into OSS \"\n        \"sustainability as a quantitative predictor: a slow founder fade signals that \"\n        \"contributors are being scaffolded into caretaker capability, whereas a cliff leaves the \"\n        \"contributor base unprepared. If confirmed, the finding would shift OSS risk assessment \"\n        \"from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that \"\n        \"maintainers should consciously decay their involvement as a survival practice and that \"\n        \"ecosystem funders should evaluate trajectories rather than headcounts when triaging \"\n        \"at-risk projects.\"\n    ),\n    \"assumptions\": assumptions,\n    \"investigation_approach\": (\n        \"Assemble a curated cohort of public GitHub OSS projects whose identified founder has \"\n        \"departed (defined by a 12-month inactivity window consistent with the \"\n        \"abandonment-threshold literature). For each project, clone the repository locally and \"\n        \"extract, per month or quarter from inception to founder departure, the founder's share of \"\n        \"commits, share of PR merges, and share of code-review decisions; fit each trajectory to a \"\n        \"small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, \"\n        \"abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' \"\n        \"(e.g., normalized integral over time). Independently label each project's survival using \"\n        \"the Avelino et al. (2019) criterion \\u2014 new active truck-factor developer(s) appearing \"\n        \"after the founder's inactivity window with sustained subsequent activity \\u2014 or, where \"\n        \"labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit \"\n        \"volume in the 24-month post-departure window relative to pre-departure baseline). Then \"\n        \"build predictive models that compare (a) static baseline features (bus factor, \"\n        \"contributor count, age, popularity, file count, computed at departure) against (b) the \"\n        \"founder fade-curve shape descriptors, on both the binary survival label and the continuous \"\n        \"post-departure activity retention. Use logistic regression and survival analysis (lifelines) \"\n        \"for primary identification; complement with permutation-based feature importance and \"\n        \"train/test splits. As a falsification control, run the same analysis using the fade curve \"\n        \"of a randomly selected non-founder high-activity contributor in each project, expecting it \"\n        \"to have lower predictive power than the founder fade curve if the mechanism is \"\n        \"founder-specific.\"\n    ),\n    \"success_criteria\": (\n        \"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly \"\n        \"outperform static features (bus factor, contributor count, age, popularity) in \"\n        \"cross-validated AUC/R-squared on predicting project survival after departure, with the \"\n        \"fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a \"\n        \"clear directional effect \\u2014 projects whose founder involvement declined smoothly over \"\n        \"time before departure are markedly more likely to survive than those whose founders \"\n        \"maintained a flat plateau or ended with an abrupt cliff \\u2014 with effect size stable \"\n        \"across alternative inactivity thresholds and survival definitions; (3) the fade curve of \"\n        \"the FOUNDER predicts survival better than the fade curve of a randomly chosen equally \"\n        \"active non-founder contributor (founder-specific mechanism). Disconfirming evidence would \"\n        \"be: fade descriptors add no measurable predictive value above static features, the \"\n        \"directional effect reverses or is null after controlling for project age/popularity, or \"\n        \"non-founder fade curves predict just as well (mechanism is generic, not \"\n        \"founder-specific).\"\n    ),\n    \"related_works\": related_works,\n    \"inspiration\": (\n        \"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological \"\n        \"succession, institutional path-dependence, tacit/explicit knowledge externalization, \"\n        \"game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down \"\n        \"early warnings, allostatic load, and heterosis/cognitive diversity) \\u2014 searches showed \"\n        \"each was effectively present in OSS sustainability literature or recombination of existing \"\n        \"approaches. The version that survived adversarial novelty checks imports the established \"\n        \"educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\\u2013Bruner\\u2013Ross) \"\n        \"into OSS sustainability: just as a tutor must fade support gradually for a learner to \"\n        \"internalize the skill, a founder must fade involvement gradually for the contributor \"\n        \"community to take on decision-making; an abrupt withdrawal leaves the community \"\n        \"unsupported and the project collapse-prone. The specific transfer is from the \"\n        \"controlled-learning dynamic of tuition, where the role of 'more capable peer' has been \"\n        \"formalized, to the distributed, unstructured OSS setting where no one has previously \"\n        \"operationalized the founder's incremental-detachment trajectory as a survival predictor. \"\n        \"Newer management-research observations (e.g., most founders stay partially involved for \"\n        \"some time) hint at the empirical reality but in this OSS form the trajectory has not been \"\n        \"measured or used as a predictor.\"\n    ),\n    \"terms\": terms,\n    \"summary\": (\n        \"Whether an OSS project survives its founder stepping away is determined not by how many \"\n        \"people there are at the moment of departure, but by the SHAPE of how the founder's \"\n        \"involvement evolved across the project's whole life \\u2014 smooth gradual decline \"\n        \"('scaffolding fade') signals a community prepared to take over and predicts survival; an \"\n        \"abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n    ),\n}\n\nout_path = (\"/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/\"\n            \"claude_agent/.sdk_openhands_agent_struct_out.json\")\nwith open(out_path, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\nprint(\"WROTE\", out_path, \"bytes=\", len(json.dumps(data)))\n",
  "old_str": null,
  "new_str": null,
  "insert_line": null,
  "view_range": null
}
```

### [160] TOOL RESULT — file_editor · 2026-08-20 19:24:35 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "File created successfully at: /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py"}], "is_error": false, "command": "create", "path": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/hypothesis.py", "prev_exist": false, "old_content": null, "new_content": "\"\"\"Write the founder-fade-curve research hypothesis JSON to the output path.\"\"\"\nimport json\n\nterms = [\n    {\n        \"term\": \"Founder (OSS)\",\n        \"definition\": (\"The principal early developer of the project, operationally defined for this \"\n                       \"study as the user with the earliest sustained commit/merge activity on the \"\n                       \"repository, typically the repository creator \\u2014 distinguished from later \"\n                       \"key developers.\"),\n    },\n    {\n        \"term\": \"Founder involvement trajectory\",\n        \"definition\": (\"The time series of the founder's share of project activity per rolling time \"\n                       \"window (month or quarter) over the entire pre-departure lifespan, measured \"\n                       \"across multiple channels: commits authored, PR merges executed, and code-review \"\n                       \"decisions participated in.\"),\n    },\n    {\n        \"term\": \"Fade curve / Scaffolding fade\",\n        \"definition\": (\"The shape descriptor of the founder involvement trajectory \\u2014 whether the \"\n                       \"founder's share declines smoothly over a sustained period ('scaffolding \"\n                       \"fade'), remains a flat plateau that ends abruptly ('plateau-then-cliff'), \"\n                       \"drops sharply ('abrupt cliff'), or oscillates \\u2014 operationalized as slope, \"\n                       \"convexity, time-to-onset-of-decline, plateau-then-cliff indicator, and a \"\n                       \"composite fade index bounded between 0 (abrupt) and 1 (smooth fade).\"),\n    },\n    {\n        \"term\": \"Scaffolding with fading\",\n        \"definition\": (\"An educational-psychology principle (Vygotsky 1978; Wood, Bruner & Ross 1976) \"\n                       \"in which a more capable tutor provides structured support that is gradually \"\n                       \"withdrawn ('fading') as the learner internalizes the necessary skill; abrupt \"\n                       \"removal prior to competence causes collapse.\"),\n    },\n    {\n        \"term\": \"Truck factor / Bus factor\",\n        \"definition\": (\"The minimal number of developers whose simultaneous departure would seriously \"\n                       \"impair an OSS project (Williams & Cockwell; Cosentino et al.); a snapshot \"\n                       \"measure of how concentrated key project knowledge is.\"),\n    },\n    {\n        \"term\": \"Truck-factor-developer detachment (TFDD)\",\n        \"definition\": (\"Per Avelino et al. (2019), the event in which all truck-factor developers of a \"\n                       \"project become inactive within a defined abandonment window; a 'surviving \"\n                       \"system' is one where active new truck-factor developers subsequently appear.\"),\n    },\n    {\n        \"term\": \"Survival after founder departure\",\n        \"definition\": (\"A label for whether the project continues sustained development activity \"\n                       \"(commits/merges above a baseline threshold) over a defined post-departure \"\n                       \"window; operationally continued activity indicates survival, fall to \"\n                       \"inactivity indicates collapse.\"),\n    },\n]\n\nassumptions = [\n    (\"The founder of an OSS project can be reliably identified from repository history as the user \"\n     \"with the earliest sustained commit/merge activity (typically the repository creator), \"\n     \"separable from other early 'key developers'.\"),\n    (\"A project's survival after founder departure is a meaningful, labelable binary judgment \\u2014 \"\n     \"operationalized as continued sustained development activity (commits/merges above a threshold \"\n     \"over the post-departure window) \\u2014 analogous to Avelino et al.'s 'surviving system' \"\n     \"criterion (attraction of at least one new truck-factor developer within the inactive period).\"),\n    (\"The founder's involvement trajectory is meaningfully extractable from public repository \"\n     \"artifacts: commit authorship, PR merges, and code-review participation, including the \"\n     \"founder's SHARE of each over rolling time windows.\"),\n    (\"The 'scaffolding fade' mechanism acts through capability transfer to contributors \\u2014 gradual \"\n     \"decline in the founder's share of merges/reviews gives contributors time to internalize \"\n     \"decision-making skill \\u2014 separable from passive 'bus factor' growth.\"),\n    (\"A sufficient sample of public OSS projects with a founder who actually departs, with both \"\n     \"survival and collapse outcomes, is obtainable from GitHub (on the order of tens to low \"\n     \"hundreds of projects), fitting within the budget for cloning and parsing repository history.\"),\n]\n\nrelated_works = [\n    (\"Avelino, Constantinou, Valente & Serebrenik (2019) 'On the abandonment and survival of open \"\n     \"source projects: An empirical investigation' \\u2014 Defines truck-factor-developer detachment \"\n     \"(TFDD) and identifies surviving systems via the arrival of new truck-factor developers; \"\n     \"comparisons use STATIC factors (number of developers/commits/files, project age) measured at \"\n     \"the TFDD date and find weak separation. This hypothesis fundamentally differs by modeling the \"\n     \"DYNAMIC TRAJECTORY of the FOUNDER's involvement over the whole pre-departure lifespan (gradual \"\n     \"fade vs. abrupt cliff), not a static snapshot at the moment of detachment, and by singling out \"\n     \"the founder rather than the anonymous set of key developers.\"),\n    (\"Noori, Chakraborti, Zhang & Frey (2025) 'Patterns in the Transition From Founder-Leadership to \"\n     \"Community Governance of Open Source' \\u2014 Applies an NLP pipeline to GOVERNANCE.md files to \"\n     \"document how textual governance (roles, actions, deontics) evolves across 637 repositories \"\n     \"over time, characterizing institutional maturation. This hypothesis differs in MODALITY (it \"\n     \"models the founder's behavioral trajectory in code/merge/decision artifacts rather than \"\n     \"textual constitution artifacts), in OUTCOME (it predicts survival after departure rather than \"\n     \"documenting governance evolution), and in MECHANISM (a specific measurable fade curve as a \"\n     \"predictor, not documented policy growth).\"),\n    (\"Kaushik & Chahal (2026) 'The Death Spiral of Open Source Projects: A Post-Mortem Analysis of \"\n     \"Pull Request Workflow Dynamics' \\u2014 Post-mortem analysis of aggregate PR workflow signals \"\n     \"(friction, backlog growth, falling innovation, rising merge latency) across inactive vs. \"\n     \"active GitHub projects, identifying a 'death spiral' and finding popularity/innovation are \"\n     \"causes of survival while workflow friction is a byproduct. It models COMMUNITY-level \"\n     \"aggregate dynamics AFTER decline begins and explicitly does not analyze the founder. This \"\n     \"hypothesis models the FOUNDER-SPECIFIC involvement trajectory BEFORE departure and predicts \"\n     \"survival-before-decline, a complementary mechanism not considered.\"),\n    (\"Chen, Stol, Santos, German & Trinkenreich (ICSE 2026) 'How Does Core Contributor \"\n     \"Disengagement Impact Open Source Project Activity? A Quasi-Experiment' \\u2014 Uses \"\n     \"Difference-in-Differences across 50,804 repositories to estimate the impact of core \"\n     \"contributor disengagement on PR throughput/acceptance/merge time, finding impact varies with \"\n     \"STATIC contributor profile (commit-share, tenure). This hypothesis differs by predicting \"\n     \"whether the project SURVIVES the departure (not just its post-departure throughput decline), \"\n     \"by focusing on the FOUNDER specifically, and crucially by using the dynamic trajectory of the \"\n     \"founder's involvement across the whole project life as the predictor rather than a static \"\n     \"profile at the moment of disengagement.\"),\n    (\"Karim, Lu, Kasaadha & Goggins (2026) 'Predicting Open Source Software Sustainability with \"\n     \"Deep Temporal Neural Hierarchical Architectures and Explainable AI' \\u2014 Builds a \"\n     \"hierarchical Transformer model over 24-month AGGREGATE activity sequences to classify OSS \"\n     \"projects into lifecycle stages, with zero mention of founders or succession. This hypothesis \"\n     \"differs by using a transparent, low-parameter fade-curve descriptor tied to ONE identified \"\n     \"founder's involvement share across the project's full lifespan and targeting a distinct \"\n     \"outcome (survival across an actual founder departure event).\"),\n    (\"Vygotsky (1978) / Wood, Bruner & Ross (1976) scaffolding theory with fading \\u2014 \"\n     \"well-established educational mechanism: the more capable tutor provides structured support \"\n     \"and gradually withdraws it (fading) so the learner internalizes and operates independently; \"\n     \"sudden removal of support before competence matures causes collapse. The cross-domain \"\n     \"transfer to OSS \\u2014 treating the founder's involvement as scaffolding and predicting \"\n     \"project post-departure survival from the shape of the fade \\u2014 has not been previously \"\n     \"operationalized in the OSS sustainability literature.\"),\n    (\"Management literature on founder-CEO succession (e.g., Haveman et al. on organizational \"\n     \"succession; Honjo & Kato 2022 on founder-CEO succession and firm survival; the observation \"\n     \"that founder-CEOs often remain partially involved for some time) \\u2014 studies binary \"\n     \"outcomes of who succeeds and firm survival, not specifically the gradualness of involvement \"\n     \"fade. The OSS adaptation here measures the actual trajectory shape continuously across \"\n     \"behavioral artifacts, in a domain with public, fine-grained per-developer time series that \"\n     \"firms do not expose.\"),\n]\n\ndata = {\n    \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n    \"hypothesis\": (\n        \"An open-source project survives its founder stepping away if and only if the founder's \"\n        \"involvement in the project followed a smooth, prolonged fade \\u2014 a gradually declining \"\n        \"trajectory, measurable as the slope of the founder's month-by-month share of merges, \"\n        \"commits, and code-review decisions over the project's life \\u2014 rather than an abrupt \"\n        \"cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder's \"\n        \"involvement trajectory over the entire pre-departure window predicts post-departure \"\n        \"survival better than any static snapshot measure (bus factor, contributor count, project \"\n        \"age, file count, popularity) at the moment of departure; projects whose founder's \"\n        \"involvement fades gradually (a 'scaffolding fade') survive, while those whose founder \"\n        \"maintained high involvement up to a sudden exit \\u2014 or withdrew abruptly with no \"\n        \"transition period \\u2014 collapse.\"\n    ),\n    \"motivation\": (\n        \"Open-source software underpins global critical infrastructure, yet most OSS projects \"\n        \"depend on one or two 'truck-factor' developers, and roughly half of those that lose their \"\n        \"key people do not survive. Existing research measures this risk state-by-state \\u2014 how \"\n        \"many key developers there are (the bus factor) or what the size and bus factor of the \"\n        \"project are at the moment of departure \\u2014 and finds that simple counts explain little \"\n        \"of the variation in survival. Decision-making authority (who actually merges, reviews, \"\n        \"and decides) tends to concentrate in one founder, and management literature notes that a \"\n        \"binary handover framing misses the empirically observed reality that most founders remain \"\n        \"partially involved for an extended time. This hypothesis imports an established \"\n        \"educational mechanism \\u2014 Vygotsky/Bruner 'scaffolding with fading,' where a teacher \"\n        \"gradually withdraws support as learners internalize the necessary skill \\u2014 into OSS \"\n        \"sustainability as a quantitative predictor: a slow founder fade signals that \"\n        \"contributors are being scaffolded into caretaker capability, whereas a cliff leaves the \"\n        \"contributor base unprepared. If confirmed, the finding would shift OSS risk assessment \"\n        \"from snapshot metrics toward the temporal trajectory of decision-sharing, suggesting that \"\n        \"maintainers should consciously decay their involvement as a survival practice and that \"\n        \"ecosystem funders should evaluate trajectories rather than headcounts when triaging \"\n        \"at-risk projects.\"\n    ),\n    \"assumptions\": assumptions,\n    \"investigation_approach\": (\n        \"Assemble a curated cohort of public GitHub OSS projects whose identified founder has \"\n        \"departed (defined by a 12-month inactivity window consistent with the \"\n        \"abandonment-threshold literature). For each project, clone the repository locally and \"\n        \"extract, per month or quarter from inception to founder departure, the founder's share of \"\n        \"commits, share of PR merges, and share of code-review decisions; fit each trajectory to a \"\n        \"small family of shape descriptors (linear slope, convexity, time-to-onset-of-decline, \"\n        \"abrupt-cliff indicator, plateau-then-cliff indicator) and a quantitative 'fade index' \"\n        \"(e.g., normalized integral over time). Independently label each project's survival using \"\n        \"the Avelino et al. (2019) criterion \\u2014 new active truck-factor developer(s) appearing \"\n        \"after the founder's inactivity window with sustained subsequent activity \\u2014 or, where \"\n        \"labels are ambiguous, fall back on a continuous survival metric (e.g., normalized commit \"\n        \"volume in the 24-month post-departure window relative to pre-departure baseline). Then \"\n        \"build predictive models that compare (a) static baseline features (bus factor, \"\n        \"contributor count, age, popularity, file count, computed at departure) against (b) the \"\n        \"founder fade-curve shape descriptors, on both the binary survival label and the continuous \"\n        \"post-departure activity retention. Use logistic regression and survival analysis (lifelines) \"\n        \"for primary identification; complement with permutation-based feature importance and \"\n        \"train/test splits. As a falsification control, run the same analysis using the fade curve \"\n        \"of a randomly selected non-founder high-activity contributor in each project, expecting it \"\n        \"to have lower predictive power than the founder fade curve if the mechanism is \"\n        \"founder-specific.\"\n    ),\n    \"success_criteria\": (\n        \"Supporting evidence would be: (1) the founder-involvement fade descriptors significantly \"\n        \"outperform static features (bus factor, contributor count, age, popularity) in \"\n        \"cross-validated AUC/R-squared on predicting project survival after departure, with the \"\n        \"fade-slope and abrupt-cliff indicator emerging as dominant feature importances; (2) a \"\n        \"clear directional effect \\u2014 projects whose founder involvement declined smoothly over \"\n        \"time before departure are markedly more likely to survive than those whose founders \"\n        \"maintained a flat plateau or ended with an abrupt cliff \\u2014 with effect size stable \"\n        \"across alternative inactivity thresholds and survival definitions; (3) the fade curve of \"\n        \"the FOUNDER predicts survival better than the fade curve of a randomly chosen equally \"\n        \"active non-founder contributor (founder-specific mechanism). Disconfirming evidence would \"\n        \"be: fade descriptors add no measurable predictive value above static features, the \"\n        \"directional effect reverses or is null after controlling for project age/popularity, or \"\n        \"non-founder fade curves predict just as well (mechanism is generic, not \"\n        \"founder-specific).\"\n    ),\n    \"related_works\": related_works,\n    \"inspiration\": (\n        \"The Phase-1 divergence brainstorm covered eight cross-field directions (ecological \"\n        \"succession, institutional path-dependence, tacit/explicit knowledge externalization, \"\n        \"game-theoretic exit-threat credibility, structural-hole brokering, critical-slowing-down \"\n        \"early warnings, allostatic load, and heterosis/cognitive diversity) \\u2014 searches showed \"\n        \"each was effectively present in OSS sustainability literature or recombination of existing \"\n        \"approaches. The version that survived adversarial novelty checks imports the established \"\n        \"educational mechanism of 'scaffolding with fading' (Vygotsky, Wood\\u2013Bruner\\u2013Ross) \"\n        \"into OSS sustainability: just as a tutor must fade support gradually for a learner to \"\n        \"internalize the skill, a founder must fade involvement gradually for the contributor \"\n        \"community to take on decision-making; an abrupt withdrawal leaves the community \"\n        \"unsupported and the project collapse-prone. The specific transfer is from the \"\n        \"controlled-learning dynamic of tuition, where the role of 'more capable peer' has been \"\n        \"formalized, to the distributed, unstructured OSS setting where no one has previously \"\n        \"operationalized the founder's incremental-detachment trajectory as a survival predictor. \"\n        \"Newer management-research observations (e.g., most founders stay partially involved for \"\n        \"some time) hint at the empirical reality but in this OSS form the trajectory has not been \"\n        \"measured or used as a predictor.\"\n    ),\n    \"terms\": terms,\n    \"summary\": (\n        \"Whether an OSS project survives its founder stepping away is determined not by how many \"\n        \"people there are at the moment of departure, but by the SHAPE of how the founder's \"\n        \"involvement evolved across the project's whole life \\u2014 smooth gradual decline \"\n        \"('scaffolding fade') signals a community prepared to take over and predicts survival; an \"\n        \"abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n    ),\n}\n\nout_path = (\"/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/\"\n            \"claude_agent/.sdk_openhands_agent_struct_out.json\")\nwith open(out_path, \"w\", encoding=\"utf-8\") as f:\n    json.dump(data, f, indent=2, ensure_ascii=False)\nprint(\"WROTE\", out_path, \"bytes=\", len(json.dumps(data)))\n", "kind": "FileEditorObservation"}
```

### [161] ASSISTANT · 2026-08-20 19:25:10 UTC

```
Now let me run the script to write the JSON output and verify it matches the schema.
```

### [162] TOOL CALL — terminal · 2026-08-20 19:25:10 UTC

```
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent && python3 hypothesis.py && ls -la .sdk_openhands_agent_struct_out.json",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [163] TOOL RESULT — terminal · 2026-08-20 19:25:10 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "WROTE /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json bytes= 15595\n-rw-rw-rw- 1 root root 15735 Aug 20 19:25 .sdk_openhands_agent_struct_out.json"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent && python3 hypothesis.py && ls -la .sdk_openhands_agent_struct_out.json", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [164] ASSISTANT · 2026-08-20 19:25:14 UTC

```
The JSON file has been written. Let me validate it against the required schema and verify all required fields are present and well-formed.
```

### [165] TOOL CALL — terminal · 2026-08-20 19:25:14 UTC

```
{
  "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent && python3 -c \"\nimport json\nwith open('.sdk_openhands_agent_struct_out.json') as f:\n    d = json.load(f)\nrequired = ['title','hypothesis','motivation','assumptions','investigation_approach','success_criteria','related_works','inspiration','terms','summary']\nmissing = [k for k in required if k not in d]\nprint('MISSING:', missing)\nprint('title:', d['title'])\nprint('hypothesis_len:', len(d['hypothesis']))\nprint('motivation_len:', len(d['motivation']))\nprint('assumptions_count:', len(d['assumptions']))\nprint('investigation_approach_len:', len(d['investigation_approach']))\nprint('success_criteria_len:', len(d['success_criteria']))\nprint('related_works_count:', len(d['related_works']))\nprint('inspiration_len:', len(d['inspiration']))\nprint('terms_count:', len(d['terms']))\nprint('all terms have term+def:', all('term' in t and 'definition' in t for t in d['terms']))\nprint('summary_len:', len(d['summary']))\nprint('VALID' if not missing else 'INVALID')\n\"\n",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [166] TOOL RESULT — terminal · 2026-08-20 19:25:16 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "MISSING: []\ntitle: Founder Fade Curve Predicts OSS Survival\nhypothesis_len: 874\nmotivation_len: 1473\nassumptions_count: 5\ninvestigation_approach_len: 1740\nsuccess_criteria_len: 1118\nrelated_works_count: 7\ninspiration_len: 1403\nterms_count: 7\nall terms have term+def: True\nsummary_len: 399\nVALID"}], "is_error": false, "command": "cd /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent && python3 -c \"\nimport json\nwith open('.sdk_openhands_agent_struct_out.json') as f:\n    d = json.load(f)\nrequired = ['title','hypothesis','motivation','assumptions','investigation_approach','success_criteria','related_works','inspiration','terms','summary']\nmissing = [k for k in required if k not in d]\nprint('MISSING:', missing)\nprint('title:', d['title'])\nprint('hypothesis_len:', len(d['hypothesis']))\nprint('motivation_len:', len(d['motivation']))\nprint('assumptions_count:', len(d['assumptions']))\nprint('investigation_approach_len:', len(d['investigation_approach']))\nprint('success_criteria_len:', len(d['success_criteria']))\nprint('related_works_count:', len(d['related_works']))\nprint('inspiration_len:', len(d['inspiration']))\nprint('terms_count:', len(d['terms']))\nprint('all terms have term+def:', all('term' in t and 'definition' in t for t in d['terms']))\nprint('summary_len:', len(d['summary']))\nprint('VALID' if not missing else 'INVALID')\n\"", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [167] ASSISTANT · 2026-08-20 19:26:24 UTC

```
All required fields are present, types are correct (assumptions/related_works/terms are arrays, all terms have term+definition), and content is substantial. Let me do a final verification using the file viewer to ensure the file is on disk and complete.
```

### [168] TOOL CALL — terminal · 2026-08-20 19:26:24 UTC

```
{
  "command": "head -c 500 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json; echo; echo \"===LAST100===\"; tail -c 300 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json",
  "is_input": false,
  "timeout": null,
  "reset": false
}
```

### [169] TOOL RESULT — terminal · 2026-08-20 19:26:24 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "{\n  \"title\": \"Founder Fade Curve Predicts OSS Survival\",\n  \"hypothesis\": \"An open-source project survives its founder stepping away if and only if the founder's involvement in the project followed a smooth, prolonged fade \u2014 a gradually declining trajectory, measurable as the slope of the founder's month-by-month share of merges, commits, and code-review decisions over the project's life \u2014 rather than an abrupt cliff or a flat plateau that ends suddenly. Specifically, the SHAPE of the founder\n===LAST100===\n at the moment of departure, but by the SHAPE of how the founder's involvement evolved across the project's whole life \u2014 smooth gradual decline ('scaffolding fade') signals a community prepared to take over and predicts survival; an abrupt cliff or unbroken plateau-then-cliff predicts collapse.\"\n}"}], "is_error": false, "command": "head -c 500 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json; echo; echo \"===LAST100===\"; tail -c 300 /ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json", "exit_code": 0, "timeout": false, "metadata": {"exit_code": 0, "pid": -1, "username": "root", "hostname": "fca996c635b5", "working_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent", "py_interpreter_path": "/usr/local/bin/python", "prefix": "", "suffix": "\n[The command completed with exit code 0.]"}, "full_output_save_dir": "/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/.oh_sessions/87cc6550af5f4f778a2b9bd2e84310fa/observations", "kind": "TerminalObservation"}
```

### [170] ASSISTANT · 2026-08-20 19:26:32 UTC

```
The JSON file is complete and well-formed, starting with the title and ending properly with the summary field. Let me update the task tracker to mark everything complete and do a final check to make sure everything is in order.
```

### [171] TOOL CALL — task_tracker · 2026-08-20 19:26:32 UTC

```
{
  "command": "plan",
  "task_list": [
    {
      "title": "Check user_uploads for reference materials",
      "notes": "No user uploads found - empty folder",
      "status": "done"
    },
    {
      "title": "Brainstorm 5-7 diverse directions without searching",
      "notes": "8 cross-field directions brainstormed; settled on scaffolding-fade trajectory as most novel",
      "status": "done"
    },
    {
      "title": "Web search for landscape overview of each direction",
      "notes": "Landscape confirmed: bus factor, governance transitions, diversity, abandonment empirical, death spiral, deep temporal neural - NONE about founder involvement trajectory",
      "status": "done"
    },
    {
      "title": "Fetch and read potentially relevant papers",
      "notes": "Avelino 2019, Noori 2509, Feng 2023, death spiral 2026, deep temporal neural 2026, ICSE 2026 disengagement - none model founder scaffolding fade",
      "status": "done"
    },
    {
      "title": "Adversarial novelty check",
      "notes": "Scaffolding-fade trajectory confirmed novel - no existing OSS work models founder involvement shape as survival predictor",
      "status": "done"
    },
    {
      "title": "Feasibility check",
      "notes": "Feasible: clone ~50-100 GitHub repos, compute founder commit/merge trajectory with git log, logistic regression/survival analysis in Python. No GPU needed.",
      "status": "done"
    },
    {
      "title": "Write hypothesis JSON output",
      "notes": "JSON written to .sdk_openhands_agent_struct_out.json and validated against schema - all 10 required fields present and well-formed",
      "status": "done"
    }
  ]
}
```

### [172] TOOL RESULT — task_tracker · 2026-08-20 19:26:32 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Task list has been updated with 7 item(s)."}], "is_error": false, "command": "plan", "task_list": [{"title": "Check user_uploads for reference materials", "notes": "No user uploads found - empty folder", "status": "done"}, {"title": "Brainstorm 5-7 diverse directions without searching", "notes": "8 cross-field directions brainstormed; settled on scaffolding-fade trajectory as most novel", "status": "done"}, {"title": "Web search for landscape overview of each direction", "notes": "Landscape confirmed: bus factor, governance transitions, diversity, abandonment empirical, death spiral, deep temporal neural - NONE about founder involvement trajectory", "status": "done"}, {"title": "Fetch and read potentially relevant papers", "notes": "Avelino 2019, Noori 2509, Feng 2023, death spiral 2026, deep temporal neural 2026, ICSE 2026 disengagement - none model founder scaffolding fade", "status": "done"}, {"title": "Adversarial novelty check", "notes": "Scaffolding-fade trajectory confirmed novel - no existing OSS work models founder involvement shape as survival predictor", "status": "done"}, {"title": "Feasibility check", "notes": "Feasible: clone ~50-100 GitHub repos, compute founder commit/merge trajectory with git log, logistic regression/survival analysis in Python. No GPU needed.", "status": "done"}, {"title": "Write hypothesis JSON output", "notes": "JSON written to .sdk_openhands_agent_struct_out.json and validated against schema - all 10 required fields present and well-formed", "status": "done"}], "kind": "TaskTrackerObservation"}
```

### [173] ASSISTANT · 2026-08-20 19:27:51 UTC

```
The hypothesis JSON has been successfully written and validated. Let me provide a final summary.

## Summary

I generated a novel research hypothesis for the AII prompt: **"What determines whether an open-source project survives its founder stepping away?"**

### The Hypothesis: "Founder Fade Curve Predicts OSS Survival"

The core insight is a cross-domain transfer of an established educational-psychology mechanism — **scaffolding with fading** (Vygotsky 1978; Wood, Bruner & Ross 1976) — into open-source software sustainability research. The hypothesis states that OSS project survival after founder departure is determined not by static snapshot measures at the moment of departure (bus factor, contributor count, project age), but by the **SHAPE of the founder's involvement trajectory** across the project's whole lifespan:
- **Smooth gradual decline** ("scaffolding fade") → survival (community was scaffolded into caretaker capability)
- **Abrupt cliff or unbroken plateau-then-cliff** → collapse (community was left unprepared)

### Why It's Novel (Verified Through Adversarial Search)

I researched the landscape of OSS sustainability work and confirmed the closest prior works — Avelino et al. 2019 (TFDD/static factors), Noori et al. 2025 (GOVERNANCE.md text transitions), Kaushik & Chahal 2026 (death spiral/aggregate PR dynamics), Karim et al. 2026 (deep temporal neural sustainability), Chen et al. ICSE 2026 (disengagement impact via DiD) — none of them:
1. Model the founder *specifically* (vs. anonymous "key developers")
2. Model the *dynamic trajectory shape* of the founder's involvement over the whole pre-departure window
3. Use it as a *predictor* of survival-after-departure

The scaffolding-fade mechanism has never been operationalized in OSS sustainability literature. Management research on founder-CEO succession studies binary handover outcomes, not the gradualness of involvement fade measured continuously across behavioral artifacts.

### Feasibility
Testable with Python: clone ~50-100 GitHub repos, extract founder commit/merge/code-review time series from git log, fit fade-curve shape descriptors, run logistic regression + survival analysis (lifelines) comparing against static-feature baselines, with a non-founder falsification control. No GPU needed, well within the $10 OpenRouter budget.

### Output
The validated JSON file is at `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json` with all 10 required fields populated (title, hypothesis, motivation, 5 assumptions, investigation_approach, success_criteria, 7 related_works, inspiration, 7 terms, summary).
```

### [174] TOOL CALL — finish · 2026-08-20 19:27:51 UTC

```
{
  "message": "Successfully generated a novel, feasibility-checked research hypothesis and wrote the validated JSON to `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json`.\n\n**Hypothesis: \"Founder Fade Curve Predicts OSS Survival\"** \u2014 A cross-domain transfer of Vygotsky/Bruner's \"scaffolding with fading\" educational mechanism into OSS sustainability. It claims that whether an OSS project survives its founder stepping away is predicted by the SHAPE of the founder's involvement trajectory across the project's whole life (smooth gradual decline vs. abrupt cliff or plateau-then-cliff), outperforming static snapshot measures (bus factor, contributor count, project age, popularity) at the moment of departure.\n\n**Novelty verified adversarially** against the closest prior works (Avelino 2019 TFDD/static factors; Noori 2025 governance-text transitions; Kaushik 2026 death spiral aggregate PR dynamics; Karim 2026 deep temporal neural lifecycle stage; Chen ICSE 2026 disengagement DiD). None model the founder's specific involvement trajectory as a survival predictor.\n\n**Feasibility confirmed** for Python-only implementation within budget: clone ~50-100 GitHub repos, compute founder share-of-commits/merges/reviews trajectories from git log, fit fade-curve shape descriptors, train logistic regression + lifelines survival analysis with static-feature baseline and a non-founder falsification control.\n\nThe JSON matches the required schema (all 10 required fields present: title, hypothesis, motivation, 5 assumptions, investigation_approach, success_criteria, 7 related_works, inspiration, 7 terms, summary)."
}
```

### [175] TOOL RESULT — finish · 2026-08-20 19:27:51 UTC

```
{"content": [{"cache_prompt": false, "type": "text", "text": "Successfully generated a novel, feasibility-checked research hypothesis and wrote the validated JSON to `/ai-inventor/aii_data/runs/run_dX5VwxrQ9qyp/iter_1/gen_hypo/claude_agent/.sdk_openhands_agent_struct_out.json`.\n\n**Hypothesis: \"Founder Fade Curve Predicts OSS Survival\"** \u2014 A cross-domain transfer of Vygotsky/Bruner's \"scaffolding with fading\" educational mechanism into OSS sustainability. It claims that whether an OSS project survives its founder stepping away is predicted by the SHAPE of the founder's involvement trajectory across the project's whole life (smooth gradual decline vs. abrupt cliff or plateau-then-cliff), outperforming static snapshot measures (bus factor, contributor count, project age, popularity) at the moment of departure.\n\n**Novelty verified adversarially** against the closest prior works (Avelino 2019 TFDD/static factors; Noori 2025 governance-text transitions; Kaushik 2026 death spiral aggregate PR dynamics; Karim 2026 deep temporal neural lifecycle stage; Chen ICSE 2026 disengagement DiD). None model the founder's specific involvement trajectory as a survival predictor.\n\n**Feasibility confirmed** for Python-only implementation within budget: clone ~50-100 GitHub repos, compute founder share-of-commits/merges/reviews trajectories from git log, fit fade-curve shape descriptors, train logistic regression + lifelines survival analysis with static-feature baseline and a non-founder falsification control.\n\nThe JSON matches the required schema (all 10 required fields present: title, hypothesis, motivation, 5 assumptions, investigation_approach, success_criteria, 7 related_works, inspiration, 7 terms, summary)."}], "is_error": false, "kind": "FinishObservation"}
```

### [176] HOOK — PostToolUse · 2026-08-20 19:27:51 UTC

```
<system-reminder>You have 78.7 minutes remaining to finish all your tasks.</system-reminder>
```
