# ==========================================
# Information Retrieval using TF-IDF
# ==========================================

import math
import re
from collections import Counter


# ------------------------------------------
# Documents
# ------------------------------------------

documents = [
    "Python is a popular programming language",
    "Python is used for data science and machine learning",
    "Machine learning is a part of artificial intelligence",
    "Information retrieval uses text processing",
    "Python programming is useful for information retrieval"
]


# Query
query = "Python programming"


# ------------------------------------------
# Preprocessing
# ------------------------------------------

def tokenize(text):
    text = text.lower()
    return re.findall(r'\b\w+\b', text)


tokenized_documents = [
    tokenize(doc)
    for doc in documents
]

tokenized_query = tokenize(query)


# ------------------------------------------
# Calculate TF
# ------------------------------------------

def calculate_tf(words):

    count = Counter(words)
    total_words = len(words)

    tf = {}

    for word, frequency in count.items():
        tf[word] = frequency / total_words

    return tf


# ------------------------------------------
# Calculate IDF
# ------------------------------------------

def calculate_idf(documents):

    N = len(documents)

    vocabulary = set()

    for document in documents:
        vocabulary.update(document)

    idf = {}

    for word in vocabulary:

        document_count = sum(
            1 for document in documents
            if word in document
        )

        idf[word] = math.log(
            N / document_count
        )

    return idf


# ------------------------------------------
# Calculate TF-IDF
# ------------------------------------------

idf = calculate_idf(tokenized_documents)

tfidf_documents = []

for document in tokenized_documents:

    tf = calculate_tf(document)

    tfidf = {}

    for word in document:
        tfidf[word] = tf[word] * idf[word]

    tfidf_documents.append(tfidf)


# ------------------------------------------
# Query TF-IDF
# ------------------------------------------

query_tf = calculate_tf(tokenized_query)

query_tfidf = {}

for word in tokenized_query:

    if word in idf:
        query_tfidf[word] = query_tf[word] * idf[word]


# ------------------------------------------
# Calculate document score
# ------------------------------------------

def document_score(document_tfidf, query_tfidf):

    score = 0

    for word in query_tfidf:

        if word in document_tfidf:
            score += (
                query_tfidf[word] *
                document_tfidf[word]
            )

    return score


# ------------------------------------------
# Rank documents
# ------------------------------------------

results = []

for i, document in enumerate(documents):

    score = document_score(
        tfidf_documents[i],
        query_tfidf
    )

    results.append((i + 1, document, score))


# Sort by score
results.sort(
    key=lambda x: x[2],
    reverse=True
)


# ------------------------------------------
# Display Results
# ------------------------------------------

print("Query:")
print(query)

print("\nDocument Ranking:")
print("-" * 70)

for rank, document, score in results:

    print(
        f"Rank {rank}: Score = {score:.4f}"
    )

    print("Document:", document)
    print()