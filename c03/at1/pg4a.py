# TASK 4: POS Tagging

sentence = "The student reads a book and writes carefully"

words = sentence.lower().split()

# Lexical dictionary
dictionary = {
    "the": "DT",
    "a": "DT",
    "an": "DT",

    "student": "NN",
    "book": "NN",

    "reads": "VBZ",
    "writes": "VBZ",
    "read": "VB",
    "write": "VB",

    "beautiful": "JJ",
    "good": "JJ",

    "carefully": "RB",
    "quickly": "RB",

    "i": "PRP",
    "he": "PRP",
    "she": "PRP",
    "they": "PRP",

    "and": "CC",
    "or": "CC",

    "in": "IN",
    "on": "IN",
    "at": "IN"
}


def rule_based_tagger(words):

    result = []

    for word in words:

        if word in dictionary:
            tag = dictionary[word]

        elif word.endswith("ly"):
            tag = "RB"

        elif word.endswith("ing"):
            tag = "VBG"

        elif word.endswith("ed"):
            tag = "VBD"

        elif word.endswith("s"):
            tag = "NNS"

        else:
            tag = "NN"

        result.append((word, tag))

    return result


print("RULE-BASED POS TAGGING")

for word, tag in rule_based_tagger(words):
    print(word, "->", tag)