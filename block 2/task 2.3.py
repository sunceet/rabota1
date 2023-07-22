def arm_num(number):
    num_str = str(number)
    num_digits = len(num_str)

    total = 0

    for digit in num_str:
        total += int(digit) ** num_digits

    if total == number:
        return True
    else:
        return False


number = int(input("Введите число:"))

if arm_num(number):
    print(number, "является числом Армстронга")
else:
    print(number, "не является числом Армстронга")
