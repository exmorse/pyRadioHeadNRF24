#!/usr/bin/python

import pyRadioHeadNRF24 as radio
import time

nrf24 = radio.nRF24()

nrf24.init()
nrf24.setChannel(1)
nrf24.setRF(1, 0)

print "StartUp Done!"
print "Receiving..."

while True:
	if nrf24.available():
	#if True:
		print "Available"
		(msg, l) = nrf24.recv()
		print "Receied: " + msg + " (" + str(l) + ")"

		msg = "AjStyles\0"
		nrf24.send(msg, len(msg))
		nrf24.waitPacketSent()

		time.sleep(1)
