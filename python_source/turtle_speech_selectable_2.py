import speech_recognition as sr
import turtle
import re

kame=turtle.Turtle()
kame.shape("turtle")
r = sr.Recognizer()
def select(count):
    try:
        return int(c.group(3))
    except as AttributeError:
        return 10
    else:
        return 10
    finally:
        return 10



def input_command(d):
    c=re.search(r"([前後左右]).?.?([回転進下])([0-9]+)?",d)
    if c.group(1)=="前":
        if c.group(2)=="進":
            kame.forward(select(c.group(3)))
        else:
            print("認識できませんでした")
    elif c.group(1)=="後":
        if c.group(2)=="下" or "進":
        　kame.backward(select(c.group(3)))
        else:
            print("認識できませんでした")
    elif c.group(1)=="右":
        if c.group(2)=="回"　or "転" or "回転":
            kame.right(select(c.group(3)))
        else:
            print("認識できませんでした")
    elif c.group(1)=="左":
        if c.group(2)=="回"　or "転" or "回転":
            kame.left(select(c.group(3)))
        else:
            print("認識できませんでした")
    else:
        print("認識できませんでした")

while True:
    with sr.Microphone() as source:
      print("何かしゃべってください")
      audio = r.listen(source)
      message = r.recognize_google(audio, language='ja-JP',
                         key="AIzaSyDhy2VoPPJTUU90sB_Z2kx8ZqHHUft_RdE")
      input_command(message)
