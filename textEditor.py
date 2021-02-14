from tkinter import Menu, Message, Widget
from tkinter.constants import END
from tk import *
import tkinter.filedialog

filename = None

def newFile():
    global filename
    filename = "Untitled"
    text.delete(0.0, END)


def saveFile():
    global filename
    t = text.get(0.0, END )
    f = open(filename, 'W')
    f.write(t)
    f.close()

def saveAs():
    f = asksaveasfile(mode='w', defaultextension='.txt')
    t = text.get(0.0, END)
    try:
        f.write(t.rstrip())
        except:  showerror(title="Oops!", Message="Unable to save file...")

def openFile():
    f = askopenfile(mode='r')
    t = f.reaf()
    text.delete(0.0, END)
    text.insert(0.0, t)

root = Tk()
root.title("My Python Text Editor")
root.minsize(width=400, height=400)
root.maxsize(width=400, height=400)


text = Text(root, width=400, height=400)
text.pack()

menubar = Menu(root)
filemenu = Menu(menubar)
filemenu.add_command(label="Much new", command=newFile)
filemenu.add_command(label="Much open", command=openFile)
filemenu.add_command(label="Much save", command=saveFile)
filemenu.add_command(label="Much save as", command=saveAs)
filemenu.add_separator()
filemenu.add_command(label="Wow, Quit", command=root.quit)

menubar.add_cascade(filemenu)

root.config(menu=menubar)

root.mainloop()