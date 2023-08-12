from typing import List
from database.model import UsersList, Requests, TrainingDiary


def _check_user_id(from_user_id: int) -> bool:
    """
    The function checks if there is such a user in the database
    :param from_user_id: User ID
    :return True: If such a user already exists in the database
    """
    # List of existing users id
    id_list: List[UsersList.from_user_id] = [user_id.from_user_id for user_id in UsersList.select()]
    if from_user_id in id_list:
        return True
    else:
        return False


def _get_last_request(from_user_id: int) -> list:
    """
    The function generates a list of parameters for the API of the site
    :param from_user_id: User ID
    :return user.last_request: The list is formed using the split() function
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User
    return _user.last_request.split('|')


def _get_last_10_notes(from_user_id: int, bot) -> None:
    """
    The function returns the last 10 entries in the diary
    :param from_user_id: User ID
    :param bot: TeleBot
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User

    # Last 10 user entries in revers order
    user_notes: List[TrainingDiary.journal_entry] = [note.journal_entry
                                                     for note in _user.records.order_by(-TrainingDiary.id).limit(10)]

    # Last 10 user entries are in the correct order
    user_notes: List[TrainingDiary.journal_entry] = user_notes[::-1]
    note_number: int = RecordOut.entry_count(from_user_id) - 10  # Number of the first entry in the list

    for i_note in range(len(user_notes)):  # Loop output all entries in turn
        note_number += 1
        msg: str = 'Entry number ' + str(note_number) + '\n' + user_notes[i_note]
        bot.send_message(from_user_id, text=msg)


def _get_range_entry(from_user_id: int, user_range: list, bot) -> None:
    """
    The function output recordings in a chat with th user for a given range
    :param from_user_id: User ID
    :param user_range: User-defined range
    :param bot: TeleBot
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User

    # List of all user records
    user_notes: List[TrainingDiary.journal_entry] = [note.journal_entry
                                                     for note in _user.records.order_by(TrainingDiary.id)]

    note_number: int = user_range[0]  # Record number from the beginning of the range

    # Ready list of range entries
    user_notes: List[TrainingDiary.journal_entry] = user_notes[user_range[0] - 1: user_range[1]]

    for i_note in range(len(user_notes)):  # Loop output all entries in turn
        msg: str = 'Entry number ' + str(note_number) + '\n' + user_notes[i_note]
        note_number += 1
        bot.send_message(from_user_id, text=msg)

    else:  # It will work if the range is larger than the actual number of records
        msg: str = 'Check the correctness of the range!'
        bot.send_message(from_user_id, text=msg)


def _get_entry_count(from_user_id: int) -> int:
    """
    Function Returns the total number of entries in the user`s diary
    :param from_user_id: User ID
    :return len(user_notes): int
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User

    # List of all user records
    user_notes: List[TrainingDiary.journal_entry] = [note.journal_entry
                                                     for note in _user.records.order_by(TrainingDiary.id)]
    return len(user_notes)


def _get_an_entry_by_number(from_user_id: int, entry_number: int, bot) -> None:
    """
    Function output an entry from the user`s diary by the specified number
    :param from_user_id: User ID
    :param entry_number: Entry number
    :param bot: TeleBot
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User

    # List of all user records
    user_notes: List[TrainingDiary.journal_entry] = [note.journal_entry
                                                     for note in _user.records.order_by(TrainingDiary.id)]

    # Requested record
    requested_record: TrainingDiary.journal_entry = user_notes[entry_number - 1]
    msg: str = 'Entry number ' + str(entry_number) + '\n' + requested_record
    bot.send_message(from_user_id, text=msg)


def _get_last_ten_requests(from_user_id: int, bot) -> None:
    """
    Function output the last 10 user requests
    :param from_user_id: User ID
    :param bot: TeleBot
    """
    _user: UsersList = UsersList.get(UsersList.from_user_id == from_user_id)  # User

    # List of 10 recent user requests                                            # split() cuts off fractions of seconds
    user_requests: List[Requests.request] = [req.request + '\n' + str(req.created_at).split('.')[0]
                                                   for req in _user.requests.order_by(-Requests.id).limit(10)]

    # List is converted into a string that is user-friendly
    mess: str = '\n'.join(user_requests)
    bot.send_message(from_user_id, text=mess)


class RecordOut:
    """Class is needed to implement the above functions in the form of class methods"""
    @staticmethod
    def check_id(from_user_id: int) -> bool:
        """Method returns "_check_user_id" function"""
        return _check_user_id(from_user_id)

    @staticmethod
    def last_request(from_user_id: int) -> list:
        """Method returns "_get_last_request" function"""
        return _get_last_request(from_user_id)

    @staticmethod
    def print_last_ten_entry(from_user_id: int, bot) -> None:
        """Method returns "_get_last_10_notes" function"""
        return _get_last_10_notes(from_user_id, bot)

    @staticmethod
    def range_entry(from_user_id: int, user_range: list, bot) -> None:
        """Method returns "_get_range_entry" function"""
        return _get_range_entry(from_user_id, user_range, bot)

    @staticmethod
    def entry_count(from_user_id: int) -> int:
        """Method returns "_get_entry_count" function"""
        return _get_entry_count(from_user_id)

    @staticmethod
    def entry_by_number(from_user_id: int, entry_number: int, bot) -> None:
        """Method returns "_get_an_entry_by_number" function"""
        return _get_an_entry_by_number(from_user_id, entry_number, bot)

    @staticmethod
    def last_ten_requests(from_user_id: int, bot) -> None:
        """Method returns "_get_last_ten_requests" function"""
        return _get_last_ten_requests(from_user_id, bot)
