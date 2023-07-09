from loader import bot
from ..default_handlers.start import bot_start
from states.paremetrs_of_choice import setting_dict





@bot.callback_query_handler(func=lambda call: True)
def setting_choice(call):
    if call.data == 'cardio':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Кардио')
        setting_dict['type'] = 'Кардио'
    elif call.data == 'olympic_weightlifting':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Олимпийский тяжёлоатлет')
        setting_dict['type'] = 'Олимпийский тяжёлоатлет'
    elif call.data == 'plyometrics':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Плиометрика')
        setting_dict['type'] = 'Плиометрика'
    elif call.data == 'powerlifting':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Пауэрлифтинг')
        setting_dict['type'] = 'Пайэрлифтинг'
    elif call.data == 'strength':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Силовая')
        setting_dict['type'] = 'Силовая'
    elif call.data == 'stretching':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Растяжка')
        setting_dict['type'] = 'Растяжка'
    elif call.data == 'strongman':
        bot.send_message(call.message.chat.id, text='Выбран тип тренировки: Силач')
        setting_dict['type'] = 'Силач'
    elif call.data == 'beginner':
        bot.send_message(call.message.chat.id, text='Установлен уровень тренировки: Начинающий')
        setting_dict['level'] = 'Начинающий'
    elif call.data == 'intermediate':
        bot.send_message(call.message.chat.id, text='Установлен уровень тренировки: Средний')
        setting_dict['level'] = 'Средний'
    elif call.data == 'expert':
        bot.send_message(call.message.chat.id, text='Установлен уровень тренировки: Эксперт')
        setting_dict['level'] = 'Эксперт'
    bot_start(call.message)
