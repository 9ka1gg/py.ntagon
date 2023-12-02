from time import sleep
from lang_check import lang_check
program = "py.ntagon 1.1"
python = "python 3.12"
run_program = "pyntagon.exe"
print(f"loading program {program} using {run_program} based on {python}")
print("")
sleep(1)
print(f"py.ntagon successfully loaded and ready for use.")
print("")
sleep(1)

# main cycle
while True:
    lang = input("Choose your language (ru/en): ")
    print("")
    lang_check(lang)
