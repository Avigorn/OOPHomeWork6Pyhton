from abc import ABC
from typing import Iterable

from small_data.StudentGroup import StudentGroup


class Stream(Iterable[StudentGroup], ABC):

    """
    Single Responsibility
    """

    def __init__(self, stream_name, stream_id=None):
        self.stream_name = stream_name
        self.__stream_id = stream_id
        self.__stream_id = []

    def getStreamName(self):
        """
        Метод получения названия потока
        """
        return self.stream_name

    def getStreamID(self):
        """
        Метод получения ID потока
        """
        return self.__stream_id

    def __str__(self):
        """
        Строчный метод для вывода названия и ID потока
        """
        return f"Stream {{stream_id='{self.__stream_id}', stream_name='{self.stream_name}}}"
