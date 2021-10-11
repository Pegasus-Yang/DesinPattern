"""
 @Author: Pegasus-Yang
 @Time: 2021/10/6 16:23
"""
from abc import ABCMeta, abstractmethod


class PC:
    def __init__(self, cpu, screen, mainboard, mouse=None, keyboard=None):
        self.cpu = cpu
        self.screen = screen
        self.mainboard = mainboard
        self.mouse = mouse
        self.keyboard = keyboard

    def __str__(self):
        return f'cpu:{self.cpu}|screen:{self.screen}|mainboard:{self.mainboard}|mouse:{self.mouse}|keyboard:{self.keyboard}'


class PCBuilder(metaclass=ABCMeta):
    def __init__(self, cpu, screen, mainboard):
        self.PC = PC(cpu=cpu, screen=screen, mainboard=mainboard)

    @abstractmethod
    def set_mouse(self):
        pass

    @abstractmethod
    def set_keyboard(self):
        pass

    @abstractmethod
    def get_PC(self):
        pass


class macPCBuilder(PCBuilder):

    def __init__(self):
        cpu = 'mac CPU'
        screen = 'mac screen'
        mainboard = 'mac mainboard'
        super().__init__(cpu, screen, mainboard)

    def set_mouse(self):
        self.PC.mouse = 'mac鼠标'

    def set_keyboard(self):
        self.PC.keyboard = 'mac键盘'

    def get_PC(self):
        return self.PC


class asusPCBuilder(PCBuilder):

    def __init__(self):
        cpu = 'x64 CPU'
        screen = 'asus screen'
        mainboard = 'asus mainboard'
        super().__init__(cpu, screen, mainboard)

    def set_mouse(self):
        self.PC.mouse = '华硕鼠标'

    def set_keyboard(self):
        self.PC.keyboard = '华硕键盘'

    def get_PC(self):
        return self.PC


def director(builder: PCBuilder):
    builder.set_mouse()
    builder.set_keyboard()
    return builder.get_PC()


if __name__ == '__main__':
    mac_builder = macPCBuilder()
    mac = director(mac_builder)
    print(mac)
    asus_builder = asusPCBuilder()
    asus = director(asus_builder)
    print(asus)