class Clock:
    def __init__(self,H,M,S):
        self.hour = H
        self.minute = M
        self.second = S

    def Tick(self):
        self.second = self.second + 1
        self.second_to_minute()
        self.minute_to_hour()
        self.if_hour_max()

    def show(self):
        hour = str(self.hour)
        minute= str(self.minute)
        second = str(self.second)
        Hour = hour.zfill(2)
        Minute = minute.zfill(2)
        Second = second.zfill(2)
        return Hour + ":" + Minute + ":" + Second

    def second_to_minute(self):
        if self.second == 60:
            self.minute = self.minute + 1
            self.second = 0

    def minute_to_hour(self):
        if self.minute ==60:
            self.hour = self.hour +1
            self.minute = 0

    def if_hour_max(self):
        if self.hour == 24:
            self.hour = 0
