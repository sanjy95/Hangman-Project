import random

def generate_random_word(word_choices):
    """Selects a random word from the list of available words."""
    return random.choice(word_choices)

def is_valid_letter_input(user_input):
    """Returns True if the input is a single alphabetical character."""
    return len(user_input) == 1 and user_input.isalpha()

def prompt_user_for_letter():
    """Prompts the user to enter a valid single letter."""
    while True:
        letter = input("Please enter a single letter: ")
        if is_valid_letter_input(letter):
            return letter.lower()
        else:
            print("Invalid letter. Please, enter a single alphabetical character.")

def evaluate_guess(guess, secret_word):
    """Checks if the guessed letter is in the secret word."""
    if guess in secret_word:
        print(f"Good guess! '{guess}' is in the word.")
    else:
        print(f"Sorry, '{guess}' is not in the word. Try again.")

# --- Main Execution ---

word_list = ["mango", "banana", "strawberry", "pineapple", "grape"]
secret_word = generate_random_word(word_list)
user_guess = prompt_user_for_letter()
evaluate_guess(user_guess, secret_word)
