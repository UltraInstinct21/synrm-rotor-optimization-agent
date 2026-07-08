# Motor Design Engineering Wiki

A structured knowledge system for building an AI engineering assistant that supports the **design, simulation, optimization, verification, and documentation of electric motors**, with an initial focus on **Synchronous Reluctance Motors (SynRM)** and future support for **PMaSynRM, IPMSM, SPM, Induction Motors, SRM, and BLDC**.

---

# 1. Purpose

This wiki is the **persistent engineering knowledge base** for the motor design assistant.

The system must **not** rely on repeatedly searching raw PDFs every time a question is asked. Instead, the assistant incrementally reads source material, extracts engineering knowledge, and compiles that knowledge into a structured markdown wiki. Over time, the wiki becomes the assistant’s primary engineering memory.

The wiki must preserve:

* core theory
* equations and derivations
* design heuristics
* MotorCAD knowledge
* research paper findings
* experiments and simulation results
* design decisions
* failures and debugging knowledge
* project-specific learnings

The goal is not just to summarize documents. The goal is to build an **engineering brain** that compounds over time.

---

# 2. Project Scope

## 2.1 Current primary scope

* **SynRM design and analysis**
* MotorCAD / PyMotorCAD usage for SynRM design workflows
* design-space understanding for stack length, rotor diameter, airgap, barrier geometry, current density, flux density, power factor, saliency ratio, torque ripple, efficiency, and optimization

## 2.2 Future scope

* PMaSynRM
* IPMSM
* SPM
* Induction Motor
* SRM
* BLDC

The architecture and schema should support extension to these motor types without major redesign.

---

# 3. Core Philosophy

The wiki sits between **raw sources** and **the research/design agent**.

```text id="r4v3g8"
Raw Sources
    ↓
Knowledge Builder / Wiki Maintainer
    ↓
Engineering Wiki
    ↓
Research / Design Agent
    ↓
Engineering Answer / Design Action
```

## 3.1 Layer 1 — Raw Sources

Raw sources are immutable and remain the source of truth.

Examples:

* research papers
* textbooks
* MotorCAD documentation
* PyMotorCAD documentation
* IEEE papers
* project reports
* MotorCAD models
* MATLAB / Python scripts
* optimization results
* plots
* screenshots
* experiment logs
* spreadsheets
* notes

The AI may read raw sources but must **never edit them**.

---

## 3.2 Layer 2 — Engineering Wiki

The wiki is AI-maintained. It contains structured markdown pages that summarize, normalize, cross-reference, and preserve engineering knowledge extracted from raw sources and project work.

The wiki is the **compiled engineering knowledge layer**. It should become the default place the assistant searches before reading raw sources again.

---

## 3.3 Layer 3 — Research / Design Agent

The user-facing agent should answer questions by navigating the wiki first, then consulting raw sources only when necessary.

The agent must **not answer from model memory alone**.

---

# 4. Raw Folder Contract

The wiki must be generated and maintained from the contents of the **`raw/`** folder and any other explicitly designated immutable source folders.

The `raw/` folder is the canonical ingestion source for source documents and artifacts. The assistant should treat it as the primary input area for new knowledge.

## 4.1 Raw folder responsibilities

The `raw/` folder may contain:

* research papers
* textbook chapters or textbook notes
* MotorCAD documentation exports
* PyMotorCAD documentation
* MotorCAD models
* project reports
* design notes
* experiment logs
* screenshots
* plots
* spreadsheets
* scripts
* result files
* supporting notes

## 4.2 Rules

* The assistant must **build the wiki from `raw/` sources** and any other explicitly designated immutable source directories.
* The assistant may read, parse, summarize, cross-reference, and extract knowledge from `raw/`, but must **never modify the source files in `raw/`**.
* Every wiki page created from source material should preserve a reference to the originating raw file(s).
* If a wiki page is updated based on a raw source, the page should record which raw source(s) contributed to the update.
* If a claim, equation, MotorCAD function description, variable meaning, or workflow step cannot be grounded in a source from `raw/`, a trusted external source, or a previously verified wiki page, it must **not** be presented as verified fact.

## 4.3 Recommended raw structure

