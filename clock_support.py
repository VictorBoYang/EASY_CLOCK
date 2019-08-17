def decide_clockType(x):
    while x != 0 and x != 1:
        print ("you can press only 0 or 1, please enter your choice again")
        user_input = input("choose the type of clock(press 0 for normal clock, press 1 for count down clock)")
        x = int(user_input)
    else:
        print ("good")
        return


def decide_clock_hour(x,y):
    while True:
        input_hour = input("please enter the starting hour(0-24)")
        clock_hour = int(input_hour)
        if x <= clock_hour <= y:
            print ("good")
            return clock_hour
            break
        else:
            print ("please enter only the integer between 0 to 24")


def decide_clock_minute(x,y):
    while True:
        input_minute = input("please enter the starting minute(0-60)")
        clock_minute = int(input_minute)
        if x <= clock_minute <= y:
            print ("good")
            break
        else:
            print ("please enter only the integer between 0 to 60")


def decide_clock_second(x,y):
    while True:
        input_second = input("please enter the starting second(0-60)")
        clock_second = int(input_second)
        if x <= clock_second <= y:
            print ("good")
            break
        else:
            print ("please enter only the integer between 0 to 60")
