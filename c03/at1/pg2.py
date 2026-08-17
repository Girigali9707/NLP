from collections import Counter

corpus = """
The student is intelligent.
The student studies computer science.
The student likes programming.
The teacher teaches computer science.
The teacher is helpful.
The student is hardworking.
The teacher likes programming.
"""

sentences = [
    s.lower().replace(".", "").split()
    for s in corpus.strip().split("\n")
]

unigram = Counter()
bigram = Counter()
trigram = Counter()

for sentence in sentences:

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


# Backoff model
def backoff_probability(w1, w2, w3):

    tri = trigram_probability(w1, w2, w3)

    if tri > 0:
        return tri

    bi = bigram_probability(w2, w3)

    if bi > 0:
        return bi

    return unigram_probability(w3)


# Deleted interpolation
lambda_tri = 0.5
lambda_bi = 0.3
lambda_uni = 0.2


def interpolation_probability(w1, w2, w3):

    tri = trigram_probability(w1, w2, w3)
    bi = bigram_probability(w2, w3)
    uni = unigram_probability(w3)

    return (
        lambda_tri * tri +
        lambda_bi * bi +
        lambda_uni * uni
    )


# Prediction function
def predict(query):

    words = query.lower().split()

    predictions = []

    for word in unigram:

        if len(words) >= 2:
            w1 = words[-2]
            w2 = words[-1]

            unsmoothed = trigram_probability(w1, w2, word)
            backoff = backoff_probability(w1, w2, word)
            interpolation = interpolation_probability(w1, w2, word)

        else:
            w2 = words[-1]

            unsmoothed = bigram_probability(w2, word)
            backoff = bigram_probability(w2, word)
            interpolation = (
                lambda_bi * bigram_probability(w2, word)
                + lambda_uni * unigram_probability(word)
            )

        predictions.append(
            (word, unsmoothed, backoff, interpolation)
        )

    return sorted(
        predictions,
        key=lambda x: x[3],
        reverse=True
    )


query = input("Enter sentence: ")

results = predict(query)

print("\nWORD\tUNSMOOTHED\tBACKOFF\tINTERPOLATION")

for word, u, b, i in results[:5]:

    print(
        word,
        "\t",
        round(u, 4),
        "\t\t",
        round(b, 4),
        "\t",
        round(i, 4)
    )