import speech_recognition as sr
import turtle

kame=turtle.Turtle()
kame.shape("turtle")
r = sr.Recognizer()
c=0
message=[]
def input_command(c):
    if c=="前に進め":
        kame.forward(10)
    if c=="後ろに進め":
        kame.backward(10)
    if c=="右に回れ":
        kame.right(90)
    if c=="左に回れ":
        kame.left(90)#認識できませんでした。

while c!=3:

    with sr.Microphone() as source:
         print("何かしゃべってください")
         audio = r.listen(source)
         message.append(r.recognize_google(audio, language='ja-JP',
                            key="AIzaSyDhy2VoPPJTUU90sB_Z2kx8ZqHHUft_RdE"))
    c+=1
for s in range(0,2):
    input_command(message[s])
