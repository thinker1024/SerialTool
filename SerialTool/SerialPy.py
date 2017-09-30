#!/usr/bin/env python
# -*- coding: utf-8 -*-

__author__ = "Tao Yang"

import serial
import time
import sys
import readline
import os

print ("\r\nA small debug tool for serial port programming.")
print ("=========\r\n")

ConfigArgs = {
            "Port":"/dev/ttyUSB0",
            "Baudrate":115200,
            "Databits":8,
            "Parity":"N",
            "Stopbits":1,
            "Txtypes":"string",
            "Rxtypes":"string"
        }

def HexShow(argv):
    result = ''
    xLen = len(argv)
    for i in xrange(xLen):
        temp = ord(argv[i])
        hhex = '%02x'%temp
        result += hhex+''
    return result

def PrintHelp():
    HelpStr="""
        usage:
        SerialTool [-s] com baudrate databits parity stopbits [TX data type] [RX data type]
        |_-s: save the current port configuration as default option
        |_com: the serial port device name
        |_baudrate: any standard baudrate, such as 9600, 115200, etc
        |_databits: 5,6,7,8
        |_parity: N,E
        |_stopbits: 1,1.5,2
        |_TX data types: string or hex, default is string if this parameter is null
        |_RX data types: string or hex, default is string if this parameter is null
        \r\nsimple usage example:
        ====\r\n
        SerialTool /dev/ttyUSB0 115200 8 N 1 hex hex
        \r\nCONTACT
        ====\r\n
        Project main page: https://pypi.python.org/pypi/SerialTool
    """
    print HelpStr

def LoadConfig():
    if len(sys.argv) < 6 and os.path.isfile('/.SerialTool.conf') == False:
        PrintHelp()
        exit()
    elif len(sys.argv) > 1 and len(sys.argv) < 6 :
        PrintHelp()
        exit()
    if os.path.isfile('/.SerialTool.conf') and len(sys.argv) == 1:
        with open('/.SerialTool.conf', 'r') as fp:
            x = fp.readlines()
            param = []
            for lines in x :
                lines = lines.replace("\r\n","").split(",")
                param.extend(lines)
            ConfigArgs["Port"] = param[0]
            ConfigArgs["Baudrate"] = param[1]
            ConfigArgs["Databits"] = param[2]
            ConfigArgs["Parity"] = param[3]
            ConfigArgs["Stopbits"] = param[4]
            ConfigArgs["Txtypes"] = param[5]
            ConfigArgs["Rxtypes"] = param[6]
    elif sys.argv[1] == '-s' :
        ConfigArgs["Port"] = sys.argv[2]
        ConfigArgs["Baudrate"] = sys.argv[3]
        ConfigArgs["Databits"] = sys.argv[4]
        ConfigArgs["Parity"] = sys.argv[5]
        ConfigArgs["Stopbits"] = sys.argv[6]
        if len(sys.argv) == 7 :
            ConfigArgs["Txtypes"] = "string"
            ConfigArgs["Rxtypes"] = "string"
        if len(sys.argv) == 9 :
            ConfigArgs["Txtypes"] = sys.argv[7]
            ConfigArgs["Rxtypes"] = sys.argv[8]
        with open("/.SerialTool.conf", "w") as fp: 
            fp.write(ConfigArgs["Port"] + "\r\n")
            fp.write(ConfigArgs["Baudrate"] + "\r\n")
            fp.write(ConfigArgs["Databits"] + "\r\n")
            fp.write(ConfigArgs["Parity"] + "\r\n")
            fp.write(ConfigArgs["Stopbits"] + "\r\n")
            fp.write(ConfigArgs["Txtypes"] + "\r\n")
            fp.write(ConfigArgs["Rxtypes"] + "\r\n")
    elif len(sys.argv) == 6 :
        ConfigArgs["Port"] = sys.argv[1]
        ConfigArgs["Baudrate"] = sys.argv[2]
        ConfigArgs["Databits"] = sys.argv[3]
        ConfigArgs["Parity"] = sys.argv[4]
        ConfigArgs["Stopbits"] = sys.argv[5]
    elif len(sys.argv) == 8 :
        ConfigArgs["Port"] = sys.argv[1]
        ConfigArgs["Baudrate"] = sys.argv[2]
        ConfigArgs["Databits"] = sys.argv[3]
        ConfigArgs["Parity"] = sys.argv[4]
        ConfigArgs["Stopbits"] = sys.argv[5]
        ConfigArgs["Txtypes"] = sys.argv[6]
        ConfigArgs["Rxtypes"] = sys.argv[7]

    print "Port Info"
    print "--------"
    print "Port:" + ConfigArgs["Port"]
    print "Baudrate:" + ConfigArgs["Baudrate"]
    print "Databits:" + ConfigArgs["Databits"]
    print "Parity:" + ConfigArgs["Parity"]
    print "Stopbits:" + ConfigArgs["Stopbits"]
    print "Txtypes:" + ConfigArgs["Txtypes"]
    print "Rxtypes:" + ConfigArgs["Rxtypes"]
    print "--------"

def main():
    LoadConfig()
    ser = serial.Serial(
            port = ConfigArgs["Port"],
            baudrate = ConfigArgs["Baudrate"],
            bytesize = int(ConfigArgs["Databits"]),
            parity = ConfigArgs["Parity"],
            stopbits = int(ConfigArgs["Stopbits"]),
            timeout = 0.5,
            xonxoff = None,
            rtscts = None,
            interCharTimeout = None
            )    
    print (">>:send")
    print ("<<:receive")
    print ("--------\r\n")
    ser.isOpen()

    try:
        while 1 :        
            RecvData = ''
            time.sleep(1)    
            while ser.inWaiting() > 0 :
                RecvData += ser.read(1)
            if RecvData != '':
                if ConfigArgs["Rxtypes"] == "hex":
                    RecvData = HexShow(RecvData)
                    print ("<<" + RecvData)
                if ConfigArgs["Rxtypes"] == "string":
                    print ("<<" + RecvData)
            InPut = raw_input(">>")
            if InPut == 'exit':
                ser.close()
                exit()
            else:
                if ConfigArgs["Txtypes"] == "hex" :
                    ser.write(InPut.decode("hex"))
                if ConfigArgs["Txtypes"] == "string" :
                    ser.write(InPut + "\r\n")

    finally:
        ser.close()
        exit()

if __name__ == '__main__':
    main()
