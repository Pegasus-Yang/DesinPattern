"""
  @Author: 天马
  @Date: 2023/2/14
  @Desc: 
"""
from abc import ABCMeta, abstractmethod
from dataclasses import dataclass


@dataclass
class Issue(metaclass=ABCMeta):
    """
    Issue模型基类，定义了Issue的基本操作和基本属性
    """
    id: int = None
    subject: str = None
    database_conn: str = None

    @abstractmethod
    def save(self):
        ...

    @abstractmethod
    def update(self, **kwargs):
        ...

    @abstractmethod
    def search(self, **kwargs):
        ...

    @abstractmethod
    def delete(self):
        ...


@dataclass
class RedmineIssue(Issue):
    """
    在Redmine中存储Issue的实现类，继承了Issue基类，包含了针对Redmine进行处理的特定方法
    """

    def get_value_from_custom_field(self):
        """
        Redmine特有的数据处理方法
        """
        ...

    def save(self):
        pass

    def update(self, **kwargs):
        pass

    def search(self, **kwargs):
        pass

    def delete(self):
        pass


@dataclass
class MysqlIssue(Issue):
    """
    在Mysql中存储Issue的实现类，继承了Issue基类，包含了针对Mysql进行处理的特定方法
    """

    def connect_to_database(self):
        """
        Mysql特有的数据处理方法
        """
        pass

    def save(self):
        pass

    def update(self, **kwargs):
        pass

    def search(self, **kwargs):
        pass

    def delete(self):
        pass


class IssueFactory:
    """
    工厂的抽象基类，用于规范具体工厂需要实现的方法
    """
    database = None

    def __init__(self, database):
        self.database = database

    @abstractmethod
    def get_issue(self, **kwargs) -> Issue:
        """
        实例化issue
        """
        ...


class RedmineIssueFactory(IssueFactory):
    """
    RedmineIssue的工厂类，用符合基类规范的方式生产RedmineIssue对象
    """

    def find_in_storage(self, **kwargs) -> Issue:
        """
        从缓存中读取数据
        """
        ...

    def get_issue(self, **kwargs) -> Issue:
        """
        通过重写父类的方法，实现具体的工厂
        """
        instance = self.find_in_storage(**kwargs)
        if instance:
            instance.database_conn = self.database
            return instance
        else:
            return RedmineIssue(database_conn=self.database, **kwargs)


class MysqlIssueFactory(IssueFactory):
    """
    MysqlIssue的工厂类，用符合基类规范的方式生产MysqlIssue对象
    """

    def get_issue(self, **kwargs) -> Issue:
        """
        通过重写父类的方法，实现具体的工厂
        """
        return MysqlIssue(database_conn=self.database, **kwargs)


if __name__ == '__main__':
    redmine = "redmine"
    mysql = "mysql"
    rf = RedmineIssueFactory(database=redmine)
    mf = MysqlIssueFactory(database=mysql)
    r_issue = rf.get_issue(id=1234, subject="测试标题")
    m_issue = mf.get_issue(id=2234, subject="测试标题")

    r_issue.save()
    m_issue.update()
    # IDE不会提示RedmineIssue的特有方法，并且在使用特有方法时出现警告，避免误用实现细节相关的方法
    r_issue.find_in_storage()
