import random

colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
random_color = random.choice(colors)

while True:
    user_color = input("Выберите один из цветов: Red, Blue, Green, Yellow, Orange:")

    if user_color == random_color:
        print("Отлично")
        break
    else:
        print("Неправильный цвет. Попробуйте еще раз.")

        if random_color in colors:
            hint_index = colors.index(random_color) + 1
            hint = colors[hint_index] if hint_index < len(colors) else colors[0]
            print(f"Подсказка: Цвет, который я выбрал имеет букву '{hint[0]}' в своем названии.")
            print()

        print("Программа завершена.")
