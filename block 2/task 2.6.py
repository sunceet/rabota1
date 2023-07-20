def optimize_trip():
    distance = float(input("Сколько километров хотите проехать на автомобиле? "))
    consumption = float(input("Сколько литров топлива расходует автомобиль на 100 километров? "))
    fuel_tank = float(input("Сколько литров топлива в вашем баке? "))

    max_distance = fuel_tank / (consumption / 100)

    if max_distance >= distance:
        print("Вы сможете проехать желаемое расстояние!")
    else:
        print("К сожалению, у вас недостаточно топлива для проезда заданного расстояния.")

optimize_trip()
