import turtle
def koch(kame,length,level):
    if level < 0:
        forward(length)
        return
    elif level==0:
        kame.forward(length)
        return
    else:
        new_length=length/3
        koch(level-1,length/3)
        kame.lt(60)
        koch(level-1,length/3)
        kame.rt(120)
        koch(level-1,length/3)
        kame.lt(60)
        koch(level-1,length/3)

kame=turtle.Turtle()
kame.shape("turtle")
koch(kame,300,3)
