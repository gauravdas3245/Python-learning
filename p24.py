
import random

secret_number = random.randint(1, 20)
attempts = 0

while True:
    guess = int(input("Guess a number (1-20): "))
    attempts += 1

    if guess < secret_number:
        print("Too low!")

    elif guess > secret_number:
        print("Too high!")

    else:
        print("Correct guess!")
        print("Attempts:", attempts)
        break
