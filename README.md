# SerialTool
## Overview
A lightweight tool for serial port debugging.

## How to install
sudo pip install SerialTool

## Usage
usage: SerialPy.py [-h] [--txtype TXTYPE] [--rxtype RXTYPE] [-s] port baudrate databits parity stopbits

A lightweight tool for serial port debugging.

positional arguments:
  port             the serial port device name
  baudrate         the baudrate
  databits         the number of data bits (5, 6, 7, 8)
  parity           parity (N, E)
  stopbits         the number of stop bits (1, 1.5, 2)

options:
  -h, --help       show this help message and exit
  --txtype TXTYPE  TX data type (string or hex)
  --rxtype RXTYPE  RX data type (string or hex)
  -s, --save       save the current port configuration as the default option

## Simple Usage Examples
SerialTool /dev/ttyUSB0 115200 8 N 1

SerialTool /dev/ttyUSB0 115200 8 N 1 --txtype [string/hex] --rxtype [string/hex]

## Project Main Page
https://pypi.python.org/pypi/SerialTool

