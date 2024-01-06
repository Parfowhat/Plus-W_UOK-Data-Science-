import random

word_list = ["aardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
display = ["_" for _ in chosen_word]

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

lives = 6
guessed_letters = []

while "_" in display and lives > 0:
    guess = input("Guess a letter: ").lower()

    if guess in guessed_letters:
        print(f"You've already guessed the letter '{guess}'. Try again.")
        continue

    guessed_letters.append(guess)

    if guess in chosen_word:
        for i in range(len(chosen_word)):
            if chosen_word[i] == guess:
                display[i] = guess
    else:
        print(f"The letter '{guess}' is not in the word.")
        lives -= 1

    print(" ".join(display))
    if 0 <= lives < len(stages):
        print(stages[lives])
    else:
        print("Invalid number of lives.")

if "_" not in display:
    print("Congratulations! You've won.")
else:
    print(f"You lose. The word was '{chosen_word}'.")
