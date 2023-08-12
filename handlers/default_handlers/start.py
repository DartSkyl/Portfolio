from telebot.types import Message, CallbackQuery
from typing import Union, List
from loader import bot
from keyboards.reply.reply_keyboards import main_markup
from database.record_func import RecordIn
from database.get_func import RecordOut
from utils.misc.message_delet_func import delete_message


def main_menu(message: Union[Message, CallbackQuery]) -> None:
    """
    Main menu function. Displays the current user settings and the
    number of entries in the diary
    :param message: A message with the "main menu" or a function message returning to the main menu
    :rtype message: Message
    """
    user_choice: List[str] = RecordOut.last_request(message.from_user.id)
    text_message: str = f'Type of training: {user_choice[0].title()}\n' \
                        f'Training level: {user_choice[1].title()}\n' \
                        f'Muscle group: {user_choice[2].title()}\n' \
                        f'Total entries in the diary: {RecordOut.entry_count(message.from_user.id)}'
    bot.send_message(message.from_user.id, text=text_message, reply_markup=main_markup)


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    """
    The bot launch function. If the user launches the bot for the first time,
    then registers it
    :param message: A message with the "start" command form the side menu or the "start" button at the very beginning
    :rtype message: Message
    """
    if RecordOut.check_id(message.from_user.id):
        text: str = f'Welcome back, {message.from_user.first_name}!'
        bot.send_message(message.from_user.id, text=text)
        main_menu(message)
    else:
        RecordIn.regist_user(from_user_id=message.from_user.id, name=message.from_user.first_name)
        text: str = f'Congratulations, you`re on the right track, {message.from_user.first_name}'
        bot.send_message(message.from_user.id, text=text)
        main_menu(message)


@bot.message_handler(commands=['main'])
def return_to_main_menu(message: Message):
    """Restarts the main menu and deletes the previous messages"""
    main_menu(message)
    delete_message(message.from_user.id, message.id, 100)
