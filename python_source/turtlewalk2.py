import random
import turtle

kame=turtle.Turtle()
kame.register_shape("fate.gif")

c=0
while c!=50:
    kame.forward(10)
    kame.left(random.choice([0,90,180,270]))
    c+=1
while True:
    kame.goto(random.randint(-1000,1000),random.randint(-1000,1000))
