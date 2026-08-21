# Transformation-Based Tagging

def transformation_tagging(sentence):

    # Split sentence into words
    words = sentence.split()

    # Step 1: Assign initial tags
    tagged = []

    for word in words:
        w = word.lower()

        # Default tagging
        if w in ["the", "a", "an"]:
            tag = "DT"
        elif w in ["is", "am", "are", "was", "were"]:
            tag = "VB"
        elif w in ["he", "she", "it", "they", "we", "i", "you"]:
            tag = "PRP"
        else:
            tag = "NN"   # Default: noun

        tagged.append([word, tag])

    # Step 2: Apply transformation rules

    for i in range(len(tagged)):

        word = tagged[i][0]
        tag = tagged[i][1]
        w = word.lower()

        # Rule 1:
        # If a word ends with "ing", change NN to VBG
        if w.endswith("ing") and tag == "NN":
            tagged[i][1] = "VBG"

        # Rule 2:
        # If a word ends with "ed", change NN to VBD
        elif w.endswith("ed") and tag == "NN":
            tagged[i][1] = "VBD"

        # Rule 3:
        # If a word ends with "ly", change NN to RB
        elif w.endswith("ly") and tag == "NN":
            tagged[i][1] = "RB"

        # Rule 4:
        # If a word follows "the", tag it as noun
        elif i > 0:
            previous_word = tagged[i - 1][0].lower()

            if previous_word == "the" and tag == "NN":
                tagged[i][1] = "NN"

    return tagged


# Input sentence
sentence = "The boy is playing quickly."

# Apply transformation-based tagging
result = transformation_tagging(sentence)

print("Sentence:")
print(sentence)

print("\nTransformation-Based POS Tags:")

for word, tag in result:
    print(word, "->", tag)