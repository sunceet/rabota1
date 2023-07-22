import itertools


def find_permutations(lst):
    permutations = list(itertools.permutations(lst))
    return permutations


lst = input("Введите элементы списка через пробел: ").split()
permutations = find_permutations(lst)
print("Все перестановки заданного списка:")
for permutation in permutations:
    print(permutation)
