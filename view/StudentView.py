import logging

from view.UserView import UserView


class StudentView(UserView):

    """
    Переменна записываю информацию об имени студента
    """
    logger = logging.getLogger(__name__)

    """
    Метод передающий в консоль записанную информацию о студентах
    """
    def sendOnConsole(self, students):
        for user in students:
            self.logger.info(user.__str__())

    """
    Метод передающий в консоль записанную информацию о группе студентов
    """
    def sendOnConsoleUserGroup(self, student_group):
        self.logger.info(student_group.__str__())
