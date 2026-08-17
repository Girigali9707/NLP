# Word Sense Disambiguation in E-Commerce

queries = {
    "Apple accessories": {
        "sense1": "Fruit",
        "sense2": "Technology Brand",
        "clicked_result": "iPhone Charger",
        "correct": "Technology Brand"
    },

    "Mouse wireless": {
        "sense1": "Animal",
        "sense2": "Computer Device",
        "clicked_result": "Bluetooth Mouse",
        "correct": "Computer Device"
    },

    "Java tutorial": {
        "sense1": "Island",
        "sense2": "Programming Language",
        "clicked_result": "Coding Lessons",
        "correct": "Programming Language"
    },

    "Python course": {
        "sense1": "Snake",
        "sense2": "Programming Language",
        "clicked_result": "Software Development Training",
        "correct": "Programming Language"
    }
}

print("WORD SENSE DISAMBIGUATION")
print("=" * 60)

for query, data in queries.items():

    print("\nQuery:", query)
    print("Possible Sense 1:", data["sense1"])
    print("Possible Sense 2:", data["sense2"])
    print("Clicked Result:", data["clicked_result"])
    print("Correct Sense:", data["correct"])

print("\nSEMANTIC CUES")
print("-" * 40)

print("Apple -> accessories + iPhone Charger -> Technology")
print("Mouse -> wireless + Bluetooth Mouse -> Computer Device")
print("Java -> tutorial + Coding Lessons -> Programming")
print("Python -> course + Software Development -> Programming")

print("\nWSD IMPACT")
print("-" * 40)
print("Correct sense -> Relevant results")
print("Incorrect sense -> Irrelevant results")
print("Better WSD -> Better recommendations and customer satisfaction")