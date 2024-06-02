# task1.py

# Створення файлів
open('Прізвище1.txt', 'w').close()
open('Прізвище2.txt', 'w').close()

# Запис частини тексту в файл Прізвище1.txt
text = "Це приклад тексту без додаткових символів"
with open('Прізвище1.txt', 'w', encoding='utf-8') as file:
    file.write(text)

def caesar_cipher(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char in 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ':
                idx = ord(char) - ord('А')
                new_char = chr((idx + shift) % 33 + ord('А'))
            elif char in 'абвгґдеєжзииіїйклмнопрстуфхцчшщьюя':
                idx = ord(char) - ord('а')
                new_char = chr((idx + shift) % 33 + ord('а'))
            else:
                new_char = char
            result += new_char
        else:
            result += char
    return result

# Читання файлу Прізвище1.txt
with open('Прізвище1.txt', 'r', encoding='utf-8') as file:
    text = file.read()

# Шифрування тексту
shift = 3
encrypted_text = caesar_cipher(text, shift)

# Запис зашифрованого тексту в Прізвище2.txt
with open('Прізвище2.txt', 'w', encoding='utf-8') as file:
    file.write(encrypted_text)
