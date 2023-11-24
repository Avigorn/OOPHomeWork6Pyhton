from abc import ABC
from typing import Iterable
from small_data.Teacher import Teacher


class TeachersGroup(Iterable[Teacher], ABC):

    """
    Interface Segregation
    """

    def __init__(self, teacher):
        self.teacher = teacher

    def getTeachers(self):
        """
        Метод получения студента
        """
        return self.teacher

    def __str__(self):
        """
        Строчный метод вывода информации о студенте
        """
        return "TeachersGroup" + "teachers=" + str(self.teacher) + ""

    def __iter__(self):
        """
        Итерация
        """
        return self
