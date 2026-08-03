# Finite State Machine for Morphological Parsing
# Generate plural forms of English nouns

def plural_fsm(word):
    state = "START"

    print(f"\nProcessing Word: {word}")
    print("State Transitions:")

    # Rule 1: Ends with s, x, z, ch, sh
    if word.endswith(("s", "x", "z", "ch", "sh")):
        print("START --> CHECK_ENDING")
        print("CHECK_ENDING --> ADD_ES")
        plural = word + "es"
        print("ADD_ES --> FINAL")

    # Rule 2: Ends with consonant + y
    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        print("START --> CHECK_ENDING")
        print("CHECK_ENDING --> REPLACE_Y_IES")
        plural = word[:-1] + "ies"
        print("REPLACE_Y_IES --> FINAL")

    # Rule 3: Default rule
    else:
        print("START --> CHECK_ENDING")
        print("CHECK_ENDING --> ADD_S")
        plural = word + "s"
        print("ADD_S --> FINAL")

    return plural


# Input words
words = ["book", "box", "city", "bus", "brush"]

print("-" * 50)
print(f"{'Singular':<15}{'Plural':<15}")
print("-" * 50)

for w in words:
    plural = plural_fsm(w)
    print(f"{w:<15}{plural:<15}")