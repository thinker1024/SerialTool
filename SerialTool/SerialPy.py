#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import serial
import time
import os
import json

DEFAULT_CONFIG_FILE = os.path.expanduser("~/.SerialTool.json")

def load_config():
    parser = argparse.ArgumentParser(description='A lightweight tool for serial port debugging.')
    parser.add_argument('port', type=str, help='the serial port device name')
    parser.add_argument('baudrate', type=int, help='the baudrate')
    parser.add_argument('databits', type=int, help='the number of data bits (5, 6, 7, 8)')
    parser.add_argument('parity', type=str, help='parity (N, E)')
    parser.add_argument('stopbits', type=int, help='the number of stop bits (1, 1.5, 2)')
    parser.add_argument('--txtype', type=str, default='string', help='TX data type (string or hex)')
    parser.add_argument('--rxtype', type=str, default='string', help='RX data type (string or hex)')
    parser.add_argument('-s', '--save', action='store_true', help='save the current port configuration as the default option')
    args = parser.parse_args()

    # Validate the provided baudrate
    if args.baudrate <= 0:
        raise ValueError("Baudrate must be a positive integer.")

    config_args = vars(args)
    print("Port Info")
    print("--------")
    for key, value in config_args.items():
        print("%s: %s" % (key.capitalize(), value))
    print("--------")

    if args.save:
        with open(DEFAULT_CONFIG_FILE, 'w') as fp:
            json.dump(config_args, fp, indent=4)

    return config_args

def is_hex_string(input_string):
    try:
        int(input_string, 16)
        return True
    except ValueError:
        return False

def main():
    global ser
    ser = None
    try:
        config_args = load_config()
        ser = serial.Serial(
            port=config_args['port'],
            baudrate=config_args['baudrate'],
            bytesize=config_args['databits'],
            parity=config_args['parity'],
            stopbits=config_args['stopbits'],
            timeout=0.5,
            xonxoff=None,
            rtscts=None,
            interCharTimeout=None
        )

        print(">>:send")
        print("<<:receive")
        print("--------\r\n")
        ser.isOpen()

        while True:
            recv_data = b''
            time.sleep(1)
            while ser.inWaiting() > 0:
                recv_data += ser.read(1)
            if recv_data:
                if config_args['rxtype'] == "hex":
                    recv_data = ''.join(['%02x' % byte for byte in recv_data])
                    print("<<" + recv_data)
                if config_args['rxtype'] == "string":
                    print("<<" + recv_data.decode('utf-8'))
            user_input = input(">>")
            if user_input == 'exit':
                ser.close()
                break
            else:
                if config_args['txtype'] == "hex":
                    try:
                        if is_hex_string(user_input):
                            ser.write(bytes.fromhex(user_input))
                        else:
                            print("Invalid hex input. Please enter a valid hex string.")
                    except ValueError:
                        print("Invalid hex input. Please enter a valid hex string.")
                else:
                    ser.write((user_input + "\n").encode('utf-8'))

    except KeyboardInterrupt:
        print("\nKeyboardInterrupt: Exiting the program.")
    except serial.SerialException as e:
        print(f"Serial Port Error: {e}")
    finally:
        if ser:
            ser.close()

if __name__ == '__main__':
    main()
