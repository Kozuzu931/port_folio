from turtle import*
from animal_circle import Animal

addshape("")
usako_t=Turtle(shape="")
usako=Animal("うさこ",0.1)
usako.start()

scale=100

def move_usako():
    (x,y)=usako.position()
    usako_t.setx(scale*x)
    usako_t.sety(scale*y)
    ontimer(move_usako,1000)

    move_usako()
