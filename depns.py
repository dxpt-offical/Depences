import time
import os
import csv
import sys

if os.name == "nt":
    win = "Вы используете Windows"
    os.system("title Depences")
elif os.name == "posix":
    linx = "Вы используете Linux или macOS"
    sys.stdout.write("\x1b]2;Depences\x07")
    sys.stdout.flush()

while True:
    print(f'''
Используется: {os.name}
█████████████████████████████████████████████████████████████████████████
█									█
█  ____                                      				█
█ |  _ \\  ___ _ __   ___ _ __   ___ ___  ___ 				█
█ | | | |/ _ \\ '_ \\ / _ \\ '_ \\ / __/\\ _ \\/ __|  |  created by @userdeza	█
█ | |_| |  __/ |_) |  __/ | | | (_|  __/\\__ \\   |  for Verkhovna Rada	█
█ |____/ \\___| .__/ \\___|_| |_|\\___\\___||___/\\  |  buy it - @cmeuso	█
█            |_|                             				█
█									█
█████████████████████████████████████████████████████████████████████████
█				   █					█
█	1. универсальный поиск     █		3. информация		█
█	2. выход		   █		4. Sosal?		█
█				   █					█
█████████████████████████████████████████████████████████████████████████
''')
    menu = input(">> ")

    if menu == "1":
        file_path = input("путь к базе: ")

        if not os.path.exists(file_path):
            print("файл не найден!")
            time.sleep(2)
            continue

        search_value = input("значение поиска: ")

        try:
            with open(file_path, "r", encoding="utf-8") as file:
                if file_path.endswith(".csv"):
                    reader = csv.reader(file)
                else:
                    reader = file.readlines()

                found = False
                for row in reader:
                    if search_value in str(row):
                        print("найдено:", row)
                        found = True

                if not found:
                    print("совпадений не нашел.")
        except Exception as e:
            print("ошибка братан:", e)

        time.sleep(2)

    elif menu == "2":
        print("выход...")
        time.sleep(2)
        break

    elif menu == "3":
        print("софт создан дезиком @userdeza для Верховной рады")
        time.sleep(2)

    elif menu == "4":
        print("СОСАЛ?)))))))))))))))))))))))))))))")
        time.sleep(2)

    else:
        print("бро такое не курим. -- Деза")
        time.sleep(2)
