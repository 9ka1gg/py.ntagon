from colorama import init
from time import sleep
from storage import codes
from storage import yes_variants
from storage import percents_interface
init()


def script_ru_start():
    sleep(1)
    choice = input("Взломать Пентагон? ")
    if choice in yes_variants:
        script_ru()
    else:
        print("Ошибка!")
        return


def script_ru():
    from storage import percent
    from storage import slp
    print("Начинается взлом Пентагона...")
    sleep(2)
    print("")
    print("")
    print("Процент взлома: 0.0%")
    percents_interface(percent)
    while percent < 99.9:
        sleep(slp)
        percent = percent + 0.1
        slp = slp + 0.00005
        print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
        percents_interface(percent)
    sleep(0.5)
    print("Пентагон успешно взломан!")
    sleep(1)
    print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
    sleep(3)


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
        print("Ошибка!")
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
        percents_interface(percent)
        while percent < 99.9:
            sleep(slp)
            percent = percent + 0.1
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
            percents_interface(percent)
        sleep(0.5)
        print("Пентагон успешно взломан!")
        sleep(1)
        print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
        sleep(3)
    else:
        print("Ошибка!")
        return


def nolimitload_ru():
    from storage import percent
    choice = input("Начать бесконечный взлом Пентагон? ")
    if choice in yes_variants:
        print("Начинается БЕСКОНЕЧНЫЙ взлом Пентагона!")
        sleep(2)
        print("")
        print("")
        print("Процент взлома: 0.0%")
        percents_interface(percent)
        while True:
            sleep(0.0001)
            percent = percent + 0.1
            print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
            percents_interface(percent)
    else:
        print("Ошибка!")
        return


def defendload_ru():
    from storage import percent
    from storage import slp
    print("Начинается защита Пентагона...")
    sleep(2)
    print("")
    print("")
    print("Процент взлома: 0.0%")
    percents_interface(percent)
    while percent > 0:
        sleep(slp)
        percent = percent - 0.1
        slp = slp + 0.00005
        print(f"\033[2AПроцент взлома: {round(percent, 1)}%")
        percents_interface(percent)
    sleep(0.5)
    print("Пентагон успешно защищен!")
    sleep(1)
    print(f"Спасибо за игру! Вот чит-коды: {codes} (их надо вводить на этапе выбора языка)")
    sleep(2)
