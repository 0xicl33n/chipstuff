#!/usr/bin/env python2
#by b0nnie
from Tkinter import *
import sys
import tkFont
import subprocess

# Constants
# ------------------------------------------------------------------------------
WINDOW_BACKGROUND = '#4D4D4D'
NTC_FONT          = tkFont.Font(family='Lato-Regular',size=14)

# Class
# ------------------------------------------------------------------------------
class ntcStyleButton(Button):
    def __init__(self, window, buttonLabel, buttonCommand, yPosition):
        # Tkinter is an old style class (does not inherit from object), therefor
        Button.__init__(
                self,
                window,
                text               = buttonLabel,   # Button Label
                font               = NTC_FONT,      # Button Font
                command            = buttonCommand, # Button Command
                height             = 1,             # Button Height
                width              = 30,            # Button Width
                fg                 = '#FFFFFF',     # Button Foreground Color
                bg                 = '#F1157F',     # Button Background Color
                relief             = FLAT,
                highlightthickness = 0,
                bd                 = 0
                )
        self.place(relx=0.5, rely=yPosition, anchor=CENTER)

class shell:
    def __init__(self, cmd):
        self.cmd = cmd

    def __call__(self):
        subprocess.Popen(self.cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True).wait()


mainWindow = Tk()
mainWindow.attributes('-fullscreen', True)
mainWindow.configure(background=WINDOW_BACKGROUND)

ntcStyleButton(mainWindow, "Start SSH", shell('sudo systemctl start ssh'), 0.20 )
ntcStyleButton(mainWindow, "Stop SSH" , shell('sudo systemctl stop ssh') , 0.35 )
ntcStyleButton(mainWindow, "Start VNC", shell('sudo vncserver')          , 0.50 )
ntcStyleButton(mainWindow, "Stop VNC" , shell('sudo vncserver -kill :1') , 0.65 )
ntcStyleButton(mainWindow, "Quit"     , sys.exit                         , 0.80 )

mainloop()
