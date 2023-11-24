from small_data.Teacher import Teacher
from typing import List, Iterator

from small_data.TeachersGroup import TeachersGroup


class TeacherGroupIterator(Iterator[Teacher]):

    """
    Dependency Inversion
    """

    def __init__(self, teacher_group: TeachersGroup):
        self._teachers = teacher_group.getTeachers()
        self.__counter = 0
        self._teachers: List[Teacher]

    def hasNext(self):
        """
        Метод получения следующего значения счётчика по отношению к преподавателю
        """
        return self.__counter < len(self._teachers)

    def __next__(self):
        """
        Метод создания следующего значения счётчика по отношению к преподавателю
        """
        if not self.hasNext():
            return None
        self.__counter += 1
        return self._teachers[self.__counter - 1]
