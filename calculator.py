import speech_recognition as SR
from requests import get
import pyttsx3
engine=pyttsx3.init('sapi5')
voices=engine.getProperty('voices')

#you can change voice by the indexing
engine.setProperty('voices',voices[1].id)
def speak(audio):
        engine.say(audio)
        print(audio)
        engine.runAndWait()

def takecommand():
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
            speak("say that again please!!")
        return query
response=['Welcome to smart calculator','Thanks for using me ','Sorry ,this is  beyond my ability']
# fetching tokens from the text command
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
    speak(response[1])
    speak("Do u have any other work?")
    exit()
  
def sorry():
    speak(response[2])
    print(response[2])

def to_suffix( s):
        st = []
        ret = ''
        tokens = s.split()
        for tok in tokens:
            if tok in ['multiply', 'divide','MULTIPLY','DIVIDE','*','/']:
                while st and st[-1] in ['multiply', 'divide','MULTIPLY','DIVIDE','*','/']:
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
                # Operations - performed on the basis of text tokens
op={'ADD':add,'PLUS':add,'SUM':add,'ADDITION':add,
                            'SUB':sub,'SUBTRACT':sub, 'MINUS':sub,
                            'DIFFERENCE':sub,'LCM':lcm,'HCF':hcf,
                            'PRODUCT':mul, 'MULTIPLY':mul,'MULTIPLICATION':mul,
                            'DIVISION':div,'DIVIDE':div,'MOD':mod,'REMAINDER'
                            :mod,'MODULAS':mod,'+':add,'-':sub,'/':div,'*':mul,'add':add,'minus':sub,'divide':div,'multiply':mul}
 
                # commands
commands={'EXIT':end,'END':end,'CLOSE':end}
speak('--------------'+response[0]+'------------')
print('--------------'+response[0]+'------------')
while True:
    speak("tell me your query")
    expression=takecommand()
    if "end" or "close" in expression:
        break
    result=evaluate(expression)
    speak(result)