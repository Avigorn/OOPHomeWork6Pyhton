from typing import List, Iterator

from small_data.Student import Teacher
from small_data.Teacher import Teacher
from small_data.TeachersGroup import TeachersGroup


# noinspection PyArgumentList
class TeachersGroupService:
    __teachers_group: TeachersGroup

    def __init__(self):
        self.teachers = None

    """
    Метод создания листа преподавателей с использование класса Teacher
    """

    def createTeachersGroup(self, teacher: Teacher, students: List[Teacher]):
        self.__teachers_group = TeachersGroup(teacher, students)

    """
    Метод получения группы преподавателей
    """

    def getTeachersGroup(self):
        return self.__teachers_group

    """
    Метод получения конкретного преподавателя из списка
    """

    def getTeacherFromStudentGroup(self, firstname, surname):
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

    """
    Сортировка группы преподавателей
    """

    def getSortedTeachersGroup(self):
        self.teachers: List[Teacher] = list(self.__teachers_group.getTeachers())
        self.teachers.sort()
        return self.teachers

    """
    Сортировка преподавателей по ФИО внутри группы
    """

    def getSortedByFIOTeachersGroup(self):
        self.teachers: List[Teacher] = list(self.__teachers_group.getTeachers())
        self.teachers.sort(TeachersComparator())
        return self.teachers