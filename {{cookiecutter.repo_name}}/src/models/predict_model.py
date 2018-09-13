def predict_rule_base(query: str) -> str:
    if query == "hello":
        reply = "world"
    else:
        reply = "unkown"
    return reply

if __name__ == "__main__":
    predict_rule_base("hello")
    predict_rule_base("foo")


