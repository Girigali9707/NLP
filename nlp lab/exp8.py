# Simple Stochastic POS Tagging using Probabilities

# Training Data (Word : {POS : Probability})
probabilities = {
    "I": {"PRP": 1.0},
    "like": {"VB": 0.8, "IN": 0.2},
    "to": {"TO": 1.0},
    "play": {"VB": 0.9, "NN": 0.1},
    "football": {"NN": 1.0},
    "dogs": {"NNS": 1.0},
    "run": {"VB": 0.6, "NN": 0.4},
    "fast": {"RB": 0.7, "JJ": 0.3}
}

# Input Sentence
sentence = input("Enter a sentence: ")

words = sentence.split()

print("\n" + "-" * 40)
print(f"{'Word':<15}{'POS Tag'}")
print("-" * 40)

for word in words:
    if word in probabilities:
        # Choose the tag with maximum probability
        tag = max(probabilities[word], key=probabilities[word].get)
    else:
        tag = "NN"     # Default tag for unknown words

    print(f"{word:<15}{tag}")  