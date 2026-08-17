# Syntax-Driven Semantic Analysis in Healthcare

sentences = [
    {
        "sentence": "Doctor prescribed medicine to patient.",
        "roles": {
            "Doctor": "Agent",
            "Medicine": "Theme/Medication",
            "Patient": "Recipient"
        }
    },
    {
        "sentence": "Patient reported severe headache.",
        "roles": {
            "Patient": "Experiencer",
            "Headache": "Symptom"
        }
    },
    {
        "sentence": "Nurse monitored patient continuously.",
        "roles": {
            "Nurse": "Agent",
            "Patient": "Patient/Theme"
        }
    },
    {
        "sentence": "Medicine reduced blood pressure.",
        "roles": {
            "Medicine": "Cause",
            "Blood Pressure": "Affected Entity"
        }
    }
]

print("SYNTAX-DRIVEN SEMANTIC ANALYSIS")
print("=" * 60)

for item in sentences:

    print("\nSentence:")
    print(item["sentence"])

    print("Semantic Roles:")

    for entity, role in item["roles"].items():
        print(entity, "->", role)

print("\nROLE ANALYSIS")
print("-" * 40)

print("Doctor -> Agent: Correct")
print("Medicine -> Theme/Medication: More appropriate")
print("Patient -> Recipient: Correct")
print("Headache -> Symptom: Correct")

print("\nPOSSIBLE PARSING ERRORS")
print("-" * 40)

print("1. Incorrect subject identification")
print("2. Incorrect object identification")
print("3. Wrong medical role assignment")
print("4. Incorrect relationship between doctor and patient")
print("5. Failure to detect symptoms or medical conditions")

print("\nIMPROVEMENT METHODS")
print("-" * 40)

print("1. Medical NLP models")
print("2. Dependency parsing")
print("3. Semantic Role Labeling")
print("4. Named Entity Recognition")
print("5. Medical dictionaries and ontologies")
print("6. Negation detection")