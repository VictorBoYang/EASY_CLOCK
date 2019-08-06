class Clock:
    def __init__(self,H,M,S):
        self.hour = H
        self.minute = M
        self.second = S

    def show(self):
        Hour = self.fill_zero(self.hour)
        Minute = self.fill_zero(self.minute)
        Second = self.fill_zero(self.second)
        return "%s:%s:%s" % (Hour,Minute,Second)


    def Tick(self):
        raise NotImplementedError

    def time_change(self):
        raise NotImplementedError


    def fill_zero(self,int):
        if int < 10:
            string = str(int)
            return "0%s" % string
        string = str(int)
        return string
