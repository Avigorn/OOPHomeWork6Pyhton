from small_data.User import User


class Teacher(User):

    """
    Open-Closed
    """
    def __init__(self, first_name, surname, patronymic):
        super().__init__(first_name, surname, patronymic)

    def __str__(self):
        """
        Строчный метод для вывода информации о преподавателе в консоль
        """
        return (f"Teacher: firstName='{super().getFirstName()}', "
                f"surName='{super().getSurname()}', patronymic='{super().getPatronymic()}'")
