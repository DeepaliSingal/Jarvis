#cd C:\Users\91999\AppData\Local\Programs\Python\Python39\Scripts
#run as administrator cmd
#run-->sysdm.cpl ---->advanced-->environment variable -->path -->edit
#to resolve module not found error head to unofficial python binaries website-->gholke
#install pyaudio there show in folder -> shift+right click  window powershell pip install file name downloaded

#to convert any ui file from designer to py file go to that file location and open cmd there and write pyuic5 -x filename.ui -o filename.py
#pip install pyttsx3 from cmd 
#follow same for other modules as well
import pyttsx3
import speech_recognition as SR
import datetime
import os
import PyPDF2
import cv2
import PyQt5
import bs4
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
import random
import webbrowser
import sys
import requests
import weather,linkedinlogin
import wordoperations
from requests import get
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QTimer,QTime,QDate,Qt
from PyQt5.QtCore import *
from PyQt5.QtGui import QMovie
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.uic import loadUiType
from jarvisui import Ui_MainWindow

engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

#you can change voice by the indexing
engine.setProperty('voices',voices[1].id)

class MainThread(QThread):
    def __init__(self):
        super(MainThread,self).__init__()

    def run(self):
        self.speak("Don't forget to wake me up whenever you need me!!")
        while True:
            self.query=self.takecommand()
            if "wake up" in self.query:
                self.speak('HII!! this is advanced JARVIS to make your life more amazing')
                self.wish()
                self.tasks()

    def speechrate(self):
        self.speak("please specify the rate to which you would like to change")
        mystring=int(input())
        engine.setProperty('rate',mystring)
        self.speak("My speech rate changed successfully")
    
    def pdf_reader(self):
        book=open('1.pdf','rb')
        pdfReader=PyPDF2.PdfFileReader(book)
        pages=pdfReader.numPages
        self.speak(f"total number of pages in this book {pages}")
        for i in range(1,pages):
            page=pdfReader.getPage(i)
            text=page.extractText()
            self.speak(text)

    #function for speech
    def speak(self,audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

    #to perform tasks
    def tasks(self):
        while True:
            self.query=self.takecommand().lower()

            #tasks
            if "open word" in self.query:
                path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Accessories\WordPad"
                os.startfile(path)
                self.speak("Do u wanna write too?")
                yon=self.takecommand()
                if(yon):
                    self.speak("tell the drive you wanna save to")
                    drive=self.takecommand()
                    self.speak("tell the name with which you wanna save")
                    name=self.takecommand()
                    self.speak("enter the number of paras")
                    num=int(input())
                    wordoperations.write(num,name,drive)

            elif "login to linkedin" in self.query:
                self.speak("please enter your mail id")
                email=input()
                self.speak("please enter your password")
                password=input()
                value=linkedinlogin.start(email,password)
                if value:
                    self.speak("Logged in successfully")
                else:
                    self.speak("couldn't login")

            elif "open notepad" in self.query:
                path="C:\Windows\notepad.exe"
                os.startfile(path)

            elif "close notepad" in self.query:
                os.system("taskkill /f /im notepad.exe")

            elif "give me the weather updates" in self.query:
                self.speak("please tell me the name of city you wanna know weather of")
                city=self.takecommand()
                city=city+" weather"
                response=weather.weather(city)
                for info in response:
                    self.speak(info)

            elif "open microsoft word" in self.query:
                path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Word.lnk"
                os.startfile(path)
                
            elif "close microsoft word" in self.query:
                os.system("taskkill /f /im Word.exe")

            elif "open excel" in self.query:
                path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Excel.lnk"
                os.startfile(path)

            elif "close excel" in self.query:
                os.system("taskkill /f /im Excel.exe")

            elif "open powerpoint" in self.query:
                path="C:\ProgramData\Microsoft\Windows\Start Menu\Programs\PowerPoint.lnk"
                os.startfile(path)

            elif "close powerpoint" in self.query:
                os.system("taskkill /f /im PowerPoint.exe")

            elif "trending news" in self.query:
                news_url="https://news.google.com/news/rss"
                Client=urlopen(news_url)
                xml_page=Client.read()
                Client.close()

                soup_page=soup(xml_page,"xml")
                news_list=soup_page.findAll("item")
                # Print news title, url and publish date
                for news in news_list:
                    self.speak(news.title.text)
                    print(news.link.text)
                    print(news.pubDate.text)
                    print("-"*60)

            elif "do some calculations" in self.query:
                response=['Welcome to smart calculator','Thanks for using me ','Sorry ,this is  beyond my ability']
                # fetching tokens from the text command
                def to_suffix( s):
                    st = []
                    ret = ''
                    tokens = s.split()
                    for tok in tokens:
                        if tok in ['multiply', 'divide','MULTIPLY','DIVIDE','*','/','X']:
                            while st and st[-1] in ['multiply', 'divide','MULTIPLY','DIVIDE','*','/','X']:
                                ret += st.pop() + ' '
                            st.append(tok)
                        elif tok in ['PLUS', 'MINUS','plus','minus','+','-']:
                            while st and st[-1] != '(':
                                ret += st.pop() + ' '
                            st.append(tok)
                        elif tok == '(':
                            st.append(tok)
                        elif tok == ')':
                            while st[-1] != '(':
                                ret += st.pop() + ' '
                            st.pop()
                        else:
                            ret += tok + ' '
                    while st:
                        ret += st.pop() + ' '
                    return ret

                def eva(s):
                        st = []
                        tokens = s.split()
                        for tok in tokens:
                            if tok.upper() not in op:
                                st.append(float(tok))
                            else:
                                n1 = st.pop()
                                n2 = st.pop()
                                st.append(op[tok](n2, n1))
                        return st.pop()
  
                def evaluate(string):
                        # print(self.to_suffix(string))
                        return eva(to_suffix(string))

                def extract_from_text(text):
                    l=[]
                    for t in text.split(' '):
                        try:
                            l.append(float(t))
                        except ValueError:
                            pass
                    return l
 
                # calculating LCM
                def lcm(a,b):
                    L=a if a>b else b
                    while L<=a*b:
                        if L%a==0 and L%b==0:
                            return L
                        L+=1
 
                # calculating HCF
                def hcf(a,b):
                    H=a if a<b else b
                    while H>=1:
                        if a%H==0 and b%H==0:
                            return H
                        H-=1
 
                # Addition
                def add(a,b):
                    return a+b
 
                # Subtraction
                def sub(a,b):
                    return a-b
 
                # Multiplication
                def mul(a,b):
                    return a*b
 
                # Division
                def div(a,b):
                    return a/b
 
                # Remainder
                def mod(a,b):
                    return a%b
 
                # Response to command
                def end():
                    self.speak(response[1])
                    return
  
                def sorry():
                    self.speak(response[2])
                    print(response[2])
  
                # Operations - performed on the basis of text tokens
                op={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,
                            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,
                            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,
                            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,
                            'DIVISION':div,'DIVIDE':div,'MOD':mod,'REMAINDER'
                            :mod,'MODULAS':mod,'+':add,'-':sub,'/':div,'*':mul,'add':add,'minus':sub,'divide':div,'multiply':mul,'X':mul}
 
                # commands
                commands={'EXIT':end,'END':end,'CLOSE':end}
                self.speak('--------------'+response[0]+'------------')
                while True:
                    self.speak("tell me your query")
                    expression=self.takecommand()
                    try:
                        result=evaluate(expression)
                        self.speak(result)
                    except:
                        end()
                        break

            elif "open command prompt" in self.query:
                os.system("start end")

            elif "open camera" in self.query:
                capture=cv2.VideoCapture(0)  #for internal camera 0 index is used 
                while True:
                    ret, img = capture.read()
                    cv2.imshow('webcam',img)
                    k = cv2.waitKey(50)
                    if k==1 :
                        break
                capture.release()
                cv2.destroyAllWindows()

            elif "play music" in self.query:
                directory_music=""                    #use the location where music files are located 
                songs=os.listdir(directory_music)
                # for song in songs:
                #if song.endswith('.mp3')
                #to play only .mp3 files
                rd=random.choice(songs)
                os.startfile(os.path.join(directory_music,rd))

            elif "ip address" in self.query:
                ip=get('https://api.ipify.org').text
                self.speak(f"your IP address is {ip}")

            elif "open youtube" in self.query:
                webbrowser.open("www.youtube.com")

            elif "open google" in self.query:
                self.speak("What shud I search for?")
                cm=self.takecommand().lower()
                webbrowser.open(f"{cm}")

            elif "close word" in self.query:
                os.system("taskkill /f /im wordpad.exe")

            elif "shutdown the system" in self.query:
                os.system("shutdown /s /t 5")

            elif "restart the system" in self.query:
                os.system("shutdown /r /t 5")

            elif "enter in sleep mode" in self.query:
                os.system("rundll32.exe powrprof.dll, SetSuspendState 0,1,0")

            elif "no thanks" in self.query:
                self.speak("thank you for using me have a nice day")
                break

            elif "change speech rate" in self.query:
                self.speechrate()

            elif "check battery percentage" in self.query:
                import psutil
                battery=psutil.sensors_battery()
                percentage=battery.percent
                self.speak(f"our system is on {percentage} percent")

            elif "check internet speed" in self.query:
                import speedtest
                st=speedtest.Speedtest()
                dl=st.download()
                up=st.upload()
                self.speak(f"we have {dl} bit per second downloading speed and {up} bit per second uploading speed")

            elif "tell me the location" in self.query:
                self.speak("wait, let me check")
                try:
                    ipadd=requests.get('https://api.ipify.org').text
                    print(ipadd)
                    url='https://get.geojs.io/v1/ip/geo/'+ipadd+'.json'
                    geo_requests=requests.get(url)
                    geo_data=geo_requests.json()
                    city=geo_data['city']
                    country=geo_data['country']
                    self.speak(f"i m not sure but i think we are in {city} in {country}")
                except Exception as e:
                    self.speak("sorry due to network issues i m not able to find our location")
                    pass

            elif "read pdf" in self.query:
                self.pdf_reader()

            self.speak("Do u have any other work?")

    #greeting function
    def wish(self):
        hour = int(datetime.datetime.now().hour)
        if hour>=0 and hour<=12:
            self.speak("GUD MORNING")
        elif hour>12 and hour<18:
            self.speak("GUD AFTERNOON")
        else:
            self.speak("GUD EVENING")
        self.speak("HELLO MA'AM , HOW CAN I HELP YOU?")

    #to take input from user
    #uses SR
    def takecommand(self):
        r=SR.Recognizer()
        with SR.Microphone() as source:
            print("LISTENING..........")
            r.pause_threshold = 10
            audio=r.listen(source,timeout=10,phrase_time_limit=50)
        try:
            print("RECOGNIZING........")
            query=r.recognize_google(audio,language='en-US')
            print(f"user said: {query}")
        except Exception as e:
            self.speak("say that again please!!")
            self.tasks()
        return query

startExecution=MainThread()

class Main(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui=Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.startTask)
        self.ui.pushButton_2.clicked.connect(self.close)
    def showTime(self):
        currenttime=QTime.currentTime()
        currentdate=QDate.currentDate()
        label_time=currenttime.toString('hh:mm:ss')
        label_date=currentdate.toString(Qt.ISODate)
        self.ui.textBrowser.setText(label_date)
        self.ui.textBrowser_2.setText(label_time)
    def startTask(self):
        self.ui.movie=QtGui.QMovie("images/iron-man.gif")
        self.ui.label.setMovie(self.ui.movie)
        self.ui.movie.start()
        self.ui.movie=QtGui.QMovie("images/initiating.gif")
        self.ui.label_2.setMovie(self.ui.movie)
        self.ui.movie.start()
        timer=QTimer(self)
        timer.timeout.connect(self.showTime)
        timer.start(1000)
        startExecution.start()

class Form(QDialog):
    def __init__(self, parent=None):
        super(Form, self).__init__(parent)
        self.browser = QTextBrowser()
        self.setWindowTitle('Just a dialog')
        self.lineedit = QLineEdit("Write something and press Enter")
        self.lineedit.selectAll()
        layout = QVBoxLayout()
        layout.addWidget(self.browser)
        layout.addWidget(self.lineedit)
        self.setLayout(layout)
        self.lineedit.setFocus()

    def update_ui(self):
        self.browser.append(self.lineedit.text())

def SplashScreenShow(str):
    splash_pix = QPixmap(str)
    splash_pix=splash_pix.scaledToHeight(600)
    splash = QSplashScreen(splash_pix, QtCore.Qt.WindowStaysOnTopHint)
    splash.setMask(splash_pix.mask())
    splash.show()
    app.processEvents()
    time.sleep(2)
    form = Form()
    splash.finish(form)

app=QApplication(sys.argv)
import sys,time
#SplashScreenShow('images/tonystark.gif')
jarvis=Main()
jarvis.show()
sys.exit(app.exec_())  