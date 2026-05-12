import random

word_list = ["aardvark", "baboon", "camel"]
placeholder = ""

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(f"Here is the random word: {chosen_word}")
for char in chosen_word:
    placeholder += "_"

print(f"Place holder: {placeholder}")
display = placeholder
game_over = False

# TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
while not game_over:
    guess = input("Guess a letter: ").lower()

    if guess in display:
        print(f"This has already been gussed: {guess}")
    else:
        counter = 0
        for letter in chosen_word:
            if letter == guess:
                display = display[:counter] + guess + display[counter+1:]
                counter += 1
            else:
                print("Do nothing!")
                counter += 1
    if display == chosen_word:
         print("You won!")
         game_over = True

    print(f"Display String: {display}")