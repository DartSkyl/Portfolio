from database.model import UsersList, Requests, TrainingDiary


def _check_user_id(from_user_id: int) -> bool:
    id_list = [user_id.from_user_id for user_id in UsersList.select()]
    if from_user_id in id_list:
        return True
    else:
        return False


def _get_last_request(from_user_id: int) -> list:
    request = UsersList.get(UsersList.from_user_id == from_user_id)
    return request.last_request.split('|')


def _get_last_10_notes(from_user_id: int, bot) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    user_notes = [note.journal_entry for note in user.records.order_by(-TrainingDiary.id).limit(10)]
    user_notes = user_notes[::-1]
    note_number = RecordOut.entry_count(from_user_id) - 10
    for i_note in range(len(user_notes)):
        note_number += 1
        msg = 'Entry number ' + str(note_number) + '\n' + user_notes[i_note]
        bot.send_message(from_user_id, text=msg)


def _get_range_entry(from_user_id: int, user_range: list, bot) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    user_notes = [note.journal_entry for note in user.records.order_by(TrainingDiary.id)]
    note_number = user_range[0]
    user_notes = user_notes[user_range[0] - 1: user_range[1]]
    for i_note in range(len(user_notes)):
        msg = 'Entry number ' + str(note_number) + '\n' + user_notes[i_note]
        note_number += 1
        bot.send_message(from_user_id, text=msg)
    else:
        msg = 'Check the correctness of the range!'
        bot.send_message(from_user_id, text=msg)


def _get_entry_count(from_user_id: int) -> int:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    user_notes = [note.journal_entry for note in user.records.order_by(TrainingDiary.id)]
    return len(user_notes)


def _get_an_entry_by_number(from_user_id: int, entry_number: int, bot) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    user_notes = [note.journal_entry for note in user.records.order_by(TrainingDiary.id)]
    requested_record = user_notes[entry_number - 1]
    msg = 'Entry number ' + str(entry_number) + '\n' + requested_record
    bot.send_message(from_user_id, text=msg)


def _get_last_ten_requests(from_user_id: int, bot) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    user_requests = [req.request + '\n' + str(req.created_at).split('.')[0]
                     for req in user.requests.order_by(-Requests.id).limit(10)]
    mess = '\n'.join(user_requests)
    bot.send_message(from_user_id, text=mess)


class RecordOut:
    @staticmethod
    def check_id(from_user_id: int) -> bool:
        return _check_user_id(from_user_id)

    @staticmethod
    def last_request(from_user_id: int) -> list:
        return _get_last_request(from_user_id)

    @staticmethod
    def print_last_ten_entry(from_user_id: int, bot) -> None:
        return _get_last_10_notes(from_user_id, bot)

    @staticmethod
    def range_entry(from_user_id: int, user_range: list, bot) -> None:
        return _get_range_entry(from_user_id, user_range, bot)

    @staticmethod
    def entry_count(from_user_id: int) -> int:
        return _get_entry_count(from_user_id)

    @staticmethod
    def entry_by_number(from_user_id: int, entry_number: int, bot) -> None:
        return _get_an_entry_by_number(from_user_id, entry_number, bot)

    @staticmethod
    def last_ten_requests(from_user_id: int, bot) -> None:
        return _get_last_ten_requests(from_user_id, bot)


if __name__ == '__main__':
    print(RecordOut.check_id(10))
