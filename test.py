"""
This file is for my test purpose only. Thank you :P
"""

import pandas as pd
import tkinter as app
from tkinter import *
# from tkinter import Text, Spinbox,INSERT,Scrollbar,Listbox,END,LEFT,RIGHT,BOTH,Y,TOP,Label,PhotoImage,Entry
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
   # filename.insert(INSERT,f"{fvalue}")
   # content.insert(INSERT,f"{cvalue}")

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
obj.configure(background="light blue")

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
filename= Entry(obj,font="Monospace 23 bold",textvariable=fvalue)
# filename.insert(INSERT,f"{fvalue}")
# content= Entry(obj,font="Monospace 12 bold",textvariable=cvalue)
content = Text(obj,font="Monospace 15 bold",height=6,fg="Black",width=0)
content.configure(background="light blue")
content.insert(INSERT,f"{cvalue}")
# content.insert(INSERT,f"{cvalue}")
_x=10
nextbutton = Button(obj,command =lambda:press("next"),text="Next",fg='White',bg='Olive',width=5,height=2)
prevbutton = Button(obj,command =lambda:press("prev"),text="Prev",bg='Olive',fg='White',width=5,height=2)

# nextbutton.place(rely=1.0, relx=1.0, x=-140+_x, y=-458, anchor=SE)
nextbutton.place(relx = 0.77, rely = 0.0875,anchor=SE)

# prevbutton.pack()

# prevbutton.place(rely=1.0, relx=1.0, x=-202+_x, y=-458, anchor=SE)
prevbutton.place(relx=0.685 ,rely=0.0875 , anchor=SE)

# filename.pack(side=TOP)

# filename.place(rely=1.0,relx=1.0,x=-255,y=-500,anchor=NE)
filename.place(relx=0.6,rely =0.0869,anchor=SE)

# content.pack(fill=X)

# content.place(rely=1.0,relx=1.0,x=233,y=-400,anchor=NE)
content.place(relx=0.008,rely=0.1,width=720)



# namebox = Spinbox(obj,values=filenameList,bg="Olive",font="Monospace 25 bold ")

# Scrollbar
scrollbar = Scrollbar(obj)
# scrollbar.pack( side = LEFT, fill = Y )

# Listbox
mylist = Listbox(obj, yscrollcommand = scrollbar.set )
for line in filenameList:
   mylist.insert(END, f"{line}")

# mylist.pack( side = LEFT, fill=BOTH)
# namebox.pack()

obj.mainloop()


# # image
# photo = PhotoImage(file="redsmoke.png")
# # using pillow
# image = Image.open("mario.jpg")
# image = image.resize((300,200))
# photo = ImageTk.PhotoImage(image)
# label = Label(obj,image=photo)
# label.pack()

