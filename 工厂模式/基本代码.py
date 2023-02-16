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

    def create(self):
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

    def get_value_from_custom_field(self, name, **kwargs):
        """
        从自定义字段中读取值
        """
        ...

    def create(self):
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

    def create(self):
        pass

    def update(self, **kwargs):
        pass

    def search(self, **kwargs):
        pass

    def delete(self):
        pass


def find_in_storage(**kwargs) -> Issue:
    """
    从存储中加载数据
    """
    ...


if __name__ == '__main__':
    redmine = "redmine"
    mysql = "mysql"

    # 优先从缓存中加载实例
    instance = find_in_storage()
    if instance:
        r_issue = instance
    else:
        r_issue = RedmineIssue(id=1234, subject="测试标题", database_conn=redmine)

    m_issue = MysqlIssue(id=2234, subject="测试标题", database_conn=mysql)

    r_issue.create()
    m_issue.update()
