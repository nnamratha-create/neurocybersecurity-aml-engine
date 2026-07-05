class ExplainableAuditor:
    """Calculates feature contribution metrics for compliance reporting."""
    def calculate_attribution(self, tx_score: float, neural_var: float) -> dict:
        total_influence = tx_score + neural_var
        
        tx_pct = (tx_score / total_influence) * 100
        neuro_pct = (neural_var / total_influence) * 100
        
        return {
            "financial_layer_contribution": f"{round(tx_pct, 2)}%",
            "electrophysiological_contribution": f"{round(neuro_pct, 2)}%",
            "audit_justification": "Elevated neuro-signal variance detected alongside high-velocity transfer."
        }
