import pandas
data = pandas.read_csv("./day 26 python - list comprehension/alphabets.csv")

new_data = {row.letter: row.code for (index,row) in data.iterrows()}
# print (new_data)

input = input("Enter your name: ").upper()
if input.isalpha():
    phonetic = [new_data[letter] for letter in input]
    print (phonetic)
else:
    raise KeyError ("PLEASE ENTER A VALID ALPHABET.")
