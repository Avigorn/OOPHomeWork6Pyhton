from typing import List, Iterator

from small_data.Student import Student
from small_data.StudentComparator import StudentComparator
from small_data.StudentGroup import StudentGroup
from small_data.Teacher import Teacher


# noinspection PyArgumentList
class StudentGroupService:
    __student_group: StudentGroup

    def __init__(self):
        self.students = None

    """
    Метод создания группы студентов с использование класса Student
    """

    def createStudentGroup(self, teacher: Teacher, students: List[Student]):
        self.__student_group = StudentGroup(teacher, students)

    """
    Метод получения группы студентов
    """

    def getStudentGroup(self):
        return self.__student_group

    """
    Метод получения конкретного студента из группы
    """

    def getStudentFromStudentGroup(self, firstname, surname):
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

    """
    Сортировка группы студентов
    """

    def getSortedStudentGroup(self):
        self.students: List[Student] = list(self.__student_group.getStudents())
        self.students.sort()
        return self.students

    """
    Сортировка студентов по ФИО внутри группы
    """

    def getSortedByFIOStudentGroup(self):
        self.students: List[Student] = list(self.__student_group.getStudents())
        self.students.sort(StudentComparator())
        return self.students
