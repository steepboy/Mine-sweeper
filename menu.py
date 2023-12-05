import tkinter as tk
import subprocess
import webbrowser
from tkinter.messagebox import showinfo
from lang import *


def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    x = (window.winfo_screenwidth() // 2) - (width // 2)
    y = (window.winfo_screenheight() // 2) - (height // 1)
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def start_game():
    print("Старт")
    root.destroy()
    subprocess.run(["python", "pt.py"])

def open_settings():
    def ua():
        with open('agrs/lang.txt', 'w') as file:
            file.write(str(1))
        showinfo("Мову змінено!", "Для продовження\nНатисніть 'Ok'")
        root.destroy()
        subprocess.run(["python", "main.py"])

    def eng():
            with open('agrs/lang.txt', 'w') as file:
                file.write(str(2))
            showinfo("Language reset!", "For continue\nPress 'Ok'")
            root.destroy()
            subprocess.run(["python", "main.py"])
    def ru():
        webbrowser.open('https://www.youtube.com/watch?v=Wx7vo__48oE')

    def debug():
        subprocess.run(["python", "part.py"])

    print("Налаштування")
    new_window = tk.Toplevel(root)
    new_window.title(language["settings"])
    new_window.geometry("300x200")
    center_window(new_window)
    tk.Label(new_window, text=(language["lang"]), bg="grey", font=("Arial", 15)).pack(side="top", fill="x", padx=10, pady=10)

    frame1 = tk.Frame(new_window)
    frame1.pack()

    btn1 = tk.Button(frame1, text="UA", command=ua)
    btn1.pack(side=tk.LEFT)

    btn2 = tk.Button(frame1, text="UK", command=eng)
    btn2.pack(side=tk.LEFT)

    btn3 = tk.Button(frame1, text="RU", command=ru)
    btn3.pack(side=tk.LEFT)

    btn_deb = tk.Button(new_window, text="Debug", command=debug)
    btn_deb.pack(side=tk.BOTTOM)

def global_args():
    lang = 1

def quit_game():
    root.quit()

root = tk.Tk()
root.title("Minesweeper")
root.geometry("300x300")
root.resizable(width=False, height=False)

def create_main_screen():
    leb = tk.Label(root, text=(language["minesweeper"]), font=("Arial", 30), fg="blue", height=2)
    leb.pack()

    start_button = tk.Button(root, text=(language["start"]), command=start_game, height=2, width=12)
    start_button.pack()

    settings_button = tk.Button(root, text=(language["settings"]), command=open_settings, height=2, width=12)
    settings_button.pack()

    quit_button = tk.Button(root, text=(language["quit"]), command=quit_game, height=2, width=12)
    quit_button.pack()

def call():
    center_window(root)
    create_main_screen()
    root.mainloop()

call()