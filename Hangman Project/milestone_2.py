import random

def get_fruit_list():
    """Returns a list of favorite fruits."""
    return ["mango", "banana", "strawberry", "pineapple", "grape"]

def select_random_word(word_list):
    """Returns a randomly selected word from the word list."""
    return random.choice(word_list)

def get_user_guess():
    """Prompts the user to enter a single letter and returns it."""
    return input("Please enter a single letter: ")

def validate_guess(guess):
    """Validates if the guess is a single alphabetical character."""
    return len(guess) == 1 and guess.isalpha()

# ---- Main Logic ----

fruits = get_fruit_list()
print("Fruit list:", fruits)

selected_word = select_random_word(fruits)
print("Randomly selected word:", selected_word)

user_guess = get_user_guess()

if validate_guess(user_guess):
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
