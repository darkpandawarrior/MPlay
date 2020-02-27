import os
from tkinter import *
from tkinter import filedialog
import tkinter.messagebox
from pygame import mixer


def abtmplay():
    tkinter.messagebox.showinfo('About Mplay', 'This is a music player built using Python Tkinter. \nCreated by Siddharth Pandalai')
def browsefile():
    global filename
    filename= filedialog.askopenfilename()

rt= Tk()
#Create Menu Bar
menubar= Menu(rt)
rt.config(menu= menubar)
#Create Submenu
submenu= Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "File", menu=submenu)
submenu.add_command(label= 'Open', command= browsefile)
submenu.add_command(label= 'Exit', command= rt.destroy)

submenu= Menu(menubar, tearoff= 0)
menubar.add_cascade(label= "Help", menu=submenu)
submenu.add_command(label= 'About MPlay', command= abtmplay)

mixer.init() #To initialize mixer
rt.title("MPlayer")
rt.iconbitmap(r'mplay.ico')
txt= Label(rt, text= 'Simple, fast and efficient Music Player')
txt.pack(pady=10)


def playmusic():
    global paused
    if paused :
        mixer.music.unpause()
        statusbar['text']= 'Now Playing: '+ os.path.basename(filename)
        paused = FALSE
    else:
        try:
           mixer.music.load(filename)
           mixer.music.play()
           statusbar['text']= 'Now Playing: '+ os.path.basename(filename)
        except:
           tkinter.messagebox.showerror('No File Loaded', 'Unable to play music till music file has been loaded' )


def stopmusic():
    mixer.music.stop()
    paused = FALSE
    statusbar['text']= 'Music Stopped. Last played: '+ os.path.basename(filename)
paused = FALSE

def pausemusic():
    global paused    
    paused= TRUE
    mixer.music.pause()
    statusbar['text']= 'Music Paused'

def setvol(val):
    volume= int(val)/100
    mixer.music.set_volume(volume) #set_volume only accepts values between 0 & 1

middleframe= Frame(rt)
middleframe.pack(padx=10, pady=10)
playpic= PhotoImage(file= 'play.png')
playbut= Button(middleframe, image= playpic, command= playmusic)
playbut.grid(row=0,column=0, padx=10)
pausepic= PhotoImage(file= 'pause.png')
pausebut= Button(middleframe, image= pausepic, command= pausemusic)
pausebut.grid(row=0,column=1, padx=10)
stoppic= PhotoImage(file= 'stop.png')
stopbut= Button(middleframe, image= stoppic, command= stopmusic)
stopbut.grid(row=0,column=2, padx=10)
volscale= Scale(rt, from_=0,to= 100, orient= HORIZONTAL, command= setvol)
volscale.set(25)
setvol(25)
volscale.pack(pady=15)
statusbar= Label(rt, text= 'Welcome to MPlay', relief= SUNKEN, anchor=W)
statusbar.pack(side= BOTTOM, fill= X)
rt.geometry("500x350")
rt.mainloop()