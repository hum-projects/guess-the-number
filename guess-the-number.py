import random

play = input("Do you want to play a guessing game, yes or no: ").lower()
if play == "no":
    print("🤫")
else:

    secret_number = random.randrange(1, 100)

    print("Guess a number between 1 and 100: ")

    guess = None

    while guess != secret_number:
        guess = int(input("Enter your guess: "))

        if guess == secret_number:
            print("CORRECT!\nYOU GUESSED THE NUMBER 🎉!")
        elif guess > secret_number:
            print("INCORRECT!\nYour guess is too high.")
        else:
            print("INCORRECT!\nYour guess is too low.")
        

