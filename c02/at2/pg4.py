# Q4: Morphological Parsing and Normalization

words = ["activate", "activation", "reactivation"]

def parse_word(word):

    if word == "activate":
        return {
            "Original": word,
            "Prefix": "-",
            "Root": "activate",
            "Suffix": "-",
            "Sequence": "activate",
            "Meaning": "To make active",
            "Normalized": "activate"
        }

    elif word == "activation":
        return {
            "Original": word,
            "Prefix": "-",
            "Root": "activate",
            "Suffix": "-ion",
            "Sequence": "activate -> activation",
            "Meaning": "The process of becoming active",
            "Normalized": "activate"
        }

    elif word == "reactivation":
        return {
            "Original": word,
            "Prefix": "re-",
            "Root": "activate",
            "Suffix": "-ion",
            "Sequence": "activate -> reactivate -> reactivation",
            "Meaning": "The process of becoming active again",
            "Normalized": "activate"
        }


print("Morphological Parsing Report")
print("-" * 100)

for word in words:
    result = parse_word(word)

    print("Original Word :", result["Original"])
    print("Prefix        :", result["Prefix"])
    print("Root Word     :", result["Root"])
    print("Suffix        :", result["Suffix"])
    print("Sequence      :", result["Sequence"])
    print("Meaning       :", result["Meaning"])
    print("Normalized    :", result["Normalized"])
    print("-" * 100)