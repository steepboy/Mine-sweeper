ua = {
    "start": "Старт",
    "settings": "Налаштування",
    "quit": "Вихід",
    "lang": "Мова",
    "uk": "UK",
    "ru": "RU",
    "ua": "UA",
    "row": "Рядків",
    "col": "Стовпчиків",
    "mines": "Мін",
    "save": "Зберегти",
    "restart_game": "Перезавантажити",
    "minesweeper": "САПЕР",
    "game_over": "Гра закінчена!",
    "you_lost": "Ви Програли!",
    "you_win": "Ви Виграли!",
    "hard_mode": "НЕРЕАЛЬНИЙ МОД",
    "menu": "Меню",
}

uk = {
    "start": "Start",
    "settings": "Settings",
    "quit": "Exit",
    "lang": "Language",
    "uk": "UK",
    "ru": "RU",
    "ua": "UA",
    "row": "Rows",
    "col": "Columns",
    "mines": "Mines",
    "save": "Apply",
    "restart_game": "Reload game",
    "minesweeper": "MINESWEEPER",
    "game_over": "Game over!",
    "you_lost": "You Lost!",
    "you_win": "You Won!",
    "hard_mode": "HARD MODE",
    "menu": "Menu",
}


try:
    with open('agrs/lang.txt', 'r') as file:
        result = file.read()
except:
    print("lang error")
if result == "1":
    language = ua
else:
    language = uk
print(language["settings"])