# QUESTION 2
# Constraint-Based Dialogue Generation

user_message = "I have an important exam tomorrow but I’m not able to concentrate."

print("USER:")
print(user_message)

# Required keywords
keywords = ["focus", "break", "confident"]

# Three possible responses
responses = [
    "Since your exam is tomorrow, take a short break and return with a clear focus on one topic at a time. You can concentrate better this way, and you should feel confident about your preparation.",

    "Because your exam is important, take a short break and study in small focused sessions to improve your concentration. Stay positive and confident—you can do this.",

    "If you are not able to concentrate, take a short break, relax, and start again with one simple topic. This can improve your focus and help you feel confident for your exam tomorrow."
]


# Display responses
print("\n1. THREE POSSIBLE RESPONSES")

for i, response in enumerate(responses, 1):
    print("\nResponse", i)
    print(response)


# Check constraints
print("\n2. CONSTRAINT CHECK")

for i, response in enumerate(responses, 1):

    response_lower = response.lower()

    # Check keywords
    found_keywords = []

    for keyword in keywords:
        if keyword in response_lower:
            found_keywords.append(keyword)

    # Count sentences
    sentence_count = response.count(".")

    # Check entity coherence
    exam = "exam" in response_lower
    concentration = "concentr" in response_lower

    print("\nResponse", i)
    print("Keywords:", found_keywords)
    print("Number of sentences:", sentence_count)
    print("Exam mentioned:", exam)
    print("Concentration mentioned:", concentration)


# Select best response
print("\n3. BEST RESPONSE")

print(responses[1])

print("\n4. JUSTIFICATION")

print("Response 2 is selected because:")
print("- It gives clear advice.")
print("- It encourages the student.")
print("- It uses focus, break and confident.")
print("- It maintains coherence.")
print("- It contains only 2 sentences.")
print("- It has a positive tone.")


# Effect of violating constraints
print("\n5. EFFECT OF VIOLATING CONSTRAINTS")

print("\nIf length constraint is violated:")
print("The response may become too long and less useful.")

print("\nIf positive tone is violated:")
print("The student may feel discouraged instead of motivated.")