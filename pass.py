import tkinter as tk
import random
import string

class PasswordGeneratorApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Generator")
        self.master.geometry("400x300")
        
        self.label_title = tk.Label(master, text="Password Generator by eracoding", font=("Arial", 16), fg="red")
        self.label_title.pack(pady=10)

        self.password_var = tk.StringVar()
        self.label_password = tk.Label(master, textvariable=self.password_var, font=("Arial", 14))
        self.label_password.pack(pady=10)

        self.generate_button = tk.Button(master, text="Generate Password", command=self.generate_password)
        self.generate_button.pack(pady=10)

        self.copy_button = tk.Button(master, text="Copy", command=self.copy_password)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=12))
        self.animate_password(password)

    def animate_password(self, password):
        self.password_var.set("")
        self.master.after(100, self.animate_characters, password, 0)

    def animate_characters(self, password, index):
        if index < len(password):
            self.password_var.set(self.password_var.get() + password[index])
            self.master.after(50, self.animate_characters, password, index+1)

    def copy_password(self):
        self.master.clipboard_clear()
        self.master.clipboard_append(self.password_var.get())

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
