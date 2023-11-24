from abc import ABC
from small_data.Student import Student
from typing import Iterable


class StudentGroup(Iterable[Student], ABC):

    """
    Liskov Substitution
    """

    def __init__(self, students):
        self.students = students

    def getStudents(self):
        """
        Метод получения студента
        """
        return self.students

    def __iter__(self):
        """
        Итерация
        """
        return self
