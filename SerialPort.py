#Python Serial Port Extension for Win32, OSX, Linux, BSD, Jython, IronPython
#https://pypi.python.org/pypi/pyserial
#http://pyserial.readthedocs.io/en/latest/
import serial


class SerialPortRdg:
        def __init__(self, port, baudrate):
            self.ser = serial.Serial()
            self.ser.baudrate = baudrate
            self.ser.port = port
            self.ser.open()

        def send(self, query):
            self.ser.write(bytes(query + '\r\n', "utf-8"))
