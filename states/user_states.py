from telebot.handler_backends import State, StatesGroup
from database.get_func import RecordOut

types_settings = {
    'cardio': 0, 'olympic_weightlifting': 0,
    'plyometrics': 0, 'powerlifting': 0,
    'strength': 0, 'stretching': 0, 'strongman': 0
}

level_settings = {'beginner': 1, 'intermediate': 1, 'expert': 1}

muscle_group_settings = {
    'abdominals': 2, 'abductors': 2, 'adductors': 2, 'biceps': 2, 'calves': 2, 'chest': 2, 'forearms': 2,
    'hamstrings': 2, 'lats': 2, 'lower_back': 2, 'middle_back': 2, 'neck': 2, 'quadriceps': 2,
    'traps': 2, 'triceps': 2, 'glutes': 2
}


def make_request(from_user_id: int):
    request_dict = {}
    user_request = RecordOut.last_request(from_user_id)
    request_dict['type'] = user_request[0]
    request_dict['difficulty'] = user_request[1]
    request_dict['muscle'] = user_request[2]
    return request_dict


class UserState(StatesGroup):
    exercise = State()
