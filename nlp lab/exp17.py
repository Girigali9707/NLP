# ==========================================
# WordNet - Synsets and Word Meanings
# ==========================================

import nltk

# Download WordNet data
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.corpus import wordnet as wn


# Input word
word = "bank"


# Get synsets
synsets = wn.synsets(word)

print("Word:", word)

print("\nNumber of Synsets:", len(synsets))

print("\nSynsets and Meanings:")
print("-" * 50)


# Display synsets
for synset in synsets:

    print("\nSynset:", synset.name())

    print("Definition:", synset.definition())

    print("Examples:", synset.examples())

    print("Lemmas:")

    for lemma in synset.lemmas():
        print("  -", lemma.name())


# ------------------------------------------
# Find synonyms
# ------------------------------------------

print("\n" + "=" * 50)
print("SYNONYMS")
print("=" * 50)

synonyms = set()

for synset in synsets:
    for lemma in synset.lemmas():
        synonyms.add(lemma.name())

print("Synonyms of", word, ":")

for synonym in sorted(synonyms):
    print("-", synonym)


# ------------------------------------------
# Find hypernyms
# ------------------------------------------

print("\n" + "=" * 50)
print("HYPERNYMS")
print("=" * 50)

for synset in synsets:

    print("\n", synset.name())

    for hypernym in synset.hypernyms():
        print("  ->", hypernym.name())