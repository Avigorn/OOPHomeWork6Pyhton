from small_data.User import User


class Teacher(User):

    __teacher_id: int

    def __init__(self, first_name, surname, patronymic):
        super().__init__(first_name, surname, patronymic)

    """
    Метод получения ID преподавателя
    """
    def getTeacherId(self):
        return self.__teacher_id

    """
    ???
    """
    class TeacherComparator:
        @staticmethod
        def compare(o1, o2):
            return 0
