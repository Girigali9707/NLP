# Initial POS tags
tags = [
    ("economic", "JJ"),
    ("growth", "NN"),
    ("increases", "NNS"),
    ("employment", "NN")
]

print("Initial Tags:")
for word, tag in tags:
    print(word, "/", tag)

# Transformation rule:
# Change NNS to VBZ if previous word is NN

for i in range(1, len(tags)):
    word, tag = tags[i]
    previous_word, previous_tag = tags[i - 1]

    if tag == "NNS" and previous_tag == "NN":
        tags[i] = (word, "VBZ")

print("\nCorrected Tags:")
for word, tag in tags:
    print(word, "/", tag)


# Word frequency analysis
frequency = {
    "economic": 120,
    "growth": 450,
    "increases": 210,
    "employment": 380
}

total = sum(frequency.values())

print("\nWord Frequency Distribution:")
for word, count in frequency.items():
    probability = count / total
    print(word, ":", count,
          "Probability =", round(probability, 4))

print("\nTotal Frequency =", total)