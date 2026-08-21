# gen_full_paper — report_results

> Phase: `gen_paper_repo` · `gen_full_paper`
> Run: `iter1_fb32313dcec5` — Founder Fade Curves Do Not Predict Open-Source Project Survival
>
> Full, verbatim record of every prompt the AI Inventor pipeline gave this agent — system-user, human-user and skill-input — in the order they landed. Nothing truncated.

## Task: `gen_full_paper` (sdk_openhands_agent)

### [1] SYSTEM-USER prompt · 2026-08-21 20:33:14 UTC

````
<workspace>
Your workspace: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace`

CRITICAL: Every file you create, write, or save MUST be inside this workspace directory (subdirectories OK). You MUST NOT write files anywhere outside this path — external paths are READ-ONLY. Use absolute paths for all file operations.

EVERY file write MUST start with `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/`:
GOOD: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/file.py`, `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/results/out.json`
BAD: `/tmp/file.py`, `~/output.json`, `./file.py`, any path outside the workspace
</workspace>

<task>
Create a publication-ready top-conference LaTeX paper with BibTeX from <paper_text> and <available_figures>, compile to PDF.
</task>

<tool_use>
Maximize parallel tool calls. Parallelize independent operations, only sequentialize dependencies.
- Multiple searches/fetches on different topics → parallel in one turn
- Search then fetch results → sequential (need URLs first)
</tool_use>

<paper_text>
title: Founder Fade Curves Do Not Predict Open-Source Project Survival
abstract: >-
  Open-source projects that lose their founder face a high risk of collapse, yet existing research predicts survival using
  static snapshots — bus factor, contributor count, project age — and finds weak separation. We test whether the temporal
  trajectory of a founder's involvement before departure provides complementary predictive signal. Drawing on scaffolding
  theory from educational psychology, we hypothesize that founders who gradually reduce their involvement scaffold their community
  into caretaker capability, whereas abrupt departures leave the community unprepared. We operationalize this as six quantitative
  descriptors extracted from monthly founder commit, merge, and review shares across 309 projects in the ESEM 2019 dataset.
  Our results disconfirm the hypothesis: fade-only models perform below chance, adding fade descriptors to static features
  yields no improvement, and the directional effect reverses. A falsification control confirms that founder fade curves carry
  no genuine signal. We conclude that the scaffolding-fade mechanism does not operate as predicted in open-source sustainability,
  and that post-departure activity — not pre-departure founder trajectories — drives survival prediction.
