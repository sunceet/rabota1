l = lambda x: [0, 1] if x <= 2 else l(x - 1) + [l(x - 1)[-1] + l(x - 1)[-2]]

n = 10
result = l(n)

print("Список чисел Фибоначчи до", n, ":", result)
