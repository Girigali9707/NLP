# QUESTION 1
# Constraint-Based Coreference Resolution

paragraph = """
John and Mary went to the park.
He brought a ball.
She wanted to play with it.
The dog chased him excitedly.
Finally, they all went home.
"""

print("ORIGINAL PARAGRAPH:")
print(paragraph)

# Referring expressions and possible antecedents
print("\n1. REFERRING EXPRESSIONS AND POSSIBLE ANTECEDENTS")

references = {
    "He": ["John", "Mary"],
    "She": ["John", "Mary"],
    "it": ["ball", "park"],
    "him": ["John", "Mary", "dog"],
    "they": ["John + Mary", "John + Mary + dog"]
}

for pronoun, candidates in references.items():
    print(pronoun, "->", candidates)


# Apply constraints
print("\n2. APPLYING CONSTRAINTS")

resolved = {
    "He": "John",
    "She": "Mary",
    "it": "ball",
    "him": "John",
    "they": "John + Mary + dog"
}

for pronoun, antecedent in resolved.items():
    print(pronoun, "->", antecedent)


# Constraint table
print("\n3. CONSTRAINT TABLE")

print("Pronoun | Candidate | Gender/Number | Recency | Semantic | Result")
print("-" * 70)

print("He      | John      | PASS          | PASS    | PASS     | SELECT")
print("He      | Mary      | FAIL          | PASS    | FAIL     | REJECT")

print("She     | John      | FAIL          | PASS    | FAIL     | REJECT")
print("She     | Mary      | PASS          | PASS    | PASS     | SELECT")

print("it      | ball      | PASS          | PASS    | PASS     | SELECT")
print("it      | park      | PASS          | FAIL    | FAIL     | REJECT")

print("him     | John      | PASS          | PASS    | PASS     | SELECT")
print("him     | Mary      | FAIL          | PASS    | FAIL     | REJECT")
print("him     | dog       | FAIL          | PASS    | FAIL     | REJECT")

print("they    | John+Mary+dog | PASS       | PASS    | PASS     | SELECT")


# Coreference chains
print("\n4. FINAL COREFERENCE CHAINS")

print("John -> He -> him -> they")
print("Mary -> She -> they")
print("ball -> it")
print("dog -> they")


# Rewritten paragraph
print("\n5. REWRITTEN PARAGRAPH")

rewritten = """
John and Mary went to the park.
John brought a ball.
Mary wanted to play with the ball.
The dog chased John excitedly.
Finally, John, Mary, and the dog all went home.
"""

print(rewritten)


# Constraint priority
print("\n6. CONSTRAINT PRIORITY")

print("1. Gender and Number Agreement")
print("2. Semantic Compatibility")
print("3. Recency")
print("4. Coherence")

print("\nIf recency is relaxed:")
print("The system can use semantic and grammatical information")
print("more strongly instead of always choosing the nearest noun.")