# Porter Stemmer using NLTK

from nltk.stem import PorterStemmer

# Create Porter Stemmer object
ps = PorterStemmer()

# List of words
words = [
    "playing",
    "played",
    "plays",
    "player",
    "relational",
    "connection",
    "connected",
    "connecting",
    "happiness",
    "happily"
]

print("-" * 45)
print(f"{'Original Word':<20}{'Stem'}")
print("-" * 45)

# Perform stemming
for word in words:
    stem = ps.stem(word)
    print(f"{word:<20}{stem}")