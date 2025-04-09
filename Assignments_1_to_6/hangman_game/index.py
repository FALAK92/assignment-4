#project 5 : Hangman Game

import random

words = ["python", "java", "kotlin", "react"]
lives = 5
word = random.choice(words)
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("_" * len(word))

while lives > 0:
    guess = input("🔤 Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    if guess in word:
        print("✅ Good guess!")
    else:
        lives -= 1
        print("❌ Wrong guess! Lives left:", lives)

    current_state = "".join([letter if letter in guessed_letters else "_" for letter in word])
    print("Word:", current_state)

    if "_" not in current_state:
        print("🎉 Congratulations! You guessed the word:", word)
        break

# Game over message only when lives are over
if lives == 0:
    print("💀 Game over! The word was:", word)
