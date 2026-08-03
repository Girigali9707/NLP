# Stemming Based Preprocessing

words = ["played", "player", "playing"]

print("-" * 100)
print(f"{'Word':<15}{'Stem':<15}{'Removed':<15}{'Type':<20}{'Normalized'}")
print("-" * 100)

for word in words:

    if word.endswith("ed"):
        stem = word[:-2]
        affix = "ed"
        mtype = "Inflectional"

    elif word.endswith("ing"):
        stem = word[:-3]
        affix = "ing"
        mtype = "Inflectional"

    elif word.endswith("er"):
        stem = word[:-2]
        affix = "er"
        mtype = "Derivational"

    else:
        stem = word
        affix = "-"
        mtype = "-"

    normalized = "play"

    print(f"{word:<15}{stem:<15}{affix:<15}{mtype:<20}{normalized}")