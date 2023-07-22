lo = lambda x: [0, 1] \
    if x <= 2 else lo(x - 1) + [lo(x - 1)[-1] + lo(x - 1)[-2]]

n = 10
result = lo(n)

print("Список чисел Фибоначчи до", n, ":", result)
