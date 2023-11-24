from typing import List

from small_data.User import User


class UserComparator(List[User]):

    """
    Open-Closed
    """

    @staticmethod
    def compare(object1, object2):
        result_of_comparing = object1.getSurname().compareTo(object2.getSurname())
        if result_of_comparing == 0:
            result_of_comparing = object1.getFirstName().compareTo(object2.getFirstName())
            if result_of_comparing == 0:
                return object1.getPatronymic().compareTo(object2.getPatronymic())
            else:
                return result_of_comparing
        else:
            return result_of_comparing
