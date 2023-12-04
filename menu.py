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
    time.sleep(0.4)
    root.destroy()

def open_settings():
    print("Налаштування")
    new_window = tk.Toplevel(root)
    new_window.title("Налаштування")
    new_window.geometry("300x500")
    center_window(new_window)
    tk.Label(new_window, text="Мова", bg="grey", font=("Arial", 15)).pack(side="top", fill="x", padx=10, pady=10)

    frame1 = tk.Frame(new_window)
    frame1.pack()

    btn1 = tk.Button(frame1, text="Кнопка 1")
    btn1.pack(side=tk.LEFT)

    btn2 = tk.Button(frame1, text="Кнопка 2")
    btn2.pack(side=tk.LEFT)

    btn3 = tk.Button(frame1, text="Кнопка 3")
    btn3.pack(side=tk.LEFT)


def quit_game():
    root.quit()

root = tk.Tk()
root.title("САПЕР")
root.geometry("300x300")
root.resizable(width=False, height=False)

def create_main_screen():
    leb = tk.Label(root, text="САПЕР", font=("Arial", 30), fg="blue", height=2)
    leb.pack()

    start_button = tk.Button(root, text="Старт", command=start_game, height=2, width=12)
    start_button.pack()

    settings_button = tk.Button(root, text="Налаштування", command=open_settings, height=2, width=12)
    settings_button.pack()

    quit_button = tk.Button(root, text="Вихід", command=quit_game, height=2, width=12)
    quit_button.pack()

def call():
    center_window(root)
    create_main_screen()
    root.mainloop()

call()