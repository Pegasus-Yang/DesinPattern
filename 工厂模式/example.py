"""
 @Author: Pegasus-Yang
 @Time: 2021/10/5 10:09
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


class ChatFactory(metaclass=ABCMeta):
    @abstractmethod
    def create_chat(self):
        pass

    def __call__(self):
        return self.create_chat()


class WechatFactory(ChatFactory):
    def create_chat(self):
        return Wechat()


class DingTalkFactory(ChatFactory):
    def create_chat(self):
        return DingTalk()


if __name__ == '__main__':
    dingtalk_factory = DingTalkFactory()
    dingtalk = dingtalk_factory.create_chat()
    dingtalk.send_message('Hello World')
    # 通过__call__方法，扩展工厂对象，省去方法调用的书写
    dingtalk2 = dingtalk_factory()
    dingtalk2.send_message('Hello World too')

    wechat_factory = WechatFactory()
    wechat = wechat_factory.create_chat()
    wechat.send_message('Hello World')
    # 通过__call__方法，扩展工厂对象，省去方法调用的书写
    wechat2 = wechat_factory()
    wechat2.send_message('Hello World too')