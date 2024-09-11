from main import preferences, texte_butoane

def save_preferences():
    with open("preferences.txt", "w") as file:
        for email, data in preferences.items():
            file.write(f"{email}:{data['password']}\n")

def update_button_text(button_process_text, button_voice_command, limba):
    button_process_text.config(text=texte_butoane[limba]["process_text"])
    button_voice_command.config(text=texte_butoane[limba]["voice_command"])
