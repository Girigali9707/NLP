# ==========================================
# Named Entity Recognition using spaCy
# ==========================================

import spacy

# Load the English NLP model
nlp = spacy.load("en_core_web_sm")

# Input text
text = """
Apple was founded by Steve Jobs in California.
Tim Cook is the CEO of Apple.
The company announced a new product in 2025.
"""

# Process the text
doc = nlp(text)

# Display named entities
print("Named Entities:")
print("-" * 40)

for entity in doc.ents:
    print(entity.text, "->", entity.label_)

# Display entity descriptions
print("\nEntity Details:")
print("-" * 40)

for entity in doc.ents:
    print(
        entity.text,
        "->",
        entity.label_,
        "->",
        spacy.explain(entity.label_)
    )