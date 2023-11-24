import logging

from view.UserView import UserView


class TeacherView(UserView):

    """
    Переменная записывающая информацию об учителях
    """
    logger = logging.getLogger(__name__)

    def sendOnConsole(self, teachers):
        """
        Метод передающий в консоль информацию об учителях
        """
        for user in teachers:
            self.logger.info(user.__str__())

