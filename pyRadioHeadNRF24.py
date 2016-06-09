#!/usr/bin/python

from cffi import FFI

ffi = FFI()
radiohead = ffi.dlopen("./libradiohead.so")

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

    		
	def init(self):
		radiohead.init();

	def managerInit(self, address):
		radiohead.managerInit(2);
