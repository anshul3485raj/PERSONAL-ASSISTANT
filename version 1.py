import pyttsx3
import os
import speech_recognition as sr
import webbrowser
import wmi
import randfacts
import time
import joke
import random
import timedisplay
from PyDictionary import PyDictionary
import pdb

dictionary = PyDictionary()
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def speak(audioo):
    engine.say(audioo)
    engine.runAndWait()


if os.path.isfile("username.txt") is False:
    speak("sir what is your name")
    Q_order=str(input("Enter your name"))
    fn = open("username.txt",'w+')
    fn.write(Q_order)
    fn.close()
    fn = open("username.txt",'r')
    call_username = fn.read()
    speak("so i will call you ")
    speak(call_username)
    speak("what do you want to call me give me a good nick name")
    wad=str(input("give me nickname of your choice"))
    f=open("callable.txt",'w+')
    f.write(wad)
    f.close()
    f = open("callable.txt", "r")
    calld_able=f.read()
    speak("I like that")
    speak("thanks for gvinig me such a good call_username" + calld_able)
    speak(call_username)
fn = open("username.txt", 'r')
f = open("callable.txt","r")
r = f.read()
rt = fn.read()
hotword = r
call_username = r
name = rt
fn.close()
f.close()

def voice_input():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.adjust_for_ambient_noise(source)
        r.pause_threshold = 1
        audio = r.listen(source)
        Q_order=""
        try:
            Q_order = r.recognize_google(audio, language='en-in')
        except Exception as e:
            "pass"

    return Q_order.lower()



