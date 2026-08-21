# ==========================================
# Word Sense Disambiguation using Lesk
# ==========================================

import nltk

# Download WordNet
nltk.download("wordnet")
nltk.download("omw-1.4")

from nltk.corpus import wordnet as wn


# ------------------------------------------
# Simple Lesk Algorithm
# ------------------------------------------

def lesk(word, sentence):

    # Get all possible meanings of the word
    synsets = wn.synsets(word)

    # Convert context sentence into words
    context = set(sentence.lower().split())

    best_synset = None
    max_overlap = 0

    # Compare each meaning with context
    for synset in synsets:

        # Get definition
        definition_words = set(
            synset.definition().lower().split()
        )

        # Get example words
        example_words = set()

        for example in synset.examples():
            example_words.update(
                example.lower().split()
            )

        # Combine definition and examples
        signature = definition_words.union(example_words)

        # Find common words
        overlap = len(context.intersection(signature))

        print(
            synset.name(),
            "-> Overlap:",
            overlap
        )

        # Select highest overlap
        if overlap > max_overlap:
            max_overlap = overlap
            best_synset = synset

    return best_synset, max_overlap


# ------------------------------------------
# Test Sentence
# ------------------------------------------

sentence = "The bank by the river was flooded."

word = "bank"

print("Sentence:")
print(sentence)

print("\nTarget Word:")
print(word)

print("\nLesk Scores:")
print("-" * 40)

best_synset, score = lesk(word, sentence)


# ------------------------------------------
# Display Result
# ------------------------------------------

print("\n" + "=" * 40)

if best_synset:

    print("Selected Sense:")
    print(best_synset.name())

    print("\nDefinition:")
    print(best_synset.definition())

    print("\nExample:")
    print(best_synset.examples())

    print("\nOverlap Score:")
    print(score)

else:

    print("No sense found.")