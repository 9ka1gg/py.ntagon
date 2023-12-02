codes = ["instantload", "sonicload", "nolimitload", "defendload"]
yes_variants = ["Да", "Да!", "ДА", "ДА!", "дА", "дА!", "да", "да!", "lf", "lf!", "Lf", "Lf!", "lF", "lF!", "LF", "LF!", "yes", "yes!", "Yes", "Yes!", "yEs", "yEs!", "yeS", "yeS!", "YEs", "YEs!", "yES", "yES!", "YES", "YES!"]
percent = float(0)
unload_percent = float(100)
slp = 0.0001


def percents_interface(perc):
    if perc < 5:
        print("[ ░░░░░░░░░░░░░░░░░░░░ ]")
    elif perc >= 5 and perc < 10:
        print("[ ▓░░░░░░░░░░░░░░░░░░░ ]")
    elif perc >= 10 and perc < 15:
        print("[ ▓▓░░░░░░░░░░░░░░░░░░ ]")
    elif perc >= 15 and perc < 20:
        print("[ ▓▓▓░░░░░░░░░░░░░░░░░ ]")
    elif perc >= 20 and perc < 25:
        print("[ ▓▓▓▓░░░░░░░░░░░░░░░░ ]")
    elif perc >= 25 and perc < 30:
        print("[ ▓▓▓▓▓░░░░░░░░░░░░░░░ ]")
    elif perc >= 30 and perc < 35:
        print("[ ▓▓▓▓▓▓░░░░░░░░░░░░░░ ]")
    elif perc >= 35 and perc < 40:
        print("[ ▓▓▓▓▓▓▓░░░░░░░░░░░░░ ]")
    elif perc >= 40 and perc < 45:
        print("[ ▓▓▓▓▓▓▓▓░░░░░░░░░░░░ ]")
    elif perc >= 45 and perc < 50:
        print("[ ▓▓▓▓▓▓▓▓▓░░░░░░░░░░░ ]")
    elif perc >= 50 and perc < 55:
        print("[ ▓▓▓▓▓▓▓▓▓▓░░░░░░░░░░ ]")
    elif perc >= 55 and perc < 60:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░░ ]")
    elif perc >= 60 and perc < 65:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░░ ]")
    elif perc >= 65 and perc < 70:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░░ ]")
    elif perc >= 70 and perc < 75:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░░ ]")
    elif perc >= 75 and perc < 80:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░░ ]")
    elif perc >= 80 and perc < 85:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░░ ]")
    elif perc >= 85 and perc < 90:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░░ ]")
    elif perc >= 90 and perc < 95:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░░ ]")
    elif perc >= 95 and perc < 99.8:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓░ ]")
    elif perc >= 99.8:
        print("[ ▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓ ]")


def instantload():
    lang = input("Choose Language (ru/en): ")
    if lang == "ru":
        from ru_localization import instantload_ru
        instantload_ru()
    if lang == "en":
        from en_localization import instantload_en
        instantload_en()


def sonicload():
    lang = input("Choose Language (ru/en): ")
    if lang == "ru":
        from ru_localization import sonicload_ru
        sonicload_ru()
    if lang == "en":
        from en_localization import sonicload_en
        sonicload_en()


def nolimitload():
    lang = input("Choose Language (ru/en): ")
    if lang == "ru":
        from ru_localization import nolimitload_ru
        nolimitload_ru()
    if lang == "en":
        from en_localization import nolimitload_en
        nolimitload_en()


def defendload():
    lang = input("Choose Language (ru/en): ")
    if lang == "ru":
        from ru_localization import defendload_ru
        defendload_ru()
    if lang == "en":
        from en_localization import defendload_en
        defendload_en()
