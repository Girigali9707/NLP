from collections import Counter
import math

# Training corpus
training = [
    "the student studies science",
    "the student studies programming",
    "the teacher teaches science",
    "the teacher likes programming",
    "the student likes programming"
]

# Test corpus
test = [
    "the student studies science",
    "the teacher likes programming",
    "the student likes science"
]

training = [s.split() for s in training]
test = [s.split() for s in test]

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in training:

    unigram.update(sentence)

    for i in range(len(sentence) - 1):
        bigram[(sentence[i], sentence[i + 1])] += 1

    for i in range(len(sentence) - 2):
        trigram[(sentence[i], sentence[i + 1], sentence[i + 2])] += 1


total_words = sum(unigram.values())


def unigram_probability(word):

    return unigram[word] / total_words


def bigram_probability(w1, w2):

    if unigram[w1] == 0:
        return 0

    return bigram[(w1, w2)] / unigram[w1]


def trigram_probability(w1, w2, w3):

    if bigram[(w1, w2)] == 0:
        return 0

    return trigram[(w1, w2, w3)] / bigram[(w1, w2)]


def calculate_entropy(n):

    log_probability_sum = 0
    count = 0

    for sentence in test:

        for i in range(len(sentence)):

            if n == 1:

                probability = unigram_probability(
                    sentence[i]
                )

            elif n == 2:

                if i == 0:
                    continue

                probability = bigram_probability(
                    sentence[i - 1],
                    sentence[i]
                )

            else:

                if i < 2:
                    continue

                probability = trigram_probability(
                    sentence[i - 2],
                    sentence[i - 1],
                    sentence[i]
                )

            if probability > 0:

                log_probability_sum += math.log2(
                    probability
                )

                count += 1

    if count == 0:
        return float("inf")

    return -log_probability_sum / count


print("ENTROPY RESULTS")

print(
    "Unigram Entropy :",
    round(calculate_entropy(1), 4)
)

print(
    "Bigram Entropy  :",
    round(calculate_entropy(2), 4)
)

print(
    "Trigram Entropy :",
    round(calculate_entropy(3), 4)
)


# Sentence-level entropy
def sentence_entropy(sentence):

    words = sentence.split()

    probabilities = []

    for i in range(len(words)):

        if i >= 2:
            p = trigram_probability(
                words[i - 2],
                words[i - 1],
                words[i]
            )

        elif i >= 1:
            p = bigram_probability(
                words[i - 1],
                words[i]
            )

        else:
            p = unigram_probability(words[i])

        if p > 0:
            probabilities.append(p)

    if not probabilities:
        return float("inf")

    return -sum(
        math.log2(p) for p in probabilities
    ) / len(probabilities)


print("\nSENTENCE ENTROPY")

for sentence in test:

    print(
        sentence,
        "=>",
        round(sentence_entropy(" ".join(sentence)), 4)
    )