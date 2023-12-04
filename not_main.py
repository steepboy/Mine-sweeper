import tkinter as tk
from random import shuffle
from tkinter.messagebox import showinfo

colors = {1: 'blue', 2: 'green', 3: 'yellow', 4: 'orange', 5: 'red', 6: 'pink', 7: 'purple', 8: 'black'}

class MyButton(tk.Button):

    def __init__(self, master, x, y, number=0, *args, **kwargs):
        super(MyButton, self).__init__(master, *args, **kwargs)
        self.x = x
        self.y = y
        self.number = number
        self.is_mine = False
        self.count_bomb = 0
        self.is_open = False

    def __repr__(self):
        return f'MyButton {self.x, self.y, self.number, self.is_mine}'


class minesweeper:
    window = tk.Tk()
    row = 5
    col = 6
    mines = 3
    is_game_over = False
    is_first_click = True

    def __init__(self):
        self.buttons = []
        for i in range(minesweeper.row + 2):
            temp = []
            for j in range(minesweeper.col + 2):
                btn = MyButton(minesweeper.window, width=3, font='Calibri 15', x=i, y=j)
                btn.config(command=lambda button=btn: self.click(button))
                temp.append(btn)
            self.buttons.append(temp)
        print("Start")

    def click(self, clicked_button):

        if minesweeper.is_game_over:
            return None

        if minesweeper.is_first_click:
            self.insert_mines(clicked_button.number)
            self.count_mines_in_buttons()
            self.print_buttons()
            minesweeper.is_first_click = False

        if clicked_button.is_mine:
            clicked_button.config(text='*', background='red', disabledforeground='black')
            clicked_button.is_open = True
            minesweeper.is_game_over = True
            showinfo("Gameover", "You lost!")
            for i in range(1, minesweeper.row + 1):
                for j in range(1, minesweeper.col + 1):
                    btn = self.buttons[i][j]
                    if btn.is_mine:
                        btn['text'] = '*'

        else:
            color = colors.get(clicked_button.count_bomb, 'black')
            clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            if clicked_button.count_bomb:
                clicked_button.config(text=clicked_button.count_bomb, disabledforeground=color)
            else:
                self.breadth_first_search(clicked_button)
        clicked_button.config(state='disabled')
        clicked_button.config(relief=tk.SUNKEN)

    def breadth_first_search(self, btn: MyButton):
        queue = [btn]
        while queue:
            cur_btn = queue.pop()
            color = colors.get(cur_btn.count_bomb, 'black')
            if cur_btn.count_bomb:
                cur_btn.config(text=cur_btn.count_bomb, disabledforeground=color)
            else:
                cur_btn.config(text='', disabledforeground=color)
            cur_btn.is_open = True
            cur_btn.config(state='disabled')
            cur_btn.config(relief=tk.SUNKEN)

            if cur_btn.count_bomb == 0:
                x, y = cur_btn.x, cur_btn.y
                for dx in [-1, 0, 1]:
                    for dy in [-1, 0, 1]:
                        if not abs(dx - dy) == 1:
                            continue

                        next_btn = self.buttons[x+dx][y+dy]
                        if not next_btn.is_open and 1 <= next_btn.x <= minesweeper.row and \
                                1 <= next_btn.y <= minesweeper.col and next_btn not in queue:
                            queue.append(next_btn)

    def replay(self):
        self.window.winfo_children()[8].destroy()
        [child.destroy() for child in self.window.winfo_children()]
        self.__init__()
        self.create_widgets()
        minesweeper.is_first_click = True

    def create_setting_win(self):
        win_settings = tk.Toplevel(self.window)
        row_entry = tk.Entry(win_settings)
        row_entry.grid(row=0, column=1, padx=20, pady=20)
        col_entry = tk.Entry(win_settings)
        col_entry.grid(row=1, column=1)
        mines_entry = tk.Entry(win_settings)
        mines_entry.grid(row=2, column=1)
    def create_widgets(self):

        menubar = tk.Menu(self.window)
        self.window.config(menu=menubar)

        settings_menu = tk.Menu(menubar, tearoff=0)
        settings_menu.add_command(label='Play', command=self.replay)
        settings_menu.add_command(label='Settings', command=self.create_settings_win)
        settings_menu.add_command(label='Exit', command=self.window.destroy)
        menubar.add_cascade(label="Menu", menu=settings_menu)
        count = 1
        for i in range(1, minesweeper.row + 1):
            for j in range(1, minesweeper.col + 1):
                btn = self.buttons[i][j]
                btn.number = count
                btn.grid(row=i, column=j, stick='NWES')
                count += 1

        for i in range(1, minesweeper.row + 1):
            tk.Grid.rowconfigure(self.window, i, weight=1)

        for i in range(1, minesweeper.col +1):
            tk.Grid.columnconfigure(self.window, i, weight=1)
    def open_all_buttons(self):
        for i in range(minesweeper.row + 2):
            for j in range(minesweeper.col + 2):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    btn.config(text='*', background='red', disabledforeground='black')
                elif btn.count_bomb in colors:
                    color = colors.get(btn.count_bomb, 'black')
                    btn.config(text=btn.count_bomb, fg=color)

    def start(self):
        self.create_widgets()

        # self.open_all_buttons()

        minesweeper.window.mainloop()

    def print_buttons(self):
        for i in range(1, minesweeper.row + 1):
            for j in range(1, minesweeper.col + 1):
                btn = self.buttons[i][j]
                if btn.is_mine:
                    print('B', end='')
                else:
                    print(btn.count_bomb, end='')
            print()

    def insert_mines(self, number):
        index_mines = self.get_mines_places(number)
        print(index_mines)
        for i in range(1, minesweeper.row + 1):
            for j in range(1, minesweeper.col + 1):
                btn = self.buttons[i][j]
                if btn.number in index_mines:
                    btn.is_mine = True

    def count_mines_in_buttons(self):
        for i in range(1, minesweeper.row + 1):
            for j in range(1, minesweeper.col + 1):
                btn = self.buttons[i][j]
                count_bomb = 0
                if not btn.is_mine:
                    for row_dx in [-1, 0, 1]:
                        for col_dx in [-1, 0, 1]:
                            neighbour = self.buttons[i+row_dx][j+col_dx]
                            if neighbour.is_mine:
                                count_bomb += 1
                btn.count_bomb = count_bomb

    def get_mines_places(self, exclude_number):
        indexes = list(range(1, minesweeper.col * minesweeper.row + 1))
        indexes.remove(exclude_number)
        shuffle(indexes)
        return indexes[:minesweeper.mines]


game = minesweeper()
game.start()
