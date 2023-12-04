import tkinter as tk

window = tk.Tk()
window.title("Гра")
row = 5
columns = 5

buttons = []
for i in range(row):
    temp = []
    for j in range(columns):
        btn = tk.Button(window, width=3, font='Calibri 15 bold')
        temp.append(btn)
    buttons.append(temp)

for row_btn in buttons:
    print(row_btn)

for i in range(row):
    for j in range(columns):
        btn = buttons[i][j]
        btn.grid(row=i, column=j)

window.mainloop()