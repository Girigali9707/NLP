# ==========================================
# Simple FOPC Parser
# First-Order Predicate Calculus
# ==========================================

import re


# ------------------------------------------
# Parse a predicate
# Example: P(x)
# Example: Likes(John, Mary)
# ------------------------------------------

def parse_predicate(expression):

    pattern = r'^([A-Za-z][A-Za-z0-9_]*)\((.*?)\)$'

    match = re.match(pattern, expression.strip())

    if match:

        predicate = match.group(1)
        arguments = match.group(2).split(",")

        arguments = [arg.strip() for arg in arguments]

        return {
            "type": "PREDICATE",
            "name": predicate,
            "arguments": arguments
        }

    return None


# ------------------------------------------
# Parse FOPC expression
# ------------------------------------------

def parse_fopc(expression):

    expression = expression.strip()

    # NOT
    if expression.startswith("NOT "):

        sub_expression = expression[4:].strip()

        return {
            "type": "NOT",
            "expression": parse_fopc(sub_expression)
        }

    # AND
    if " AND " in expression:

        parts = expression.split(" AND ", 1)

        return {
            "type": "AND",
            "left": parse_fopc(parts[0]),
            "right": parse_fopc(parts[1])
        }

    # OR
    if " OR " in expression:

        parts = expression.split(" OR ", 1)

        return {
            "type": "OR",
            "left": parse_fopc(parts[0]),
            "right": parse_fopc(parts[1])
        }

    # FORALL
    match = re.match(
        r'^FORALL\s+([a-zA-Z])\s+(.+)$',
        expression
    )

    if match:

        variable = match.group(1)
        sub_expression = match.group(2)

        return {
            "type": "FORALL",
            "variable": variable,
            "expression": parse_fopc(sub_expression)
        }

    # EXISTS
    match = re.match(
        r'^EXISTS\s+([a-zA-Z])\s+(.+)$',
        expression
    )

    if match:

        variable = match.group(1)
        sub_expression = match.group(2)

        return {
            "type": "EXISTS",
            "variable": variable,
            "expression": parse_fopc(sub_expression)
        }

    # Predicate
    predicate = parse_predicate(expression)

    if predicate:
        return predicate

    return {
        "type": "ERROR",
        "expression": expression
    }


# ------------------------------------------
# Display parsed structure
# ------------------------------------------

def display(tree, level=0):

    space = "  " * level

    if tree["type"] == "PREDICATE":

        print(
            space + "Predicate:",
            tree["name"]
        )

        print(
            space + "Arguments:",
            tree["arguments"]
        )

    elif tree["type"] == "NOT":

        print(space + "Operator: NOT")
        display(tree["expression"], level + 1)

    elif tree["type"] == "AND":

        print(space + "Operator: AND")

        print(space + "Left:")
        display(tree["left"], level + 1)

        print(space + "Right:")
        display(tree["right"], level + 1)

    elif tree["type"] == "OR":

        print(space + "Operator: OR")

        print(space + "Left:")
        display(tree["left"], level + 1)

        print(space + "Right:")
        display(tree["right"], level + 1)

    elif tree["type"] == "FORALL":

        print(
            space + "Quantifier: FORALL"
        )

        print(
            space + "Variable:",
            tree["variable"]
        )

        display(
            tree["expression"],
            level + 1
        )

    elif tree["type"] == "EXISTS":

        print(
            space + "Quantifier: EXISTS"
        )

        print(
            space + "Variable:",
            tree["variable"]
        )

        display(
            tree["expression"],
            level + 1
        )

    else:

        print(
            space + "Invalid Expression:",
            tree["expression"]
        )


# ------------------------------------------
# Test FOPC expressions
# ------------------------------------------

expressions = [
    "P(x)",
    "Likes(John, Mary)",
    "P(x) AND Q(x)",
    "P(x) OR Q(x)",
    "NOT P(x)",
    "FORALL x P(x)",
    "EXISTS x Likes(x, John)"
]


# ------------------------------------------
# Run parser
# ------------------------------------------

for expression in expressions:

    print("\n" + "=" * 50)

    print("Expression:")
    print(expression)

    tree = parse_fopc(expression)

    print("\nParsed Structure:")
    display(tree)