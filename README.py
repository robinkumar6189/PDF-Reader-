# PDF-Reader-
'''it is a python program which can read any pdf for you and also it can read huge file for you'''
import pyttsx3
#reding files lines
filepath=input('enter the file path or its name you want to read')
f=open(f'{filepath}.txt','r')
a=f.read()
#importing pyaudio
voi=int(input("press 0 for mail vioc or press 1 for femail voice"))
print(a)

en=pyttsx3.init('sapi5')
voices=en.getProperty("voices")
#conditions for mail and femail voice
if voi==0:
    en.setProperty("voice",voices[0].id)
elif voi==1:
    en.setProperty("voice",voices[1].id)
else:
    en.setProperty("voice",voices[1].id)

#defining seeaking  module
def speeak(audio):
    en.say(audio)
    en.runAndWait()
speeak(a)
