# Q2: Morphological Parsing

words = ["disagree", "agreement", "agreeable"]

def parse_word(word):

    if word == "disagree":
        return {
            "Original": word,
            "Prefix": "dis-",
            "Root": "agree",
            "Suffix": "-",
            "Type": "Derivational",
            "Meaning": "Not agree / opposite of agree",
            "Normalized": "agree"
        }

    elif word == "agreement":
        return {
            "Original": word,
            "Prefix": "-",
            "Root": "agree",
            "Suffix": "-ment",
            "Type": "Derivational",
            "Meaning": "The state or result of agreeing",
            "Normalized": "agree"
        }

    elif word == "agreeable":
        return {
            "Original": word,
            "Prefix": "-",
            "Root": "agree",
            "Suffix": "-able",
            "Type": "Derivational",
            "Meaning": "Pleasant or acceptable",
            "Normalized": "agree"
        }


print("Morphological Parsing Report")
print("-" * 90)

for word in words:
    result = parse_word(word)

    print("Original Word :", result["Original"])
    print("Prefix        :", result["Prefix"])
    print("Root Word     :", result["Root"])
    print("Suffix        :", result["Suffix"])
    print("Type          :", result["Type"])
    print("Meaning       :", result["Meaning"])
    print("Normalized    :", result["Normalized"])
    print("-" * 90)
