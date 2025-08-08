import spacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

def extract_entities(text):
    doc = nlp(text)
    return [(ent.text, ent.label_) for ent in doc.ents]

if __name__ == "__main__":
    df = pd.read_csv("data/news_dataset.csv")
    df["entities"] = df["content"].apply(extract_entities)
    df.to_csv("data/ner_output.csv", index=False)
