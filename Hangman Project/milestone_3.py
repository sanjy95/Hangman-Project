# milestone_3.py

# Step 1: Loop runs continuously
while True:
    # Step 2: Ask the user for input
    guess = input("Please enter a single letter: ")
    
    # Step 3: Validate input
    if len(guess) == 1 and guess.isalpha():
        # Step 4: Break the loop if valid
        print("Good guess!")
        break
    else:
        # Step 5: Print error message if invalid
        print("Invalid letter. Please, enter a single alphabetical character.")
