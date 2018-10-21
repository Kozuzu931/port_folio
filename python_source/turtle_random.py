import random
import turtle

kame=turtle.Turtle()
kame.shape("turtle")

while True:
    x=random.uniform(-100,100)
    y=random.uniform(-100,100)
    e=abs(turtle.xcor())
    f=abs(turtle.ycor())
    if e >= 50 or f >= 50 or e <= -50 or f <= -50:
        pass
    else:
        kame.goto(x,y)
