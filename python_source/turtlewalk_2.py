import random
import turtle
import math

kame=turtle.Turtle()
kame.shape("turtle")
kame.penup()
kame.goto(0, -100)
kame.pendown()
kame.circle(100)
kame.penup()
kame.home()
kame.pendown()
while True:
    if kame.distance(0,0)>100:
        kame.undo()
        kame.undo()
        kame.penup()
        kame.home()
        kame.pendown()
    else:
         kame.forward(10)
         kame.left(random.choice([0,90,180,270]))

  
