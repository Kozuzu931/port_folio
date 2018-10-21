import speech_recognition as sr
import turtle

kame=turtle.Turtle()
kame.shape("turtle")
r = sr.Recognizer()

def input_command(c):
    if c=="前に進め":
        kame.forward(10)
    elif c=="後ろに進め":
        kame.backward(10)
    elif c=="右に回れ":
        kame.right(90)
    elif c=="左に回れ":
        kame.left(90)
    else:
        print("認識できませんでした")

while True:
    with sr.Microphone() as source:
      print("何かしゃべってください")
      audio = r.listen(source)
      message = r.recognize_google(audio, language='ja-JP',
                         key="AIzaSyDhy2VoPPJTUU90sB_Z2kx8ZqHHUft_RdE")
      input_command(message)
