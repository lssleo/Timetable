# This is simple timetable on Python!

print(
    "\n\nHello! I'm your timetable program. \nI'll help you to be effective. \n I believe in you!\n\n"
)
# Welcome message


def timetable():  # func

    try:
        # you can set any time, for ex: 15:43.
        time = float(input("What time is it?  : \n\n"))

        if time >= 6.30 and time < 7.00:
            print("\nWake Up!")
        elif time >= 7.00 and time < 8.00:
            print("\nSwimming Pool / Walk / Loading : 7.00 - 8.00")
        elif time >= 8.00 and time < 9.00:
            print("\nBreakfast + Shower  : 8.00 - 9.00")
        elif time >= 9.00 and time < 10.00:
            print("\nFree time ( Awake! ) : 9.00 - 10.00")
        elif time >= 10.00 and time < 13.00:
            print("\nCoding - 10.00 : 13.00")
        elif time >= 13.00 and time < 14.00:
            print("\nDinner / Free time : 13.00 - 14.00")
        elif time >= 14.00 and time < 18.00:
            print("\nCoding(IT) : 14.00 - 18.00")
        elif time >= 18.00 and time < 19.00:
            print("\nSupper(light) : 18.00 - 19.00")
        elif time >= 19.00 and time < 21.30:
            print("\nFree time : 19.00 - 21.30")
        elif time >= 21.30 and time < 22.00:
            print("\nPreparation for sleep : 21.30 - 22.00")
        elif time >= 22.00 and time <= 24.00 or time < 6.30:
            print("\nSleep : 22.00 - 6.30")
        else:
            print("Incorrect time!")

    except (ZeroDivisionError, NameError, ValueError, TypeError):  # catch errors
        print("\nError")


def restart():  # this cycle for chance to try again

    restart = 0

    while restart != "y" or restart != "n":
        if restart == "y":
            timetable()
        if restart == "n":
            break
        else:
            restart = str(input("\n\nrestart? y/n. : \n"))


timetable()  # start function with timetable

restart()  # opportunity to restart in any option
