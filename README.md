# pyRdgBargraphCommunication
[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]

An example showing how to connect and communicate with a Radwag bargraph via RS232 using Json protocol.

# Technology
Project was written in the Python.

# Working description
After entering the serial port name, you can manage the bargraph via json protocol.

# Commands
* Set all red segments light on with power of light 70%
```bash
{"Content": {"Address": 255, "IsRequest": true, "Power":70, "Red": [1, 1, 1, 1, 1, 1, 1, 1, 1], "Green": [0, 0, 0, 0, 0, 0, 0, 0, 0]}, "Crc": "bf"}
```
* Set all green segments light on with power of light 70%
```bash
{"Content": {"Address": 255, "IsRequest": true, "Power":70, "Red": [0, 0, 0, 0, 0, 0, 0, 0, 0], "Green": [1, 1, 1, 1, 1, 1, 1, 1, 1]}, "Crc": "bf"}
```
* Set all segments light on with power of light 100%
```bash
{"Content": {"Address": 255, "IsRequest": true, "Power":100, "Red": [1, 1, 1, 1, 1, 1, 1, 1, 1], "Green": [1, 1, 1, 1, 1, 1, 1, 1, 1]}, "Crc": "bf"}
```
* Set all segments light off with power of light 0%
```bash
{"Content": {"Address": 255, "IsRequest": true, "Power":0, "Red": [0, 0, 0, 0, 0, 0, 0, 0, 0], "Green": [0, 0, 0, 0, 0, 0, 0, 0, 0]}, "Crc": "bf"}
```
# Command structure

![image](https://user-images.githubusercontent.com/46632727/163963048-c0aed0c2-fca9-47da-8b66-adae1f3073fa.png)
* Content - object with all settings necessary to manage bargraph device.
  * Address - Address of device (default 255)
  * IsRequest - 
  * Power - power of luminous segments
  * Red - a table containing the states of individual bargraph (Red)segments
  * Green - a table containing the states of individual bargraph (Green)segments
* Crc - 8bit CRC

# Installation
1. Clone or download this repository.
2. Open project in JestBrains PyCharm.
3. Build and run.

[contributors-shield]: https://img.shields.io/github/contributors/Radwag/pyRdgBargraphCommunication.svg?style=for-the-badge
[contributors-url]: https://github.com/Radwag/pyRdgBargraphCommunication/contributors
[forks-shield]: https://img.shields.io/github/forks/Radwag/pyRdgBargraphCommunication.svg?style=for-the-badge
[forks-url]: https://github.com/Radwag/pyRdgBargraphCommunication/network/members
[stars-shield]: https://img.shields.io/github/stars/Radwag/pyRdgBargraphCommunication.svg?style=for-the-badge
[stars-url]: https://github.com/Radwag/pyRdgBargraphCommunication/stargazers
[issues-shield]: https://img.shields.io/github/issues/Radwag/pyRdgBargraphCommunication.svg?style=for-the-badge
[issues-url]: https://github.com/Radwag/pyRdgBargraphCommunication/issues
