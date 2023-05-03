"""
 @Author: Pegasus-Yang
 @Time: 2021/10/5 10:22
"""
from abc import ABCMeta, abstractmethod


class CPU(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class Mainboard(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass


class Screen(metaclass=ABCMeta):
    @abstractmethod
    def run(self):
        pass

class x86CPU(CPU):
    def run(self):
        print(f'X86 CPU running')


class x64CPU(CPU):
    def run(self):
        print(f'X64 CPU running')


class armCPU(CPU):
    def run(self):
        print(f'arm CPU running')


class bigMainboard(Mainboard):
    def run(self):
        print(f'big Mainboard running')


class smallMainboard(Mainboard):
    def run(self):
        print(f'small Mainboard running')


class itxMainboard(Mainboard):
    def run(self):
        print(f'itx Mainboard running')


class i27Screen(Screen):
    def run(self):
        print(f'i27 Screen running')


class i24Screen(Screen):
    def run(self):
        print(f'i24 Screen running')


class i21Screen(Screen):
    def run(self):
        print(f'i21 Screen running')


class PCFactory(metaclass=ABCMeta):
    @abstractmethod
    def chose_cpu(self) -> CPU:
        pass

    @abstractmethod
    def chose_mainboard(self) -> Mainboard:
        pass

    @abstractmethod
    def chose_screen(self) -> Screen:
        pass


class asusPCFactory(PCFactory):
    def chose_cpu(self):
        return x64CPU()

    def chose_mainboard(self):
        return bigMainboard()

    def chose_screen(self):
        return i27Screen()


class macPCFactory(PCFactory):
    def chose_cpu(self):
        return armCPU()

    def chose_mainboard(self):
        return itxMainboard()

    def chose_screen(self):
        return i24Screen()


class PC:
    """通过factory的传入，通过工厂限制了cpu/mainboard/screen的组合可能性，进行了约束"""
    def __init__(self, factory: PCFactory):
        self.cpu = factory.chose_cpu()
        self.mainboard = factory.chose_mainboard()
        self.screen = factory.chose_screen()

    def power_on(self):
        self.cpu.run()
        self.mainboard.run()
        self.screen.run()


def makePC(pc_type):
    if pc_type == 'mac':
        return PC(macPCFactory())
    elif pc_type == 'asus':
        return PC(asusPCFactory())
    else:
        raise TypeError(f'No PC type named:{pc_type}')


if __name__ == '__main__':
    pc_type = input('请输入计算机类别:')
    pc = makePC(pc_type=pc_type)
    pc.power_on()
