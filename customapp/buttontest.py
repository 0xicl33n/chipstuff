#!/usr/bin/env python2
#by b0nnie
from Tkinter import *
from os import system as sysc
import sys
import tkFont

BCHIP_BG = '#F1157F' # button background
BCHIP_FG = 'white' # button text
B_WIDTH = 10 # button width
B_HEIGHT = 1 # button height
WINDOW_BG = '#4D4D4D' # window background

master = Tk()

def keep_flat(event):    
    if event.widget is btn: 
        event.widget.config(relief=FLAT) 

ntcFont = tkFont.Font(family='Lato-Regular',size=18) # this is the font chip uses for its interface
master.attributes('-fullscreen', True)
master.configure(background='#4D4D4D')

def sshd():
	sysc('sudo systemctl stop ssh')

def sshe():
	sysc('sudo systemctl start ssh')

def smbd():
	sysc('sudo systemctl stop samba')

def smbe():
	sysc('sudo systemctl start samba')

def quitApp():
	sys.exit(1)

def pressed(self, index):
	Button.buttons[index].configure(bg="red")
ssh_e = Button(master, text="Start SSH", font=ntcFont, command=sshd, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
ssh_d = Button(master, text="Stop SSH",font=ntcFont, command=sshe, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
smb_e = Button(master, text="Start Samba", font=ntcFont, command=smbe, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
smb_d = Button(master, text="Stop Samba", font=ntcFont, command=smbd, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
quit = Button(master, text="Quit", font=ntcFont, command=quitApp, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)

ssh_e.pack(side=TOP, padx=5, pady=5)
ssh_d.pack(side=TOP, padx=5, pady=5)
smb_e.pack(side=TOP, padx=5, pady=5)
smb_d.pack(side=TOP, padx=5, pady=5)
quit.pack(side=TOP, padx=5, pady=5)

mainloop()