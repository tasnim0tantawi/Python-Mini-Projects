import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
phonetic_alphabet = {row["letter"]: row["code"] for (index, row) in data.iterrows()}


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        output = [phonetic_alphabet[letter] for letter in word]
    except KeyError:
        print(f"Sorry! Only letters from the alphabet are allowed!")
        generate_phonetic()
    else:
        print(output)


generate_phonetic()