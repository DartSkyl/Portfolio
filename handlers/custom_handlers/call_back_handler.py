from loader import bot
from ..default_handlers.start import bot_start
from states.paremetrs_of_choice import setting_dict, types_settings, level_settings, muscle_group_settings


@bot.callback_query_handler(func=lambda call: call.data in types_settings.values())
def setting_choice(call):
    for type_name, value in types_settings.items():
        if call.data == value:
            setting_dict['type'] = type_name
    bot_start(call.message)


@bot.callback_query_handler(func=lambda call: call.data in level_settings.values())
def setting_choice(call):
    for type_name, value in level_settings.items():
        if call.data == value:
            setting_dict['level'] = type_name
    bot_start(call.message)


@bot.callback_query_handler(func=lambda call: call.data in muscle_group_settings.values())
def setting_choice(call):
    for type_name, value in muscle_group_settings.items():
        if call.data == value:
            setting_dict['muscle'] = type_name
    bot_start(call.message)
