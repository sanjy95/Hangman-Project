# 🕹️ Hangman Game (Milestone Project)

## 📚 Table of Contents
- [Project Description](#project-description)
- [Installation](#installation)
- [Usage](#usage)
- [File Structure](#file-structure)
- [License](#license)

---

## 🎯 Project Description

This is a command-line **Hangman game** written in Python. The goal is to guess a randomly selected word one letter at a time. The player loses a life for each incorrect guess and wins if they guess all unique letters before running out of lives.

### ✅ Milestones Completed:

- **Milestone 2**: Basic list setup, random word selection, and input validation.
- **Milestone 3**: Added a loop to validate user guesses until a correct input is given. Checked if guessed letter is in the word.
- **Milestone 4**: 
  - Introduced a `Hangman` class with attributes and methods.
  - `check_guess()` updates `word_guessed` and tracks remaining lives and letters.
  - `ask_for_input()` handles user input, validates it, and tracks duplicate guesses.

### 🧠 What I Learned:
- Object-oriented programming (classes, methods, and attributes)
- Input validation and state management
- Working with lists, strings, and loops
- Structuring a Python program using milestones

---

## 💾 Installation

1. Make sure Python 3 is installed on your machine.
2. Clone this repo or download the project files:

``
📁 File Structure
bash
Copy
Edit
hangman-project/
├── milestone_2.py         # Random word selection and basic input validation
├── milestone_3.py         # Input loop and guess checking
├── milestone_4.py         # Hangman class with full logic for guessing and lives
├── README.md              # Project documentation