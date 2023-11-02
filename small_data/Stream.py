from abc import ABC
from typing import Iterable

from small_data.StudentGroup import StudentGroup


class Stream(Iterable[StudentGroup], ABC):

    __stream_id = []

    def __init__(self, stream_name, stream_id=None):
        self.stream_name = stream_name
        self.__stream_id = stream_id

    """
    Метод получения названия потока
    """
    def getStreamName(self):
        return self.stream_name

    """
    Метод получения ID потока
    """
    def getStreamID(self):
        return self.__stream_id

    """
    Строчный метод для вывода названия и ID потока
    """
    def __str__(self):
        return f"Stream {{stream_id='{self.__stream_id}', stream_name='{self.stream_name}}}"

    """
    Метод сравнения ID студентов
    """
    def __lt__(self, other):
        return self.__stream_id.compare_to.other.__stream_id
