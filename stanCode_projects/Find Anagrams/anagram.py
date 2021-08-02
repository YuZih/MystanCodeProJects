"""
File: anagram.py
Name: Yuzu
----------------------------------
This program recursively finds all the anagram(s)
for the word input by user and terminates when the
input string matches the EXIT constant defined
at line 19

If you correctly implement this program, you should see the
number of anagrams for each word listed below:
    * arm -> 3 anagrams
    * contains -> 5 anagrams
    * stop -> 6 anagrams
    * tesla -> 10 anagrams
    * spear -> 12 anagrams
"""

import time                   # This file allows you to calculate the speed of your algorithm
from collections import Counter
import sys


# Constants
FILE = 'dictionary.txt'       # This is the filename of an English dictionary
EXIT = '-1'                   # Controls when to stop the loop


def main():
    """
    Features:
        * This code will find all the anagrams.
        * No matter how long the string inputted is, it costs almost the same time.
         (The time of this algorithm costs will not be affected by the length of string inputted.)

    Process:
        1. User inputs a string to search.
        2. While reading the dictionary, find anagrams at the same time.
        3. The method of finding anagrams: (1) same letter type (2) same letter numbers
        4. The method of speeding algorithm up:
            (1) Distinguish the length of inputted string first.
            (2) Check whether the types of letter in the inputted string are matched to the word in dictionary or not.
            (3) Check whether the length of inputted string equals to the word in dictionary or not.
            (4) Check whether the letter numbers of inputted string are matched to the word in dictionary or not.
        5. Print all anagrams and how long the algorithm costs
    """
    print(f'Welcome to stanCode "Anagram Generator" (or {EXIT} to quit)')
    while True:
        # user input a string to search
        inputted = str(input('Find anagrams for: '))

        # start to count time
        start = time.time()

        # end of finding
        if inputted == EXIT:
            break

        # pre-setting
        len_inputted = len(inputted)             # if input "tree", then len_inputted is 4.
        letter_type_inputted = set(inputted)     # if input "tree", then letter_type_inputted is {t, r, e}.
        letter_num_inputted = Counter(inputted)  # if input "tree", then letter_num_inputted is {t:1, r:1, e:2}.
        lst_anagram = []                         # list of all anagrams

        # read dictionary and also find anagrams
        with open(FILE, 'r') as dictionary:
            find_anagram(inputted, dictionary, len_inputted, letter_type_inputted, letter_num_inputted, lst_anagram)

        # end of counting time and print how long the algorithm costs
        end = time.time()
        print('----------------------------------')
        print(f'The speed of your anagram algorithm: {end-start} seconds.')


def find_anagram(inputted, dictionary, len_inputted, letter_type_inputted, letter_num_inputted, lst_anagram):
    # pre-setting
    sys.stdout.write('Searching...\n')
    inputted_0 = inputted[0]

    # when inputted string is short (len <= 4)
    if len_inputted <= 4:

        # (length == 1)
        if len_inputted == 1:
            for line in dictionary:
                if inputted_0 in line:
                    if len(line) == len_inputted + 1:
                        word = line.strip()
                        when_found(word, lst_anagram)

        # (length == 2)
        elif len_inputted == 2:
            inputted_1 = inputted[1]
            for line in dictionary:
                if inputted_0 in line and inputted_1 in line:
                    if len(line) == len_inputted + 1:
                        word = line.strip()
                        if set(word) == letter_type_inputted:
                            when_found(word, lst_anagram)

        # (length == 3)
        elif len_inputted == 3:
            inputted_1 = inputted[1]
            inputted_2 = inputted[2]
            for line in dictionary:
                if inputted_0 in line and inputted_1 in line and inputted_2 in line:
                    if len(line) == len_inputted + 1:
                        word = line.strip()
                        if set(word) == letter_type_inputted:
                            when_found(word, lst_anagram)

        # (length == 4)
        else:
            inputted_1 = inputted[1]
            inputted_2 = inputted[2]
            inputted_3 = inputted[3]
            for line in dictionary:
                if inputted_0 in line and inputted_1 in line and inputted_2 in line and inputted_3 in line:
                    if len(line) == len_inputted + 1:
                        word = line.strip()
                        if set(word) == letter_type_inputted:
                            when_found(word, lst_anagram)

    # when inputted string is long (len >= 5)
    else:
        inputted_1 = inputted[1]
        inputted_2 = inputted[2]
        inputted_3 = inputted[3]
        inputted_4 = inputted[4]

        # no repeated letters
        if len_inputted == len(letter_type_inputted):
            for line in dictionary:
                if inputted_0 in line and inputted_1 in line and inputted_2 in line:
                    if inputted_3 in line and inputted_4 in line:
                        if len(line) == len_inputted + 1:
                            word = line.strip()
                            if set(word) == letter_type_inputted:
                                when_found(word, lst_anagram)
        # some letters repeated
        else:
            for line in dictionary:
                if inputted_0 in line and inputted_1 in line and inputted_2 in line:
                    if inputted_3 in line and inputted_4 in line:
                        if len(line) == len_inputted + 1:
                            word = line.strip()
                            if set(word) == letter_type_inputted and Counter(word) == letter_num_inputted:
                                when_found(word, lst_anagram)
    sys.stdout.write(f'{len(lst_anagram)} anagrams: {lst_anagram}\n')


def when_found(word, lst_anagram):
    """
    If found the word is a anagram, print the anagram and append the word to the lst_anagram.
    """
    sys.stdout.write(f'Found: {word} \n')
    sys.stdout.write('Searching... \n')
    lst_anagram.append(word)


if __name__ == '__main__':
    main()
