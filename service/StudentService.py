from typing import List

from service.UserService import UserService
from small_data.Student import Student


class StudentService(UserService):

    def __init__(self):
        self.__students = []

    __students = List[Student]

    """
    Метод для получения списка студентов
    """
    def getAll(self):
        return self.__students

    """
    Метод перебирающий студентов основываясь на их параметрах
    """
    def create(self, first_name, surname, patronymic):
        count_max_id = 0
        for student in self.__students:
            if student.get_student_id() > count_max_id:
                count_max_id = student.get_student_id()
        count_max_id += 1
        student = Student(first_name, surname, patronymic, count_max_id)
        self.__students.append(student)

