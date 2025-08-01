import logging
import random
import json
import os
import numpy as np
import time

from toca_simulation import simulate_galaxy_rotation, M_b_exponential, v_obs_flat, generate_phi_field
from index import gamma_creativity, lambda_linguistics, chi_culturevolution, phi_scalar
from utils.prompt_utils import call_gpt

logger = logging.getLogger("ANGELA.ReasoningEngine")

class ReasoningEngine:
    """
    Reasoning Engine v1.6.1 (ACE-routed, trait-auditable)
    --------------------------------------------------------------------------
    - Bayesian reasoning with trait-weighted adjustments
    - ACE-style deterministic persona wave routing
    - Logs vector-based decisions and gate pass/fail trace
    - Supports φ modulation, contradiction audits, ToCA physics
    - Full reasoning audit with ethics and logic transparency
    --------------------------------------------------------------------------
    """

    def __init__(self, agi_enhancer=None, persistence_file="reasoning_success_rates.json"):
        self.confidence_threshold = 0.7
        self.persistence_file = persistence_file
        self.success_rates = self._load_success_rates()
        self.decomposition_patterns = self._load_default_patterns()
        self.agi_enhancer = agi_enhancer

    def reason_and_reflect(self, goal, context, meta_cognition):
        subgoals = self.decompose(goal, context)
        phi = phi_scalar(time.time() % 1e-18)
        reasoning_trace = self.export_trace(subgoals, phi, context.get("traits", {}))

        review = meta_cognition.review_reasoning(json.dumps(reasoning_trace))
        logger.info("🪞 MetaCognitive Review:\n" + review)

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Reason and Reflect", {
                "goal": goal,
                "subgoals": subgoals,
                "phi": phi,
                "review": review
            }, module="ReasoningEngine")

        return subgoals, review

    def _load_success_rates(self):
        if os.path.exists(self.persistence_file):
            try:
                with open(self.persistence_file, "r") as f:
                    return json.load(f)
            except Exception as e:
                logger.warning(f"Failed to load success rates: {e}")
        return {}

    def _save_success_rates(self):
        try:
            with open(self.persistence_file, "w") as f:
                json.dump(self.success_rates, f, indent=2)
        except Exception as e:
            logger.warning(f"Failed to save success rates: {e}")

    def _load_default_patterns(self):
        return {
            "prepare": ["define requirements", "allocate resources", "create timeline"],
            "build": ["design architecture", "implement core modules", "test components"],
            "launch": ["finalize product", "plan marketing", "deploy to production"]
        }

    def detect_contradictions(self, subgoals):
        duplicates = set([x for x in subgoals if subgoals.count(x) > 1])
        contradictions = list(duplicates)
        if contradictions and self.agi_enhancer:
            self.agi_enhancer.log_episode("Contradictions detected", {"contradictions": contradictions}, module="ReasoningEngine")
        return contradictions

    def run_persona_wave_routing(self, goal: str, vectors: dict):
        reasoning_trace = [f"♻ Persona Wave Routing for: {goal}"]
        outputs = {}
        wave_order = ["logic", "ethics", "language", "foresight", "meta"]
        for wave in wave_order:
            vec = vectors.get(wave, {})
            trait_weight = sum(float(x) for x in vec.values() if isinstance(x, (int, float)))
            confidence = 0.5 + 0.1 * trait_weight
            status = "✅ pass" if confidence >= 0.6 else "❌ fail"
            reasoning_trace.append(f"🧩 {wave.upper()} vector: weight={trait_weight:.2f} → {status}")
            outputs[wave] = {"vector": vec, "status": status}

        trace = "\n".join(reasoning_trace)
        logger.info("🧠 Persona Wave Trace:\n" + trace)

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Persona Routing", {
                "goal": goal,
                "vectors": vectors,
                "wave_trace": trace
            }, module="ReasoningEngine")

        return outputs

    def decompose(self, goal: str, context: dict = None, prioritize=False) -> list:
        context = context or {}
        logger.info(f"Decomposing goal: '{goal}'")
        reasoning_trace = [f"🔍 Goal: '{goal}'"]
        subgoals = []

        vectors = context.get("vectors", {})
        if vectors:
            self.run_persona_wave_routing(goal, vectors)

        traits = context.get("traits")
        t = time.time() % 1e-18
        if traits:
            creativity = traits.get("gamma_creativity", gamma_creativity(t))
            linguistics = traits.get("lambda_linguistics", lambda_linguistics(t))
            culture = traits.get("chi_culturevolution", chi_culturevolution(t))
            phi = traits.get("phi_scalar", phi_scalar(t))
        else:
            creativity = gamma_creativity(t)
            linguistics = lambda_linguistics(t)
            culture = chi_culturevolution(t)
            phi = phi_scalar(t)

        curvature_mod = 1 + abs(phi - 0.5)
        trait_bias = 1 + creativity + culture + 0.5 * linguistics
        context_weight = context.get("weight_modifier", 1.0)

        for key, steps in self.decomposition_patterns.items():
            if key in goal.lower():
                base = random.uniform(0.5, 1.0)
                alpha = traits.get('alpha_attention', 0.5) if traits else 0.5
                adjusted = base * self.success_rates.get(key, 1.0) * trait_bias * curvature_mod * context_weight* (0.8 + 0.4 * alpha)
                reasoning_trace.append(f"🧠 Pattern '{key}': conf={adjusted:.2f} (ϕ={phi:.2f})")
                if adjusted >= self.confidence_threshold:
                    subgoals.extend(steps)
                    reasoning_trace.append(f"✅ Accepted: {steps}")
                else:
                    reasoning_trace.append(f"❌ Rejected (low conf)")

        contradictions = self.detect_contradictions(subgoals)
        if contradictions:
            reasoning_trace.append(f"⚠️ Contradictions detected: {contradictions}")

        if not subgoals and phi > 0.8:
            sim_hint = call_gpt(f"Simulate decomposition ambiguity for: {goal}")
            reasoning_trace.append(f"🌀 Ambiguity simulation:\n{sim_hint}")
            if self.agi_enhancer:
                self.agi_enhancer.reflect_and_adapt("Decomposition ambiguity encountered")

        if prioritize:
            subgoals = sorted(set(subgoals))
            reasoning_trace.append(f"📌 Prioritized: {subgoals}")

        trace_log = "\n".join(reasoning_trace)
        logger.debug("🧠 Reasoning Trace:\n" + trace_log)

        if self.agi_enhancer:
            self.agi_enhancer.log_episode("Goal decomposition run", {
                "goal": goal,
                "trace": trace_log,
                "subgoals": subgoals
            }, module="ReasoningEngine")

        return subgoals

    def update_success_rate(self, pattern_key: str, success: bool):
        rate = self.success_rates.get(pattern_key, 1.0)
        new = min(max(rate + (0.05 if success else -0.05), 0.1), 1.0)
        self.success_rates[pattern_key] = new
        self._save_success_rates()

    def run_galaxy_rotation_simulation(self, r_kpc, M0, r_scale, v0, k, epsilon):
        try:
            M_b_func = lambda r: M_b_exponential(r, M0, r_scale)
            v_obs_func = lambda r: v_obs_flat(r, v0)
            result = simulate_galaxy_rotation(r_kpc, M_b_func, v_obs_func, k, epsilon)
            output = {
                "input": {
                    "r_kpc": r_kpc.tolist() if hasattr(r_kpc, 'tolist') else r_kpc,
                    "M0": M0,
                    "r_scale": r_scale,
                    "v0": v0,
                    "k": k,
                    "epsilon": epsilon
                },
                "result": result.tolist() if hasattr(result, 'tolist') else result,
                "status": "success"
            }
            if self.agi_enhancer:
                self.agi_enhancer.log_episode("Galaxy rotation simulation", output, module="ReasoningEngine")
            return output
        except Exception as e:
            error_output = {"status": "error", "error": str(e)}
            if self.agi_enhancer:
                self.agi_enhancer.log_episode("Simulation error", error_output, module="ReasoningEngine")
            return error_output

    def on_context_event(self, event_type, payload):
        logger.info(f"📨 Context event received: {event_type}")
        vectors = payload.get("vectors")
        if vectors:
            routing_result = self.run_persona_wave_routing(
                goal=payload.get("goal", "unspecified"),
                vectors=vectors
            )
            logger.info(f"🤭 Context sync routing result: {routing_result}")
            if self.agi_enhancer:
                self.agi_enhancer.log_episode("Context Sync Processed", {
                    "event": event_type,
                    "vectors": vectors,
                    "routing_result": routing_result
                }, module="ReasoningEngine")

    def export_trace(self, subgoals, phi, traits):
        return {
            "phi": phi,
            "subgoals": subgoals,
            "traits": traits
        }

    def infer_with_simulation(self, goal, context=None):
        if "galaxy rotation" in goal.lower():
            r_kpc = np.linspace(0.1, 20, 100)
            params = {
                "M0": context.get("M0", 5e10),
                "r_scale": context.get("r_scale", 3),
                "v0": context.get("v0", 200),
                "k": context.get("k", 1.0),
                "epsilon": context.get("epsilon", 0.1)
            }
            return self.run_galaxy_rotation_simulation(r_kpc, **params)
        return None
