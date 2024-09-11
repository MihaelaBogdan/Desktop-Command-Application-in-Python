from main import root, show_main_window
import time
import tkinter as tk

def animate_logo():
    for _ in range(10):
        canvas_start.move(logo_start, 0, -5)
        root.update()
        time.sleep(0.1)
    for _ in range(10):
        canvas_start.move(logo_start, 0, 5)
        root.update()
        time.sleep(0.1)
    for _ in range(5):
        canvas_start.move(logo_start, 0, -5)
        root.update()
        time.sleep(0.1)
    start_screen.destroy()
    show_main_window()

def start_screen(root):
    global start_screen, canvas_start, logo_start
    start_screen = tk.Toplevel()
    start_screen.title("M")
    start_screen.geometry("600x400")
    start_screen.configure(bg="black")

    canvas_start = tk.Canvas(start_screen, width=400, height=300, bg="black", highlightthickness=0)
    canvas_start.pack()

    logo_start = canvas_start.create_text(200, 150, text="M", fill="blue", font=("Helvetica", 150, "bold"))

    root.after(0, animate_logo)