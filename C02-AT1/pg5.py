# Porter Stemmer Demonstration

from nltk.stem import PorterStemmer

ps = PorterStemmer()

words = ["relational", "relation", "relate"]

print("-" * 110)
print(f"{'Word':<15}{'Applied Rule':<30}{'Intermediate':<20}{'Final Stem'}")
print("-" * 110)

for word in words:

    if word.endswith("ational"):
        rule = "Remove 'ational'"
        intermediate = word.replace("ational", "ate")

    elif word.endswith("ation"):
        rule = "Remove 'ation'"
        intermediate = word.replace("ation", "ate")

    else:
        rule = "General Porter Rule"
        intermediate = word

    stem = ps.stem(word)

    print(f"{word:<15}{rule:<30}{intermediate:<20}{stem}")