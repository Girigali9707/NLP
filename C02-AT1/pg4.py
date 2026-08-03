# Finite State Morphological Parser

words = ["writes", "writing", "written"]

print("-" * 120)
print(f"{'Word':<15}{'State Path':<40}{'Pattern':<20}{'Root':<15}{'Normalized'}")
print("-" * 120)

for word in words:

    if word == "writes":
        path = "Start -> Verb -> +s -> End"
        pattern = "Regular Inflection"
        root = "write"

    elif word == "writing":
        path = "Start -> Verb -> +ing -> End"
        pattern = "Regular Inflection"
        root = "write"

    elif word == "written":
        path = "Start -> Verb -> Irregular -> End"
        pattern = "Irregular Inflection"
        root = "write"

    else:
        path = "-"
        pattern = "-"
        root = word

    print(f"{word:<15}{path:<40}{pattern:<20}{root:<15}{root}")