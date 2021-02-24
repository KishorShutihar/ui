import tkinter as app
from tkinter import *
import os
import threading
from os import path
 
import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback

def getTextInput():
    result=content.get("1.0","end")
    print(result)

def clear():
    content.delete("1.0","end")

def playSound():
    filename = 'NP-0(2).wav'
    data, fs = sf.read(filename, dtype='float32')  
    sd.play(data, fs)
    status = sd.wait()  # Wait until file is done playing

obj = app.Tk()
obj.title('Recording GUI')
# obj.geometry('733x500')
obj.geometry('928x600')
# obj.minsize(700,200)
obj.maxsize(928,600)
# obj.configure(background="light blue")
obj['bg']="#d45f5f"

fvalue=StringVar()
fvalue.set("Filename.wav")

input_Label= Label(obj,font="Courier 16 bold",height=1,fg="Black",width=0,text="TEXT INPUT")
content = Text(obj,font="Courier 15 normal",height=5,fg="Black",width=61)
content.configure(background="light blue")
content.insert(INSERT,"Provide your input here")

title = Label(obj,font="Courier 20 bold",height=3,fg="White",width=58,text="TEXT TO SPEECH SYNTHESIS FOR REGIONAL LANGUAGES OF NEPAL")
title['bg']='#d45f5f'
title.pack(pady=10)
input_Label.pack()
input_Label['bg']='#d45f5f'

content.pack(pady=10)

button_frame = Frame(obj)
button_frame.pack(pady=40)
button_frame['bg']='#d45f5f'

generateBtn = Button(button_frame,command =lambda:getTextInput(),font='Arial 10 bold',text="Generate speech",fg='White',bg='Olive',height=2)
generateBtn.grid(row=0,column=1,padx=440)

clearBtn = Button(button_frame,command =lambda:clear(),font='Arial 10 bold',text="Clear",bg='Olive',fg='White',width=5,height=2)
clearBtn.grid(row=0,column=0,padx=100)

output_label= Label(obj,font="Courier 16 bold",height=1,fg="Black",width=0,text="SPEECH OUTPUT")
output_label.pack(pady=10)
output_label['bg']='#d45f5f'

filename_frame = Frame(obj)
filename_frame.pack(pady=0)
filename_frame['bg']='#d45f5f'

# filename_entry=Entry(filename_frame,font="Courier 20 normal",textvariable=fvalue,width=40,fg='Black')
filename_entry = Text(filename_frame,font="Courier 15 normal",height=1.4,fg="Black",width=30)
filename_entry.grid(row=0,column=2,padx=130)
filename_entry.configure(background='white')
filename_entry.insert(INSERT,"Filename.wav")

photo = PhotoImage(file = "/home/kishor/Desktop/ui/Desktop.png") 
photoimage = photo.subsample(7, 7) 
playBtn = Button(filename_frame,command =lambda:playSound(),image=photoimage,font="Arial 12 bold",bg='Maroon',fg='White')
playBtn.grid(row=0,column=3,padx=0)

obj.mainloop()


