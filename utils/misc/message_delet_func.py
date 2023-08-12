from typing import List
from telebot.apihelper import ApiTelegramException
from loader import bot


def delete_message(chat_id: int, message_id: int, del_mess_count: int) -> None:
    """
    Function deletes the specified messages
    :param chat_id: ID of the chat in which you want to delete messages
    :param message_id: ID of the message from which to start deleting
    :param del_mess_count: Total numbers of deleted messages
    """
    message_id_list: List[int] = [message_id - number for number in range(del_mess_count)]
    for index in message_id_list:
        try:  # Tries to delete messages fom the list
            bot.delete_message(chat_id=chat_id, message_id=index)
        except ApiTelegramException:  # If something goes wrong, it interrupts the cycle
            break
