from main import chat_log, open_application, search_on_google, applications
import tkinter as tk

def process_command(command):
    command = command.lower()
    app_name = command.replace("deschide", "").strip() if "deschide" in command else command.strip()
    
    if app_name in applications:
        open_application(app_name)
    else:
        chat_log.insert(tk.END, f"Aplicația {app_name} nu este în lista noastră. Căutăm pe Google...\n")
        search_on_google(app_name)

if __name__ == "__main__":
    pass
