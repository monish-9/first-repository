import pyttsx3
import datetime
import speechRecognition as sr

engin=pyttsx3.init('sapi5')
voices=engin.getProperty('voices')
#print(voices[1].id)//female voice
engin.setProperty('voice',voices[1].id)


def speak(audio):
    engin.say(audio)
    engin.runAndWait()
def wishMe():
    time=datetime.datetime.now().hour
    if(time>=0 and time<12):
        speak("Good Morning!!")
    elif(time>=12 and time<18):
        speak("Good Afternoon!!")
    else:
        speak("Good Evening!!")
    speak("I am Jarvis Sir. Please tell me how may I help you")

if __name__ == '__main__':
    wishMe();
