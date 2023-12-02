from colorama import init
from time import sleep
from storage import codes
from storage import yes_variants
from percents_interface import pif_init
init()


def script_en():
    from storage import percent
    from storage import slp
    choice = input("Hack the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon hacking begins...")
        sleep(2)
        print("")
        print("")
        print("The hacking percent: 0.0%")
        pif_init(percent)
        while percent < 99.9:
            sleep(slp)
            percent = percent + 0.1
            slp = slp + 0.00005
            print(f"\033[2AThe hacking percent: {round(percent, 1)}%")
            pif_init(percent)
        sleep(0.5)
        print("The Pentagon has been successfully hacked!")
        sleep(1)
        print(f"Thanks for playing! Here are cheat codes: {codes}")
        sleep(3)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return


def instantload_en():
    percent = 100.0
    choice = input("instantly hack the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon will be hacked instantly!")
        sleep(1)
        print("")
        print("")
        print("The hacking percent: 100.0%")
        pif_init(percent)
        sleep(0.5)
        print("The Pentagon has been successfully instantly-hacked!")
        sleep(1)
        print(f"Thanks for playing! Here are cheat codes: {codes}")
        sleep(3)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return


def sonicload_en():
    choice = input("Hack the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon will be hacked in a split second!..")
        print("The hacking percent: 100%")
        sleep(1)
        print(f"Thanks for playing! Here are its cheat codes: {codes}")
        sleep(2)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return


def endlessload_en():
    from storage import percent
    choice = input("Hack the Pentagon? ")
    if choice in yes_variants:
        print("The ENDLESS hacking of the Pentagon begins!")
        sleep(2)
        print("")
        print("")
        print("The hacking percent: 0.0%")
        pif_init(percent)
        while percent < 99.9:
            sleep(0.0001)
            percent = percent + 0.1
            print(f"\033[2AThe hacking percent: {round(percent, 1)}%")
            pif_init(percent)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return


def defendload_en():
    from storage import slp
    percent = float(100)
    choice = input("Protect the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon defense begins!")
        sleep(2)
        print("")
        print("")
        print("The hacking percent: 0.0%")
        pif_init(percent)
        while percent > 0.1:
            sleep(slp)
            percent = percent - 0.1
            slp = slp + 0.00005
            print(f"\033[2AThe hacking percent: {round(percent, 1)}%                        ")
            pif_init(percent)
        sleep(0.5)
        print("The Pentagon has been successfully defended!")
        sleep(1)
        print(f"Thanks for playing! Here are its cheat codes: {codes}")
        sleep(3)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return


def endlessdefload_en():
    percent = float(100)
    choice = input("Start an endless defense of the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon ENDLESS defense begins!")
        sleep(2)
        print("")
        print("")
        print("The hacking percent: 100.0%")
        pif_init(percent)
        while True:
            sleep(0.0001)
            percent = percent - 0.1
            print(f"\033[2AThe hacking percent: {round(percent, 1)}%                                        ")
            pif_init(percent)
    else:
        print(f"Error! input doesn't match any of the given list:\n\n{yes_variants}")
        print("")
        return
