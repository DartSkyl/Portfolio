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


class RecordOut:
    @staticmethod
    def check_id(from_user_id: int):
        return _check_user_id(from_user_id)

    @staticmethod
    def last_request(from_user_id: int):
        return _get_last_request(from_user_id)


if __name__ == '__main__':
    print(RecordOut.check_id(10))
