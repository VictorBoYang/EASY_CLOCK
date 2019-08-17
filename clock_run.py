from clock_support import *
from class_clock import *
from Normal_Clock import *
from Countdown_Clock import *
import time
#user input clock mode

user_input = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
user_choice = int(user_input)
while user_choice != 0 and user_choice != 1:
    print ("you can press only 0 or 1, please enter your choice again")
    user_input = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
    user_choice = int(user_input)
else:
    print ("good")

#user input clock starting hour
input_hour = input("please enter the starting hour(0-24)")
clock_hour = int(input_hour)
while 0 > clock_hour or clock_hour > 24:
    print ("please enter only the integer between 0 to 24")
    input_hour = input("please enter the starting hour(0-24)")
    clock_hour = int(input_hour)
else:
    print ("good")

#user input clock starting Minute
input_minute = input("please enter the starting minute(0-60)")
clock_minute = int(input_minute)
while 0 > clock_minute or clock_minute > 60:
    print ("please enter only the integer between 0 to 60")
    input_minute = input("please enter the starting minute(0-60)")
    clock_minute = int(input_minute)
else:
    print ("good")

#user input clock starting Second
input_second = input("please enter the starting second(0-60)")
clock_second = int(input_second)
while 0 > clock_second or clock_second > 60:
    print ("please enter only the integer between 0 to 60")
    input_second = input("please enter the starting second(0-60)")
    clock_second = int(input_second)
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
