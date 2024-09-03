import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_password(length):
    all_characters = string.ascii_letters + string.digits + string.punctuation
    if length < 8:
        messagebox.showerror("Erro", "A senha deve ter pelo menos 8 caracteres.")
        return None
    password = ''.join(random.choice(all_characters) for i in range(length))
    return password

def criar_senha():
    length = int(entry_length.get())
    password = generate_password(length)
    if password:
        label_password.config(text=f"Senha gerada: {password}")

def copiar_senha():
    password = label_password.cget("text").split(": ")[1]
    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo("Senha copiada", "A senha foi copiada para a área de transferência.")

root = tk.Tk()
root.title("Gerador de Senhas")

label_length = tk.Label(root, text="Tamanho da senha:")
label_length.pack()

entry_length = tk.Entry(root)
entry_length.pack()

button_gerar = tk.Button(root, text="Gerar senha", command=criar_senha)
button_gerar.pack()

label_password = tk.Label(root, text="")
label_password.pack()

button_copiar = tk.Button(root, text="Copiar senha", command=copiar_senha)
button_copiar.pack()

root.mainloop()