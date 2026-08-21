# ==========================================
# Probabilistic Context-Free Grammar Parser
# ==========================================

# PCFG Rules
grammar = {
    "S": [
        (["NP", "VP"], 1.0)
    ],

    "NP": [
        (["Det", "N"], 0.6),
        (["N"], 0.4)
    ],

    "VP": [
        (["V", "NP"], 0.7),
        (["V"], 0.3)
    ],

    "Det": [
        (["the"], 0.6),
        (["a"], 0.4)
    ],

    "N": [
        (["boy"], 0.4),
        (["girl"], 0.3),
        (["ball"], 0.3)
    ],

    "V": [
        (["eats"], 0.6),
        (["sees"], 0.4)
    ]
}


# ------------------------------------------
# PCFG Parser
# ------------------------------------------

def parse(symbol, words, position):

    # Check terminal word
    if symbol not in grammar:

        if position < len(words) and words[position] == symbol:
            return 1.0, {
                "symbol": symbol,
                "children": []
            }, position + 1

        return 0, None, position

    best_probability = 0
    best_tree = None
    best_position = position

    # Try every grammar rule
    for rule, rule_probability in grammar[symbol]:

        current_position = position
        children = []
        probability = rule_probability
        valid = True

        for item in rule:

            child_probability, child_tree, new_position = parse(
                item,
                words,
                current_position
            )

            if child_probability == 0:
                valid = False
                break

            probability *= child_probability
            children.append(child_tree)
            current_position = new_position

        # Keep the most probable parse
        if valid and probability > best_probability:

            best_probability = probability
            best_tree = {
                "symbol": symbol,
                "children": children
            }

            best_position = current_position

    return best_probability, best_tree, best_position


# ------------------------------------------
# Print Parse Tree
# ------------------------------------------

def print_tree(tree, level=0):

    print("  " * level + tree["symbol"])

    for child in tree["children"]:
        print_tree(child, level + 1)


# ------------------------------------------
# Input Sentence
# ------------------------------------------

sentence = "the boy eats a ball"

words = sentence.lower().split()


# ------------------------------------------
# Parse Sentence
# ------------------------------------------

probability, tree, position = parse("S", words, 0)


# ------------------------------------------
# Display Result
# ------------------------------------------

print("Sentence:")
print(sentence)

if tree is not None and position == len(words):

    print("\nSentence is valid.")

    print("Most Probable Parse Probability:")
    print(probability)

    print("\nMost Probable Parse Tree:")
    print_tree(tree)

else:

    print("\nSentence cannot be parsed.")