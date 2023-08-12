from typing import List, Dict
from telebot.handler_backends import State, StatesGroup
from database.get_func import RecordOut

types_settings: Dict[str, int] = {  # Dictionary with workout types
    'cardio': 0, 'olympic_weightlifting': 0,
    'plyometrics': 0, 'powerlifting': 0,
    'strength': 0, 'stretching': 0, 'strongman': 0
}

level_settings: Dict[str, int] = {'beginner': 1, 'intermediate': 1, 'expert': 1}  # Dictionary with training levels

muscle_group_settings: Dict[str, int] = {  # Dictionary with muscle groups
    'abdominals': 2, 'abductors': 2, 'adductors': 2, 'biceps': 2, 'calves': 2, 'chest': 2, 'forearms': 2,
    'hamstrings': 2, 'lats': 2, 'lower_back': 2, 'middle_back': 2, 'neck': 2, 'quadriceps': 2,
    'traps': 2, 'triceps': 2, 'glutes': 2
}


def make_request(from_user_id: int) -> Dict[str, str]:
    """
    Function Generates a dictionary with the parameters selected by the user to request the API of the site
    :param from_user_id: User ID
    :return request_dict: Dictionary with parameters
    """
    request_dict: Dict[str, str] = dict()
    user_request: List[str] = RecordOut.last_request(from_user_id)
    request_dict['type'] = user_request[0]
    request_dict['difficulty'] = user_request[1]
    request_dict['muscle'] = user_request[2]
    return request_dict


class UserState(StatesGroup):
    """A class with a single user state for saving a list of exercises
    at the user`s request and subsequent demonstration"""
    exercise: State = State()
