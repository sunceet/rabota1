number = input("Введите число: ")
sorted_number = "".join(sorted(number, reverse=True))
print(f"Наиб число, которое можно получить {number}: {sorted_number}")
