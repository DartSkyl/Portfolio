from database.model import UsersList, Requests, TrainingDiary, create_tables


def _user_registration(from_user_id: int, name: str) -> None:
    UsersList.create(from_user_id=from_user_id, user_name=name)


def _request_load(from_user_id: int, request: str, request_result: str) -> None:
    Requests.create(from_user_id=from_user_id, request=request, request_result=request_result)


def _make_a_record(from_user_id: int, diary_entry: str) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    TrainingDiary.create(user=user, journal_entry=diary_entry)


def _regist_user_choice(from_user_id: int, choice: str, set_index: int) -> None:
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    request = user.last_request.split('|')
    request[set_index] = choice
    request = '|'.join(request)
    user.last_request = request
    user.save()


def _registration_user_request(from_user_id: int):
    user = UsersList.get(UsersList.from_user_id == from_user_id)
    Requests.create(user=user, request=user.last_request)


class RecordIn:
    @staticmethod
    def regist_user(from_user_id: int, name: str):
        return _user_registration(from_user_id, name)

    @staticmethod
    def request_record(from_user_id: int, request: str, request_result: str):
        return _request_load(from_user_id, request, request_result)

    @staticmethod
    def diary_entry(from_user_id: int, diary_entry: str):
        return _make_a_record(from_user_id, diary_entry)

    @staticmethod
    def choice_regist(from_user_id: int, choice: str, set_index: int):
        return _regist_user_choice(from_user_id, choice, set_index)

    @staticmethod
    def regist_user_request(from_user_id: int):
        return _registration_user_request(from_user_id)


if __name__ == '__main__':
    create_tables()
    # UsersList.create(from_user_id=100, user_name='name')
    # Requests.create(user=UsersList.get(UsersList.user_name == 'Alina'), request='Hash')
    user = UsersList.get(UsersList.from_user_id == 100)
    print(user.last_request)
    Requests.create(user=user, request=user.last_request)
