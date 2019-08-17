from class_clock import *


class Normal_Clock(Clock):
    def Tick(self):
        self.second = self.second + 1
        self.time_change()

    def time_change(self):
        if self.second == 60:
            self.minute = self.minute + 1
            self.second = 0
        if self.minute == 60:
            self.hour = self.hour +1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0

# class Incrementor:
#     def __init__(self, var1, max_val, incrementor):
#         self.var1 = var1
#         self.max_val = max_val
#         self.incrementor = incrementor
#
#     def update(self):
#         if self.var1 < self.max_val:
#             return
#         self.var1 = 0
#         if self.incrementor != None:
#             self.incrementor.update()
