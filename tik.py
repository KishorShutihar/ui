import pandas as pd
import tkinter as app
from tkinter import *
from PIL import Image,ImageTk
import os

index = 0
def press(key):
   global fvalue,cvalue,index,filenameList,contentList
   if key=='next':
      index+=1
   else:
      index-=1
   clear()
   fvalue.set(filenameList[index])
   content.insert(INSERT,contentList[index])

def clear():
   global fvalue,content
   print("I am from clear function")
   fvalue.set("")
   content.delete('1.0',END)

# Tkinter object
obj = app.Tk()
obj.title('Recording GUI')
obj.geometry('733x500')
obj.minsize(400,490)
obj.maxsize(733,500)
obj.configure(background="light blue")

file = "./metadata.csv"

# csv file manipulationmanipulation
head = ['filename','content1','content2']
data = pd.read_csv(file,names=head,header=None,sep="|")
filenameList = data.filename.tolist()
contentList= data.content1.tolist()
count = len(filenameList)

fvalue=StringVar()
fvalue.set(filenameList[index])
cvalue=contentList[index]

# text
print(f"This is fvalue: {fvalue} and cvalue:{cvalue}")
filename= Entry(obj,font="Monospace 23 bold",textvariable=fvalue)
content = Text(obj,font="Monospace 15 bold",height=6,fg="Black",width=0)
content.configure(background="light blue")
content.insert(INSERT,f"{cvalue}")

nextbutton = Button(obj,command =lambda:press("next"),text="Next",fg='White',bg='Olive',width=5,height=2)
prevbutton = Button(obj,command =lambda:press("prev"),text="Prev",bg='Olive',fg='White',width=5,height=2)

nextbutton.place(relx = 0.77, rely = 0.0875,anchor=SE)
prevbutton.place(relx=0.685 ,rely=0.0875 , anchor=SE)

filename.place(relx=0.6,rely =0.0869,anchor=SE)
content.place(relx=0.008,rely=0.1,width=720)

obj.mainloop()
