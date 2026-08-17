# Q5: Inflectional Morphology

words = ["create", "creates", "creating"]

def analyze_word(word):

    if word == "create":
        return {
            "Original": word,
            "Suffix": "-",
            "Category": "Base form",
            "Root": "create",
            "Normalized": "create"
        }

    elif word == "creates":
        return {
            "Original": word,
            "Suffix": "-s",
            "Category": "Third-person singular present",
            "Root": "create",
            "Normalized": "create"
        }

    elif word == "creating":
        return {
            "Original": word,
            "Suffix": "-ing",
            "Category": "Present participle",
            "Root": "create",
            "Normalized": "create"
        }


print("Inflectional Morphology Report")
print("-" * 90)

for word in words:
    result = analyze_word(word)

    print("Original Word :", result["Original"])
    print("Suffix        :", result["Suffix"])
    print("Category      :", result["Category"])
    print("Root Word     :", result["Root"])
    print("Normalized    :", result["Normalized"])
    print("-" * 90)