from telebot.apihelper import ApiTelegramException
from loader import bot


def delete_message(chat_id: int, message_id_list: list) -> None:
    for index in message_id_list:
        try:
            bot.delete_message(chat_id=chat_id, message_id=index)
        except ApiTelegramException:
            pass
