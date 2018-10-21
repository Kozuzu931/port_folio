from datetime import datetime as dt
import time
class Animal:
    def __init__(self, nm,spd):
        self.name=nm
        self.speed=spd
    def start(self):
        self.start_time=dt.now()
    def position(self):
        now=dt.now()
        pos=self.speed*(now-self.start_time).seconds
        return pos
    def distance(self,a2):
        pos1=self.position()
        pos2=a2.position()
        d=pos1-pos2
        print(self.name+"は"+a2.name+"より"+str(d)+"前方")
x=Animal("かめ男",10)
y=Animal("うさぎ",100)
x.start()
time.sleep(5)
y.start()
y.distance(y)
time.sleep(5)
x.distance(y)
