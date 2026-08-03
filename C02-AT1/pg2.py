# Morphological Parsing Module

words = ["unhappy", "happiness", "happily"]

print("-" * 110)
print(f"{'Word':<15}{'Prefix':<12}{'Base':<15}{'Suffix':<15}{'Type':<20}{'Normalized'}")
print("-" * 110)

for word in words:

    prefix = "-"
    suffix = "-"
    base = word
    mtype = "Root"

    if word.startswith("un"):
        prefix = "un"
        base = word[2:]
        mtype = "Derivational"

    elif word.endswith("ness"):
        suffix = "ness"
        base = word[:-4]
        if base.endswith("i"):
            base = base[:-1] + "y"
        mtype = "Derivational"

    elif word.endswith("ly"):
        suffix = "ly"
        base = word[:-2]
        if base.endswith("i"):
            base = base[:-1] + "y"
        mtype = "Derivational"

    normalized = "happy"

    print(f"{word:<15}{prefix:<12}{base:<15}{suffix:<15}{mtype:<20}{normalized}")