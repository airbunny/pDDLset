#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
import time
import getpass
import sys
import os
import threading
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
from tkinter import *

testvar =1101

def threadfun():

    
    while ThreadIsRun.isSet():
        time.sleep(1)
        print("testvar = %s"%testvar)

    return
def setvar(vars):
    global testvar
    
    testvar = vars

    return

#########################################
#     windows class
#########################################
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, fg="blue", width=30, height=2, text="Input NetWorkID below",justify="left").grid(row=0)
        self.inputbox = tk.Entry(self)
        self.inputbox.config(textvariable = "111001")
        self.inputbox.grid(row=1)

        self.showset = tk.Button(self)
        self.showset["text"] = "show set"
        self.showset["command"] = self.setmessagebox
        self.showset.grid(row=5,column=1)
        
        self.quit = tk.Button(self, text="QUIT",command=self.quitbox)
        self.quit.grid(row=3,column=1)
    
    def quitbox(self):
        ThreadIsRun.clear()
        root.destroy()

    def setmessagebox(self):
        global testvar
        testvar = self.inputbox.get()
        messagebox.showinfo("猞猁饲养指南","Network ID: %s"%(testvar))  

ThreadIsRun = threading.Event()
ThreadIsRun.set()
thread = threading.Thread(target=threadfun)
thread.start()

root = tk.Tk()
root.title("猞猁饲养指南") #title
root.geometry("640x280")
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()