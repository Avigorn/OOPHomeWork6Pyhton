import logging

from view.UserView import UserView


class TeacherView(UserView):

    """
    Переменная записывающая информацию об учителях
    """
    logger = logging.getLogger(__name__)

    """
    Метод передающий в консоль информацию об учителях
    """
    def sendOnConsole(self, teachers):
        for user in teachers:
            self.logger.info(user.__str__())

    """
    Метод передающий в консоль информацию о группе учителей
    """
    def sendOnConsoleUserGroup(self, teachers_group):
        self.logger.info(teachers_group.__str__())
