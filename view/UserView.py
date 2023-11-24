import logging
from typing import List

from small_data.User import User


class UserView(List[User]):

    """
    Interface Segregation
    """
    def __init__(self):
        super().__init__()
        self.logger = logging.getLogger(UserView.__class__.__name__)
