import tkinter as tk

def encrypt_vigenere(key, message):
    encrypted_text = ""
    key_index = 0
    for letter in message:
        if letter.isalpha():
            key_letter = key[key_index].upper()
            shift = ord(key_letter) - 65
            new_letter = chr((ord(letter.upper()) + shift - 65) % 26 + 65)
            encrypted_text += new_letter
            key_index = (key_index + 1) % len(key)
        else:
            encrypted_text += letter

    return encrypted_text


def decrypt_vigenere(key, message):
    decrypted_text = ""
    key_index = 0
    for letter in message:
        if letter.isalpha():
            key_letter = key[key_index].upper()
            shift = ord(key_letter) - 65
            new_letter = chr((ord(letter.upper()) - shift - 65) % 26 + 65)
            decrypted_text += new_letter
            key_index = (key_index + 1) % len(key)
        else:
            decrypted_text += letter

    return decrypted_text


def encrypt():
    key = key_entry.get()
    message = message_entry.get()
    encrypted_text = encrypt_vigenere(key, message)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, encrypted_text)


def decrypt():
    key = key_entry.get()
    message = message_entry.get()
    decrypted_text = decrypt_vigenere(key, message)
    result_text.delete('1.0', tk.END)
    result_text.insert(tk.END, decrypted_text)


# Interface graphique
window = tk.Tk()
window.title("Chiffrement de Vigenère")

# Création des widgets
key_label = tk.Label(window, text="Clé :")
key_entry = tk.Entry(window)

message_label = tk.Label(window, text="Message :")
message_entry = tk.Entry(window)

encrypt_button = tk.Button(window, text="Chiffrer", command=encrypt)
decrypt_button = tk.Button(window, text="Déchiffrer", command=decrypt)

result_label = tk.Label(window, text="Résultat :")
result_text = tk.Text(window, height=10)

# Placement des widgets
key_label.grid(row=0, column=0, sticky="W", padx=10, pady=10)
key_entry.grid(row=0, column=1, padx=10, pady=10)

message_label.grid(row=1, column=0, sticky="W", padx=10, pady=10)
message_entry.grid(row=1, column=1, padx=10, pady=10)

encrypt_button.grid(row=2, column=0, padx=10, pady=10)
decrypt_button.grid(row=2, column=1, padx=10, pady=10)

result_label.grid(row=3, column=0, sticky="W", padx=10, pady=10)
result_text.grid(row=4, column=0, columnspan=2, padx=10, pady=10)

# Boucle principale
window.mainloop()
