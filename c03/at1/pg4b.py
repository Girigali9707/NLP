from collections import Counter

# Small training corpus
training_data = [
    [
        ("the", "DT"),
        ("student", "NN"),
        ("reads", "VBZ"),
        ("a", "DT"),
        ("book", "NN")
    ],
    [
        ("the", "DT"),
        ("teacher", "NN"),
        ("writes", "VBZ"),
        ("a", "DT"),
        ("letter", "NN")
    ],
    [
        ("the", "DT"),
        ("student", "NN"),
        ("writes", "VBZ"),
        ("carefully", "RB")
    ]
]

word_tag = Counter()
tag_count = Counter()
transition = Counter()

for sentence in training_data:

    previous_tag = "<START>"

    for word, tag in sentence:

        word_tag[(word, tag)] += 1
        tag_count[tag] += 1

        transition[(previous_tag, tag)] += 1

        previous_tag = tag


def emission_probability(word, tag):

    if tag_count[tag] == 0:
        return 0

    return word_tag[(word, tag)] / tag_count[tag]


def transition_probability(previous, current):

    total = sum(
        transition[(previous, tag)]
        for tag in tag_count
    )

    if total == 0:
        return 0

    return transition[(previous, current)] / total


tags = list(tag_count.keys())


def stochastic_tagger(sentence):

    result = []
    previous_tag = "<START>"

    for word in sentence.lower().split():

        best_tag = None
        best_score = 0

        for tag in tags:

            emission = emission_probability(word, tag)

            transition_p = transition_probability(
                previous_tag,
                tag
            )

            score = emission * transition_p

            if score > best_score:

                best_score = score
                best_tag = tag

        if best_tag is None:
            best_tag = "NN"

        result.append((word, best_tag))

        previous_tag = best_tag

    return result


sentence = "the student reads a book"

print("STOCHASTIC POS TAGGING")

for word, tag in stochastic_tagger(sentence):
    print(word, "->", tag)