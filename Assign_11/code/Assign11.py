import time
class Clock:
    def __init__(self,hour,minute,second,style) -> None:
        self.style = style
        self.hour = hour
        self.minute = minute
        self.second = second
        pass
    def __str__(self):
        if int(self.style) == 0:
            print('{}:{}:{} am'.format(str(self.hour).zfill(2),str(self.minute).zfill(2),str(self.second).zfill(2)))
        if int(self.style) == 1:
            self.hour = int(self.hour) + 12
        if int(self.style) == 1:
            if int(self.hour) < 13:
                print('{}:{}:{} am'.format(str(self.hour).zfill(2),str(self.minute).zfill(2),str(self.second).zfill(2)))
            if int(self.hour) >= 13:
               print('{}:{}:{} pm'.format(str(self.hour).zfill(2),str(self.minute).zfill(2),str(self.second).zfill(2)))    
    def tick(self):
        self.second = int(self.second) + 1
        if int(self.second) == 60:
            self.second = 0
            self.minute = int(self.minute) + 1
        if int(self.minute) == 60:
            self.minute = 0
            self.hour = int(self.hour) + 1
    



def main():
    style = 0
    hour = input('What is the current hour ==> ')
    minute = input('What is the current minute ==> ')
    second = input('What is the current second ==> ')
    clock = Clock(hour,minute,second,style)
    while True:
        clock.__str__()
        clock.tick()
        time.sleep(1)
main()