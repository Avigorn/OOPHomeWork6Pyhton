from controller.UserController import UserController
from service.TeacherService import TeacherService
from view.TeacherView import TeacherView


class StudentController(UserController):

    __data_service: TeacherService = []

    __teacher_view: TeacherView = []

    """
    Класс задающий основные параметры учителю
    """
    def create(self, first_name, surname, patronymic):
        self.__data_service.create(first_name, surname, patronymic)
        self.__student_view.sendOnConsole(self.__data_service.getAll())
