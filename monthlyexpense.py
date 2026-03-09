from functools import reduce

# 1. Collect the data
expenses = []

print("--- Monthly Expense Tracker ---")
print("Enter your expenses (type 'done' when finished)")

while True:
    name = input("\nWhat is the expense?")
    if name.lower() == 'done':
        break

    try:
        cost = float(input(f"How much was the {name}? "))
        # Store as a dictionary so we keep the name and cost together
        expenses.append({'type': name, 'amount': cost})
    except ValueError:
        print("Please enter a valid number for the cost.")

# 2. Analyze the data (only if the list isn't empty)
if expenses:
    # Calculate Total
    total = reduce(lambda acc, curr: acc + curr['amount'], expenses, 0)

    # Find Highest - compares 'amount' but returns the whole dictionary
    highest = reduce(lambda a, b: a if a['amount'] > b['amount'] else b, expenses)

    # Find Lowest - compares 'amount' but returns the whole dictionary
    lowest = reduce(lambda a, b: a if a['amount'] < b['amount'] else b, expenses)

    # 3. Display Results
    print("\n--- Expense Analysis ---")
    print(f"Total Monthly Expenses: ${total:.2f}")
    print(f"Highest Expense: {highest['type']} (${highest['amount']:.2f})")
    print(f"Lowest Expense: {lowest['type']} (${lowest['amount']:.2f})")
else:
    print("No expenses were entered.")