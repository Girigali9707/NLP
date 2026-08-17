# Q3: Morphology-Based Normalization

words = ["govern", "government", "governance"]

def normalize_word(word):

    if word == "govern":
        return {
            "Original": word,
            "Root": "govern",
            "Affix": "-",
            "Hierarchy": "govern",
            "Normalized": "govern"
        }

    elif word == "government":
        return {
            "Original": word,
            "Root": "govern",
            "Affix": "-ment",
            "Hierarchy": "govern -> government",
            "Normalized": "govern"
        }

    elif word == "governance":
        return {
            "Original": word,
            "Root": "govern",
            "Affix": "-ance",
            "Hierarchy": "govern -> governance",
            "Normalized": "govern"
        }


print("Morphological Normalization Report")
print("-" * 90)

for word in words:
    result = normalize_word(word)

    print("Original Word :", result["Original"])
    print("Root Word     :", result["Root"])
    print("Affix         :", result["Affix"])
    print("Hierarchy     :", result["Hierarchy"])
    print("Normalized    :", result["Normalized"])
    print("-" * 90)