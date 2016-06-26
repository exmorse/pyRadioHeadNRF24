#include <stdio.h>
#include <signal.h>
#include <unistd.h>
#include <string.h>
#include <RH_NRF24.h>
#include <RHReliableDatagram.h>

RH_NRF24 radio(RPI_V2_GPIO_P1_22, RPI_V2_GPIO_P1_24);
RHReliableDatagram* manager = NULL;

int _init() {
        if (!bcm2835_init()) {
                printf("Startup Failed\n");
                return -1;
        }
        if (!radio.init()) {
		printf("Init Failed\n");
		return -1;
	}

	return 0;
}

int _setChannel(int c) {
	bool b = radio.setChannel(c);
	if (b) return 0;
	else return -1;
}

int _setRF(int dr, int tp) {

	RH_NRF24::DataRate datarate;
	RH_NRF24::TransmitPower transmitpower;
	
	/* Data Rate */
	switch (dr) {
		case 1:
			datarate = RH_NRF24::DataRate1Mbps;
			break;

		case 2:
			datarate = RH_NRF24::DataRate2Mbps;
			break;

		default:
			printf("Invalid Argument: DataRate\n");
			return -1;
	}

	/* Transmit Power */
	switch (tp) {
		case 18:
			transmitpower = RH_NRF24::TransmitPowerm18dBm;
			break;
	
		case 12:
			transmitpower = RH_NRF24::TransmitPowerm12dBm;
			break;
	
		case 6:
			transmitpower = RH_NRF24::TransmitPowerm6dBm;
			break;
	
		case 0:
			transmitpower = RH_NRF24::TransmitPower0dBm;
			break;
	
		default:
			printf("Invalid Argument: TransmitPower\n");
			return -1;
	}
	
	bool b = radio.setRF(datarate, transmitpower);
	if (b) return 0;
	else return -1; 
}

int _send(uint8_t* data, uint8_t len) {
	bool b = radio.send(data, len);
	if (b) return 0;
	else return -1;
}

int _waitPacketSent() {
	bool b = radio.waitPacketSent();
	if (b) return 0;
	else return -1;
}

int _waitAvailableTimeout(int ms) {
	return radio.waitAvailableTimeout(ms);
}

int _available() {
	/* If manager has been initialized use manager.available(), else radio.available() */
	/* Manager available */
	if (manager != NULL ) {
		return (int) manager->available();
	}
	
	/* Radio available */
	return (int) radio.available();
}

int _recv(char* buf, uint8_t* len) {
	uint8_t buf2[RH_NRF24_MAX_MESSAGE_LEN];
	uint8_t len2 = sizeof(buf2);
	
	bool b = radio.recv(buf2, &len2);
	//printf("Received : %s (%d)\n", (char*)buf2, len2);

	strcpy(buf, (char*)buf2);
	//buf[(int)len2] = 0;
	*len = len2; 	

	if (b) return *len;
	else return -1;
}

int _maxMessageLength() {
	return radio.maxMessageLength();
}

int _setNetworkAddress(uint8_t* address, uint8_t len) {
	bool b = radio.setNetworkAddress(address, len);
	if (b) return 0;
	else return -1;
}

int _isSending() {
	return (int) radio.isSending();
}

int _printRegisters() {
	bool b = radio.printRegisters();
	if (b) return 0;
	else return -1;
}

int _enterSleepMode() {
	bool b = radio.sleep();
	if (b) return 0;
	else return -1;
}

int _managerInit(int address) {
	manager = new RHReliableDatagram(radio, (uint8_t)address); 
        
	if (!bcm2835_init()) {
                printf("Startup Failed\n");
                return -1;
        }
	
	if (!manager->init())
                printf("Init Failed\n");
}

int _recvfromAck(char* buf, uint8_t* len, uint8_t* from) {
	uint8_t buf2[RH_NRF24_MAX_MESSAGE_LEN];
	uint8_t len2 = sizeof(buf2);
	uint8_t from2;
		
	bool b = manager->recvfromAck(buf2, &len2, &from2);
	//printf("Received : %s (%d) (from %d)\n", (char*)buf2, len2, from2);
	strcpy(buf, (char*)buf2);
	*len = len2; 	
	*from = from2;

	if (b) return *len;
	else return -1;
}

int _recvfromAckTimeout(char* buf, uint8_t* len, uint16_t timeout, uint8_t* from) {
	uint8_t buf2[RH_NRF24_MAX_MESSAGE_LEN];
	uint8_t len2 = sizeof(buf2);
	uint8_t from2;

	bool b = manager->recvfromAckTimeout(buf2, &len2, timeout, &from2);

	if (b) {
		//printf("Received : %s (%d) (from %d)\n", (char*)buf2, len2, from2);
		strcpy(buf, (char*)buf2);
		*len = len2; 	
		*from = from2;
		return *len;
	}

	else {
		printf("Timeout Expired\n");
		return 0;
	}
}	

int _sendtoWait(uint8_t* data, uint8_t len, uint8_t dst) {
	bool b = manager->sendtoWait(data, len, dst);
	if (b) return 0;
	else return -1;
}

int _setTimeout(uint16_t timeout) {
	manager->setTimeout(timeout);
	return 0;
}

int _setRetries(uint8_t retries) {
	manager->setRetries(retries);
	return 0;
}

int _retries() {
	return (int) manager->retries();
}

int _retransmissions() {
	return (int) manager->retransmissions();
}

int _resetRetransmissions() {
	manager->resetRetransmissions();
	return 0;
}

extern "C" {
        extern int init() {
                return _init();
        }
	
	extern int setChannel(int c) {
		return _setChannel(c);
	}

	extern int setRF(int dr, int tp) {
		return _setRF(dr, tp);
	}

	extern int send(uint8_t* data, uint8_t len) {
		return _send(data, len);
	}

	extern int waitPacketSent() {
		return _waitPacketSent();
	}

	extern int waitAvailableTimeout(int ms) {
		return _waitAvailableTimeout(ms);
	}

	extern int available() {
		return _available();
	}

	extern int recv(char* buf, uint8_t* len) {
		return _recv(buf, len);
	}

	extern int maxMessageLength() {
		return _maxMessageLength();
	}

	extern int isSending() {
		return _isSending();
	}

	extern int printRegisters() {
		return _printRegisters();
	}

	extern int setNetworkAddress(uint8_t* address, uint8_t len) {
		return _setNetworkAddress(address, len);
	}

	extern int enterSleepMode() {
		return _enterSleepMode();
	}

	extern int managerInit(int address) {		
		return _managerInit(address);
	}

	extern int recvfromAck(char* buf, uint8_t* len, uint8_t* from) {
		return _recvfromAck(buf, len, from);
	}

	extern int recvfromAckTimeout(char* buf, uint8_t* len, uint16_t timeout, uint8_t* from) {
		return _recvfromAckTimeout(buf, len, timeout, from);
	}

	extern int sendtoWait(uint8_t* data, uint8_t len, uint8_t dst) {
		return _sendtoWait(data, len, dst);
	}

	extern int retries() {
		return _retries();
	}

	extern int setRetries(uint8_t retries) {
		return _setRetries(retries);
	}

	extern int retransmissions() {
		return _retransmissions();
	}

	extern int resetRetransmissions() {
		return _resetRetransmissions();
	}

	extern int setTimeout(uint16_t timeout) {
		return _setTimeout(timeout);
	}
}
