"""
 @Author: Pegasus-Yang
 @Time: 2021/10/7 8:22
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


class Talk(metaclass=ABCMeta):
    """抽象基类，只做约束，无使用意义"""

    @abstractmethod
    def talk(self, msg):
        """抽象方法，约束子类必须实现该方法"""
        pass


class QQ(Talk):
    def talk(self, msg):
        print(f'通过QQ发送消息：{msg}')


class InheritanceQQ(Chat, QQ):
    def send_message(self, message):
        self.talk(msg=message)


class WangWang(Talk):
    def talk(self, msg):
        print(f'通过旺旺发送消息：{msg}')


class Wework(Talk):
    def talk(self, msg):
        print(f'通过企业微信发送消息：{msg}')


class TalkToChat(Chat):
    def __init__(self, talk_ins):
        self.talk_ins = talk_ins

    def send_message(self, message):
        self.talk_ins.talk(msg=message)


def msg(tool, msg):
    if tool == 'qq':
        # target = InheritanceQQ()
        target = TalkToChat(QQ())
    elif tool == 'wechat':
        target = Wechat()
    elif tool == 'dingding':
        target = DingTalk()
    elif tool == 'wework':
        target = TalkToChat(Wework())
    elif tool == 'wangwang':
        target = TalkToChat(WangWang())
    else:
        raise TypeError(f'没有类型为：{tool}的聊天工具')
    target.send_message(msg)


if __name__ == '__main__':
    msg('wechat', 'Hello World!!!')
    msg('dingding', 'Hello World!!!')
    msg('qq', 'Hello World!!!')
    msg('wework', 'Hello World!!!')
    msg('wangwang', 'Hello World!!!')
