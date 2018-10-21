import speech_recognition as sr
# マイクから音声を収集する
r = sr.Recognizer()
# with構文は次週学びます。ここではマイクの
# 利用開始・終了を確実に行うために利用しています。
with sr.Microphone() as source:
  print("何かしゃべってください")
  audio = r.listen(source)
# 音声を認識する
try:
  message = r.recognize_google(audio, language='ja-JP',
                     key="AIzaSyDhy2VoPPJTUU90sB_Z2kx8ZqHHUft_RdE") # APIキーは授業のときに先生に聞いてください。予習で使いたい方はキーの取得方法をスライドにかいてありますので、ご利用ください。
  print("認識結果:", message) # 認識結果はmessage変数に文字列として入る
except sr.UnknownValueError:
  print("音声を認識できませんでした")
except sr.RequestError as e:
  print("結果を取得できませんでした; {0}".format(e))
