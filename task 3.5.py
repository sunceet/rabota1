numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

non_prime_numbers = [x for x in numbers if not all(x % i != 0 for i in range(2, int(x**0.5) + 1))]

print(non_prime_numbers)