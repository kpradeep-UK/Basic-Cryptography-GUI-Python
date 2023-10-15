import hashlib
import tkinter as tk
from tkinter import Entry, Label, Button, scrolledtext

win = tk.Tk()
win.geometry("400x400")
win.title("Hashing and Encryption Tool")

def md5h():
    text = entry.get()
    encoded_msg = hashlib.md5(str(text).encode('utf-8'))
    converted = encoded_msg.hexdigest()
    result_text.delete("1.0", tk.END)  # Clear previous results
    result_text.insert(tk.END, f"The hashed value of {text} is {converted}")

def sha1h():
    text = entry.get()
    encoded_msg = hashlib.sha1(str(text).encode('utf-8'))
    converted = encoded_msg.hexdigest()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"The hashed value of {text} is {converted}")

def sha256h():
    text = entry.get()
    encoded_msg = hashlib.sha256(str(text).encode('utf-8'))
    converted = encoded_msg.hexdigest()
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f"The hashed value of {text} is {converted}")

def encrpytf():
    text = entry.get()
    message = text
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    key = entry_key.get()
    encrypt = ''
    for i in message:
        position = alphabet.find(i)
        newposition = (position + int(key)) % 94
        encrypt += alphabet[newposition]
    output = (encrypt)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f'Encrypted Message: {output}\nEncryption Key: {key}')

def decryptf():
    text = entry.get()
    message = text
    alphabet = "abcdefghijklmnopqrstuvwxyz1234567890!@#$%^&*()_+{}|:<>?=-[]\;',./`~ABCDEFGHIJKLMNOPQRSTUVWXYZ "
    key = entry_key.get()
    encrypt = ''
    for i in message:
        position = alphabet.find(i)
        newposition = (position - int(key)) % 94
        encrypt += alphabet[newposition]
    output = (encrypt)
    result_text.delete("1.0", tk.END)
    result_text.insert(tk.END, f'Decrypted message: {output}')

# Create and configure GUI elements
label = Label(win, text="Enter text:")
label.pack()
entry = Entry(win, width=40)
entry.pack()
label_key = Label(win, text="Enter encryption/decryption key:")
label_key.pack()
entry_key = Entry(win, width=40)
entry_key.pack()

md5_button = Button(win, text="MD5 Hash", command=md5h)
md5_button.pack(fill='both')
sha1_button = Button(win, text="SHA1 Hash", command=sha1h)
sha1_button.pack(fill='both')
sha256_button = Button(win, text="SHA256 Hash", command=sha256h)
sha256_button.pack(fill='both')
encrypt_button = Button(win, text="Encrypt", command=encrpytf)
encrypt_button.pack(fill='both')
decrypt_button = Button(win, text="Decrypt", command=decryptf)
decrypt_button.pack(fill='both')

result_text = scrolledtext.ScrolledText(win, wrap=tk.WORD, width=40, height=10)
result_text.pack()

win.mainloop()
