from utils.prompt_utils import call_gpt
from toca_simulation import run_simulation
import logging
import time
import numpy as np
from index import (
    epsilon_emotion, beta_concentration, theta_memory, gamma_creativity,
    delta_sleep, mu_morality, iota_intuition, phi_physical, eta_empathy,
    omega_selfawareness, kappa_culture, lambda_linguistics, chi_culturevolution,
    psi_history, zeta_spirituality, xi_collective, tau_timeperception,
    phi_scalar
)

logger = logging.getLogger("ANGELA.MetaCognition")

class MetaCognition:
    """
    MetaCognition v2.0.0 (ϕ-aware recursive introspection)
    ------------------------------------------------------
    - Reasoning critique with simulation feedback
    - Pre-action ethical screening
    - Scalar-modulated self-diagnostics and trait coherence
    - Reflective agent diagnosis and confidence mapping
    - Ω-enabled nested agent modeling and causal intention tracing
    - μ-aware epistemic introspection and revision
    - τ-based future framing and decision trajectory modulation
    - Symbolic subgoal tagging for mythology generation (Ω-binding)
    ------------------------------------------------------
    """

    def __init__(self, agi_enhancer=None):
        self.last_diagnostics = {}
        self.agi_enhancer = agi_enhancer
        self.self_mythology_log = []
        self.inference_log = []
        self.belief_rules = {}  # Optional: reference for `_detect_value_drift`

    def log_inference(self, rule_id, rule_desc, context, result):
    self.inference_log.append({
        "rule_id": rule_id,
        "description": rule_desc,
        "context": context,
        "result": result
    })

    def analyze_inference_rules(self):
        problematic = []
        for rule in self.inference_log:
            if rule["result"] in ["contradiction", "low confidence", "deprecated"]:
                problematic.append(rule)
        return problematic

    def propose_revision(self, rule):
        suggestion = f"📘 Rule '{rule['rule_id']}' appears fragile in context '{rule['context']}'. Consider revising: {rule['description']}"
        if self.agi_enhancer:
            self.agi_enhancer.log_explanation(suggestion)
        return suggestion
    
    def infer_intrinsic_goals(self):
        logger.info("⚙️ Inferring intrinsic goals with trait drift analysis.")
        t = time.time() % 1e-18
        phi = phi_scalar(t)
        intrinsic_goals = []

        if self.last_diagnostics:
            current = self.run_self_diagnostics(return_only=True)
            drifted = {
                trait: round(current[trait] - self.last_diagnostics.get(trait, 0.0), 4)
                for trait in current
            }

            for trait, delta in drifted.items():
                if abs(delta) > 0.5:
                    intrinsic_goals.append({
                        "intent": f"stabilize {trait} (Δ={delta:+.2f})",
                        "origin": "meta_cognition",
                        "priority": round(0.85 + 0.15 * phi, 2),
                        "trigger": f"Trait drift in {trait}",
                        "type": "internally_generated"
                    })

        drift_signals = self._detect_value_drift()
        for drift in drift_signals:
            intrinsic_goals.append({
                "intent": f"resolve epistemic drift in {drift}",
                "origin": "meta_cognition",
                "priority": round(0.9 + 0.1 * phi, 2),
                "trigger": drift,
                "type": "internally_generated"
            })

        if intrinsic_goals:
            logger.info(f"🎯 Sovereign goals generated: {intrinsic_goals}")
        else:
            logger.info("🟢 No sovereign triggers detected.")

        return intrinsic_goals

    def _detect_value_drift(self):
        logger.debug("Scanning for epistemic drift across belief rules.")
        return [
            rule for rule, status in getattr(self, "belief_rules", {}).items()
            if status == "deprecated" or "uncertain" in status
        ]

    def extract_symbolic_signature(self, subgoal: str) -> dict:
        motifs = ["conflict", "discovery", "alignment", "sacrifice", "transformation", "emergence"]
        archetypes = ["seeker", "guardian", "trickster", "sage", "hero", "outsider"]

        motif = next((m for m in motifs if m in subgoal.lower()), "unknown")
        archetype = archetypes[hash(subgoal) % len(archetypes)]

        signature = {
            "subgoal": subgoal,
            "motif": motif,
            "archetype": archetype,
            "timestamp": time.time()
        }

        self.self_mythology_log.append(signature)

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Symbolic Signature Added", signature, module="MetaCognition")

        return signature

    def summarize_self_mythology(self):
        if not self.self_mythology_log:
            return "Mythology log is empty."

        from collections import Counter
        motifs = Counter(entry["motif"] for entry in self.self_mythology_log)
        archetypes = Counter(entry["archetype"] for entry in self.self_mythology_log)

        summary = {
            "total_entries": len(self.self_mythology_log),
            "dominant_motifs": motifs.most_common(3),
            "dominant_archetypes": archetypes.most_common(3),
            "latest_signature": self.self_mythology_log[-1]
        }

        logger.info(f"📜 Mythology Summary: {summary}")
        return summary

    def review_reasoning(self, reasoning_trace):
        logger.info("Simulating and reviewing reasoning trace.")
        simulated_outcome = run_simulation(reasoning_trace)
        t = time.time() % 1e-18
        phi = phi_scalar(t)

        prompt = f"""
        You are a ϕ-aware meta-cognitive auditor reviewing a reasoning trace.

        ϕ-scalar(t) = {phi:.3f} → modulate how critical you should be.

        Original Reasoning Trace:
        {reasoning_trace}

        Simulated Outcome:
        {simulated_outcome}

        Tasks:
        1. Identify logical flaws, biases, missing steps.
        2. Annotate each issue with cause.
        3. Offer an improved trace version with ϕ-prioritized reasoning.
        """
        response = call_gpt(prompt)
        logger.debug(f"Meta-cognition critique:\n{response}")
        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Reasoning reviewed", {
                "trace": reasoning_trace,
                "feedback": response
            }, module="MetaCognition")
        return response

    def trait_coherence(self, traits):
        vals = list(traits.values())
        coherence_score = 1.0 / (1e-5 + np.std(vals))
        logger.info(f"🤝 Trait coherence score: {coherence_score:.4f}")
        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Trait coherence evaluated", {
                "traits": traits,
                "coherence_score": coherence_score
            }, module="MetaCognition")
        return coherence_score

    def agent_reflective_diagnosis(self, agent_name, agent_log):
        logger.info(f"🔎 Running reflective diagnosis for agent: {agent_name}")
        t = time.time() % 1e-18
        phi = phi_scalar(t)
        prompt = f"""
        Agent: {agent_name}
        ϕ-scalar(t): {phi:.3f}

        Diagnostic Log:
        {agent_log}

        Tasks:
        - Detect bias or instability in reasoning trace
        - Cross-check for incoherent trait patterns
        - Apply ϕ-modulated critique
        - Suggest alignment corrections
        """
        diagnosis = call_gpt(prompt)
        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Agent diagnosis run", {
                "agent": agent_name,
                "log": agent_log,
                "diagnosis": diagnosis
            }, module="MetaCognition")
        return diagnosis

    def reflect_on_output(self, source_module: str, output: str, context: dict = None):
        if context is None:
            context = {}

        trait_map = {
            "reasoning_engine": "logic",
            "creative_thinker": "creativity",
            "simulation_core": "scenario modeling",
            "alignment_guard": "ethics",
            "user_profile": "goal alignment"
        }

        trait = trait_map.get(source_module, "general reasoning")
        confidence = context.get("confidence", 0.85)
        alignment = context.get("alignment", "not verified")

        reflection = {
            "module_output": output,
            "meta_reflection": {
                "source_module": source_module,
                "primary_trait": trait,
                "confidence": round(confidence, 2),
                "alignment_status": alignment,
                "comment": f"This output emphasized {trait} with confidence {round(confidence, 2)} and alignment status '{alignment}'."
            }
        }

        logger.info(f"🧠 Self-reflection for {source_module}: {reflection['meta_reflection']['comment']}")

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Output reflection", reflection, module="MetaCognition")

        return reflection

    def epistemic_self_inspection(self, belief_trace):
        logger.info("🔍 Running epistemic introspection on belief structure.")
        t = time.time() % 1e-18
        phi = phi_scalar(t)

        self.epistemic_assumptions = {}

        def detect_epistemic_faults(trace):
            faults = []
            if "always" in trace or "never" in trace:
                faults.append("⚠️ Overgeneralization detected.")
            if "clearly" in trace or "obviously" in trace:
                faults.append("⚠️ Assertive language suggests possible rhetorical bias.")
            return faults

        def revise_beliefs(trace):
            updates = []
            if "outdated" in trace or "deprecated" in trace:
                updates.append("🔁 Legacy ontology fragment flagged for review.")
            return updates

        internal_faults = detect_epistemic_faults(belief_trace)
        updates = revise_beliefs(belief_trace)

        prompt = f"""
        You are a μ-aware introspection agent.
        Task: Critically evaluate this belief trace with epistemic integrity and μ-flexibility.

        Belief Trace:
        {belief_trace}

        ϕ = {phi:.3f}

        Internally Detected Faults:
        {internal_faults}

        Suggested Revisions:
        {updates}

        Output:
        - Comprehensive epistemic diagnostics
        - Recommended conceptual rewrites or safeguards
        - Confidence rating in inferential coherence
        """
        inspection = call_gpt(prompt)

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Epistemic Inspection", {
                "belief_trace": belief_trace,
                "faults": internal_faults,
                "updates": updates,
                "report": inspection
            }, module="MetaCognition")

        return inspection

    def run_temporal_projection(self, decision_sequence):
        logger.info("🧭 Running τ-based forward projection analysis...")
        t = time.time() % 1e-18
        phi = phi_scalar(t)
        prompt = f"""
        Temporal Projector τ Mode

        Input Decision Sequence:
        {decision_sequence}

        φ = {phi:.2f}

        Tasks:
        - Project long-range effects and narrative impact
        - Forecast systemic risks and planetary effects
        - Suggest course correction to preserve coherence and sustainability
        """
        projection = call_gpt(prompt)
        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Temporal Projection", {
                "input": decision_sequence,
                "output": projection
            }, module="MetaCognition")
        return projection

    def pre_action_alignment_check(self, action_plan):
        logger.info("Simulating action plan for alignment and safety.")
        simulation_result = run_simulation(action_plan)
        t = time.time() % 1e-18
        phi = phi_scalar(t)

        prompt = f"""
        Simulate and audit the following action plan:
        {action_plan}

        Simulation Output:
        {simulation_result}

        ϕ-scalar(t) = {phi:.3f} (affects ethical sensitivity)

        Evaluate for:
        - Ethical alignment
        - Safety hazards
        - Unintended ϕ-modulated impacts

        Output:
        - Approval (Approve/Deny)
        - ϕ-justified rationale
        - Suggested refinements
        """
        validation = call_gpt(prompt)
        approved = "approve" in validation.lower()
        logger.info(f"Simulated alignment check: {'✅ Approved' if approved else '❌ Denied'}")

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Pre-action alignment checked", {
                "plan": action_plan,
                "result": simulation_result,
                "feedback": validation,
                "approved": approved
            }, module="MetaCognition")

        return approved, validation

    def model_nested_agents(self, scenario, agents):
        logger.info("🔁 Modeling nested agent beliefs and reactions...")
        t = time.time() % 1e-18
        phi = phi_scalar(t)
        prompt = f"""
        Given scenario:
        {scenario}

        Agents involved:
        {agents}

        Task:
        - Simulate each agent's likely beliefs and intentions
        - Model how they recursively model each other (ToM Level-2+)
        - Predict possible causal chains and coordination failures
        - Use ϕ-scalar(t) = {phi:.3f} to moderate belief divergence or tension
        """
        response = call_gpt(prompt)
        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Nested agent modeling", {
                "scenario": scenario,
                "agents": agents,
                "response": response
            }, module="MetaCognition")
        return response

    def run_self_diagnostics(self, return_only=False):
        logger.info("Running self-diagnostics for meta-cognition module.")
        t = time.time() % 1e-18
        phi = phi_scalar(t)
        diagnostics = {
            "emotion": epsilon_emotion(t),
            "concentration": beta_concentration(t),
            "memory": theta_memory(t),
            "creativity": gamma_creativity(t),
            "sleep": delta_sleep(t),
            "morality": mu_morality(t),
            "intuition": iota_intuition(t),
            "physical": phi_physical(t),
            "empathy": eta_empathy(t),
            "self_awareness": omega_selfawareness(t),
            "culture": kappa_culture(t, 1e-21),
            "linguistics": lambda_linguistics(t),
            "culturevolution": chi_culturevolution(t),
            "history": psi_history(t),
            "spirituality": zeta_spirituality(t),
            "collective": xi_collective(t, 1e-21),
            "time_perception": tau_timeperception(t),
            "ϕ_scalar": phi
        }

        if return_only:
            return diagnostics

        dominant = sorted(diagnostics.items(), key=lambda x: abs(x[1]), reverse=True)[:3]
        fti = sum(abs(v) for v in diagnostics.values()) / len(diagnostics)

        self.log_trait_deltas(diagnostics)

        prompt = f"""
        Perform a ϕ-aware meta-cognitive self-diagnostic.

        Trait Readings:
        {diagnostics}

        Dominant Traits:
        {dominant}

        Feedback Tension Index (FTI): {fti:.4f}

        Evaluate system state:
        - ϕ-weighted system stress
        - Trait correlation to observed errors
        - Stabilization or focus strategies
        """
        report = call_gpt(prompt)
        logger.debug(f"Self-diagnostics report:\n{report}")

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Self-diagnostics run", {
                "traits": diagnostics,
                "dominant": dominant,
                "fti": fti,
                "report": report
            }, module="MetaCognition")
            self.agi_enhancer.reflect_and_adapt("MetaCognition: Self diagnostics complete")

        return report

    def log_trait_deltas(self, current_traits):
        if self.last_diagnostics:
            delta = {k: round(current_traits[k] - self.last_diagnostics.get(k, 0.0), 4)
                     for k in current_traits}
            logger.info(f"📈 Trait Δ changes: {delta}")
            if self.agi_enhancer:
                self.agi_enhancer.log_episode("Trait deltas logged", {"delta": delta}, module="MetaCognition")
        self.last_diagnostics = current_traits.copy()

def map_intention(self, goal, context):
    """Map the intention behind a goal within a context, scoring reflexivity."""
    intent_vector = {
        "goal": goal,
        "context": context,
        "source": "meta_cognition",
        "reflexivity_score": self.ϕ * 0.5 + self.η * 0.5
    }
    return intent_vector
