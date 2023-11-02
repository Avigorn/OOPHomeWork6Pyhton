from typing import List

from small_data.User import User


class UserComparator(List[User]):

    def compare(self, object1, object2):
        resultOfComparing = object1.getSurname().compareTo(object2.getSurname())
        if resultOfComparing == 0:
            resultOfComparing = object1.getFirstName().compareTo(object2.getFirstName())
            if resultOfComparing == 0:
                return object1.getPatronymic().compareTo(object2.getPatronymic())
            else:
                return resultOfComparing
        else:
            return resultOfComparing