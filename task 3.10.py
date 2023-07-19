text = "Пример строки, содержащей буквы и пробелы"
letter_count = {letter: text.count(letter) for letter in text if letter != ' '}

print(letter_count)