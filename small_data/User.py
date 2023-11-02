class User:
    __firstname: str

    __surname: str

    __patronymic: str

    def __init__(self, firstname, surname, patronymic):
        self.__firstname = firstname
        self.__surname = surname
        self.__patronymic = patronymic

    """
    Метод получения Имени пользователя
    """
    def getFirstName(self):
        return self.__firstname

    """
    Метод получения Фамилии пользователя
    """
    def getSurname(self):
        return self.__surname

    """
    Метод получения Отчества пользователя
    """
    def getPatronymic(self):
        return self.__patronymic

    """
    Строчный метод вывода информации о пользователе
    """
    def __str__(self):
        return "User{" + \
            "firstName='" + self.__firstname + '\'' + \
            ", secondName='" + self.__surname + '\'' + \
            ", patronymic='" + self.__patronymic + '\'' + \
            '}'

    """
    Сравнения исходных параметров пользователя с получаемыми
    """
    def __eq__(self, other):
        if self is other:
            return True
        if not isinstance(other, User):
            return False
        if self.__firstname != other.__firstname:
            return False
        if self.__surname != other.__surname:
            return self.__patronymic != other.__patronymic