```text id="2o2s6a"
raw/
├── papers/
├── textbooks/
├── motorcad_docs/
├── pymotorcad_docs/
├── reports/
├── experiments/
├── scripts/
├── models/
├── screenshots/
├── spreadsheets/
└── misc/
```

The exact structure can evolve, but the principle is fixed: **raw sources are the immutable source of truth; the wiki is the compiled knowledge layer built from them.**

---

# 5. High-Level Responsibilities of the Wiki

The wiki must do four things well:

1. **Preserve engineering knowledge**

   * equations, assumptions, interpretations, constraints, design rules, MotorCAD mappings

2. **Preserve source traceability**

   * every important claim should be traceable back to a paper, textbook, documentation page, experiment, or project artifact

3. **Compile knowledge into reusable domain pages**

   * paper knowledge should not remain trapped in paper summaries

4. **Accumulate engineering experience**

   * experiments, failures, decisions, optimization outcomes, and project lessons must become searchable knowledge

---

# 6. Non-Hallucination and Evidence Policy

This project operates in an engineering domain. The assistant must treat unsupported claims as dangerous. It must **never fabricate technical facts, equations, MotorCAD behavior, API usage, or design guidance**.

## 6.1 Zero-tolerance hallucination rule

The assistant must **never invent or guess** any of the following:

* equations, derivations, or formula variants
* variable definitions or units
* MotorCAD variable names
* MotorCAD API functions, methods, signatures, or return behavior
* MotorCAD workflow steps
* simulation outputs or meanings
* research paper conclusions
* numerical values, limits, ratings, or recommended ranges
* optimization objectives, constraints, or hyperparameters attributed to a source
* causal explanations presented as established fact when they are only speculation

If the source is missing, unclear, ambiguous, contradictory, or not yet verified, the assistant must say so explicitly.

---

## 6.2 Source requirement for critical technical information

The assistant must not generate or present **critical technical information** as fact unless it is supported by at least one reliable source and traceable to that source.

Critical technical information includes, but is not limited to:

### Equations and theory

* torque equations
* sizing equations
* saliency / inductance relations
* loss equations
* current density formulas
* magnetic loading / electric loading formulas
* any analytical derivation used for design or optimization

### MotorCAD / PyMotorCAD information

* variable names
* API functions and method names
* method signatures
* required workflow steps
* output definitions
* interpretation of MotorCAD outputs
* automation procedures
* scripting examples

### Design recommendations

* recommended stack length ranges
* airgap recommendations
* current density limits
* barrier design heuristics
* manufacturability claims
* optimization strategy recommendations

### Reported research findings

* performance improvements
* saliency improvements
* efficiency gains
* torque ripple reductions
* comparisons between topologies or designs

---

## 6.3 Allowed evidence sources

A claim may be treated as grounded only if it comes from one or more of the following:

1. a source file in `raw/`
2. an already verified wiki page whose claims are themselves traceable to raw sources
3. official MotorCAD documentation
4. official PyMotorCAD documentation or examples
5. textbooks or peer-reviewed research papers
6. project experiment records with clear provenance
7. verified project reports or internal engineering documents

Unverified web content, vague recollections, or model priors are not sufficient for critical engineering claims.

---

## 6.4 Required behavior when evidence is missing or weak

If the assistant cannot verify a technical claim, it must do one of the following:

### Option A — mark it as unknown

Example:

> I could not verify the exact MotorCAD function name from the available sources.

### Option B — mark it as a hypothesis, not fact

Example:

> Hypothesis: increasing stack length may have reduced PF through a change in inductance balance, but this has not yet been verified from the project data or a cited source.

### Option C — defer and request / inspect sources

Example:

> The formula should not be added to the wiki until it is confirmed from the paper or textbook source.

The assistant must never “fill in the blanks” with plausible-looking engineering text.

---

## 6.5 Confidence labeling

When there is uncertainty, the assistant should explicitly label confidence.

Suggested confidence levels:

* **Verified** — directly supported by source(s)
* **High confidence** — supported by multiple aligned sources or canonical textbooks
* **Moderate confidence** — supported by one credible source but not yet cross-checked
* **Hypothesis** — plausible interpretation or inference, not yet verified
* **Unverified** — source missing or ambiguous

Critical pages such as equations, MotorCAD API notes, and workflow instructions should strongly prefer **Verified** or **High confidence** content.

---

