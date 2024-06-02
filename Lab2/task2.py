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

# Читання файлу Прізвище2.txt
with open('Прізвище2.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

# Розшифрування тексту
shift = -3
decrypted_text = caesar_cipher(encrypted_text, shift)

# Запис розшифрованого тексту в Прізвище3.txt
with open('Прізвище3.txt', 'w', encoding='utf-8') as file:
    file.write(decrypted_text)
