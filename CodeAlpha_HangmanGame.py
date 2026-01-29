import random

# List of predefined words
words = ["python", "java", "apple", "chair", "laptop"]

# Randomly choose a word
secret_word = random.choice(words)

# Create a list of underscores for the guessed word
guessed_word = ["_"] * len(secret_word)

# Variables
attempts = 6
guessed_letters = []

print("🎮 Welcome to Hangman Game!")
print("Guess the word letter by letter.")
print("You have 6 incorrect guesses.\n")

# Game loop
while attempts > 0 and "_" in guessed_word:
    print("Word:", " ".join(guessed_word))
    print("Guessed letters:", guessed_letters)
    print("Remaining attempts:", attempts)

    guess = input("Enter a letter: ").lower()

    # Check for valid input
    if len(guess) != 1 or not guess.isalpha():
        print("❌ Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("⚠️ You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    # Check if guess is in the secret word
    if guess in secret_word:
        print("✅ Good guess!\n")
        for i in range(len(secret_word)):
            if secret_word[i] == guess:
                guessed_word[i] = guess
    else:
        print("❌ Wrong guess!\n")
        attempts -= 1

# Result
if "_" not in guessed_word:
    print("🎉 Congratulations! You guessed the word:", secret_word)
else:
    print("💀 Game Over! The word was:", secret_word)
