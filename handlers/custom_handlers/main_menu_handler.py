from typing import Dict, List, Tuple
from telebot.types import Message, ReplyKeyboardMarkup
from loader import bot, api_url, api_headers
from states.user_states import make_request, UserState
from utils.site_api import main_api_func
from handlers.default_handlers.start import main_menu
from keyboards.inline.inline_keyboards import *
from database.record_func import RecordIn
from utils.misc.message_delet_func import delete_message

# List of main menu command
main_menu_commands: List[str] = [
    'Choose the type of training',
    'Set the training level',
    'Choose a muscle group'
]

# Dictionary with keyboards for selecting training parameters
main_menu_dict: Dict[str, Tuple[str, ReplyKeyboardMarkup]] = {
    'Choose the type of training': ('Choose the type of training:', type_setting_keyboard()),
    'Set the training level': ('Choose a training level:', level_setting_keyboard()),
    'Choose a muscle group': ('Choose a muscle group:', muscle_setting_keyboard()),
}


def view_exercise(message: Message, msg_id: int, user_req: Dict) -> None:
    """
    Function first checks if all parameters are set and if so, it starts showing exercises
    :param message: It is necessary to remove the user`s ID from it
    :param msg_id: Identify the message from which the cleaning of the message will begin
    :param user_req: Dictionary with user training parameters
    """
    text_message: str = ''

    for key, value in user_req.items():  # Check if all parameters are set
        if value == 'None':
            if key == 'type':
                text_message += 'You need to choose the type of workout\n'
            elif key == 'difficulty':
                text_message += 'You need to choose the training level\n'
            elif key == 'muscle':
                text_message += 'You need to choose the a muscle group\n'

    # If the message is left empty, then you can request the API of the site
    if text_message == '':
        RecordIn.regist_user_request(message.from_user.id)  # Registering a user request
        # We create a user state, which would then save the result of the request to it
        bot.set_state(message.from_user.id, UserState.exercise)
        main_api_func(url=api_url,
                      headers=api_headers,
                      querystring=user_req,
                      bot=bot,
                      from_user_id=message.from_user.id)

    # Otherwise, we send the user a message in which it is written what
    # parameters are missing and send him to the main menu
    else:
        bot.send_message(message.from_user.id, text=text_message)
        main_menu(message)
    delete_message(message.from_user.id, msg_id, 3)  # And delete the message history


@bot.message_handler(func=lambda message: message.text in main_menu_commands)
def training_setting(message: Message) -> None:
    """
    Handler catches the main menu commands
    :param message: It is necessary to remove the user`s ID from it
    """
    mess: str = main_menu_dict[message.text][0]  # A message about which parameter to select
    reply_markup: ReplyKeyboardMarkup = main_menu_dict[message.text][1]  # Keyboard with appropriate selection
    bot.send_message(message.from_user.id, text=mess, reply_markup=reply_markup)
    delete_message(message.from_user.id,  message.id, 3)


@bot.message_handler(func=lambda message: message.text == 'View exercises')
def view_exercise_handler(message: Message) -> None:
    """
    Handler for launching the exercise display
    :param message: It is necessary to remove the user`s ID from it
    """
    user_req: Dict[str: str] = make_request(message.from_user.id)
    view_exercise(message, message.id, user_req)  # Function of starting the display of exercises
