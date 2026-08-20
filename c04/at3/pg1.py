sentence = "The student reads the book."

print("Sentence:", sentence)

print("\nCFG Representation:")
print("S")
print("├── NP")
print("│   ├── The")
print("│   └── student")
print("└── VP")
print("    ├── reads")
print("    └── NP")
print("        ├── the")
print("        └── book")

print("\nDependency Representation:")
print("reads -> student : subject")
print("reads -> book : object")
print("student -> The : determiner")
print("book -> the : determiner")