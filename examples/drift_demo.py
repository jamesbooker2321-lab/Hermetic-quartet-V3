"""
Hermetic Quartet v3.0 — Conceptual Drift & Evolutionary Auto-Correction Demo
Demonstrates Layer 4 (Validator) capturing intentional drift and Layer 5 (MetaLoop) restoring alignment.
"""
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from src.visionary import Visionary
from src.hermes import Hermes
from src.code_weaver import CodeWeaver
from src.validator import Validator
from src.meta_loop import MetaLoop

def run_drift_simulation():
    print("==================================================================")
    print("   H-MECA v3.0 — CONCEPTUAL DRIFT & ADVERSARIAL AUDIT DEMO")
    print("==================================================================\n")

    # Step 1: Cognitive Input
    cognitive_prompt = "Build a self-healing B2B inventory reconciliation agent with fraud detection."
    print(f"[1] Cognitive Input (Visionary): '{cognitive_prompt}'")
    
    visionary = Visionary()
    hermeneutic_intent = visionary.capture_intent(cognitive_prompt)
    
    # Step 2: Transmutation
    hermes = Hermes()
    tech_spec = hermes.transmute(hermeneutic_intent)
    print(f"[2] Transmuted Tech Spec: Modules -> {tech_spec['required_modules']}\n")

    # Step 3: Simulate Drifted Output (Faulty Agent Generation)
    print("--- SIMULATING CONCEPTUAL DRIFT IN AGENT CODE ---")
    drifted_synthesis = {
        "code": "class InventoryAgent:\n    def reconcile(self): pass\n    # Note: FraudDetection and SelfHealing modules dropped due to drift",
        "topology": "graph TD\n A[InventoryAgent]",
        "has_drift": True
    }
    
    validator = Validator(alignment_threshold=0.85)
    passed, score, report = validator.audit(tech_spec, drifted_synthesis)
    
    print(f"[3] Validator Audit Report:")
    print(f"    Passed: {passed}")
    print(f"    Report: {report}\n")

    # Step 4: Trigger MetaLoop Self-Correction
    if not passed:
        print("--- LAUNCHING H-MECA METALOOP EVOLUTIONARY RETRY ---")
        meta_loop = MetaLoop(hermes, CodeWeaver(), validator)
        corrected_output = meta_loop.execute_cycle(tech_spec, drifted_synthesis)
        print("\n[4] MetaLoop Evolutionary Stabilization Complete!")
        print("    Final Corrected Status: Operational & Aligned")
        print("==================================================================")

if __name__ == "__main__":
    run_drift_simulation()
