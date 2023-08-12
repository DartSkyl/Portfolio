from typing import Dict
from telebot.types import CallbackQuery
from loader import bot
from ..default_handlers.start import main_menu
from states.user_states import types_settings, level_settings, muscle_group_settings
from database.record_func import RecordIn
from handlers.custom_handlers.main_menu_handler import delete_message

# Dictionary will contain all possible parameters as a key and an index as a value.
# This is necessary for interaction with the database and a more convenient
# implementation of the handler described below
setting_index_dict: Dict[str, int] = dict()
for elem in [types_settings, level_settings, muscle_group_settings]:
    setting_index_dict.update(elem)


@bot.callback_query_handler(func=lambda call: call.data in types_settings or level_settings or muscle_group_settings)
def setting_choice(call: CallbackQuery) -> None:
    """
    Handler catches the user`s choice and saves it to the database
    :param call: A message with a callback_data containing the user`s choice
    """
    RecordIn.choice_regist(
        from_user_id=call.from_user.id,
        choice=call.data,
        set_index=setting_index_dict[call.data]
    )
    main_menu(call)  # After making a choice, return the user to the main menu
    delete_message(call.from_user.id, call.message.id, 3)  # and cleans the message history
