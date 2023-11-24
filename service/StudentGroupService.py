from typing import List, Iterator

from small_data.Student import Student
from small_data.StudentComparator import StudentComparator
from small_data.StudentGroup import StudentGroup
from small_data.Teacher import Teacher


# noinspection PyArgumentList
class StudentGroupService:

    """
    Single Responsibility
    """

    def __init__(self):
        self.__student_group = None
        self.students = None
        self.__student_group: StudentGroup

    def createStudentGroup(self, teacher: Teacher, students: List[Student]):
        """
        Метод создания группы студентов с использованием класса Student
        """
        self.__student_group = StudentGroup(teacher, students)

    def getStudentGroup(self):
        """
        Метод получения группы студентов
        """
        return self.__student_group

    def getStudentFromStudentGroup(self, firstname, surname):
        """
        Метод получения конкретного студента из группы
        """
        iterate: Iterator[Student] = self.__student_group.__iter__()
        result: List[Student] = []
        while True:
            try:
                student: Student = next(iterate)
                if student.getFirstName().lower() == firstname.lower() and student.getSurname().lower() == surname.lower():
                    result.append(student)
            except StopIteration:
                break
            if len(result) == 0:
                raise ValueError(f"Студент с именем {firstname} и фамилией {surname} не найден")
            if len(result) != 1:
                raise ValueError("Найдено более одного студента с указанными именем и фамилией")
            return result[0]
