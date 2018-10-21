from datetime import datetime as dt
import time
import math

class Animal:
    def __init__(self,nm,spd):
        self.name=nm
        self.speed=spd
    def start(self):
        self.start_time=dt.now()
    def position(self):
        now=dt.now()
        t=(now-self.start_time).seconds
        x=math.cos(self.speed*t)
        y=math.sin(self.speed*t)
        return  (x,y)
        
