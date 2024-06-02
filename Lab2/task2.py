# task2.py

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

# Читання файлу Прізвище2.txt
with open('Прізвище2.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Розшифрування тексту
shift = -3
decrypted_text = caesar_cipher(encrypted_text, shift)

# Запис розшифрованого тексту в Прізвище3.txt
with open('Прізвище3.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_text)
