# Створення файлів
open('Прізвище1.txt', 'w').close()
open('Прізвище2.txt', 'w').close()

# Запис частини тексту в файл Прізвище1.txt
text = "ІвсенасвітітребапережитиікоженфінішцепосутістартІнапереднетребаворожитиІзаминулимплакатиневарт"
with open('Прізвище1.txt', 'w', encoding='utf-8') as file:
    file.write(text)

def caesar_cipher(text, shift):
    result = ""
    alphabet_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯ'
    alphabet_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    alphabet_length = len(alphabet_upper)

    for char in text:
        if char.isalpha():
            if char in alphabet_upper:
                idx = alphabet_upper.index(char)
                new_char = alphabet_upper[(idx + shift) % alphabet_length]
            elif char in alphabet_lower:
                idx = alphabet_lower.index(char)
                new_char = alphabet_lower[(idx + shift) % alphabet_length]
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