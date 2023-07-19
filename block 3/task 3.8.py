import string

alphabet = string.ascii_lowercase

letter_dict = {}

for index, letter in enumerate(alphabet, start=1):
    letter_dict[letter] = index

print(letter_dict)