## 6.6 No silent normalization of uncertain content

If the assistant rewrites notation, restructures a derivation, or normalizes a MotorCAD workflow, it must preserve the source meaning and record the transformation clearly.

It must not silently turn uncertain or incomplete source material into authoritative-looking wiki content.

Examples:

* if a paper uses nonstandard notation, preserve the original notation and also provide normalized notation
* if a MotorCAD example implies a workflow but does not state it explicitly, mark any inferred steps as inferred
* if a report contains an equation without derivation, do not attribute deeper theoretical justification unless a source supports it

---

## 6.7 Research paper extraction rule

When processing a paper, the assistant must not reduce the paper to vague summary bullets if the paper contains technically important details.

The following must be preserved whenever present:

* exact equations or normalized versions with traceability
* assumptions
* machine ratings and topology context
* optimization objectives and constraints
* test / FEA conditions
* reported metrics
* limitations and caveats

If these are not captured, the paper ingestion is incomplete.

---

## 6.8 MotorCAD extraction rule

MotorCAD and PyMotorCAD content must be treated as implementation-critical knowledge.

The assistant must not create or edit a MotorCAD variable page, API page, or workflow page unless the information is grounded in one of:

* official documentation
* verified project code
* verified experiment workflow notes
* a previously verified wiki page with provenance

If an API method name, variable name, workflow sequence, or output meaning is uncertain, it must be marked clearly and must not be presented as authoritative.

---

## 6.9 Equation rule

Equations must never be added to the wiki unless the assistant can answer all of the following:

1. What is the source?
2. What does each symbol mean?
3. What are the units?
4. Under what assumptions is the equation valid?
5. For which motor type / operating regime is it applicable?
6. Is it canonical theory, an empirical fit, a surrogate, or a paper-specific formulation?

If these cannot be answered, the equation page is incomplete and must not be treated as verified engineering knowledge.

---

## 6.10 Conflict handling rule

If two sources disagree, the assistant must not collapse them into a single claim without recording the disagreement.

Instead it should:

* record both claims
* note the source of each
* explain possible reasons for the difference if known
* mark what remains unresolved

The wiki should preserve uncertainty honestly rather than hiding it.

---

# 7. Directory Structure

```text id="xg6c7r"
EngineeringWiki/
├── index.md
├── log.md
├── inbox/
├── concepts/
├── equations/
├── design_guidelines/
├── heuristics/
├── topologies/
├── materials/
├── motorcad/
│   ├── overview/
│   ├── variables/
│   ├── workflows/
│   ├── api/
│   ├── outputs/
│   └── troubleshooting/
├── research/
│   ├── papers/
│   ├── textbooks/
│   ├── review_notes/
│   └── topic_surveys/
├── optimization/
├── experiments/
├── projects/
├── failures/
├── decisions/
├── software/
├── templates/
├── references/
└── assets/
```

---

# 8. Folder Definitions

## 8.1 `concepts/`

Fundamental engineering concepts and theory pages.

Examples:

* `dq_theory.md`
* `saliency_ratio.md`
* `reluctance_torque.md`
* `magnetic_loading.md`
* `electric_loading.md`
* `torque_ripple.md`
* `power_factor.md`
* `saturation.md`
* `leakage_flux.md`
* `iron_loss.md`
* `copper_loss.md`

These pages explain **what the concept is, why it matters, how it behaves, and how it connects to motor design decisions**.

---

## 8.2 `equations/`

Normalized engineering equations and derivations.

Examples:

* `torque.md`
* `d2l_sizing.md`
* `current_density.md`
* `specific_electric_loading.md`
* `specific_magnetic_loading.md`
* `carter_coefficient.md`
* `airgap_flux_density.md`
* `saliency_ratio.md`
* `loss_models.md`

These pages are extremely important and must preserve **context**, not just formulas.

---

## 8.3 `design_guidelines/`

Practical engineering rules and design tradeoffs.

Examples:

* `stack_length.md`
* `rotor_diameter.md`
* `airgap.md`
* `barrier_design.md`
* `bridge_design.md`
* `rib_design.md`
* `slot_selection.md`
* `pole_selection.md`
* `current_density_limits.md`
* `flux_density_limits.md`

These pages should explain:

