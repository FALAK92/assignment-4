#project 3: Guess the number game (user)
# 1 t0 100 numbers

import random

def user_guesses_number():
    print("🎯 Welcome to the Guess the Number Game!")
    print("I have picked a number between 1 and 100.")
    print("Can you guess what it is? 🤔")

    number = random.randint(1, 100)
    attempts = 0

    while True:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("🚫 Please enter a number between 1 and 100.")
                continue

            if guess < number:
                print("📉 Too low! Try again.")
            elif guess > number:
                print("📈 Too high! Try again.")
            else:
                print(f"🎉 Congratulations! You guessed the number {number} in {attempts} attempts.")
                break

        except ValueError:
            print("❗ Please enter a valid number.")

# Run the game
user_guesses_number()
