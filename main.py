import tkinter as tk
import time
from tkinter import Menu, colorchooser, messagebox
import webbrowser
import speech_recognition as sr
import urllib.parse
import os
import subprocess

# Define global variables
preferences = {}
limba = "romana"  # Default language

# Text for buttons in different languages
texte_butoane = {
    "romana": {"process_text": "Procesează Text", "voice_command": "Comandă Vocală"},
    "engleza": {"process_text": "Process Text", "voice_command": "Voice Command"},
    "germana": {"process_text": "Text Verarbeiten", "voice_command": "Sprachbefehl"},
    "italiana": {"process_text": "Elabora Testo", "voice_command": "Comando Vocale"},
    "spaniola": {"process_text": "Procesar Texto", "voice_command": "Comando de Voz"},
    "chineza": {"process_text": "处理文本", "voice_command": "语音指令"},
    "japoneza": {"process_text": "テキスト処理", "voice_command": "音声コマンド"}
}

# Define dictionary with application names and paths
applications = {
    "notepad": "C:\\Windows\\System32\\notepad.exe",
    "calculator": "C:\\Windows\\System32\\calc.exe",
    "task manager": "C:\\Windows\\System32\\Taskmgr.exe",
    "system info": "C:\\Windows\\System32\\msinfo32.exe",
    "mail": "C:\\Program Files\\Microsoft Office\\root\\Office16\\outlook.exe",
    "microsoft store": "C:\\Windows\\explorer.exe shell:::{4234d49b-0245-4df3-b780-3893943456e1}",
    "file explorer": "C:\\Windows\\explorer.exe",
    "media player": "C:\\Program Files\\Windows Media Player\\wmplayer.exe",
    "calendar": "C:\\Program Files\\Windows Calendar\\WinCal.exe",
    "photos": "C:\\Program Files\\Windows Photo Viewer\\PhotoViewer.dll",
    "settings": "ms-settings:"
}

# Define the main window
root = tk.Tk()
root.title("Main Application")
root.geometry("600x400")
root.configure(bg="black")

def show_main_window():
    root.deiconify()
    add_buttons_and_entry()

def add_buttons_and_entry():
    global button_process_text, button_voice_command, entry, chat_log, lang_menu, buttons

    menubar = Menu(root)
    root.config(menu=menubar)
    settings_menu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Meniu", menu=settings_menu)

    lang_menu = Menu(settings_menu, tearoff=0)
    settings_menu.add_cascade(label="Schimbă Limba", menu=lang_menu)
    for lang in texte_butoane.keys():
        lang_menu.add_command(label=lang, command=lambda l=lang: change_language(l))

    settings_menu.add_command(label="Schimbă Culoarea Butoanelor", command=change_button_color)
    settings_menu.add_command(label="Schimbă Culoarea Fundalului", command=change_background_color)
    settings_menu.add_command(label="Autentificare", command=show_login_screen)

    entry = tk.Entry(root, width=40)
    entry.pack(side=tk.TOP, padx=10, pady=10)

    button_process_text = tk.Button(root, text=texte_butoane[limba]["process_text"], bg="blue", fg="white", command=lambda: process_command(entry.get()))
    button_process_text.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    button_voice_command = tk.Button(root, text=texte_butoane[limba]["voice_command"], bg="blue", fg="white", command=process_voice_command)
    button_voice_command.pack(side=tk.TOP, fill=tk.X, padx=10, pady=5)

    chat_log = tk.Text(root, bg="black", fg="white", font=("Helvetica", 12), wrap=tk.WORD)
    chat_log.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    buttons = {"process_text": button_process_text, "voice_command": button_voice_command}

def change_language(lang):
    global limba
    limba = lang
    update_button_text()
    for item in lang_menu.winfo_children():
        item.destroy()
    for lang in texte_butoane.keys():
        lang_menu.add_command(label=lang, command=lambda l=lang: change_language(l))

def update_button_text():
    global limba
    button_process_text.config(text=texte_butoane[limba]["process_text"])
    button_voice_command.config(text=texte_butoane[limba]["voice_command"])

def process_command(command):
    command = command.lower()
    app_name = command.replace("deschide", "").strip() if "deschide" in command else command.strip()
    
    if app_name in applications:
        open_application(app_name)
    else:
        chat_log.insert(tk.END, f"Aplicația {app_name} nu este în lista noastră. Căutăm pe Google...\n")
        search_on_google(app_name)

def process_voice_command():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        print("Ascultă...")
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio, language="en-US")
        process_command(command)
    except sr.UnknownValueError:
        print("Nu s-a putut recunoaște comanda vocală.")
        chat_log.insert(tk.END, "Nu s-a putut recunoaște comanda vocală.\n")
    except sr.RequestError as e:
        print("Eroare la cererea serviciului Google:", str(e))
        chat_log.insert(tk.END, f"Eroare la cererea serviciului Google: {str(e)}\n")

def open_application(app_name):
    app_name = app_name.lower()
    if app_name in applications:
        app_path = applications[app_name]
        chat_log.insert(tk.END, f"Încercăm să deschidem aplicația: {app_name}\n")
        if os.path.exists(app_path):
            try:
                subprocess.Popen(app_path, shell=True)
                chat_log.insert(tk.END, f"Deschiderea aplicației: {app_name}\n")
            except Exception as e:
                chat_log.insert(tk.END, f"Nu s-a putut deschide aplicația {app_name}. Eroare: {str(e)}\n")
        else:
            chat_log.insert(tk.END, f"Aplicația {app_name} nu a fost găsită local. Căutăm pe Google...\n")
            search_on_google(app_name)
    else:
        chat_log.insert(tk.END, f"Aplicația {app_name} nu este disponibilă în lista noastră. Căutăm pe Google...\n")
        search_on_google(app_name)

def search_on_google(query):
    search_query = urllib.parse.quote(query)
    search_url = f"https://www.google.com/search?q={search_query}"
    webbrowser.open(search_url)

def change_background_color():
    color = colorchooser.askcolor()[1]
    if color:
        root.configure(bg=color)

def change_button_color():
    color = colorchooser.askcolor()[1]
    if color:
        for button in buttons.values():
            button.configure(bg=color)

def show_login_screen():
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
        registration_screen()

    button_register = tk.Button(login_screen, text="Înregistrare", command=show_registration_screen)
    button_register.pack(pady=10)

def registration_screen():
    global registration_window
    registration_window = tk.Toplevel(root)
    registration_window.title("Înregistrare")
    registration_window.geometry("300x250")

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
        if email in preferences:
            messagebox.showwarning("Înregistrare", "Acest email este deja utilizat.")
        else:
            preferences[email] = {"password": password}
            messagebox.showinfo("Înregistrare", "Înregistrare reușită!")
            registration_window.destroy()

    button_register = tk.Button(registration_window, text="Înregistrare", command=register)
    button_register.pack(pady=10)

def load_preferences():
    global preferences
    preferences = {
        "user@example.com": {"password": "password123"},
        "admin@example.com": {"password": "adminpass"}
    }

if __name__ == "__main__":
    root.withdraw()  # Ascunde fereastra principală până când sunt completate toate inițializările
    show_main_window()
    root.mainloop()
