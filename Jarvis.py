import pyttsx3 
import speech_recognition as sr 
import datetime
import wikipedia 
import webbrowser
import os 
import smtplib
import pyautogui
import time
import sys
import speedtest
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()
         
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")   

    else:
        speak("Good Evening!")        
        speak("hello sir i am jarvis")
        speak("how can i help you")        

def takeCommand():

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening the command...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing the command...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
           
        print("Say that again please...")  
        return "None"
    return query

def tasks():
    wishMe()
    while True:
    
        query = takeCommand().lower()
        
        if 'change password' in query:
            speak("What is the new password")
            new_pw = input("Enter the new password here:")
            new_password = open("Password.txt","w")
            new_password.write(new_pw)
            new_password.close()
            speak("Sir Done")
            print("Sir Done")
            speak("Your password is changed")
            print("Your password is changed")
            speak(f"Youe new password is {new_pw}")
            print(f"Youe new password is {new_pw}")
        
        elif 'open youtube' in query:
            print("Youtube s opening")
            speak("Youtube s opening\n")
            webbrowser.open("youtube.com")

        elif 'close chrome' in query:
            print("closing chrome")
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'close youtube' in query:
            print("closing youtube")
            speak("closing youtube")
            os.system("taskkill /f /im msedge.exe")

        elif 'close google' in query:
            print("closing google")
            speak("closing google")
            os.system("taskkill /f /im msedge.exe")

        elif 'play pokemon movie' in query:
            npath = ""#Add path to movie
            print("playing pokemon movie")
            speak("playing pokemon movie")
            os.startfile(npath)

        elif 'open bluestacks' in query:
            print("opening notepad")
            speak("opning bluestacks")
            os.system("C:\\Program Files\\BlueStacks_bgp64\\Bluestacks.exe")

        elif 'open Gmail' in query:
            print("opening Gmail")
            speak("opning gmail")
            os.system("C:\\Windows.old\\Users\\xstechcoding\\AppData\\Local\\Google\\Chrome\\Application\\chrome_proxy.exe  --profile-directory=Default --app-id=fmgjjmmmlfnkbppncabfkddbjimcfncm")

        elif 'open Google Drive' in query:
            print("opening google drive")
            speak("opning google drive")
            os.system

        elif "restart the system" in query:
            speak("Are you sure to restart the system")
            qret = takeCommand().lower()
            if 'yes' in query or 'sure' in query: 
                os.system("restart /r /t 5")
                
            else:
                speak("OK")

        elif "Lock the system" in query:
            speak("Are you sure to lock the system")
            qret = takeCommand().lower()
            if 'yes' in query or 'sure' in query: 
                os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

            else:
                speak("OK")

        elif 'open notepad' in query:
            print("opening notepad")
            speak("opening notepad")
            os.startfile("C:\\Windows\\System32\\notepad.exe")

        elif "close notepad" in query:
            print("closing notepad")
            speak("closing notepad")
            os.system("taskkill /f /im notepad.exe")

        elif "open command prompt" in query:
            print("opning command prompt")
            speak("opning command prompt")
            os.system("start cmd")

        elif "close command prompt" in query:
            print("closing command prompt")
            speak("closing command prompt")
            os.system("taskkill /f /im cmd.exe")

        elif "open calculator" in query:
            print("opening calculator")
            speak("opening calculator")
            os.system("C:\\Windows.old\\Windows\\WinSxS\\wow64_microsoft-windows-calc_31bf3856ad364e35_10.0.10240.16397_none_bc130c25e9ca15b2")

        elif "close calculator" in query:
            print("closing calculator")
            speak("closing calculator")
            os.system("taskkill /f /im calc.exe")

        elif "volume up" in query:
                print("Increasing volume")
                speak("Increasing volume")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")
                pyautogui.press("volumeup")

        elif "volume down" in query:
                print("Decreasing volume")
                speak("Decreasing volume")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")
                pyautogui.press("volumedown")

        elif "mute" in query:
                pyautogui.press("volumemute")

        elif "refresh" in query:
                print("OK")
                speak("OK")
                pyautogui.moveTo(1551,551, 2)
                pyautogui.click(x=1551, y=551, clicks=1, interval=0, button='right')
                pyautogui.moveTo(1620,667, 1)
                pyautogui.click(x=1620, y=667, clicks=1, interval=0, button='left')
                
        elif "scroll down" in query:
                print("Scrolling down")
                speak("Scrolling down")
                pyautogui.scroll(1000)

        elif "open paint" in query:
                print("opning ms paint")
                speak("opning ms paint")
                os.system("%windir%\system32\mspaint.exe")

        elif "close paint" in query:
                print("closing paint")
                speak("closing paint")
                os.system("taskkill /f /im mspaint.exe")

        elif "who are you" in query:
                print('My Name Is jarvis')
                speak('My Name Is jarvis')
                print('I can Do Everything that my creator programmed me to do')
                speak('I can Do Everything that my creator programmed me to do')

        elif "who created you" in query:
                print('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
                speak('I Do not Know His Name, I created with Python Language, in Visual Studio Code.')
        
        elif 'type' in query: 
                query = query.replace("type", "")
                pyautogui.write(f"{query}")

        elif 'Enter HTML code' in query: 
                query =  '''<html>
                            <head>
                            	<!-- Information about the page -->
                            	<!--This is the comment tag-->

                            	<title>GeeksforGeeks</title>
                            </head>

                            <body>
                            	<!--Contents of the webpage-->
                            </body>

                            </html>
                            '''
                pyautogui.write(f"{query}")

        elif 'open chrome' in query:
            print("opning chrome")
            speak("opning chrome")
            os.startfile("")#Add path to chrome

        elif 'maximize this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('x')

        elif 'open new window' in query:
            pyautogui.hotkey('ctrl', 'n')

        elif 'open incognito window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'n')

        elif 'minimise this window' in query:
            pyautogui.hotkey('alt', 'space')
            time.sleep(1)
            pyautogui.press('n')

        elif 'open history' in query:
            pyautogui.hotkey('ctrl', 'h')

        elif 'open downloads' in query:
            pyautogui.hotkey('ctrl', 'j')

        elif 'previous tab' in query:
            pyautogui.hotkey('ctrl', 'shift', 'tab')

        elif 'next tab' in query:
            pyautogui.hotkey('ctrl', 'tab')

        elif 'close tab' in query:
            pyautogui.hotkey('ctrl', 'w')

        elif 'close window' in query:
            pyautogui.hotkey('ctrl', 'shift', 'w')

        elif 'clear browsing history' in query:
         pyautogui.hotkey('ctrl', 'shift', 'delete')

        elif 'close chrome' in query:
            print("closing chrome")
            speak("closing chrome")
            os.system("taskkill /f /im chrome.exe")

        elif 'sleep' in query:
            speak("OK sir")
            speak("you can call me anytime")
            speak("just say wake up jarvis")
            break
        
        elif 'how are you' in query:
            print("I am fine, Thank you")
            print("How are you, ")
            speak("I am fine, Thank you")
            speak("How are you, ")

        elif "good morning" in query or "good afternoon" in query or "good evening" in query:
            speak("A very" +query)
            speak("Thank you for wishing me! Hope you are doing well!")

        elif 'fine' in query or "good" in query:
            print("It's good to know that your fine")
            speak("It's good to know that your fine")
       
        elif "who are you" in query:
            print("I am your virtual assistant.")
            speak("I am your virtual assistant.")

        elif "write a note" in query:
            speak("What should i write, sir")
            note = takeCommand()
            file = open('jarvis.txt', 'w')
            speak("Sir, Should i include date and time")
            snfm = takeCommand()
            if 'yes' in snfm or 'sure' in snfm:
                strTime = datetime.datetime.now().strftime("% H:% M:% S")
                file.write(strTime)
                file.write(" :- ")
                file.write(note)
            else:
                file.write(note)
             
        elif 'exit' in query:
            exit()     
                
        elif "schedule my day" in query:
                    tasks = [] #Empty list 
                    speak("Do you want to clear old tasks (Plz speak YES or NO)")
                    query = takeCommand().lower()
                    if "yes" in query:
                        file = open("schedule.txt","w")
                        file.write(f"")
                        file.close()
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        i = 0
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("schedule.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
                    elif "no" in query:
                        i = 0
                        no_tasks = int(input("Enter the no. of tasks :- "))
                        for i in range(no_tasks):
                            tasks.append(input("Enter the task :- "))
                            file = open("schedule.txt","a")
                            file.write(f"{i}. {tasks[i]}\n")
                            file.close()
            
        elif "focus mode" in query:
                    a = int(input("Are you sure that you want to enter focus mode :- [1 for YES / 2 for NO "))
                    if (a==1):
                        speak("Entering the focus mode....")
                        exit()   
                    else:
                        pass
      
        elif "translate" in query:
                    from Translator import translategl
                    query = query.replace("jarvis","")
                    query = query.replace("translate","")
                    translategl(query)         
                    
        elif "internet speed" in query:
                    wifi  = speedtest.Speedtest()
                    upload_net = wifi.upload()/1048576         #Megabyte = 1024*1024 Bytes
                    download_net = wifi.download()/1048576
                    print("Internet Upload Speed is", upload_net)
                    print("Internet download speed is ",download_net)
                    speak(f"Internet download speed is {download_net}")
                    speak(f"Internet Upload speed is {upload_net}")                    
            
        elif "ipl score" in query:
                    from plyer import notification  #pip install plyer
                    import requests #pip install requests
                    from bs4 import BeautifulSoup #pip install bs4
                    url = "https://www.cricbuzz.com/"
                    page = requests.get(url)
                    soup = BeautifulSoup(page.text,"html.parser")
                    team1 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[0].get_text()
                    team2 = soup.find_all(class_ = "cb-ovr-flo cb-hmscg-tm-nm")[1].get_text()
                    team1_score = soup.find_all(class_ = "cb-ovr-flo")[8].get_text()
                    team2_score = soup.find_all(class_ = "cb-ovr-flo")[10].get_text()

                    a = print(f"{team1} : {team1_score}")
                    b = print(f"{team2} : {team2_score}")

                    notification.notify(
                        title = "IPL SCORE :- ",
                        message = f"{team1} : {team1_score}\n {team2} : {team2_score}",
                        timeout = 15
                    )
            
        elif "play a game" in query:
                    from game import game_play
                    game_play()
        
        elif "screenshot" in query:
                     import pyautogui 
                     im = pyautogui.screenshot()
                     im.save("ss.jpg")
        
        elif "tired" in query:
                    speak("Playing your favourite songs, sir")
                    a = (1,2,3)
                    b = random.choice(a)
                    if b==1:
                        webbrowser.open("")#add url to your fav song
                    
        elif "open" in query:
            from Dictapp import openappweb
            openappweb(query)
                    
        elif "close" in query:
            from Dictapp import closeappweb
            closeappweb(query)
        
        elif "google" in query:
            from SearchNow import searchGoogle
            searchGoogle(query)
                    
        elif "youtube" in query:
            from SearchNow import searchYoutube
            searchYoutube(query)
            
        elif "wikipedia" in query:
            from SearchNow import searchWikipedia
            searchWikipedia(query)
        
        elif "news" in query:
                    from NewsRead import latestnews
                    latestnews()
        
        elif "temperature" in query:
            wp = takeCommand()
            search = ("temperature in" + {wp})
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")
            
        elif "weather" in query:
            ws = takeCommand()
            search = ("weather in" + {wp})
            url = f"https://www.google.com/search?q={search}"
            r  = requests.get(url)
            data = BeautifulSoup(r.text,"html.parser")
            temp = data.find("div", class_ = "BNeawe").text
            speak(f"current{search} is {temp}")

        elif "set an alarm" in query:
                    print("input time example:- 10 and 10 and 10")
                    speak("Set the time")
                    a = input("Please tell the time :- ")
                    alarm(a)
                    speak("Done,sir")
        
        elif "the time" in query:
                    strTime = datetime.datetime.now().strftime("%H:%M")    
                    speak(f"Sir, the time is {strTime}")
        
        elif "remember that" in query:
                    rememberMessage = query.replace("remember that","")
                    rememberMessage = query.replace("jarvis","")
                    speak("You told me to remember that"+rememberMessage)
                    remember = open("Remember.txt","a")
                    remember.write(rememberMessage)
                    remember.close()
                    
        elif "what do you remember" in query:
            remember = open("Remember.txt","r")
            speak("You told me to remember that" + remember.read())

        elif "shutdown system" in query:
                    speak("Are You sure you want to shutdown")
                    shutdown = input("Do you wish to shutdown your computer? (yes/no)")
                    if shutdown == "yes":
                        os.system("shutdown /s /t 1")

                    else:
                     shutdown == "no"
                    break
        
    else:
        speak("Sorry, I am not able to understand you")

for i in range(2):
    speak("Enter the password to access jarvis")
    a = input("Enter the password to access jarvis:")
    pw_file = open("Password.txt","r")
    pw = pw_file.read()
    pw_file.close()
    if (a==pw):
        print("Access granted")
        speak("Access granted")
        print("Say [Wake Up] to start jarvis")
        speak("Say [Wake Up] to start jarvis")
        break
    
    elif (a!=pw):
        print("Access not granted")
        speak("Access not granted")
        print("Try again")
        speak("Try again")
        sys.exit()

if __name__ == "__main__":
    while True:
        permission = takeCommand()
        if 'wake up' in permission:
            tasks()
        elif 'bye' in permission:
            speak("bye sir")
            sys.exit()
            
def alarm(query):
    timehere = open("Alarmtext.txt","a")
    timehere.write(query)
    timehere.close()
    os.startfile("alarm.py")
    
    