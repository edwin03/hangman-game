import random

word_list = ["aardvark", "baboon", "camel"]
placeholder = ""

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"Here is the random word: {chosen_word}")
for char in chosen_word:
    placeholder += "_"

print(f"Place holder: {placeholder}")

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
guess = input("Guess a letter: ").lower()

# TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word. Print "Right" if it
#  is, "Wrong" if it's not.
display = ""

for letter in chosen_word:
    if letter == guess:
        display += guess
    else:
        display += "_"

print(f"Display String: {display}")