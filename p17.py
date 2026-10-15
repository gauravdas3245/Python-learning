numbers = [12, 7, 9, 24, 16, 5, 8]

groups = {
    "Even": [],
    "Odd": []
}

for num in numbers:
    if num % 2 == 0:
        groups["Even"].append(num)
    else:
        groups["Odd"].append(num)

print("Even numbers:", groups["Even"])
print("Odd numbers:", groups["Odd"])