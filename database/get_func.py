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
    users_notes = [note.journal_entry for note in user.records.order_by(TrainingDiary.id).limit(10)]
    for i_note in range(len(users_notes)):
        msg = 'Entry number ' + str(i_note + 1) + '\n' + users_notes[i_note]
        bot.send_message(from_user_id, text=msg)





class RecordOut:
    @staticmethod
    def check_id(from_user_id: int):
        return _check_user_id(from_user_id)

    @staticmethod
    def last_request(from_user_id: int):
        return _get_last_request(from_user_id)

    @staticmethod
    def print_last_ten_entry(from_user_id: int, bot):
        return _get_last_10_notes(from_user_id, bot)


if __name__ == '__main__':
    print(RecordOut.check_id(10))
