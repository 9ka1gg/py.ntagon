from colorama import init
from time import sleep
from storage import codes
from storage import yes_variants
from percents_interface import pif_init
init()


def script_ru():
    from storage import percent
    from storage import slp
    choice = input("Взломать Пентагон? ")
    if choice in yes_variants:
        print("Начинается взлом Пентагона...")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 0.0%")
        pif_init(percent)
        while percent < 99.9:
            sleep(slp)
            percent = percent + 0.1
            slp = slp + 0.00005
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
            pif_init(percent)
        sleep(0.5)
        print("Пентагон успешно взломан!")
        sleep(1)
        print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
        sleep(3)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return


def instantload_ru():
    choice = input("Взломать Пентагон моментально? ")
    if choice in yes_variants:
        print("Пентагон будет взломан моментально!")
        sleep(1)
        print(f"Процент взлома: 100.0%\n[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ]\nПентагон успешно взломан!")
        sleep(1)
        print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
        sleep(2)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return


def sonicload_ru():
    from storage import percent
    from storage import slp
    choice = input("Взломать Пентагон? ")
    if choice in yes_variants:
        print("Начинается взлом Пентагона...")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 0.0%")
        pif_init(percent)
        while percent < 99.9:
            sleep(slp)
            percent = percent + 0.1
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
            pif_init(percent)
        sleep(0.5)
        print("Пентагон успешно взломан!")
        sleep(1)
        print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
        sleep(3)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return


def endlessload_ru():
    from storage import percent
    choice = input("Начать бесконечный взлом Пентагона? ")
    if choice in yes_variants:
        print("Начинается БЕСКОНЕЧНЫЙ взлом Пентагона!")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 0.0%")
        pif_init(percent)
        while True:
            sleep(0.0001)
            percent = percent + 0.1
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
            pif_init(percent)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return


def defendload_ru():
    from storage import slp
    percent = float(100)
    choice = input("Начать защиту Пентагон? ")
    if choice in yes_variants:
        print("Начинается защита Пентагона!")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 100.0%")
        pif_init(percent)
        while percent > 0.1:
            sleep(slp)
            percent = percent - 0.1
            slp = slp + 0.00005
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%                                    ")
            pif_init(percent)
        sleep(0.5)
        print("Пентагон успешно защищен!")
        sleep(1)
        print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
        sleep(2)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return


def endlessdefload_ru():
    percent = float(100)
    choice = input("Начать БЕСКОНЕЧНУЮ защиту Пентагона? ")
    if choice in yes_variants:
        print("Начинается БЕСКОНЕЧНАЯ защита Пентагона!")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 100.0%")
        pif_init(percent)
        while True:
            sleep(0.0001)
            percent = percent - 0.1
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%                                        ")
            pif_init(percent)
    else:
        print(f"Ошибка! Введёный ответ не соответствует не одному из данного списка:\n\n{yes_variants}")
        print("")
        return
