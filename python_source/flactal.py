from turtle import *

def koch(n, length):
    if n <= 0:
        fd(length)
        return
    koch(n-1, length/3)
    lt(60)
    koch(n-1, length/3)
    rt(120)
    koch(n-1, length/3)
    lt(60)
    koch(n-1, length/3)

if __name__ == '__main__':
    n = 4
    length = 400
    pu()
    setpos(-200, 200)
    pd()
    speed(0)
    for _ in range(4):
        koch(n, length)
        rt(90)
    done()
