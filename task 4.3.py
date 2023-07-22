def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def find_primes(start, end):
    primes = []
    for number in range(start, end + 1):
        if is_prime(number):
            primes.append(number)
    return primes


start = int(input("Введите начало диапазона: "))
end = int(input("Введите конец диапазона: "))
primes = find_primes(start, end)

if len(primes) > 0:
    print(f"Простые числа в диапазоне от {start} до {end}:")
    for prime in primes:
        print(prime)
else:
    print(f"В диапазоне от {start} до {end} нет простых чисел.")
