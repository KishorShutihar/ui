import pandas as pd
import tkinter as app
from tkinter import *
import os
import threading
from os import path
 
import argparse
import tempfile
import queue
import sys

import sounddevice as sd
import soundfile as sf
import numpy  # Make sure NumPy is loaded before it is used in the callback
assert numpy  # avoid "imported but unused" message (W0611)

index = 0
v=0

def delete():
    path='/home/kishor/Desktop/ui'
    filename= args.filename
    filenamelist=os.listdir(path)
    dict={}
    j=0
    for file in filenamelist:
        if (file[:-5:-1])[::-1]==".wav":
            if filename[:16] in file:
                j=int(file[-6:-7:-1])
                dict[j]=file
                j+=1

    maximum=max(dict.keys())

    for k in range(len(dict)-1):
        if k!=maximum:
            os.remove(os.path.join(path,dict[k]))


def press(key):
   global fvalue,cvalue,index,filenameList,contentList,args,v
   val=0
   if key=='next':
      index+=1
   else:
      index-=1
   clear()
   fvalue.set(filenameList[index])
   iindex.set(index)
   content.insert(INSERT,contentList[index])
   args.filename = f"{filenameList[index]}({val}).wav"
   v=0

def int_or_str(text):
    """Helper function for argument parsing."""
    try:
        return int(text)
    except ValueError:
        return text

def callback(indata, frames, time, status):
    """This is called (from a separate thread) for each audio block."""
    if status:
        print(status, file=sys.stderr)
    q.put(indata.copy())

class App():
    def __init__(self,master):
        self.isrecording = False
        self.button = app.Button(obj, text='rec',width=5,height=2,bg='maroon',fg='white')
        self.button.bind("<Button-1>", self.startrecording)
        self.button.bind("<ButtonRelease-1>", self.stoprecording)
        self.button.place(relx = 0.77+0.085+0.1, rely = 0.0875,anchor=SE)

    def stoprecording(self,event):
        self.isrecording = False
        print("Iam from stoprecording")
        print('\nRecording finished: ' + repr(args.filename))

    def _record(self):
        global args,v
        i=0
        if args.samplerate is None:
            device_info = sd.query_devices(args.device, 'input')
            # soundfile expects an int, sounddevice provides a float:
            args.samplerate = int(device_info['default_samplerate'])

        if args.filename is None:
            args.filename = f"{filenameList[index]}({v}).wav"

        if path.exists(f"{filenameList[index]}({v}).wav"):
            v+=1
            args.filename = f"{filenameList[index]}({v}).wav"


        # Make sure the file is opened before recording anything:
        with sf.SoundFile(args.filename, mode='x', samplerate=args.samplerate,
                        channels=args.channels, subtype=args.subtype) as file:
            with sd.InputStream(samplerate=args.samplerate, device=args.device,
                                channels=args.channels, callback=callback):
                while self.isrecording == True:
                    file.write(q.get())
                    i+=1
                    print(f"lets see {i}")

    def startrecording(self,event):
        self.isrecording = True
        t = threading.Thread(target=self._record)
        t.start()   

def clear():
   global fvalue,content
   print("I am from clear function")
   fvalue.set("")
   content.delete('1.0',END)

# Tkinter object
obj = app.Tk()
obj.title('Recording GUI')
obj.geometry('733x500')
obj.minsize(700,200)
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
iindex=IntVar()
iindex.set(index)
fvalue.set(filenameList[index])
cvalue=contentList[index]

######
parser = argparse.ArgumentParser(add_help=False)
parser.add_argument(
    '-l', '--list-devices', action='store_true',
    help='show list of audio devices and exit')
args, remaining = parser.parse_known_args()
if args.list_devices:
    print(sd.query_devices())
    parser.exit(0)
parser = argparse.ArgumentParser(
    description=__doc__,
    formatter_class=argparse.RawDescriptionHelpFormatter,
    parents=[parser])
parser.add_argument(
    'filename', nargs='?', metavar='FILENAME',
    help='audio file to store recording to')
parser.add_argument(
    '-d', '--device', type=int_or_str,
    help='input device (numeric ID or substring)')
parser.add_argument(
    '-r', '--samplerate', type=int, help='sampling rate')
parser.add_argument(
    '-c', '--channels', type=int, default=1, help='number of input channels')
parser.add_argument(
    '-t', '--subtype', type=str, help='sound file subtype (e.g. "PCM_24")')
args = parser.parse_args(remaining)
# args.filename=""

q = queue.Queue()

# text

print(f"This is fvalue: {fvalue} and cvalue:{cvalue}")
filename= Entry(obj,font="Monospace 12 bold",textvariable=fvalue)
indexnumber=Entry(obj,font="Monospace 20 bold",textvariable=iindex)
content = Text(obj,font="Monospace 15 bold",height=6,fg="Black",width=0)
content.configure(background="light blue")
content.insert(INSERT,f"{cvalue}")

nextbutton = Button(obj,command =lambda:press("next"),text="Next",fg='White',bg='Olive',width=5,height=2)
prevbutton = Button(obj,command =lambda:press("prev"),text="Prev",bg='Olive',fg='White',width=5,height=2)
deletebutton = Button(obj,command =lambda:delete(),text="Delete",bg='Orange',fg='Black',width=5,height=2)

deletebutton.place(relx=0.678,rely=0.0875, anchor=SE)
nextbutton.place(relx = 0.77+0.085, rely = 0.0875,anchor=SE)
prevbutton.place(relx=0.685+ 0.085,rely=0.0875 , anchor=SE)

filename.place(relx=0.65,rely =0.0869,anchor=SE)
content.place(relx=0.008,rely=0.1,width=720)
indexnumber.place(relx=1.9,rely=0.7,anchor=SE)
gui=App(obj)


obj.mainloop()


