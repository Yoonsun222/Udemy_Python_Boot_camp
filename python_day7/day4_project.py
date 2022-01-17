import random
import hangman_art
import hangman_words

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

end_of_game = False
word_list = hangman_words.word_list
chosen_word = random.choice(word_list)
word_length = len(chosen_word)


print(hangman_art.logo)
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = ["_"]*len(stages)
cnt = 0

while not end_of_game:
    guess = input("Guess a letter: ").lower()
    state = False

    if guess in display:
        print(f"You've already guessed {guess}")
        state = True

    for position in range(word_length):
        letter = chosen_word[position]
        if letter == guess:
            display[position] = letter
            state = True
        
            
    if state == False:
        cnt += 1
        print(f"You guessed {guess}, that's not in the word. You lose a life")

    if cnt == len(stages)-1:
        print("You lose")
        print(stages[-1-cnt])
        break

    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win.")

    print(stages[-1-cnt])
    