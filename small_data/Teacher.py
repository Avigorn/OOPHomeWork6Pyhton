from small_data.User import User


class Teacher(User):

    def __init__(self, first_name, surname, patronymic):
        super().__init__(first_name, surname, patronymic)


    """
    Строчный метод для вывода информации о студенте в консоль
    """
    def __str__(self):
        return (f"Teacher: firstName='{super().getFirstName()}', "
                f"surName='{super().getSurname()}', patronymic='{super().getPatronymic()}'")
