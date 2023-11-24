from typing import List

from service.UserService import UserService
from small_data.Teacher import Teacher


class TeacherService(UserService):

    """
    Liskov Substitution
    """

    def __init__(self):
        self.__teachers = List[Teacher]
        self.__teachers = []

    def getAll(self) -> List:
        """
        Метод получения всех учителей
        """
        return self.__teachers

    def create(self, first_name, surname, patronymic):
        """
        Метод для сортировки учителей
        """
        count_max_id = 0
        for teacher in self.__teachers:
            if teacher.get_student_id() > count_max_id:
                count_max_id = teacher.get_student_id()
        count_max_id += 1
        teacher = Teacher(first_name, surname, patronymic)
        self.__teachers.append(teacher)
