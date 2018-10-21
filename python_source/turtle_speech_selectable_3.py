import turtle
import re

kame=turtle.Turtle()
kame.shape("turtle")





def input_command(d):
    c=re.search(r"([f]|[b]|[l]|[r])([0-9]+)",d)
    if c.group(1)=="f":
            kame.forward((c.group(2))
        else:
            print("認識できませんでした")
    elif c.group(1)=="b":
        kame.backward(c.group(2))
    elif c.group(1)=="r":
        kame.right(c.group(2))
    elif c.group(1)=="l":
        kame.left(c.group(2))
    else:
        print("認識できませんでした")

while True:
    a=input("コマンド・・・？ex:f10")
    input(a)
