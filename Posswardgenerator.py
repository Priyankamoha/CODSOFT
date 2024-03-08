import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            messagebox.showerror("Negative Input", "Please enter a positive integer for the length.")
            return
        if length >= 20:
            messagebox.showerror("Error", "Please enter a positive integer less then 20 ")
            return
        characters = string.ascii_letters + string.digits# + string.punctuation
        password = ''.join(random.choice(characters) for _ in range(length))
        password_entry.config(state='normal')
        password_entry.delete(0, tk.END)
        password_entry.insert(tk.END, password)
        password_entry.config(state='readonly')
    except ValueError:
        messagebox.showerror("Character Input Error", "Invalid input. Please enter a valid integer for the length.")




root = tk.Tk()
root.title("Password Generator")
length_label = tk.Label(root, text="Password Length:")
length_label.grid(row=0, column=0, padx=10, pady=10)
length_entry = tk.Entry(root)
length_entry.grid(row=0, column=1, padx=10, pady=10)
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)
password_label = tk.Label(root, text="Generated Password:")
password_label.grid(row=2, column=0, padx=10, pady=10)
password_entry = tk.Entry(root, state="readonly")
password_entry.grid(row=2, column=1, padx=10, pady=10)
root.mainloop()
