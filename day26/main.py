import pandas as pd

nato_data = pd.read_csv("nato_phonetic_alphabet.csv")

nato_format = {row.letter: row.code for (index, row) in nato_data.iterrows()}
print(nato_format)


def nato():

    user_name = input("Enter a word: ").upper()
    try:
        name_in_nato = [nato_format[letter] for letter in user_name]
    except KeyError:
        print("Sorry only letters in the alphabet please.")
        nato()
    else:
        print(name_in_nato)


nato()
