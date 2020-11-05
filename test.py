import tkinter as tk
from tkinter import *

root = tk.Tk()
text=Text(root)
content="hi"
c="bye"
text.insert(INSERT,content)
text.delete('1.0',END)
text.insert(INSERT,c)
text.pack()
root.mainloop()