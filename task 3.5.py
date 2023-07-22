n = [1, 2, 3, 4, 5, 6, 7, 8, 9]

p = [x for x in n if not all(x % i != 0 for i in range(2, int(x ** 0.5) + 1))]

print(p)
