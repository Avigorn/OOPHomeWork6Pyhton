from typing import List

from small_data.Student import Student
from small_data.StudentGroup import StudentGroup
from small_data.StudentGroupIterator import StudentGroupIterator
from small_data.Teacher import Teacher

"""
Класс тестового запуска Итератора
"""


def testIterator(student_group: StudentGroup):
    group_iterator = StudentGroupIterator(student_group)
    while group_iterator.hasNext():
        print(group_iterator.next())


"""
Головной класс выводящий в консоль результат работы всех прочих классов
"""


class Main:
    student1 = Student("Ivan", "Ivanov", "Ivanovich", 1)
    student2 = Student("Alexandr", "Alexandrovich", "Alexandrov", 2)
    teacher1 = Teacher("Vasiliy", "Smirnov", "Petrovich")
    teacher2 = Teacher("Arkadiy", "Smirnoff", "Al'bertovich")

    group_students: List[Student] = [student1, student2]
    group_teachers: List[Teacher] = [teacher1, teacher2]
    group_of_students = StudentGroup(group_teachers, group_students)
    testIterator(group_of_students)
