from Tkinter import *
from os import system as sysc
import sys
import tkFont

master = Tk()

def keep_flat(event):       # on click,
    if event.widget is btn: # if the click came from the button
        event.widget.config(relief=FLAT) # enforce an option

arial36 = tkFont.Font(family='Lato-Regular',size=18)#, weight='bold')  
master.attributes('-fullscreen', True)
master.configure(background='#4D4D4D')

def sshd():
	keep_flat()
	sys('sudo systemctl disable ssh')

def sshe():
	keep_flat()
	sys('sudo systemctl enable ssh')

def smbd():
	keep_flat()
	sys('sudo systemctl disable samba')

def smbe():
	keep_flat()
	sys('sudo systemctl enable samba')

def quitApp():
	sys.exit(1)

ssh_e = Button(master, text="Enable SSH", font=arial36, command=sshd, height = 1, width = 50, fg='white', bg='#F1157F', relief=FLAT,highlightthickness=0,bd=0)
ssh_d = Button(master, text="Disable SSH",font=arial36, command=sshe, height = 1, width = 50, fg='white', bg='#F1157F', relief=FLAT,highlightthickness=0,bd=0)
smb_e = Button(master, text="Enable Samba", font=arial36, command=smbe, height = 1, width = 50, fg='white', bg='#F1157F', relief=FLAT,highlightthickness=0,bd=0)
smb_d = Button(master, text="Disable Samba", font=arial36, command=smbd, height = 1, width = 50, fg='white', bg='#F1157F', relief=FLAT,highlightthickness=0,bd=0)
quit = Button(master, text="Quit", font=arial36, command=quitApp, height = 1, width = 50, fg='white', bg='#F1157F', relief=FLAT,highlightthickness=0,bd=0)

ssh_e.pack(side=TOP, padx=5, pady=5)
ssh_d.pack(side=TOP, padx=5, pady=5)
smb_e.pack(side=TOP, padx=5, pady=5)
smb_d.pack(side=TOP, padx=5, pady=5)
quit.pack(side=TOP, padx=5, pady=5)

mainloop()