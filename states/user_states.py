from telebot.handler_backends import State, StatesGroup
from database.get_func import RecordOut

types_settings = {'cardio', 'olympic_weightlifting',
                  'plyometrics', 'powerlifting',
                  'strength', 'stretching', 'strongman'}

level_settings = {'beginner', 'intermediate', 'expert'}

muscle_group_settings = {'abdominals', 'abductors', 'adductors', 'biceps', 'calves', 'chest', 'forearms', 'glutes',
                         'hamstrings', 'lats', 'lower_back', 'middle_back', 'neck', 'quadriceps',
                         'traps', 'triceps'}


def make_request(from_user_id: int):
    request_dict = {}
    user_request = RecordOut.last_request(from_user_id)
    request_dict['type'] = user_request[0]
    request_dict['difficulty'] = user_request[1]
    request_dict['muscle'] = user_request[2]
    return request_dict


class UserState(StatesGroup):
    diary_entry = State()
    #     name = State()
    #     type = State()
    #     level = State()
    #     muscle = State()
    exercise = State()
