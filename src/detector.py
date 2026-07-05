import json
import numpy as np
from models import NeuroAmlClassifier
from compliance import ExplainableAuditor

class EngineInferenceController:
    def __init__(self):
        with open("config/model_thresholds.json", "r") as f:
            self.config = json.load(f)
            
        self.model = NeuroAmlClassifier(
            tx_weight=self.config["weights"]["transaction_risk_weight"],
            neuro_weight=self.config["weights"]["cognitive_load_weight"]
        )
        self.auditor = ExplainableAuditor()

    def run_assessment(self, mock_pipeline_packet: dict):
        """Processes the state packet to output explicit risk classifications."""
        print("[ENGINE] Consuming synchronized state packet from Repo 2...")
        
        # Extracted mock values for computation
        simulated_tx_risk = 0.72  
        simulated_signal_variance = 7.84 

        # Execute decision model
        final_risk = self.model.forward_inference(simulated_tx_risk, simulated_signal_variance)
        is_flagged = final_risk >= self.config["critical_risk_boundary"]

        # Run feature attribution
        explanations = self.auditor.calculate_attribution(simulated_tx_risk, simulated_signal_variance)

        output = {
            "transaction_id": mock_pipeline_packet["metadata"]["tx_id"],
            "composite_risk_score": round(final_risk, 4),
            "regulatory_flag_active": is_flagged,
            "feature_attributions": explanations
        }
        
        print("\n[INFERENCE COMPLETE] Engine Output Struct:")
        print(json.dumps(output, indent=2))
        return output

if __name__ == "__main__":
    # Mocking the output produced directly by Repo 2's pipeline
    mock_input_from_repo2 = {
        "metadata": {"tx_id": "tx_hash_89f72c1a93b2", "value": 45000.0, "timestamp": 1783344000},
        "neural_tensor_shape":,
        "status": "READY_FOR_INFERENCE_ENGINE"
    }
    
    controller = EngineInferenceController()
    controller.run_assessment(mock_input_from_repo2)
