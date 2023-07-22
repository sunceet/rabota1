number = float(input("Введите вещественное число: "))
formatted_number = "{:.2f}".format(number)
print(formatted_number.replace(".", ","))
