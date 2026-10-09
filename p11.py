numbers = [12, 45, 7, 89, 45, 56]

unique_numbers = list(set(numbers))
unique_numbers.sort()

if len(unique_numbers) >= 2:
    print("Second largest:", unique_numbers[-2])
else:
    print("Second largest does not exist")