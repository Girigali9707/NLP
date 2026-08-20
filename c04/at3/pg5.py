sentence = "The student reads the book."
words = sentence.split()

print("Sentence:", sentence)

print("\nTransition-Based Parsing:")

for word in words:
    print("SHIFT ->", word)

print("Dependency tree created using local transitions.")

print("\nGraph-Based Parsing:")
print("Possible dependency edges evaluated.")
print("Best global dependency tree selected.")