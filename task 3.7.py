vowels = ['a', 'e', 'i', 'o', 'u', 'y']
string = input("Введите строку: ").lower()

letter_dict = {}

for letter in string:
    if letter.isalpha():
        if letter in vowels:
            letter_dict[letter] = True
        else:
            letter_dict[letter] = False

print(letter_dict)
