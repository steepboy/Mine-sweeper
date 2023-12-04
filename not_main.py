import tkinter as tk
window = tk.Tk()

row_num = 10
col_num = 10

button_list = []
for i in range(row_num):
    temp = []
    for j in range(col_num):
        cell = tk.Button(window, width = 3)
        temp.append(cell)
    button_list.append(temp)

for row in button_list:
    print(row)

for i in range(row_num):
    for j in range(col_num):
        cell = button_list[i][j]
        cell.grid(row=i, column=j)

window.mainloop()
#h