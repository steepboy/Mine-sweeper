import subprocess

def read_lang_file(file_path):
    with open(file_path, 'r') as file:
        return file.read().strip()

lang_file_path = 'agrs/lang.txt'

lang_value = read_lang_file(lang_file_path)

if lang_value == '1':
    subprocess.Popen(['python', 'ua/menu.py'])
else:
    subprocess.Popen(['python', 'eng/menu.py'])