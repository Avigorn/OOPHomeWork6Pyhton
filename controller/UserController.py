from zope.interface import Interface

from small_data.User import User


class UserController(Interface(User)):
    """
    Изначальный класс присвоения параметров пользователям
    Interface Segregation
    """
    def __init__(self, patronymic, surname, first_name):
        self.patronymic = patronymic
        self.surname = surname
        self.first_name = first_name
