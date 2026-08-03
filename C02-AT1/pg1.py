# Morphological Analysis Pipeline

words = ["connected", "connecting", "connection"]

print("-" * 90)
print(f"{'Word':<15}{'Root':<15}{'Suffix':<15}{'Type':<20}{'Normalized'}")
print("-" * 90)

for word in words:
    if word.endswith("ed"):
        root = word[:-2]
        suffix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        root = word[:-3]
        suffix = "ing"
        mtype = "Inflectional"

    elif word.endswith("ion"):
        root = word[:-3]
        suffix = "ion"
        mtype = "Derivational"

    else:
        root = word
        suffix = "-"
        mtype = "-"

    # Normalize to common base
    if root.startswith("connect"):
        normalized = "connect"
    else:
        normalized = root

    print(f"{word:<15}{root:<15}{suffix:<15}{mtype:<20}{normalized}")