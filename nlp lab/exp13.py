# ==========================================
# Parse Tree using Context-Free Grammar
# ==========================================

# Grammar
grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["ball"]],
    "V": [["eats"], ["sees"]]
}


# ------------------------------------------
# Parse Tree Function
# ------------------------------------------

def parse(symbol, words, position=0):

    # Terminal symbol
    if symbol not in grammar:

        if position < len(words) and words[position] == symbol:
            return {
                "symbol": symbol,
                "children": []
            }, position + 1

        return None, position

    # Try grammar rules
    for rule in grammar[symbol]:

        children = []
        current_position = position
        success = True

        for item in rule:

            tree, new_position = parse(
                item,
                words,
                current_position
            )

            if tree is None:
                success = False
                break

            children.append(tree)
            current_position = new_position

        if success:
            return {
                "symbol": symbol,
                "children": children
            }, current_position

    return None, position


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
# Generate Parse Tree
# ------------------------------------------

tree, position = parse("S", words)


# ------------------------------------------
# Display Result
# ------------------------------------------

print("Sentence:")
print(sentence)

print("\nParse Tree:")

if tree is not None and position == len(words):
    print_tree(tree)
else:
    print("No valid parse tree found.")