from class_clock import *

class Normal_Clock(Clock):
    def Tick(self):
        self.second = self.second + 1
        self.time_change()

    def time_change(self):
        if self.second == 60:
            self.minute = self.minute + 1
            self.second = 0
        # self.second_minute_changing(self.second,self.minute)
        if self.minute == 60:
            self.hour = self.hour +1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0

    # def second_minute_changing(self,x,y):
    #     if  == 60:
    #          = y + 1
    #         x = 0
