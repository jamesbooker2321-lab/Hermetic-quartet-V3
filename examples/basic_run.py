import sys
import os
import json

# Ensure project root is in path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from src.meta_loop import MetaLoopEngine

def main():
    print("=========================================================")
    print("        H-MECA v3.0 — LIVE DEMONSTRATION RUN")
    print("=========================================================\n")
    
    # Initialize MetaLoop engine
    engine = MetaLoopEngine()
    
    # Metaphor-dense input
    prompt = "A rendszer egy önreflexív tükörként mûködik, ahol a beérkezõ adatok hurkot képeznek a kontroll réteggel."
    
    print(f"[INPUT PROMPT]: \"{prompt}\"\n")
    
    # Execute full pipeline
    results = engine.run_pipeline(prompt)
    
    print("\n---------------------------------------------------------")
    print("               SYNTHESIZED ARCHITECTURE STUB")
    print("---------------------------------------------------------")
    print(results["code_weaver_payload"]["generated_code_stub"])
    
    print("---------------------------------------------------------")
    print("               MERMAID TOPOLOGY DIAGRAM")
    print("---------------------------------------------------------")
    print(results["code_weaver_payload"]["mermaid_topology"])
    print("\n---------------------------------------------------------")
    print(f"AUDIT STATUS: {results['pipeline_status']}")
    print(f"ALIGNMENT SCORE: {results['validator_payload']['alignment_score']}")
    print("=========================================================")

if __name__ == "__main__":
    main()
