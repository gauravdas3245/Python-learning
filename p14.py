numbers = [4, 7, 2, 7, 4, 9]

for i in range(len(numbers)):
    found = False

    for j in range(i + 1, len(numbers)):
        if numbers[i] == numbers[j]:
            print("First repeating element:", numbers[i])
            found = True
            break

    if found:
        break
else:
    print("No repeating element found")