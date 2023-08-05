from telebot.apihelper import ApiTelegramException
from loader import bot


def delete_message(chat_id: int, message_id: int, del_mess_count: int) -> None:
    message_id_list = [message_id - number for number in range(del_mess_count)]
    for index in message_id_list:
        try:
            bot.delete_message(chat_id=chat_id, message_id=index)
        except ApiTelegramException:
            break
