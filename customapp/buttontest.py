from Tkinter import *
from os import system as sysc
import sys
import tkFont

master = Tk()


arial36 = tkFont.Font(family='Arial',size=18, weight='bold')  
master.attributes('-fullscreen', True,)
def sshd():
	sys('sudo systemctl disable ssh')

def sshe():
	sys('sudo systemctl enable ssh')

def smbd():
	sys('sudo systemctl disable samba')

def smbe():
	sys('sudo systemctl enable samba')

def quitApp():
	sys.exit(1)

ssh_e = Button(master, text="ENABLE SSH", font=arial36, command=sshd)#, height = 1, width = 3)
ssh_d = Button(master, text="DISABLE SSH",font=arial36, command=sshe)#, height = 1, width = 3)
smb_e = Button(master, text="ENABLE SAMBA", font=arial36, command=smbe)#, height = 1, width = 3)
smb_d = Button(master, text="DISABLE SAMBA", font=arial36, command=smbd)#, height = 1, width = 3)
quit = Button(master, text="QUIT", font=arial36, command=quitApp)#, height = 1, width = 3)

ssh_d.pack()
ssh_e.pack()
smb_d.pack()
smb_e.pack()
quit.pack()

mainloop()