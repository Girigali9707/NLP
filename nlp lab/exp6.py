import random

# Sample training text
text = """
natural language processing is interesting
natural language processing is useful
language processing helps computers understand language
"""

# Tokenize text
words = text.split()

# Build Bigram Model
bigram = {}

for i in range(len(words) - 1):
    current = words[i]
    next_word = words[i + 1]

    if current not in bigram:
        bigram[current] = []

    bigram[current].append(next_word)

# Generate text
start_word = "natural"
generated = [start_word]

current = start_word

for i in range(10):
    if current in bigram:
        current = random.choice(bigram[current])
        generated.append(current)
    else:
        break

print("Generated Text:")
print(" ".join(generated))