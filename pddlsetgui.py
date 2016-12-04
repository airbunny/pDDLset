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

version = [1,0]

#define
HostType = "NEWPRODUCT"
pDDLType = "New"
pDDLTarg = "Air"
OldFarmware = False

username = b"admin"
oldpass = b"admin"
newpass = b"123456"
otherpass = b"admin123"

#
if HostType == "Air":
    HOST = "192.168.1.12"
elif HostType == "Ground":
    HOST = "192.168.1.11"
else:
    HOST = "192.168.168.1"

if pDDLType == "New":
    PASSWORD = oldpass
elif pDDLType == "Old":
    PASSWORD = newpass
elif pDDLType =="AP01":
    PASSWORD = otherpass

#default Network ID
NetWorkID = "11101L0001"
#Var = IntVar()

#######################################
#           Telnet process
#######################################
def TelnetProcess(NWID):
    tn = telnetlib.Telnet()
    tn.set_debuglevel(2)

    print ("Setting NetWorkID %s   password as %s    HOST as %s Tag as %s"%(NWID,PASSWORD,HOST,pDDLTarg));
    print ("Connecting...");

    #
    #  Connect telnet
    #
    try:
        tn.open(HOST)
        print ("Connected!");
        res = True
    except:
        print ("Can not link host");
        tn.close();
        app.enableall();
        return False

    print("start reading...");
    time.sleep(5);

    #
    #   input username
    #
    try:
        print(tn.read_until(b"login"));
        time.sleep(2);
        tn.write(b"admin"+b"\n");
        print("username input passed");
    except:
        print("can not input username!");
        tn.close();
        return False

    #
    #   input password
    #
    time.sleep(2);
    print("password inputing...");
    try:
        print(tn.read_some());
        time.sleep(2);
        tn.write(PASSWORD+b"\n");
        print("password input passed");
    except:
        print("can not input password");
        tn.close();
        return False

    #
    # comfirm login
    #
    time.sleep(5);
    try:
        command = tn.read_until(b"evice>");
        print(command);
        drawline();
    except:
        print("poland can not into space");
        return False

    #
    #  login sucsses and input network id
    #
    print("  ");
    print("  ");
    drawline();
    print("login sucsses!!!");
    print("  ");
    print("  ");
    print("  ");
    print("****************************************************");
    print("Now writing command.....");
    print("   ");

    #
    #   writing setup data
    #

    #write wan bright
    tn.write(b"at+mnwan"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("wan bright set sucsses!");
        drawline();
    except:
        print("Error 101");
        return False

    #write wan set
    tn.write(b"at+mnwan=1"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("wan set sucsses!");
        drawline();
    except:
        print("Error 102");
        return False

    #write lan set
    tn.write(b"at+mcps2=1"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("lan set sucsses!");
        drawline();
    except:
        print("Error 103");
        return False

    #write some set
    tn.write(b"at+mcbr2=13"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("some set sucsses!");
        drawline();
    except:
        print("Error 105");
        return False

    #write whatever set
    tn.write(b"at+mcdf2=0"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("whatever set sucsses!");
        drawline();
    except:
        print("Error 106");
        return False

    #write somehow set
    tn.write(b"at+mcdm2=0"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("somehow set sucsses!");
        drawline();
    except:
        print("Error 109");
        return False

    #write Seria timeout set
    tn.write(b"at+mcct2=60"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("#01 set sucsses!");
        drawline();
    except:
        print("Error 201");
        return False

    #write Seria packae size set
    tn.write(b"at+mcmps2=1024"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("Seria packae size set sucsses!");
        drawline();
    except:
        print("Error 961");
        return False

    #write #02 set
    tn.write(b"at+mcipm2=2"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("#02 set sucsses!");
        drawline();
    except:
        print("Error 204");
        return False

    #write seria target set
    if pDDLTarg == "Air":
        tn.write(b"at+mctcs2=192.168.1.11,20002,60,0,10,20002,300"+b"\n");
    elif pDDLTarg == "Ground":
        tn.write(b"at+mctcs2=192.168.1.12,20002,60,0,10,20002,300"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("seria target set sucsses!");
        drawline();
    except:
        print("Error 209");
        return False

    #write seria band set
    tn.write(b"at+mwband=0"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("seria band set sucsses!");
        drawline();
    except:
        print("Error 211");
        return False

    #write RF frequse set
    tn.write(b"at+mwfreq=76"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("RF freqnse set sucsses!");
        drawline();
    except:
        print("Error 233");
        return False

    #write RF txpower set
    tn.write(b"at+mwtxpower=28"+b"\n");#paramenter 28 used in new firmware
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("RF txpower set sucsses!");
        drawline();
    except:
        print("Error 666");
        return False

    #write RF mode set
    if pDDLTarg == "Ground":
        tn.write(b"at+mwvmode=1"+b"\n");
    elif pDDLTarg == "Air":
        tn.write(b"at+mwvmode=0"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("RF mode set sucsses!");
        drawline();
    except:
        print("Error sm");
        return False

    #write lan basic set
    if pDDLTarg == "Ground":
        tn.write(b"at+mnlan=lan,EDIT,0,192.168.1.11,255.255.255.0"+b"\n");
    elif pDDLTarg == "Air":
        tn.write(b"at+mnlan=lan,EDIT,0,192.168.1.12,255.255.255.0"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("lan basic set sucsses!");
        drawline();
    except:
        print("Error lan");
        return False
        
    #write network id.....
    tn.write(b"at+mwnetworkid="+bytes(NWID,encoding ="utf-8")+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("network id set sucsses!");
        drawline();
    except:
        print("Error 401");
        return False
    
    #write new password set
    tn.write(b"at+mspwd=123456,123456"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("new password set sucsses!");
        drawline();
    except:
        print("Error 609");
        return False

    #
    # final move
    #

    #Enable all set
    tn.write(b"at&W"+b"\n");
    drawline();
    print("now solid all seting...");
    print(".");
    print(".");
    print(".");
    print(".");
    print(".");
    print(".");
    time.sleep(8);
    try:
        command = tn.read_until(b"recently");
        print("All set had been writen in pDDL!");
        drawline();
    except:
        print("Failed to solid seting!");

        return False

    #exit command interface
    time.sleep(2)
    tn.write(b"ata");
    #close telnet
    time.sleep(6)
    tn.close()

    print("pDDL setup sucsses!");
    print("****************************************************");
    print("   ");
    
    return True
#########################################
#     thread function
#########################################
def threadfun():
    #
    while ThreadIsRun.isSet():
        time.sleep(1)
        if TelnetRun.isSet():
            TelnetProcess(NetWorkID)
            print("Net = %s"%NetWorkID)
            TelnetRun.clear()
            print("Telnet exit...")
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
        textid = StringVar()
        textid.set(b"11101L0001")
        self.inputbox.config(textvariable = textid)
        self.inputbox.grid(row=1)

        self.airset = tk.Button(self)
        self.airset["text"] = "set pddl air side"
        self.airset["command"] = self.telnetair
        self.airset.grid(row=1,column=1)

        self.grset = tk.Button(self)
        self.grset["text"] = "set pddl ground side"
        self.grset["command"] = self.telnetground
        self.grset.grid(row=2,column=1)
        self.showset = tk.Button(self)
        self.showset["text"] = "show set"
        self.showset["command"] = self.setmessagebox
        self.showset.grid(row=3,column=1)

        self.quit = tk.Button(self, text="QUIT",
                              command=self.quitbox)
        self.quit.grid(row=4,column=1)

       
        self.checkb = tk.Checkbutton(text = "使用旧固件")
        self.checkb.pack()
    
    def quitbox(self):
        #ThreadIsRun = False
        ThreadIsRun.clear()
        root.destroy()

    #set pddl as airside
    def telnetair(self):
        #when telnet client is working disable all button to keeping safe 
        self.disableall()
        #set paraments to air side
        global NetWorkID
        global pDDLTarg
        global HOST
        global PASSWORD
        PASSWORD = oldpass
        pDDLTarg = "Air"
        HOST = "192.168.168.1"
        NetWorkID = self.inputbox.get()
        #and just start working...
        TelnetRun.set()
        #enable button after working

    #set pddl as groundside
    def telnetground(self):
        #when telnet client is working disable all button to keeping safe 
        self.disableall()
        #set paraments to air side
        global NetWorkID
        global pDDLTarg
        global HOST
        global PASSWORD
        PASSWORD = otherpass
        pDDLTarg = "Ground"
        HOST = "192.168.1.11"
        NetWorkID = self.inputbox.get()
        #and just start working...
        TelnetRun.set()
        #enable button after working

    #enable all button after telnet work
    def enableall(self):
        self.airset["state"] = "active"
        self.grset["state"] = "active"
    #disable all button when telnet working...
    def disableall(self):
        self.airset["state"] = "disable"
        self.grset["state"] = "disable"

    def setmessagebox(self):
        global NetWorkID
        global OldFarmware
        NetWorkID = self.inputbox.get()
        OldFarmware = self.checkb.getvar()
        messagebox.showinfo("猞猁饲养指南","Password:%s  IP:%s  Network ID: %s   Use old Firmware: %s"%(PASSWORD,HOST,NetWorkID,OldFirmware)) 

        TelnetRun.clear()   


###########################################
#       main process
###########################################

# 条件变量
ThreadIsRun = threading.Event()
TelnetRun = threading.Event()
ThreadIsRun.set()
TelnetRun.clear()
thread = threading.Thread(target=threadfun)
thread.start()

root = tk.Tk()
root.title("猞猁饲养指南") #title
root.geometry("380x220")
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
