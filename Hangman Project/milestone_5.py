import random

class Hangman:
    """
    A class representing the Hangman game.

    Attributes:
        word (str): The secret word to guess.
        word_guessed (list): The current state of guessed letters.
        num_letters (int): Number of unique letters remaining.
        num_lives (int): Lives remaining.
        word_list (list): The list of possible words.
        list_of_guesses (list): All letters the player has guessed so far.
    """

    def __init__(self, word_list, num_lives=5):
        """Initialize the Hangman game with a random word and setup state."""
        self._word = random.choice(word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self.num_lives = num_lives
        self.word_list = word_list
        self._list_of_guesses = []

    def _reveal_correct_letters(self, guess):
        """Reveal all positions of the guessed letter in the secret word."""
        for index, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[index] = guess
        self._num_letters -= 1

    def _is_valid_guess(self, guess):
        """Check if the input is a single alphabetical character."""
        return len(guess) == 1 and guess.isalpha()

    def _has_already_been_guessed(self, guess):
        """Check if the letter has already been guessed."""
        return guess in self._list_of_guesses

    def _display_word_state(self):
        """Print the current state of the guessed word."""
        print("Current word: ", " ".join(self._word_guessed))

    def _check_guess(self, guess):
        """Evaluate the player's guess and update game state."""
        guess = guess.lower()
        if guess in self._word:
            print(f"Good guess! '{guess}' is in the word.")
            self._reveal_correct_letters(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")
        self._display_word_state()

    def ask_for_input(self):
        """Prompt the user to enter a guess, validate it, and check it."""
        while True:
            guess = input("Please enter a single letter: ")

            if not self._is_valid_guess(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self._has_already_been_guessed(guess):
                print("You already tried that letter!")
            else:
                self._check_guess(guess)
                self._list_of_guesses.append(guess)
                break


def play_game(word_list):
    """
    Runs the Hangman game using the given word list.
    """
    num_lives = 5
    game = Hangman(word_list, num_lives)

    while True:
        if game.num_lives == 0:
            print("You lost!")
            break
        elif game._num_letters > 0:
            game.ask_for_input()
        else:
            print("Congratulations. You won the game!")
            break


if __name__ == "__main__":
    words = ["mango", "banana", "grape"]
    play_game(words)
    