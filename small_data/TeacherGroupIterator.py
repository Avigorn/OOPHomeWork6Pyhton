from small_data.Teacher import Teacher
from typing import List

from small_data.TeachersGroup import TeachersGroup


class TeacherGroupIterator(Teacher):
    __counter: int

    _teachers: List[Teacher]

    def __init__(self, teacher_group: TeachersGroup):
        self._teachers = teacher_group.getTeachers()
        self.__counter = 0

    """
    Метод получения следующего значения счётчика по отношению к преподавателю
    """
    def hasNext(self):
        return self.__counter < len(self._teachers)

    """
    Метод создания следующего значения счётчика по отношению к преподавателю
    """
    def next(self):
        if not self.hasNext():
            return None
        self.__counter += 1
        return self._teachers[self.__counter - 1]
