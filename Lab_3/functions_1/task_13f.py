import random

def guess_the_number():
    print("Hello! What is your name?")
    name = input()

    print(f"\nWell, {name}, I am thinking of a number between 1 and 20.")
    hidden_number = random.randint(1, 20)
    attempts = 0

    while True:
        print("\nTake a guess.")
        try:
            guess = int(input())
            attempts += 1

            if guess < hidden_number:
                print("Your guess is too low.")
            elif guess > hidden_number:
                print("Your guess is too high.")
            else:
                print(f"Good job, {name}! You guessed my number in {attempts} guesses!")
                break
        except ValueError:
            print("Please enter a valid number.")

guess_the_number()
