import random
stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["aardvark", "baboon", "camel"]
placeholder = ""

# TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word. Then print it.
chosen_word = random.choice(word_list)
print(chosen_word)
for char in chosen_word:
    placeholder += "_"

print(placeholder)
display = placeholder
game_over = False
lives = 6

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
                counter += 1
                print(stages[lives])
                lives -= 1
    print(display)
    if display == chosen_word:
         print("You win!")
         game_over = True
    if counter == 0:
        print("You lose!")
        game_over = True