from clock_support import *
from class_clock import *
from Normal_Clock import *
from Countdown_Clock import *
import time

#user input clock mode
user_choice = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
user_choice = int(user_choice)
check_user_choice(user_choice)

#user input clock starting hour
clock_hour = input("please enter the starting hour(0-23)")
clock_hour = int(clock_hour)
check_in_hour(clock_hour)

#user input clock starting Minute
clock_minute = input("please enter the starting minute(0-59)")
clock_minute = int(clock_minute)
check_in_minute(clock_minute)

#user input clock starting Second
clock_second = input("please enter the starting second(0-59)")
clock_second = int(clock_second)
check_in_second(clock_second)

#clock run
clock_run(user_choice,clock_hour,clock_minute,clock_second)
