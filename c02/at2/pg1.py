# Q1: Morphological Processing

words = ["analyzing", "analysis", "analytical"]

def analyze_word(word):
    if word == "analyzing":
        return {
            "Original": word,
            "Root": "analyze",
            "Affix": "-ing",
            "Type": "Inflectional",
            "Normalized": "analyze"
        }

    elif word == "analysis":
        return {
            "Original": word,
            "Root": "analyze",
            "Affix": "-sis",
            "Type": "Derivational",
            "Normalized": "analyze"
        }

    elif word == "analytical":
        return {
            "Original": word,
            "Root": "analyze",
            "Affix": "-ical",
            "Type": "Derivational",
            "Normalized": "analyze"
        }


print("Morphological Analysis Report")
print("-" * 80)

for word in words:
    result = analyze_word(word)

    print("Original Word :", result["Original"])
    print("Root Word     :", result["Root"])
    print("Affix         :", result["Affix"])
    print("Type          :", result["Type"])
    print("Normalized    :", result["Normalized"])
    print("-" * 80)