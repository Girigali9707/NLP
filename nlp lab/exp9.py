import re

# Rule-based POS tagger using Regular Expressions

def pos_tag(sentence):

    # Tokenize the sentence
    words = re.findall(r"\b[\w']+\b", sentence)

    tagged_words = []

    for word in words:
        w = word.lower()

        # Determiner
        if re.match(r"^(a|an|the|this|that|these|those)$", w):
            tag = "DT"

        # Pronoun
        elif re.match(r"^(i|you|he|she|it|we|they|me|him|her|us|them)$", w):
            tag = "PRP"

        # Verb - common forms
        elif re.match(r"^(is|am|are|was|were|be|been|being)$", w):
            tag = "VB"

        # Verb ending with -ing
        elif re.match(r".*ing$", w):
            tag = "VBG"

        # Verb ending with -ed
        elif re.match(r".*ed$", w):
            tag = "VBD"

        # Adverb ending with -ly
        elif re.match(r".*ly$", w):
            tag = "RB"

        # Adjective endings
        elif re.match(r".*(ous|ful|able|ible|al|ive|less|ic)$", w):
            tag = "JJ"

        # Plural noun
        elif re.match(r".*s$", w):
            tag = "NNS"

        # Number
        elif re.match(r"^\d+$", w):
            tag = "CD"

        # Preposition
        elif re.match(r"^(in|on|at|by|with|from|to|for|of|under|over)$", w):
            tag = "IN"

        # Conjunction
        elif re.match(r"^(and|or|but|because|while|if)$", w):
            tag = "CC"

        # Default = noun
        else:
            tag = "NN"

        tagged_words.append((word, tag))

    return tagged_words


# Input sentence
sentence = "The boy is playing with a beautiful ball."

# POS tagging
result = pos_tag(sentence)

print("Sentence:")
print(sentence)

print("\nPOS Tags:")
for word, tag in result:
    print(word, "->", tag)