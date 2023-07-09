from telebot.types import Message
from loader import bot
from keyboards.reply.reply_keyboards import markup
from states.paremetrs_of_choice import setting_dict


@bot.message_handler(commands=["start"])
def bot_start(message: Message):
    bot.send_message(message.chat.id,
                                      f"Выбранный тип тренировок: {setting_dict.get('type')}\n"
                                      f"Выбранный уровень тренировок: {setting_dict.get('level')}\n"
                                      f"Последняя группа мышц: (группа мышц)\n"
                                      f"Кол-во записей в дневнике: (кол-во записей)",
                     reply_markup=markup)
