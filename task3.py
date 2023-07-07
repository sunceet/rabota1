#Напишите программу, сравнивающую 3 числа, поочередно выведенные пользователем.
#Программа должна сообщить о том, какое число является наибольшим и выводить все три
#числа по убыванию.

num1 = int(input("Введите первое число: "))
num2 = int(input("Введите второе число: "))
num3 = int(input("Введите третье число: "))

if num1 >= num2 and num1 >= num3:
    max_num = num1
    if num2 >= num3:
        print("Числа в убывающем порядке:", num1, num2, num3)
    else:
        print("Числа в убывающем порядке:", num1, num3, num2)
elif num2 >= num1 and num2 >= num3:
    max_num = num2
    if num1 >= num3:
        print("Числа в убывающем порядке:", num2, num1, num3)
    else:
        print("Числа в убывающем порядке:", num2, num3, num1)
else:
    max_num = num3
    if num1 >= num2:
        print("Числа в убывающем порядке:", num3, num1, num2)
    else:
        print("Числа в убывающем порядке:", num3, num2, num1)
print("Наибольшее число:", max_num)
