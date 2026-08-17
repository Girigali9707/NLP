# POS tagging

sentence1 = {
    "Book": "VB",
    "a": "DT",
    "flight": "NN",
    "ticket": "NN",
    "now": "RB"
}

sentence2 = {
    "This": "DT",
    "book": "NN",
    "is": "VBZ",
    "interesting": "JJ"
}

print("Sentence 1:")
for word, tag in sentence1.items():
    print(word, "/", tag)

print("\nSentence 2:")
for word, tag in sentence2.items():
    print(word, "/", tag)


# HMM probabilities
P_start_VB = 0.5
P_book_VB = 0.6

P_start_NN = 0.5
P_book_NN = 0.4

# Probability of book being Verb
prob_VB = P_start_VB * P_book_VB

# Probability of book being Noun
prob_NN = P_start_NN * P_book_NN

print("\nHMM Results:")
print("Probability of book as VB =", prob_VB)
print("Probability of book as NN =", prob_NN)

if prob_VB > prob_NN:
    print("Prediction: book = VB")
else:
    print("Prediction: book = NN")