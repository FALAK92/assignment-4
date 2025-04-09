#Guess My Number
#I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high
#Enter a new number: 25 Your guess is too low
#Enter a new number: 40 Your guess is too low
#Enter a new number: 45 Your guess is too low
#Enter a new number: 48 Congrats! The number was: 48

import random

# ANSI escape codes for colors
YELLOW = "\033[93m"
GREEN = "\033[92m"
RED = "\033[91m"
RESET = "\033[0m"

def guess_the_number():
    
    secret_number = random.randint(1, 99)  # generate a random number between 1 and 99
    print("🌟 I am thinking of a number between 1 and 99...")

    guess = None  # initialize guess to None
    attempts = 0  # initialize attempts to 0

    while guess != secret_number:
        try:
            guess = int(input(f"{YELLOW}🔢 Enter your guess: {RESET}"))   # input from users
            attempts += 1  # increment attempts by 1

            if guess < secret_number:
                print(f"{RED}📉 Your guess is too low! Try again.{RESET}")  # if guess is too low
            elif guess > secret_number:
                print(f"{RED}📈 Your guess is too high! Try again.{RESET}")  #if guess is too high

        except ValueError:
            print(f"{RED}⚠️ Invalid input! Please enter a valid number.{RESET}")  # if invalid input

    # when the user guesses the correct number
    print(f"{GREEN}🎉 Congrats! The number was {secret_number}! It took you {attempts} attempts! 🎯{RESET}")

if __name__ == '__main__':
    guess_the_number()