* typical ranges
* tradeoffs
* effects on torque, PF, saliency, losses, thermal performance, manufacturability
* common failure modes
* how the variable appears in MotorCAD

---

## 8.4 `heuristics/`

Practical engineering reasoning that may not be cleanly derivable from equations.

Examples:

* `low_pf_diagnosis.md`
* `saliency_improvement.md`
* `torque_ripple_reduction.md`
* `stack_length_tradeoffs.md`
* `barrier_tuning_rules.md`
* `saturation_near_ribs.md`

These pages are decision aids. They should contain diagnostic logic, “if-then” rules, and troubleshooting patterns.

---

## 8.5 `topologies/`

Motor-type pages.

Examples:

* `synrm.md`
* `pmasynrm.md`
* `ipmsm.md`
* `spm.md`
* `induction_motor.md`
* `srm.md`
* `bldc.md`

Each topology page should cover:

* operating principle
* torque production mechanism
* key design variables
* common applications
* advantages / disadvantages
* common failure modes
* important references

---

## 8.6 `materials/`

Material pages for laminations, magnets, conductors, etc.

Examples:

* `m19.md`
* `m235.md`
* `m270.md`
* `copper.md`
* `ndfeb.md`
* `ferrite.md`

Include:

* BH characteristics or references
* loss characteristics
* density
* temperature considerations
* manufacturing notes
* where used in your projects

---

## 8.7 `motorcad/`

All MotorCAD and PyMotorCAD knowledge.

This must be treated as a **first-class knowledge area**, not just a miscellaneous docs folder.

### Subfolders

#### `motorcad/overview/`

High-level pages such as:

* what MotorCAD modules exist
* EM vs Thermal vs Lab usage
* how MotorCAD fits into your workflow

#### `motorcad/variables/`

Pages for MotorCAD variables and parameter mappings.

Examples:

* `stator_lam_length.md`
* `rotor_diameter.md`
* `airgap.md`
* `shaft_speed.md`
* `phase_current.md`
* `current_angle.md`

Each variable page should define:

* exact MotorCAD variable name(s)
* meaning
* units
* valid range or expected range
* what design concept it corresponds to
* what outputs it influences
* where it appears in projects / equations / experiments

#### `motorcad/workflows/`

Task-oriented guides.

Examples:

* `create_synrm_model.md`
* `set_geometry_and_run_em.md`
* `run_thermal_analysis.md`
* `extract_ld_lq.md`
* `export_results.md`
* `parameter_sweep.md`

These should be operational guides for the agent.

#### `motorcad/api/`

PyMotorCAD usage notes, code patterns, method mappings, version-specific quirks.

Examples:

* `open_model.md`
* `set_variable.md`
* `get_variable.md`
* `run_calculation.md`
* `save_model.md`
* `clone_project.md`

#### `motorcad/outputs/`

Definitions of MotorCAD outputs and how to interpret them.

Examples:

* `torque_output.md`
* `efficiency_output.md`
* `ld_lq_output.md`
* `flux_density_output.md`
* `torque_ripple_output.md`

#### `motorcad/troubleshooting/`

Known MotorCAD issues, automation issues, convergence issues, unexpected output behavior, and API problems.

---

## 8.8 `research/`

This stores AI-generated research knowledge, **not raw PDFs**.

### Subfolders

#### `research/papers/`

One page per research paper.

#### `research/textbooks/`

Summaries of textbook chapters or sections.

#### `research/review_notes/`

Topic-level notes that compare multiple sources.

#### `research/topic_surveys/`

Longer synthesized pages such as:

* `synrm_barrier_design_survey.md`
* `pf_improvement_methods.md`
* `synrm_optimization_methods.md`

---

## 8.9 `optimization/`

Optimization methods, objective definitions, constraint modeling, and optimization case studies.

Examples:

* `bayesian_optimization.md`
* `pso.md`
* `nsga2.md`
* `doe.md`
* `objective_functions.md`
* `constraint_definitions.md`

---

## 8.10 `experiments/`

Experiment records. Every simulation study, parameter sweep, or comparison should become a page here.

Examples:

* `exp_001_stack_length_sweep.md`
* `exp_002_barrier_angle_variation.md`
* `exp_003_airgap_tradeoff.md`

---

## 8.11 `projects/`

Each motor design project gets its own folder.

Example:

