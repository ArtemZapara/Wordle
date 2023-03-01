
import random
from string import ascii_letters

def get_secter_word():
    wordList = []
    with open("wordList.txt") as f:
        lines = f.readlines()
        for line in lines:
            word = line.strip().upper()
            if len(word) == 5 and all(letter in ascii_letters for letter in word):
                wordList.append(word)

    return random.choice(wordList)