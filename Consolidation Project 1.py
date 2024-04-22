# Consolidation Project: Mystery Word Guessing Game

import random

def choose_mystery_word(words):
    return random.choice(words)

def play_game(mystery_word):
    turns = 0
    words_guesses = 0
    guessed_letters = []

    print("Welcome to the Mystery Word Guessing Game")
    print("Rules: You have to guess the mystery word by guessing letters from the alphabet")
    print("Only three guesses are allowed in the process of finding out what the mystery word is")

    while words_guesses < 3:
        print("\nGuessed letters:", ', '.join(guessed_letters))
        letter = input("Guess a letter: ")

        while letter in guessed_letters or not letter.isalpha() or len(letter) != 1:
            letter = input("Invalid or already guessed. Guess a different letter: ")

        guessed_letters.append(letter)
        letter_count = mystery_word.count(letter)
        print(f"The letter '{letter}' appears {letter_count} times in the word.")
        turns += 1
        

