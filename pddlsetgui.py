#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
import time
import getpass
import sys
import os
import tkinter as tk
from tkinter import StringVar

version = [1,0]

#define
HostType = "NEWPRODUCT"
pDDLType = "New"
pDDLTarg = "Air"

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


NetWorkID = "11101L249"

#######################################
#           Telnet process
#######################################
def TelnetProcess():
    tn = telnetlib.Telnet()
    tn.set_debuglevel(2)

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

    #write #01 set
    tn.write(b"at+mcct2=1024"+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("#01 set sucsses!");
        drawline();
    except:
        print("Error 201");
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

    #write RF mode set
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
    tn.write(b"at+mwnetworkid="+bytes(NetWorkID,encoding ="utf-8")+b"\n");
    time.sleep(2);
    try:
        command = tn.read_until(b"OK");
        print("network id set sucsses!");
        drawline();
    except:
        print("Error 401");
        return False


    #
    # Last move
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
#     windows class
#########################################
class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        label = tk.Label(self, fg="blue", width=30, height=2, text="Input NetWorkID below").pack()
        self.inputbox = tk.Entry(self)
        NetWorkID = StringVar()
        NetWorkID.set(b"11101L0001")
        self.inputbox.config(textvariable = NetWorkID)
        self.inputbox.pack()

        self.airset = tk.Button(self)
        self.airset["text"] = "set pddl air side"
        self.airset["command"] = self.telnetair
        self.airset.pack(side="top")

        self.grset = tk.Button(self)
        self.grset["text"] = "set pddl ground side"
        self.grset["command"] = self.telnetground
        self.grset.pack(side="top")
        
        self.quit = tk.Button(self, text="QUIT",
                              command=root.destroy)
        self.quit.pack(side="bottom")

    def telnetair(self):
        print("pddl")
        self.quit["state"] = "disable"
        print("Networkid:",self.inputbox.get())
        
    def telnetground(self):
        print("ap01")
        self.quit["state"] = "active"
    #enable all button after telnet work
    def enableall(self):
        self.quit["state"] = "active"
        self.airset["state"] = "active"
        self.grset["state"] = "active"
    #disable all button when telnet working...
    def disableall(self):
        self.quit["state"] = "disable"
        self.airset["state"] = "disable"
        self.grset["state"] = "disable"


###########################################
#       main process
###########################################
root = tk.Tk()
root.title("猞猁饲养指南") #title
root.geometry("320x280")
root.resizable(width=False, height=False)
app = Application(master=root)
app.mainloop()
