from controller.UserController import UserController
from service.StudentGroupService import StudentGroupService
from service.StudentService import StudentService
from view.StudentView import StudentView


class StudentController(UserController):
    """
    Класс задающий основные параметры студенту
    Liskov Substitution
    """
    __data_service: StudentService = []

    __student_group_service: StudentGroupService = []

    __student_view: StudentView = []

    def __init__(self, first_name, surname, patronymic):
        super().__init__(patronymic, surname, first_name)
        self.__data_service.create(first_name, surname, patronymic)
        self.__student_view.sendOnConsole(self.__data_service.getAll())

