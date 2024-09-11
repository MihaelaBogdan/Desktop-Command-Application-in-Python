import tkinter as tk
from tkinter import messagebox
from preferences import load_preferences, save_preferences, update_button_text

def show_login_screen(root, preferences, update_button_text):
    global login_screen
    login_screen = tk.Toplevel(root)
    login_screen.title("Autentificare")
    login_screen.geometry("300x200")

    label_email = tk.Label(login_screen, text="Email:")
    label_email.pack(pady=5)
    entry_email = tk.Entry(login_screen)
    entry_email.pack(pady=5)

    label_password = tk.Label(login_screen, text="Parolă:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(login_screen, show="*")
    entry_password.pack(pady=5)

    def authenticate():
        email = entry_email.get()
        password = entry_password.get()
        if email in preferences and preferences[email]["password"] == password:
            messagebox.showinfo("Autentificare", "Autentificare reușită!")
            login_screen.destroy()
            load_preferences()
            update_button_text()
        else:
            messagebox.showerror("Autentificare", "Autentificare eșuată! Email sau parolă incorectă.")

    button_authenticate = tk.Button(login_screen, text="Autentificare", command=authenticate)
    button_authenticate.pack(pady=10)

    def show_registration_screen():
        registration_screen(root, preferences, update_button_text)

    button_register = tk.Button(login_screen, text="Înregistrare", command=show_registration_screen)
    button_register.pack(pady=10)

def registration_screen(root, preferences, update_button_text):
    global registration_window
    registration_window = tk.Toplevel(root)
    registration_window.title("Înregistrare")
    registration_window.geometry("300x200")

    label_email = tk.Label(registration_window, text="Email:")
    label_email.pack(pady=5)
    entry_email = tk.Entry(registration_window)
    entry_email.pack(pady=5)

    label_password = tk.Label(registration_window, text="Parolă:")
    label_password.pack(pady=5)
    entry_password = tk.Entry(registration_window, show="*")
    entry_password.pack(pady=5)

    def register():
        email = entry_email.get()
        password = entry_password.get()
     

