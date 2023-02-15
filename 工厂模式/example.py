"""
 @Author: Pegasus-Yang
 @Time: 2021/10/5 10:09
"""
from abc import ABCMeta, abstractmethod


class Chat(metaclass=ABCMeta):
    """抽象基类，只做约束，无使用意义"""

    def __init__(self, **kwargs):
        ...

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


class ChatFactory(metaclass=ABCMeta):
    """
    在java中，工厂的父类可以通过设定并限制部分方法的实现，对子类的逻辑进行规范
    比如使用final描述部分关键方法，用来保护不变的部分逻辑
    """

    @abstractmethod
    def create_chat(self, **kwargs):
        pass

    def __call__(self, **kwargs):
        return self.create_chat(**kwargs)


class WechatFactory(ChatFactory):
    def create_chat(self, **kwargs):
        return Wechat(**kwargs)


class DingTalkFactory(ChatFactory):
    def create_chat(self, **kwargs):
        # 创建实例前的逻辑
        return DingTalk(**kwargs)


if __name__ == '__main__':
    dingtalk_factory = DingTalkFactory()
    dingtalk = dingtalk_factory.create_chat()
    dingtalk.send_message('Hello World')
    dingtalk2 = dingtalk_factory()
    dingtalk2.send_message('Hello World too')

    wechat_factory = WechatFactory()
    wechat = wechat_factory.create_chat()
    wechat.send_message('Hello World')
    wechat2 = wechat_factory()
    wechat2.send_message('Hello World too')
