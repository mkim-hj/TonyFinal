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
import time

ParsePy.APPLICATION_ID = "nfVBFXHTVmVpMr5HHRWl0e3mFk2SDm1hOBoGATxp"
ParsePy.MASTER_KEY = "i5vvmxea6IBPYRIncjHImfdhoWwUSxYpvRnREx97"

Stark = "F3:DA:73:20:77:03"
IronMan = "ED:01:19:83:2D:F4"
Tony = "F3:FA:BE:3A:4B:96"

r = sr.Recognizer()
with sr.Microphone(0) as source:                # use the default microphone as the audio source
    audio = r.listen(source)                   # listen for the first phrase and extract it into audio data

prevTime = 0
currTime = 0

def setARGB(a, r, g, b):
	alpha = a
	redval = r
	greenval = g
	blueval = b

while (1):
	colorQuery = ParsePy.ParseQuery("ColorObject").limit(1).order("createdAt", decending=True)
	colorObject = colorQuery.fetch()[0]
	alpha = colorObject.alpha / 255.0
	redval=int(colorObject.red * alpha)
	greenval=int(colorObject.green * alpha)
	blueval=int(colorObject.blue * alpha)

	print redval, " ", greenval, " ", blueval

	RGB = hex(redval)[2:].zfill(2) + hex(greenval)[2:].zfill(2) + hex(blueval)[2:].zfill(2)
	mycmd = "gatttool "

	myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB
	# myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB
	# myarg = " -b " + Stark + " -t random --char-write --handle=0x0011 --value=" + RGB

	os.system(mycmd + myarg)

	# SPEECH RECOGNITION
	try:
		speech = r.recognize(audio)
		print("You said: " + speech)
		if "Tony" in speech:
			print "Activated..."
			if "light on" in speech:
				print "Turning On"
				setARGB(1, 220, 220, 220)
			elif "turn on the lights" in speech:
				print "Turning On"
				setARGB(1, 220, 220, 220)
			elif "light off" in speech:
				print "Turning Off"
				setARGB(0, 0, 0, 0)
			elif "turn off the lights" in speech:
				print "Turning Off"
				setARGB(0, 0, 0, 0)
			elif "dim" in speech:
				print "Dimming light"
				alpha = 127
			elif "dinner" in speech:
				print "It's time for dinner!"
				setARGB(1, 255, 220, 80)
		else:
			print("Please begin your phrase with 'Tony'")	
	except LookupError: 
		print("Could not understand audio")	