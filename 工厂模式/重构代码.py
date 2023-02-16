"""
  @Author: 天马
  @Date: 2023/2/14
  @Desc: 
"""
from dataclasses import dataclass


@dataclass
class Issue:
    """Issue"""
    id: int = None
    subject: str = None
    database_conn: str = None

    def save(self):
        raise NotImplementedError

    def update(self, **kwargs):
        raise NotImplementedError

    def search(self, **kwargs):
        raise NotImplementedError

    def delete(self):
        raise NotImplementedError


@dataclass
class RedmineIssue(Issue):
    """使用redmine存储Issue"""

    def get_value_from_custom_field(self):
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
    """使用mysql存储Issue"""

    def save(self):
        pass

    def update(self, **kwargs):
        pass

    def search(self, **kwargs):
        pass

    def delete(self):
        pass


class IssueFactory:
    database = None

    def __init__(self, database):
        self.database = database

    def find_in_storage(self, **kwargs) -> Issue:
        """
        从存储中加载数据
        """
        ...

    def get_issue(self, **kwargs) -> Issue:
        """
        实例化issue
        """
        return Issue()


class RedmineIssueFactory(IssueFactory):

    def get_issue(self, **kwargs) -> Issue:
        instance = self.find_in_storage(**kwargs)
        if instance:
            return instance
        else:
            return RedmineIssue(database_conn=self.database, **kwargs)


class MysqlIssueFactory(IssueFactory):
    def get_issue(self, **kwargs) -> Issue:
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
