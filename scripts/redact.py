import pandas as pd

def redact_entities(text, entities):
    for ent, _ in entities:
        text = text.replace(ent, "[REDACTED]")
    return text

if __name__ == "__main__":
    df = pd.read_csv("data/ner_output.csv")
    df["redacted_text"] = [
        redact_entities(text, eval(entities))
        for text, entities in zip(df["content"], df["entities"])
    ]
    df.to_csv("data/redacted_output.csv", index=False)
