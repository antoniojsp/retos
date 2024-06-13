import random

# Define the word list with words of 5 letters or less
words = ["boy", "cat", "moon", "star", "ship"]

# Pick a random word from the list
word = random.choice(words)
print(word)

# Create a blank space for each letter in the word
blank_word = ["_"] * len(word)

# Define the game variables
incorrect_guesses = 0

# Play the game until the word is guessed or the user runs out of attempts
while "_" in blank_word and incorrect_guesses < 3:
    # Print the current state of the word
    print(" ".join(blank_word))

    # Ask the user to guess a letter
    print("Guess a letter: ")
    guess = input().strip().lower()

    # Check if the letter is in the word
    if guess in word:
        # Fill in all occurrences of the correct letter
        for i, letter in enumerate(word):
            if letter == guess:
                blank_word[i] = guess
        print("Correct!")
    else:
        # Keep track of the incorrect guess
        incorrect_guesses += 1
        print(f"Incorrect! {3 - incorrect_guesses} guesses left.")

    # Print a blank line for better readability between attempts
    print()

# If the word blanks are all filled correctly, print a congratulatory message
if "_" not in blank_word:
    print("Congratulations, you won! The word was:", word)
else:
    # If the user ran out of attempts, print a game over message
    print("Game over! The word was:", word)