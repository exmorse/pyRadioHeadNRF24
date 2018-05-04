#!/usr/bin/python

import sys, os

# Add path to pyRadioHeadNRF24 module
sys.path.append(os.path.dirname(__file__) + "/../")

import pyRadioHeadNRF24 as radio
import time

nrf24 = radio.nRF24()

nrf24.init()
nrf24.setChannel(1)
nrf24.setRF(radio.nRF24.DataRate2Mbps, radio.nRF24.TransmitPower0dBm)

print "StartUp Done!"
print "Receiving..."

while True:
	if nrf24.available():
	#if True:
		print "Available"
		(msg, l) = nrf24.recv()
		print "Received: " + msg + " (" + str(l) + ")"

		msg = "Hello\0"
		nrf24.send(msg, len(msg))
		nrf24.waitPacketSent()

		time.sleep(1)

