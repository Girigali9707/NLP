# Transformation-Based Tagging

def initial_tag(word):

    if word in ["i", "he", "she", "they"]:
        return "PRP"

    elif word in ["the", "a", "an"]:
        return "DT"

    elif word in ["and", "or"]:
        return "CC"

    elif word.endswith("ly"):
        return "RB"

    elif word.endswith("ing"):
        return "VBG"

    elif word.endswith("s"):
        return "NNS"

    else:
        return "NN"


def transformation_tagger(sentence):

    words = sentence.lower().split()

    tags = [initial_tag(word) for word in words]

    # Transformation rules

    for i in range(1, len(words)):

        # Rule 1:
        # NN after pronoun -> VB
        if tags[i] == "NN" and tags[i - 1] == "PRP":
            tags[i] = "VB"

        # Rule 2:
        # NN after "to" -> VB
        if i > 0 and words[i - 1] == "to":
            tags[i] = "VB"

        # Rule 3:
        # NN after "is" -> JJ
        if i > 0 and words[i - 1] == "is":
            tags[i] = "JJ"

    return list(zip(words, tags))


sentence = "I read the book"

print("TRANSFORMATION-BASED TAGGING")

for word, tag in transformation_tagger(sentence):
    print(word, "->", tag)