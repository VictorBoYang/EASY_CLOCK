from class_clock import *

class Countdown_Clock(Clock):
    def Tick(self):
        self.second = self.second - 1
        self.time_change()

    def time_change(self):
        if self.hour == 0:
            self.CountDown_limit()
        else:
            if self.second == -1:
                self.minute = self.minute - 1
                self.second = 59
            if self.minute == -1:
                self.hour = self.hour - 1
                self.minute = 59

    def CountDown_limit(self):
        if self.hour == 0 and self.minute == 0 and self.second == -1:
            self.second = 0
            return self.second
