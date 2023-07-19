text = "Пример строки с повторяющимися буквами"
unique_letters = {letter: text.count(letter) for letter in set(text)}

print(unique_letters)