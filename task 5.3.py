import csv

# Функция для чтения данных из файла books.csv и возврата списка книг
def read_books():
    books = []
    with open('books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Запрашиваем у пользователя начальный и конечный год
try:
    start_year = int(input('Введите начальный год: '))
    end_year = int(input('Введите конечный год: '))
except ValueError:
    print('Ошибка: введены некорректные данные.')
    exit()

# Читаем список книг из файла
books = read_books()

# Ищем книги, выпущенные в заданном промежутке времени
found_books = []
for book in books:
    year = int(book['Year'])
    if start_year <= year <= end_year:
        found_books.append(book)

# Выводим результаты поиска
if len(found_books) > 0:
    print(f'Найдены книги, выпущенные в промежутке {start_year}-{end_year}:')
    for book in found_books:
        print(f'Название: {book["Title"]}, Автор: {book["Author"]}, Год выпуска: {book["Year"]}')
else:
    print(f'Книг, выпущенных в промежутке {start_year}-{end_year}, не найдено.')
