import nltk
from nltk.tokenize import word_tokenize

# Download required resources (run once)
nltk.download('punkt')
nltk.download('punkt_tab')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')

text = "Natural Language Processing is an interesting subject."

# Tokenize
words = word_tokenize(text)

# POS Tagging
tagged_words = nltk.pos_tag(words)

print("Word\t\tPOS Tag")
print("-" * 30)

for word, tag in tagged_words:
    print(f"{word}\t\t{tag}")