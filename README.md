# The Founder Fade Curve: Trajectory Shape as a Complementary Predictor of OSS Project Survival

<div align="center">

<a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival@main/workflow.svg">
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="workflow-dark.svg">
  <img alt="Artifact workflow — how every artifact in this repo was built" src="workflow.svg">
</picture>
</a>

<sub>🖱️ <b><a href="https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival@main/workflow.svg">Open the interactive diagram</a></b> — every card links to its artifact folder.</sub>

</div>

> **TL;DR** — First quantitative evaluation of the founder fade curve hypothesis: trajectory shape descriptors (slope, convexity, cliff indicator, fade index) do not predict OSS project survival beyond static features (contributor count, bus factor, project age) in a pilot of 14 projects. Static features achieve AUC=0.857, shape features perform below chance (AUC=0.408), and adding shape features worsens net reclassification (NRI=-0.143). Power analysis estimates minimum N=100 needed for 80% power. Synthetic validation confirms descriptor pipeline works correctly. Falsification control finds no founder-specific effect. The null finding calls for larger-scale validation with full trajectory data.

<details>
<summary>Full hypothesis</summary>

An open-source project's post-departure survival may be marginally enhanced by the shape of the founder's involvement trajectory, but this effect is secondary to and subsumed by static snapshot measures (contributor count, bus factor, project age). Specifically, a smooth, prolonged founder fade — where the founder's share of commits, merges, and review decisions gradually declines over an extended pre-departure window — is hypothesized to be *complementary* to static features rather than superior to them, and its incremental value is expected to be small (AUC improvement < 0.05). The core empirical claims are now: (1) trajectory shape descriptors add at most marginal predictive value beyond static features, and only in a sufficiently large cohort (N ≥ 100); (2) the founder-specific mechanism claim is unsupported — pilot evidence showed identical AUC (0.408) for founder and non-founder fade curves, suggesting trajectory shape effects, if any, are generic to any high-activity contributor rather than unique to the founder role; (3) multi-dimensional involvement metrics (code review, architectural decisions, governance participation) should be incorporated alongside commit share, as founders may fade from commits while retaining influence through other channels; (4) survival labels must be computed from TFDD framework data in each study rather than pre-assigned from public knowledge, to avoid circularity. The hypothesis is now restricted to well-powered studies (N ≥ 100) with data-derived survival labels, and explicitly acknowledges that static features already capture the bulk of predictable variance.

</details>

[![Download PDF](https://img.shields.io/badge/Download-PDF-red)](https://cdn.jsdelivr.net/gh/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival@main/paper.pdf) [![LaTeX Source](https://img.shields.io/badge/LaTeX-Source-orange)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/paper_latex)

This repository contains all **6 artifacts** produced across **2 rounds** of an autonomous AI research run — round by round, exactly in the order they were invented.

## Round 1

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Literature Survey: Founder Fade & OSS Survival](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-1/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/research-1/src) | — |
| **[GitHub OSS Repos for Founder Fade Study](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/dataset-1)** | [![dataset](https://img.shields.io/badge/dataset-f59e0b)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/dataset-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-1/dataset-1/demo/data_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/dataset-1/src) | — |
| **[Founder Fade Curve Predicts OSS Survival](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-1/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/experiment-1/src) | — |

## Round 2

| Artifact | Type | Demo | Source | Builds on |
|----------|------|------|--------|-----------|
| **[Founder Fade Curve Analysis on OSS Projects](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/experiment-1)** | [![experiment](https://img.shields.io/badge/experiment-8b5cf6)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/experiment-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-2/experiment-1/demo/method_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/experiment-1/src) | <sub><i>differences:</i><br/>[dataset‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/dataset-1)</sub> |
| **[Citation Verification & Real OSS Survival Papers](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/research-1)** | [![research](https://img.shields.io/badge/research-3b82f6)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/research-1) | [![View Research](https://img.shields.io/badge/View-Research-green)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-2/research-1/demo/research_demo.md) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/research-1/src) | <sub><i>extends:</i><br/>[research‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/research-1)</sub> |
| **[Bootstrap CI and Power Analysis for Founder Fade Curve Pilot](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/evaluation-1)** | [![evaluation](https://img.shields.io/badge/evaluation-10b981)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/evaluation-1) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/blob/main/round-2/evaluation-1/demo/eval_code_demo.ipynb) | [![Source Code](https://img.shields.io/badge/Source_Code-2962FF)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/evaluation-1/src) | <sub><i>differences:</i><br/>[experiment‑1&nbsp;(R1)](https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-1/experiment-1)</sub> |

## Repository Structure

Artifacts are grouped by the round of invention that produced them. Each
artifact has its own folder with source code and a self-contained demo:

```
.
├── round-1/                         # One folder per round of invention
│   ├── experiment-1/
│   │   ├── README.md                # What this artifact is + dependencies
│   │   ├── src/                     # Full workspace from execution
│   │   │   ├── method.py            # Main implementation
│   │   │   ├── method_out.json      # Full output data
│   │   │   └── ...                  # All execution artifacts
│   │   └── demo/                    # Self-contained demo
│   │       └── method_code_demo.ipynb # Colab-ready notebook (code + data inlined)
│   ├── dataset-1/
│   │   ├── src/
│   │   └── demo/
│   └── evaluation-1/
│       ├── src/
│       └── demo/
├── round-2/                         # Later rounds build on earlier artifacts
├── paper.pdf                        # Research paper
├── paper_latex/                     # LaTeX source files
├── chat/                            # Every prompt, response and tool call, per module
├── workflow.svg                     # Artifact dependency diagram (this page's header)
└── README.md
```

## Running Notebooks

### Option 1: Google Colab (Recommended)

Click the "Open in Colab" badges above to run notebooks directly in your browser.
No installation required!

### Option 2: Local Jupyter

```bash
# Clone the repo
git clone https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival
cd ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival

# Install dependencies
pip install jupyter

# Run any artifact's demo notebook
jupyter notebook <artifact_folder>/demo/
```

## Source Code

The original source files are in each artifact's `src/` folder.
These files may have external dependencies - use the demo notebooks for a self-contained experience.

---
*Generated by AI Inventor Pipeline - Automated Research Generation*
