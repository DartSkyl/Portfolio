from loader import bot
from ..default_handlers.start import main_menu
from states.user_states import types_settings, level_settings, muscle_group_settings
from database.record_func import RecordIn
from handlers.custom_handlers.main_menu_handler import delete_message


setting_index_dict = dict()
for elem in [types_settings, level_settings, muscle_group_settings]:
    setting_index_dict.update(elem)


@bot.callback_query_handler(func=lambda call: call.data in types_settings or level_settings or muscle_group_settings)
def setting_choice(call):
    msg_id = call.message.id
    RecordIn.choice_regist(
        from_user_id=call.from_user.id,
        choice=call.data,
        set_index=setting_index_dict[call.data]
    )
    delete_message(call.from_user.id, [msg_id, msg_id - 1])
    main_menu(call)
