from abc import ABC
from typing import Iterable
from small_data.Teacher import Teacher


class TeachersGroup(Iterable[Teacher], ABC):

    def __init__(self, teacher):
        self.teacher = teacher

    """
    Метод получения студента
    """
    def getTeachers(self):
        return self.teacher

    """
    Строчный метод вывода информации о студенте
    """
    def __str__(self):
        return "TeachersGroup" + "teachers=" + str(self.teacher) + ""

    """
    Итерация
    """
    def __iter__(self):
        return self