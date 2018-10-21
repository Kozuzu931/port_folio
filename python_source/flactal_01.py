from turtle import *
kame=Turtle()
kame.shape("turtle")

def koch(n, length):
    if n <= 0:
        fd(length)
        return
    koch(n-1, length/3)
    left(60)
    koch(n-1, length/3)
    right(120)
    koch(n-1, length/3)
    left(60)
    koch(n-1, length/3)

koch(3,300)
