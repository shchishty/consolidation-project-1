# Consolidation Project: Mystery Word Guessing Game

import random

def choose_mystery_word(words):
    return random.choice(words)

def play_game(mystery_word):
    turns = 0
    words_guesses = 0
    guessed_letters = []

    print("Welcome to the Mystery Word Guessing Game")
    print("Rules for the game: You have to guess the mystery word by guessing letters from the alphabet")
    print("Only three guesses are allowed in this game")

    while words_guesses < 3:
        print("\nGuessed letters:", ', '.join(guessed_letters))
        letter = input("Guess a letter: ")

        while letter in guessed_letters or not letter.isalpha() or len(letter) != 1:
            letter = input("Invalid guess or already guessed. Guess a different letter: ")

        guessed_letters.append(letter)
        letter_count = mystery_word.count(letter)
        print(f"The letter '{letter}' appears {letter_count} times in the word.")
        turns += 1

        if input("Do you want to guess the whole word? (yes/no):") == 'yes':
            word_guess = input("Enter your mystery word guess: ")
            words_guesses += 1
            if word_guess == mystery_word:
                print("Congratulations! You have guessed the mystery word correctly!")
                print("Your score (number of turns): " + turns)
                return
        else:
            print("Wrong guess!")
            if words_guesses == 3:
                print("You have used all mystery word guesses and the game is over.")
                print(f"The correct word was: {mystery_word}")
                return
def main():
    mystery_words = ["horse", "mouse", "trace"]
    mystery_word = choose_mystery_word(mystery_words)
    print("\nA new game starts now!\n")

    play_game(mystery_word)

if __name__ == "__main__":
    main()