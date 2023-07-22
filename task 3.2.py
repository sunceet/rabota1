fi = lambda n: [0, 1] \
    if n <= 2 else fi(n - 1) + [fi(n - 1)[-1] + fi(n - 1)[-2]]

n = 10
result = fi(n)

print("Список чисел Фибоначчи до", n, ":", result)
