import logging

from view.UserView import UserView


class StudentView(UserView):

    """
    Переменна записываю информацию об имени студента
    """
    logger = logging.getLogger(__name__)

    def sendOnConsole(self, students):
        """
        Метод передающий в консоль записанную информацию о студентах
        """
        for user in students:
            self.logger.info(user.__str__())
