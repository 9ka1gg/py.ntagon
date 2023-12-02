import time as t

programm = "pyntagon 1.0"
ru_local = "ru_localization.py"
en_local = "en_localization.py"
python = "python v3.12"
run_programm = "pyntagon.exe"
storage = "storage.py"

print(f"loading programm {programm} using {run_programm} based on {python}")
print("")
glob_tic = t.perf_counter()

# a ru_localization.py load
print(f"loading {ru_local}")
tic = t.perf_counter()
from ru_localization import script_ru_start
tac = t.perf_counter()
print(f"{ru_local} successfully loaded in {tic-tac} seconds.")
print("")

# an en_localization.py load
print(f"loading {en_local}")
tac = t.perf_counter()
from en_localization import script_en_start
tic = t.perf_counter()
print(f"{en_local} successfully loaded in {tic-tac} seconds.")
print("")

glob_tac = t.perf_counter()
print(f"py.ntagon successfully loaded in {glob_tac-glob_tic} seconds and ready for use.")
print("")
t.sleep(1)

# main cycle
while True:
    lang = input("Choose your language (ru/en): ")
    print("")
    if lang == "ru":
        script_ru_start()
    elif lang == "en":
        script_en_start()
    elif lang == "instantload":
        from storage import instantload
        instantload()
    elif lang == "sonicload":
        from storage import sonicload
        sonicload()
    elif lang == "nolimitload":
        from storage import nolimitload
        nolimitload()
    elif lang == "defendload":
        from storage import defendload
        defendload()
    else:
        print("error, try again.")
        t.sleep(3)
