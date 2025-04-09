#Project 4: Rock-Paper-Scissors

import random

choices = ["rock", "paper", "scissors"]

player_choice = input("Enter rock, paper, or scissors: ").lower()

computer_choice = random.choice(choices)

if player_choice == computer_choice:
    print("It's a tie!")
elif player_choice == "rock" and computer_choice == "scissors":
    print("You win! Rock crushes scissors.")
elif player_choice == "paper" and computer_choice == "rock":
    print("You win! Paper covers rock.")
elif player_choice == "scissors" and computer_choice == "paper":
    print("You win! Scissors cuts paper.")
else:
    print("You lose! " + computer_choice.capitalize() + " beats " + player_choice + ".")

    
    