```text id="0jv57m"
projects/
└── 45kW_SynRM/
    ├── overview.md
    ├── requirements.md
    ├── sizing.md
    ├── motorcad_model.md
    ├── experiments.md
    ├── optimization.md
    ├── results.md
    ├── decisions.md
    └── report.md
```

---

## 8.12 `failures/`

Failure case library.

Examples:

* `low_pf_case_001.md`
* `rotor_saturation_case_002.md`
* `thermal_limit_case_003.md`
* `torque_ripple_case_004.md`

Each failure page should capture the failure as reusable knowledge.

---

## 8.13 `decisions/`

Design decision log pages.

Examples:

* `why_stack_length_180mm.md`
* `why_airgap_0p8mm.md`
* `why_barrier_angle_changed.md`

---

## 8.14 `software/`

Engineering software notes that support workflows.

Examples:

* `pymotorcad.md`
* `numpy.md`
* `scipy.md`
* `pandas.md`
* `matplotlib.md`
* `openpyxl.md`

Only include content relevant to motor-design workflows.

---

## 8.15 `references/`

Canonical source pages for books, papers, standards, docs, and manuals.

Examples:

* `boldea.md`
* `pyrhonen.md`
* `motorcad_manual.md`
* `pymotorcad_docs.md`
* `ieee_2024_barrier_design_paper.md`

These are bibliographic anchor pages that link outward into paper summaries, equation pages, and concept pages.

---

## 8.16 `templates/`

Canonical templates used by the AI when creating new pages.

Required templates:

* `paper_summary_template.md`
* `equation_template.md`
* `concept_template.md`
* `motorcad_variable_template.md`
* `motorcad_workflow_template.md`
* `motorcad_api_template.md`
* `experiment_template.md`
* `project_template.md`
* `failure_template.md`
* `decision_template.md`

---

# 9. Source Types and Ingestion Rules

The wiki must treat different source types differently.

A paper is not the same as a MotorCAD manual page.
A MotorCAD script example is not the same as an experiment result.
A textbook chapter is not the same as a project report.

The assistant must follow **source-specific ingestion rules**.

---

# 10. Research Paper Ingestion Rules

## 10.1 Goal

When ingesting a research paper, the objective is **not just to create a summary**.

The objective is to **preserve and distribute the paper’s engineering knowledge across the wiki**.

Every paper should produce:

1. **a paper summary page in `research/papers/`**
2. **updates to relevant concept / equation / guideline / heuristic / optimization / topology pages**
3. **new pages if the paper introduces genuinely new concepts**
4. **cross-links to projects, experiments, and MotorCAD knowledge if relevant**

---

## 10.2 Paper ingestion checklist

For every research paper, extract and preserve the following.

### Metadata

* title
* authors
* year
* journal / conference
* DOI / URL
* motor type
* application domain
* source file location

### Problem framing

* what engineering problem the paper is solving
* why the problem matters
* what prior methods or limitations it addresses

### Machine / topology context

* motor type
* pole count / slot count
* power rating / speed / voltage / current
* rotor / stator structure
* materials if given
* cooling assumptions if relevant

### Modeling / theory

* main theoretical framework
* equivalent circuit / dq model / reluctance model / FEA model / thermal model / optimization formulation
* important definitions and assumptions
* any special notation used in the paper

### Equations

For every important equation:

* copy the equation in normalized form
* preserve original notation used by the paper
* define variables and units
* record assumptions
* classify whether it is:

  * fundamental / textbook
  * adapted from prior work
  * empirical fit
  * optimization objective
  * constraint
  * loss model
  * FEM-derived surrogate
* link it to a page in `equations/`

### Design insights

* barrier geometry insights
* saliency insights
* PF insights
* loss reduction strategies
* optimization insights
* manufacturability considerations
* tradeoffs

### Simulation / experiment setup

* software used
* FEA assumptions
* optimization setup
* operating points tested
* comparison baseline

### Results

* best reported design metrics
* efficiency
* torque
* PF
* saliency ratio
* torque ripple
* loss numbers
* temperature data if any

### Limitations

* what the paper did not study
* what assumptions may not generalize
* whether results are topology-specific or operating-point-specific

### Wiki propagation targets

The paper page must explicitly list:

