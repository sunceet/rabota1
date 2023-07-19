fibonacci = lambda n: [0, 1] if n <= 2 else fibonacci(n-1) + [fibonacci(n-1)[-1] + fibonacci(n-1)[-2]]

n = 10
result = fibonacci(n)

print("Список чисел Фибоначчи до", n, ":", result)