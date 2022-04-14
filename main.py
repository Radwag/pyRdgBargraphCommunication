# This is a sample Python script.
import time

from Bargraph import Bargraph


class Main:
    # Initialize cargraph device
    bargraph = Bargraph(255, True)

    def main(self):
        # connect to bargraph
        self.bargraph.connect(str(input("Enter serial port name: ")).upper(), 9600)

        # set power from 0 to 100
        self.bargraph.power = 56

        # set light on diode [0, 0, 0, 0, 0, 0, 0, 0, 0] on = 1, off = 0
        self.bargraph.green = [1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.bargraph.red =   [0, 0, 0, 0, 0, 1, 1, 1, 1]

        # send settings to bargraph device
        self.bargraph.send_settings()

        # waiting 5 seconds look on bargraph
        time.sleep(5)

        # set power from 0 to 100
        self.bargraph.power = 100

        # set light on diode [0, 0, 0, 0, 0, 0, 0, 0, 0] on = 1, off = 0
        self.bargraph.green = [1, 0, 1, 0, 1, 0, 1, 0, 1]
        self.bargraph.red = [0, 1, 0, 1, 0, 1, 0, 1, 0]

        # send settings to bargraph device
        self.bargraph.send_settings()

        self.animation()

    def animation(self):
        # waiting 1 seconds look on bargraph
        time.sleep(1)

        self.bargraph.power = 100
        self.bargraph.green = [1, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bargraph.red = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 0, 0, 0, 0, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 0, 0, 0, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 0, 0, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 1, 0, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 1, 1, 0, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 1, 1, 1, 0, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 1, 1, 1, 1, 0]
        self.bargraph.send_settings()

        time.sleep(1)
        self.bargraph.green = [1, 1, 1, 1, 1, 1, 1, 1, 1]
        self.bargraph.send_settings()


if __name__ == '__main__':
    Main().main()
