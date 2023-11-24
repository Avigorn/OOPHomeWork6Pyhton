from typing import List

from service.UserService import UserService
from small_data.Student import Student


class StudentService(UserService):

    """
    Liskov Substitution
    """

    def __init__(self):
        self.__students = List[Student]
        self.__students = []

    def getAll(self):
        """
        Метод для получения списка студентов
        """
        return self.__students

    def create(self, first_name, surname, patronymic):
        """
        Метод перебирающий студентов основываясь на их параметрах
        """
        count_max_id = 0
        for student in self.__students:
            if student.get_student_id() > count_max_id:
                count_max_id = student.get_student_id()
        count_max_id += 1
        student = Student(first_name, surname, patronymic, count_max_id)
        self.__students.append(student)

