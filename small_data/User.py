class User:
    """
    Single Responsibility
    """

    __firstname: str

    __surname: str

    __patronymic: str

    def __init__(self, firstname, surname, patronymic):
        self.__firstname = firstname
        self.__surname = surname
        self.__patronymic = patronymic

    def getFirstName(self):
        """
            Метод получения Имени пользователя
            """
        return self.__firstname

    def getSurname(self):
        """
           Метод получения Фамилии пользователя
           """
        return self.__surname

    def getPatronymic(self):
        """
        Метод получения Отчества пользователя
        """
        return self.__patronymic
