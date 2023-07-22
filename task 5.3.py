import csv


def read_books():
    books = []
    with open('books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


try:
    start_year = int(input('Введите начальный год: '))
    end_year = int(input('Введите конечный год: '))
except ValueError:
    print('Ошибка: введены некорректные данные.')
    exit()

books = read_books()

found_books = []
for book in books:
    year = int(book['Year'])
    if start_year <= year <= end_year:
        found_books.append(book)

if len(found_books) > 0:
    print(f'Найдены книги {start_year}-{end_year}:')
    for book in found_books:
        print(f'Название: {book["Title"]}, Автор: {book["Author"]},'
              f' Год выпуска: {book["Year"]}')
else:
    print(f'Книг, выпущенных в промежутке '
          f'{start_year}-{end_year}, не найдено.')
