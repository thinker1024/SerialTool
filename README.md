# SerialTool
## Overview
A small debug tool for serial port programming.

## How to install
sudo pip install SerialTool

## Usage
**SerailTool -s com baudrate databits parity stopbits types types**
  1. **-s**: save the current port configuration as default option
  2. **com**: the serial port device name
  3. **baudrate**: any standard baudrate, such as 9600, 115200, etc.
  4. **databits**: 5,6,7,8
  5. **parity**: N,E
  6. **stopbits**: 1,1.5,2 
  7. **types**: Optional, TX data type, string or hex, default is string if this parameter is null.
  8. **types**: Optional, RX data type, string or hex, default is string if this parameter is null.

## Simple Usage Examples
SerialTool /dev/ttyUSB0 115200 8 N 1

## Project Main Page
https://pypi.python.org/pypi/SerialTool

