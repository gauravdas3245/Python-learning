number = 153
temp = number
total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** 3
    temp //= 10

if total == number:
    print("Armstrong number")
else:
    print("Not an Armstrong number")