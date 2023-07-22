from math import sqrt

a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

D = b ** 2 - 4 * a * c

if D < 0:
    print("Уравнение не имеет действительных корней")
elif D == 0:
    x = - b / (2 * a)
    print("Уравнение имеет один корень:", x)
else:
    x1 = (- b + sqrt(D)) / (2 * a)
    x2 = (- b - sqrt(D)) / (2 * a)
    print("Уравнение имеет два корня:", x1, "и", x2)
