from loader import bot
from ..default_handlers.start import main_menu
from states.user_states import types_settings, level_settings, muscle_group_settings
from database.record_func import RecordIn
from handlers.custom_handlers.main_menu_handler import delete_message


@bot.callback_query_handler(func=lambda call: call.data in types_settings)
def setting_choice(call):
    msg_id = call.message.id
    for value in types_settings:
        if call.data == value:
            RecordIn.choice_regist(
                from_user_id=call.from_user.id,
                choice=value,
                set_index=0
            )
    delete_message(call.from_user.id, [msg_id, msg_id - 1])
    main_menu(call)


@bot.callback_query_handler(func=lambda call: call.data in level_settings)
def setting_choice_2(call):
    msg_id = call.message.id
    for value in level_settings:
        if call.data == value:
            RecordIn.choice_regist(
                from_user_id=call.from_user.id,
                choice=value,
                set_index=1
            )
    delete_message(call.from_user.id, [msg_id, msg_id - 1])
    main_menu(call)


@bot.callback_query_handler(func=lambda call: call.data in muscle_group_settings)
def setting_choice_3(call):
    msg_id = call.message.id
    for value in muscle_group_settings:
        if call.data == value:
            RecordIn.choice_regist(
                from_user_id=call.from_user.id,
                choice=value,
                set_index=2
            )
    delete_message(call.from_user.id, [msg_id, msg_id - 1])
    main_menu(call)
