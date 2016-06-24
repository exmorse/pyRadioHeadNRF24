#!/usr/bin/python

from cffi import FFI
import os

ffi = FFI()

buf = ffi.new("char*")
l = ffi.new("uint8_t*")
l[0] = 0
src = ffi.new("uint8_t*")
src[0] = 0

class nRF24:
	def __init__(self):

		ffi.cdef("int init();\
		  int setChannel(int c);\
	  	  int setRF(int dr, int tp);\
		  int send(uint8_t* data, uint8_t len);\
		  int waitPacketSent();\
	  	  int waitAvailableTimeout(int ms);\
	  	  int available();\
	  	  int recv(char* buf, uint8_t* len);\
	  	  int maxMessageLength();\
	  	  int isSending();\
	 	  int printRegisters();\
	  	  int setNetworkAddress(uint8_t* address, uint8_t len);\
	 	  int enterSleepMode();\
	  	  \
	  	  int managerInit(int address);\
	  	  int sendtoWait(uint8_t* data, uint8_t len, uint8_t dst);\
	  	  int recvfromAck(char* buf, uint8_t* len, uint8_t* form);\
	 	  int recvfromAckTimeout(char* buf, uint8_t* len, uint16_t timeout, uint8_t* form);\
	  	  int setTimeout(uint16_t timeout);\
		  int retries();\
	 	  int setRetries(uint8_t retries);\
	 	  int retransmissions();\
	  	  int resetRetransmissions();")
	
		global radiohead 
		#radiohead = ffi.dlopen("./libradiohead.so")
		path_string = os.path.dirname(__file__) + "/libradiohead.so"
		radiohead = ffi.dlopen(path_string)

    		
	def init(self):
		r = radiohead.init()
		if r != 0:
			raise RuntimeError("nRF24 init failed")

	def managerInit(self, address):
		radiohead.managerInit(address)

	def setChannel(self, channel):
		r = radiohead.setChannel(channel)
		if r != 0:
			raise RuntimeError("nRF24 setChannel failed")

	def setRF(self, datarate, transmitpower):
		r = radiohead.setRF(datarate, transmitpower)
		if r != 0:
			raise RuntimeError("nRF24 setRF failed")

	def send(self, data, l):
		r = radiohead.send(data, l)
		if r != 0:
			raise RuntimeError("nRF24 send failed")

	def waitPacketSent(self):
		radiohead.waitPacketSent()

	def waitAvailableTimeout(self):
		radiohead.waitAvailableTimeout()

	def available(self):
		b = radiohead.available()
		if (b == 1):
			return True
		else:
			return False
		

	def recv(self):
		radiohead.recv(buf, l)
		return (ffi.string(buf), l[0])

	def maxMessageLength(self):
		return radiohead.maxMessageLength()

	def isSending(self):
		b = radiohead.isSending()
		if b == 1:
			return True
		else:
			return False

	def printRegisters(self):
		radiohead.printRegisters()

	def setNetworkAddress(self, address, l):
		radiohead.setNetworkAddress(address, l)

	def sleep(self):
		radiohead.enterSleepMode()

	def recvfromAck(self):
		radiohead.recvfromAck(buf, l, src)
		return (ffi.string(buf), l[0], src[0])

	def recvfromAckTimeout(self, timeout):
		ris = radiohead.recvfromAck(buf, l, timeout, src)
		if ris > 0:
			return (ffi.string(buf), l[0], src[0])
		else:
			return ("", -1, -1)

	def sendtoWait(self, data, l, dst):
		return radiohead.sendtoWait(data, l, dst)

	def retries(self):
		return radiohead.retries()

	def setRetries(self, retries):
		radiohead.setRetries(retries)

	def retransmissions(self):
		return radiohead.retransmissions()

	def resetRetransmissions(self):
		radiohead.resetRetransmissions()

	def setTimeout(self, timeout):
		radiohead.setTimeout(timeout)
