numbers = [1, 2, 3, 4, 5, 6]

total = 0

for x in numbers:
    if x % 2 == 0:
        total += x

print("Sum of even numbers:", total)