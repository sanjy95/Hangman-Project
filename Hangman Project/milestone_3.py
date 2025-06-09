import random

# List of words
word_list = ["mango", "banana", "strawberry", "pineapple", "grape"]

# Randomly choose a secret word
word = random.choice(word_list)

while True:
    # Ask the user for a letter
    guess = input("Please enter a single letter: ")

    # Validate the guess
    if len(guess) == 1 and guess.isalpha():
        # Check if the letter is in the word
        if guess in word:
            print(f"Good guess! '{guess}' is in the word.")
        else:
            print(f"Sorry, '{guess}' is not in the word. Try again.")
        break  # Exit the loop after one valid guess
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
