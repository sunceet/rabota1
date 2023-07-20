def find_first_square(n):
    i = 1
    while i**2 <= n:
        i += 1
    return i
    
n = int(input("Введите число: "))
result = find_first_square(n)
print("Первое натуральное число, квадрат которого больше", n, ":", result)
