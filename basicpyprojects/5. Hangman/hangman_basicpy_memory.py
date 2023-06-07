# attempt to rebuild hangman from memory

import random
import string
from hangmanwords_basicpy import words

def get_valid_word(words):
    # pick a random word from list
    word = random.choice(words)
    # let's remove words with hypens or spaces
    while "-" in word or " " in word:
        word = random.choice(words)

    # let's return word in upper case for case sensitivity
    return word.upper()

def hangman():
    word = get_valid_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    lives = 10

    while len(word_letters) > 0 and lives > 0:
        print(f"You have {lives} life left.\nYou have used these letters: ", " ".join(used_letters))
        
        word_list = [letter if letter in used_letters else "-" for letter in word]
        print("Current word: ", " ".join(word_list))

        user_letter = input("Guess a letter: ").upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives -= 1
                print("Letter is not in the word")
        
        elif user_letter in used_letters:
            print("You've guessed that already..")

        else:
            print("That's an invalid guess")

    if lives == 0:
        print(f"You ran out of guesses. The word is '{word}'")
    else:
        print(f"You guessed '{word}' correctly!")

hangman()