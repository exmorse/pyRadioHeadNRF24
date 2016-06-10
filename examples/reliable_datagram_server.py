#!/usr/bin/python

import sys, os

# Add path to pyRadioHeadNRF24 module
sys.path.append(os.path.dirname(__file__) + "/../")

import pyRadioHeadNRF24 as radio
import time

nrf24 = radio.nRF24()

nrf24.managerInit(2)

print "StartUp Done!"
print "Receiving..."

while True:
	if nrf24.available():
		print "Available"
		(msg, l, source) = nrf24.recvfromAck()
		print "Receied: " + msg + " (" + str(l) + ") from: " + str(source) 

		msg = "AjStyles\0"
		nrf24.sendtoWait(msg, len(msg), source)

		time.sleep(1)

