"""
 @Author: Pegasus-Yang
 @Time: 2021/10/6 22:07
"""


class Singleton:

    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_ins'):
            cls._ins = super().__new__(cls)
        return cls._ins


class realClass(Singleton):
    def __init__(self, a):
        self.a = a


if __name__ == '__main__':
    a = realClass(10)
    b = realClass(20)
    print(a.a)
    print(b.a)
