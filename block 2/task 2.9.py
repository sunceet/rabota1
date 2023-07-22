def max_digit_position(number):
    number = str(number)
    max_digit = 0
    max_digit_position_from_end = 0
    max_digit_position_from_start = 0

    for i in range(len(number)):
        digit = int(number[i])
        if digit > max_digit:
            max_digit = digit
            max_digit_position_from_end = len(number) - i
        if digit >= max_digit:
            max_digit_position_from_start = i + 1

    return max_digit_position_from_end, max_digit_position_from_start


number = input("Введите натуральное число, в котором все цифры различны: ")
result_end, result_start = max_digit_position(number)
print("Порядковый номер максимальной цифры (от конца):", result_end)
print("Порядковый номер максимальной цифры (от начала):", result_start)
