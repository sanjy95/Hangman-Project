import random
favorite_fruits = ["mango", "banana", "strawberry", "pineapple", "grape"]
word_list = ["mango", "banana", "strawberry", "pineapple", "grape"]
print(word_list)
random_word = random.choice(word_list)
word = random.choice(word_list)
print("Randomly selected word:", word)
guess = input("Please enter a single letter: ")
if len(guess) == 1 and guess.isalpha():
    print("Good guess!")
else:
    print("Oops! That is not a valid input.")
    