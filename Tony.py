#!/usr/bin/env python
# encoding: utf-8
# myRGB.py by Thomas Olson
#
# This test script connects to the RFduino, sends it RGB data and disconnects.
# Nothing fancy here. Just shell curses in a X terminal.

#import curses
import os
import sys

# Change ble_mac to your MAC address
ble_mac = "F3:DA:73:20:77:03"
#OR get it from the command line



redval=int(255)
greenval=int(128)
blueval=int(64)
RGB = hex(redval)[2:].zfill(2) + hex(greenval)[2:].zfill(2) + hex(blueval)[2:].zfill(2)
mycmd = "gatttool "
myarg = " -b " + ble_mac + " -t random --char-write --handle=0x0011 --value=" + RGB

#myarg = " -b " + ble_mac + "random --char-write --handle=0x0011 --value=" + RGB
os.system(mycmd + myarg)



