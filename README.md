pyRadioHeadNRF24
===============

Requirements:
---------
- bcm2835 (http://www.airspayce.com/mikem/bcm2835) 
- cffi (http://cffi.readthedocs.io/en/latest/index.html)


Compiling:
----------
Move to the main directory and run:

	make

Wirings:
----------
Refere to the standard RadioHead nRF24L01(+) wirings

(http://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html)

Writing programs using pyRadioHeadNRF24
---------------------------------------
- Import the module: ```import pyRadioHeadNRF24 as Radio```
- Initialize an instance of the ```nRF24``` class: ```nrf24 = Radio.nRF24()```

Running Examples:
-----------------
Once the package is compiled run:

	sudo ./server.py

or

	sudo ./reliable_datagram_server.py
