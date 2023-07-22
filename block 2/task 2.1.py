import random

colors = ["Red", "Blue", "Green", "Yellow", "Orange"]
random_color = random.choice(colors)

while True:
    user_color = input("Выберите одну: Red, Blue, Green, Yellow, Orange:")

    if user_color == random_color:
        print("Отлично")
        break
    else:
        print("Неправильный цвет. Попробуйте еще раз.")

        if random_color in colors:
            hinti = colors.index(random_color) + 1
            hint = colors[hinti] if hinti < len(colors) else colors[0]
            print(f"Цвет, который я выбрал имеет букву '{hint[0]}' .")
            print()

        print("Программа завершена.")
