# First-Order Predicate Calculus for Smart Manufacturing

machines = {
    "M1": "Active",
    "M2": "Active",
    "M3": "Maintenance",
    "M4": "Active"
}

print("SMART MANUFACTURING")
print("-" * 40)

# Predicate representation
print("\nPredicate Representation:")

for machine, status in machines.items():
    if status == "Active":
        print(f"Active({machine})")
    else:
        print(f"Maintenance({machine})")

# Apply rules
print("\nApplying Rules:")

producing = []

for machine, status in machines.items():

    if status == "Active":
        print(f"Active({machine}) -> Producing({machine})")
        producing.append(machine)

    elif status == "Maintenance":
        print(f"Maintenance({machine}) -> NOT Producing({machine})")

print("\nCurrently Producing Machines:")
print(producing)

# Example product mapping
products = {
    "M1": "Engine",
    "M2": "Gear",
    "M3": "Gear",
    "M4": "Wheel"
}

print("\nAvailable Products:")

available = []

for machine in producing:
    product = products[machine]
    available.append(product)
    print(product, "is available")

print("\nMaintenance Analysis:")

if machines["M3"] == "Maintenance":
    print("M3 is under maintenance.")
    print("M3 is NOT producing.")
    print("Gear production through M3 is affected.")