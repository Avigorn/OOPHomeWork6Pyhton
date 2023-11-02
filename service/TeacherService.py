from datetime import datetime
from typing import List

from service.UserService import UserService
from small_data.Teacher import Teacher


class TeacherService(UserService):

    def __init__(self):
        self.__teachers = []

    __teachers = List[Teacher]

    """
    Метод получения всех учителей
    """
    def getAll(self) -> List:
        return self.__teachers

    """
    Метод для сортировки учителей
    """
    def create(self, first_name, surname, patronymic):
        count_max_id = 0
        for teacher in self.__teachers:
            if teacher.get_student_id() > count_max_id:
                count_max_id = teacher.get_student_id()
        count_max_id += 1
        teacher = Teacher(first_name, surname, patronymic)
        self.__teachers.append(teacher)
