# -*- coding: utf-8 -*-
import sys
import time
try:
    c_words, l_values = sys.argv[1], sys.argv[2]
    correct_word_dict, letter_val_dict = dict(), dict()
    correct_words = open(c_words, encoding='utf-8')
    letter_values = open(l_values, encoding='utf-8')
    key_list = []
    for line in correct_words:
        a = line.replace("\ufeff", ""); b = a.replace("\n", "")
        key, val = b.split(":")
        if "İ" in key or val:
            key, val = key.replace("İ", "i"), val.replace("İ", "i")
        if "I" in key or val:
            key, val = key.replace("I", "ı"), val.replace("I", "ı")
        key, val = key.lower(), val.lower()
        key_list.append(key)
        correct_word_dict[key] = val.split(",")
    for line in letter_values:
        a = line.replace("\ufeff", ""); b = a.replace("\n", "")
        key, val = b.split(":")
        if "I" or "İ" in key:
            key = key.replace("I", "ı").replace("İ", "i")
        letter_val_dict[key.lower()] = int(val)
    for key in key_list:
        print("Shuffled letters are: ", key, "Please guess words for these letters with minimum three letters")
        word_sum = []
        guessed_words = []
        start = time.time()
        while time.time()-start < 29:
            print("You have ", 30 - round(time.time() - start), " time")
            guess = input("Guessed word: ")
            if "İ" in guess:
                guess = guess.replace("İ", "i")
            if "I" in guess:
                guess = guess.replace("I", "ı")
            guess = guess.lower()
            if guess in correct_word_dict[key]:
                letter_sum = []
                if guess not in guessed_words:
                    if time.time() - start < 30:
                        guessed_words.append(guess)
                        for letter in guess:
                            letter_sum.append(letter_val_dict[letter])
                        word_sum.append(sum(letter_sum) * len(guess))
                else:
                    print("This word is guessed before")
            elif guess not in correct_word_dict[key]:
                print("Your guessed word is not a valid word")
        print("Time is up")
        if len(guessed_words) == 0:
            print("Score for ", key, " is ", sum(word_sum), "and no words were guessed")
        else:
            print("Score for ", key, " is ", sum(word_sum), " and guessed words are: ", "-".join(map(str, guessed_words)))
except IndexError:
    print("You must write two arguments for this program")
    quit()
