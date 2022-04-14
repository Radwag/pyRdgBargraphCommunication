import json

import crc8 as crc8

from SerialPort import SerialPortRdg


class Bargraph:

    def __init__(self, address, is_request):

        self.address = address
        self.is_request = is_request
        self.command = 'BargraphSet'
        self.power = 70
        self.green = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.red = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.crc = 90

    def set_power(self, power):
        self.power = power

    def set_green(self, green):
        self.green = green

    def set_red(self, red):
        self.red = red

    def send_settings(self):
        content_body = json.loads(
            json.dumps({'Address': self.address, 'IsRequest': self.is_request, 'Red': self.red, 'Green': self.green}))
        query = json.loads(json.dumps({'Content': content_body}))
        query['Crc'] = self.crc
        print()
        crc8_calc = self.calculate_crc(json.dumps(query))
        query['Crc'] = crc8_calc
        self.serial_port.send(json.dumps(query))

    def connect(self, port, baudrate):
        self.serial_port = SerialPortRdg(port, baudrate)

    def calculate_crc(self, message):
        hash = crc8.crc8()
        hash.update(bytes(message + "\n", "utf-8"))
        return hash.hexdigest()
