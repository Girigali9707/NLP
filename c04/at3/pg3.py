sentence = "She saw the man with a telescope."

parses = {
    "She uses telescope": 0.70,
    "Man has telescope": 0.30
}

best = max(parses, key=parses.get)

print("Sentence:", sentence)

print("\nPossible interpretations:")

for interpretation, probability in parses.items():
    print(interpretation, "->", probability)

print("\nSelected interpretation:", best)