from itertools import combinations


def find_combinations(numbers, target):
    def check_sum(combination, target):
        return sum(combination) == target

    unique_combinations = []

    for r in range(1, len(numbers) + 1):
        for combination in combinations(numbers, r):
            if check_sum(combination, target):
                unique_combinations.append(combination)

    return unique_combinations


numbers = [2, 4, 6, 3, 8]
target = 10

all_combinations = find_combinations(numbers, target)
print(f"Уникальные комбинации  {numbers}, сумма которых равна {target}:")
for combination in all_combinations:
    print(combination)
