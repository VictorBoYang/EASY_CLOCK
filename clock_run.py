from clock_support import *
from class_clock import *
from Normal_Clock import *
from Countdown_Clock import *
import time
#user input clock mode

user_choice = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
user_choice = int(user_choice)
while user_choice != 0 and user_choice != 1:
    print ("you can press only 0 or 1, please enter your choice again")
    user_choice = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
    user_choice = int(user_choice)
else:
    print ("good")

#user input clock starting hour
clock_hour = input("please enter the starting hour(0-23)")
clock_hour = int(clock_hour)
while 0 > clock_hour or clock_hour > 23:
    print ("please enter only the integer between 0 to 23")
    clock_hour = input("please enter the starting hour(0-23)")
    clock_hour = int(clock_hour)
else:
    print ("good")

#user input clock starting Minute
clock_minute = input("please enter the starting minute(0-59)")
clock_minute = int(clock_minute)
while 0 > clock_minute or clock_minute > 59:
    print ("please enter only the integer between 0 to 59")
    clock_minute = input("please enter the starting minute(0-59)")
    clock_minute = int(clock_minute)
else:
    print ("good")

#user input clock starting Second
clock_second = input("please enter the starting second(0-59)")
clock_second = int(clock_second)
while 0 > clock_second or clock_second > 59:
    print ("please enter only the integer between 0 to 59")
    clock_second = input("please enter the starting second(0-59)")
    clock_second = int(clock_second)
else:
    print("good")

#clock run
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


# decide_clockType(user_choice)
# decide_clock_hour(0,24)
# decide_clock_minute(0,60)
# decide_clock_second(0,60)
