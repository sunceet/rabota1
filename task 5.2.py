import csv


def read_books():
    books = []
    with open('books.csv', mode='r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            books.append(row)
    return books


def write_books(books):
    with open('books.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
        writer.writeheader()
        writer.writerows(books)


num_of_records = int(input('Сколько записей вы хотите добавить? '))
books = []
for _ in range(num_of_records):
    title = input('Введите название книги: ')
    author = input('Введите автора книги: ')
    year = input('Введите год выпуска книги: ')
    book = {'Title': title, 'Author': author, 'Year': year}
    books.append(book)
write_books(books)
author_to_find = input('Введите автора, книги которого нужно найти: ')
books = read_books()
found_books = []
for book in books:
    if book['Author'] == author_to_find:
        found_books.append(book)
if len(found_books) > 0:
    print(f'Найдены книги автора {author_to_find}:')
    for book in found_books:
        print(f'Название: {book["Title"]}, Год выпуска: {book["Year"]}')
else:
    print(f'Книг автора {author_to_find} не найдено.')
