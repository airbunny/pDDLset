#!/usr/bin/python
# -*- coding: utf-8 -*-

import telnetlib
import time
import getpass
import sys
import os
#from __future__ import print_function

version = [1,0]

HOST = "bbs.newsmth.net"

#######################################
#  Welcome screen
#######################################
def WelcomeScreen():
    print"***********************************************"
    print"*     PowerEye communication system set       *"
    print"*       version %d.%d                        *"%(version[0],version[1])
    print"***********************************************"
    return


#######################################
#           Telnet connect
#######################################


#######################################
#           Telnet process
#######################################
def TelnetProcess():
    tn = telnetlib.Telnet()
    tn.set_debuglevel(2)

    print "Connecting..."

    try:
        tn.open(HOST)
        print "Connect!"
        res = True
    except:
        print "Can not link host"
        return False

    print"start reading..."

    try:
        print tn.read_some()
        print"gocha!"

        insert = input ("input login")
        tn.write(insert)
        print tn.read_some()
        
        insert = input ("input password")
        tn.write(insert)
        print tn.read_some()
    except:
        print"Got nothing"

    print "show time"
    time.sleep(5);
    print tn.read_some()

    return True


#######################################
#            main process
#######################################



WelcomeScreen();

TelnetProcess();

command = input("Press any key to exit...");
######################
#      End of file   #
######################
