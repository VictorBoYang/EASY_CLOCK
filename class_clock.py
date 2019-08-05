class Clock:
    def __init__(self,H,M,S):
        self.hour = H
        self.minute = M
        self.second = S

    def Tick(self):
        self.second = self.second + 1
        self.time_change()



    def show(self):
        Hour = self.fill_zero(self.hour)
        Minute = self.fill_zero(self.minute)
        Second = self.fill_zero(self.second)
        return "%s:%s:%s" % (Hour,Minute,Second)

    def time_change(self):
        if self.second == 60:
            self.minute = self.minute + 1
            self.second = 0
        if self.minute == 60:
            self.hour = self.hour +1
            self.minute = 0
        if self.hour == 24:
            self.hour = 0



    def fill_zero(self,int):
        if int < 10:
            string = str(int)
            return "0%s" % string
        string = str(int)
        return string
