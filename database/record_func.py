from typing import List
from database.model import UsersList, Requests, TrainingDiary


def _user_registration(from_user_id: int, name: str) -> None:
    """
    Function registers new users
    :param from_user_id: User ID
    :param name: First name
    """
    UsersList.create(from_user_id=from_user_id, user_name=name)


def _make_a_record(from_user_id: int, diary_entry: str) -> None:
    """
    Function saves the user`s entry in the diary
    :param from_user_id: User ID
    :param diary_entry: User entry
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User
    TrainingDiary.create(user=_user, journal_entry=diary_entry)


def _regist_user_choice(from_user_id: int, choice: str, set_index: int) -> None:
    """
    Function saves the training parameters selected by the user
    :param from_user_id: User ID
    :param choice: Parameter selected by the user
    :param set_index: Index of the selected parameter. 0 - type, 1 - level, 2 - muscle group
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User
    # Since the training parameters are stored as a string, first we convert it into a list
    request: List[str] = _user.last_request.split('|')
    request[set_index]: str = choice  # Then we assign the change to the parameter with the corresponding index
    request: str = '|'.join(request)  # Re-add to the list
    _user.last_request = request  # And save
    _user.save()


def _registration_user_request(from_user_id: int):
    """
    Function registers users requests
    :param from_user_id: User ID
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User
    Requests.create(user=_user, request=_user.last_request)


class RecordIn:
    """Class is needed to implement the above functions in the form of class methods"""
    @staticmethod
    def regist_user(from_user_id: int, name: str):
        """Method returns "_user_registration" function"""
        return _user_registration(from_user_id, name)

    @staticmethod
    def diary_entry(from_user_id: int, diary_entry: str):
        """Method returns "_make_a_record" function"""
        return _make_a_record(from_user_id, diary_entry)

    @staticmethod
    def choice_regist(from_user_id: int, choice: str, set_index: int):
        """Method returns "_regist_user_choice" function"""
        return _regist_user_choice(from_user_id, choice, set_index)

    @staticmethod
    def regist_user_request(from_user_id: int):
        """Method returns "_registration_user_request" function"""
        return _registration_user_request(from_user_id)
