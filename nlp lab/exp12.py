# ==========================================
# Simple Earley Parser
# ==========================================

# Grammar:
# S  -> NP VP
# NP -> Det N
# VP -> V NP
# Det -> "the" | "a"
# N -> "boy" | "girl" | "ball"
# V -> "eats" | "sees"

grammar = {
    "S": [["NP", "VP"]],
    "NP": [["Det", "N"]],
    "VP": [["V", "NP"]],
    "Det": [["the"], ["a"]],
    "N": [["boy"], ["girl"], ["ball"]],
    "V": [["eats"], ["sees"]]
}

start_symbol = "S"


# ------------------------------------------
# Earley Parser
# ------------------------------------------

def earley_parser(words):

    n = len(words)

    # Chart: one list for every word position
    chart = [[] for _ in range(n + 1)]

    # State format:
    # (LHS, RHS, dot, start_position)

    # Add initial state
    chart[0].append(
        ("S'", ["S"], 0, 0)
    )

    # Process every chart position
    for i in range(n + 1):

        changed = True

        while changed:
            changed = False

            for state in list(chart[i]):

                lhs, rhs, dot, start = state

                # ----------------------------------
                # COMPLETER
                # ----------------------------------

                if dot == len(rhs):

                    for prev_state in list(chart[start]):

                        prev_lhs, prev_rhs, prev_dot, prev_start = prev_state

                        if (prev_dot < len(prev_rhs)
                                and prev_rhs[prev_dot] == lhs):

                            new_state = (
                                prev_lhs,
                                prev_rhs,
                                prev_dot + 1,
                                prev_start
                            )

                            if new_state not in chart[i]:
                                chart[i].append(new_state)
                                changed = True

                # ----------------------------------
                # PREDICTOR
                # ----------------------------------

                elif rhs[dot] in grammar:

                    next_symbol = rhs[dot]

                    for production in grammar[next_symbol]:

                        new_state = (
                            next_symbol,
                            production,
                            0,
                            i
                        )

                        if new_state not in chart[i]:
                            chart[i].append(new_state)
                            changed = True

        # ------------------------------------------
        # SCANNER
        # ------------------------------------------

        if i < n:

            for state in chart[i]:

                lhs, rhs, dot, start = state

                if dot < len(rhs):

                    next_symbol = rhs[dot]

                    # Check if next symbol is a terminal
                    if next_symbol not in grammar:

                        if words[i] == next_symbol:

                            new_state = (
                                lhs,
                                rhs,
                                dot + 1,
                                start
                            )

                            if new_state not in chart[i + 1]:
                                chart[i + 1].append(new_state)

    # ------------------------------------------
    # Check final state
    # ------------------------------------------

    final_state = (
        "S'",
        ["S"],
        1,
        0
    )

    return final_state in chart[n], chart


# ------------------------------------------
# Test Sentence
# ------------------------------------------

sentence = "the boy eats a ball"

words = sentence.lower().split()

result, chart = earley_parser(words)


# ------------------------------------------
# Display Result
# ------------------------------------------

print("Sentence:")
print(sentence)

if result:
    print("\nSentence is grammatically valid.")
else:
    print("\nSentence is NOT grammatically valid.")


# ------------------------------------------
# Display Earley Chart
# ------------------------------------------

print("\nEarley Chart:")

for i, states in enumerate(chart):

    print("\nChart[{}]".format(i))

    for state in states:

        lhs, rhs, dot, start = state

        before_dot = " ".join(rhs[:dot])
        after_dot = " ".join(rhs[dot:])

        if before_dot:
            before_dot += " "

        print(
            "  {} -> {}•{} , {}".format(
                lhs,
                before_dot,
                after_dot,
                start
            )
        )