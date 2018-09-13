from src.models.predict_model import predict_rule_base

def predict(query: str, argolism = "rule_base") -> str:
    if argolism == "rule_base":
        return predict_rule_base(query)

