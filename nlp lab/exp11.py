# Simple Top-Down Parser for Context-Free Grammar

# Grammar:
# S  -> NP VP
# NP -> Det N
# VP -> V NP
# Det -> "the" | "a"
# N -> "boy" | "girl" | "ball"
# V -> "eats" | "sees"

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["ball"]],
    "V": [["eats"], ["sees"]]
}


# Top-down parser
def parse(symbol, words, position=0):

    # If symbol is a terminal word
    if symbol not in grammar:
        if position < len(words) and words[position] == symbol:
            return position + 1
        else:
            return None

    # Try each grammar rule
    for rule in grammar[symbol]:

        current_position = position
        success = True

        for item in rule:
            result = parse(item, words, current_position)

            if result is None:
                success = False
                break

            current_position = result

        if success:
            return current_position

    return None


# Input sentence
sentence = "the boy eats a ball"

# Tokenize
words = sentence.lower().split()

# Parse the sentence
result = parse("S", words)

print("Sentence:")
print(sentence)

if result == len(words):
    print("\nSentence is grammatically valid.")
else:
    print("\nSentence is NOT grammatically valid.")