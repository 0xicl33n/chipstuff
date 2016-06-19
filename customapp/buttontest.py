#!/usr/bin/env python2
#by b0nnie
from Tkinter import *
import sys
import tkFont
import subprocess

BCHIP_BG = '#F1157F' # button background
BCHIP_FG = 'white' # button text
B_WIDTH = 30 # button width
B_HEIGHT = 1 # button height
WINDOW_BG = '#4D4D4D' # window background

master = Tk()

def keep_flat(event):    
    if event.widget is btn: 
        event.widget.config(relief=FLAT) 

ntcFont = tkFont.Font(family='Lato-Regular',size=14) # this is the font chip uses for its interface
master.attributes('-fullscreen', True)
master.configure(background=WINDOW_BG)

class createButton():
	def __init__(self):
		self.data = []
		self.opts = 'height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0'
		self.text = ''
		self.cmd = ''
		self.clicky = Button(master,self.text,self.cmd,self.opts)

def runAcmd(cmd):
	subprocess.Popen(cmd,stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()


def quitApp():
	sys.exit(1)

def pressed(self, index):
	Button.buttons[index].configure(bg="red")



ssh_e = Button(master, text="Start SSH", font=ntcFont, command=runAcmd('sudo systemctl start ssh'), height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
ssh_d = Button(master, text="Stop SSH",font=ntcFont, command=runAcmd('sudo systemctl stop ssh'), height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
vnc_e = Button(master, text="Start VNC", font=ntcFont, command=runAcmd('sudo vncserver'), height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
vnc_d = Button(master, text="Stop VNC", font=ntcFont, command=runAcmd('sudo vncserver -kill :1'), height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)
quit = Button(master, text="Quit", font=ntcFont, command=quitApp, height = B_HEIGHT, width = B_WIDTH, fg=BCHIP_FG, bg=BCHIP_BG, relief=FLAT,highlightthickness=0,bd=0)



ssh_e.place(relx=0.5, rely=0.2, anchor=CENTER)
ssh_d.place(relx=0.5, rely=0.35, anchor=CENTER)
vnc_e.place(relx=0.5, rely=0.5, anchor=CENTER)
vnc_d.place(relx=0.5, rely=0.65, anchor=CENTER)
quit.place(relx=0.5, rely=0.8, anchor=CENTER)

mainloop()