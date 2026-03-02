import spacy
from spacy import displacy
import pandas as pd

nlp = spacy.load("en_core_web_sm")

text = """
Amazon announced its quarterly earnings on July 30, 2023. 
CEO Andy Jassy said the company is investing $4 billion in AI technology. 
Google, based in Mountain View, California, also shared its financial report. 
The 2024 Summer Olympics will be held in Paris, France.
"""

doc = nlp(text)

def extract_entities(doc):
    entities = []
    for ent in doc.ents:
        entities.append({
            'Entity': ent.text,
            'Label': ent.label_,
            'Explanation': spacy.explain(ent.label_)
        })
    return pd.DataFrame(entities)

entities_df = extract_entities(doc)

print("Extracted Nmed Entities:")
print(entities_df)

displacy.render(doc, style="ent", jupyter=True)

entities_df.to_csv("extracted_entities.csv", index=False)
print("\nEntities saved to 'extracted_entities.csv'")