#project 2 : Guess the number game
# 1 to 100 numbers

def computer_guesses_number():
    print("🎮 Welcome to the Guess the Number Game!")
    print("Think of a number between 1 and 100, and I will try to guess it.")
    print("Just tell me if my guess is too High (H), too Low (L), or Correct (C).")

    low = 1
    high = 100
    attempts = 0

    while low <= high:
        guess = (low + high) // 2
        attempts += 1

        print(f"\n🤖 My guess is: {guess}")
        try:
            feedback = input("Is it (H)igh, (L)ow, or (C)orrect? ").strip().lower()

            if feedback == 'l':
                low = guess + 1
            elif feedback == 'h':
                high = guess - 1
            elif feedback == 'c':
                print(f"\n🎉 Yay! I guessed your number in {attempts} attempts.")
                break
            else:
                print("⚠️ Please respond only with 'H', 'L', or 'C'.")
                attempts -= 1  # Invalid input attempt count se minus
        except Exception as e:
            print("❌ Error:", e)
            attempts -= 1

    else:
        print("🤔 Are you sure you gave correct feedback?")

# Game ko run karo
computer_guesses_number()



    