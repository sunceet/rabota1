def sum_of_range(a, b):
    sum = 0
    for number in range(a, b+1):
        sum += number
    return sum

a = int(input("Введите значение a: "))
b = int(input("Введите значение b: "))

result = sum_of_range(a, b)
print("Сумма чисел от", a, "до", b, "включительно:", result)