paper_text: |
  # Introduction

  Open-source software underpins critical global infrastructure, from Linux kernels to Python package ecosystems. Yet the sustainability of these projects remains fragile: roughly half of open-source projects that lose their primary maintainer cease active development within two years [1]. The dominant framework for studying this problem — Truck Factor Developer Detachment (TFDD) [1] — defines abandonment as the point when all developers holding significant codebase expertise become inactive. Projects are then classified as surviving if new core developers subsequently emerge, or collapsed if they do not.

  The static snapshot approach has proven limited. Avelino et al. [1] found that among 1,932 popular GitHub projects, only 41 percent of those experiencing TFDD survived. Nourry et al. [2] replicated this on 36,464 projects and found an even lower 27 percent survival rate. Both studies identify static factors — project age, contributor count, bus factor, star count — as weak predictors, with little variance explained. As Nourry et al. note, the only metric showing a clear difference between surviving and non-surviving projects was project age at TFDD [2].

  This limitation motivates searching for better predictors. Educational psychology offers a well-established framework for understanding how expertise transfers: Vygotsky's sociocultural theory [13] and Bruner, Wood, and Ross's scaffolding research [14, 15] demonstrate that expert learners internalize capabilities most effectively when support is gradually withdrawn rather than abruptly removed. In the open-source context, the founder's involvement — commits, merges, code reviews — constitutes a form of scaffolding: each decision they make models judgment for the community. A gradual decline in this involvement gives contributors repeated opportunities to observe, practice, and internalize decision-making. An abrupt departure, by contrast, leaves the community without the cognitive support needed to assume responsibility.

  We test this scaffolding-fade hypothesis on real-world data. We ask three questions: (1) Do temporal fade descriptors of founder involvement outperform static project metrics in predicting whether a project survives its founder's departure? (2) Do projects with gradually fading founder involvement survive at higher rates than those with abrupt departures? (3) Does the fade curve of the founder predict survival better than the fade curve of other active contributors?

  Our results disconfirm the hypothesis across all three questions. Using the ESEM 2019 dataset of 309 GitHub projects with founder departure events, we find that fade-only models perform below chance and that adding fade descriptors to static features yields no improvement. The directional effect reverses: collapsed projects have a slightly higher mean fade index than survived projects. A falsification control confirms that founder fade curves carry no genuine signal, performing worse than shuffled trajectories. The full quantitative results are presented in Section 4.

  [FIGURE:fig1]

  Our contributions are:

  1. We rigorously test the scaffolding-fade hypothesis on real-world OSS data (309 projects from the ESEM 2019 dataset) and find it disconfirmed.
  2. We define six quantitative fade descriptors extracted from monthly founder commit, merge, and review shares, and demonstrate their construction from public repository artifacts \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/experiment-1}}.
  3. We provide empirical evidence that fade descriptors perform below chance (AUC 0.462) and add no predictive value beyond static features, ruling out a theoretically motivated mechanism.
  4. We identify that post-departure activity — not pre-departure founder trajectories — is the dominant predictor of survival, with commits after departure accounting for 33.5 percent of permutation importance.
  5. We expand the related work to cover recent temporal analysis in OSS, including survival analysis with time-varying covariates, deep learning sequence models, and workflow dynamics analysis \footnote{Code: \url{https://github.com/ai-inventor-outputs/ai-invention-ad55a2-founder-fade-curve-predicts-oss-survival/tree/main/round-2/research-1}}.

  # Related Work

  ## Open-Source Abandonment and Survival

  The foundational work on open-source project survival is Avelino et al.'s Truck Factor Developer Detachment framework [1]. They define the truck factor as the minimum number of developers whose simultaneous departure would seriously impair a project, computed using the Degree of Authorship metric [16]. A TFDD event occurs when all truck-factor developers become inactive, defined as one year without commits. Among 1,932 popular GitHub projects, 16 percent experienced TFDD and 41 percent of those survived by attracting at least one new truck-factor developer [1]. Surviving projects tended to be younger at TFDD, have more post-departure commits, and attract a single new core developer in 86 percent of cases.

  Nourry et al. [2] replicated this on 36,464 projects including smaller, less popular ones, and found dramatically different rates: 89.6 percent faced TFDD but only 27 percent survived. The disparity is explained by sample composition — smaller projects lack the community gravity to attract new maintainers. Nourry et al. found that project age at TFDD was the only static metric showing a clear difference between survivors and non-survivors.

  Other work has examined core developer turnover patterns. Calefato et al. [3] found that 45 percent of core developers disengage for at least one year, with 35 to 55 percent returning. Jamieson et al. [4] showed that value-related discussions in GitHub issues predict contributor turnover, suggesting that social dynamics matter beyond pure code metrics.

  ## Founder and Governance Dynamics

  Noori et al. [5] applied natural-language processing to GOVERNANCE.md files across 637 repositories to characterize how textual governance evolves as projects mature. They documented institutional maturation but did not predict survival outcomes. Their work differs from ours in modality — textual governance rather than behavioral trajectory — and in outcome — descriptive rather than predictive.

  Chen et al. [6] used difference-in-differences across 50,804 repositories to estimate the impact of core contributor disengagement on pull-request throughput, acceptance rates, and merge time. They found that impact varies with static contributor profiles but did not model the founder specifically or predict survival. (This work is cited from the hypothesis literature review; the full publication details remain pending.)

  ## Temporal Methods for OSS Prediction

  Recent work has explored temporal approaches to OSS sustainability prediction. Karim et al. [7] built a hierarchical Transformer model over 24-month aggregate activity sequences to classify projects into lifecycle stages, achieving over 94 percent accuracy. Their work covers aggregate temporal patterns but does not isolate founder involvement trajectories or predict post-departure survival. The temporal modeling literature also includes survival analysis with time-varying covariates [8], typically using project-level aggregates like commit frequency, and deep learning sequence models (LSTM/GRU/Transformer) modeling aggregate activity patterns [7].

  Kaushik and Chahal [9] identified a death spiral in open-source projects through pull-request workflow dynamics — increasing friction, backlog growth, falling innovation, and rising merge latency. Their analysis is post-hoc, beginning after decline starts, and is community-level rather than founder-specific. They note that popularity and innovation are causes of survival while workflow friction is a byproduct, but do not analyze the founder's behavioral trajectory before departure.

  ## Scaffolding and Fading in Education

  The concept of scaffolding originates in Vygotsky's sociocultural theory [13], which posits that learning occurs within a Zone of Proximal Development — the space between what a learner can do independently and what they can achieve with guidance. Bruner, Wood, and Ross [14] operationalized this as scaffolding: a tutor provides structured support that is gradually withdrawn as the learner internalizes the skill. Wood et al. [15] demonstrated that optimal learning occurs when support is reduced incrementally; abrupt removal before competence matures causes performance collapse.

  This educational mechanism has been replicated across domains including mathematics education, programming education, and second-language acquisition, but has never been applied to open-source sustainability. Our contribution is the cross-domain transfer attempt: we treat the founder's involvement as scaffolding and test whether the shape of the fade curve predicts post-departure survival. Our results show that this transfer does not hold in the OSS context.

  # Methods

  ## Problem Definition

  We study the prediction of open-source project survival after founder departure. Let $P$ be an open-source project with founder $f$. Let $T$ be the set of monthly time points from project inception to founder departure, where $n$ is the number of months observed.

  For each month $t_i$, we define three involvement measures for the founder:

  - $C(t_i)$: founder's share of total commits in month $t_i$
  - $M(t_i)$: founder's share of total pull-request merges in month $t_i$
  - $R(t_i)$: founder's share of total code-review decisions in month $t_i$

  The founder's combined involvement at time $t_i$ is the average of these three shares:

  $$S(t_i) = \frac{C(t_i) + M(t_i) + R(t_i)}{3}$$

  We define the founder fade curve as the time series of $S$ values over the pre-departure window.

  The founder departs at time $t_n$, defined as a 12-month inactivity window from the last commit, consistent with the Avelino et al. criterion [1]. We label the project as surviving if at least one new truck-factor developer appears with sustained activity in the 24 months post-departure, following the ESEM 2019 criterion [1]. Otherwise, the project is labeled collapsed.

  ## Fade Descriptors

  We extract six quantitative descriptors from the fade curve. All curves are denoised using a Savitzky-Golay filter with window length five and polynomial order two before computing descriptors, following signal-processing best practices for noisy time-series data.

  1. **Linear slope**: The slope of a linear regression of $S$ on time, normalized by the initial value $S(t_0)$. Negative slope indicates gradual decline; positive slope indicates increasing involvement.

  2. **Convexity**: The leading coefficient of a quadratic fit to the smoothed curve, normalized by $S(t_0)$, capturing whether the fade accelerates or decelerates.

  3. **Decline onset time**: The first month where the smoothed first derivative is consistently negative (below -0.01), measured as a fraction of total months from project start.

  4. **Cliff score**: The ratio of the final two-month drop to the average of the preceding six months, bounded between 0 and 1. High values indicate abrupt departure.

  5. **Plateau indicator**: A binary flag indicating whether the curve maintained low variance for at least five months before the decline onset, suggesting a plateau-then-cliff pattern.

  6. **Fade index**: A composite score bounded between 0 and 1, where 1 indicates a smooth linear fade and 0 indicates an abrupt cliff. Computed as $1 - \text{cliff\_score} + 0.3$ if slope is negative, minus 0.2 if plateau is detected.

  ## Static Features

  We compare fade descriptors against seven static features measured at departure:

  - Bus factor: Minimum number of developers whose departure would impair the project [16].
  - Contributor count: Total number of unique contributors at departure.
  - Stars (log-transformed): GitHub star count at departure.
  - File count (log-transformed): Number of files in the repository at departure.
  - Repository age: Years from repository creation to departure.
  - Commits before departure (log-transformed): Total commits in the pre-departure period.
  - Commits after departure (log-transformed): Total commits in the 24-month post-departure period.

  ## Data Sources

  We use the ESEM 2019 dataset [1], which provides 315 GitHub projects with TFDD events, sourced from Zenodo (10.5281/zenodo.2546008). After filtering for projects with at least 6 months of pre-departure trajectory data, we obtain 309 projects: 127 survived and 182 collapsed . The dataset includes monthly time-series features for founder commit, merge, and review shares, along with static project metadata (stars, forks, contributors, bus factor).

  ## Experimental Setup

  We train four models using stratified five-fold cross-validation:

  - **Model A**: Logistic regression with static features only.
  - **Model B**: Logistic regression with fade descriptors only.
  - **Model C**: Logistic regression with all features combined (static + fade + interaction terms).
  - **Model D**: Random forest with all features combined.

  We evaluate using area under the ROC curve for classification and log-loss for probability calibration. Permutation importance assesses feature contribution. For directionality analysis, we compare mean fade descriptors between survived and collapsed groups using independent two-sample t-tests with Cohen's $d$ effect sizes. A falsification control replaces the founder's fade index with uniformly random values and retrains the fade-only model.

  # Experiments and Results

  ## Main Results

  Table 1 summarizes the cross-validated performance of all models on the 309-project ESEM 2019 dataset.

  **Table 1: Model Performance on 309 Projects**

  | Model | Features | AUC | AUC Std | Log-Loss |
  |-------|----------|-----|---------|----------|
  | A (Static) | bus_factor, contributors, age, stars, files, commits_before, commits_after | 0.928 | 0.029 | 0.356 |
  | B (Fade) | slope, convexity, onset, cliff, plateau, fade_idx | 0.462 | 0.091 | 0.692 |
  | C (Combined) | All features + interactions | 0.929 | 0.030 | 0.358 |
  | D (Random Forest) | All features + interactions | 0.880 | 0.032 | — |

  [FIGURE:fig2]

  Model B achieves AUC of 0.462, which is below the chance level of 0.500. This indicates that fade descriptors not only fail to predict survival — they predict it in the wrong direction. Model C achieves AUC of 0.929, essentially identical to Model A's 0.928, confirming that fade descriptors add no meaningful predictive value beyond static features. The random forest model (Model D) achieves lower AUC (0.880), suggesting that the relationship between features and survival is approximately linear and that the logistic regression captures it well.

  The static-only model's strong performance (AUC 0.928) is driven primarily by post-departure activity. The feature log-transformed commits after departure accounts for 33.5 percent of permutation importance in the combined model, followed by the interaction term the interaction between fade index and contributor count (16.8 percent) and contributor count (12.7 percent). Pure fade descriptors rank at the bottom: cliff score (0.09 percent) and fade index (-0.007 percent).

  **Table 2: Permutation Feature Importance (Combined Model)**

  | Feature | Importance |
  |---------|-----------|
  | commits_after_log | 0.335 |
  | fade_idx_x_contributors | 0.168 |
  | contributor_count | 0.127 |
  | commits_before_log | 0.125 |
  | bus_factor | 0.052 |
  | cliff_x_bus_factor | 0.002 |
  | stars_log | 0.001 |
  | file_count_log | 0.001 |
  | S_cliff | 0.001 |
  | S_fade_idx | -0.000 |

  ## Directionality

  The directionality analysis reveals that the predicted relationship between fade patterns and survival does not hold in the data. The mean fade index for survived projects is 0.934, while collapsed projects have a mean of 0.962 — opposite to the predicted direction. The difference is not statistically significant (t = -1.329, p = 0.185, Cohen's $d$ = -0.154).

  The cliff score shows a similar pattern: survived projects have a mean cliff score of 0.111 versus 0.076 for collapsed projects (p = 0.231), again opposite to the predicted direction. The only descriptor showing a significant difference is the normalized slope: survived projects have a mean slope of -0.0114 versus -0.0086 for collapsed projects (p = 0.0009), with survived projects showing a slightly more negative (steeper declining) slope. However, this effect is small and its interpretation is ambiguous — a steeper decline could indicate either more aggressive fading or a sharper pre-departure withdrawal.

  [FIGURE:fig3]

  ## Falsification Control

  To test whether founder fade curves carry any genuine signal, we replace the founder's fade index with uniformly random values drawn from [0, 1] and retrain the fade-only model. The shuffled model achieves AUC of 0.536, compared to 0.462 for the actual founder fade curve. The difference of -0.074 indicates that the founder's actual fade trajectory performs worse than random noise. This falsification control confirms that the fade descriptors do not encode any genuine predictive signal about project survival.

  # Discussion

  ## Interpretation

  Our results disconfirm the scaffolding-fade hypothesis in the open-source context. Despite the theoretical plausibility that gradual founder involvement reduction would scaffold community capability, the empirical data shows no such effect. Three findings are notable:

  First, fade descriptors perform below chance (AUC 0.462), suggesting that the relationship between founder involvement trajectories and project survival is either absent or operates in a direction opposite to our hypothesis. The slight reversal in directionality (collapsed projects having higher fade indices) may reflect confounding factors: projects that survive may do so because they are larger and more active, and larger projects naturally have flatter founder involvement curves (the founder's share of activity is diluted across more contributors), producing higher fade indices by construction rather than by design.

  Second, the dominant predictor of survival is post-departure activity (log-transformed commits after departure, importance 0.335). This suggests that survival is determined by what happens after the founder leaves — whether the community continues to contribute — rather than by what happened before. The static features that drive prediction are largely measures of project momentum and community size, not of the founder's departure pattern.

  Third, the interaction term the interaction between fade index and contributor count ranks second in importance (0.168), suggesting that the relationship between fade patterns and survival may depend on project size. However, this interaction does not rescue the main effect: in isolation, fade descriptors remain uninformative.

  ## Why the Hypothesis Failed

  Several factors may explain why the scaffolding-fade hypothesis does not hold in open-source contexts:

  **Different mechanism of knowledge transfer**: Educational scaffolding operates through deliberate, structured support withdrawal. Open-source founder involvement is rarely a planned fade — it is typically driven by external factors (career changes, burnout, personal circumstances) rather than intentional capability transfer. The founder's declining involvement may reflect personal constraints rather than community readiness.

  **Implicit vs. explicit scaffolding**: In education, scaffolding is explicit and observable. In open-source projects, the founder's "scaffolding" — if it exists — is implicit in the codebase architecture, documentation, and community norms. These may transfer regardless of the founder's activity trajectory.

  **Community self-organization**: Open-source communities may self-organize around capability transfer through mechanisms not captured by founder activity curves — issue discussions, pull-request reviews by non-founders, documentation contributions, and informal mentorship.

  **Selection effects**: Projects that survive may do so because of inherent characteristics (topic relevance, ecosystem position, funding) that are independent of founder behavior. The founder's involvement trajectory may be a byproduct of these characteristics rather than a cause of survival.

  ## Comparison to Prior Work

  Our results are consistent with Nourry et al.'s finding that static metrics explain little variance in survival [2], but they extend that finding to temporal descriptors. Where Nourry et al. found that project age was the only static metric showing clear separation, we find that post-departure activity (a retrospective measure) is the strongest predictor. This suggests that survival is determined by post-departure dynamics rather than pre-departure conditions.

  Our results contrast with Karim et al.'s success in predicting lifecycle stages using temporal sequences [7]. The difference may be that lifecycle stage classification is a different task from survival prediction: the former classifies current state from aggregate patterns, while the latter predicts a binary outcome from a specific event. Our fade descriptors target a narrower signal (founder-specific trajectory) that may be too weak to carry predictive value.

  ## Practical Implications

  For open-source maintainers: The absence of a fade effect suggests that conscious fading of involvement is not a proven survival strategy. Instead, maintainers should focus on building community capacity through explicit mechanisms: documentation, onboarding processes, and distributed decision-making — regardless of their own activity trajectory.

  For ecosystem funders: Evaluating fade trajectories is not a reliable triage signal. Resources should be directed toward projects based on community size, post-departure activity, and ecosystem position — the features that actually predict survival.

  ## Limitations

  Our study has several limitations. The 309-project dataset, while drawn from real-world data, is modest in size and may lack power to detect small effects. Our founder identification relies on repository creation metadata and earliest sustained contribution, which may misidentify founders in projects with early co-founders. Our analysis is restricted to GitHub artifacts and may not generalize to other platforms. We use the Avelino et al. criterion for survival, which may misclassify projects that survive through distributed maintenance without a single new core developer. Our observational analysis cannot establish causality, and the negative results could reflect measurement error in the fade descriptors rather than absence of the underlying mechanism.

  # Conclusion

  We tested the scaffolding-fade hypothesis — that the shape of a founder's involvement trajectory predicts open-source project survival after departure — on the ESEM 2019 dataset of 309 GitHub projects. The hypothesis is disconfirmed: fade-only models achieve AUC of 0.462 (below chance), adding fade descriptors to static features yields no improvement (combined AUC 0.929 versus static-only AUC 0.928), and the directional effect reverses (collapsed projects have higher mean fade index). A falsification control confirms that founder fade curves carry no genuine signal.

  The primary predictor of survival is post-departure activity, not pre-departure founder trajectories. This suggests that open-source project survival is determined by what happens after the founder leaves — whether the community continues to contribute — rather than by how the founder departed. The scaffolding-fade mechanism from educational psychology, while theoretically plausible, does not operate in the open-source context as hypothesized.

  Future work should explore alternative mechanisms of capability transfer in open-source communities, including explicit governance structures, documentation quality, and community self-organization patterns. The negative result reported here rules out one specific mechanism and sharpens the question of what actually enables open-source projects to survive their founders.

  # References

  \bibliography{references}
  \bibliographystyle{plainnat}
summary: >-
  We rigorously tested the scaffolding-fade hypothesis — that gradual founder involvement reduction predicts OSS project survival
  — on 309 real projects from the ESEM 2019 dataset. The hypothesis is disconfirmed: fade descriptors perform below chance
  (AUC=0.462), add no value beyond static features, and show reversed directionality. Post-departure activity, not pre-departure
  founder trajectories, drives survival prediction. This negative result rules out a theoretically motivated mechanism and
  sharpens the question of what actually enables OSS projects to survive their founders.
</paper_text>

<available_figures>
--- Item 1 ---
id: fig1
figure_type: concept
title: Scaffolding-Fade Hypothesis Pipeline
caption: >-
  Experimental pipeline: from monthly founder activity shares to fade curve descriptors, compared against static features
  in predicting project survival. The hypothesis predicted that smooth fade curves would correlate with survival; our results
  disconfirm this prediction.
image_gen_detailed_description: >-
  Horizontal flow diagram, left to right, clean white background, sans-serif font. Six stages connected by arrows: (1) 'GitHub
  Repository' (gray box with git icon) -> (2) 'Monthly Founder Shares: commits, merges, reviews' (blue box with small bar
  chart icon) -> (3) 'Fade Curve: S(t) over time' (green box with a curved line icon) -> (4) 'Six Descriptors: slope, convexity,
  onset, cliff, plateau, fade_index' (orange box with list icon) -> (5) 'Models: Static vs Fade vs Combined' (purple box with
  three model icons) -> (6) 'Result: AUC=0.462 (below chance)' (red box with X mark). Below the main flow, a dashed arrow
  from stage 4 to a smaller box labeled 'Hypothesis: smooth fade -> survival' with a red X through it. The final result box
  should be prominent and red to emphasize the negative finding.
aspect_ratio: '21:9'
summary: Hero diagram showing the experimental pipeline and the disconfirmed hypothesis
figure_path: figures/fig1_v0.jpg

--- Item 2 ---
id: fig2
figure_type: data
title: Model Performance Comparison
caption: >-
  Cross-validated AUC-ROC for four models on 309 projects. Static-only model (A) achieves AUC=0.928. Fade-only model (B) performs
  below chance at AUC=0.462. Combined model (C) matches static-only at AUC=0.929. Random forest (D) achieves AUC=0.880. Error
  bars show standard deviation across 5 folds.
image_gen_detailed_description: >-
  Grouped bar chart with 4 bars. X-axis labels: 'Static (A)', 'Fade (B)', 'Combined (C)', 'RF (D)'. Y-axis: 'AUC-ROC' from
  0.3 to 1.0. Bar values: Static=0.928, Fade=0.462, Combined=0.929, RF=0.880. Error bars (std): Static=0.029, Fade=0.091,
  Combined=0.030, RF=0.032. Color scheme: Static=blue, Fade=red (to highlight below-chance), Combined=green, RF=gray. A horizontal
  dashed line at y=0.5 labeled 'Chance'. A horizontal dashed line at y=0.928 labeled 'Static baseline'. Font: sans-serif,
  white background.
aspect_ratio: '4:3'
summary: >-
  Bar chart comparing AUC across four models, highlighting that fade-only performs below chance
figure_path: figures/fig2_v0.pdf

--- Item 3 ---
id: fig3
figure_type: data
title: Fade Index Distribution by Survival
caption: >-
  Distribution of fade index for survived (mean=0.934) versus collapsed (mean=0.962) projects. The collapsed group has a slightly
  higher mean fade index, opposite to the predicted direction. The difference is not statistically significant (p=0.185, Cohen's
  d=-0.154).
image_gen_detailed_description: >-
  Side-by-side box plot with two groups. X-axis labels: 'Survived (n=127)', 'Collapsed (n=182)'. Y-axis: 'Fade Index' from
  0.5 to 1.0. Box plot statistics: Survived group - mean=0.934, median approximately 0.95, IQR roughly 0.88 to 0.98. Collapsed
  group - mean=0.962, median approximately 0.97, IQR roughly 0.91 to 0.99. Color scheme: Survived=blue, Collapsed=red. Add
  a horizontal line at y=0.934 labeled 'Survived mean' and y=0.962 labeled 'Collapsed mean'. Annotate with 'p=0.185, d=-0.154'
  above the plot. Font: sans-serif, white background.
aspect_ratio: '4:3'
summary: >-
  Box plot showing fade index distributions, with collapsed projects having higher mean opposite to hypothesis
figure_path: figures/fig3_v0.pdf
</available_figures>

<figure_requirements>
CRITICAL: Include ALL figures from <available_figures>. No exceptions.

- Every figure MUST use \includegraphics{figures/<the filename from its own `figure_path` above>} — INCLUDING the extension it actually has. Data figures are delivered as `.pdf` (vector, so their axis labels stay sharp) and concept figures as `.jpg`. Writing `.jpg` for a `.pdf` figure names a file that is not in figures/ and the build fails on it
- Do NOT skip, convert to tables, or describe without inserting
- Each needs: \begin{figure}[placement], \includegraphics, \caption, \label, \end{figure} — one placement for every figure, see FLOAT PLACEMENT below. Constrain every \includegraphics with `width=\linewidth,height=0.85\textheight,keepaspectratio`. The height is a LAST RESORT, not the usual limit: it exists so a very tall figure cannot overrun the page, and at 0.4 it bound almost everything instead — a 1:1 confusion matrix printed at 50.9% and its 11 pt axis labels reached the page at 5.6 pt, below what any venue accepts. At 0.85 every ratio the paper prompt prescribes (21:9, 16:9, 4:3, 1:1) is limited by WIDTH, prints at 93% and keeps its text above 10 pt. Use exactly these option keys — `max height=` is NOT valid LaTeX
- Use the `caption` field from each figure for \caption{...} — do NOT invent new captions
- Place figures where their [FIGURE:fig_id] markers appear in paper_text
- VERIFICATION: paper.tex MUST have exact same number of \includegraphics as <available_figures>
- Do NOT generate new figure images (no matplotlib, no PIL, no image generation). Use ONLY the pre-generated figures from <available_figures>. They were already created by a previous pipeline step.

FLOAT PLACEMENT: every figure gets \begin{figure}[!htbp]. Measured, not chosen:
the document the aii-paper-to-latex skill sets up is ONE column, so `figure*` is
exactly as wide as `figure` (469.76pt either way) and gains nothing; and any
placement asking for a page TOP — `[!t]`, `[!tbp]` — floated the hero diagram above
the paper's own title on page 1, while `[!htbp]` did not. `[!htbp]` also gives LaTeX
four options, so a float can never be deferred to the end of the document, which one
option alone risks. Where the hero ENDS UP is decided by its [FIGURE:] marker in
paper_text, which is already placed near the end of the Introduction — preserve it.
</figure_requirements>

<artifact_links>
The paper_text contains \footnote{Code: \url{...}} references linking to artifact source code
on GitHub. Include \usepackage{hyperref} and \usepackage{url}.
Preserve these exactly as-is — do not remove, rewrite, or convert them to plain text.
The URLs will not resolve yet (the repo is deployed after compilation) — do NOT try to verify or fix them.
</artifact_links>

<headings>
NEVER use inline math (``$...$``) inside ``\section{...}`` / ``\subsection{...}`` / ``\subsubsection{...}`` arguments — hyperref's bookmark builder errors out (``Token not allowed in a PDF string``) and the PDF outline breaks. If a section heading needs a math-looking term, use the text equivalent (``d star`` not ``$d^*$``, ``alpha-equivalent`` not ``$\alpha$-equivalent``) or wrap it in ``\texorpdfstring{$math$}{plain}``. Inline math inside body paragraphs is fine.
</headings>

FIRST, add ALL of these to your todo list using your task/todo-tracking tool:

CRITICAL: Todo content must be copied exactly as is written here, with NO CHANGES. These todos are intentionally detailed so that another LLM could read each one without any external context and understand exactly what it has to do.

<todos>
TODO 1. Read and STRICTLY follow these skills: aii-paper-to-latex, aii-semscholar-bib.
TODO 2. Review <paper_text> and <available_figures>. Copy all figure images into ./figures/ in your workspace. Count figures — MUST include every one. Plan placements per section. Build `./references.bib` via aii_semscholar_bib__fetch — collect DOIs/ArXiv IDs from <paper_text> and batch-fetch all BibTeX in one call. Do NOT fabricate entries.
TODO 3. Create `./paper.tex` per aii-paper-to-latex skill's setup, write ALL sections, insert ALL figures from <available_figures>, include `./references.bib` via \bibliography. Compile to PDF per skill's process. Fix errors.
TODO 4. CRITICAL VERIFICATION: Run `grep -c 'includegraphics' paper.tex`, confirm count equals figures in <available_figures>. If not, add missing figures. Verify `./paper.pdf` was created.
TODO 5. VISUAL REVIEW: Write Python script to convert EVERY page of paper.pdf to PNG at 150 DPI (use pdf2image or pymupdf). Then read ALL page screenshots — each page image costs ~1,600 tokens so a 15-page paper is only ~24K tokens. You MUST read every page. The ONLY exception is if all page images would not fit in your remaining context — in that case, read as many as fit and state which pages you are skipping and why. Check every page for layout issues, overlapping figures, cut-off text, bad spacing, formatting problems. Fix issues and recompile.
TODO 6. FINAL READ: Check page count (`pdfinfo paper.pdf` or pymupdf). Read entire paper.pdf — check for missing sections, unclear explanations, inconsistencies, typos. Fix and recompile. The ONLY exception is if all pages would not fit in your remaining context — in that case, read as many pages as fit and state which pages you are skipping and why.
</todos>

---

Output the result as JSON to: `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json`

JSON Schema:
```json
{
  "$defs": {
    "FullPaperExpectedFiles": {
      "description": "All expected output files from full paper generation.",
      "properties": {
        "paper_tex_path": {
          "description": "Path to LaTeX source file. Example: 'paper.tex'",
          "title": "Paper Tex Path",
          "type": "string"
        },
        "paper_pdf_path": {
          "description": "Path to compiled PDF. Example: 'paper.pdf'",
          "title": "Paper Pdf Path",
          "type": "string"
        },
        "references_bib_path": {
          "description": "Path to BibTeX bibliography file. Example: 'references.bib'",
          "title": "References Bib Path",
          "type": "string"
        },
        "figure_paths": {
          "description": "Paths to all figure image files. Example: ['figures/fig1_v0.jpg', 'figures/fig2_v0.jpg']",
          "items": {
            "type": "string"
          },
          "title": "Figure Paths",
          "type": "array"
        }
      },
      "required": [
        "paper_tex_path",
        "paper_pdf_path",
        "references_bib_path",
        "figure_paths"
      ],
      "title": "FullPaperExpectedFiles",
      "type": "object"
    }
  },
  "description": "Full paper \u2014 structured output from paper generation.",
  "properties": {
    "title": {
      "description": "Paper title in plain, everyday language \u2014 short and jargon-free so a non-expert grasps it at a glance. Aim for about 4-8 words (~40 characters).",
      "maxLength": 90,
      "minLength": 12,
      "title": "Title",
      "type": "string"
    },
    "summary": {
      "description": "Brief summary of the generated paper: sections written, figures included, compilation status",
      "maxLength": 5000,
      "minLength": 500,
      "title": "Summary",
      "type": "string"
    },
    "out_expected_files": {
      "$ref": "#/$defs/FullPaperExpectedFiles",
      "description": "All output files you created. Must include paper.tex, paper.pdf, references.bib, and paths to all figure files."
    }
  },
  "required": [
    "title",
    "summary",
    "out_expected_files"
  ],
  "title": "FullPaper",
  "type": "object"
}
```

IMPORTANT: this task is NOT complete until `/ai-inventor/aii_data/runs/run_xVr6aECXuY7S/4_gen_paper_repo/_4_assemble_paper/paper/workspace/.sdk_openhands_agent_struct_out.json` exists and contains JSON matching the schema above.
````

### [2] HUMAN-USER prompt · 2026-08-21 20:33:14 UTC

```
What determines whether an open-source project survives its founder stepping away?
```

### [3] SKILL-INPUT — aii-paper-to-latex · 2026-08-21 20:35:03 UTC

The agent loaded the **aii-paper-to-latex** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-paper-to-latex
description: "Assembles and compiles a LaTeX paper into paper.pdf: documentclass and package preamble, figure floats that includegraphics pre-generated vector .pdf and .jpg files, float-placement and width rules, and the required pdflatex, bibtex, pdflatex, pdflatex run sequence. Use whenever pre-written text and pre-generated figures must become a compiled PDF, and whenever a build misbehaves — citations printing as question marks, figures drifting to the end or above the title, shrunken axis labels, undefined references. Triggers: latex, tex, pdflatex, bibtex, natbib, includegraphics, figure float, htbp, compile or build the paper, paper.tex, paper.pdf. NOT for: writing the paper's text or deciding its structure (use aii-paper-writing), creating the figure images (aii-data-fig-gen, aii-concept-fig-gen), or fetching bibliography entries (use aii-semscholar-bib); NOT for reshaping a PDF that already exists — merging, splitting, form filling, table extraction (use anthropic-pdf)."
---

## LaTeX Paper Assembly

Assembles a research paper from paper text, pre-generated figures (vector `.pdf` for data figures, `.jpg` for concept figures) and a bibliography into a compiled PDF.

### Document Setup

```latex
\documentclass[11pt,letterpaper]{article}
\usepackage{graphicx, geometry, amsmath, hyperref, natbib, booktabs, xcolor, listings}
\geometry{margin=1in}
\hypersetup{colorlinks=true, linkcolor=black, citecolor=black, urlcolor=black}
```

### Figure Inclusion

CRITICAL: Include ALL figures. Every figure MUST appear in the paper.

```latex
\begin{figure}[!htbp]
  \centering
  \includegraphics[width=0.92\textwidth,keepaspectratio]{figures/filename.pdf}
  \caption{Descriptive caption.}
  \label{fig:label}
\end{figure}
```

Rules:
- ALWAYS `[!htbp]` — all four options, so a float can never be deferred to the end of the
  document, which `[t]` or `[h]` alone risks. Do not ask for a page TOP: `[!t]` and
  `[!tbp]` both floated a figure ABOVE the paper's own title on page 1, where `[!htbp]`
  on the same document did not. Where a figure lands is decided by where it is declared
  in the text
- Use `figure`, never `figure*`. This document class is ONE column, so `figure*` is exactly
  as wide as `figure` (469.76pt either way) and gains nothing, while restricting the float
  to a page top
- ALWAYS constrain with `width` and `keepaspectratio`. Add `height` only as a
  LAST RESORT against a very tall figure overrunning the page, and keep it
  generous — `0.85\textheight`. A tight height cap binds on ordinary figures
  and LaTeX then shrinks the TEXT with them: at `0.4\textheight` a square
  figure printed at 50.9%, putting 11 pt axis labels on the page at 5.6 pt.
  The figure generator measures legibility at the figure's OWN size, so it
  cannot see this happen
- Every figure needs `\caption`, `\label`, and a `\ref` in the text
- Do NOT convert figures to tables or describe them without inserting the image
- Do NOT skip any figures

### Compilation Process

Run each command separately (do NOT chain with `&&` — pdflatex often exits non-zero on warnings, which would skip bibtex and leave citations as `??`):

```bash
pdflatex -interaction=nonstopmode paper.tex
bibtex paper
pdflatex -interaction=nonstopmode paper.tex
pdflatex -interaction=nonstopmode paper.tex
```

All four commands are required. Skipping bibtex causes `??` in all citations.
Fix any errors between runs. Verify `./paper.pdf` was created.

### Output Files

- `./paper.tex` — LaTeX source
- `./references.bib` — bibliography file
- `./paper.pdf` — compiled PDF
- `./figures/` — all figure images (pre-generated, copied into workspace). Data
  figures are `.pdf` (vector — LaTeX renders their text at page resolution, which
  is what keeps axis labels sharp in print); concept figures are `.jpg`. Use each
  file's OWN extension in `\includegraphics`; there is no conversion step.
````

### [4] SKILL-INPUT — aii-web-research-tools · 2026-08-21 20:38:25 UTC

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

### [5] SKILL-INPUT — aii-semscholar-bib · 2026-08-21 20:39:27 UTC

The agent loaded the **aii-semscholar-bib** skill; its `SKILL.md` (the instructions injected into the agent's context) follows verbatim.

````
---
name: aii-semscholar-bib
description: "Fetches real BibTeX entries in one batch from Semantic Scholar by DOI, ArXiv ID or title via aii_semscholar_bib__fetch, normalises citation keys to AuthorYYYY, injects DOIs, and writes the result into references.bib, with a mandatory web-search fallback for anything not found. ALWAYS use whenever a bibliography, reference list or .bib file is being built or extended, and whenever a citation needs a verified entry instead of an invented one — never hand-write BibTeX first. Triggers: bibliography, references.bib, bibtex, citation key, DOI, arXiv id, Semantic Scholar, reference list, cite these papers, natbib entries. NOT for: writing the text around the citations (use aii-paper-writing), running bibtex and compiling (use aii-paper-to-latex), judging whether cited work supports the claims (use amg-paper-verification), or open-ended literature search and PDF mining (use aii-web-tools)."
---

## Tool: `aii_semscholar_bib__fetch`

Batch-fetch BibTeX entries from Semantic Scholar. Pass all references in a single call — the tool handles batching internally.

### How it works

1. **DOI/ArXiv refs** → batched into POST /paper/batch calls (up to 500 per API call, auto-chunked)
2. **Title-only refs** → individual GET /paper/search/match (1s delay between)
3. **Post-process** → fix entry type, fix citation key (AuthorYYYY), inject DOI

The ability server runs a single worker (`max_threads: 1`). Multiple concurrent tool calls are queued — each runs independently (no cross-request aggregation). Batching happens within each request.

### Input format

```json
{
  "references": [
    {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
    {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
    {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
  ]
}
```

Each reference object can have:
- `doi` — DOI string (ArXiv DOIs like `10.48550/arXiv.XXXX.XXXXX` auto-convert to ArXiv IDs)
- `arxiv` — ArXiv ID (e.g. `"2305.14325"`)
- `title` — Paper title (used for search/match when no DOI/ArXiv)
- `author` — First author last name (for cleaner citation key)
- `year` — Publication year (int, for citation key)

At least one of `doi`, `arxiv`, or `title` is required per reference.

### Output format

```json
{
  "success": true,
  "bib_text": "@inproceedings{Vaswani2017, ...}\n\n@article{Wei2022, ...}",
  "total": 3,
  "found": 3,
  "failed_count": 0,
  "entries": [{"citation_key": "Vaswani2017", "bibtex": "...", "title": "...", "doi": "...", "arxiv": ""}],
  "failed": []
}
```

### Workflow

1. Collect DOIs, ArXiv IDs, or titles for all papers you need to cite
2. Call `aii_semscholar_bib__fetch` with the full list in **one call**
3. Save `bib_text` from the response to your `references.bib` file
4. Check `failed` — for any missed papers, follow the **fallback procedure** below

### Fallback for failed references (MANDATORY)

NEVER fabricate BibTeX. For each failed reference:
1. **WebSearch** for `"Title" author year` (try `site:arxiv.org` too)
2. **WebFetch** the paper page → extract title, authors, year, venue, DOI/ArXiv ID
3. If DOI/ArXiv found → retry `aii_semscholar_bib__fetch` with it
4. Last resort: write BibTeX by hand using **only verified info from the actual paper page**

---

### CLI (for manual use / debugging)

```bash
SKILL_DIR="$(git rev-parse --show-toplevel 2>/dev/null || echo /ai-inventor)/.claude/skills/aii-semscholar-bib" && \
$SKILL_DIR/../.ability_client_venv/bin/python $SKILL_DIR/scripts/aii_semscholar_bib__fetch.py --refs '[
  {"doi": "10.48550/arXiv.1706.03762", "author": "Vaswani", "year": 2017},
  {"arxiv": "2201.11903", "author": "Wei", "year": 2022},
  {"title": "Tree of Thoughts", "author": "Yao", "year": 2023}
]'
```

`--json, -j` — output raw JSON instead of .bib text

**If the script fails** with a connection error (ability server not running): create a local `.venv`, install server deps from `server_requirements.txt` into it, then import the `@aii_ability` function from the script and call it directly — bypassing the server:
```bash
uv venv .venv --python=3.12 && uv pip install --python=.venv/bin/python -r "$SKILL_DIR/scripts/server_requirements.txt"
```
````

### [6] SYSTEM-USER prompt · 2026-08-21 20:40:12 UTC

```
<validation-feedback>
Attempt 1 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```

### [7] SYSTEM-USER prompt · 2026-08-21 20:41:57 UTC

```
<validation-feedback>
Attempt 2 failed validation.

The output file `.sdk_openhands_agent_struct_out.json` does not exist yet. Produce it as JSON matching the schema.

Produce `.sdk_openhands_agent_struct_out.json` again so it contains corrected JSON that matches the schema. Do not invent new fields.
</validation-feedback>
```
