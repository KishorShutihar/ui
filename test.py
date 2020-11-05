import pandas as pd
import tkinter as app
from tkinter import *
from PIL import Image,ImageTk
import os

index=0
print(f"index outside: {index}")

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

file = "./metadata.csv"

print(os.path.join('/home/kishor/Desktop','tik.py'))

# csv file manipulationmanipulation
head = ['filename','content1','content2']
data = pd.read_csv(file,names=head,header=None,sep="|")
filenameList = data.filename.tolist()
contentList= data.content1.tolist()
count = len(filenameList)

# while(1):
fvalue=StringVar()
fvalue.set(filenameList[index])
cvalue=contentList[index]

# text
print(f"This is fvalue: {fvalue} and cvalue:{cvalue}")
filename= Entry(obj,font="Monospace 12 bold",textvariable=fvalue)
content = Text(obj,font="Monospace 12 bold",height=6)
content.insert(INSERT,f"{cvalue}")
nextbutton = Button(obj,command =lambda:press("next"),text="Next",fg='White',bg='Olive',width=5,height=2)
print('hello guys aha guys aha aha guys')
prevbutton = Button(obj,command =lambda:press("prev"),text="Prev",bg='Olive',fg='White',width=5,height=2)
nextbutton.pack()
prevbutton.pack()
filename.pack(side=TOP)
content.pack(fill=X)

# Scrollbar
scrollbar = Scrollbar(obj)

# Listbox
mylist = Listbox(obj, yscrollcommand = scrollbar.set )
for line in filenameList:
   mylist.insert(END, f"{line}")

obj.mainloop()

