# Semantic Representation in Customer Support Chatbot

queries = {
    "Q1": {
        "representation": "ACTIVATE(Roaming, Customer)",
        "actual": "Activate Roaming",
        "predicted": "Activate Roaming"
    },
    "Q2": {
        "representation": "DEACTIVATE(CallerTune, Customer)",
        "actual": "Deactivate Caller Tune",
        "predicted": "Activate Caller Tune"
    },
    "Q3": {
        "representation": "QUERY(DataBalance, Customer)",
        "actual": "Query Data Balance",
        "predicted": "Query Data Balance"
    },
    "Q4": {
        "representation": "ACTIVATE(5GService, Customer)",
        "actual": "Activate 5G Service",
        "predicted": "Activate 5G Service"
    }
}

print("SEMANTIC REPRESENTATION ANALYSIS")
print("-" * 50)

for qid, data in queries.items():
    print("\n", qid)
    print("Representation:", data["representation"])
    print("Actual Intent:", data["actual"])
    print("Predicted Intent:", data["predicted"])

    if data["actual"] == data["predicted"]:
        print("Result: Correct")
    else:
        print("Result: ERROR")

print("\nAction-Object Relationships:")
print("ACTIVATE -> Roaming")
print("DEACTIVATE -> CallerTune")
print("QUERY -> DataBalance")
print("ACTIVATE -> 5GService")

print("\nSemantic Error:")
print("Q2 has an error.")
print("Actual: Deactivate Caller Tune")
print("Predicted: Activate Caller Tune")# Semantic Representation in Customer Support Chatbot

queries = {
    "Q1": {
        "representation": "ACTIVATE(Roaming, Customer)",
        "actual": "Activate Roaming",
        "predicted": "Activate Roaming"
    },
    "Q2": {
        "representation": "DEACTIVATE(CallerTune, Customer)",
        "actual": "Deactivate Caller Tune",
        "predicted": "Activate Caller Tune"
    },
    "Q3": {
        "representation": "QUERY(DataBalance, Customer)",
        "actual": "Query Data Balance",
        "predicted": "Query Data Balance"
    },
    "Q4": {
        "representation": "ACTIVATE(5GService, Customer)",
        "actual": "Activate 5G Service",
        "predicted": "Activate 5G Service"
    }
}

print("SEMANTIC REPRESENTATION ANALYSIS")
print("-" * 50)

for qid, data in queries.items():
    print("\n", qid)
    print("Representation:", data["representation"])
    print("Actual Intent:", data["actual"])
    print("Predicted Intent:", data["predicted"])

    if data["actual"] == data["predicted"]:
        print("Result: Correct")
    else:
        print("Result: ERROR")

print("\nAction-Object Relationships:")
print("ACTIVATE -> Roaming")
print("DEACTIVATE -> CallerTune")
print("QUERY -> DataBalance")
print("ACTIVATE -> 5GService")

print("\nSemantic Error:")
print("Q2 has an error.")
print("Actual: Deactivate Caller Tune")
print("Predicted: Activate Caller Tune")