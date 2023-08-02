from telebot.types import Message
from loader import bot, api_url, api_headers
from states.user_states import make_request, UserState
from utils.site_api import main_api_func
from handlers.default_handlers.start import main_menu
from keyboards.inline.inline_keybords import *
from database.record_func import RecordIn


main_menu_commands = ['Choose the type of training', 'Set the training level',
                      'Choose a muscle group', 'View exercises']


def delete_message(chat_id: int, message_id_list: list) -> None:
    for index in message_id_list:
        try:
            bot.delete_message(chat_id=chat_id, message_id=index)
        except BaseException:
            pass


def view_exercise(message, msg_id):
    user_req = make_request(message.from_user.id)
    text_message = ''
    for key, value in user_req.items():
        if value == 'None':
            if key == 'type':
                text_message += 'You need to choose the type of workout\n'
            elif key == 'difficulty':
                text_message += 'You need to choose the training level\n'
            elif key == 'muscle':
                text_message += 'You need to choose the a muscle group\n'
    if text_message == '':
        RecordIn.regist_user_request(message.from_user.id)
        bot.set_state(message.from_user.id, UserState.exercise)
        main_api_func(url=api_url,
                      headers=api_headers,
                      querystring=user_req,
                      bot=bot,
                      from_user_id=message.from_user.id)
    else:
        bot.send_message(message.from_user.id, text=text_message)
        main_menu(message)
    delete_message(message.from_user.id, [msg_id - 1, msg_id - 2, msg_id - 3])


@bot.message_handler(func=lambda message: message.text in main_menu_commands)
def training_setting(message: Message):
    msg_id = message.id
    if message.text == 'Choose the type of training':
        bot.send_message(message.from_user.id, f'Choose the type of training:\n',
                         reply_markup=type_setting_keyboard())
        delete_message(message.from_user.id, [msg_id - 1, msg_id - 2, msg_id - 3])
    elif message.text == 'Set the training level':
        bot.send_message(message.from_user.id, 'Choose a training level:',
                         reply_markup=level_setting_keyboard())
        delete_message(message.from_user.id, [msg_id - 1, msg_id - 2, msg_id - 3])
    elif message.text == 'Choose a muscle group':
        bot.send_message(message.from_user.id, 'Choose a muscle group:',
                         reply_markup=muscle_setting_keyboard())
        delete_message(message.from_user.id, [msg_id - 1, msg_id - 2, msg_id - 3])
    elif message.text == 'View exercises':
        view_exercise(message, msg_id)
