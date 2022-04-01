"""
Name: <Kate Culpepper>
<HW9>.py

Problem: <This program runs a series of functions, when put together 
 creates a game of hangman >

Certification of Authenticity:

I certify that this assignment is entirely my own work.

from graphics import *
import random


def get_words(file_name):
    in_file = open(file_name, "r")
    list_file = in_file.readlines()
    return list_file


def get_random_word(words):
    rand_word = words[random.randint(0, len(words) - 1)]
    rand_word = rand_word.strip()
    return rand_word


def letter_in_secret_word(letter, secret_word):
    if letter in secret_word:
        return True
    else:
        return False


def already_guessed(letter, guesses):
    if letter in guesses:
        return True
    else:
        return False


def make_hidden_secret(secret_word, guesses):
    secret = []
    secret_str = ""
    for j in range(0, len(secret_word)):
        secret.append('_')

    for i in guesses:
        for k in range(0, len(secret_word)):
            if secret_word[k] == i:
                secret[k] = i
    for z in secret:
        secret_str = secret_str + z + " "

    return secret_str.strip()


def won(guessed):
    if "_" in guessed:
        return False
    else:
        return True


def play_graphics(secret_word):
    width_px = 700
    height_px = 700
    win = GraphWin("Hang Man", width_px, height_px)
    width = 10
    height = 10
    win.setCoords(0, 0, width, height)

    gallows_one = Line(Point(3, 3), Point(7, 3))
    gallows_one.draw(win)
    gallows_two = Line(Point(5, 3), Point(5, 9))
    gallows_two.draw(win)
    gallows_three = Line(Point(5, 9), Point(3, 8))
    gallows_three.draw(win)

    chances = 6
    guess_list = []
    while won(make_hidden_secret(secret_word, guess_list)) == False and chances != 0:
        txt_instr = Text(Point(3.5, 2), " Guess a letter: ")
        txt_instr.draw(win)
        guess_entry = Entry(Point(5, 2), 10)
        guess_entry.draw(win)
        guess = guess_entry.getText()
        hidden_msg = Text(Point(5, 2.5), make_hidden_secret(secret_word, guess_list))
        hidden_msg.draw(win)

        if already_guessed(guess, guess_list) == False:
            guess_list.append(guess)
            guess_box = Text(Point(5, 9.5), "already guessed: " + str(guess_list))
            guess_box.draw(win)
            if letter_in_secret_word(guess, secret_word):
                if won(make_hidden_secret(secret_word, guess_list)):
                    break
                head = Circle(Point(3, 7.5), .5)
                head.draw(win)
                hidden_msg = Text(Point(5, 2.5), make_hidden_secret(secret_word, guess_list))
                hidden_msg.draw(win)

    win.getMouse()


def play_command_line(secret_word):
    user_instructions = "lets play a game of Hang Man!"
    print(user_instructions)

    chances = 6
    guess_list = []
    print("already guessed: " + str(guess_list))
    print("guesses remaining: " + str(chances))
    print(make_hidden_secret(secret_word, guess_list))

    while won(make_hidden_secret(secret_word, guess_list)) == False and chances != 0:
        guess = input("guess a letter: ")
        print(" ")
        if already_guessed(guess, guess_list) == False:
            guess_list.append(guess)
            print("already guessed: " + str(guess_list))

            if letter_in_secret_word(guess, secret_word):
                if won(make_hidden_secret(secret_word, guess_list)):
                    break
                print("guesses remaining: " + str(chances))
                print(make_hidden_secret(secret_word, guess_list))

            else:
                chances = chances - 1
                print("guesses remaining: " + str(chances))
                print(make_hidden_secret(secret_word, guess_list))

    if chances == 0:
        print("Sorry you did not guess the word.")
        print("the secret word was " + secret_word)
    else:
        print("Winner!")
        print(secret_word)


if __name__ == '__main__':
    # get_words('words.txt')
    # get_random_word(get_words('words.txt'))

    play_command_line(get_random_word(get_words('words.txt')))
    play_graphics(get_random_word(get_words('words.txt')))
