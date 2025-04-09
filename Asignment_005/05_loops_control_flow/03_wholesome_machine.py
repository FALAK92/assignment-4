#Write a Python program that asks the user to type a given affirmation exactly as shown.
# If they make a mistake, prompt them to try again until they enter it correctly.


AFFIRMATION = "I am strong, confident, and capable of achieving my dreams. ✨"

BLUE = "\033[94m"
RESET = "\033[0m"

def main():
    print(BLUE + "Please type the following affirmation: " + AFFIRMATION + RESET)

    user_feedback = input(BLUE)  
    while user_feedback != AFFIRMATION:  
        print(BLUE + "That was not the affirmation. Try again! 😊" + RESET)

        print(BLUE + "Please type the following affirmation: " + AFFIRMATION + RESET)
        user_feedback = input(BLUE)  

    print(BLUE + "That's right! You are amazing! 💙✨" + RESET)

if __name__ == '__main__':
    main()

