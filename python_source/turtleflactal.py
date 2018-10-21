from turtle import*
def move(n):
    if n=="f":
        forward(10)
        return n
    elif n=="r":
        right(60)
        return n
    elif n=="l":
        left(60)
        return n

    comand="frr"*3
