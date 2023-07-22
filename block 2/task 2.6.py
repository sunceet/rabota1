def optimize_trip():
    distance = float(input("Сколько км хотите проехать на автомобиле? "))
    kl = float(input("Сколько топлива расходует авто на 100 километров? "))
    fuel_tank = float(input("Сколько литров топлива в вашем баке? "))

    max_distance = fuel_tank / (kl / 100)

    if max_distance >= distance:
        print("Вы сможете проехать желаемое расстояние!")
    else:
        print("у вас недостаточно для проезда заданного расстояния.")


optimize_trip()
