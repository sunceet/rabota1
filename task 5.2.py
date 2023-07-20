import csv

# Функция для чтения данных из файла books.csv и возврата списка книг
def read_books():
    books = []
    with open('books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books

# Функция для записи данных в файл books.csv
def write_books(books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
        writer.writeheader()
        writer.writerows(books)

# Запрашиваем у пользователя количество записей, которые он хочет добавить
num_of_records = int(input('Сколько записей вы хотите добавить? '))

# Запрашиваем у пользователя данные для каждой записи и добавляем их в список книг
books = []
for _ in range(num_of_records):
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год выпуска книги: ')
    book = {'Title': title, 'Author': author, 'Year': year}
    books.append(book)

# Записываем обновленный список книг в файл books.csv
write_books(books)

# Запрашиваем у пользователя автора, книги которого нужно вывести
author_to_find = input('Введите автора, книги которого нужно найти: ')

# Читаем список книг из файла
books = read_books()

# Проверяем, есть ли в списке книги указанного автора и выводим их
found_books = []
for book in books:
    if book['Author'] == author_to_find:
        found_books.append(book)

# Выводим результаты поиска
if len(found_books) > 0:
    print(f'Найдены книги автора {author_to_find}:')
    for book in found_books:
        print(f'Название: {book["Title"]}, Год выпуска: {book["Year"]}')
else:
    print(f'Книг автора {author_to_find} не найдено.')
