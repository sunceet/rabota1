shows = ["Serega Pirat", "MUZTV", "+100500", "Hata NIXA"]

print("Список передач:")
for show in shows:
    print(show)

new_show = input("Введите название новой передачи:")
position = int(input("Введите позицию на которой она должная быть вставлена:"))

shows.insert(position, new_show)
print("\nОбновленный список передач:")
for show in shows:
    print(show)
