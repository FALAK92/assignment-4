#Is project ka naam High-Low Game hai. Aapka maqsad ek simple Python console game banana hai jo user se guessing karwata hai:
#User ko ek number dikhaya jata hai aur computer ke paas bhi ek number hota hai (jo chhupa hota hai). 
# User ko guess karna hota hai ke uska number higher hai ya lower computer ke number se.



import random

# Constant for number of rounds
NUM_ROUNDS = 5

# Game starts here
print("Welcome to the High-Low Game!")
print("--------------------------------")

# Initialize score
score = 0

# Game loop
for round_num in range(1, NUM_ROUNDS + 1):
    print(f"Round {round_num}")
    
    # Generate numbers
    user_num = random.randint(1, 100)
    comp_num = random.randint(1, 100)
    
    # Show user's number only
    print(f"Your number is {user_num}")
    
    # Get user guess with input validation
    guess = input("Do you think your number is higher or lower than the computer's?: ").strip().lower()
    while guess not in ["higher", "lower"]:
        guess = input("Please enter either higher or lower: ").strip().lower()

    # Determine result
    if user_num > comp_num and guess == "higher":
        print(f"You were right! The computer's number was {comp_num}")
        score += 1
    elif user_num < comp_num and guess == "lower":
        print(f"You were right! The computer's number was {comp_num}")
        score += 1
    else:
        print(f"Aww, that's incorrect. The computer's number was {comp_num}")
    
    print(f"Your score is now {score}\n")

# Final messages
print("Thanks for playing!")

if score == NUM_ROUNDS:
    print("Wow! You played perfectly!")
elif score >= NUM_ROUNDS // 2:
    print("Good job, you played really well!")
else:
    print("Better luck next time!")
