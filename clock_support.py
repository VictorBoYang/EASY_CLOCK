from class_clock import *
from Normal_Clock import *
from Countdown_Clock import *
import time

def check_user_choice(x):
    x = int(x)
    while x != 0 and x != 1:
        print ("you can press only 0 or 1, please enter your choice again")
        x = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
        x = int(x)
    else:
        print ("good")


def check_in_hour(hour_in):
    while 0 > hour_in or hour_in > 23:
        print ("please enter only the integer between 0 to 23")
        hour_in = input("please enter the starting hour(0-23)")
        hour_in = int(hour_in)
    else:
        print ("good")


def check_in_minute(min_in):
    while 0 > min_in or min_in > 59:
        print ("please enter only the integer between 0 to 59")
        min_in = input("please enter the starting minute(0-59)")
        min_in = int(min_in)
    else:
        print ("good")


def check_in_second(sec_in):
    while 0 > sec_in or sec_in > 59:
        print ("please enter only the integer between 0 to 59")
        sec_in = input("please enter the starting second(0-59)")
        sec_in = int(sec_in)
    else:
        print("good")


def clock_run(user_choice,clock_hour,clock_minute,clock_second):
    if user_choice == 0:
        Clock = Normal_Clock(clock_hour,clock_minute,clock_second)
        while True:
            Clock.show()
            Clock.Tick()
            time.sleep(1)
    elif user_choice == 1:
        Clock = Countdown_Clock(clock_hour,clock_minute,clock_second)
        while True:
            Clock.show()
            Clock.Tick()
            time.sleep(1)
