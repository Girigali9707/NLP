from collections import Counter

# Training corpus
corpus = """
The student is intelligent.
The student studies computer science.
The student likes programming.
The teacher teaches computer science.
The teacher is helpful.
The student is hardworking.
Students study computer science.
The teacher likes programming.
"""

# Preprocessing
sentences = corpus.lower().replace(".", "").split("\n")

# Remove empty sentences
sentences = [s.strip().split() for s in sentences if s.strip()]

# Create N-gram counts
unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in sentences:
    unigram.update(sentence)

    for i in range(len(sentence) - 1):
        bigram[(sentence[i], sentence[i + 1])] += 1

    for i in range(len(sentence) - 2):
        trigram[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1


# Probability functions
def unigram_probability(word):
    return unigram[word] / sum(unigram.values())


def bigram_probability(w1, w2):
    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):
    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


# Display counts
print("UNIGRAM COUNTS")
print(unigram)

print("\nBIGRAM COUNTS")
for pair, count in bigram.items():
    print(pair, ":", count)

print("\nTRIGRAM COUNTS")
for triple, count in trigram.items():
    print(triple, ":", count)


# Select N
n = int(input("\nEnter N (1, 2 or 3): "))

# Query
query = input("Enter incomplete sentence: ").lower().split()

predictions = []

if n == 1:

    for word in unigram:
        predictions.append(
            (word, unigram_probability(word))
        )

elif n == 2:

    previous = query[-1]

    for word in unigram:
        probability = bigram_probability(previous, word)

        if probability > 0:
            predictions.append((word, probability))

elif n == 3:

    if len(query) < 2:
        print("Trigram requires at least two previous words.")
    else:
        w1 = query[-2]
        w2 = query[-1]

        for word in unigram:
            probability = trigram_probability(w1, w2, word)

            if probability > 0:
                predictions.append((word, probability))


predictions.sort(key=lambda x: x[1], reverse=True)

print("\nTOP-5 NEXT WORD PREDICTIONS")

for word, probability in predictions[:5]:
    print(word, "=", round(probability, 4))


# Demonstrate unseen N-gram
print("\nUNSEEN N-GRAM EXAMPLE")

print(
    "P(student | teacher) =",
    bigram_probability("teacher", "student")
)

print(
    "P(programming | student is) =",
    trigram_probability("student", "is", "programming")
)2
