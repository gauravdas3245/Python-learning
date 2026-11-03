
def track_expenses(expenses):
    summary = {}

    for category, amount in expenses:
        if category in summary:
            summary[category] += amount
        else:
            summary[category] = amount

    return summary


expenses = [
    ("Food", 150),
    ("Travel", 80),
    ("Food", 100),
    ("Shopping", 300)
]

result = track_expenses(expenses)

total = 0

for category, amount in result.items():
    print(category, ":", amount)
    total += amount

print("Total Expense:", total)
