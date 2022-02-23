from operator import ge
from re import U
import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')

phonetic_dict = {row.letter: row.code for (index, row) in data.iterrows()}

# check user input word agains the dictionary


def generate_phonetic():
    user_word = input('Enter your name here: ').upper()
    try:
        nato_alphabet = [phonetic_dict[letter] for letter in user_word]

    except KeyError:
        print('Name should not containt any number or any space')
        generate_phonetic()
    else:
        print(nato_alphabet)


generate_phonetic()
