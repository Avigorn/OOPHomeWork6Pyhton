from typing import List

from small_data.Student import Student
from small_data.StudentGroup import StudentGroup
from small_data.StudentGroupIterator import StudentGroupIterator
from small_data.Teacher import Teacher
from small_data.TeacherGroupIterator import TeacherGroupIterator
from small_data.TeachersGroup import TeachersGroup

"""
Класс тестового запуска Итератора
"""


def testIterator(student_group: StudentGroup, teachers_group: TeachersGroup):
    student_group_iterator = StudentGroupIterator(student_group)
    teachers_group_iterator = TeacherGroupIterator(teachers_group)
    while student_group_iterator.hasNext() or teachers_group_iterator.hasNext():
        print(student_group_iterator.next())
        print(teachers_group_iterator.next())


"""
Головной класс выводящий в консоль результат работы всех прочих классов
"""


class Main:
    student1 = Student("Ivan", "Ivanov", "Ivanovich", 1)
    student2 = Student("Alexandr", "Alexandrovich", "Alexandrov", 2)
    student3 = Student("Petr", "Petrov", "Petrovich", 3)
    teacher1 = Teacher("Vasiliy", "Smirnov", "Petrovich")
    teacher2 = Teacher("Arkadiy", "Smirnoff", "Al'bertovich")

    group_students: List[Student] = [student1, student2, student3]
    group_teachers: List[Teacher] = [teacher1, teacher2]
    group_of_students = StudentGroup(group_students)
    group_of_teachers = TeachersGroup(group_teachers)
    testIterator(group_of_students, group_of_teachers)
