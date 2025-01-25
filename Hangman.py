import random
import word_list
chosen_word = random.choice(word_list.words)

display = ['_'] * len(chosen_word)

lives = 6

hangman_stages = [
    '''
     ------
     |    |
          |
          |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
          |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
     |    |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|    |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\   |
          |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\   |
    /     |
          |
    ========
    ''',
    '''
     ------
     |    |
     O    |
    /|\   |
    / \   |
          |
    ========
    '''
]


game_over = False

print("Welcome to Hangman!")
print(display)
wrong_letter= set()

while not game_over:
    guessed_letter = input("Guess a letter: ").lower()
    if len(guessed_letter) == 1:
      if guessed_letter in display:
        print(f"You've already guessed correct letter'{guessed_letter}'. Try a different letter.")
        continue

      for i in range(len(chosen_word)):
        if chosen_word[i] == guessed_letter:
            display[i] = guessed_letter
            print("Correct guess!")

      print(display)
      
      if guessed_letter in wrong_letter:
        print("You've already guessed that letter wrong! Try a different one.")
      elif guessed_letter not in chosen_word:
        lives -= 1
        wrong_letter.add(guessed_letter)
        print(f"Incorrect guess! You have {lives} lives left.")
        print(hangman_stages[6 - lives])

      if lives == 0:
        game_over = True
        print(f"You Lose! The word was: {chosen_word}")

      if '_' not in display:
        game_over = True
        print(f"You Win! The word is: {chosen_word}")
    else:
       print("Please enter exactly one letter.")