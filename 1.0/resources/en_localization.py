from colorama import init
from time import sleep
from storage import codes
from storage import yes_variants
from storage import percents_interface
init()


def script_en_start():
    choice = input("Hack the Pentagon? ")
    if choice in yes_variants:
        script_en()
    else:
        print("Error!")
        return


def script_en():
    from storage import percent
    from storage import slp
    print("The Pentagon hacking begins...")
    sleep(2)
    print("")
    print("")
    print("The hacking percent: 0.0%")
    percents_interface(percent)
    while percent < 99.9:
        sleep(slp)
        percent = percent + 0.1
        slp = slp + 0.00005
        print(f"\033[2AThe hacking percent: {round(percent, 1)}%")
        percents_interface(percent)
    sleep(0.5)
    print("The Pentagon has been successfully hacked!")
    sleep(1)
    print(f"Thanks for playing! Here are cheat codes: {codes}")
    sleep(3)


def instantload_en():
    percent = 100.0
    choice = input("instantly hack the Pentagon? ")
    if choice in yes_variants:
        print("The Pentagon will be hacked instantly!")
        sleep(1)
        print("")
        print("")
        print("The hacking percent: 100.0%")
        percents_interface(percent)
        sleep(0.5)
        print("The Pentagon has been successfully instantly-hacked!")
        sleep(1)
        print(f"Thanks for playing! Here are cheat codes: {codes}")
        sleep(3)
    else:
        print("Error!")
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
        print("Error!")
        return


def nolimitload_en():
    from storage import percent
    choice = input("Hack the Pentagon? ")
    if choice in yes_variants:
        print("The ENDLESS hacking of the Pentagon begins!")
        sleep(2)
        print("")
        print("")
        print("The hacking percent: 0.0%")
        percents_interface(percent)
        while percent < 99.9:
            sleep(0.0001)
            percent = percent + 0.1
            print(f"\033[2AThe hacking percent: {round(percent, 1)}%")
            percents_interface(percent)
    else:
        print("Error!")
        return


def defendload_en():
    from storage import percent
    from storage import slp
    print("The Pentagon defense begins!")
    sleep(2)
    print("")
    print("")
    print("The hacking percent: 0.0%")
    percents_interface(percent)
    while percent > 0:
        sleep(slp)
        percent = percent - 0.1
        slp = slp + 0.00005
        print(f"\033[2AThe hacking percent: {round(percent, 1)}%")
        percents_interface(percent)
    sleep(0.5)
    print("The Pentagon has been successfully defended!")
    sleep(1)
    print(f"Thanks for playing! Here are its cheat codes: {codes}")
    sleep(3)