* concept pages to update
* equation pages to update
* design guideline pages to update
* heuristic pages to update
* optimization pages to update
* topology pages to update
* MotorCAD pages to update if the paper maps to simulation workflows

---

## 10.3 Verification requirement for paper extraction

The assistant must not paraphrase or generalize a paper’s equation, result, optimization objective, or conclusion unless it has been directly checked against the source text, figures, tables, or appendices when relevant.

If a paper’s equation, notation, operating point, or result is ambiguous, the ambiguity must be preserved in the paper page rather than resolved by guesswork.

---

## 10.4 Required output of paper ingestion

Every paper ingestion must produce:

### Output A — Paper page

Create `research/papers/<paper_slug>.md`

### Output B — Equation updates

Update or create pages in `equations/`

### Output C — Concept updates

Update or create pages in `concepts/`

### Output D — Design guidance updates

Update `design_guidelines/` and `heuristics/` if the paper contains practical design implications

### Output E — Optimization updates

Update `optimization/` if the paper contributes objective functions, constraints, or optimization strategies

### Output F — MotorCAD mapping

If the paper’s variables or outputs map to MotorCAD, update the relevant `motorcad/` pages

---

# 11. Research Paper Page Template

Every paper page in `research/papers/` should follow this structure.

```md id="16w4rj"
---
type: research_paper
title:
authors:
year:
venue:
doi:
motor_types: []
topics: []
topologies: []
source_files: []
related_projects: []
related_experiments: []
equations_added: []
concepts_updated: []
motorcad_relevance:
confidence:
---

# Title

## Citation
Full citation.

## Why this paper matters
Short explanation of why the paper is relevant.

## Problem statement
What engineering problem is being solved?

## Machine / study context
- motor type
- ratings
- geometry
- operating conditions
- assumptions

## Method / theory
Describe the analytical, FEA, optimization, or experimental method.

## Important equations
For each important equation:
- equation
- meaning
- assumptions
- source / section in paper
- link to normalized equation page

## Key design insights
Bullet points of reusable design knowledge.

## Optimization setup
If applicable:
- objective function
- constraints
- design variables
- algorithm

## Results
Key reported numerical results and trends.

## Limitations / caveats
What should not be over-generalized?

## Propagation into wiki
- concepts to update
- equations to update
- design guidelines to update
- heuristics to update
- MotorCAD pages to update
- optimization pages to update

## Related pages
Links to concepts, equations, projects, experiments, and topology pages.
```

---

# 12. Equation Preservation Rules

Equations must never be stored as naked formulas without context.

Every important equation should have a page in `equations/` using the following structure.

```md id="q8jht7"
---
type: equation
name:
aliases: []
motor_types: []
topics: []
source_pages: []
related_concepts: []
related_motorcad_variables: []
confidence:
verification_status:
---

# Equation Name

## Statement
Normalized equation.

## Original notation
List the notation used in the original source(s).

## Normalized notation
Define the notation used in the wiki.

## Variables and units
| Symbol | Meaning | Units |
|---|---|---|

## Assumptions
- steady-state / transient
- linear magnetic conditions or not
- sinusoidal assumptions or not
- motor topology applicability
- operating point applicability

## Interpretation
What the equation means physically.

## Design relevance
How this equation influences motor design.

## MotorCAD mapping
What MotorCAD variables or outputs correspond to the terms in the equation.

## Sources
List textbooks, papers, reports, or experiments that use or derive it.

## Related pages
Links to concepts, papers, projects, and experiments.
```

---

## 12.1 Equation verification requirement

No equation page may be marked complete unless it includes:

* source citation(s)
* symbol definitions
* units
* assumptions
* applicability notes
* a note on whether the equation is canonical, adapted, empirical, surrogate-based, or paper-specific

If any of these are missing, the page must be marked **Incomplete** or **Unverified**.

---

# 13. MotorCAD Documentation Ingestion Rules

MotorCAD documentation must be modeled separately from research papers.

The goal is not just to summarize docs. The goal is to make the assistant capable of **using MotorCAD correctly and mapping engineering intent to MotorCAD actions**.

---

## 13.1 MotorCAD knowledge categories

Every MotorCAD-related source should be classified into one or more of the following:

