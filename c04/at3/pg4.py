subject = {
    "word": "student",
    "number": "singular"
}

verb = {
    "word": "reads",
    "number": "singular"
}

print("Subject:", subject["word"])
print("Verb:", verb["word"])

if subject["number"] == verb["number"]:
    print("Agreement: Correct")
else:
    print("Agreement: Error")

print("\nSubcategorization Frames:")

frames = {
    "eat": "NP",
    "give": "NP NP",
    "depend": "PP"
}

for verb, frame in frames.items():
    print(verb, "->", frame)