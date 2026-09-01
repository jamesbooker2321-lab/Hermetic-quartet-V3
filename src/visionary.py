import json
from typing import Dict, Any, Optional

class VisionaryModule:
    \"\"\"
    Visionary Module (H-MECA Layer 1)
    Captures metaphor-dense, high-level Hungarian cognitive inputs and translates
    them into a structured cognitive payload containing hidden architectural intent.
    \"\"\"
    def __init__(self, max_word_limit: int = 150):
        self.max_word_limit = max_word_limit

    def process_cognitive_input(self, raw_thought: str, context_tag: Optional[str] = "core_system") -> Dict[str, Any]:
        \"\"\"
        Processes raw conceptual thoughts into a structured cognitive dictionary.
        \"\"\"
        words = raw_thought.strip().split()
        if len(words) > self.max_word_limit:
            raw_thought = " ".join(words[:self.max_word_limit])

        payload = {
            "meta_layer": "Visionary",
            "context_tag": context_tag,
            "raw_cognitive_stream": raw_thought,
            "structural_cues": {
                "has_metaphor": any(word in raw_thought.lower() for word in ["tükör", "hurok", "szövet", "kristály", "áramlás"]),
                "complexity_degree": "high" if len(words) > 50 else "standard"
            },
            "status": "ready_for_transmutation"
        }
        return payload

if __name__ == "__main__":
    visionary = VisionaryModule()
    sample_input = "A rendszer egy önreflexív tükörként mûködik, ahol a beérkezõ adatok hurkot képeznek a kontroll réteggel."
    result = visionary.process_cognitive_input(sample_input)
    print("--- Visionary Module Output ---")
    print(json.dumps(result, indent=2, ensure_ascii=False))
