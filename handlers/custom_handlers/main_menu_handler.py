from telebot.types import Message
from loader import bot, api_url, api_headers
from states.user_states import make_request, UserState
from utils.site_api import main_api_func
from handlers.default_handlers.start import main_menu
from keyboards.inline.inline_keyboards import *
from database.record_func import RecordIn
from utils.misc.message_delet_func import delete_message

main_menu_commands = [
    'Choose the type of training',
    'Set the training level',
    'Choose a muscle group'
]

main_menu_dict = {
    'Choose the type of training': ('Choose the type of training:', type_setting_keyboard),
    'Set the training level': ('Choose a training level:', level_setting_keyboard),
    'Choose a muscle group': ('Choose a muscle group:', muscle_setting_keyboard),
}


def view_exercise(message, msg_id, user_req):
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
    delete_message(message.from_user.id, msg_id, 3)


@bot.message_handler(func=lambda message: message.text in main_menu_commands)
def training_setting(message: Message):
    mess = main_menu_dict[message.text][0]
    reply_markup = main_menu_dict[message.text][1]
    bot.send_message(message.from_user.id, text=mess, reply_markup=reply_markup())
    delete_message(message.from_user.id,  message.id, 3)


@bot.message_handler(func=lambda message: message.text == 'View exercises')
def view_exercise_handler(message: Message):
    user_req = make_request(message.from_user.id)
    view_exercise(message, message.id, user_req)
