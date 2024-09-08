#!/usr/bin/env python3

import random
import string

def load_words():
    return ["python", "programming", "computer", "algorithm", "database", "network", "software", "developer"]

def choose_word(words):
    return random.choice(words)

def get_masked_word(word, guessed_letters):
    return ''.join([letter if letter in guessed_letters else '_' for letter in word])

def play_game():
    words = load_words()
    word = choose_word(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    guessed_letters = set()

    lives = 6

    print("Welcome to the Word Guessing Game!")
    print(f"I'm thinking of a word that is {len(word)} letters long.")

    while len(word_letters) > 0 and lives > 0:
        print("\nYou have", lives, "lives left.")
        print("Available letters:", ' '.join(sorted(alphabet - guessed_letters)))
        print("Current word:", get_masked_word(word, guessed_letters))

        guess = input("Guess a letter: ").lower()
        if guess in alphabet - guessed_letters:
            guessed_letters.add(guess)
            if guess in word_letters:
                word_letters.remove(guess)
                print("Good guess!")
            else:
                lives = lives - 1
                print("Oops! That letter is not in the word.")
        elif guess in guessed_letters:
            print("You've already guessed that letter. Try again!")
        else:
            print("Invalid character. Please enter a letter.")

    if lives == 0:
        print("\nSorry, you died. The word was", word)
    else:
        print("\nCongratulations! You guessed the word", word, "!!")

if __name__ == "__main__":
    play_game()
