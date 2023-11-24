from controller.UserController import UserController
from service.TeacherService import TeacherService
from view.TeacherView import TeacherView


class StudentController(UserController):
    """
    Класс задающий основные параметры учителю
    Liskov Substitution
    """
    __data_service: TeacherService = []
    __teacher_view: TeacherView = []

    def __init__(self, first_name, surname, patronymic):
        super().__init__(patronymic, surname, first_name)
        self.__data_service.create(first_name, surname, patronymic)
        self.__student_view.sendOnConsole(self.__data_service.getAll())
