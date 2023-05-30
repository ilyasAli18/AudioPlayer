from datetime import datetime
import os, psutil,sys
from platform import system
system = system()

dic = { "046":"Ahqaf",
       "020":"Taha",
       "042": "As-Shura",
       "017":"Isra",
       "045":"Jathiya",
       "016":"Nahl",
       "013":"Ra'ad",
       "112":"Ikhlas"
        }
# Check whether an audio is already running.
def checkIfAudioIsRunning():
   processes = psutil.process_iter()
   for proc in processes:
      if proc.name() == "afplay" and proc.is_running():
         return True
   return False


def play():
   counter = 1; global dic; lst = []; T = "Do You To Play Audio? (Y/n): "
   print(T,end="")
   inp = input();
   while inp[0].lower() == "y":
      if inp[0].lower() == "n":
           break
      hours = datetime.now().strftime("%H:%M:%S")
      print(hours+":","Select the audio you want to play from the list below (Choose numbers)")
      for i in dic:
         print("\t",i,dic[i])
      file = input(); lst.append(file)
      if file in dic:
         if lst[0] == file:
            counter += 1
         else:
            lst = []
            counter = 1
         hours = datetime.now().strftime("%H:%M:%S")
         print(hours+":", "Playing",dic[file],"("+str(counter)+" time.)")
         if system=="Darwin":
            os.system("afplay audios/"+file+".mp3")
            os.system("open -a /System/Applications/Utilities/Terminal.app")
         """
          -------------------------
          MAY NOT WORK FOR WINDOWS
          ------------------------
          elif system == "Window":
             import windsound
             winsound.playSound("audios/"+file+".mp3",winsound.SND_FILENAME)
         """     
         hrs = datetime.now().strftime("%H:%M:%S")
         print("Time it took to play",dic[file]+":",calculateTime(hrs,hours)+".")
         print(hrs+": ----------------------------")
         hours = datetime.now().strftime("%H:%M:%S")
         print(hours+":",T,end="")
         inp = input()
      else:
         hours = datetime.now().strftime("%H:%M:%S")
         print(hours+":","Unknown audio! Try pick from the list below or type N to exit. ",end="")

#Calculates time taken since the start
def calculateTime(a,b):
   (fh,fm,fs) = a.split(":")
   (sh,sm,ss) = b.split(":")
   fh = (int(fh)-int(sh)) %24
   fm = (int(fm)-int(sm)) %60
   fss = (int(fs)-int(ss)) %60
   final = [str(fh),str(fm),str(fss)]
   if (int(final[2])+int(ss))%60==int(fs) and int(fm)== 1 :
      return ("0:0:"+final[2])
   return ":".join(final)

def main():
   
   if not checkIfAudioIsRunning():
      play()
   else:
      print("-"*50)
      print("An audio is already running. Try again once the audio has finished or press ctrl + C to quit!".upper())
      print("-"*50,"\n")
      sys.exit()
main()
