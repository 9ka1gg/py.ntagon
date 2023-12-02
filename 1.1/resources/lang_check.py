from time import sleep
from ru_localization import script_ru
from en_localization import script_en


def lang_check(lang):
    if lang == "ru":
        script_ru()
    elif lang == "en":
        script_en()
    elif lang == "instantload":
        from cheats_init import instantload
        instantload()
    elif lang == "sonicload":
        from cheats_init import sonicload
        sonicload()
    elif lang == "endlessload":
        from cheats_init import endlessload
        endlessload()
    elif lang == "defendload":
        from cheats_init import defendload
        defendload()
    elif lang == "endlessdefload":
        from cheats_init import endlessdefload
        endlessdefload()
    else:
        print("error! Incorrect input.")
        sleep(2)
