import csv

# Создаем список книг
books = [
    {'Title': 'Berserk', 'Author': 'Kentaro Miura', 'Year': '1989'},
    {'Title': 'Oyasumi PunPun', 'Author': 'Asano Inio', 'Year': '2007'},
    {'Title': 'Overlord', 'Author': 'Kugane Maruyama', 'Year': '2010'},
    {'Title': 'Vagabond', 'Author': 'Takehiko Inoye, Eidzi Yosikava', 'Year': '1998'}
]

# Открываем файл books.csv для записи
with open('books.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
    
    # Записываем заголовки столбцов
    writer.writeheader()
    
    # Записываем данные по книгам в файл
    writer.writerows(books)

print('Файл books.csv успешно создан.')
