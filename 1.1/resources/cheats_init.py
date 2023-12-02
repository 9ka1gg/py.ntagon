def instantload():
    lang = input("Choose Language for cheat-mode (ru/en): ")
    if lang == "ru":
        from ru_localization import instantload_ru
        instantload_ru()
    elif lang == "en":
        from en_localization import instantload_en
        instantload_en()
    else:
        print("Error! Incorrect language!")


def sonicload():
    lang = input("Choose Language for cheat-mode (ru/en): ")
    if lang == "ru":
        from ru_localization import sonicload_ru
        sonicload_ru()
    elif lang == "en":
        from en_localization import sonicload_en
        sonicload_en()
    else:
        print("Error! Incorrect language!")


def endlessload():
    lang = input("Choose Language for cheat-mode (ru/en): ")
    if lang == "ru":
        from ru_localization import endlessload_ru
        endlessload_ru()
    elif lang == "en":
        from en_localization import endlessload_en
        endlessload_en()
    else:
        print("Error! Incorrect language!")


def defendload():
    lang = input("Choose Language for cheat-mode (ru/en): ")
    if lang == "ru":
        from ru_localization import defendload_ru
        defendload_ru()
    elif lang == "en":
        from en_localization import defendload_en
        defendload_en()
    else:
        print("Error! Incorrect language!")


def endlessdefload():
    lang = input("Choose Language for cheat-mode (ru/en): ")
    if lang == "ru":
        from ru_localization import endlessdefload_ru
        endlessdefload_ru()
    elif lang == "en":
        from en_localization import endlessdefload_en
        endlessdefload_en()
    else:
        print("Error! Incorrect language!")
