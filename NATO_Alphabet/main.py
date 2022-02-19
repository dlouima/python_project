import pandas

data = pandas.read_csv('nato_phonetic_alphabet.csv')
alphabet = {letter.letter: letter.code for (
    index, letter) in data.iterrows()}

# check user input word agains the dictionary
user_word = input('Enter your name here: ').upper()
nato_alphabet = []
for letter in user_word:
    nato_alphabet.append(alphabet[letter])

# print data back to the user
print(nato_alphabet)
