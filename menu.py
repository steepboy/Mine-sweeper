import tkinter as tk
import subprocess
import time

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 1)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def start_game():
    print("Старт")
    process = subprocess.Popen(["python", "launcher.py"])
    process.wait()
    time.sleep(0.3)
    root.destroy()

def open_settings():
    print("Настройки")

def quit_game():
    root.quit()

root = tk.Tk()
root.title("САПЕР")
root.geometry("300x300")
root.resizable(width=False, height=False)

def create_main_screen():
    leb = tk.Label(root, text="САПЕР", font=("Arial", 30), fg="blue", height=2)
    leb.pack()

    start_button = tk.Button(root, text="Старт", command=start_game, height=2, width=10)
    start_button.pack()

    settings_button = tk.Button(root, text="Настройки", command=open_settings, height=2, width=10)
    settings_button.pack()

    quit_button = tk.Button(root, text="Выход", command=quit_game, height=2, width=10)
    quit_button.pack()

center_window(root)
create_main_screen()

root.mainloop()