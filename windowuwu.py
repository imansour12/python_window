# This will import all the widgets 
# and modules which are available in 
# tkinter and ttk module 
from tkinter import * 
from tkinter.ttk import *
from PIL import ImageTk,Image  
from tkinter import messagebox

# creates a Tk() object 
master = Tk() 
#sets icon to ball
master.iconbitmap("ball.ico")
# sets the geometry of main  
# root window 
master.geometry("400x400") 


#defines name 'window'
window = Tk()

  
  
# function to open a new window  
# on a button click 
def openNewWindow(): 
      
    # Toplevel object which will  
    # be treated as a new window 
    newWindow = Toplevel(master) 
  
    # sets the title of the 
    # Toplevel widget 
    newWindow.title("Wow, New window") 
  
    # sets the geometry of toplevel 
    newWindow.geometry("400x400") 
  
    # A Label widget to show in toplevel 
    Label(newWindow,  
          text ="Wow! Much window!").pack() 
    #shows ball
    canvas = Canvas(master, width = 300, height = 300)  
    canvas.pack()  
    img = ImageTk.PhotoImage(Image.open("ball.png"))  
    canvas.create_image(20, 20, anchor=NW, image=img) 
  
  
label = Label(master,  
              text ="This is stronk window") 
  
label.pack(pady = 10) 
  
# a button widget which will open a  
# new window on button click 
btn = Button(master,  
             text ="Much open",  
             command = openNewWindow) 
btn.pack(pady = 10) 


#Shows the click for ball part
def clicked():

    messagebox.showinfo('Click for ball', 'Ball')
    window.geometry('350x200')
btn = Button(window,text='Click here for ball', command=clicked)
btn.grid(column=0,row=0)



canvas = Canvas(master, width = 300, height = 300)  
canvas.pack()  
img = ImageTk.PhotoImage(Image.open("ball.png"))  
canvas.create_image(20, 20, anchor=NW, image=img) 



menubar = Menu(master)
filemenu = Menu(menubar)
filemenu.add_command(label="Much new")

# mainloop, runs infinitely 
mainloop() 