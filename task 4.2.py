def find_palindromes(string):
    palindromes = []
    for i in range(len(string)):
        for j in range(i, len(string)):
            substring = string[i:j+1]
            if substring == substring[::-1]:
                palindromes.append(substring)
    return palindromes

# Пример выполнения программы
string = input("Введите строку: ")
palindromes = find_palindromes(string)

if len(palindromes) > 0:
    print(f"Подстроки-палиндромы в строке {string}:")
    for palindrome in palindromes:
        print(palindrome)
else:
    print(f"В строке {string} нет подстрок-палиндромов.")