from small_data.Student import Student
from typing import List, Iterator

from small_data.StudentGroup import StudentGroup


class StudentGroupIterator(Iterator[Student]):

    """
    Dependency Inversion
    """

    def __init__(self, student_group: StudentGroup):
        self._students = student_group.getStudents()
        self.__counter = 0
        self._students: List[Student]

    def hasNext(self):
        """
        Метод получения следующего значения счётчика по отношению студенту
        """
        return self.__counter < len(self._students)

    def __next__(self):
        """
             Метод создания следующего значения счётчика по отношению к студенту
             """
        if not self.hasNext():
            return None
        self.__counter += 1
        return self._students[self.__counter - 1]
