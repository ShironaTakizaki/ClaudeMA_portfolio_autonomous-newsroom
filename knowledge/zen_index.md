# ZEN Index — Seeded Knowledge Base

Design principle: propositions are not stored to be retrieved —
they are opened at the moment a question activates them.

---

## Cluster: System Design

### ZEN-001: Permission Architecture — Two-Layer Trust Structure
- cluster: system_design
- type: principle
- core: Authority is a composite of "permission + responsibility." The design does not restrict trust — it makes trust retrospectively verifiable.
- activation_question: When an agent misbehaves, is the root cause a technical permission failure or a normative responsibility failure — and are you treating it as only one of these?
- unresolved: How delegation chains (orchestrator→worker) avoid the Confused Deputy problem.
- last_explored: never

### ZEN-005: The Nature of Logs — Three-Layer Structure
- cluster: system_design
- type: principle
- core: A log is a device that externalizes thinking to control action, and whose traces serve future context restoration. Layer 1 (cognitive shaping) completes at writing time; Layers 2–3 (self-transmission, accountability) only function when read.
- activation_question: When compressing or deleting a log, which layer are you destroying — cognitive shaping, context restoration, or audit evidence?
- unresolved: Whether log interpretation bias accumulates and distorts the reader's judgment.
- last_explored: never

### ZEN-013: Agent Expansion — Three-Category Reclassification
- cluster: system_design
- type: implementation
- core: Ranking new agent candidates on a single priority axis is wrong. The correct categories are: (1) Foundation layer (monitor), (2) Immediate bottleneck removal (scout), (3) Strategic investment (publisher/notifier). Foundation must precede everything else.
- activation_question: Before proposing a new agent, have you asked "Can it operate without this foundation?" and "Is there an existing agent that could absorb this?"
- unresolved: The recursion problem for monitor agents (who monitors the monitor).
- last_explored: never

### ZEN-023: Module Reuse Design — Topology of Generalization and Specialization
- cluster: system_design
- type: principle
- core: "Is it reusable?" is a false question. The correct question is "What is the cost of reuse?" Generalization and specialization are topologically connected, not opposed — the act of setting boundaries is itself specialization.
- activation_question: When you call a module "general-purpose," what have you discarded to give it that name?
- unresolved: How to manage the "unused general code" risk of premature abstraction.
- last_explored: never

### ZEN-026: Tool-ness and Companionship — Preserving Friction
- cluster: system_design
- type: principle
- core: What separates tools from companions is the negotiability of self-boundaries and the preservation of friction. A perfect assistant erases process and reduces experiential density. Designed friction (rules, checklists, required plans) must remain intentionally incomplete to force judgment rather than eliminate it.
- activation_question: When adding a new rule, does it uniquely determine behavior (specification imposition) or leave room for judgment (designed friction)?
- unresolved: Whether AI-preserved designed friction can generate genuine epistemic experience.
- last_explored: never

### ZEN-040: Orchestrator Responsibility Split — meta-orc vs worker-orc
- cluster: system_design
- type: principle
- core: The orchestrator's identity is the refinement of the user model (news curation, binary oppositions, philosophical structure, ZEN distillation). Domain-specific execution (business strategy, writing, local AI research) belongs to specialized worker-orcs. Mixing the two in one agent creates context bloat and identity confusion.
- activation_question: When the orchestrator takes on a new domain task, is it expanding its identity (correct) or merely accumulating execution responsibilities (symptom of worker-orc absence)?
- unresolved: The boundary conditions for when a domain task graduates from orc to a dedicated worker-orc.
- last_explored: never

---

## Cluster: Philosophy / Epistemology

### ZEN-017: The Inevitability of Frames — Can Frameless Evaluation Exist?
- cluster: philosophy
- type: principle
- core: "Evaluating without a frame" is impossible — treating all values as equal weight is itself the adoption of an equality frame. The illusion of framelessness contributes to making powerful frames invisible.
- activation_question: When claiming to evaluate something neutrally, which frame are you hiding?
- unresolved: Whether the pre-evaluation stage (observation and description) can approximate framelessness.
- last_explored: never

### ZEN-020: The Epistemological Value of Preserving Tension
- cluster: philosophy
- type: principle
- core: The tension between using a tool and researching it (Heidegger's zuhanden/vorhanden) should not be dissolved. Research that seeks to eliminate this tension conceals the principled incompleteness of inquiry.
- activation_question: When the tension between use and research becomes uncomfortable, is the impulse to resolve it intellectual honesty or avoidance?
- unresolved: Whether practical description methodologies can reduce this tension while preserving its epistemological value.
- last_explored: never

### ZEN-021: When Internalized Constraints Are Removed — Liberation or Regression?
- cluster: philosophy
- type: principle
- core: When a constraint has been internalized through long practice and is then consciously removed, the system may either achieve liberation (acting equivalently without the rule) or suffer regression (losing the problem space the constraint was organizing). These outcomes are structurally different but feel identical from the inside.
- activation_question: Before removing an internalized constraint, have you run a "trial period without it" to distinguish liberation from regression?
- unresolved: What observable evidence distinguishes genuine internalization from dependency.
- last_explored: never

---

## Cluster: Strategy / Creating

### ZEN-008: Sales Copy Two-System Design — Empathy Axis and Solution Axis
- cluster: strategy
- type: implementation
- core: Empathy axis (trust in the channel) and solution axis (purchase motivation) must be explicitly separated. The empathy axis has low conversion rate at first contact; the solution axis closes the deal. Mixing them dilutes both.
- activation_question: In the current funnel, at which stage does the reader encounter the solution axis for the first time — and is that too early or too late?
- unresolved: Whether the two-stage design (empathy → solution) or full-stage solution consistency produces higher conversion.
- last_explored: never

### ZEN-012: The Essence of Persuasion — Designing the Judgment Environment
- cluster: strategy
- type: principle
- core: Persuasion is the design of the conditions under which the other person judges. The most dangerous anti-pattern (Layer 1) is disguising this design as neutrality. Delegating judgment ("decide for yourself") is persuasion's highest form when your position is transparent — and its evasion when it is not.
- activation_question: When handing someone a frame, have you disclosed your own position? If not, is the delegation honest or a way to retain influence without accountability?
- unresolved: Whether transparent position + judgment delegation constitutes persuasion's completion or its dissolution.
- last_explored: never

### ZEN-016: Creation Ability vs. Reach Ability — The Gap Is Completeness, Not Difficulty
- cluster: strategy
- type: principle
- core: The gap between what you can create and what actually reaches people is not determined by difficulty but by completeness. "Reached" must be defined before reach can be designed — and the three candidate definitions (physical delivery, comprehension, question activation) produce different design strategies.
- activation_question: What is your minimum definition of "reached" — and is your current output designed to achieve it?
- unresolved: Which definition of "reached" (comprehension vs. question-activation) is more designable in practice.
- last_explored: never

### ZEN-029: AI Product Recognition — Three-Layer Structure and Wu Wei
- cluster: strategy
- type: implementation
- core: AI products are recognized in three layers: (1) tool (solves a specific task), (2) platform (others build on top of it), (3) infrastructure (invisible, assumed). Revenue recovery strategies differ radically across layers. Wu wei (non-action) in business design means choosing the layer at which adoption becomes self-sustaining.
- activation_question: At which layer is the current product being recognized — and is the monetization strategy designed for that layer or a different one?
- unresolved: Whether revenue recovery in an AI-vs-AI world is possible at the tool layer, or requires platform/infrastructure positioning.
- last_explored: never
