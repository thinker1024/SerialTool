SerialTool Project 
=======================

overview
----
A small debug tool for serial port programming.

How to install
----
#sudo pip install SerialTool

usage
----
SerailTool com baudrate databits parity stopbits [tx data types] [rx data types]
    com: the serial port device name
    baudrate: any standard baudrate, such as 9600, 115200, etc.
    databits: 5,6,7,8
    parity: N,E
    stopbits: 1,1.5,2 
    tx data types: string or hex, default is string if this parameter is null.
    rx data types: string or hex, default is string if this parameter is null.

simple usage examples
----
#SerialTool /dev/ttyUSB0 115200 8 N 1

CONTACT
----
yangtao.now@gmail.com
