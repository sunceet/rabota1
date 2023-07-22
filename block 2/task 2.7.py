def sum_positive_numbers():
    sum = 0
    while True:
        number = int(input("Введите число: "))
        if number < 0:
            break
        sum += number
    return sum


result = sum_positive_numbers()
print("Сумма положительных чисел:", result)
