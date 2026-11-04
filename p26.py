
def even_generator(start, end):
    for num in range(start, end + 1):
        if num % 2 == 0:
            yield num


numbers = even_generator(1, 10)

for value in numbers:
    print(value)
