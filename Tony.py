#!/usr/bin/env python
# encoding: utf-8
# myRGB.py by Thomas Olson
#
# This test script connects to the RFduino, sends it RGB data and disconnects.
# Nothing fancy here. Just shell curses in a X terminal.

#import curses
import os
import sys
import ParsePy
import speech_recognition as sr

ParsePy.APPLICATION_ID = "nfVBFXHTVmVpMr5HHRWl0e3mFk2SDm1hOBoGATxp"
ParsePy.MASTER_KEY = "i5vvmxea6IBPYRIncjHImfdhoWwUSxYpvRnREx97"

Stark = "F3:DA:73:20:77:03"
IronMan = "ED:01:19:83:2D:F4"
Tony = "F3:FA:BE:3A:4B:96"

lastred = 0
lastblue = 0
lastgreen = 0
lastalpha = 0
while (1):
	try:
		os.system("sudo hciconfig hci0 up")
		colorQuery = ParsePy.ParseQuery("ColorObject").limit(1).order("createdAt", decending=True)
		colorObject = colorQuery.fetch()[0]
		alpha = colorObject.alpha / 255.0
		redval=int(colorObject.red * alpha)
		greenval=int(colorObject.green * alpha)
		blueval=int(colorObject.blue * alpha)

		print redval, " ", greenval, " ", blueval
		if (lastred == redval and lastgreen == greenval and lastblue==blueval and lastalpha == alpha):
			pass
		RGB = hex(redval)[2:].zfill(2) + hex(greenval)[2:].zfill(2) + hex(blueval)[2:].zfill(2)
		mycmd = "gatttool "
		
		myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB
		# myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB
		# myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB

		os.system(mycmd + myarg)
		lastred = redval
		lastgreen = greenval
		lastblue = blueval
		lastalpha = alpha
	except:
		pass



