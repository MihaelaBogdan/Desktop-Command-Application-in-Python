from main import root, add_buttons_and_entry, change_language, change_button_color, change_background_color

def setup_gui():
    root.configure(bg="black")
    add_buttons_and_entry()

if __name__ == "__main__":
    setup_gui()
