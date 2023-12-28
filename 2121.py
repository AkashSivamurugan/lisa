import speech_recognition as sr
import webbrowser as web 
import wikipedia 
import pyjokes 
from googlesearch import search
import pyttsx3 
import sys,time
import datetime

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


converter = pyttsx3.init() 
converter.setProperty('rate', 120) 
converter.setProperty('volume', 1.0) 
voice = converter.getProperty('voices')
converter.setProperty('voice', voice[1].id)


engine = pyttsx3.init()
engine.setProperty('rate', 190)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 1)


def wishme():
    
    speak("Welcome Back")
    hour = datetime.datetime.now().hour
    if (hour >= 6 and hour < 12):
        speak("Good Morning sir!")
    elif (hour >= 12 and hour < 18):
        speak("Good afternoon sir")
    elif (hour >= 18 and hour < 24):
        speak("Good Evening sir")
    else:
        speak("Goodnight sir")

    speak("Lisa at your service, Initializing the Services?")

wishme()
def delprint(text="Hello, I am Your Virtual Assistant.",delay_time=.09): 
  
  for character in text:      
    sys.stdout.write(character) 
    sys.stdout.flush()
    time.sleep(delay_time)
converter.say("Hello, I am your Virtual Assistant......") 
converter.runAndWait() 
delprint()

                                
r = sr.Recognizer()
tl=["tell","say","answer","text","search","what","write"] 
for i in range(0,len(tl)):
      pass



def start():     
                                            
    with sr.Microphone() as source:
        converter.setProperty('voice', voice[1].id)
        converter.say("Authentication Required") 
        converter.runAndWait() 
        
        print("\nAuthentication Required....!!!")



        
       

                                                                                       
        audio = r.listen(source)
        b= r.recognize_google(audio)
        
        

 
    
        if("admin"in b):
         
            converter.setProperty('voice', voice[1].id)
            converter.say("The session was invoked for you as admin") 
            print("The session was invoked for you as Admin...!")
            converter.runAndWait() 
            print("Recogonizing Your voice....")
            converter.say("Recogonizing Your voice") 
            converter.runAndWait()
            if("baby" or "babe" in b):
                print("Yaa...I'm Ready Akash")
                converter.setProperty('voice', voice[1].id)
                converter.say("yaa i am ready akash") 
                converter.runAndWait() 
                main()
            else:
                print("Other User")
                main()
           
            
        else:
             
             print("\nDoesn't Contain Key/Root Word")
             converter.setProperty('voice', voice[1].id)
             converter.say("Doesn't Contain Key or Root Word") 
             converter.runAndWait()
                    
def main():
    with sr.Microphone() as source:
            print("\nKindly voice out your command!")
            converter.say("Kindly voice out your command!")  
            converter.runAndWait()
            audio = r.listen(source)
            a= r.recognize_google(audio)

                     
        
                    
            try:
                print("\nDid You Say: " + r.recognize_google(audio))
    
                print("\nWorking For You...")
     
                query = r.recognize_google(audio)
         
                        
           
            
                if("joke" in a ):
                 
                            My_joke = pyjokes.get_joke(language="en", category="all") 

                            print(My_joke) 
                            main()
                elif(tl[i] in a):
                       result = wikipedia.summary(r.recognize_google(audio), sentences = 5) 
                       print(result)
                       main()
            
                elif("play" or "open" in a):
                            query = r.recognize_google(audio)
                            for j in search(query, tld="co.in", num=1, stop=1,pause=2):
                                print(j)
                                web.open(j)
                                main()
               
                else:
                            result = wikipedia.summary(r.recognize_google(audio), sentences = 5) 
                            print(result)
                            main()
            except wikipedia.exceptions.PageError as e:
                        print("\nAsk Something Better...!")
                        main()
       
              
                

       
          
   
    
    
  



while(True):
    if __name__=="__main__": 
     start()
    
     
  