from controller.UserController import UserController
from service.StudentGroupService import StudentGroupService
from service.StudentService import StudentService
from view.StudentView import StudentView


class StudentController(UserController):

    __data_service: StudentService = []

    __student_group_service: StudentGroupService = []

    __student_view: StudentView = []

    """
    класс задающий основные параметры студенту
    """
    def create(self, first_name, surname, patronymic):
        self.__data_service.create(first_name, surname, patronymic)
        self.__student_view.sendOnConsole(self.__data_service.getAll())

