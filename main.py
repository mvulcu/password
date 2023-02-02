import tkinter as tk
import string
import random

def generate_password():
    password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=16))
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)

root = tk.Tk()
root.title("Password Generator")

password_label = tk.Label(root, text="Password:")
password_label.grid(row=0, column=0, sticky="W")

password_entry = tk.Entry(root, width=30)
password_entry.grid(row=0, column=1)

generate_button = tk.Button(root, text="Generate", command=generate_password)
generate_button.grid(row=1, column=0, columnspan=2, pady=10)

root.mainloop()
