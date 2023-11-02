from small_data.Student import Student


class StudentComparator(Student):

    @staticmethod
    def compare(o1: Student, o2: Student) -> int:
        result_of_comparing = o1.getSurname().compare_to(o2.getSurname())
        if result_of_comparing == 0:
            result_of_comparing = o1.getFirstName().compare_to(o2.getFirstName())
            if result_of_comparing == 0:
                return o1.getPatronymic().compare_to(o2.getPatronymic())
            else:
                return result_of_comparing
        else:
            return result_of_comparing
