from typing import List, Iterator

from small_data.Teacher import Teacher
from small_data.TeachersGroup import TeachersGroup


# noinspection PyArgumentList
class TeachersGroupService:

    """
    Interface Segregation
    """

    def __init__(self):
        self.__teachers_group = None
        self.teachers = None
        self.__teachers_group: TeachersGroup

    def createTeachersGroup(self, teacher: Teacher, students: List[Teacher]):
        """
        Метод создания листа преподавателей с использованием класса Teacher
        """
        self.__teachers_group = TeachersGroup(teacher, students)

    def getTeachersGroup(self):
        """
        Метод получения группы преподавателей
        """
        return self.__teachers_group

    def getTeacherFromStudentGroup(self, firstname, surname):
        """
        Метод получения конкретного преподавателя из списка
        """
        iterate: Iterator[Teacher] = self.__teachers_group.__iter__()
        result: List[Teacher] = []
        while True:
            try:
                teacher: Teacher = next(iterate)
                if teacher.getFirstName().lower() == firstname.lower() and teacher.getSurname().lower() == surname.lower():
                    result.append(teacher)
            except StopIteration:
                break
            if len(result) == 0:
                raise ValueError(f"Преподаватель с именем {firstname} и фамилией {surname} не найден")
            if len(result) != 1:
                raise ValueError("Найдено более одного преподавателя с указанными именем и фамилией")
            return result[0]

    def getSortedTeachersGroup(self):
        """
        Сортировка группы преподавателей
        """
        self.teachers: List[Teacher] = list(self.__teachers_group.getTeachers())
        self.teachers.sort()
        return self.teachers
