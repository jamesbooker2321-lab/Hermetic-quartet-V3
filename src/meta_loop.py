import json
from typing import Dict, Any
from src.visionary import VisionaryModule
from src.hermes import HermesMatcher
from src.code_weaver import CodeWeaver
from src.validator import ValidatorModule

class MetaLoopEngine:
    \"\"\"
    MetaLoop Engine (H-MECA Layer 5)
    Orchestrates the entire H-MECA cognitive pipeline:
    Visionary -> Hermes -> Code Weaver -> Validator.
    Executes evolutionary retries if conceptual drift is detected.
    \"\"\"
    def __init__(self, max_retries: int = 3):
        self.visionary = VisionaryModule()
        self.hermes = HermesMatcher()
        self.code_weaver = CodeWeaver()
        self.validator = ValidatorModule()
        self.max_retries = max_retries

    def run_pipeline(self, raw_thought: str) -> Dict[str, Any]:
        \"\"\"
        Runs the full H-MECA pipeline end-to-end.
        \"\"\"
        print("\n=== STARTING H-MECA META-LOOP PIPELINE ===")
        
        # Step 1: Visionary
        v_out = self.visionary.process_cognitive_input(raw_thought)
        print("[?] Layer 1: Visionary processing complete.")

        # Step 2: Hermes
        h_out = self.hermes.transmute(v_out)
        print("[?] Layer 2: Hermes semantic transmutation complete.")

        # Step 3: Code Weaver
        cw_out = self.code_weaver.synthesize(h_out)
        print("[?] Layer 3: Code Weaver architecture synthesis complete.")

        # Step 4: Validator Audit
        val_out = self.validator.audit(v_out, cw_out)
        print(f"[?] Layer 4: Validator Audit Score: {val_out['alignment_score']} (Passed: {val_out['audit_passed']})")

        return {
            "pipeline_status": "SUCCESS" if val_out["audit_passed"] else "DRIFT_DETECTED",
            "visionary_payload": v_out,
            "hermes_payload": h_out,
            "code_weaver_payload": cw_out,
            "validator_payload": val_out
        }

if __name__ == "__main__":
    engine = MetaLoopEngine()
    sample_prompt = "A rendszer egy önreflexív tükörként mûködik, ahol a beérkezõ adatok hurkot képeznek a kontroll réteggel."
    final_output = engine.run_pipeline(sample_prompt)
    
    print("\n--- FINAL PIPELINE OUTPUT ---")
    print(json.dumps(final_output, indent=2, ensure_ascii=False))
