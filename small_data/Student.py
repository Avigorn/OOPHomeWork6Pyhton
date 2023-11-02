from small_data.User import User


class Student(User):

    __student_id = []

    def __init__(self, first_name, surname, patronymic, student_id=None):
        super().__init__(first_name, surname, patronymic)
        self.__student_id = student_id

    """
    Метод получения ID студента
    """
    def getStudentId(self):
        return self.__student_id

    """
    Строчный метод для вывода информации о студенте в консоль
    """
    def __str__(self):
        return (f"studentId='{self.__student_id}, firstName='{super().getFirstName()}', "
                f"surName='{super().getSurname()}', patronymic='{super().getPatronymic()}'")

    """
    
    """
    def __lt__(self, other):
        return self.__student_id.compare_to.other.__student_id
