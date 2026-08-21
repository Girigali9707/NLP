# ==========================================
# Subject-Verb Agreement Checker using CFG
# ==========================================

# Singular and plural subjects
singular_subjects = ["boy", "girl", "cat", "dog", "student"]
plural_subjects = ["boys", "girls", "cats", "dogs", "students"]

# Singular and plural verbs
singular_verbs = ["eats", "runs", "plays", "is"]
plural_verbs = ["eat", "run", "play", "are"]


# ------------------------------------------
# Function to check agreement
# ------------------------------------------

def check_agreement(sentence):

    words = sentence.lower().split()

    # Remove punctuation
    words = [word.strip(".,!?") for word in words]

    subject = None
    verb = None

    # Find subject
    for word in words:
        if word in singular_subjects:
            subject = word
            subject_type = "singular"
            break

        elif word in plural_subjects:
            subject = word
            subject_type = "plural"
            break

    # Find verb
    for word in words:
        if word in singular_verbs:
            verb = word
            verb_type = "singular"
            break

        elif word in plural_verbs:
            verb = word
            verb_type = "plural"
            break

    # Check whether subject and verb exist
    if subject is None or verb is None:
        return "Unable to identify subject or verb."

    print("Subject:", subject)
    print("Verb:", verb)
    print("Subject type:", subject_type)
    print("Verb type:", verb_type)

    # Check agreement
    if subject_type == verb_type:
        return "Sentence has correct subject-verb agreement."
    else:
        return "Sentence has incorrect subject-verb agreement."


# ------------------------------------------
# Test sentences
# ------------------------------------------

sentences = [
    "The boy eats.",
    "The boys eat.",
    "The girl runs.",
    "The girls run.",
    "The boy eat.",
    "The girls runs."
]


# ------------------------------------------
# Display results
# ------------------------------------------

for sentence in sentences:

    print("\n" + "=" * 40)
    print("Sentence:", sentence)

    result = check_agreement(sentence)

    print("Result:", result)