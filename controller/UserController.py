from zope.interface import Interface

from small_data.User import User


class UserController(Interface(User)):

    def __init__(self):
        self.patronymic = None
        self.surname = None
        self.first_name = None

    """
    Изначальный класс присвоения параметров пользователям
    """
    def create(self, first_name, surname, patronymic):
        self.first_name = first_name
        self.surname = surname
        self.patronymic = patronymic
