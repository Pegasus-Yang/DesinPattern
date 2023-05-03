"""
 @Author: Pegasus-Yang
 @Time: 2021/10/5 8:59
"""
from abc import ABCMeta, abstractmethod


class Chat(metaclass=ABCMeta):
    """抽象基类，只做约束，无使用意义"""

    @abstractmethod
    def send_message(self, message):
        """抽象方法，约束子类必须实现该方法"""
        pass


class Wechat(Chat):
    def send_message(self, message):
        print(f'通过微信发送消息:{message}')


class DingTalk(Chat):
    def send_message(self, message):
        print(f'通过钉钉发送消息:{message}')


def chat_factory(c_type):
    """
    在正常的设计模式中，需要创建一个工厂类进行实例的创建和返回，封装其中的逻辑。
    但是在python中，只需要直接使用一个函数就可以实现工厂类的作用，
    并且避免了重复创建工厂类对象造成的资源占用
    可以通过配置文件+反射进行工厂的扩展，避免新增类型对工厂方法的修改
    """
    if c_type == 'wechat':
        return Wechat()
    elif c_type == 'dingtalk':
        return DingTalk()
    else:
        raise TypeError(f'No chat named {c_type}')


if __name__ == '__main__':
    dingtalk = chat_factory('dingtalk')
    dingtalk.send_message('Hello World')

    wechat = chat_factory('wechat')
    wechat.send_message('Hello World')