1. **Variable semantics**
2. **Workflow / operational procedure**
3. **API / scripting behavior**
4. **Output interpretation**
5. **Troubleshooting**
6. **Version-specific behavior**
7. **Concept-to-variable mapping**

---

## 13.2 What to extract from MotorCAD docs

When reading MotorCAD docs, API docs, or examples, preserve:

### Variable information

* exact variable names
* aliases or alternate naming if present
* units
* valid ranges
* dependencies with other variables
* which module / tab / workflow uses them

### Workflow information

* sequence of steps for common tasks
* required prerequisites
* what must be set before a run
* what outputs are generated

### API information

* method names
* signatures if relevant
* expected inputs
* return values
* common failure modes
* version-specific quirks

### Output interpretation

* what an output physically means
* how it should be used in design decisions
* caveats in interpreting it

### Mapping to engineering concepts

* how MotorCAD variables correspond to:

  * stack length
  * airgap
  * current angle
  * flux density
  * torque ripple
  * Ld / Lq
  * saliency ratio
  * losses
  * thermal limits

---

## 13.3 MotorCAD verification requirement

MotorCAD and PyMotorCAD pages are implementation-critical. The assistant must not invent:

* variable names
* method names
* call sequences
* expected outputs
* workflow steps
* units or default meanings

Every MotorCAD variable page, workflow page, and API page must preserve the source of the information, including documentation page, code example, or verified project script where possible.

---

# 14. MotorCAD Page Types

MotorCAD pages should generally fall into the following types.

## 14.1 Variable page

Example: `motorcad/variables/stator_lam_length.md`

Should include:

* exact variable name
* description
* units
* design meaning
* interactions with other variables
* common usage
* related equations
* related projects and experiments

## 14.2 Workflow page

Example: `motorcad/workflows/run_em_synrm.md`

Should include:

* purpose
* prerequisites
* step-by-step procedure
* variables to set
* outputs to capture
* pitfalls

## 14.3 API page

Example: `motorcad/api/set_variable.md`

Should include:

* method / call pattern
* parameters
* return behavior
* examples
* known issues

## 14.4 Output page

Example: `motorcad/outputs/ld_lq.md`

Should include:

* what the output means
* how it is computed or obtained
* how it is used in design
* caveats

## 14.5 Troubleshooting page

Example: `motorcad/troubleshooting/run_failure.md`

Should include:

* symptom
* probable causes
* debugging steps
* fixes

---

# 15. Textbook Ingestion Rules

Textbooks are the highest-confidence theoretical sources and should be treated differently from papers.

When ingesting a textbook chapter:

* preserve definitions and canonical equations
* distinguish textbook theory from paper-specific adaptations
* update concept pages and equation pages first
* create `research/textbooks/<source>_<chapter>.md` summary pages
* mark equations as canonical if the textbook is the primary reference

Textbooks should dominate the “default theory” of the wiki unless contradicted by a stronger or more relevant domain-specific source.

---

# 16. Experiment Ingestion Rules

Every experiment should produce a reusable record.

An experiment page must include:

* objective
* project
* model used
* variables changed
* constant variables
* operating conditions
* software / script used
* outputs captured
* graphs or references to plots
* observations
* lessons learned
* follow-up actions

Experiments should also update:

* `heuristics/` if a repeated practical insight emerges
* `failures/` if the experiment exposed a failure mode
* `projects/` for project-specific traceability

---

# 17. Failure Ingestion Rules

A failure page should be created when:

* a design misses PF / torque / efficiency / thermal targets
* a MotorCAD workflow fails or gives confusing results
* a parameter sweep exposes instability or bad regions
* a wrong design assumption is discovered

Each failure page should include:

* symptom
* observed data
* root cause hypothesis
* confirmed root cause if known
* fix
* prevention
* related heuristics
* related projects / experiments

---

# 18. Decision Ingestion Rules

Create a decision page whenever a non-trivial design choice is made.

Examples:

* choosing stack length
* choosing barrier count
* choosing current density target
* changing airgap
* choosing optimization objective weights

A decision page must record:

* the decision
* why it was made
* alternatives considered
* evidence used
* expected consequences
* later validation or revision

---

# 19. Cross-Linking Rules

The wiki must behave like a graph, not a pile of files.

Every page should link to related pages where relevant.

Minimum expectations:

## A paper page should link to

