def encrypt_rot13(string):
    encrypted_string = ""
    for char in string:
        if char.isalpha():
            if char.islower():
                xix = chr((ord(char) - ord('a') + 13) % 26 + ord('a'))
            else:
                xix = chr((ord(char) - ord('A') + 13) % 26 + ord('A'))
        else:
            xix = char
        encrypted_string += xix
    return encrypted_string


string = input("Введите строку: ")
encrypted_string = encrypt_rot13(string)
print(f"Зашифрованная строка по алгоритму ROT13: {encrypted_string}")
