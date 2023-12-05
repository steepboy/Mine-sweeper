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
    "restar_game": "Перезавантажити",
    "minesweeper": "САПЕР",
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
    "restar_game": "Reload game",
    "minesweeper": "MINESWEEPER",
}

def lang():
    try:
        with open('agrs/lang.txt', 'r') as file:
            result = file.read()
    except:
        print("lang error")
    if result == "1":
        language = ua
    else:
        language = uk
    print(language["start"])
lang()