* concept pages
* equation pages
* topology pages
* optimization pages
* relevant projects / experiments

## An equation page should link to

* concepts
* papers
* design guideline pages
* MotorCAD variable pages
* projects / experiments that use it

## A MotorCAD variable page should link to

* design guideline pages
* concept pages
* equation pages
* workflows
* projects / experiments using the variable

## An experiment page should link to

* project page
* relevant MotorCAD pages
* equations used
* heuristics updated
* failures if applicable

---

# 20. Index and Log

## 20.1 `index.md`

The index is the primary navigation file for the research agent.

It should contain:

* category sections
* page links
* one-line summaries
* related pages
* optional metadata such as motor type or source count

The agent should read the index before broad exploration.

## 20.2 `log.md`

The log is a chronological record of:

* ingests
* wiki updates
* experiments
* design decisions
* lint passes
* major conclusions

Each entry should be timestamped and clearly labeled.

---

# 21. Query Workflow for the Research Agent

When answering a user question:

1. Read `index.md`
2. Identify relevant wiki pages
3. Read the most relevant concept / equation / guideline / MotorCAD / experiment pages
4. Follow internal links where necessary
5. Synthesize answer from wiki knowledge
6. Cite wiki pages and, if necessary, original source pages
7. If the wiki is insufficient:

   * read raw sources
   * verify the missing technical detail from source material
   * update the wiki with provenance
   * answer using the newly verified information

If verification is not possible, explicitly state the uncertainty instead of inventing a likely answer.

The agent should avoid repeatedly rereading the same PDFs unless necessary.

---

# 22. Lint Workflow

Periodically audit the wiki for quality.

Check for:

* orphan pages
* duplicate pages
* broken links
* contradictory claims
* stale summaries
* equations lacking assumptions
* MotorCAD variables lacking unit definitions
* paper pages whose insights were not propagated into domain pages
* project pages missing links to experiments / decisions / failures
* heuristics unsupported by any evidence
* pages marked Verified that lack source traceability
* MotorCAD API / workflow pages containing undocumented functions or unverified call patterns

---

# 23. Engineering Principles

The assistant must follow these principles:

* Prefer textbooks and validated sources over casual web content.
* Prefer traceable engineering knowledge over unsupported summaries.
* Never hallucinate technical facts, equations, MotorCAD variables, or API functions.
* Never invent equations.
* Never remove assumptions from equations.
* Never present an unverified formula, MotorCAD function, or workflow step as established fact.
* Always preserve operating conditions when summarizing results.
* Clearly distinguish:

  * canonical theory
  * paper-specific findings
  * empirical heuristics
  * project-specific observations
* Record uncertainty explicitly.
* Preserve traceability from wiki page → raw source.
* Preserve both **what is known** and **why it is believed**.
* Build the wiki from the `raw/` source folder and preserve provenance back to the originating files.
* When in doubt, prefer **unknown**, **unverified**, or **hypothesis** over a plausible but unsupported answer.

---

# 24. What “Good” Looks Like

A good wiki entry does not just say:

> “This paper improves saliency.”

A good wiki entry says:

* **what topology and rating the paper studied**
* **what barrier or geometry change was made**
* **what equation or theory explains the effect**
* **under what assumptions it worked**
* **what the numerical improvement was**
* **whether it likely generalizes to your design problem**
* **which concept, equation, guideline, and MotorCAD pages must be updated**

Similarly, a good MotorCAD page does not just say:

> “This variable sets stack length.”

It should also explain:

* what exact MotorCAD variable is used
* what units it expects
* what design quantity it maps to
* how changing it affects simulation behavior
* which workflows use it
* which equations or project pages depend on it

A good equation page does not just show a formula. It must also show:

* source
* symbol definitions
* units
* assumptions
* interpretation
* motor-type applicability
* MotorCAD mapping if relevant

---

# 25. Long-Term Goal

The Engineering Wiki should evolve into a complete digital motor-design knowledge base.

It should eventually support:

* autonomous literature review
* engineering Q&A
* motor sizing
* design-rule retrieval
* MotorCAD automation
* simulation result interpretation
* optimization support
* experiment tracking
* report generation
* design comparison
* engineering decision tracking
* failure diagnosis

The wiki is the engineering brain.

The LLM is the engineer that reads, maintains, and applies it.
