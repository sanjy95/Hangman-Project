import random

# Word list and secret word
word_list = ["mango", "banana", "strawberry", "pineapple", "grape"]
word = random.choice(word_list)

# Step 1: Define check_guess function
def check_guess(guess):
    guess = guess.lower()  # Step 2: Convert to lowercase
    if guess in word:      # Step 3: Check if guess is in word
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# Step 1: Define ask_for_input function
def ask_for_input():
    while True:
        guess = input("Please enter a single letter: ")  # Ask user for input
        if len(guess) == 1 and guess.isalpha():          # Validate input
            break
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")
    
    check_guess(guess)  # Step 3: Call check_guess with the valid guess

# Step 4: Call the ask_for_input function to run the program
ask_for_input()

