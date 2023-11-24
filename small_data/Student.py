from small_data.User import User


class Student(User):

    """
    Open-Closed
    """

    def __init__(self, first_name, surname, patronymic, student_id=None):
        super().__init__(first_name, surname, patronymic)
        self.__student_id = []
        self.__student_id = student_id

    def getStudentId(self):
        """
        Метод получения ID студента
        """
        return self.__student_id

    def __str__(self):
        """
        Строчный метод для вывода информации о студенте в консоль
        """
        return (f"Student: studentId='{self.__student_id}, firstName='{super().getFirstName()}', "
                f"surName='{super().getSurname()}', patronymic='{super().getPatronymic()}'")
