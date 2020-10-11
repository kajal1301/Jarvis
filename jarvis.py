import pyttsx3
import speech_recognition as sr 
import datetime
import wikipedia
import webbrowser
import os




engine= pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()
def Increase_brightness():
    try:
        currrent_brightness=sbc.get_brightness()
        increased_brightness=currrent_brightness+10
        sbc.set_brightness(increased_brightness)
    except Exception as e:
        speak("sir brightness is full")

def Decrease_brightness():
    try:
        currrent_brightness=sbc.get_brightness()
        decreased_brightness=currrent_brightness-10
        sbc.set_brightness(decreased_brightness)
    except Exception as e:
        speak("sir brightness is low")


def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("Good Morning")
    elif hour> 12 and hour<=18:
        speak("Good Afternoon")
    else:
        speak("Good evening")
    speak("I am jarvis, How may I help you")
 
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)
   
   
    try:
        print("Recognizing")
        query= r.recognize_google(audio, language= 'en-in')
        print("user said:{query}\n")

    except Exception as e:
        print(e)
        print("Say that again please")
        return "None"
    return query


if __name__ == "__main__":
    wishMe()
    #while True:
    if 1:
        query = takeCommand().lower()
        if 'wikipedia'in query:
            speak("Searching in wikipedia")
            query= query.replace("wikipedia"," ")
            results= wikipedia.summary(query,sentences=2)
            speak("According to Wikipedia")
            speak(results)
        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")
        elif 'play music' in query:
            music_dir = 'C:\\Users\\admin\\Music\\songs'
            songs = os.listdir(music_dir)
            print(songs)    
            os.startfile(os.path.join(music_dir, songs[0]))
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")    
            speak(f"Kajal, the time is {strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\admin\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Visual Studio Code"
            os.startfile(codePath)
        elif 'open notepad' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\notepad++"
            os.startfile(codePath)
        elif 'open android studio' in query:
            codePath= "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Android Studio"   
            os.startfile(codePath)
         elif "increase the brightness" in query or "yes increase the brightness" in query or "increase brightness" in query:
            Increase_brightness()
            speak("sir should i increase the brightness or its good")

        elif "decrease the brightness" in query or "yes decrease the brightness" in query or "decrease brightness" in query:
            Decrease_brightness()
            speak("sir should i decrease the brightness or its good")
        elif "show battery status" in query:
            battery=psutil.sensors_battery()
            percent = str(battery.percent)
            plugged=battery.power_plugged
            #plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug='plugged'
            else:
                plug='not plugged'
            per = int(percent)
            # plugged = "Plugged In" if plugged else "Not Plugged In"
            if plugged:
                plug = "plugged"
            else:
                plug = "not_plugged"

            if plug == 'not_plugged' and per <= 30:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir please pluggin your charger because your battery is low ")
            elif plug == 'plugged' and battery > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'not_plugged' and per > 20:
                speak("Sir your battery is ")
                speak(percent)
            elif plug == 'plugged' and battery <= 20:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is low dont remove your charger")
            elif plug == 'plugged' and battery == 100:
                speak("Sir your battery is ")
                speak(percent)
                speak("sir your battery is full please remove charger ")
            else:
                print(percent)

    #speak("Hello kajal, how are you")
