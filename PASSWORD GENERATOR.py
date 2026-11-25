
import secrets
import string
import tkinter as tk
from tkinter import messagebox


def generate_password():
    try:
        length = int(length_entry.get())

        if length < 4 or length > 128:
            messagebox.showwarning(
                "Invalid Length",
                "Password length must be between 4 and 128."
            )
            return

        characters = ""

        if upper_var.get():
            characters += string.ascii_uppercase

        if lower_var.get():
            characters += string.ascii_lowercase

        if number_var.get():
            characters += string.digits

        if symbol_var.get():
            characters += string.punctuation

        if not characters:
            messagebox.showwarning(
                "Warning",
                "Please select at least one character type."
            )
            return

        password = ''.join(
            secrets.choice(characters)
            for _ in range(length)
        )

        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)

    except ValueError:
        messagebox.showerror(
            "Error", "Please enter a valid password length."
        )


def copy_password():
    password = password_entry.get()

    if not password:
        messagebox.showwarning(
            "Warning", "Generate a password first!"
        )
        return

    root.clipboard_clear()
    root.clipboard_append(password)
    messagebox.showinfo(
        "Success", "Password copied to clipboard!"
    )


# Main Window
root = tk.Tk()
root.title("Password Generator")
root.geometry("450x450")
root.configure(bg="#202A44")
root.resizable(False, False)

# Heading
tk.Label(
    root,
    text="PASSWORD GENERATOR",
    font=("Arial", 20, "bold"),
    bg="#202A44",
    fg="white"
).pack(pady=20)

# Password Length
tk.Label(
    root,
    text="Password Length:",
    font=("Arial", 12),
    bg="#202A44",
    fg="white"
).pack()

length_entry = tk.Entry(
    root, font=("Arial", 12), justify="center"
)
length_entry.insert(0, "12")
length_entry.pack(pady=10)

# Character Options
upper_var = tk.BooleanVar(value=True)
lower_var = tk.BooleanVar(value=True)
number_var = tk.BooleanVar(value=True)
symbol_var = tk.BooleanVar(value=True)

options = [
    ("Uppercase Letters", upper_var),
    ("Lowercase Letters", lower_var),
    ("Numbers", number_var),
    ("Special Characters", symbol_var)
]

for text, variable in options:
    tk.Checkbutton(
        root,
        text=text,
        variable=variable,
        bg="#202A44",
        fg="white",
        selectcolor="#202A44",
        activebackground="#202A44",
        activeforeground="white",
        font=("Arial", 11)
    ).pack(anchor="w", padx=110)

# Password Output
password_entry = tk.Entry(
    root,
    font=("Arial", 13),
    width=30,
    justify="center"
)
password_entry.pack(pady=20)

# Buttons
tk.Button(
    root,
    text="Generate Password",
    command=generate_password,
    bg="#28A745",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22
).pack(pady=5)

tk.Button(
    root,
    text="Copy Password",
    command=copy_password,
    bg="#007BFF",
    fg="white",
    font=("Arial", 11, "bold"),
    width=22
).pack(pady=5)

root.mainloop()
