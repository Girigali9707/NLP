# QUESTION 3
# Constraint-Based Word Sense Disambiguation

sentence = "The bank by the river flooded after the storm, but it was saved by quick action."

print("SOURCE SENTENCE:")
print(sentence)


# Possible meanings
print("\n1. POSSIBLE MEANINGS OF 'BANK'")

print("Meaning 1: Financial Bank")
print("- Financial institution")
print("- Deals with money")

print("\nMeaning 2: River Bank")
print("- Land beside a river")
print("- Can flood")
print("- Located near a river")


# Context
print("\n2. CONTEXT WORDS")

context = ["river", "flooded", "storm"]

for word in context:
    print(word)


# WSD scoring
river_bank_score = 0
financial_bank_score = 0

for word in context:

    if word == "river":
        river_bank_score += 2

    elif word == "flooded":
        river_bank_score += 2

    elif word == "storm":
        river_bank_score += 1


print("\n3. WSD SCORES")

print("River Bank:", river_bank_score)
print("Financial Bank:", financial_bank_score)


# Resolve word sense
if river_bank_score > financial_bank_score:
    result = "River Bank"
else:
    result = "Financial Bank"

print("\n4. RESOLVED MEANING")
print("bank ->", result)


# Justification
print("\n5. JUSTIFICATION")

print("The words 'river', 'flooded', and 'storm' strongly indicate")
print("that 'bank' means the land beside a river.")


# Predicate Logic
print("\n6. PREDICATE LOGIC")

print("""
RiverBank(x)
River(r)
Location(x,r)
Storm(s)
Flood(x)
Caused(s,x)
QuickAction(a)
SavedBy(x,a)
""")


print("Complete representation:")

print("""
∃x ∃r ∃s ∃a [
    RiverBank(x)
    AND River(r)
    AND Location(x,r)
    AND Storm(s)
    AND Flood(x)
    AND Caused(s,x)
    AND QuickAction(a)
    AND SavedBy(x,a)
]
""")


# English paraphrase
print("\n7. SIMPLE ENGLISH PARAPHRASE")

print("The riverbank flooded after the storm, but quick action saved it.")


# RST Discourse Tree
print("\n8. RST-STYLE DISCOURSE TREE")

print("""
                 CONTRAST
                /        \\
               /          \\
        CLAUSE 1          CLAUSE 2
           |                  |
   Riverbank flooded     Quick action
    after the storm        saved it
""")


# Advantages
print("\n9. ADVANTAGES OF CONSTRAINT-BASED APPROACH")

print("1. Uses context to resolve ambiguity.")
print("2. Uses semantic compatibility.")
print("3. Maintains important entities.")
print("4. Preserves discourse structure.")
print("5. Produces more coherent output.")
print("6. Avoids selecting an incorrect common meaning.")