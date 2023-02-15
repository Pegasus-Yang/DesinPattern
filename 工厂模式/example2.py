"""
  @Author: 天马
  @Date: 2023/2/12
  @Desc: 
"""
from dataclasses import dataclass


@dataclass
class RedmineIssue:
    """Issue"""
    id: int = None
    subject: str = None
    redmine_conn: str = None

    def save(self):
        ...

    def update(self, **kwargs):
        ...


@dataclass
class RedmineStudent(RedmineIssue):
    """学生"""
    name: str = None
    class_name: str = None

    def choose_class(self):
        ...


@dataclass
class RedmineTeacher(RedmineIssue):
    """教师"""
    name: str = None
    level: str = None

    def prepare_homework(self):
        ...


@dataclass
class RedmineAssistant(RedmineIssue):
    """助教"""
    name: str = None
    teacher_name: str = None


class RedmineIssueFactory:
    redmine_conn = None

    def __init__(self, redmine_conn):
        self.redmine_conn = redmine_conn

    def get_instance(self, **kwargs) -> RedmineIssue:
        raise NotImplementedError


class RedmineStudentFactory(RedmineIssueFactory):

    def get_instance(self, id, subject, name, class_name, **kwargs) -> RedmineIssue:
        ...
        return RedmineStudent(id=id, subject=subject, name=name, class_name=class_name, redmine_conn=self.redmine_conn)


class RedmineTeacherFactory(RedmineIssueFactory):

    def get_instance(self, id, subject, name, level, **kwargs) -> RedmineIssue:
        ...
        return RedmineTeacher(id=id, subject=subject, name=name, level=level, redmine_conn=self.redmine_conn)


class RedmineAssistantFactory(RedmineIssueFactory):

    def get_instance(self, id, subject, name, teacher_name, **kwargs) -> RedmineIssue:
        ...
        return RedmineAssistant(id=id, subject=subject, name=name, teacher_name=teacher_name,
                                redmine_conn=self.redmine_conn)


if __name__ == '__main__':
    redmine = "http"
    # 创建对应连接的工厂
    dev_redmine_student_factory = RedmineStudentFactory(redmine_conn=redmine)
    dev_redmine_teacher_factory = RedmineTeacherFactory(redmine_conn=redmine)
    dev_redmine_assistant_factory = RedmineAssistantFactory(redmine_conn=redmine)

    student = dev_redmine_student_factory.get_instance(id=1234, subject="测试标题", name="学生", class_name="class")
    teacher = dev_redmine_teacher_factory.get_instance(id=2234, subject="测试标题", name="老师", level="junior")
    assistant = dev_redmine_assistant_factory.get_instance(id=3234, subject="测试标题", name="助教", teacher_name="老师")

    student.save()
    teacher.update()
    # 对于特有的方法有提示
    student.choose_class()
