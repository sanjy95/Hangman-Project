import random

class Hangman:
    """
    A class representing the Hangman game logic.

    Attributes:
        _word (str): The secret word to guess.
        _word_guessed (list): Current state of guessed letters.
        _num_letters (int): Number of unique letters remaining to guess.
        num_lives (int): Lives remaining.
        word_list (list): List of potential words.
        _guessed_letters (list): All previously guessed letters.
    """

    def __init__(self, word_list, num_lives=5):
        """
        Initializes the game with a random word and sets initial state.

        Args:
            word_list (list): List of words to choose from.
            num_lives (int, optional): Starting number of lives. Defaults to 5.
        """
        self._word = random.choice(word_list)
        self._word_guessed = ['_' for _ in self._word]
        self._num_letters = len(set(self._word))
        self.num_lives = num_lives
        self.word_list = word_list
        self._guessed_letters = []

    def _reveal_letters(self, guess):
        """
        Reveals all matching letters in the guessed word.

        Args:
            guess (str): The letter guessed correctly.
        """
        for i, letter in enumerate(self._word):
            if letter == guess:
                self._word_guessed[i] = guess
        self._num_letters -= 1

    def _is_valid_input(self, guess):
        """
        Validates that the guess is a single alphabetical character.

        Args:
            guess (str): The user's input.

        Returns:
            bool: True if valid, False otherwise.
        """
        return len(guess) == 1 and guess.isalpha()

    def _is_duplicate_guess(self, guess):
        """
        Checks if the guess was already made.

        Args:
            guess (str): The letter guessed.

        Returns:
            bool: True if already guessed, False otherwise.
        """
        return guess in self._guessed_letters

    def _update_state_on_guess(self, guess):
        """
        Updates the game state based on the guess.

        Args:
            guess (str): The letter guessed.
        """
        guess = guess.lower()

        if guess in self._word:
            print(f"Good guess! '{guess}' is in the word.")
            self._reveal_letters(guess)
        else:
            self.num_lives -= 1
            print(f"Sorry, '{guess}' is not in the word.")
            print(f"You have {self.num_lives} lives left.")

        self._display_word_state()

    def _display_word_state(self):
        """Displays the current state of the word being guessed."""
        print("Current word: ", " ".join(self._word_guessed))

    def ask_for_input(self):
        """
        Handles user input: validation, duplicate checking, and game update.
        """
        while True:
            guess = input("Please enter a single letter: ").lower()

            if not self._is_valid_input(guess):
                print("Invalid letter. Please, enter a single alphabetical character.")
            elif self._is_duplicate_guess(guess):
                print("You already tried that letter!")
            else:
                self._update_state_on_guess(guess)
                self._guessed_letters.append(guess)
                break


def play_game(word_list):
    """
    Starts and manages the game loop.

    Args:
        word_list (list): List of possible words.
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
