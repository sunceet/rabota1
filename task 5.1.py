import csv
books = [
    {'Title': 'Berserk', 'Author': 'Kentaro Miura', 'Year': '1989'},
    {'Title': 'Oyasumi PunPun', 'Author': 'Asano Inio', 'Year': '2007'},
    {'Title': 'Overlord', 'Author': 'Kugane Maruyama', 'Year': '2010'},
    {'Title': 'Vagabond', 'Author': 'Takehiko, Eidzi ', 'Year': '1998'}
]
with open('books.csv', mode='w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['Title', 'Author', 'Year'])
    writer.writeheader()
    writer.writerows(books)
print('Файл books.csv успешно создан.')
