# 🕹️ Hangman Game

> **Started**: 08/06/2025  
> **Status**: In Progress – Up to Milestone 5

---

## 📚 Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

---

## 🎯 Project Description

**Hangman** is a classic word-guessing game where one player thinks of a word and the other tries to guess it within a limited number of attempts.  
In this Python implementation, the computer randomly selects a word from a list, and the user tries to guess it letter by letter.

---

### ✅ Milestones Completed:

#### Milestone 2:
- Created a word list and randomly selected one
- Took user input and validated it

#### Milestone 3:
- Created a loop that continuously asked the user for a valid letter
- Checked whether the guessed letter is in the word

#### Milestone 4:
- Created a `Hangman` class
- Defined attributes like `word_guessed`, `num_letters`, `num_lives`, and `list_of_guesses`
- Added `check_guess()` and `ask_for_input()` methods
- Updated guessed letters and tracked lives

#### Milestone 5:
- Created a `play_game()` function to run the full game loop
- Handled win and lose conditions
- Refactored for clean logic and better structure

---

### 🧠 What I Learned
- Object-oriented programming with Python (classes, methods, attributes)
- Code refactoring and modularity
- Input validation and state tracking
- How to structure multi-milestone projects cleanly
- Writing clean, readable code using best practices (SRP, naming, docstrings)

---

## 💾 Installation

1. Install Python 3 if not already installed
2. Clone the project:

```bash
git clone https://github.com/sanjy95/hangman-project.git
cd hangman-project

hangman-project/
├── milestone_2.py         # Basic word selection and input
├── milestone_3.py         # Input loop and guess checking
├── milestone_4.py         # Hangman class with full methods
├── milestone_5.py         # Final game loop (play_game function)
├── README.md              # Project documentation


