#!/usr/bin/python

from cffi import FFI
import time

ffi = FFI()

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

radiohead = ffi.dlopen("./libradiohead.so")

radiohead.managerInit(2);

print "StartUp Done!"

print "Receiving..."
buf = ffi.new("char*")
l = ffi.new("uint8_t*")
l[0] = 0
src = ffi.new("uint8_t*")
src[0] = 0
data = "Got It!"

while True:
	#if (radiohead.available()):
	if True:
		b = radiohead.recvfromAckTimeout(buf, l, 1000, src)
		buf_str = ffi.string(buf)
		print buf_str + " " + str(l[0]) + " (from " + str(src[0]) + ") " + str(b) 

		radiohead.sendtoWait(data, len(data), src[0])
		time.sleep(1)

#while True:
#	if (radiohead.available()):
#		b = radiohead.recv(buf, l)
#		buf_str = ffi.string(buf)
#		print buf_str + " " + str(l[0]) + " " + str(b) 
#		time.sleep(1)

#for i in range(0, 10):
#	msg = "AjStyles\0"
#	b = radiohead.send(msg, len(msg))
#	print "Send " + str(b)
#	b = radiohead.waitPacketSent()
#	print "WaitPacketSent " + str(b)
#	time.sleep(1)
