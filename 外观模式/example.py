"""
 @Author: Pegasus-Yang
 @Time: 2021/10/7 17:33
"""


class Screen:
    def power_on(self):
        print('打开显示器')


class CPU:
    def power_on(self):
        print('CPU上电')


class Mainboard:
    def power_on(self):
        print('主板上电')


class PC:
    def __init__(self):
        self.screen = Screen()
        self.cpu = CPU()
        self.mainboard = Mainboard()

    def power_on(self):
        self.screen.power_on()
        self.cpu.power_on()
        self.mainboard.power_on()


if __name__ == '__main__':
    PC().power_on()
