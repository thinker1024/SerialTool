#!/usr/bin/env python

__author__ = "Tao Yang"

import serial
import time
import sys

print "\r\nA small debug tool for serial port programming."
print "-----------------\r\n"
# The serial port configuration
def HexShow(argv):
    result = ''
    xLen = len(argv)
    for i in xrange(xLen):
        temp = ord(argv[i])
        hhex = '%02x'%temp
        result += hhex+''
    return result

def main():
    if len(sys.argv) < 6:
        print "usage:"
        print "====\r\n"
        print "SerialTool com baudrate databits parity stopbits [TX data type] [RX data type]"
        print "|_com: the serial port device name"
        print "|_baudrate: any standard baudrate, such as 9600, 115200, etc"
        print "|_databits: 5,6,7,8"
        print "|_parity: N,E"
        print "|_stopbits: 1,1.5,2"
        print "|_TX data types: string or hex, default is string if this parameter is null"
        print "|_RX data types: string or hex, default is string if this parameter is null"
        print "\r\nsimple usage example:"
        print "====\r\n"
        print "SerialTool /dev/ttyUSB0 115200 8 N 1 hex hex"
        print "\r\nCONTACT"
        print "====\r\n"
        print "Project main page: https://pypi.python.org/pypi/SerialTool"
        exit()
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
    print "Port Info:" + ser.portstr
    print ">>:send"
    print "<<:receive"
    print "====\r\n"
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
                    print "<<" + RecvData
                elif len(sys.argv) > 7 and sys.argv[7] == 'string':
                    print "<<" + RecvData
                else:
                    print "<<" + RecvData

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
