#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tao Yang"

import serial
import time
import sys
import readline
import os

print ("\r\nA small debug tool for serial port programming.")
print ("-----------------\r\n")
# The serial port configuration
def HexShow(argv):
    result = ''
    xLen = len(argv)
    for i in xrange(xLen):
        temp = ord(argv[i])
        hhex = '%02x'%temp
        result += hhex+''
    return result

def PrintHelp():
    print ("usage:")
    print ("SerialTool [-s] com baudrate databits parity stopbits [TX data type] [RX data type]")
    print ("|_-s: save the current port configuration as default option")
    print ("|_com: the serial port device name")
    print ("|_baudrate: any standard baudrate, such as 9600, 115200, etc")
    print ("|_databits: 5,6,7,8")
    print ("|_parity: N,E")
    print ("|_stopbits: 1,1.5,2")
    print ("|_TX data types: string or hex, default is string if this parameter is null")
    print ("|_RX data types: string or hex, default is string if this parameter is null")
    print ("\r\nsimple usage example:")
    print ("====\r\n")
    print ("SerialTool /dev/ttyUSB0 115200 8 N 1 hex hex")
    print ("\r\nCONTACT")
    print ("====\r\n")
    print ("Project main page: https://pypi.python.org/pypi/SerialTool")


def main():
    ser = serial.Serial()
    if len(sys.argv) < 6 and os.path.isfile('/.SerialTool.conf') == False:
        PrintHelp()
        exit()
    elif len(sys.argv) > 1 and len(sys.argv) < 6 :
        PrintHelp()
        exit()
    print ("Port Info:")
    if os.path.isfile('/.SerialTool.conf') and len(sys.argv) == 1:
        with open('/.SerialTool.conf', 'r') as fp:
            x = fp.readlines()
            param = []
            for lines in x :
                lines = lines.replace("\r\n","").split(",")
                param.extend(lines)

            ser = serial.Serial(
                port = param[0],
                baudrate = param[1],
                bytesize = int(param[2]),
                parity = param[3],
                stopbits = int(param[4]),
                timeout = 0.5,
                xonxoff = None,
                rtscts = None,
                interCharTimeout = None
                )
            for i in param:
                print (i)

    elif len(sys.argv) > 6 and sys.argv[1] == '-s' :
        config = sys.argv[2:9]
        with open("/.SerialTool.conf", "w") as fp:
            for i in config :
                print (i)
                fp.write(i)
                fp.write('\r\n')
            ser = serial.Serial(
                    port = sys.argv[2],
                    baudrate = sys.argv[3],
                    bytesize = int(sys.argv[4]),
                    parity = sys.argv[5],
                    stopbits = int(sys.argv[6]),
                    timeout = 0.5,
                    xonxoff = None,
                    rtscts = None,
                    interCharTimeout = None
                    )

    elif len(sys.argv) == 6 or len(sys.argv) == 8 :
        ser = serial.Serial(
                port = sys.argv[1],
                baudrate = sys.argv[2],
                bytesize = int(sys.argv[3]),
                parity = sys.argv[4],
                stopbits = int(sys.argv[5]),
                timeout = 0.5,
                xonxoff = None,
                rtscts = None,
                interCharTimeout = None
                )
        for i in sys.argv[1:6] :
            print (i)
    print (">>:send")
    print ("<<:receive")
    print ("====\r\n")
    ser.isOpen()

    try:
        while 1 :        
            RecvData = ''
            time.sleep(1)    
            while ser.inWaiting() > 0 :
                RecvData += ser.read(1)
            if RecvData != '':
                if len(sys.argv) > 7 and sys.argv[7] == 'hex':
                    RecvData = HexShow(RecvData)
                    print ("<<" + RecvData)
                elif len(sys.argv) > 7 and sys.argv[7] == 'string':
                    print ("<<" + RecvData)
                else:
                    print ("<<" + RecvData)

            InPut = raw_input(">>")
            if InPut == 'exit':
                ser.close()
                exit()
            else:
                #string or hex data InPut
                if len(sys.argv) > 6 and sys.argv[6] == 'hex':
                    ser.write(InPut.decode("hex"))
                elif len(sys.argv) > 6 and sys.argv[6] == 'string':
                    ser.write(InPut + "\r\n")
                else:
                    ser.write(InPut + "\r\n")
    finally:
        ser.close()
        exit()

if __name__ == '__main__':
    main()
