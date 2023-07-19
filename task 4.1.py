number = input("Введите число: ")
sorted_number = "".join(sorted(number, reverse=True))
print(f"Наибольшее число, которое можно получить путем перестановки цифр числа {number}: {sorted_number}")
