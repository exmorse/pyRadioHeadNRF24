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
pyRadioHeadNRF24 uses the standard RadioHead nRF24L01(+) wirings

      RasPi    pin            nRF24L01
      3.3V       2 ------------- VCC   (3.3V in)
    GPIO25      22 ------------- CE   (chip enable in)
    GPIO8       24 ------------- CSN   (chip select in)
    GPIO11      23 ------------- SCK   (SPI clock in)
    GPIO10      19 ------------- SDI/MOSI (SPI Data in)
    GPIO9       21 ------------- SDO/MISO (SPI data out)
                                 IRQ   (Interrupt output, not connected)
       GND       6 ------------- GND   (ground in)

(http://www.airspayce.com/mikem/arduino/RadioHead/classRH__NRF24.html)

Writing programs using pyRadioHeadNRF24
---------------------------------------
- Import the module: ```import pyRadioHeadNRF24 as Radio```
* If the program is in a different directory, the path to pyRadioHeadNRF24 need to be added to PYTONPATH
- Initialize an instance of the ```nRF24``` class: ```nrf24 = Radio.nRF24()```

Running Examples:
-----------------
Once the package is compiled run:

	sudo ./examples/server.py

or

	sudo ./examples/reliable_datagram_server.py