if __name__ == "__main__":
    wake_key = hotword

    while True:
        t = voice_input()
        if t.count(wake_key) > 0:
            print("listening")
            speak("tada")

            uInput = voice_input()
            print(f"{name}: {uInput}\n")
            if 'xc' in uInput:
                print("k")
            elif 'open youtube' in uInput or 'go to youtube' in uInput or 'youtube' in uInput:
                speak('okay')
                webbrowser.open('www.youtube.com')
            elif 'open google' in uInput or 'go to google' in uInput:
                speak('okay')
                webbrowser.open('www.google.com')
            elif 'open' in uInput or 'take me to ' in uInput or 'go to' in uInput:
                if 'open' in uInput:
                    website = uInput.split(" ")
                    # speak(call_username+'which website')
                    # website=voice_input()
                    website = str(website[1])
                    if website == 'instagram':
                        webbrowser.open("https://www.instagram.com")
                    elif website == 'yahoo':
                        webbrowser.open("https://www.yahoo.com")
                    elif website == 'gmail':
                        webbrowser.open("https://www.gmail.com")
                    elif website == 'amazon':
                        webbrowser.open("https://www.amazon.com/")
                    elif website == 'flipkart':
                        webbrowser.open("https://www.flipkart.com")
                    elif website == 'stackoverflow':
                        webbrowser.open("https://www.stackoverflow.com")
                    else:
                        webbrowser.open("https://www.google.com/search?q=" + website)
                elif 'take me to' in uInput:
                    website = uInput.split(" ")
                    # speak(call_username+'which website')
                    # website=voice_input()
                    website = str(website[3])
                    if website == 'instagram':
                        webbrowser.open("https://www.instagram.com")
                    elif website == 'yahoo':
                        webbrowser.open("https://www.yahoo.com")
                    elif website == 'gmail':
                        webbrowser.open("https://www.gmail.com")
                    elif website == 'amazon':
                        webbrowser.open("https://www.amazon.com/")
                    elif website == 'flipkart':
                        webbrowser.open("https://www.flipkart.com")
                    elif website == 'stackoverflow':
                        webbrowser.open("https://www.stackoverflow.com")
                    else:
                        webbrowser.open("https://www.google.com/search?q=" + website)
                elif 'go to' in uInput:
                    website = uInput.split(" ")
                    # speak(call_username+'which website')
                    # website=voice_input()
                    website = str(website[2])
                    if website == 'instagram':
                        webbrowser.open("https://www.instagram.com")
                    elif website == 'yahoo':
                        webbrowser.open("https://www.yahoo.com")
                    elif website == 'gmail':
                        webbrowser.open("https://www.gmail.com")
                    elif website == 'amazon':
                        webbrowser.open("https://www.amazon.com/")
                    elif website == 'flipkart':
                        webbrowser.open("https://www.flipkart.com")
                    elif website == 'stackoverflow':
                        webbrowser.open("https://www.stackoverflow.com")
                    else:
                        webbrowser.open("https://www.google.com/search?q=" + website)
            elif 'shutdown pc' in uInput or 'shutdown my system' in uInput or 'shutdown my desktop' in uInput or 'shutdown' in uInput:
                speak("shutting down your system. please confirm you want to countine or not")
                cnfrm = voice_input()
                if 'no' in cnfrm or 'no dont ' in cnfrm or 'dont restart' in cnfrm:
                    speak("okay, mission abort "+name)
                    pass
                else:
                    speak('please save your unsaved work your device will shutdown in t-60 second')
                    time.sleep(60)
                    speak("shuting down")
                    os.system("shutdown /s /t 1")
            elif'restart my pc' in uInput or 'restart my device' in uInput or 'restart pc' in uInput:
                speak("restarting your system. please confirm you want to countine or not")
                cnfrm = voice_input()
                if'no' in cnfrm or 'no dont ' in cnfrm or 'dont restart' in cnfrm:
                    speak("okay, mission abort " + name)
                    pass
                else:
                    speak('please save your unsaved work your device will restart in t-60 second')
                    time.sleep(60)
                    os.system("shutdown /r /t 1")
            elif 'pc sleep' in uInput or 'put my device on sleep' in uInput or 'sleep' in uInput:
                speak("putting your pc on sleep, please confirm you want to countine or not")
                cnfrm = voice_input()
                if 'no' in cnfrm or 'no dont ' in cnfrm or 'dont restart' in cnfrm:
                    speak("okay, mission abort " + name)
                    pass
                else:
                    speak('take a break'+call_username)
                    time.sleep(6)
                    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")
            elif 'fact' in uInput or "tell me a fact" in uInput or "please tell me a fact" in uInput:
                speak('a great fact coming for you'+call_username)
                fact = randfacts.getFact()
                print(fact)
                speak(fact)
            elif 'tell me meaning of' in uInput or 'what does' in uInput or 'meaning of' in uInput or 'define' in uInput:
                if 'tell me meaning of' in uInput:
                    word = uInput.split(" ")
                    word = str(word[4])
                    print(dictionary.meaning(word))
                    speak(dictionary.meaning(word))
                if 'what does' in uInput or 'meaning of' in uInput:
                    word = uInput.split(" ")
                    word = str(word[2])
                    print(dictionary.meaning(word))
                    speak(dictionary.meaning(word))
                if 'define' in uInput:
                    word = uInput.split(" ")
                    word = str(word[1])
                    print(dictionary.meaning(word))
                    speak(dictionary.meaning(word))
            elif 'joke'  in uInput :
                ug=joke.getjoke()
                print(ug)
                speak(ug)

                # TODO  add fc feature , add gui
            elif 'commit suicide' in uInput or 'i am going to kill myself' in uInput or 'i will kill myself' in uInput:
                speak("sending mail to your parents, telling them to look after you")
                speak("hey you are not alone, anyone whom  you like to talk")
                ask=voice_input()
                if"yes"in ask or "yes to" in ask or"yup i would " in ask:
                    if "yup i would " in ask:
                        name = ask.split(" ")
                        print(speak("getting" + name[5] + "on-line for you" + call_username))
                    if "yes to"in ask:
                        name=ask.split(" ")
                        print(speak("getting" + name[2] + "on-line for you" + call_username))
                    if "yes" in ask:
                        tt = ask.split(" ")

                        if len(tt)!=0:
                            name=tt[1]
                            print(speak("getting" + name + "on-line for you" + call_username))
                        if len(tt)==1:
                            speak("whom would you like to talk pls tell name")
                            ask = voice_input()
                            ask=ask.split(" ")
                            name=ask[0]

                            if len(ask)!=0:
                                print(speak("getting"+name+"on-line for you"+call_username))
            elif 'hi' in uInput or 'hello' in uInput or 'hey' in uInput :
                greetings=("hi","how are you",'yo',"how you doing")
                r=random.choice(greetings)+""+call_username
                speak(r)
                uInput=voice_input()
                if"good"  in uInput or "fine" in uInput or "doing great" in uInput or "great" in uInput :
                    pos_rev= ("good to hear that","nice","great","you look fresh and active","perfect")
                    r = random.choice(pos_rev) + "" + call_username
                    speak(r)
                    fut_rev=("i knewed you were about to ask that, im doing great","between im good too","between im just like you")
                    speak(fut_rev)
                elif"sad" in uInput or "not good"in uInput :
                    speak("hey"+call_username+"dont worry do you wanna share your problem with me")
                    ask=voice_input()
                    if "yes" in ask or "yeah" in ask or "yup" in ask:
                        import bot
                        speak("okay "+call_username+"lets start")
                        os.open("bot.py")
                    if "no" in uInput or "not at all" in uInput:
                        speak("thats sad you dont wanna talk to me, but im now telling your parents to look after you ")
                        #TODO mail support here , wikki search option
                        speak("mail sent they will check on you")
            elif 'good morning' in uInput or 'good evening' in uInput or 'good afternoon'in uInput or 'morning' in uInput or 'evening' in uInput or 'night' in uInput:
                import datetime
                now = datetime.datetime.now()
                time = int(datetime.datetime.now().hour)
                t=['good morning','good evening','good night','good afternon']
                if time>=12 and time <16:
                    t=t[3]
                    if t==uInput:
                        speak(t+call_username)
                        print(now.strftime("%H:%M"))
                    if t!=uInput:
                        speak(call_username+"do you think im fool between"+t+call_username)
                    print(now.strftime("%H:%M"))
                elif time>=16 and time <19:
                    t=t[1]
                    if t==uInput:
                        speak(t+call_username)
                        print(now.strftime("%H:%M"))
                    if t!=uInput:
                        speak(call_username+"do you think im fool between"+t+call_username)
                        print(now.strftime("%H:%M"))


                elif time>=3and time <12:
                    t=t[0]
                    if t==uInput:
                        speak(t + call_username)
                        print(now.strftime("%H:%M"))
                    if t!=uInput:
                        speak(call_username+"do you think im fool between"+t+call_username)
                        print(now.strftime("%H:%M"))
                elif time>19 and time <3:
                    t="you should sleep btw its night"
                    print('ds')
                    if t==uInput:
                        speak(t+call_username)
                    if t!=uInput:
                        speak(call_username+"do you think im fool"+t+call_username)
                        print(now.strftime("%H:%M"))




            elif "time" in uInput:
                timedisplay.main()



