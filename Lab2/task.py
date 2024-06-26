import tkinter as tk
from tkinter import filedialog, messagebox

def create_files():
    open('Молька1.txt', 'w').close()
    open('Молька2.txt', 'w').close()

def write_text_to_file(text, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        file.write(text)

def read_text_from_file(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return file.read()

def caesar_cipher(text, shift):
    result = ""
    alphabet_upper = 'АБВГҐДЕЄЖЗИІЇЙКЛМНОПРСТУФХЦЧШЩЬЮЯABC'
    alphabet_lower = 'абвгґдеєжзиіїйклмнопрстуфхцчшщьюяd'
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

def encrypt_text():
    text = text_entry.get("1.0", tk.END).strip()
    if text:
        write_text_to_file(text, 'Молька1.txt')
        shift = 3
        encrypted_text = caesar_cipher(text, shift)
        write_text_to_file(encrypted_text, 'Молька2.txt')
        messagebox.showinfo("Успіх", "Текст зашифровано та збережено.")
    else:
        messagebox.showerror("Помилка", "Будь ласка, введіть текст для шифрування.")

def decrypt_file():
    file_path = filedialog.askopenfilename(title="Виберіть файл для розшифрування", filetypes=[("Text files", "*.txt")])
    if not file_path:
        messagebox.showwarning("Увага", "Файл не обрано!")
        return

    shift = -3
    with open(file_path, 'r', encoding='utf-8') as file:
        encrypted_text = file.read()

    decrypted_text = caesar_cipher(encrypted_text, shift)

    save_path = filedialog.asksaveasfilename(title="Зберегти розшифрований текст", defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if save_path:
        write_text_to_file(decrypted_text, save_path)
        messagebox.showinfo("Успіх", "Текст успішно розшифровано та збережено.")
    else:
        messagebox.showwarning("Увага", "Розшифрований текст не збережено.")

# GUI setup
root = tk.Tk()
root.title("Шифрування та розшифрування тексту за допомогою шифру Цезаря")

create_files_button = tk.Button(root, text="Створити порожні файли", command=create_files)
create_files_button.pack(pady=10)

text_label = tk.Label(root, text="Введіть текст для шифрування:")
text_label.pack()

text_entry = tk.Text(root, height=10, width=50)
text_entry.pack(pady=10)

encrypt_button = tk.Button(root, text="Зашифрувати та зберегти", command=encrypt_text)
encrypt_button.pack(pady=10)

decrypt_button = tk.Button(root, text="Розшифрувати файл", command=decrypt_file)
decrypt_button.pack(pady=10)

root.mainloop()